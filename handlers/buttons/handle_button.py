from bot import disp
from aiogram import types
from handlers.group_list.get_full_group import get_full_group
from handlers.group_list.get_sub_1 import get_sub_1
from handlers.group_list.get_sub_2 import get_sub_2
from handlers.queue.get_queue_1 import get_q_1
from handlers.queue.get_queue_2 import get_q_2
from handlers.reminder.get_reminder import get_reminder
from handlers.rights.get_access import get_access
from handlers.shiman_worktime.get_worktime import shiman_worktime
from handlers.timetable.get_timetable import get_timetable

@disp.message_handler(content_types=['text'])
async def handle_button(message: types.Message):
      stripped=message.text.strip() 
      if stripped == "*Расписание занятий":
         return await get_timetable(message)
      elif stripped == "*Список группы":
         return await get_full_group(message)
      elif stripped == "*Список первой пг":
         return await get_sub_1(message)
      elif stripped == "*Список второй пг":
         return await get_sub_2(message)
      elif stripped == "*Очередь первой пг":
         return await get_q_1(message)
      elif stripped == "*Очередь второй пг":
         return await get_q_2(message)
      elif stripped == "*Время деканата":
         return await shiman_worktime(message)
      elif stripped == "*Супер-пользователи":
         return await get_access(message)
      elif stripped == "*Напоминания":
         return await get_reminder(message)