from daemons.main import getUserTName
from daemons.redirects.checkRedirect_telegram import checkRedirect_telegram
import config
from main import module


def listener(messages):
    for m in messages:

        if m.content_type == 'text':

            # На команду 'Дай ID' кидает ID чата
            if m.text == 'Дай ID':
                module.bot.send_message(m.chat.id, str(m.chat.id))
                continue

            checkRedirect_telegram(str(m.chat.id), str(
                m.text), getUserTName(m.from_user), None)

        elif m.content_type == 'sticker':

            if not (config.getCell('vk_EnableStickers')):
                return False

            filePath = module.bot.get_file(m.sticker.file_id).file_path

            checkRedirect_telegram(str(m.chat.id), str(
                m.text), getUserTName(m.from_user), str(filePath))
