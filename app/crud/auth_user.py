from fastapi import HTTPException, Depends, Request
from jose import jwt, ExpiredSignatureError, JWTError
from pydantic import EmailStr

from app.core import settings
from app.crud.user import get_user, get_user_by_id
from app.utils.utils_func import verify_password


async def authenticate_user(email: EmailStr, password: str):
    user = await get_user(email=email)
    if not (user and verify_password(password, user.password)):
        raise HTTPException(status_code=500)
    return user


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=500)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=500)
    except JWTError:
        raise HTTPException(status_code=500)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=500)
    user = await get_user_by_id(user_id=int(user_id))
    if not user:
        raise HTTPException(status_code=500)

    return user
