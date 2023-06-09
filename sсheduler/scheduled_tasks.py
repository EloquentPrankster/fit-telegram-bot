import aioschedule as sched
from VK_api.get_messages.get_messages import get_messages
from handlers.reminder.helpers.clean_reminder import clean_reminder
from handlers.reminder.helpers.notifier import notifier


def scheduled_tasks():
    sched.every().day.at('00:10').do(clean_reminder)
    sched.every().day.at('06:00').do(notifier)
    sched.every(15).seconds.do(get_messages)
