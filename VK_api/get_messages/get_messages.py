from VK_api.core.core import vk
from VK_api.get_messages.Classes.Dictionary import Dictionary
from config import VK_PEER_ID
from VK_api.transfer_messages.transfer_messages import transfer_messages
async def get_messages():
    """Get messages from vk. If there are messages, then sends them to Telegram"""
    unreaded_dialogs = vk.method('messages.getDialogs',{'unread':1})['items']
    count=0
    if(len(unreaded_dialogs)==0): return
    for i in unreaded_dialogs:
        if(i['message'].get('chat_id')==int(VK_PEER_ID)-2000000000):
            count=i['unread']
            unread_messages = vk.method('messages.getHistory',{'count':count,'peer_id':int(VK_PEER_ID),})['items']
            messages_to_handle=[Dictionary(i) for i in unread_messages]
            messages_to_transfer=[i.pop(['date','id','conversation_message_id','important','is_hidden','peer_id','random_id','out']).getdict() for i in messages_to_handle]
            vk.method('messages.markAsRead',{'peer_id':int(VK_PEER_ID),'mark_conversation_as_read':1})
            await transfer_messages(messages_to_transfer[::-1])
        else:
            continue