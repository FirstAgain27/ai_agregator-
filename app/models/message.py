from app.config.database import Base
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional
from sqlalchemy.sql import func
from datetime import datetime


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    role: Mapped[str] = mapped_column(String(20))
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversation.id"))
    content: Mapped[str] = mapped_column(Text) 
    tokens_used: Mapped[Optional[int]] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")