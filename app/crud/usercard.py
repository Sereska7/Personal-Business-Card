from typing import Dict

from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy import select, update, delete

from app.core.models import UserCard
from app.core.models.db_helper import db_helper as db
from app.core.schemas.user_card import CardCreate, CardRead, CardUpdate


async def create_user_card(
        card_create: CardCreate,
        user_id: int,
        email: EmailStr
) -> CardRead:
    if len(card_create.phone) == 11:
        if card_create.phone.isdigit():
            async with db.session_factory() as session:
                user_card = UserCard(
                    name=card_create.name,
                    email=email,
                    phone=card_create.phone,
                    company=card_create.company,
                    position=card_create.position,
                    date_reg=card_create.date_reg,
                    user_id=user_id
                )
                session.add(user_card)
                await session.commit()
                await session.refresh(user_card)
                return user_card
        else:
            raise HTTPException(status_code=500)
    else:
        raise HTTPException(status_code=500)


async def get_cards() -> list[CardRead]:
    async with db.session_factory() as session:
        query = select(UserCard.__table__.columns)
        cards = await session.execute(query)
        return cards.mappings().all()


async def get_card_by_user_id(user_id: int) -> CardRead:
    async with db.session_factory() as session:
        query = select(UserCard).where(UserCard.user_id == user_id)
        cards = await session.execute(query)
        return cards.scalar()


async def update_card(
        email: EmailStr,
        card_update: CardUpdate,
) -> Dict:
    if len(card_update.phone) == 11:
        if card_update.phone.isdigit():
            async with db.session_factory() as session:
                query = (
                    update(UserCard)
                    .where(UserCard.email == email)
                    .values(
                        name=card_update.name,
                        email=email,
                        phone=card_update.phone,
                        company=card_update.company,
                        position=card_update.position,
                    )
                    .execution_options(synchronize_session="fetch")
                )
                up_card = await session.execute(query)
                await session.commit()
                return up_card.mappings().one_or_none()
        else:
            raise HTTPException(status_code=500)
    else:
        raise HTTPException(status_code=500)


async def delete_card(email: EmailStr):
    async with db.session_factory() as session:
        await session.execute(delete(UserCard).where(UserCard.email == email))
        await session.commit()
