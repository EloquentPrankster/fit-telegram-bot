import aioschedule as shed
from handlers.reminder.helpers.clean_reminder import clean_reminder
from handlers.reminder.helpers.notifier import notifier

def task_definition():
    shed.every().day.at('0:10').do(clean_reminder)
    shed.every().day.at('6:30').do(notifier)
    
