"""Python exception model. Try, except, else, finally. Modules."""

# +
# 1


import hashlib
from collections import deque
from typing import Callable, Iterable, List


def func() -> None:
    """Raise ValueError."""
    a_var = int("Hello, world!")  # noqa: F841


try:
    func()
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")
except Exception as e:  # noqa: F841
    print("Unexpected error: {e}")
else:
    print("No Exceptions")

# +
# 2


# pylint: disable=all
def unsafe_sum(val_1, val_2) -> int:  # type: ignore
    """Add two values without type safety."""
    return val_1 + val_2  # type: ignore


# pylint: enable=all


try:
    unsafe_sum("7", None)
except Exception:
    print("Ура! Ошибка!")

# +
# 3


# pylint: disable=all
def unsafe_concat(b_var, c_var, d_var) -> str:  # type: ignore
    """Concatenate any three values as strings, unsafely."""
    return "".join(map(str, (b_var, c_var, d_var)))


class ReprFails:
    """Object that raises exception when converted to string."""

    def __repr__(self):  # type: ignore
        """Raise an exception when attempting to convert to string."""
        raise Exception("Repr failure")


# pylint: enable=all


try:
    unsafe_concat(ReprFails(), 3, 5)
except Exception:
    print("Ура! Ошибка!")


# +
# 4

# fmt: off

def only_positive_even_sum(
    num_1: str | int | float, 
    num_2: str | int | float,
) -> int:
    """Return the sum of two strictly positive even integers."""
    num_1 = int(num_1)
    num_2 = int(num_2)

    if not isinstance(num_1, int) or not isinstance(num_2, int):
        raise TypeError("Both arguments must be of type int")

    if num_1 <= 0 or num_1 % 2 != 0 or num_2 <= 0 or num_2 % 2 != 0:
        raise ValueError("Both numbers must be strictly positive and even")

    return num_1 + num_2


print(only_positive_even_sum("3", 2.5))

# +
# 5


def is_sorted(sequence: Iterable[int]) -> bool:
    """Return True if the sequence is sorted in ascending order."""
    it = iter(sequence)
    try:
        prev = next(it)
    except StopIteration:
        return True
    for current in it:
        if current < prev:
            return False
        prev = current
    return True


def validate_sequence(*queues: Iterable[int]) -> None:
    """Validate that queues are iterable, sorted and homogeneous."""
    combined: List[int] = []

    for queue in queues:
        try:
            _ = iter(queue)
        except TypeError:
            print("StopIteration exception triggered")
            raise StopIteration("Queue is not iterable") from None

        q_list = list(queue)

        if len(q_list) == 1:
            print("StopIteration exception triggered")
            raise StopIteration("Queue must contain more than one element") from None

        if not is_sorted(q_list):
            raise ValueError("Queue is not sorted")

        combined.extend(q_list)

    if len(set(map(type, combined))) != 1:
        raise TypeError("Queues contain elements of different types")


def merge(queue_1: Iterable[int], queue_2: Iterable[int]) -> tuple[int, ...]:
    """Merge two sorted integer queues into a single sorted list."""
    validate_sequence(queue_1, queue_2)
    q1 = deque(queue_1)
    q2 = deque(queue_2)
    merged: List[int] = []

    while q1 and q2:
        merged.append(q1.popleft() if q1[0] <= q2[0] else q2.popleft())

    merged.extend(q1)
    merged.extend(q2)
    return tuple(merged)


print(*merge((35,), (1, 2, 3)))

# +
# 6


class InfiniteSolutionsError(Exception):
    """Raised when the equation has infinite solutions."""

    pass


class NoSolutionsError(Exception):
    """Raised when the equation has no real solutions."""

    pass


def find_roots(
    a_squared: float,
    linear: float,
    constant: float,
) -> tuple[float, float] | float:
    """Find roots of a quadratic or linear equation."""
    if not all(isinstance(x, (int, float)) for x in (a_squared, linear, constant)):
        raise TypeError("All coefficients must be int or float")

    if a_squared == linear == constant == 0:
        raise InfiniteSolutionsError("Infinite solutions")
    if a_squared == linear == 0:
        raise NoSolutionsError("No solution")
    if a_squared == 0:
        root = -constant / linear
        return (root, root)
    if constant == 0 and linear == 0:
        return (0.0, 0.0)

    discriminant = linear**2 - 4 * a_squared * constant

    if discriminant < 0:
        raise NoSolutionsError("No real solution")

    sqrt_disc = discriminant**0.5
    x1 = (-linear - sqrt_disc) / (2 * a_squared)
    x2 = (-linear + sqrt_disc) / (2 * a_squared)

    return (x1, x2) if x1 <= x2 else (x2, x1)


