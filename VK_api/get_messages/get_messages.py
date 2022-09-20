from VK_api.core.core import vk
from VK_api.get_messages.Classes.Dictionary import Dictionary

def get_messages()->list[dict]:
    unreaded_dialogs = vk.method('messages.getDialogs',{
        'unread':1
    })['items']
    a=0
    messages_to_handle=[]
    messages_to_transfer=[]

    for i in unreaded_dialogs:
        if(i['message'].get('chat_id')==156):
            a=i['unread']
        
            unread_messages = vk.method('messages.getHistory',{
                'count':a,
                'peer_id':2000000000+156,
            })['items']
            for i in unread_messages:
                messages_to_handle.append(Dictionary(i))
            for i in messages_to_handle:
                i.pop('date').pop('from_id').pop('id').pop('conversation_message_id').pop('important').pop('is_hidden').pop('peer_id').pop('random_id').pop('out')
                messages_to_transfer.append(i.getdict())
            print(messages_to_transfer)
            return messages_to_transfer
        else:
            continue
