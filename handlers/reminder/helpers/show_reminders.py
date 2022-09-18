def show_reminders(reminders_from_db:list[tuple])->str:
    """Returns pretty string (list of reminders)"""
    list_of_reminders ='Список напоминаний:\n'
    j=0
    for i in reminders_from_db:
        list_of_reminders+=f'{j+1}. '+i[1].strftime('%d-%m-%Y')+': '+i[0]+'\n'
        j+=1
    return list_of_reminders