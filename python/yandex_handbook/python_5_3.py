"""Yandex handbook "Python Basics" answers."""

# +
from __future__ import annotations

import hashlib
from collections import deque
from typing import Callable, Iterable


# 1
def func_1() -> None:
    """Вызывает ValueError."""
    _ = int("Hello, world!")


try:
    func_1()
except ValueError:
    pass
except TypeError:
    pass
except SystemError:
    pass
except Exception:
    pass
else:
    pass


# +
# 2
# pylint: disable=all
def unsafe_sum_2(val_1: any, val_2: any) -> int:  # type: ignore
    """Складывает два значения без проверки типов."""
    return val_1 + val_2  # type: ignore


# pylint: enable=all

try:
    unsafe_sum_2("7", None)
except Exception:
    pass


# +
# 3
# pylint: disable=all
def unsafe_concat_3(b_var: any, c_var: any, d_var: any) -> str:  # type: ignore
    """Конкатенирует три значения как строки без безопасности."""
    return "".join(map(str, (b_var, c_var, d_var)))


class ReprFails3:
    """Объект, который вызывает исключение при преобразовании в строку."""

    def __repr__(self) -> str:
        """Вызывает исключение при попытке преобразовать в строку."""
        raise Exception("Repr failure")


# pylint: enable=all

try:
    unsafe_concat_3(ReprFails3(), 3, 5)
except Exception:
    pass


# +
# 4
def only_positive_even_sum_4(
    num_1: str | int | float,
    num_2: str | int | float,
) -> int:
    """Возвращает сумму двух строго положительных четных целых чисел."""
    num_1_int = int(num_1)
    num_2_int = int(num_2)

    if not isinstance(num_1_int, int) or not isinstance(num_2_int, int):
        raise TypeError("Оба аргумента должны быть типа int")

    if num_1_int <= 0 or num_1_int % 2 != 0 or num_2_int <= 0 or num_2_int % 2 != 0:
        raise ValueError("Оба числа должны быть строго положительными и четными")

    return num_1_int + num_2_int


try:
    only_positive_even_sum_4("3", 2.5)
except Exception:
    pass


# +
# 5
def is_sorted_5(sequence: Iterable[int]) -> bool:
    """Возвращает True, если последовательность отсортирована по возрастанию."""
    iterator = iter(sequence)
    try:
        previous = next(iterator)
    except StopIteration:
        return True
    for current in iterator:
        if current < previous:
            return False
        previous = current
    return True


def validate_sequence_5(*queues: Iterable[int]) -> None:
    """Проверяет, что очереди итерируемы, отсортированы и однородны."""
    combined: list[int] = []

    for queue in queues:
        try:
            _ = iter(queue)
        except TypeError:
            raise StopIteration("Очередь не итерируема") from None

        queue_list = list(queue)

        if len(queue_list) == 1:
            raise StopIteration("Очередь должна содержать более одного элемента")

        if not is_sorted_5(queue_list):
            raise ValueError("Очередь не отсортирована")

        combined.extend(queue_list)

    if len(set(map(type, combined))) != 1:
        raise TypeError("Очереди содержат элементы разных типов")


def merge_5(queue_1: Iterable[int], queue_2: Iterable[int]) -> tuple[int, ...]:
    """Объединяет две отсортированные целочисленные очереди в один список."""
    validate_sequence_5(queue_1, queue_2)
    deque_1 = deque(queue_1)
    deque_2 = deque(queue_2)
    merged: list[int] = []

    while deque_1 and deque_2:
        if deque_1[0] <= deque_2[0]:
            merged.append(deque_1.popleft())
        else:
            merged.append(deque_2.popleft())

    merged.extend(deque_1)
    merged.extend(deque_2)
    return tuple(merged)


try:
    merge_5((35,), (1, 2, 3))
except Exception:
    pass


# +
# 6
class InfiniteSolutionsError6Error(Exception):
    """Вызывается, когда уравнение имеет бесконечное количество решений."""

    pass


class NoSolutionsError6Error(Exception):
    """Вызывается, когда уравнение не имеет действительных решений."""

    pass


def find_roots_6(
    a_squared: float,
    linear: float,
    constant: float,
) -> tuple[float, float] | float:
    """Находит корни квадратного или линейного уравнения."""
    if not all(isinstance(x, (int, float)) for x in (a_squared, linear, constant)):
        raise TypeError("Все коэффициенты должны быть int или float")

    if a_squared == linear == constant == 0:
        raise InfiniteSolutionsError6Error("Бесконечное количество решений")
    if a_squared == linear == 0:
        raise NoSolutionsError6Error("Нет решения")
    if a_squared == 0:
        root = -constant / linear
        return (root, root)
    if constant == 0 and linear == 0:
        return (0.0, 0.0)

    discriminant = linear**2 - 4 * a_squared * constant

    if discriminant < 0:
        raise NoSolutionsError6Error("Нет действительного решения")

    sqrt_discriminant = discriminant**0.5
    x1 = (-linear - sqrt_discriminant) / (2 * a_squared)
    x2 = (-linear + sqrt_discriminant) / (2 * a_squared)

    return (x1, x2) if x1 <= x2 else (x2, x1)


try:
    find_roots_6(0, 0, 1)
