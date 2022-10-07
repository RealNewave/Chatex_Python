from fastapi import APIRouter, Depends

from .. import models
from ..database import threaddao, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/threads"
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[models.Thread])
async def get_threads(db: Session = Depends(get_db)):
    return threaddao.get_threads(db)


@router.get("/{thread_id}", response_model=models.Thread)
async def get_thread(thread_id: int, db: Session = Depends(get_db)):
    return threaddao.get_thread(db, thread_id)


@router.post("/start")
async def start_thread(thread: models.StartThread, db: Session = Depends(get_db)):
    return threaddao.start_thread(db, thread)


@router.post("/reply/{thread_id}")
async def reply_to_thread(thread_id: int, message: models.ReplyMessage, db: Session = Depends(get_db)):
    threaddao.reply_to_thread(db, thread_id, message)
