import pyshorteners
s = pyshorteners.Shortener().tinyurl


def get_photo_link(attachment) -> str:
    photoLink = s.short(attachment['photo']['sizes'][-1]['url'])
    return photoLink


def get_poll_link(attachment) -> str:
    attachmentLink = 'https://vk.com/poll' + str(attachment['poll']['owner_id']) + '_' + str(attachment['poll']['id'])
    return attachmentLink


def get_document_link(attachment) -> str:
    documentLink = str(attachment['doc']['url'])
    return documentLink


def get_video_title(attachment) -> str:
    videoTitle = str(attachment['video']['title'])
    return videoTitle


def get_video_link(attachment) -> str:
    videoLink = s.short(str(attachment['video']['files']['mp4_480']))
    return videoLink


def get_audio_title(attachment) -> str:
    audioTitle = str(attachment['audio']['artist']) + ' — ' + str(attachment['audio']['title'])
    return audioTitle


def get_audio_link(attachment) -> str:
    audioLink = s.short(str(attachment['audio']['url']))
    return audioLink


def get_audio_message_link(attachment) -> str:
    audioMesLink = s.short(str(attachment['audio_message']['link_mp3']))
    return audioMesLink


def get_wall_link(attachment) -> str:
    wallLink = 'https://vk.com/wall' + str(attachment['wall']['from_id']) + '_' + str(attachment['wall']['id'])
    return wallLink
