import logging
from random import shuffle
import re
from aiogram import types
from config import CHAT_ID
from middlewares.check_admin import check_admin
from services import db_manager


async def set_queue(message: types.Message):
    if not await check_admin(message.from_user.username, message.bot, CHAT_ID):
        return await message.answer("У вас нет прав на использование этой команды")
    args = message.get_args()
    subgroup = None
    if len(args) != 0:
        if not re.match(r'^[1|2]$', args):
            return message.reply("Параметр subgroup должен быть 1 или 2")
        subgroup = args
    students_list_length = len(db_manager.get_students(subgroup))
    if students_list_length == 0:
        return await message.reply("Ошибка. В базе нет студентов")
    order = [i for i in range(1, students_list_length+1)]
    shuffle(order)
    result = db_manager.set_queue(order, subgroup)
    if not result:
        return await message.reply("Ошибка генерации очереди :[")
    formatted_list = "".join(
        f"{x}. {i.surname} {i.name}\n" for x, i in enumerate(db_manager.get_queue(subgroup), 1))
    await message.reply(f"Очередь построена\n{formatted_list}")
    logging.info(f"set_queue completed")


async def get_queue(message: types.Message):
    args = message.get_args()
    subgroup = None
    if len(args) != 0:
        if not re.match(r'^[1|2]$', args):
            return await message.reply("Параметр subgroup должен быть 1 или 2")
        subgroup = int(args)
    formatted_list = "".join(
        f"{x}. {i.surname} {i.name}\n" for x, i in enumerate(db_manager.get_queue(subgroup), 1))
    await message.answer(formatted_list if len(formatted_list) > 0 else "Очередь отсутствует")
    logging.info(f"get_queue completed")
