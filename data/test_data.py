# Пользователь, существующий в системе (для теста дубликата)
EXISTING_USER = {
    "email": "andrey@yandex.ru",
    "password": "password",
    "name": "andrey"
}

# Хэши реальных ингредиентов
VALID_INGREDIENT_IDS = [
    "61c0c5a71d1f82001bdaaa79",
    "609646e4dc916e00276b2870",
]

# Хэши несуществующих ингредиентов
INVALID_INGREDIENT_IDS = [
    "61c0c5a71d1f88001bdaaa79",
    "609646e4dc916e20276b2870",
]

USER_WITH_EMPTY_FIELDS = {
    "email": "",
    "password": "",
    "name": ""
}

INVALID_CREDENTIALS = {
    "email": "nonexistent_user@invalid.xx",
    "password": "wrongpassword123",
}

VALID_INGREDIENTS = {"ingredients": VALID_INGREDIENT_IDS}
INVALID_INGREDIENTS = {"ingredients": INVALID_INGREDIENT_IDS}

# Сообщения об ошибках
MSG_INVALID_CREDENTIALS = "email or password are incorrect"
MSG_USER_ALREADY_EXISTS = "User already exists"
MSG_REQUIRED_FIELDS = "Email, password and name are required fields"
MSG_NOT_AUTHORISED = "You should be authorised"
MSG_NO_INGREDIENTS = "Ingredient ids must be provided"
EXPECTED_BURGER_NAME = "Экзо-плантаго бургер"