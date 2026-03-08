import allure
import requests

from constants import BASE_URL, AUTH_URL


class AuthApi:

    @staticmethod
    @allure.step("Отправить запрос на авторизацию")
    def login(payload: dict) -> requests.Response:
        return requests.post(BASE_URL + AUTH_URL, json=payload)

    @staticmethod
    @allure.step("Получить токен из ответа")
    def get_token(response: requests.Response) -> str:
        return response.json().get("accessToken")
