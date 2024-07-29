from datetime import date

from pydantic import BaseModel, EmailStr


class CardRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    company: str
    position: str
    user_id: int
    date_reg: date


class CardCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = "80000000000"
    company: str
    position: str
    date_reg: date


class CardUpdate(BaseModel):
    name: str
    phone: str = "80000000000"
    company: str
    position: str
