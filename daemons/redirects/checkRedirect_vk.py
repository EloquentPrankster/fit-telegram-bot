import config
from daemons.main import checkAttachments, checkEvents, getFwdMessages, getUserName
import transferMessagesToTelegram

def checkRedirect_vk(msg):

    chatid = str(msg['conversation']['peer']['local_id'])

    # Проверка на существование переадресации в конфиге
    if not config.getCell("vk_" + chatid) is None:

        forwardMessage = getFwdMessages(msg['last_message'], chatid)

        userName = getUserName(msg['last_message'])
        mbody = msg['last_message'].get('text')

        # Чтобы при событии не посылалось пустое сообщение
        if checkEvents(msg, chatid) is None:
            transferMessagesToTelegram(chatid, userName, mbody, forwardMessage)

        # Проверка на аттачменты, пересланные сообщения, видео...
        # Проверка сделана, чтобы исключить повтор картинки
        if forwardMessage is None:
            checkAttachments(msg['last_message'], chatid)

        return True
    return False