print(find_roots(0, 0, 1))

# +
# 7


class CyrillicError(Exception):
    """Raised when the name contains non-Cyrillic characters."""

    pass


class CapitalError(Exception):
    """Raised when the name does not start with a capital letter."""

    pass


def name_validation_1(name: str) -> str:
    """Validate that the name is a title-case Cyrillic string."""
    if not isinstance(name, str):
        raise TypeError("Expected a string")

    if not name.isalpha() or not all(
        "а" <= char.lower() <= "я" or char.lower() == "ё" for char in name
    ):
        raise CyrillicError("Name must contain only Cyrillic letters")

    if not name.istitle():
        raise CapitalError(
            "Name must start with a capital letter and continue with lowercase"
        )

    return name


print(name_validation_1("user"))

# +
# 8


class BadCharacterError(Exception):
    """Raised when the username contains invalid characters."""

    pass


class StartsWithDigitError(Exception):
    """Raised when the username starts with a digit."""

    pass


def username_validation_1(username: str) -> str:
    """Validate that a username contains only acceptable components."""
    valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")

    if not isinstance(username, str):
        raise TypeError("Username must be a string")

    if not all(char.lower() in valid_chars for char in username):
        raise BadCharacterError("Username contains invalid characters")

    if username and username[0].isdigit():
        raise StartsWithDigitError("Username must not start with a digit")

    return username


print(username_validation_1("$user_45$"))

# +
# 9


class UserCyrillicError(Exception):
    """Raised when a name contains non-Cyrillic characters."""

    pass


class UserCapitalError(Exception):
    """Raised when a name does not start with a capital letter."""

    pass


class UserBadCharacterError(Exception):
    """Raised when a username contains invalid characters."""

    pass


class UserStartsWithDigitError(Exception):
    """Raised when a username starts with a digit."""

    pass


def name_validation_2(name: str) -> str:
    """Check if name is Cyrillic and capitalized."""
    valid_cyrillic_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    if not all(char.lower() in valid_cyrillic_chars for char in name):
        raise UserCyrillicError("Name contains non-Cyrillic characters")

    if not name.istitle():
        raise UserCapitalError("Name must start with a capital letter")

    return name


def username_validation_2(username: str) -> str:
    """Check if username has valid characters and no leading digit."""
    valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")

    if not isinstance(username, str):
        raise TypeError("Username must be a string")

    if not all(char.lower() in valid_chars for char in username):
        raise UserBadCharacterError("Username contains invalid characters")

    if username and username[0].isdigit():
        raise UserStartsWithDigitError("Username must not start with a digit")

    return username


def user_validation(**kwargs: str) -> dict[str, str]:
    """Validate a user's first name, last name and username."""
    required_fields = {"last_name", "first_name", "username"}

    if not required_fields.issuperset(kwargs.keys()):
        raise KeyError("Unexpected field(s) in user data")

    for field in required_fields:
        if field not in kwargs or kwargs[field] == "":
            raise KeyError(f"Missing or empty required field: {field}")

    name_validation_2(kwargs["last_name"])
    name_validation_2(kwargs["first_name"])
    username_validation_2(kwargs["username"])

    return kwargs


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))

# +
# 10


class PasswordMinLengthError(Exception):
    """Raised when the password is shorter than the minimum allowed length."""

    pass


class PasswordInvalidCharacterError(Exception):
    """Raised when the password contains characters outside the allowed set."""

    pass


class PasswordMissingRequiredCharError(Exception):
    """Raised when password lacks a required character."""

    pass


POTENTIAL_PASSWORD_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
)


def password_validation(
    password: str,
    min_length: int = 8,
    allowed_chars: str = POTENTIAL_PASSWORD_CHARS,
    required_char_check: Callable[[str], bool] = str.isdigit,
) -> str:
    """Check password length, characters, and required char."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if len(password) < min_length:
        raise PasswordMinLengthError("Password is too short.")

    if any(char not in allowed_chars for char in password):
        raise PasswordInvalidCharacterError("Password contains invalid characters.")

    if not any(required_char_check(char) for char in password):
        raise PasswordMissingRequiredCharError(
            "Password lacks required characters (e.g., digit)."
        )

    return hashlib.sha256(password.encode()).hexdigest()


print(password_validation("Hello12345"))
