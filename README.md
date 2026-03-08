# Stellar Burgers — API Tests

Автотесты REST API сервиса Stellar Burgers на Python.

## Стек

| Инструмент    | Назначение                |
|---------------|---------------------------|
| pytest        | Фреймворк тестирования    |
| requests      | HTTP-клиент               |
| allure-pytest | Отчётность                |
| Faker         | Генерация тестовых данных |

## Структура проекта

```
stellar_burgers_api/
├── api/                 
│   ├── auth_api.py
│   ├── user_api.py
│   └── order_api.py
├── data/
│   └── data_generator.py 
├── tests/                
│   ├── test_create_user.py
│   ├── test_auth_user.py
│   ├── test_change_user.py
│   ├── test_create_order.py
│   └── test_get_orders.py
├── conftest.py          
├── constants.py         
├── pytest.ini
└── requirements.txt
```

## Установка

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest
```

## Генерация Allure-отчёта

```bash
# Запуск с формированием результатов
pytest --alluredir=allure-results

# Открыть отчёт
allure serve allure-results
```
