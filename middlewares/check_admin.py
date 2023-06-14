import logging
from middlewares.get_chat_admins import get_chat_admins


async def check_admin(username, bot, chat_id):
    list_of_admin = await get_chat_admins(bot, chat_id)
    logging.info(f"check_admin completed")
    return username in list_of_admin
