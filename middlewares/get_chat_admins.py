import logging
from aiogram import Bot


async def get_chat_admins(bot: Bot, chat_id) -> list[str]:
    result = await bot.get_chat_administrators(chat_id=chat_id)
    logging.info(f"get_chat_admins completed")
    return [f"{i['user']['username']}" for i in result]
