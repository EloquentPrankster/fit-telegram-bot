from aiogram.dispatcher.filters.state import StatesGroup, State


class StateMachine(StatesGroup):
    SET_GROUP = State()
