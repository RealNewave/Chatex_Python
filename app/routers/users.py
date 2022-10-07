from fastapi import APIRouter, Depends

from .. import models
from ..database import userdao, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users"
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}", response_model=models.User, response_model_exclude={"password"})
async def get_thread(user_id: int, db: Session = Depends(get_db)):
    return userdao.get_user(db, user_id)


@router.post("/create")
async def create_user(user: models.User, db: Session = Depends(get_db)):
    return userdao.create_user(db, user)

