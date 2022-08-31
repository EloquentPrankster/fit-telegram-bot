import config
import transferMessageToVK
def checkRedirect_telegram(chatid, text, fromUser, attachment):
    if not config.getCell('t_' + chatid) is None:
        transferMessageToVK(chatid, text, fromUser, attachment)
        return False

# Посылаем простые сообщения в Telegram
