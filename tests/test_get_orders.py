import allure

from api.order_api import OrderApi


@allure.feature("Order")
@allure.story("Получение заказов пользователя")
class TestGetOrders:

    @allure.title("Получение заказов — авторизованный пользователь")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_orders_authorized_user(self, new_user):
        token = new_user["token"]
        response = OrderApi.get_orders_with_auth(token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()

    @allure.title("Получение заказов — неавторизованный пользователь")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_orders_unauthorized_user(self):
        response = OrderApi.get_orders_without_auth()

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "You should be authorised"
