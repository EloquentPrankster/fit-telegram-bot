from bot import disp
from aiogram import types
from db_api.get.get_queue_db import get_queue_db
from handlers.queue.helpers.show_queue import show_queue


@disp.message_handler(commands=['getq1'])
async def get_q_1(message: types.Message):
    await show_queues(1, message)


@disp.message_handler(commands=['getq2'])
async def get_q_2(message: types.Message):
    await show_queues(2, message)


async def show_queues(sub_num: int, message):
    queues_list = await get_queue_db(sub_num)
    await message.answer(show_queue(queues_list, sub_num))
