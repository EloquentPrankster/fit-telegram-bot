import vk_api

from config import VK_TOKEN


def get_vk_instance():
    return vk_api.VkApi(token=VK_TOKEN)


vk = get_vk_instance()
