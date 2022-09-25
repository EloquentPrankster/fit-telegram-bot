from bot import bot
from config import CHAT_TO_NOTIFY

from VK_api.convert_message.convert_message import convert_message

async def transfer_messages(listMes):
    try:
        for mes in listMes:
            respond = convert_message(mes, 1)

            try:
                await bot.send_message(CHAT_TO_NOTIFY, respond)
            except Exception: 
                await bot.send_message(CHAT_TO_NOTIFY, 'Траблы. Пиши админу.')
    except Exception as ex:
        print(ex)
