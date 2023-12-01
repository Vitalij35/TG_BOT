from aiogram.dispatcher.filters.state import StatesGroup, State


class restrict(StatesGroup):
    warning = State()
    decision = State()