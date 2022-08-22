import os
from bot import disp
from aiogram import types
from bot import bot


@disp.message_handler(commands=['shiman_worktime'])
async def shiman_worktime(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open(os.path.abspath('./img/shiman_time.jpg'), 'rb'))
