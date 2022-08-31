
import config
from main import module
from listener import listener

def input_telegram():

    if (config.getCell('telegram_useProxy')):
        proxyType = str(config.getCell('p_type'))
        proxyUserInfo = str(config.getCell('p_user') +
                            ':' + config.getCell('p_password'))
        proxyData = str(config.getCell('p_host') +
                        ':' + config.getCell('p_port'))
        telebot.apihelper.proxy = {
            'http': '%s://%s@%s' % (proxyType, proxyUserInfo, proxyData),
            'https': '%s://%s@%s' % (proxyType, proxyUserInfo, proxyData)
        }

    module.bot.set_update_listener(listener)
    while True:  # Костыль на случай timeout'a
        try:
            module.bot.polling(none_stop=False)
        except:
            continue
