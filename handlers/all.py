import logging
from aiogram import types
from config import CHAT_ID
from app import app


async def all(message: types.Message):
    try:
        administrators = []
        async for m in app.get_chat_members(message.chat.id):
            administrators.append(m.user.username)

        await message.answer("".join(['@'+str(i) + " "for i in administrators]))
        logging.info("All command completed successfully")
    except Exception as e:
        logging.error("All command error")
        logging.error(e)
