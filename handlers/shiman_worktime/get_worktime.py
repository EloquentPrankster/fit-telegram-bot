import os
from bot import disp
from aiogram import types
from db_api.get_shiman_wt_db import get_shiman_wt_from_db


@disp.message_handler(commands=['getshiman'])
async def shiman_worktime(message: types.Message):
    old_wt = get_shiman_wt_from_db()
    await message.answer(old_wt)