except Exception:
    pass


# +
# 7
class CyrillicError7Error(Exception):
    """Вызывается, когда имя содержит некириллические символы."""

    pass


class CapitalError7Error(Exception):
    """Вызывается, когда имя не начинается с заглавной буквы."""

    pass


def name_validation_7(name: str) -> str:
    """Проверяет, что имя является строкой в кириллице с заглавной буквы."""
    if not isinstance(name, str):
        raise TypeError("Ожидается строка")

    if not name.isalpha() or not all(
        "а" <= char.lower() <= "я" or char.lower() == "ё" for char in name
    ):
        raise CyrillicError7Error("Имя должно содержать только кириллические буквы")

    if not name.istitle():
        raise CapitalError7Error(
            "Имя должно начинаться с заглавной буквы и продолжаться строчными"
        )

    return name


try:
    name_validation_7("user")
except Exception:
    pass


# +
# 8
class BadCharacterError8Error(Exception):
    """Вызывается, когда имя пользователя содержит недопустимые символы."""

    pass


class StartsWithDigitError8Error(Exception):
    """Вызывается, когда имя пользователя начинается с цифры."""

    pass


def username_validation_8(username: str) -> str:
    """Проверяет, что имя пользователя содержит только допустимые компоненты."""
    valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")

    if not isinstance(username, str):
        raise TypeError("Имя пользователя должно быть строкой")

    if not all(char.lower() in valid_chars for char in username):
        raise BadCharacterError8Error("Имя пользователя содержит недопустимые символы")

    if username and username[0].isdigit():
        raise StartsWithDigitError8Error(
            "Имя пользователя не должно начинаться с цифры"
        )

    return username


try:
    username_validation_8("$user_45$")
except Exception:
    pass


# +
# 9
class UserCyrillicError9Error(Exception):
    """Вызывается, когда имя содержит некириллические символы."""

    pass


class UserCapitalError9Error(Exception):
    """Вызывается, когда имя не начинается с заглавной буквы."""

    pass


class UserBadCharacterError9Error(Exception):
    """Вызывается, когда имя пользователя содержит недопустимые символы."""

    pass


class UserStartsWithDigitError9Error(Exception):
    """Вызывается, когда имя пользователя начинается с цифры."""

    pass


def name_validation_9(name: str) -> str:
    """Проверяет, является ли имя кириллическим и с заглавной буквы."""
    valid_cyrillic_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")

    if not all(char.lower() in valid_cyrillic_chars for char in name):
        raise UserCyrillicError9Error("Имя содержит некириллические символы")

    if not name.istitle():
        raise UserCapitalError9Error("Имя должно начинаться с заглавной буквы")

    return name


def username_validation_9(username: str) -> str:
    """Проверяет, имеет ли имя пользователя допустимые символы без цифры в начале."""
    valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")

    if not isinstance(username, str):
        raise TypeError("Имя пользователя должно быть строкой")

    if not all(char.lower() in valid_chars for char in username):
        raise UserBadCharacterError9Error(
            "Имя пользователя содержит недопустимые символы"
        )

    if username and username[0].isdigit():
        raise UserStartsWithDigitError9Error(
            "Имя пользователя не должно начинаться с цифры"
        )

    return username


def user_validation_9(**kwargs: str) -> dict[str, str]:
    """Проверяет имя, фамилию и имя пользователя пользователя."""
    required_fields = {"last_name", "first_name", "username"}

    if not required_fields.issuperset(kwargs.keys()):
        raise KeyError("Неожиданные поля в данных пользователя")

    for field in required_fields:
        if field not in kwargs or kwargs[field] == "":
            raise KeyError(f"Отсутствует или пустое обязательное поле: {field}")

    name_validation_9(kwargs["last_name"])
    name_validation_9(kwargs["first_name"])
    username_validation_9(kwargs["username"])

    return kwargs


user_validation_9(last_name="Иванов", first_name="Иван", username="ivanych45")


# +
# 10
class PasswordMinLengthError10Error(Exception):
    """Вызывается, когда пароль короче минимально допустимой длины."""

    pass


class PasswordInvalidCharacterError10Error(Exception):
    """Вызывается, когда пароль содержит символы вне допустимого набора."""

    pass


class PasswordMissingRequiredCharError10Error(Exception):
    """Вызывается, когда пароль не содержит обязательный символ."""

    pass


POTENTIAL_PASSWORD_CHARS_10 = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
)


def password_validation_10(
    password: str,
    min_length: int = 8,
    allowed_chars: str = POTENTIAL_PASSWORD_CHARS_10,
    required_char_check: Callable[[str], bool] = str.isdigit,
) -> str:
    """Проверяет длину пароля, символы и обязательный символ."""
    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")

    if len(password) < min_length:
        raise PasswordMinLengthError10Error("Пароль слишком короткий")

    if any(char not in allowed_chars for char in password):
        raise PasswordInvalidCharacterError10Error(
            "Пароль содержит недопустимые символы"
        )

    if not any(required_char_check(char) for char in password):
        raise PasswordMissingRequiredCharError10Error(
            "Пароль не содержит обязательные символы (например, цифру)"
        )

    return hashlib.sha256(password.encode()).hexdigest()


password_validation_10("Hello12345")
