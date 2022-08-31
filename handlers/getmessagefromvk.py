from aiogram import types
from bot import disp
import vk_api
session = vk_api.VkApi(token='Хуй те а не токен')
vk = session.get_api()


@disp.message_handler(commands=['getmessages'])
async def peacedeath(message: types.Message):
    a = session.method('messages.getHistory',
                       {
                           'count': 10,
                           'peer_id': 2000000141
                       })

    for i in a['items']:
        await message.answer(i)
