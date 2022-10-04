from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

button_getgroup = KeyboardButton('*Список группы')
button_getsub1 = KeyboardButton('*Список первой пг')
button_getsub2 = KeyboardButton('*Список второй пг')
button_getq1 = KeyboardButton('*Очередь первой пг')
button_getq2 = KeyboardButton('*Очередь второй пг')
button_gett = KeyboardButton('*Расписание занятий')
button_getmind = KeyboardButton('*Время деканата')
button_geacc = KeyboardButton('*Напоминания')
button_getshiman = KeyboardButton('*Супер-пользователи')


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row(button_getgroup,button_getsub1,button_getsub2).row(button_getq1,button_getq2,button_getmind).row(button_geacc,button_getshiman,button_gett)