from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import EventCreate, EventResponse
from app.models import Event, Idea
from app.db import get_db
from app.llm import extract_ideas
from app.llm_client import llm_client  # your OpenAI client

router = APIRouter(prefix="/events", tags=["events"])


@router.post("/", response_model=EventResponse)
async def ingest_event(
    payload: EventCreate,
    db: Session = Depends(get_db)
):
    # 1. Store raw event
    event = Event(content=payload.content)
    db.add(event)
    db.commit()
    db.refresh(event)

    # 2. Extract ideas
    ideas_data = await extract_ideas(llm_client, payload.content)

    ideas = []
    for idea in ideas_data:
        idea_obj = Idea(
            event_id=event.id,
            content=idea["content"],
            idea_type=idea["idea_type"],
            confidence=idea["confidence"],
        )
        db.add(idea_obj)
        ideas.append(idea_obj)

    db.commit()

    return {
        "event_id": event.id,
        "ideas": ideas
    }
