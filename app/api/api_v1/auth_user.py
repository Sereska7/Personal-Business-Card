from fastapi import APIRouter, Response, Depends
from fastapi import HTTPException

from app.core.schemas.user import UserCreate, UserRead
from app.crud.auth_user import authenticate_user
from app.crud.user import get_user, user_register
from app.utils.utils_func import verify_password, create_access_token

router = APIRouter(tags=["Auth"])


@router.post("/register_user")
async def register_user(user_reg: UserCreate) -> UserRead:
    user = await get_user(user_reg.email)
    if user:
        raise HTTPException(status_code=500)
    else:
        return await user_register(user_reg)


@router.post("/login_user")
async def logining_user(user_lig: UserCreate, response: Response):
    user = await authenticate_user(user_lig.email, user_lig.password)
    if not user:
        raise HTTPException(status_code=401)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/log_out")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
    return {"access": "True"}
