from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from typing_extensions import Generator

from database import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
