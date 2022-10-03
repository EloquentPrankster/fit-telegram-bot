import re
from VK_api.core.core import vk
from VK_api.get_messages.Classes.Dictionary import Dictionary
def clean_messages(raw_messages:list[dict], handled_messages:list=[],level=0)->list[dict]:
    vk_trash=['date','id','conversation_message_id','important','is_hidden','peer_id','random_id','out']
    messages_to_handle=[Dictionary(i) for i in raw_messages]
    prepared_messages = [i.pop(vk_trash).getdict() for i in messages_to_handle]
    
    for item in prepared_messages:
        item.update({'level':level})
        user = vk.method('users.get',{'user_ids': item['from_id']})
        sender = user[-1]['first_name'] + ' ' + user[-1]['last_name']
        item.update({'sender':sender})
        item.pop('from_id')

        if 'reply_message' in item:
            user = vk.method('users.get',{'user_ids': item['reply_message']['from_id']})
            item.update({'reply_to':user[-1]['first_name'] + ' ' + user[-1]['last_name']})

        attachments=[]
        for attach in item['attachments']:
            match(attach['type']):
                case "photo":
                    photo=Dictionary(attach['photo'].copy()).clear().update(
                        {
                            'type':'photo',
                            'url':attach['photo']['sizes'][-2]['url'],
                        }
                    ).getdict()
                    attachments.append(photo)

                case "poll":
                    poll=Dictionary(attach['poll'].copy()).clear().update(
                        {
                            'type':'poll',
                            'url':'https://vk.com/poll' + str(attach['poll']['owner_id']) + '_' + str(attach['poll']['id']),
                        }
                    ).getdict()
                    attachments.append(poll)

                case "doc":
                    doc=Dictionary(attach['doc'].copy()).clear().update(
                            {
                                'type':'doc',
                                'title':attach['doc']['title'],
                                'url':attach['doc']['url'],
                            }
                        ).getdict()
                    attachments.append(doc)

                case "wall":
                    wall=Dictionary(attach['wall'].copy()).clear().update(
                        {
                            'type':'wall',
                            'url':'https://vk.com/wall' + str(attach['wall']['from_id']) + '_' + str(attach['wall']['id']),
                        }
                    ).getdict()
                    attachments.append(wall)

                case "video":
                    if 'mp4_720' in attach['video']['files']: quality='mp4_720'
                    elif 'mp4_480' in attach['video']['files']: quality='mp4_480'
                    elif 'mp4_240' in attach['video']['files']: quality='mp4_240'
                    elif 'mp4_144' in attach['video']['files']: quality='mp4_144'

                    if re.match(r'.*\.mp4.*',attach['video']['files'][quality]): 
                        url=attach['video']['files'][quality]
                        attach['video'].update({'by_direct':True})
                    else: 
                        owner_id=str(attach['video']['owner_id'])
                        video_id=str(attach['video']['id'])
                        attach['video'].update({'by_direct':False})
                        url='https://vk.com/im?z=video'+owner_id+'_'+video_id
                    video=Dictionary(attach['video'].copy()).clear().update(
                        {
                            'type':'video',
                            'title':attach['video']['title'],
                            'by_direct':attach['video']['by_direct'],
                            'url':url,
                        }
                    ).getdict()
                    attachments.append(video)

                case "audio":
                    audio=Dictionary(attach['audio'].copy()).clear().update(
                        {
                            'type':'audio',
                            'artist':attach['audio']['artist'],
                            'title':attach['audio']['title'],
                            'duration':attach['audio']['duration'],
                            'url':attach['audio']['url'],
                        }
                    ).getdict()
                    attachments.append(audio)

                case "audio_message":
                    audio_message=Dictionary(attach['audio_message'].copy()).clear().update(
                        {
                            'type':'audio_message',
                            'duration':attach['audio_message']['duration'],
                            'link_ogg':attach['audio_message']['link_ogg'],
                        }
                    ).getdict()
                    attachments.append(audio_message)
                
        item.update({'attachments':attachments})   
             
        if 'fwd_messages' in item:
            poped_fwd=item.pop('fwd_messages')
            handled_messages.append(item)
            clean_messages(poped_fwd,handled_messages, level+1)
        else:
            handled_messages.append(item)
    return handled_messages