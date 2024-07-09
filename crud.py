from sqlmodel import Session

import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: models.UserCreate):
    password = user.password + "Fake"
    db_user = models.User(email=user.email, password=password, name=user.name, is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
