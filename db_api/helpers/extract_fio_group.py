def extract_fio_group(group: list[tuple]) -> list:
    splist = []
    for i in group:
        splist.append(i[1])
    return splist
