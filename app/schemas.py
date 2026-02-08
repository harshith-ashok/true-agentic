from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class EventCreate(BaseModel):
    content: str


class IdeaOut(BaseModel):
    content: str
    idea_type: str
    confidence: float


class EventResponse(BaseModel):
    event_id: str
    ideas: List[IdeaOut]
