"""Модуль requests."""

# +
from __future__ import annotations

import json
from json.decoder import JSONDecodeError

from requests import delete, get, post, put
from requests.models import Response


# -

# 1
def api_greeting_1() -> str:
    """Возвращает приветственное сообщение от сервера."""
    response: Response = get("http://127.0.0.1:5000/")
    answer: str = response.content.decode("utf-8")
    return answer


# 2
def sum_numbers_until_zero_2(address: str) -> int:
    """Суммирует числа от сервера до получения нуля."""
    total: int = 0
    while True:
        response: Response = get(f"http://{address}/")
        number: int = int(response.content.decode("utf-8"))
        if number == 0:
            break
        total += number
    return total


# 3
def sum_integers_from_json_3(address: str) -> int:
    """Суммирует целые числа из JSON ответа сервера."""
    response: Response = get(f"http://{address}/")
    data: list[int | str] = response.json()
    numbers: list[int] = [x for x in data if isinstance(x, int)]
    return sum(numbers)


# 4
def get_value_by_key_4(address: str, key: str) -> str:
    """Возвращает значение по ключу из JSON ответа сервера."""
    response: Response = get(f"http://{address}/")
    data: dict[str, int | str] = response.json()
    return str(data.get(key, "No data"))


# 5
def sum_numbers_from_paths_5(address: str, paths: list[str]) -> int:
    """Суммирует числа из всех указанных путей на сервере."""
    all_numbers: list[int] = []
    for path in paths:
        url: str = f"http://{address}{path}"
        data: list[int] = get(url).json()
        all_numbers.extend(data)
    return sum(all_numbers)


# 6
def get_sorted_full_names_6(address: str) -> list[str]:
    """Возвращает отсортированный список полных имен пользователей."""
    url: str = f"http://{address}/users/"
    response: Response = get(url)
    users: list[dict[str, str]] = response.json()
    full_names: list[str] = [
        f"{user['last_name']} {user['first_name']}" for user in users
    ]
    full_names.sort()
    return full_names


# 7
def format_user_message_7(address: str, user_id: str, message_lines: list[str]) -> str:
    """Форматирует сообщение для пользователя с подстановкой данных."""
    url: str = f"http://{address}/users/{user_id}"
    response: Response = get(url)

    if response.status_code == 404:
        return "Пользователь не найден"

    try:
        user: dict[str, str] = response.json()
        message_template: str = "\n".join(message_lines)
        formatted_message: str = message_template.format(**user)
        return formatted_message
    except JSONDecodeError:
        return "Ошибка при декодировании JSON"


# 8
def add_user_get_list_8(
    address: str, username: str, last_name: str, first_name: str, email: str
) -> str:
    """Добавляет пользователя и возвращает обновленный список."""
    user_data: dict[str, str] = {
        "username": username,
        "last_name": last_name,
        "first_name": first_name,
        "email": email,
    }

    url: str = f"http://{address}/users/"
    response_post: Response = post(url, json=user_data)

    if response_post.status_code == 201:
        response_get: Response = get(url)
        if response_get.status_code == 200:
            users: list[dict[str, str]] = response_get.json()
            return json.dumps(users, ensure_ascii=False, indent=4)
        return f"Ошибка при получении списка пользователей: {response_get.status_code}"
    return f"Ошибка при добавлении пользователя: {response_post.status_code}"


# 9
def update_user_get_list_9(
    address: str, user_id: str, user_updates: dict[str, str]
) -> str:
    """Обновляет пользователя и возвращает обновленный список."""
    url: str = f"http://{address}/users/{user_id}"
    response_put: Response = put(url, json=user_updates)

    if response_put.status_code == 200:
        response_get: Response = get(f"http://{address}/users/")
        if response_get.status_code == 200:
            users: list[dict[str, str]] = response_get.json()
            return json.dumps(users, ensure_ascii=False, indent=4)
        return f"Ошибка при получении списка пользователей: {response_get.status_code}"
    return f"Ошибка при обновлении пользователя: {response_put.status_code}"


# 10
def delete_user_get_list_10(address: str, user_id: str) -> str:
    """Удаляет пользователя и возвращает обновленный список."""
    url: str = f"http://{address}/users/{user_id}"
    response_del: Response = delete(url)

    if response_del.status_code == 204:
        response_get: Response = get(f"http://{address}/users/")
        if response_get.status_code == 200:
            users: list[dict[str, str]] = response_get.json()
            return json.dumps(users, ensure_ascii=False, indent=4)
        return f"Ошибка при получении списка пользователей: {response_get.status_code}"
    return f"Ошибка при удалении пользователя: {response_del.status_code}"
