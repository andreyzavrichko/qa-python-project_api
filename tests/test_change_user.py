import allure

from api.user_api import UserApi
from data.data_generator import get_user
from data.test_data import MSG_NOT_AUTHORISED


@allure.feature("User")
@allure.story("Редактирование данных пользователя")
class TestChangeUser:

    @allure.title("Получение данных пользователя с авторизацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_with_auth(self, new_user):
        payload = new_user["payload"]
        token = new_user["token"]

        response = UserApi.get_user(token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == payload["email"]
        assert response.json()["user"]["name"] == payload["name"]

    @allure.title("Изменение email пользователя с авторизацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_email_with_auth(self, new_user):
        token = new_user["token"]
        new_data = get_user()

        response = UserApi.update_user({"email": new_data["email"]}, token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == new_data["email"]

    @allure.title("Изменение имени пользователя с авторизацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_name_with_auth(self, new_user):
        token = new_user["token"]
        new_data = get_user()

        response = UserApi.update_user({"name": new_data["name"]}, token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == new_data["name"]

    @allure.title("Изменение пароля пользователя с авторизацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_password_with_auth(self, new_user):
        token = new_user["token"]
        new_data = get_user()

        response = UserApi.update_user({"password": new_data["password"]}, token)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Изменение email пользователя без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_email_without_auth(self):
        new_data = get_user()

        response = UserApi.update_user_without_auth({"email": new_data["email"]})

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_NOT_AUTHORISED

    @allure.title("Изменение имени пользователя без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_name_without_auth(self):
        new_data = get_user()

        response = UserApi.update_user_without_auth({"name": new_data["name"]})

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_NOT_AUTHORISED

    @allure.title("Изменение пароля пользователя без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_change_password_without_auth(self):
        new_data = get_user()

        response = UserApi.update_user_without_auth({"password": new_data["password"]})

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_NOT_AUTHORISED