from fastapi import FastAPI

from .database.database import Base, engine
from .routers import threads, users

Base.metadata.create_all(bind=engine, checkfirst=True)


app = FastAPI()
app.include_router(threads.router)
app.include_router(users.router)
