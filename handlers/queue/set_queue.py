import random
from bot import disp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from handlers.queue.states.Queue import Queue
from db_api.get_group_db import get_group_db
from db_api.get_queue_db import get_queue_db
from db_api.set_queue_db import set_queue_db
from handlers.queue.helpers.show_queue import show_queue
from handlers.rights.helpers.check_acc import has_access


@disp.message_handler(Command('setq'), state=None)
async def start_set(message: types.Message, state: FSMContext):
    if not has_access(message.from_user.username): return await message.answer("У вас нет прав на эту команду")
    await message.answer('На какую подгруппу сгенерировать очередь? (1|2)')
    await Queue.Q1.set()


@disp.message_handler(state=Queue.Q1)
async def stop_set(message: types.Message, state: FSMContext):
    if not (message.text == '1' or message.text == '2'):
        await message.answer('Введите 1 или 2')
        return
    sgroup_num = int(message.text)
    sgroup = await get_group_db(sgroup_num)
    range_of_num = list(range(1, len(sgroup)+1))
    random.shuffle(range_of_num)
    isCommited = set_queue_db(sgroup_num, sgroup, range_of_num)
    await message.answer("Список изменен" if isCommited else "Ошибка обновления")
    await state.finish()
    if isCommited:
        await message.answer(show_queue(await get_queue_db(sgroup_num), sgroup_num))
