from aiogram.dispatcher.filters.state import StatesGroup, State

class AddCardState(StatesGroup):

    name = State()
    description = State()
    photo = State()

class AddAdminState(StatesGroup):

    new_user = State()