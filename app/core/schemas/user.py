from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseUser):
    pass


class UserRead(BaseUser):
    id: int


class UserUpdate(BaseUser):
    pass
