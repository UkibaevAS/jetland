from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

kb_choise_loan_rate: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

kb_text = [
    '20% годовых и выше',
    '22% годовых и выше',
    '24% годовых и выше',
    '26% годовых и выше',
]

buttons: list[KeyboardButton] = [KeyboardButton(text=kb_text[i]) for i in range(len(kb_text))]

kb_choise_loan_rate.row(*buttons, width=1)
