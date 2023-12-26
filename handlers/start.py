from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import (
    CommandStart,
)
from filters.filter_id import id_verification
from keyboard.kb_auth_users import kb_choise_loan_rate

from FSM.states import auth_user

# Инициализируем роутер уровня модуля
router: Router = Router()


# Хэндлер на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    """
    Стартовое меню
    """

    user_id = message.from_user.id

    print(f'{user_id} - {message.from_user.first_name} {message.from_user.username}')

    if not await id_verification(str(user_id)):
        await message.answer(f'Доступ ограничен!')
    else:
        await message.answer(f'Привет, {message.from_user.username}!')
        await state.set_state(auth_user.start)
        await message.answer('Какая эффективная ставка интересует?',
                             reply_markup=kb_choise_loan_rate.as_markup(resize_keyboard=True))


# Хэндлер на любое сообщение, кроме команды /start
@router.message()
async def send_echo(message: Message):
    await message.reply('Используй кнопку MENU')
