def show_queue(list: list[tuple], subgroup: int) -> str:
    splitlist = f'Очередь подгруппы №{subgroup}:\n'
    splitlist += 'ФИО-Позиция\n'
    for s in list:
        splitlist += f'{s[0]}-{s[2]}\n'
    return splitlist
