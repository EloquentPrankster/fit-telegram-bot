from VK_api.core.core import vk
from VK_api.convert_message.get_link import *

def convert_message(mes, numi) -> str:
    user = vk.method('users.get',{'user_ids': mes['from_id']})
    userFio = user[-1]['first_name'] + ' ' + user[-1]['last_name']

    respond = userFio

    print(mes)

    if mes['text'] != '':
        respond += '\n"' + mes['text'] + '"'
    
    if 'reply_message' in mes:
        replyUser = vk.method('users.get',{'user_ids': mes['reply_message']['from_id']})
        replyFio = replyUser[-1]['first_name'] + ' ' + user[-1]['last_name']
        respond += '\n' + 'Ответ на сообщение -> ' + str(replyFio)
        if mes['reply_message']['text'] != '':
            respond += ':\n"' + mes['reply_message']['text'] + '"'
    
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
                documentLink = get_document_link(attachment)
                respond += '\n' + str(i) + '. Документ: \n' + documentLink
            case "wall":
                wallLink = get_wall_link(attachment)
                respond += '\n' + str(i) + '. Запись сообщества: \n' + wallLink
            case "video":
                videoTitle = get_video_title(attachment)
                videoLink = get_video_link(attachment)
                respond += '\n' + str(i) + '. Видео: ' + videoTitle + '\n' + videoLink
            case "audio":
                audioTitle = get_audio_title(attachment)
                audioLink = get_audio_link(attachment)
                respond += '\n' + str(i) + '. Аудио: ' + audioTitle + '\n' + audioLink
            case "audio":
                audioTitle = get_audio_title(attachment)
                audioLink = get_audio_link(attachment)
                respond += '\n' + str(i) + '. Аудио: ' + audioTitle + '\n' + audioLink
            case _:
                respond += '\n' + str(i) + '. Вложение не распознано!'
        i = i + 1

    if not 'fwd_messages' in mes: return respond
    i = 1
    for fwd_mes in mes['fwd_messages']:
        respond += '\n-------------\n' + str(numi) + '.' + str(i) + '. Пересланные сообщения: \n' + convert_message(fwd_mes, numi + 1)
        i = i + 1
    try:
        return respond
    except Exception: 
        return 'Ошибка с формированием сообщения. Обратись к админу.'
