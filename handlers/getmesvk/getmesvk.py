from aiogram import types
from bot import *

from VK_api.core.core import vk
from VK_api.get_messages.get_messages import get_messages
from VK_api.convert_message.get_link import *
from VK_api.convert_message.convert_message import convert_message

@disp.message_handler(commands=['getmesvk'])
async def getmesvk(message: types.Message):
    
    listMes = get_messages()

    for mes in listMes:
        respond = convert_message(mes)

        try:
            await message.answer(respond)
        except Exception: 
            await message.answer('что-нибудь')
