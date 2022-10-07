import sqlite3
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime, create_engine, Table, Boolean, func

con = sqlite3.connect("chat.db")
database_url = "sqlite:///chat.db"
engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    last_online = Column(DateTime(True), onupdate=func.now())
    created = Column(DateTime(True), server_default=func.now())
    username = Column(Text, unique=True)
    # add encryption
    password = Column(Text)
    threads = relationship("Thread")
    messages = relationship("Message")


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("user.id"))
    message = Column(Text)
    visible_to_strangers = Column(Boolean)
    timestamp = Column(DateTime(True), server_default=func.now())


thread_users = Table(
    "thread_users",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("thread_id", ForeignKey("thread.id"))
)

thread_replies = Table(
    "thread_replies",
    Base.metadata,
    Column("message_id", ForeignKey("message.id")),
    Column("thread_id", ForeignKey("thread.id"))
)


class Thread(Base):
    __tablename__ = "thread"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("user.id"))
    message = Column(Text, ForeignKey("message.id"))
    receivers = relationship("User", secondary=thread_users)
    replies = relationship("Message", secondary=thread_replies)
    timestamp = Column(DateTime(True), server_default=func.now())
