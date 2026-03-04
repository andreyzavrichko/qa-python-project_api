from faker import Faker

fake = Faker()

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


def get_user() -> dict:
    """Случайный валидный пользователь."""
    return {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name(),
    }


def get_duplicate_user() -> dict:
    """Пользователь, уже зарегистрированный в системе."""
    return EXISTING_USER.copy()


def get_user_with_empty_fields() -> dict:
    """Пользователь с пустыми обязательными полями."""
    return {"email": "", "password": "", "name": ""}


def get_invalid_credentials() -> dict:
    """Несуществующие логин и пароль."""
    return {
        "email": "nonexistent_user@invalid.xx",
        "password": "wrongpassword123",
    }


def get_valid_ingredients() -> dict:
    return {"ingredients": VALID_INGREDIENT_IDS}


def get_invalid_ingredients() -> dict:
    return {"ingredients": INVALID_INGREDIENT_IDS}
