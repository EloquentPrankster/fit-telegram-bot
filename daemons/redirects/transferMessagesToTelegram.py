from daemons.main import current_time
from main import module
import config


def transferMessagesToTelegram(idd, userName, mbody, fwdList):
    # Условие выполняется в случае какого-либо события
    if userName is None:
        if mbody:
            module.bot.send_message(config.getCell('vk_' + idd), str(mbody))
        return False

    time = current_time()
    niceText = str(time + ' | ' + userName + ': ' + mbody)

    if not fwdList is None:

        forwardText = ''

        for f in fwdList[0:]:
            forwardText = forwardText + \
                str(' | ' + f.get('userName') + ':' +
                    ' ' + f.get('body') + ' \n\n')

        module.bot.send_message(config.getCell(
            'vk_' + idd), niceText + '\n\n' + forwardText)

    else:
        module.bot.send_message(config.getCell('vk_' + idd), niceText)
