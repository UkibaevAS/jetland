import os
import dotenv

"""
Получение списка пользователей с правом доступа к приложению
"""
dotenv.load_dotenv()
auth_user = os.getenv('USERS_ID')


async def id_verification(user_id: str) -> bool:
    """
    Проверка пользователя по id

    :param user_id
    :return: bool
    """
    if user_id in auth_user:
        return True
    return False
