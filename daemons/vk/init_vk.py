import vk_api
import config
from daemons.vk.input_vk import input_vk
from main import module
import auth_handler
import captcha_handler


def init_vk():

    login = config.getCell('vk_login')
    password = config.getCell('vk_password')
    app = config.getCell('app_id')

    print("login in vk as: " + login)

    global vk_session

    vk_session = vk_api.VkApi(login, password, app_id=app,
                              auth_handler=auth_handler, captcha_handler=captcha_handler)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    module.vk = vk_session.get_api()  # Важная штука

    input_vk()
