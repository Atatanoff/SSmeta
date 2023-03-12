from aiogram.filters.state import State, StatesGroup



class FSMWorkEstimate(StatesGroup):
    create_est = State()
    edit_est = State()
    edit_room = State()
    num_int = State()
