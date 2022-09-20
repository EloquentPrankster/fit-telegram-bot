from VK_api.core.core import vk
from VK_api.get_messages.Classes.Dictionary import Dictionary

def get_messages()->list[dict]:
    unreaded_dialogs = vk.method('messages.getDialogs',{'unread':1})['items']
    count=0
    for i in unreaded_dialogs:
        if(i['message'].get('chat_id')==156):
            count=i['unread']
            unread_messages = vk.method('messages.getHistory',{'count':count,'peer_id':2000000000+156,})['items']
            messages_to_handle=[Dictionary(i) for i in unread_messages]
            messages_to_transfer=[i.pop(['date','from_id','id','conversation_message_id','important','is_hidden','peer_id','random_id','out']).getdict() for i in messages_to_handle]

            vk.method('messages.markAsRead',{'peer_id':2000000000+156,'mark_conversation_as_read':1})
            return messages_to_transfer[::-1]
        else:
            continue
