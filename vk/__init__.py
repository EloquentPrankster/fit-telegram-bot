import re
import urllib3
import vk_api
from aiogram import Bot, types
from middlewares.dictionary import Dictionary


class VKManager:
    def __init__(self, bot: Bot, VK_TOKEN, VK_PEER_ID, NEWS_ID) -> None:
        self.vk_instance = vk_api.VkApi(token=VK_TOKEN)
        self.__bot = bot
        self.__VK_PEER_ID = VK_PEER_ID
        self.__NEWS_CHAT_ID = NEWS_ID

    async def get_messages(self):
        """Get messages from self.vk_instance. If there are messages, then sends them to Telegram"""
        unread_dialogs: list[dict] = self.vk_instance.method(
            'messages.getDialogs', {'unread': 1})['items']
        count = 0
        if len(unread_dialogs) == 0:
            return
        for i in unread_dialogs:
            if i['message'].get('chat_id') == int(self.__VK_PEER_ID) - 2000000000:
                count = i['unread']
                unhandled_messages: list[dict] = \
                    self.vk_instance.method('messages.getHistory', {
                        'count': count, 'peer_id': int(self.__VK_PEER_ID)})['items']
                self.vk_instance.method('messages.markAsRead', {'peer_id': int(
                    self.__VK_PEER_ID), 'mark_conversation_as_read': 1})
                unhandled_messages = unhandled_messages[::-1]
                handled_messages = self.clean_up_messages(
                    unhandled_messages, [], 0)
                await self.transfer_messages(handled_messages)
            else:
                continue
        return

    def clean_up_messages(self, raw_messages: list[dict], handled_messages=[], level=0) -> list[dict]:
        vk_trash = ['date', 'id', 'conversation_message_id',
                    'important', 'is_hidden', 'peer_id', 'random_id', 'out']
        messages_to_handle = [Dictionary(i) for i in raw_messages]
        prepared_messages = [i.pop(vk_trash).get_dictionary()
                             for i in messages_to_handle]

        for item in prepared_messages:
            item.update({'level': level})
            user = self.vk_instance.method(
                'users.get', {'user_ids': item['from_id']})
            sender = user[-1]['first_name'] + ' ' + user[-1]['last_name']
            item.update({'sender': sender})
            item.pop('from_id')

            if 'reply_message' in item:
                user = self.vk_instance.method(
                    'users.get', {'user_ids': item['reply_message']['from_id']})
                reply_to = item['reply_message']['text'] if 'text' in item['reply_message'] else ''
                item.update(
                    {
                        'reply_to': user[-1]['first_name'] + ' ' + user[-1]['last_name'],
                        'reply_text': reply_to
                    }
                )

            attachments = []
            for attach in item['attachments']:
                match (attach['type']):
                    case "photo":
                        link = ""
                        for i in attach["photo"]["sizes"]:
                            if "w" in i["type"]:
                                link = i["url"]
                                break
                            elif "z" in i["type"]:
                                link = i["url"]
                            elif "y" in i["type"]:
                                link = i["url"]
                            elif "x" in i["type"]:
                                link = i["url"]
                            elif "m" in i["type"]:
                                link = i["url"]
                            elif "s" in i["type"]:
                                link = i["url"]
                        photo = Dictionary(attach['photo'].copy()).clear().update(
                            {
                                'type': 'photo',
                                'url': link,
                            }
                        ).get_dictionary()
                        attachments.append(photo)

                    case "poll":
                        poll = Dictionary(attach['poll'].copy()).clear().update(
                            {
                                'type': 'poll',
                                'url': 'https://vk.com/poll' + str(attach['poll']['owner_id']) + '_' + str(
                                    attach['poll']['id']),
                            }
                        ).get_dictionary()
                        attachments.append(poll)

                    case "doc":
                        doc = Dictionary(attach['doc'].copy()).clear().update(
                            {
                                'title': attach['doc']['title'],
                                'type': 'doc',
                                'url': attach['doc']['url'],
                            }
                        ).get_dictionary()
                        attachments.append(doc)

                    case "wall":
                        wall = Dictionary(attach['wall'].copy()).clear().update(
                            {
                                'type': 'wall',
                                'url': 'https://vk.com/wall' + str(attach['wall']['from_id']) + '_' + str(
                                    attach['wall']['id']),
                            }
                        ).get_dictionary()
                        attachments.append(wall)

                    case "video":
                        if 'external' in attach['video']['files']:
                            url = attach['video']['files']['external']
                            attach['video'].update({'by_direct': False})

                        else:
                            if 'mp4_720' in attach['video']['files']:
                                quality = 'mp4_720'
                            elif 'mp4_480' in attach['video']['files']:
                                quality = 'mp4_480'
                            elif 'mp4_240' in attach['video']['files']:
                                quality = 'mp4_240'
                            elif 'mp4_144' in attach['video']['files']:
                                quality = 'mp4_144'
                            if re.match(r'.*\.mp4.*', attach['video']['files'][quality]):
                                url = attach['video']['files'][quality]
                                attach['video'].update({'by_direct': True})
                            else:
                                owner_id = str(attach['video']['owner_id'])
                                video_id = str(attach['video']['id'])
                                attach['video'].update({'by_direct': False})
                                url = 'https://vk.com/im?z=video' + owner_id + '_' + video_id

                        video = Dictionary(attach['video'].copy()).clear().update(
                            {
                                'type': 'video',
                                'title': attach['video']['title'],
                                'by_direct': attach['video']['by_direct'],
                                'url': url,
                            }
                        ).get_dictionary()
                        attachments.append(video)

                    case "audio":
                        audio = Dictionary(attach['audio'].copy()).clear().update(
                            {
                                'type': 'audio',
                                'artist': attach['audio']['artist'],
                                'title': attach['audio']['title'],
                                'duration': attach['audio']['duration'],
                                'url': attach['audio']['url'],
                            }
                        ).get_dictionary()
                        attachments.append(audio)

                    case "audio_message":
                        audio_message = Dictionary(attach['audio_message'].copy()).clear().update(
                            {
                                'type': 'audio_message',
                                'duration': attach['audio_message']['duration'],
                                'link_ogg': attach['audio_message']['link_ogg'],
                            }
                        ).get_dictionary()
                        attachments.append(audio_message)

                    case "link":
                        link = Dictionary(attach['link'].copy()).clear().update(
                            {
                                'type': 'link',
                                'url': attach['link']['url'],
                            }
                        ).get_dictionary()
                        attachments.append(link)

                    case _:
                        attachments.append({'type': 'undefined'})

            item.update({'attachments': attachments})

            if 'fwd_messages' in item:
                popped_fwd = item.pop('fwd_messages')
                handled_messages.append(item)
                self.clean_up_messages(popped_fwd, handled_messages, level + 1)
            else:
                handled_messages.append(item)
        return handled_messages

    async def transfer_messages(self, handled_messages: list[dict]):
        http = urllib3.PoolManager()
        decorator = '<strong>></strong>'
        for message in handled_messages:
            if 'reply_to' in message or message['text'] != '':
                await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.TYPING)
                text = '<strong>' + decorator * message['level'] + message['sender'] + '</strong>' + '\n' + message[
                    'text'] + '\n'
                if 'reply_to' in message:
                    text += '<i>^ Ответ на сообщение от ' + '<strong>' + message[
                        'reply_to'] + '</strong>' + '\n"' + message['reply_text'] + '"</i>\n'
                await self.__bot.send_message(self.__NEWS_CHAT_ID, text=text, parse_mode='HTML')

            photo_count = 0
            for i in message['attachments']:
                if 'photo' in i['type']:
                    photo_count += 1
            if photo_count > 1:
                photo_group = types.MediaGroup()

            for attachment in message['attachments']:
                match (attachment['type']):
                    case 'photo':
                        if photo_count > 1:
                            photo_group.attach_photo(attachment['url'],
                                                     caption=decorator * message['level'] + 'Фото от: ' + '<strong>' +
                                                     message['sender'] + '</strong>', parse_mode='HTML')
                            continue

                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.UPLOAD_PHOTO)
                        await self.__bot.send_photo(self.__NEWS_CHAT_ID, attachment['url'],
                                                    caption=decorator * message['level'] + 'Фото от: ' + '<strong>' + message[
                            'sender'] + '</strong>', parse_mode='HTML')

                    case 'doc':
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.UPLOAD_DOCUMENT)
                        r = http.request('GET', attachment['url']).data
                        await self.__bot.send_document(self.__NEWS_CHAT_ID, (attachment['title'], r),
                                                       caption=decorator * message['level'] + 'Документ от: ' + '<strong>' +
                                                       message['sender'] + '</strong>', parse_mode='HTML')

                    case 'video':
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.UPLOAD_VIDEO)
                        if attachment['by_direct']:
                            await self.__bot.send_video(self.__NEWS_CHAT_ID, attachment['url'],
                                                        caption=decorator * message['level'] + 'Видео от: ' + '<strong>' + message[
                                'sender'] + '</strong>', parse_mode='HTML')
                        else:
                            await self.__bot.send_message(self.__NEWS_CHAT_ID, text=decorator * message['level'] + '<a href="' + attachment[
                                'url'] + '">Видео</a> от: ' + '<strong>' + message['sender'] + '</strong>' + '\n',
                                parse_mode='HTML')

                    case "audio":
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.UPLOAD_AUDIO)
                        r = http.request('GET', attachment['url']).data
                        await self.__bot.send_audio(self.__NEWS_CHAT_ID, r, performer=attachment['artist'], title=attachment['title'],
                                                    duration=attachment['duration'],
                                                    caption=decorator * message['level'] + 'Аудио от: ' + '<strong>' + message[
                            'sender'] + '</strong>', parse_mode='HTML')

                    case 'audio_message':
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.UPLOAD_VOICE)
                        await self.__bot.send_voice(self.__NEWS_CHAT_ID, attachment['link_ogg'], caption=decorator * message[
                            'level'] + 'Голосовое сообщение от: ' + '<strong>' + message['sender'] + '</strong>',
                            parse_mode='HTML')

                    case 'link':
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.TYPING)
                        if attachment['url'] in message['text']:
                            pass
                        else:
                            await self.__bot.send_message(self.__NEWS_CHAT_ID, text=decorator * message['level'] + '<a href="' + attachment[
                                'url'] + '">Ссылка</a> от ' + '<strong>' + message['sender'] + '</strong>',
                                parse_mode='HTML')

                    case "poll":
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.TYPING)
                        await self.__bot.send_message(self.__NEWS_CHAT_ID, text=decorator * message['level'] + '<a href="' + attachment[
                            'url'] + '">Голосование</a> от ' + '<strong>' + message['sender'] + '</strong>',
                            parse_mode='HTML')

                    case "wall":
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.TYPING)
                        await self.__bot.send_message(self.__NEWS_CHAT_ID, text=decorator * message['level'] + '<a href="' + attachment[
                            'url'] + '">Запись на стене</a> от ' + '<strong>' + message['sender'] + '</strong>',
                            parse_mode='HTML')

                    case 'undefined':
                        await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.TYPING)
                        await self.__bot.send_message(self.__NEWS_CHAT_ID, text='<strong>' + decorator * message['level'] + message[
                            'sender'] + '</strong>' + '\n' + 'Вложение не распознано. Вероятно стикер, карта или другой шлак.',
                            parse_mode='HTML')

            if photo_count > 1:
                await self.__bot.send_chat_action(self.__NEWS_CHAT_ID, types.ChatActions.UPLOAD_PHOTO)
                await self.__bot.send_media_group(self.__NEWS_CHAT_ID, photo_group)
