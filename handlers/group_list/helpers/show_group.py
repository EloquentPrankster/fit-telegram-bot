from config import GROUP


def show_group(group_list: list[tuple]):
    split_list = f'Список студентов {GROUP}:\n'
    split_list += '№-ФИО-Подгруппа\n'
    num = 1
    for student in group_list:
        s = student[1].split(' ')
        split_list += f'{num}-{s[0]}\n{s[1]} {s[2]}-{student[2]}\n'
        num += 1
    return split_list
