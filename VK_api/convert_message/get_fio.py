from VK_api.core.core import vk

def get_fio(from_id) -> str:
    user = vk.method('users.get',{'user_ids': from_id})
    fio = user[-1]['first_name'] + ' ' + user[-1]['last_name']
    return fio
