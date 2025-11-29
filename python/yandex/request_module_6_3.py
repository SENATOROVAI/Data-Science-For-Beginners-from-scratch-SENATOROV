"""Модуль requests.

Мы познакомимся с модулем requests — одним из самых  популярных инструментов для работы с
интернет-запросами    в Python. Вы узнаете, как отправлять HTTP-запросы    (GET, POST и
другие), обрабатывать ответы сервера, а    также как получать данные от внешних API-
сервисов. На примерах Яндекс Карт и Яндекс Диска вы увидите, как подключаться к API,
передавать параметры, получать изображения и сохранять файлы. Кроме того, мы поговорим о
ключевых понятиях: протокол HTTP, коды состояния, структура запросов и принципы
авторизации через OAuth 2.0.
"""

# ## Проверка системы.
#
# - В локальной сети тестирующей системы работает сервер 127.0.0.1. Он слушает порт 5000 и отвечает на запросы.
# - Обратитесь к серверу и выведите сообщение, полученное от него.
# - Примечания
# - Во всех задачах данной главы используется протокол http
# - Не забудьте, что ответ сервера является бинарным объектом и его следует декодировать.

# +
import json
from json.decoder import JSONDecodeError

from requests import Response, delete, get, post, put

response: Response = get("http://127.0.0.1:5000/")
answer: str = response.content.decode("utf-8")
print(answer)
# -

# ## Суммирование ответов.
#
# - Напишите программу, которая суммирует данные, передаваемые с сервера.
# - Если сервер передал число 0, значит, данные закончились и он перезапустит выдачу ответов.
# - Формат ввода
# - Вводится адрес сервера.
# - Формат вывода
# - Одно число — сумма всех данных, полученных с сервера.

# +
address7: str = input().strip()
total: int = 0

while (num := int(get(f"http://{address7}/").text)) != 0:
    total += num

print(total)
# -

# ## Суммирование ответов 2.
#
# - Сервер отвечает на запрос JSON списком.
# - Выведите сумму чисел в полученном списке.
# - Формат ввода
# - Вводится адрес сервера
# - Формат вывода
# - Одно число — сумма всех чисел в полученном списке.

print(sum(x for x in get(f"http://{input().strip()}/").json() if isinstance(x, int)))


# ## Конкретное значение.
#
# - Сервер отвечает на запрос JSON объект.
# - Выведите значение, находящееся в объекте по заданному ключу.
# - Если такое значение не обнаружено, то выведите сообщение «No data».
# - Формат ввода
# - В первой строке вводится адрес сервера. Во второй строке — имя ключа.
# - Формат вывода
# - Одна строка — значение, полученное по заданному ключу, или сообщение «No data».


def specific_meaning(address3: str, key: str) -> str:
    """Возвращает значение по ключу из JSON ответа сервера."""
    response2: Response = get(f"http://{address3}/")
    data: dict[str, int | str] = response2.json()
    return str(data.get(key, "No data"))


# ## Суммирование ответов 3.
#
# - Сервер отвечает на несколько путей, каждый из которых возвращает свой JSON список.
# - Напишите программу, которая произведёт сбор и суммирование всех данных по заданным путям.
# - Формат ввода
# - Вводится адрес сервера и список анализируемых путей.
# - Формат вывода
# - Одно число — сумма всех чисел из полученных списков.


def sum_numbers_3(address4: str, paths: list[str]) -> int:
    """Суммирует числа из всех указанных путей на сервере."""
    all_numbers: list[int] = []
    for path in paths:
        url: str = f"http://{address4}{path}"
        data: list[int] = get(url).json()
        all_numbers.extend(data)
    return sum(all_numbers)


# ## Список пользователей.
#
# - На сервере по пути /users, доступен список пользователей, представленных JSON объектами с ключами:
# - id — уникальный идентификатор пользователя;
# - username — имя пользователя;
# - last_name — фамилия;
# - first_name — имя;
# - email — адрес электронной почты.
# - Формат ввода
# - В первой строке вводится адрес сервера.
# - Формат вывода
# - Выведите список всех пользователей системы в алфавитном порядке.


def get_sorted(address5: str) -> list[str]:
    """Возвращает отсортированный список полных имен пользователей."""
    url: str = f"http://{address5}/users/"
    response3: Response = get(url)
    users: list[dict[str, str]] = response3.json()
    full_names: list[str] = [
        f"{user['last_name']} {user['first_name']}" for user in users
    ]
    full_names.sort()
    return full_names


# ## Рассылка сообщений.
#
# - Продолжим работу с сервером из прошлой задачи. По пути /users/<id> доступен JSON объект пользователя с заданным id.
# - Подготовьте текст письма для отправки важной рассылки.
# - Если пользователь с заданным идентификатором не найден, выведите сообщение «Пользователь не найден».
# - Формат ввода
# - В первой строке вводится адрес сервера.
# - Во второй строке вводится id пользователя, которому требуется отправить письмо.
# - В последующих строках записано содержание сообщения с форматированными вставками любого из полей объекта.
# - Формат вывода
# - Выведите подготовленное сообщение.


def format_user_message(address6: str, user_id: str, message_lines: list[str]) -> str:
    """Форматирует сообщение для пользователя с подстановкой данных."""
    url: str = f"http://{address6}/users/{user_id}"
    response4: Response = get(url)

    if response4.status_code == 404:
        return "Пользователь не найден"

    try:
        user: dict[str, str] = response4.json()
        message_template: str = "\n".join(message_lines)
        formatted_message: str = message_template.format(**user)
        return formatted_message
    except JSONDecodeError:
        return "Ошибка при декодировании JSON"


# ## Регистрация нового пользователя.
#
# - Продолжим работу с сервером из прошлых задач. При POST запросе по пути /users доступна возможность создания новых пользователей. Для этого в данные запроса (data) требуется передать JSON объект с информацией о пользователе (без указания идентификатора).
# - Напишите программу, которая добавляет нового пользователя в систему.
# - Формат ввода
# - В первой строке вводится адрес сервера.
# - В следующих строках вводятся: имя пользователя, фамилия, имя и адрес электронной почты.
# - Формат вывода
# - Ничего выводить не требуется.


def user_get_list(
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


# ## Изменение данных.
#
# - Продолжим работу с сервером из прошлых задач. При PUT запросе по пути /users/<id> доступна возможность изменение информации о пользователе. Для этого в данные запроса (data) требуется передать JSON объект с новой информацией (без указания идентификатора).
# - Напишите программу, которая изменяет информацию о пользователе.
# - Формат ввода
# - В первой строке вводится адрес сервера.
# - Во второй строке записан идентификатор пользователя, информацию о котором требуется изменить. В следующих строках вводятся данные для изменения в формате: <название поля>=<новое значение>.
# - Формат вывода
# - Ничего выводить не требуется.


def update_user_get_list(
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


# ## Удаление данных.
#
# - Завершим эпопею с сервером из прошлых задач. При DELETE запросе по пути /users/<id> производится удаление пользователя с заданным идентификатором.
# - Напишите программу, которая удаляет пользователя из системы.
# - Формат ввода
# - В первой строке вводится адрес сервера.
# - Во второй строке записан идентификатор пользователя, информацию о котором требуется удалить.
# - Формат вывода
# - Ничего выводить не требуется.


def delete_user_get_list(address: str, user_id: str) -> str:
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
