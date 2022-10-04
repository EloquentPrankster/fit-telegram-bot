import aioschedule as shed
from VK_api.get_messages.get_messages import get_messages
from handlers.reminder.helpers.clean_reminder import clean_reminder
from handlers.reminder.helpers.notifier import notifier

def task_definition():
    shed.every().day.at('00:10').do(clean_reminder)
    shed.every().day.at('06:00').do(notifier)
    shed.every(15).seconds.do(get_messages)
