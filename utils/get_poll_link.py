def get_poll_link(attachment) -> str:
    attachmentLink = 'https://vk.com/poll' + str(attachment['poll']['owner_id']) + '_' + str(attachment['poll']['id'])
    return attachmentLink
