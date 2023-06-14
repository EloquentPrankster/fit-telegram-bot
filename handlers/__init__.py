from statemachine import StateMachine
from handlers import all, cancel, group_list, description, help, hate_you, queue, aliases

# Array of available handlers. h – handler, c – command name, d – description
# The array must match the pattern!

MESSAGE_HANDLERS = [
    {
        "h": [{"func": all.all, "state": "*"}],
        "c": "all",
        "d": "#Позвать всех",
    },
    {
        "h": [{"func": cancel.cancel, "state": "*"}],
        "c": "cancel",
        "d": "#Отмена команды",
    },
    {
        "h": [{"func": group_list.get_group, "state": "*"}],
        "c": "getgroup",
        "d": "@subgroup* #Вывод группы",
    },
    {
        "h": [{"func": aliases.get_aliases, "state": "*"}],
        "c": "getalias",
        "d": "#Вывести псевдонимы",
    },
    {
        "h": [
            {"func": group_list.set_group, "state": "*"},
            {"func": group_list.set_group2, "state": StateMachine.SET_GROUP},
        ],
        "c": "setgroup",
        "d": "#Запись группы",
    },
    {
        "h": [{"func": description.add_description, "state": "*"}],
        "c": "adddescr",
        "d": "@description #Добавить описание беседы",
    },
    {
        "h": [{"func": description.get_descriptions, "state": "*"}],
        "c": "getdescr",
        "d": "#Вывести описания беседы",
    },
    {
        "h": [{"func": description.del_description, "state": "*"}],
        "c": "deldescr",
        "d": "@id #Удалить описание беседы",
    },
    {
        "h": [{"func": help.help, "state": "*"}],
        "c": "help",
        "d": "#Помощь",
    },
    {
        "h": [{"func": hate_you.hate_you, "state": "*"}],
        "c": "hateyou",
        "d": "#Новая версия всем знакомой команды",
    },
    {
        "h": [{"func": queue.set_queue, "state": "*"}],
        "c": "setq",
        "d": "#Сгенерить очередь",
    },
    {
        "h": [{"func": queue.get_queue, "state": "*"}],
        "c": "getq",
        "d": "@subgroup* #Вывести очередь",
    },
    {
        "h": [{"func": aliases.bind_alias, "state": "*"}],
        "c": "bindme",
        "d": "#Привязать username",
    },
    {
        "h": [{"func": aliases.unbind_alias, "state": "*"}],
        "c": "unbindme",
        "d": "#Отвязать username",
    },
]
