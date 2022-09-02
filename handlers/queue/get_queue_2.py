from bot import disp
from aiogram import types
from utils.get_queue_db import get_queue_db
from utils.show_queue import show_queue


@disp.message_handler(commands=['getq2'])
async def get_q_2(message: types.Message):
    list = await get_queue_db(2)
    await message.answer(show_queue(list, 2))
