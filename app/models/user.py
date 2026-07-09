from sqlalchemy import Integer

from app.models.api_key import ApiKey

from app.config.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import func
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    api_keys: Mapped["ApiKey"] = relationship(back_populates="user")
