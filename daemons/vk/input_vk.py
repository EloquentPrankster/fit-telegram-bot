from daemons.main import checkRedirect_vk, checknewfriends
from main import module
import config


def input_vk():

    while True:

        try:
            # Ставим онлайн боту, чому бы и нет?
            module.vk.account.setOnline()

            # Проверка на наличие подписчиков
            if (config.getCell('vk_AddFriends')):
                checknewfriends()

            rawMessages = module.vk.messages.getConversations(
                filter='unread', count=config.getCell('vk_msgForPick'))['items']
            if not rawMessages:
                continue

            msg = rawMessages[0]['conversation']['peer']
            if checkRedirect_vk(rawMessages[0]) or config.getCell('vk_markAsReadEverything'):
                module.vk.messages.markAsRead(
                    messages_ids=msg['local_id'], peer_id=msg['id'])

        # Чтобы не вылетало, а работало дальше
        except BaseException as e:
            print(e)
            print('Что-то пошло не так...')
            continue
