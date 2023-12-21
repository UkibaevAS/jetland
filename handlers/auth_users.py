from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from aiogram import F

from FSM.states import auth_user

from services.parsing import loan_parsing

# Словарь для перевода рейтинга надежности из буквенного в числовое значение
safety_rating = {
    "AAA+": 1,
    "AAA": 2,
    "AA+": 3,
    "AA": 4,
    "A+": 5,
    "A": 6,
    "BBB+": 7,
    "BBB": 8,
}

# Инициализируем роутер уровня модуля
router: Router = Router()
router.message.filter(StateFilter(auth_user.start))


# Этот хэндлер срабатывает на выбранную эффективную ставку
@router.message(F.text.in_({'20% годовых и выше',
                            '22% годовых и выше',
                            '24% годовых и выше',
                            '26% годовых и выше',
                            })
                )
async def value_capture_rate(message: Message):
    loan_rate = int(message.text[: 2])  # Получение численного значения интересующей ставки финансирования
    dct = await loan_parsing()
    count = 0
    url_exchange = f"https://jetlend.ru/invest/v3/company/"
    for i_comp in dct.get("data"):
        if i_comp.get('ytm') * 100 >= loan_rate and \
                (i_comp.get('invested_company_debt') is None or i_comp.get('invested_company_debt') < 70):
            await message.answer(f"Название займа: {i_comp.get('loan_name')},"
                                 f"\nРейтинг: {safety_rating.get(i_comp.get('rating'))},"
                                 f"\nЭффективная ставка: {round(i_comp.get('ytm') * 100, 2)}%,"
                                 f"\nОстаток по займу: {round(100 - i_comp.get('progress') * 100, 2)} руб,"
                                 f"\nКонтрактов в портфеле: {i_comp.get('invested_contracts_count')},"
                                 f"\nИнвестировано в выпуск: {i_comp.get('invested_debt')},"
                                 f"\nОстаток долга по компании: {i_comp.get('invested_company_debt')},"
                                 f"\nКупить: {url_exchange}{i_comp.get('loan_id')}/market")
            count += 1
    await message.answer(f"Найдено {count}")


# Хэндлер на любые текстовые сообщения
@router.message()
async def send_echo(message: Message):
    await message.reply('Используй кнопки ниже')
