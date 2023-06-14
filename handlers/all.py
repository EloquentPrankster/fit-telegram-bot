import logging
from aiogram import types
import services


async def all(message: types.Message):
    usernames = services.db_manager.get_bound_usernames()
    if (len(usernames) == 0):
        return await message.answer("Список пуст. На фан-встречу никто не придет :[")
    username = message.from_user.username
    if username not in usernames:
        return await message.reply("Используйте /bindme, чтобы получить доступ к команде")
    res = "".join(f"@{i.username} " for i in usernames)
    await message.answer(res)
    logging.info(f"all completed")
