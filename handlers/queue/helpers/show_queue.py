def show_queue(list: list[tuple], subgroup: int) -> str:
    split_list = f'Очередь подгруппы №{subgroup}:\n'
    split_list += 'ФИО-Позиция\n'
    for s in list:
        split_list += f'{s[0]}-{s[2]}\n'
    return split_list
