from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base_model import Base

if TYPE_CHECKING:
    from .user_card import UserCard


class User(Base):
    email: Mapped[str]
    password: Mapped[str]

    user_card: Mapped["UserCard"] = relationship(back_populates="user")

