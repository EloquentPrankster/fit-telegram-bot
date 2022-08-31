from main import module
import config


def transferAttachmentsToTelegram(idd, attachments):
    for j in attachments[0:]:

        attType = j.get('type')
        link = j.get('link')

        if attType == 'photo' or attType == 'sticker':
            module.bot.send_photo(config.getCell('vk_' + idd), link)

        elif attType == 'doc' or attType == 'gif' or attType == 'audio_message':
            module.bot.send_document(config.getCell('vk_' + idd), link)

        elif attType == 'other':
            module.bot.send_message(config.getCell('vk_' + idd), link)

        elif attType == 'video':

            # Потому что в ВК не может отправить полную ссылку на файл видео -_-
            module.bot.send_message(config.getCell('vk_' + idd), link)

        else:
            module.bot.send_message(config.getCell(
                'vk_' + idd), '( Неизвестный тип аттачмента )')
