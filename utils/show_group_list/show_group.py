def show_group(list: list[tuple]):
    splitlist = 'Список студентов ИСИТ 3-1:\n'
    splitlist += '№|ФИО|Подгруппа\n'
    num = 1
    for student in list:
        splitlist += f'{num}|{student[1]}|{student[2]}\n'
        num += 1
    return splitlist
