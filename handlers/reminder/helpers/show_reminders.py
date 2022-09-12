def show_reminders(reminders_from_db:list[tuple])->str:
    list_of_reminders ='Список напоминаний:\n'
    j=0
    for i in reminders_from_db:
        list_of_reminders+=f'{j+1}. '+str(i[1])+': '+i[0]+'\n'
        j+=1
    return list_of_reminders