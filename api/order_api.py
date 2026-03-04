import allure
import requests

from constants import BASE_URL, POST_ORDERS_URL, GET_ORDERS_URL


class OrderApi:

    @staticmethod
    @allure.step("Отправить запрос на создание заказа без авторизации")
    def create_order_without_auth(payload: dict) -> requests.Response:
        return requests.post(BASE_URL + POST_ORDERS_URL, json=payload)

    @staticmethod
    @allure.step("Отправить запрос на создание заказа с авторизацией")
    def create_order_with_auth(payload: dict, token: str) -> requests.Response:
        return requests.post(
            BASE_URL + POST_ORDERS_URL,
            json=payload,
            headers={"authorization": token}
        )

    @staticmethod
    @allure.step("Отправить запрос на создание заказа без ингредиентов")
    def create_order_without_ingredients(token: str = None) -> requests.Response:
        headers = {"authorization": token} if token else {}
        return requests.post(BASE_URL + POST_ORDERS_URL, json={}, headers=headers)

    @staticmethod
    @allure.step("Отправить запрос на получение заказов без авторизации")
    def get_orders_without_auth() -> requests.Response:
        return requests.get(BASE_URL + GET_ORDERS_URL)

    @staticmethod
    @allure.step("Отправить запрос на получение заказов с авторизацией")
    def get_orders_with_auth(token: str) -> requests.Response:
        return requests.get(
            BASE_URL + GET_ORDERS_URL,
            headers={"authorization": token}
        )
