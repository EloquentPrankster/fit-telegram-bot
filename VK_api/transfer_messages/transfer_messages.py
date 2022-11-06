from bot import bot
from aiogram import types
import urllib3
from config import NEWS_CHAT
async def transfer_messages(handled_messages:list[dict]):
    http=urllib3.PoolManager()
    decorator='<strong>></strong>'
    for message in handled_messages:
        if 'reply_to' in message or message['text']!='': 
            await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING)
            text= '<strong>'+decorator*message['level']+message['sender']+'</strong>'+'\n'+message['text']+'\n'
            if 'reply_to' in message: text+= '<i>^ Ответ на сообщение от '+'<strong>'+message['reply_to']+'</strong>'+'\n"'+message['reply_text']+'"</i>\n'
            await bot.send_message(NEWS_CHAT, text=text, parse_mode='HTML')

        for attachment in message['attachments']:
            match(attachment['type']):
                case 'photo':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_PHOTO)
                    r=http.request('GET',attachment['url']).data
                    await bot.send_document(NEWS_CHAT, attachment['url'], caption=decorator*message['level']+'Фото от: '+'<strong>' + message['sender'] + '</strong>', parse_mode='HTML')

                case 'doc':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_DOCUMENT)
                    r=http.request('GET',attachment['url']).data
                    await bot.send_document(NEWS_CHAT,(attachment['title'],r), caption=decorator*message['level']+'Документ от: '+'<strong>' + message['sender'] + '</strong>', parse_mode='HTML') 

                case 'video':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_VIDEO)
                    if attachment['by_direct']: await bot.send_video(NEWS_CHAT,attachment['url'], caption=decorator*message['level']+'Видео от: '+ '<strong>' + message['sender'] + '</strong>', parse_mode='HTML')
                    else : await bot.send_message(NEWS_CHAT,text=decorator*message['level']+'<a href="'+attachment['url']+'">Видео</a> от: '+'<strong>' + message['sender'] + '</strong>'+'\n',parse_mode='HTML')

                case "audio":
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLO)
                    r=http.request('GET',attachment['url']).data
                    await bot.send_audio(NEWS_CHAT,r,performer=attachment['artist'],title=attachment['title'], duration=attachment['duration'],caption=decorator*message['level']+'Аудио от: '+ '<strong>' + message['sender'] + '</strong>', parse_mode='HTML')

                case 'audio_message':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_VOICE)
                    await bot.send_voice(NEWS_CHAT, attachment['link_ogg'],caption=decorator*message['level']+'Голосовое сообщение от: '+ '<strong>' + message['sender'] + '</strong>', parse_mode='HTML')  

                case 'link':
                    await bot.send_message(NEWS_CHAT, text=decorator*message['level']+'<a href="'+attachment['url']+'">'+attachment['title']+'</a> от '+'<strong>' + message['sender'] + '</strong>', parse_mode='HTML')

                case "poll":
                    await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING) 
                    await bot.send_message(NEWS_CHAT, text=decorator*message['level']+'<a href="'+attachment['url']+'">Голосование</a> от '+'<strong>' + message['sender'] + '</strong>', parse_mode='HTML')

                case "wall":
                    await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING)
                    await bot.send_message(NEWS_CHAT, text=decorator*message['level']+'<a href="'+attachment['url']+'">Запись на стене</a> от '+'<strong>' + message['sender'] + '</strong>', parse_mode='HTML')

                case 'undefined':
                    await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING)
                    await bot.send_message(NEWS_CHAT, text='<strong>'+decorator*message['level']+message['sender']+'</strong>'+'\n'+'Вложение не распознано. Вероятно стикер, карта или другой шлак.', parse_mode='HTML')
