from fastapi import FastAPI
from .services import MessageService as messageService
from .models import Thread
from .models import ReplyMessage

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#
# @app.get("/messages/{message_id}")
# async def get_message_by_id(message_id: int):
#     return messageService.get_message_by_id(message_id)


@app.get("/threads")
async def get_threads():
    return messageService.get_threads()


@app.get("/threads/{thread_id}")
async def get_thread():
    return messageService.get_threads()


@app.post("/threads/start")
async def start_thread(thread: Thread):
    return messageService.start_thread(thread)


@app.post("/threads/reply/{thread_id}")
async def reply_to_thread(thread_id: int, message: ReplyMessage):
    messageService.reply_to_thread(thread_id, message)
