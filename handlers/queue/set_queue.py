from bot import disp
from aiogram import types
import random
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from handlers.queue.states.Queue import Queue
from utils.get_group_db import get_group_db
from utils.get_queue_db import get_queue_db


@disp.message_handler(Command('setq'), state=None)
async def start_set(message: types.Message, state: FSMContext):
    await message.answer('На какую подгруппу сгенерировать очередь? (1|2)')
    await Queue.Q1.set()


@disp.message_handler(state=Queue.Q1)
async def stop_set(message: types.Message, state: FSMContext):
    if not ('1' in message.text or '2' in message.text):
        await message.answer('Введите 1 или 2')
        return
    subgroup = message.text
    group = await get_group_db()

    group_len = len(group)
    range_of_num = list(range(1, group_len+1))
    random.shuffle(range_of_num)

    await message.answer(range_of_num)
    await state.finish()
