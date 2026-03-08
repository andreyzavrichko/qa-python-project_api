import allure

from api.auth_api import AuthApi
from data.test_data import INVALID_CREDENTIALS, MSG_INVALID_CREDENTIALS


@allure.feature("Auth")
@allure.story("Авторизация пользователя")
class TestAuthUser:

    @allure.title("Логин под существующим пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid_user(self, new_user):
        payload = new_user["payload"]
        credentials = {"email": payload["email"], "password": payload["password"]}
        response = AuthApi.login(credentials)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_invalid_credentials(self):
        response = AuthApi.login(INVALID_CREDENTIALS)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_INVALID_CREDENTIALS
