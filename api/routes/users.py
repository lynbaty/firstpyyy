from typing import Any

from fastapi import APIRouter, HTTPException

import crud
from api.deps import SessionDep
from models import UserCreate

router = APIRouter()


@router.get("")
def get_users() -> Any:
    return {"message": "Hello World"}


@router.post("")
def get_users(*, session: SessionDep, user: UserCreate) -> Any:
    existing_user = crud.get_user_by_email(session, user.email)
    if existing_user is None:
        raise HTTPException(
            status_code=400,
            detail="Not found",
        )

    user_dto = crud.create_user(session, user)
    return user_dto
