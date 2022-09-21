from VK_api.core.core import vk
from VK_api.get_messages.get_messages import get_messages
from VK_api.convert_message.get_link import *

def convert_message(mes) -> str:
    user = vk.method('users.get',{'user_ids': mes['from_id']})
    userFio = user[-1]['first_name'] + ' ' + user[-1]['last_name']

    respond = userFio

    if mes['text'] != '':
        respond += '\n' + mes['text'] 

    i = 1
    for attachment in mes['attachments']:
        match attachment['type']:
            case "photo":
                photoLink = get_photo_link(attachment)
                respond += '\n' + str(i) + '. Фото: \n' + photoLink
            case "poll":
                pollLink = get_poll_link(attachment)
                respond += '\n' + str(i) + '. Опрос: \n' + pollLink
            case "doc":
                documentLink = get_document_link()
                respond += '\n' + str(i) + '. Документ: \n' + documentLink
            case "video":
                videoTitle = get_video_title(attachment)
                videoLink = get_video_link(attachment)
                respond += '\n' + str(i) + '. Видео: ' + videoTitle + '\n' + videoLink
            case "audio":
                audioTitle = get_audio_title(attachment)
                audioLink = get_audio_link(attachment)
                respond += '\n' + str(i) + '. Аудио: ' + audioTitle + '\n' + audioLink
            case _:
                respond += '\n' + str(i) + '. Вложение не распознано!'
        i = i + 1
    try:
        return respond
    except Exception: 
        return 'Ошибка с формированием сообщения. Обратись к админу.'
