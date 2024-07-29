from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr

from app.core.schemas import CardCreate, UserRead, CardUpdate, CardRead
from app.crud.auth_user import get_current_user
from app.crud.usercard import create_user_card, get_cards, get_card_by_user_id, update_card, delete_card

router = APIRouter(tags=["UserCard"])


@router.post("/create_card")
async def user_card_create(
        user_create: CardCreate,
        user: UserRead = Depends(get_current_user)
) -> CardRead:
    if user:
        card_user = await get_card_by_user_id(user.id)
        if not card_user:
            create_card = await create_user_card(
                card_create=user_create,
                user_id=user.id,
                email=user.email
            )
            return create_card
        else:
            raise HTTPException(status_code=500)
    else:
        raise HTTPException(status_code=500)


@router.get("/me_card")
async def get_user_card(
        user: UserRead = Depends(get_current_user)
) -> CardRead:
    user_card = await get_card_by_user_id(user.id)
    if user_card:
        return user_card
    else:
        raise HTTPException(status_code=500)


@router.get("/get_cards")
async def get_user_cards() -> List[CardRead]:
    cards = await get_cards()
    return cards


@router.patch("/update_card{email}")
async def update_user_card(
        email: EmailStr,
        card_update: CardUpdate,
        user: UserRead = Depends(get_current_user)
):
    card = await get_card_by_user_id(user.id)
    if card:
        new_card = await update_card(
            email,
            card_update
        )
        return new_card
    else:
        raise HTTPException(status_code=500)


@router.delete("/delete_card/{email}")
async def delete_card_user(
        email: EmailStr,
        user: UserRead = Depends(get_current_user)
):
    card = await get_card_by_user_id(user.id)
    if card:
        await delete_card(email)
        return {"process": True}
    else:
        raise HTTPException(status_code=500)

