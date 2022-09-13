from bot import disp
from aiogram import types
from db_api.get.get_queue_db import get_queue_db
from handlers.queue.helpers.show_queue import show_queue


@disp.message_handler(commands=['getq1'])
async def get_q_1(message: types.Message):
    list = await get_queue_db(1)
    await message.answer(show_queue(list, 1))
