from aiogram import types
from bot import disp
from config import VK_TOKEN
import vk_api
from vk_api.get_poll_link import *
from vk_api.get_photo_link import *
from bot import * 

session = vk_api.VkApi(token=VK_TOKEN)


@disp.message_handler(commands=['getmessages'])
async def get_messages(message: types.Message):
    listMes = session.method('messages.getHistory',
                       {
                           'count': 10,
                           #'peer_id': 2000000084
                           'peer_id': 2000000099
                       })
    for mes in listMes['items']:
        user = session.method('users.get',{'user_ids': mes['from_id']})
        text = mes['text']
        attachmentList = mes['attachments']
        pollLink = ''
        photoLink = ''
        for attachment in attachmentList:
            match attachment['type']:
                case 'poll':
                    pollLink = get_poll_link(attachment)
                case 'photo':
                    photoLink = get_photo_link(attachment)

        
        #respond = user[0]['last_name'] + user[0]['first_name'] + '\n' + text + '\n' +  pollLink
        
        await bot.send_photo(chat_id=message.chat.id, photo=photoLink)
        pollLink = ''
        photoLink = ''
        

        try:
            await message.answer(respond)
        except Exception: 
            await message.answer('что-нибудь')
