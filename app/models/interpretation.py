from sqlalchemy import DateTime, ForeignKey, String, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import uuid
from datetime import datetime
from app.database.base import Base


class Interpretation(Base):
    __tablename__ = "interpretations"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("events.id"))
    model_name: Mapped[str] = mapped_column(String)
    output: Mapped[dict] = mapped_column(JSONB)
    confidence: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
