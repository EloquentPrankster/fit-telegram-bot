from datetime import datetime
import logging
import random
from peewee import PostgresqlDatabase
from config import CHAT_ID
# all functions must have in their parameters bot and db_manager


async def set_chat_description(bot, db_manager: PostgresqlDatabase):
    list_of_descriptions = db_manager.get_descriptions()
    phrase = ""
    length = len(list_of_descriptions)
    if length != 0:
        formatted_list = [i.description for i in list_of_descriptions]
        phrase = str(formatted_list[random.randint(0, length-1)])
    time = datetime.now()
    title = f"Время: {time.date()} {time.hour}:{f'0{time.minute}' if time.minute<10 else time.minute}\n{phrase}"

    try:
        await bot.bot.set_chat_description(CHAT_ID, title)
        logging.info(f"Chat description updated: {title}")
    except Exception as ex:
        logging.error(f"Failed to update chat title: {ex}")


async def get_messages_from_vk(bot, db_manager: PostgresqlDatabase):
    try:
        await bot.vk_manager.get_messages()
        logging.info('get_messages_from_vk: task completed')
    except Exception as ex:
        logging.error(f"Failed to read messages: {ex}")

list_of_tasks = [
    {"func": set_chat_description, "time": 60, },
    {"func": get_messages_from_vk, "time": 15, }
]
