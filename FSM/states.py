from aiogram.filters.state import State, StatesGroup


class auth_user(StatesGroup):
    start = State()  # Состояние для старта
    loan_rate = State()  # Состояние для выбора эффективной ставки займа
