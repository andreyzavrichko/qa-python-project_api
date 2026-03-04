import allure

from api.order_api import OrderApi
from data.data_generator import get_valid_ingredients, get_invalid_ingredients

EXPECTED_BURGER_NAME = "Экзо-плантаго бургер"


@allure.feature("Order")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа без авторизации, с ингредиентами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_without_auth_with_ingredients(self):
        payload = get_valid_ingredients()
        response = OrderApi.create_order_without_auth(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == EXPECTED_BURGER_NAME

    @allure.title("Создание заказа с авторизацией, с ингредиентами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_auth_with_ingredients(self, new_user):
        token = new_user["token"]
        payload = get_valid_ingredients()
        response = OrderApi.create_order_with_auth(payload, token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["name"] == EXPECTED_BURGER_NAME

    @allure.title("Создание заказа без ингредиентов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_without_ingredients(self):
        response = OrderApi.create_order_without_ingredients()

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверными хэшами ингредиентов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_invalid_ingredient_hashes(self):
        payload = get_invalid_ingredients()
        response = OrderApi.create_order_without_auth(payload)

        assert response.status_code == 400
