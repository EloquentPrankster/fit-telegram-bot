def show_group(list: list[tuple]):
    splitlist = 'Список студентов ИСИТ 3-1:\n'
    splitlist += '№-ФИО-Подгруппа\n'
    num = 1
    for student in list:
        s = student[1].split(' ')
        splitlist += f'{num}-{s[0]}\n{s[1]} {s[2]}-{student[2]}\n'
        num += 1
    return splitlist
