from sqlalchemy import Column, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from db import Base


def gen_id():
    return str(uuid.uuid4())


class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, default=gen_id)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    ideas = relationship("Idea", back_populates="event")


class Idea(Base):
    __tablename__ = "ideas"

    id = Column(String, primary_key=True, default=gen_id)
    event_id = Column(String, ForeignKey("events.id"), nullable=False)

    content = Column(Text, nullable=False)
    idea_type = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    event = relationship("Event", back_populates="ideas")
