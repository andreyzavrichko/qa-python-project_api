import allure

from api.auth_api import AuthApi
from api.user_api import UserApi
from data.data_generator import get_user, get_duplicate_user, get_user_with_empty_fields


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
        payload = get_duplicate_user()
        response = UserApi.create_user(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя с незаполненными обязательными полями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_empty_fields(self):
        payload = get_user_with_empty_fields()
        response = UserApi.create_user(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"
