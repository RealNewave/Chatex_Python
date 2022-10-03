from .models import Thread
from .models import ReplyMessage
from .models import EditMessage


# from .models import User


threads = {}
message_id = 1


class MessageService:

    # def get_message_by_id(message_id: int):
    #     for message in threads:
    #         if message.message_id == message_id:
    #             return message

    def start_thread(thread: Thread):
        global message_id
        threads[message_id] = thread
        yield message_id
        message_id += 1

    def get_threads():
        return list(threads.values())

    def get_thread(thread_id: int):
        return threads[thread_id]

    def reply_to_thread(thread_id: int, message: ReplyMessage):
        thread: Thread = threads.get(thread_id)
        thread.replies.append(message)
        threads.update({thread_id: thread})

    # def get_new_messages(user_id: int):
    #     current_user: User = next(
    #         filter(
    #             lambda user: user.user_id == user_id, users
    #         )
    #     )
    #     new_messages = filter(
    #         lambda message: message.timestamp > current_user.last_online, threads
    #     )
    #     # probably still have to save this back to the list but whatever for now
    #     for new_message in new_messages:
    #         new_message.received = True
    #     return new_messages

    def edit_message(message: EditMessage):
        pass
