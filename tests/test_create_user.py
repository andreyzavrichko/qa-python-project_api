import allure

from api.auth_api import AuthApi
from api.user_api import UserApi
from data.data_generator import get_user
from data.test_data import EXISTING_USER, USER_WITH_EMPTY_FIELDS, MSG_USER_ALREADY_EXISTS, MSG_REQUIRED_FIELDS


@allure.feature("User")
@allure.story("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_unique_user(self):
        payload = get_user()
        response = UserApi.create_user(payload)
        token = AuthApi.get_token(response)

        assert response.status_code == 200
        assert response.json()["success"] is True

        if token:
            UserApi.delete_user(token)

    @allure.title("Создание пользователя, уже зарегистрированного в системе")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_duplicate_user(self):
        response = UserApi.create_user(EXISTING_USER.copy())

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_USER_ALREADY_EXISTS

    @allure.title("Создание пользователя с незаполненными обязательными полями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_empty_fields(self):
        response = UserApi.create_user(USER_WITH_EMPTY_FIELDS.copy())

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_REQUIRED_FIELDS