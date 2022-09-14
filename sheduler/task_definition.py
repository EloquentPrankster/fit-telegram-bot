import aioschedule as shed
from handlers.reminder.helpers.notifier import notifier

def task_definition():
    shed.every().day.at('6:30').do(notifier)
    
