from pydantic import BaseModel, EmailStr
from sqlmodel import Field


class User(BaseModel):
    name: str | None
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool


class UserCreate(User):
    password: str

