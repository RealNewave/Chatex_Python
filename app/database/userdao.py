from sqlalchemy.orm import Session
from . import database
from .. import models


def create_user(db: Session, user: models.User):
    created_user = database.User(username=user.username, password=user.password)
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user.id


def get_user(db: Session, user_id: int):
    return db.get(database.User, user_id)
