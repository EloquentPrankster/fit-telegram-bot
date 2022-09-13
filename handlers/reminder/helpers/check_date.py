from datetime import datetime
from handlers.reminder.exceptions.InvalidDate import InvalidDate

def check_date(date_from_message:str):
    try:
        input_date=datetime.strptime(date_from_message,'%d.%m.%Y')
    except ValueError:
        raise InvalidDate("Неправильно введена дата. Попробуйте ещё раз")
    today = datetime.now()
    if(input_date.date()<=today.date()): 
        raise InvalidDate('Дата меньше или равна дате настоящего дня. Введите другую дату')
    if(input_date.date().year-today.date().year>1): 
        raise InvalidDate('Максимальный интервал напоминания 1 год')