"""4.2 Arguments."""

import re
from datetime import datetime
from typing import Callable, Optional, TypeVar, Union

# +
# Генератор списков


def make_list(length: int, value: int = 0) -> list[int]:
    """Создает список с заданным значением."""
    return [value] * length


# +
# Генератор матриц


def make_matrix(size: int | tuple[int, int], value: int = 0) -> list[list[int]]:
    """Создает матрицу с заданным значением."""
    if isinstance(size, int):
        return [[value] * size for _ in range(size)]

    return [[value] * size[0] for _ in range(size[1])]


# +
# Функциональный нод 2.0


def gcd(*args: int) -> int:
    """Рассчитывает наибольший НОД."""
    if not args:
        return 0

    current_gcd = args[0]

    for number in args[1:]:
        number1, number2 = current_gcd, number
        while number2:
            number1, number2 = number2, number1 % number2
        current_gcd = number1

    return current_gcd


# +
# Имя of the month 2.0


def month(number: int, language: str = "ru") -> str:
    """Возвращает название месяца на нужном языке."""
    months = {
        "en": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "ru": [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь",
        ],
    }

    return months[language][number - 1]


# +
# Подготовка данных


def to_string(*args: int | float | str, sep: str = " ", end: str = "\n") -> str:
    """Формирует строку с разделителем и окончанием."""
    return sep.join(map(str, args)) + end


# +
# Арифметический помощник


def get_operator(oper: str) -> Callable[[int, int], int]:
    """Возвращается функция с нужной операцией."""
    if oper == "+":
        return lambda number1, number2: number1 + number2
    if oper == "-":
        return lambda number1, number2: number1 - number2
    if oper == "*":
        return lambda number1, number2: number1 * number2
    if oper == "//":
        return lambda number1, number2: number1 // number2
    return lambda number1, number2: number1**number2


# +
# Подготовитель данных


def get_formatter(sep: str = " ", end: str = "") -> Callable[[tuple[int, str]], str]:
    """Возвращает функцию для формирования строки."""
    return lambda *args: sep.join(map(str, args)) + end


# +
# Странный рост


def grow(*args: int, **kwargs: int) -> tuple[int, ...]:
    """Преобразует полученные значения согласно параметрам."""
    res_values = []
    for value in args:
        new_value = value
        for name, add_value in kwargs.items():
            remainder = value % len(name)
            if remainder == 0:
                new_value += add_value

        res_values.append(new_value)

    return tuple(res_values)


# +
# Странное произведение


def product(*args: str, **kwargs: int) -> tuple[int, ...]:
    """Выполняет странное произведение."""
    hash_table: dict[str, int] = {symbol: value for symbol, value in kwargs.items()}

    res_values = []
    for text in args:
        is_find_symbol = False
        res_value = 1
        for symbol in set(text):
            if symbol in hash_table:
                is_find_symbol = True
                res_value *= hash_table[symbol]

        if is_find_symbol:
            res_values.append(res_value)

    return tuple(res_values)


# +
# Наилучший выбор


def choice(*args: int, **kwargs: Callable[[int], int]) -> int:
    """Применяет функцию и находит макс или мин."""
    if "max" in kwargs:
        return max(map(kwargs["max"], args))

    return min(map(kwargs["min"], args))


# +
# Кофейня


def order(*prefers_user: str) -> str:
    """Находит кофе для приготовления."""
    recipes = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }
    for prefer_user in prefers_user:
        need_products = recipes[prefer_user]
        for need_product, count in need_products.items():
            if count > in_stock[need_product]:
                break
        else:
            for need_product, count in need_products.items():
                in_stock[need_product] -= count
            return prefer_user

    return "К сожалению, не можем предложить Вам напиток"


in_stock: dict[str, int] = {"coffee": 4, "milk": 4, "cream": 0}

# +
# В эфире рубрика «Эксперименты»
first_numbers: list[int | float] = []
second_numbers: list[int | float] = []


def enter_results(*args: int | float) -> None:
    """Заполняет списки."""
    first_numbers.extend(args[::2])
    second_numbers.extend(args[1::2])


def get_sum() -> tuple[int | float, int | float]:
    """Находит суммы элементов списков."""
    return sum(first_numbers), sum(second_numbers)


