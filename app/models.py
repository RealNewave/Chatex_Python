from datetime import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    username: str
    password: str
    # last_online: datetime

    class Config:
        orm_mode = True


class Message(BaseModel):
    sender_id: int
    message: str
    # timestamp: datetime


class ReplyMessage(Message):
    visible_to_strangers: bool = False

    class Config:
        orm_mode = True


class StartThread(Message):
    receivers: list[int]


class Thread(Message):
    receivers: list[User] = []
    replies: list[ReplyMessage] = []

    class Config:
        orm_mode = True


class EditMessage(Message):
    class Config:
        orm_mode = True
