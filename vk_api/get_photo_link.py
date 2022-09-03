def get_photo_link(attachment) -> str:
    photoLink = attachment['photo']['sizes'][-1]['url']
    return photoLink