def get_average() -> tuple[float, float]:
    """Находит средние значения списков."""
    return (
        round(sum(first_numbers) / len(first_numbers), 2),
        round(sum(second_numbers) / len(second_numbers), 2),
    )


# -

# # Длинная сортировка
# lambda element: (len(element), element.lower())

# # Чётная фильтрация
# lambda number: sum(map(int, list(str(number)))) % 2 == 0

# +
# Повторюшка


def get_repeater(func: Callable[[int], int], count: int) -> Callable[[int], int]:
    """Выполняет count раз функцию."""

    def wrapper(number: int) -> int:
        """Функция-повторялка."""
        for _ in range(count):
            number = func(number)

        return number

    return wrapper


# +
# Обратная связь


def login(
    username: str,
    password: str,
    success: Callable[[str], None],
    failure: Callable[[str], None],
) -> None:
    """Вход в аккаунт."""
    reverse_password = hex(sum(ord(symbol) for symbol in username) * len(username))[2:]

    if reverse_password[::-1].lower() == password.lower():
        success(username)
    else:
        failure(username)


# -

# # Фильтрация словаря
# lambda di: any([isinstance(value, int) and value % 2 == 0 for value in di[1]]) if isinstance(di[1], list) else False

# # Преобразование словаря
# lambda di: (
#     "".join(filter(lambda sym: sym.isalpha(), di[0])).lower(),
#     sum(di[1]) if isinstance(di[1], (list, tuple, set)) else di[1],
# )

# +
# Ключевой секрет


def secret_replace(text: str, **kwargs: tuple[str, str]) -> str:
    """Шифрует текст."""
    for symbol, ciphers in kwargs.items():
        index = 0
        while symbol in text:
            text = text.replace(symbol, ciphers[index], 1)
            index += 1
            if index >= len(ciphers):
                index = 0

    return text


# +
# Глобальная "база данных" - список пользователей
database: list[dict[str, Union[int, str]]] = []

# Типовые переменные для generic функции сравнения
T = TypeVar("T", int, str, datetime)


def insert(*users: dict[str, Union[int, str]]) -> None:
    """Добавление одного или нескольких пользователей в базу данных."""
    for user in users:
        database.append(user)


def select(condition: Optional[str] = None) -> list[dict[str, Union[int, str]]]:
    """Выборка пользователей из базы данных с возможностью фильтрации."""
    # Если условие не задано, возвращаем всех пользователей
    if condition is None:
        return sorted(database, key=lambda x: x["id"])

    # Парсим условие с помощью регулярного выражения
    pattern = r"(\w+)\s*([<>=!]+)\s*(.+)"
    match = re.match(pattern, condition)

    if not match:
        raise ValueError("Неверный формат условия")

    field, operator, value = match.groups()
    value = value.strip()

    # Фильтруем пользователей
    filtered_users: list[dict[str, Union[int, str]]] = []

    for user in database:
        if field not in user:
            continue

        user_field_value = user[field]

        # Сравнение в зависимости от типа поля
        result = False
        if field == "id":
            # Для id сравниваем как числа
            result = _is_condition_met(int(user_field_value), operator, int(value))
        elif field == "name":
            # Для имени сравниваем как строки
            result = _is_condition_met(str(user_field_value), operator, str(value))
        elif field == "birth":
            # Для даты рождения преобразуем в datetime для сравнения
            user_date = datetime.strptime(str(user_field_value), "%d.%m.%Y")
            compare_date = datetime.strptime(value, "%d.%m.%Y")
            result = _is_condition_met(user_date, operator, compare_date)

        if result:
            filtered_users.append(user)

    # Возвращаем отсортированный по id список
    return sorted(filtered_users, key=lambda x: x["id"])


def _is_condition_met(user_value: T, operator: str, compare_value: T) -> bool:
    """Проверяет, соответствует ли значение пользователя заданному условию."""
    operations: dict[str, Callable[[T, T], bool]] = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        "<": lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
        ">": lambda x, y: x > y,
        ">=": lambda x, y: x >= y,
    }

    operation_func = operations.get(operator)
    if operation_func is None:
        return False

    return operation_func(user_value, compare_value)
