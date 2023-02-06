from VK_api.clean_messages.clean_messages import clean_messages
from VK_api.core.core import vk
from VK_api.transfer_messages.transfer_messages import transfer_messages
from config import VK_PEER_ID


async def get_messages():
    """Get messages from vk. If there are messages, then sends them to Telegram"""
    unreaded_dialogs: list[dict] = vk.method('messages.getDialogs', {'unread': 1})['items']
    count = 0
    if len(unreaded_dialogs) == 0: return
    for i in unreaded_dialogs:
        if i['message'].get('chat_id') == int(VK_PEER_ID) - 2000000000:
            count = i['unread']
            unhandled_messages: list[dict] = \
                vk.method('messages.getHistory', {'count': count, 'peer_id': int(VK_PEER_ID)})['items']
            vk.method('messages.markAsRead', {'peer_id': int(VK_PEER_ID), 'mark_conversation_as_read': 1})
            unhandled_messages = unhandled_messages[::-1]
            handled_messages = clean_messages(unhandled_messages, [], 0)
            await transfer_messages(handled_messages)
        else:
            continue
