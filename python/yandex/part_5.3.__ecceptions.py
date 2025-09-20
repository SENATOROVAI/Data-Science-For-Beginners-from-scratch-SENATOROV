"""5.3 Exceptions."""

import hashlib
from typing import Any, Callable

# +
# Обработка ошибок


def func(*args, **kwargs):  # type: ignore
    """Функция."""
    print("Заглушка.")
    print(*args)
    print(*kwargs)


try:
    func()  # type: ignore
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")
else:
    print("No Exceptions")
# -

# Ломать — не строить
try:
    func("4", None)  # type: ignore
except ValueError:
    print("Ура! Ошибка!")

# +
# Ломать — не строить 2


class Empty:
    """Класс-ошибка."""

    def __repr__(self):  # type: ignore
        """Ошибка."""
        raise TypeError("Упс.")


try:
    func(Empty(), 1, 2)  # type: ignore
except TypeError:
    print("Ура! Ошибка!")

# +
# Контроль параметров


def only_positive_even_sum(object1: Any, object2: Any) -> Any:  # type: ignore
    """Сумма двух параметров."""
    if not (isinstance(object1, int) and isinstance(object2, int)):
        raise TypeError("Нужно больше intов")
    if not (object1 > 0 and not object1 % 2) or not (object2 > 0 and not object2 % 2):
        raise ValueError
    return object1 + object2


# +
# Слияние с проверкой


def merge(seq1, seq2) -> tuple:  # type: ignore
    """Слияния двух сортированных последовательностей."""
    try:
        iter(seq1)
        iter(seq2)
    except TypeError as exc:
        raise StopIteration from exc  # Исправлено: явное связывание исключений

    # Исправлено: перенос строки после оператора, а не перед ним
    cond1 = all(isinstance(i, type(seq1[0])) for i in seq1)
    cond2 = all(isinstance(i, type(seq1[0])) for i in seq2)
    if not (cond1 and cond2):
        raise TypeError

    if list(seq1) != sorted(seq1) or list(seq2) != sorted(seq2):
        raise ValueError

    merged_seq = list(seq1) + list(seq2)
    merged_seq.sort()
    return tuple(merged_seq)


# +
# Корень зла 2


class InfiniteSolutionsError(Exception):
    """Ошибка: бесконечно много решений."""


class NoSolutionsError(Exception):
    """Ошибка: нет решений."""


def find_roots(
    coef_a: float, coef_b: float, coef_c: float
) -> tuple[float, float] | float:
    """Решает квадратное уравнение ax² + bx + c = 0."""
    coefficients = (coef_a, coef_b, coef_c)
    if any(not isinstance(coeff, (int, float)) for coeff in coefficients):
        raise TypeError

    if all(coeff == 0 for coeff in coefficients):
        raise InfiniteSolutionsError

    if coef_a == 0 and coef_b == 0 and coef_c != 0:
        raise NoSolutionsError

    if coef_a != 0 and coef_b**2 < 4 * coef_a * coef_c:
        raise NoSolutionsError

    if coef_a == 0:
        return -coef_c / coef_b

    discriminant = coef_b**2 - 4 * coef_a * coef_c

    if discriminant == 0:
        root = -coef_b / (2 * coef_a)
        return (root, root)

    root1 = (-coef_b - discriminant**0.5) / (2 * coef_a)
    root2 = (-coef_b + discriminant**0.5) / (2 * coef_a)
    return (root1, root2) if root1 < root2 else (root2, root1)


# +
# Валидация имени


class CyrillicError(Exception):
    """Найдена НЕкириллица."""


class CapitalError(Exception):
    """Заглавная буква не на своём месте."""


def name_validation(name: str) -> str:
    """Валидация имени."""
    if not isinstance(name, str):
        raise TypeError

    characters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if sum((char_val.lower() not in characters) for char_val in name):
        raise CyrillicError

    if not name[0].isupper() or any(c.isupper() for c in name[1:]):
        raise CapitalError

    return name


# +
# Валидация имени пользователя


class BadCharacterError(ValueError):
    """Плохие символы."""


class StartsWithDigitError(ValueError):
    """Начало с цифры."""


def username_validation(username: str) -> str:
    """Валидация имени пользователя."""
    if not isinstance(username, str):
        raise TypeError

    characters = "0123456789_abcdefghijklmnopqrstuvwxyz"

    if sum((char_val.lower() not in characters) for char_val in username):
        raise BadCharacterError

    if username[0].isdigit():
        raise StartsWithDigitError

    return username


# +
# Валидация пользователя


def user_validation(**kwargs: str) -> dict[str, str]:
    """Validate user data."""
    required_keys = {"last_name", "first_name", "username"}

    if set(kwargs.keys()) != required_keys:
        raise KeyError

    for value in kwargs.values():
        if not isinstance(value, str):
            raise TypeError

    return {
        "last_name": name_validation(kwargs["last_name"]),
        "first_name": name_validation(kwargs["first_name"]),
        "username": username_validation(kwargs["username"]),
    }


# +
# Валидация пароля


class MinLengthError(ValueError):
    """Недостаточная длина."""


class PossibleCharError(ValueError):
    """Невалидные символы."""


class NeedCharError(ValueError):
    """Нет обязательного символа."""


letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"


def password_validation(
    password: str,
    min_length: int = 8,
    possible_chars: str = letters + digits,
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    """Валидирует пароль и возвращает хэш."""
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if any(char not in possible_chars for char in password):
        raise PossibleCharError

    if not any(at_least_one(char) for char in password):
        raise NeedCharError

    return hashlib.sha256(password.encode()).hexdigest()
