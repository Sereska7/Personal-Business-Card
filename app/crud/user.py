from sqlalchemy import select

from app.core.models import User
from app.core.models.db_helper import db_helper as db
from app.core.schemas.user import UserCreate, UserRead
from app.utils.utils_func import get_password_hash


async def user_register(user_reg: UserCreate) -> UserRead:
    async with db.session_factory() as session:
        new_user = User(
            email=user_reg.email,
            password=get_password_hash(user_reg.password)
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


async def get_user(email: str) -> UserRead:
    async with db.session_factory() as session:
        request = select(User.__table__.columns).where(User.email == email)
        user = await session.execute(request)
        return user.mappings().one_or_none()


async def get_user_by_id(user_id: int):
    async with db.session_factory() as session:
        request = select(User.__table__.columns).where(User.id == user_id)
        user = await session.execute(request)
        return user.mappings().one_or_none()
