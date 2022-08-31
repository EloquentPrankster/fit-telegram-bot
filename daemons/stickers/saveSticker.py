import urllib.request as ur
import os
import config
from PIL import Image  # Для преобразования изображений из webp в PNG
import addStickerIntoVK
import db


def saveSticker(stickerURL, attachment):

    attachment = attachment.split('/')

    content = ur.urlopen(stickerURL).read()

    path = attachment[0] + '/'
    if not os.path.exists(path):
        os.makedirs(path)

    # Перекодирование из webp в png

    imageWebp = path + attachment[1]

    out = open(imageWebp, 'wb')
    out.write(content)
    out.close()

    img = Image.open(imageWebp)

    if (config.getCell('vk_sticker_EnableScale')):
        scale = config.getCell('vk_sticker_size')
        img.thumbnail((scale, scale))
    img.save(imageWebp + ".png", "PNG")
    os.remove(imageWebp)

    #print( 'Sticker saved!' )

    stickers = addStickerIntoVK(path, attachment[1])
    db.addStickerIntoDb(stickers)
