from sqlalchemy import DateTime, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import uuid
from datetime import datetime
from app.database.base import Base


class Memory(Base):
    __tablename__ = "memory"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    memory_type: Mapped[str] = mapped_column(String, index=True)
    key: Mapped[str] = mapped_column(String, index=True)
    value: Mapped[dict] = mapped_column(JSONB)
    strength: Mapped[float] = mapped_column(Float, default=0.0)
    last_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
