from aiogram import types
from bot import disp
from config import VK_TOKEN
import vk_api
from utils.get_poll_link import *
session = vk_api.VkApi(token=VK_TOKEN)


@disp.message_handler(commands=['getmessages'])
async def get_messages(message: types.Message):
    listMes = session.method('messages.getHistory',
                       {
                           'count': 10,
                           'peer_id': 2000000084
                       })
    for mes in listMes['items']:
        attachmentList = mes['attachments']
        attachmentLink = ''
        for attachment in attachmentList:
            match attachment['type']:
               case 'poll':
                    attachmentLink = get_poll_link(attachment)
        respond = attachmentLink
        try:
            await message.answer(respond)
        except Exception: 
            await message.answer('что-нибудь')
