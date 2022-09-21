from aiogram import types
from bot import disp

from VK_api.transfer_messages.transfer_messages import transfer_messages
from VK_api.get_messages.get_messages import get_messages

@disp.message_handler(commands=['getmesvk'])
async def getmesvk(message: types.Message):
    listMes = get_messages()
    await transfer_messages(listMes)
