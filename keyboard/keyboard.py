from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

button_getgroup = KeyboardButton('*Список группы')
button_getsub1 = KeyboardButton('*Список первой подгруппы')
button_getsub2 = KeyboardButton('*Список второй подгруппы')
button_getq1 = KeyboardButton('*Очередь первой подгруппы')
button_getq2 = KeyboardButton('*Очередь второй подгруппы')
button_gett = KeyboardButton('*Расписание занятий')
button_getmind = KeyboardButton('*Время работы деканата')
button_geacc = KeyboardButton('*Список напоминаний')
button_getshiman = KeyboardButton('*Список супер-пользователей')


keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard.row(button_getgroup,button_getsub1,button_getsub2).row(button_getq1,button_getq2,button_getmind).row(button_geacc,button_getshiman,button_gett)