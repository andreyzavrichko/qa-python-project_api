import pytest

from api.auth_api import AuthApi
from api.user_api import UserApi
from data.data_generator import get_user


@pytest.fixture
def new_user():
    """
    Создаёт случайного пользователя перед тестом,
    удаляет после завершения теста.
    Возвращает кортеж (payload, token, response).
    """
    payload = get_user()
    response = UserApi.create_user(payload)
    token = AuthApi.get_token(response)

    yield {"payload": payload, "token": token, "response": response}

    if token:
        UserApi.delete_user(token)
