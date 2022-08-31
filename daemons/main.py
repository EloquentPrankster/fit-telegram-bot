#!/usr/lib/python3 python
# -*- coding: utf-8 -*-
import sys
import config
from daemons.redirects.transferAttachmentsToTelegram import transferAttachmentsToTelegram
from daemons.telegram.init_telegram import init_telegram
import datetime
import telebot
from vk import init_vk
from redirects import transferMessagesToTelegram
import threading

config.initConfig()

module = sys.modules[__name__]


def current_time():
    delta = datetime.timedelta(hours=3)
    utc = datetime.timezone.utc
    fmt = '%H:%M:%S'
    time = (datetime.datetime.now(utc) + delta)
    timestr = time.strftime(fmt)
    return timestr

# Получение имени пользователя


def getUserName(msg):
    # Для приёма личных сообщений когда пишут через группу
    if (int(msg.get('from_id')) < 0):
        return None
    else:
        dataname = module.vk.users.get(user_ids=msg.get('from_id'))
        name = str(dataname[0]['first_name'] + ' ' + dataname[0]['last_name'])
    return name


def getUserTName(msg):
    if msg.last_name is None:
        userName = str(msg.first_name)
    else:
        userName = str(msg.first_name + " " + msg.last_name)
    return userName

# Проверка на наличие аттачментов в сообщении


def checkAttachments(msg, idd):
    if not (msg.get('attachments')):
        return False
    transferAttachmentsToTelegram(idd, getAttachments(msg))
    return True

# Получаем аттачменты из сообщения ВК


def getAttachments(msg):

    attachList = []

    for att in msg['attachments'][0:]:

        attType = att.get('type')

        attachment = att[attType]

        if attType == 'photo':  # Проверка на тип фотографии

            for photoType in attachment.get('sizes')[0:]:
                if photoType.get('type') == 'x':  # <=604x604
                    attachments = photoType.get('url')
                if photoType.get('type') == 'y':  # >605x605
                    attachments = photoType.get('url')
                if photoType.get('type') == 'z':  # <=1280x720
                    attachments = photoType.get('url')
                if photoType.get('type') == 'w':  # >1280x720
                    attachments = photoType.get('url')  # <=2560x1440
                    attType = 'other'

        elif attType == 'doc':  # Проверка на тип документа:
            # Про типы документов можно узнать тут: https://vk.com/dev/objects/doc
            docType = attachment.get('type')
            if docType != 3 and docType != 4 and docType != 5:
                attType = 'other'
            if attachment.get('url'):
                attachments = attachment.get('url')

        elif attType == 'sticker':  # Проверка на стикеры:
            for sticker in attachment.get('images')[0:]:
                # Можно 256 или 512, но будет слишком огромная пикча
                if sticker.get('width') == 128:
                    attachments = sticker.get('url')

        elif attType == 'audio':
            attachments = str('𝅘𝅥𝅮 ' + attachment.get('artist') + ' - ' +
                              attachment.get('title') + ' 𝅘𝅥𝅮')
            attType = 'other'

        elif attType == 'audio_message':
            attachments = attachment.get('link_ogg')

        elif attType == 'video':

            ownerId = str(attachment.get('owner_id'))
            videoId = str(attachment.get('id'))
            accesskey = str(attachment.get('access_key'))

            fullURL = str(ownerId + '_' + videoId + '_' + accesskey)

            attachments = module.vk.video.get(videos=fullURL)[
                'items'][0].get('player')

        elif attType == 'graffiti':
            attType = 'other'
            attachments = attachment.get('url')

        elif attType == 'link':
            attType = 'other'
            attachments = attachment.get('url')

        elif attType == 'wall':
            attType = 'other'
            attachments = 'https://vk.com/wall'
            from_id = str(attachment.get('from_id'))
            post_id = str(attachment.get('id'))
            attachments += from_id + '_' + post_id

        elif attType == 'wall_reply':
            attType = 'other'
            attachments = 'https://vk.com/wall'
            owner_id = str(attachment.get('owner_id'))
            reply_id = str(attachment.get('id'))
            post_id = str(attachment.get('post_id'))
            attachments += owner_id + '_' + post_id
            attachments += '?reply=' + reply_id

        elif attType == 'poll':
            attType = 'other'
            attachments = 'https://vk.com/poll'
            owner_id = str(attachment.get('owner_id'))
            poll_id = str(attachment.get('id'))
            attachments += owner_id + '_' + poll_id
        # Неизвестный тип?
        else:

            attachments = None

        attachList.append({'type': attType,
                           'link': attachments})

    #print( attachList )

    return attachList

# Проверка чата ВК на различные события


def checkEvents(msg, chatid):

    if not (msg['last_message'].get('action')):
        return None  # И так сойдёт

    event = msg['last_message']['action'].get('type')
    userName = getUserName(msg['last_message'])

    # Ниже проверям наш чат на различные события
    # См. https://vk.com/dev/objects/message

    if event == 'chat_title_update':
        eObject = str(msg['last_message']['action'].get('text'))
        mbody = " *** " + userName + \
            " изменил(а) название беседы на " + eObject + " ***"

    elif event == 'chat_invite_user':
        dataname = module.vk.users.get(
            user_ids=msg['last_message']['action'].get('member_id'))
        eObject = str(dataname[0]['first_name'] +
                      ' ' + dataname[0]['last_name'])
        mbody = " *** " + userName + \
            " пригласил(а) в беседу " + eObject + " ***"

    elif event == 'chat_kick_user':
        dataname = module.vk.users.get(
            user_ids=msg['last_message']['action'].get('member_id'))
        eObject = str(dataname[0]['first_name'] +
                      ' ' + dataname[0]['last_name'])
        mbody = " *** " + userName + " кикнул(а) из беседы " + eObject + " ***"

    elif event == 'chat_photo_update':
        mbody = " *** " + userName + " обновил(а) фото беседы: ***"

    elif event == 'chat_photo_remove':
        mbody = " *** " + userName + " удалил(а) фото беседы! ***"

    elif event == 'chat_pin_message':
        eObject = str(msg['last_message']['action'].get('message'))
        if (eObject):
            mbody = " *** " + userName + " закрепил(а): " + eObject + " ***"
        else:
            mbody = " *** " + userName + " закрепил(а) сообщение! ***"

    elif event == 'chat_unpin_message':
        mbody = " *** " + userName + " открепил(а) сообщение! ***"

    elif event == 'chat_create':
        print('Беседа была создана!')

    else:
        return None

    transferMessagesToTelegram(chatid, None, mbody, None)

# Проверка на наличие перешлённых сообщений


def getFwdMessages(msg, idd):

    if not (msg.get('fwd_messages')):
        return None  # И так сойдёт

    fwdList = []
    fwdMsg = msg.get('fwd_messages')

    while not fwdMsg is None:

        userName = getUserName(fwdMsg[0])

        fwdList.append({'body': fwdMsg[0].get('text'), 'userName': userName})

        checkAttachments(fwdMsg[0], idd)

        fwdMsg = fwdMsg[0].get('fwd_messages')

    return fwdList


def checknewfriends():
    newfriends = module.vk.friends.getRequests(
        out=0, count=1, need_viewed=1)  # Смотрим, если ли заявки в друзья
    if newfriends['count'] != 0:
        # Добавляем человека в друзья
        module.vk.friends.add(user_id=newfriends['items'])


t1 = threading.Thread(target=init_vk)
t2 = threading.Thread(target=init_telegram)

t1.start()
t2.start()
t1.join()
t2.join()
