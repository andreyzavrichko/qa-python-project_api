import allure
import requests

from constants import BASE_URL, CREATE_USER_URL, DELETE_USER_URL, GET_USER_URL, PATCH_USER_URL


class UserApi:

    @staticmethod
    @allure.step("Отправить запрос на создание пользователя")
    def create_user(payload: dict) -> requests.Response:
        return requests.post(BASE_URL + CREATE_USER_URL, json=payload)

    @staticmethod
    @allure.step("Отправить запрос на получение данных пользователя")
    def get_user(token: str) -> requests.Response:
        return requests.get(
            BASE_URL + GET_USER_URL,
            headers={"authorization": token}
        )

    @staticmethod
    @allure.step("Отправить запрос на обновление данных пользователя с токеном")
    def update_user(payload: dict, token: str) -> requests.Response:
        return requests.patch(
            BASE_URL + PATCH_USER_URL,
            json=payload,
            headers={"authorization": token}
        )

    @staticmethod
    @allure.step("Отправить запрос на обновление данных пользователя без токена")
    def update_user_without_auth(payload: dict) -> requests.Response:
        return requests.patch(BASE_URL + PATCH_USER_URL, json=payload)

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user(token: str) -> requests.Response:
        return requests.delete(
            BASE_URL + DELETE_USER_URL,
            headers={"Authorization": token}
        )
