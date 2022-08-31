from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import disp
from handlers.shiman_worktime.states.ShimanWorktime import ShimanWorktime
from aiogram.dispatcher import FSMContext
from db import db_cursor, db
from utils.get_shiman_wt_from_db import get_shiman_wt_from_db


@disp.message_handler(Command('set_shiman_worktime'), state=None)
async def start_set(message: types.Message):
    old_wt = get_shiman_wt_from_db()
    await message.answer(old_wt)
    await message.answer("Это текущее расписание.\nСкопируйте, поправьте и отправьте новое. Проверьте правильность.")
    await ShimanWorktime.Q1.set()


@disp.message_handler(state=ShimanWorktime.Q1)
async def stop_set(message: types.Message, state: FSMContext):
    new_wt = message.text
    old_wt = get_shiman_wt_from_db()
    db_cursor.execute(
        f"UPDATE shiman SET worktime='{new_wt}' WHERE worktime='{old_wt}'")
    db.commit()
    await message.answer('Расписание установлено')
    await state.finish()
