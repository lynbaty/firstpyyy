from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Field


class User(BaseModel):
    name: str | None
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool
    password: str


class UserCreate(User):
    password: str

