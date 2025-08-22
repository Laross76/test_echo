import requests

def test_get_request():
    """Тест для GET-запроса с параметрами."""
    url = "https://postman-echo.com/get"
    params = {
        "key1": "value1",
        "key2": "value2"
    }

    # Выполняем GET-запрос
    response = requests.get(url, params=params)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Проверяем, что параметры переданы правильно
    data = response.json()
    assert data['args'] == params


def test_post_request():
    """Тест для POST-запроса с телом запроса."""
    url = "https://postman-echo.com/post"
    payload = {
        "name": "Anna Volk",
        "age": 45
    }

    # Выполняем POST-запрос
    response = requests.post(url, json=payload)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Проверяем, что тело запроса вернулось правильно
    data = response.json()
    assert data['json'] == payload


def test_put_request():
    """Тест для PUT-запроса с телом запроса."""
    url = "https://postman-echo.com/put"
    payload = {
        "key1": "updatedValue1",
        "key2": "updatedValue2"
    }

    # Выполняем PUT-запрос
    response = requests.put(url, json=payload)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Проверяем, что тело запроса вернулось правильно
    data = response.json()
    assert data['json'] == payload


def test_delete_request():
    """Тест для DELETE-запроса с параметрами."""
    url = "https://postman-echo.com/delete"
    params = {
        "key1": "value1"
    }

    # Выполняем DELETE-запрос
    response = requests.delete(url, params=params)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Проверяем, что параметры переданы правильно
    data = response.json()
    assert data['args'] == params


def test_patch_request():
    """Тест для PATCH-запроса с телом запроса."""
    url = "https://postman-echo.com/patch"
    payload = {
        "key1": "patchedValue1",
        "key2": "patchedValue2"
    }

    # Выполняем PATCH-запрос
    response = requests.patch(url, json=payload)

    # Проверяем статус ответа
    assert response.status_code == 200

    # Проверяем, что тело запроса вернулось правильно
    data = response.json()
    assert data['json'] == payload


if __name__ == "__main__":
    # Запускаем все тесты
    test_get_request()
    test_post_request()
    test_put_request()
    test_delete_request()
    test_patch_request()

print("Все тесты пройдены успешно!")
