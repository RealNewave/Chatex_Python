from _datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    password: str
    last_online: datetime
    threads = {}


class Thread(BaseModel):
    sender_id: int
    message: str
    receivers = []
    replies = []
    # sender_visibility: bool
    timestamp = datetime.now()


class ReplyMessage(BaseModel):
    sender_id: int
    message: str
    timestamp = datetime.now()


class EditMessage(BaseModel):
    message_id: int
    message: str
    timestamp_edited = datetime.now()
