from bot import bot
from config import CHAT_TO_NOTIFY

from VK_api.core.core import vk
from VK_api.get_messages.get_messages import get_messages
from VK_api.convert_message.get_link import *
from VK_api.convert_message.convert_message import convert_message

async def transfer_messages():
    try:
        listMes = get_messages()
        for mes in listMes:
            respond = convert_message(mes)

            try:
                await bot.send_message(CHAT_TO_NOTIFY, respond)
            except Exception: 
                await bot.send_message(CHAT_TO_NOTIFY, 'Траблы. Пиши админу.')
    except Exception:
        pass
