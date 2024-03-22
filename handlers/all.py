import asyncio
import logging
from math import log
from aiogram import types
from config import CHAT_ID
from app import app


async def all(message: types.Message):
    try:
        users = []
        async for m in app.get_chat_members(message.chat.id):
            users.append(m.user.username)

        matrix_with_users = [[] for _ in range(0, (len(users)/5).__ceil__())]

        i = row = 0
        for user in users:
            matrix_with_users[row].append(user)
            i += 1
            if i % 5 == 0:
                row += 1

        for i in matrix_with_users:
            await message.answer("".join(['@'+str(b) + " " for b in i]))
            await asyncio.sleep(1)

        logging.info("All command completed successfully")
    except Exception as e:
        logging.error("All command error")
        logging.error(e)
