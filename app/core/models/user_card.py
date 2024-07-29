from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base_model import Base

if TYPE_CHECKING:
    from .user import User


class UserCard(Base):

    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(60))
    phone: Mapped[str] = mapped_column(String(15))
    company: Mapped[str] = mapped_column(String(100))
    position: Mapped[str] = mapped_column(String(60))
    date_reg: Mapped[date] = mapped_column(Date)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    user: Mapped["User"] = relationship(back_populates="user_card")
