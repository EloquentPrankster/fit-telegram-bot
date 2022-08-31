import os
import config
import vk_api
from main import vk_session
# Загрузка стикеров в ВК


def addStickerIntoVK(path, sticker):

    stickerList = []
    ourFile = path + sticker

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        ourFile + ".png", album_id=config.getCell('vk_album_id'))

    if (config.getCell('vk_detelestickers')):
        os.remove(ourFile + ".png")

    ourVK = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])

    stickerList.append({'sticker_t': ourFile,
                        'sticker_vk': ourVK})
    return stickerList
