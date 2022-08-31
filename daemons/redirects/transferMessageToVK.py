import random
import config
from daemons.main import current_time
from main import module
import vk_api
import db
from stickers import saveSticker


def transferMessageToVK(chatid, text, fromUser, attachment):
    if (config.getCell('telegram_SendName')):
        time = current_time()
        text = str(time + ' | ' + fromUser + ': ' + text)

    randid = random.randint(-9223372036854775808, +
                            9223372036854775807)  # int64

    if attachment is None:

        try:
            module.vk.messages.send(chat_id=config.getCell(
                't_' + chatid), message=text, random_id=randid)
        except vk_api.ApiError as error_msg:
            module.vk.messages.send(user_id=config.getCell(
                't_' + chatid), message=text, random_id=randid)
        #print( 'Сообщение успешно отправлено! ( ' + text + ' )' )

    else:

        getSticker = db.checkSticker(attachment)

        # Если стикер не найден в БД
        if getSticker is None:
            stickerURL = 'https://api.telegram.org/file/bot{0}/{1}'.format(
                config.getCell('telegram_token'), attachment)
            saveSticker(stickerURL, attachment)
            getSticker = db.checkSticker(attachment)

        #print( getSticker )

        try:
            module.vk.messages.send(chat_id=config.getCell(
                't_' + chatid), message="", attachment=getSticker, random_id=randid)
        except vk_api.ApiError as error_msg:
            module.vk.messages.send(user_id=config.getCell(
                't_' + chatid), message="", attachment=getSticker, random_id=randid)

    return False
