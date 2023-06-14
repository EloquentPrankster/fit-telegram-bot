import logging
from services import db_manager
from aiogram import types


async def bind_alias(message: types.Message):
    username = message.from_user.username
    result = db_manager.bind_username(username=username)
    await message.answer("Username добавлен" if result
                         else "Ошибка добавления. Возможно, запись уже есть")
    logging.info(f"bind_alias completed with result: {result}")


async def unbind_alias(message: types.Message):
    username = message.from_user.username
    result = db_manager.unbind_username(username=username)
    await message.answer("Username удален" if result
                         else "Ошибка удаления. Возможно, записи нет")
    logging.info(f"unbind_alias completed with result: {result}")


async def get_aliases(message: types.Message):
    aliases = db_manager.get_bound_usernames()
    if len(aliases) == 0:
        return await message.answer("Список пуст")
    formatted_list = "".join(f"{i.username} " for i in aliases)
    await message.answer(formatted_list)
    logging.info(f"get_aliases completed")
