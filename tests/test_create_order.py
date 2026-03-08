import allure

from api.order_api import OrderApi
from data.test_data import VALID_INGREDIENTS, INVALID_INGREDIENTS, EXPECTED_BURGER_NAME, MSG_NO_INGREDIENTS


@allure.feature("Order")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа без авторизации, с ингредиентами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_without_auth_with_ingredients(self):
        response = OrderApi.create_order_without_auth(VALID_INGREDIENTS)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == EXPECTED_BURGER_NAME

    @allure.title("Создание заказа с авторизацией, с ингредиентами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_auth_with_ingredients(self, new_user):
        token = new_user["token"]
        response = OrderApi.create_order_with_auth(VALID_INGREDIENTS, token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == EXPECTED_BURGER_NAME

    @allure.title("Создание заказа без ингредиентов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_without_ingredients(self):
        response = OrderApi.create_order_without_ingredients()

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == MSG_NO_INGREDIENTS

    @allure.title("Создание заказа с неверными хэшами ингредиентов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_invalid_ingredient_hashes(self):
        response = OrderApi.create_order_without_auth(INVALID_INGREDIENTS)

        assert response.status_code == 400