from sqlalchemy.orm import Session
from . import database
from .. import models


def start_thread(db: Session, thread: models.StartThread):
    users = db.query(database.User).filter(database.User.id in thread.receivers).all()
    new_thread = database.Thread(sender_id=thread.sender_id, message=thread.message, receivers=users, replies=[])
    db.add(new_thread)
    db.commit()
    db.refresh(new_thread)
    return new_thread.id


def get_threads(db: Session):
    return db.query(database.Thread).all()


def get_thread(db: Session, thread_id: int):
    return db.get(database.Thread, thread_id)


def reply_to_thread(db: Session, thread_id: int, reply: models.ReplyMessage):
    thread = db.get(database.Thread, thread_id)
    new_reply = database.Message(sender_id=reply.sender_id, message=reply.message, visible_to_strangers=reply.visible_to_strangers)
    thread.replies.append(new_reply)
    db.add(thread)
    db.commit()
