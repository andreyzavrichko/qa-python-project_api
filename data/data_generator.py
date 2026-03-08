from faker import Faker

fake = Faker()


def get_user() -> dict:
    """Случайный валидный пользователь."""
    return {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name(),
    }