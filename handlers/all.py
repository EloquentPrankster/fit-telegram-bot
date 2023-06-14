import logging
from aiogram import types
import services


async def all(message: types.Message):
    res = "".join(
        f"@{i.username} " for i in services.db_manager.get_bound_usernames())
    await message.answer(res if len(res) != 0 else "Никто не пришел на фан-встречу :[")
    logging.info(f"all completed")
