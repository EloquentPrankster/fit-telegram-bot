import logging
import re
from aiogram import types
from services import db_manager


async def add_description(message: types.Message):
    args = message.get_args()
    if args == "":
        return await message.reply("Не хватает аргументов")
    if len(args) > 120:
        return await message.reply("Описание не может быть больше 120 символов")
    result = db_manager.add_description(args)
    await message.reply("Успешно добавлено" if result else "Ошибка добавления ;(")
    logging.info(f"add_description completed with result {result}")


async def get_descriptions(message: types.Message):
    result = db_manager.get_descriptions()
    if len(result) == 0:
        return await message.reply("Список пуст")
    formatted_list = "".join(
        [f"{x}.(ID={i.id}): {i.description}\n" for x, i in enumerate(result)])
    await message.answer(formatted_list)
    logging.info(f"get_descriptions completed with result {result}")


async def del_description(message: types.Message):
    args = message.get_args()
    if args == "":
        return await message.reply("Не хватает аргументов")
    if re.match(r'^[0-9]*$', args) is None:
        return await message.reply("ID должен быть числом")
    result = db_manager.del_description(args)
    await message.reply("Успешно удалено" if result else "Ошибка удаления")
    logging.info(f"del_description completed with result {result}")
