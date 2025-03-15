"""Python Exception Model.

Try, except, else, finally. Modules.
"""

#
# The Look Before You Leap (LBYL) approach prevents errors by checking
# conditions before execution, but it can make code more complex and harder to read.
#
# An alternative is Easier to Ask Forgiveness than Permission (EAFP),
# which executes code first and handles errors if they occur.
# This approach is commonly used in Python via exception handling.
#
# ### Standard exception hierarchy tree
#
# ```
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- EncodingWarning
#            +-- ResourceWarning
# ```
#
#
# ### Syntax
#
# ```
# try:
#     <code that may raise an exception>
# except <ExceptionClass_1>:
#     <exception handling code>
# except <ExceptionClass_2>:
#     <exception handling code>
# ...
# else:
#     <code that runs if no exceptions occur in the try block>
# finally:
#     <code that always executes>
# ```
#
#
# ### Create own exceptions
#
# ```
# class NumbersError(Exception):
#     pass
#
#
# class EvenError(NumbersError):
#     pass
#
#
# class NegativeError(NumbersError):
#     pass
#
#
# def no_even(numbers):
#     if all(x % 2 != 0 for x in numbers):
#         return True
#     raise EvenError("В списке не должно быть чётных чисел")
#
#
# def no_negative(numbers):
#     if all(x >= 0 for x in numbers):
#         return True
#     raise NegativeError("В списке не должно быть отрицательных чисел")
#
#
# def main():
#     print("Введите числа в одну строку через пробел:")
#     try:
#         numbers = [int(x) for x in input().split()]
#         if no_negative(numbers) and no_even(numbers):
#             print(f"Сумма чисел равна: {sum(numbers)}.")
#     except NumbersError as e:  # обращение к исключению как к объекту
#         print(f"Произошла ошибка: {e}.")
#     except Exception as e:
#         print(f"Произошла непредвиденная ошибка: {e}.")
#
#
# if __name__ == "__main__":
#     main()
# ```
#
# In Python, modules allow code reuse by enabling one program to import functions, classes, or variables from another.
# The if __name__ == "__main__": condition ensures that a script runs only when executed directly,
# preventing unintended execution when imported as a module.
# Modules can be imported using import module_name or from module_name import function/class.
# Avoid from module import * to prevent namespace conflicts.
#
#

# +
# 1
import hashlib
from typing import Callable


def func() -> None:
    """Raise ValueError."""
    num_val = int("Hello, world!")


try:
    func()
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")
else:
    print("No Exceptions")

# +
# 2


# pylint: disable=all
# flake8: noqa
def sum_of_two(num1, num2) -> int:  # type: ignore
    """Add two values."""
    return num1 + num2  # type: ignore


# pylint: enable=all
# flake8: enable


try:
    sum_of_two("4", None)
except ValueError as err:
    print("Ура! Ошибка!")

# +
# 3


# pylint: disable=all
# flake8: noqa
def concat_val(a_val, b_val, c_val) -> str:  # type: ignore
    """Join three strings."""
    return "".join(map(str, (a_val, b_val, c_val)))


class BadStr:
    """Bad string class."""

    def __repr__(self):  # type: ignore
        """Return string representation of BadStr."""
        raise Exception


# pylint: enable=all
# flake8: enable


try:
    concat_val(BadStr(), 1, 2)
except Exception:
    print("Ура! Ошибка!")

# +
# 4


def only_positive_even_sum(num1: int | float, num2: int | float) -> int:
    """Return sum of two positive even integers."""
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise TypeError
    if not (num1 > 0 and not num1 % 2) or not (num2 > 0 and not num2 % 2):
        raise ValueError
    return num1 + num2


# +
# 5


def merge(seq1, seq2) -> tuple:  # type: ignore
    """Merge two sorted sequences."""
    try:
        iter(seq1)
        iter(seq2)
    except TypeError:
        raise StopIteration
    if not (
        all(isinstance(i, type(seq1[0])) for i in seq1)
        and all(isinstance(i, type(seq1[0])) for i in seq2)
    ):
        raise TypeError
    if list(seq1) != sorted(seq1) or list(seq2) != sorted(seq2):
        raise ValueError
    merged_seq = list(seq1) + list(seq2)
    merged_seq.sort()
    return tuple(merged_seq)


# +
# 6


class InfiniteSolutionsError(Exception):
    """Exception raised when the equation has infinitely many solutions."""

    pass


class NoSolutionsError(Exception):
    """Exception raised when the equation has no solutions."""

    pass


def find_roots(
    coefficient_x_squared: float,
    coefficient_x: float,
    constant_term: float,
) -> tuple[float, float] | float:
    """Find the roots of a quadratic equation of the form ax² + bx + c = 0."""
    coefficients = (coefficient_x_squared, coefficient_x, constant_term)
    if any(not isinstance(coeff, (int, float)) for coeff in coefficients):
        raise TypeError

    if all(coeff == 0 for coeff in coefficients):
        raise InfiniteSolutionsError
    elif coefficient_x_squared == 0 and coefficient_x == 0 and constant_term != 0:
        raise NoSolutionsError
    elif coefficient_x**2 < 4 * coefficient_x_squared * constant_term:
        raise NoSolutionsError

    if coefficient_x_squared == 0:
        return -constant_term / coefficient_x

    discriminant = coefficient_x**2 - 4 * coefficient_x_squared * constant_term

    if discriminant == 0:
        root = -coefficient_x / (2 * coefficient_x_squared)
        return root, root
    else:
        root1 = (-coefficient_x - discriminant**0.5) / (2 * coefficient_x_squared)
        root2 = (-coefficient_x + discriminant**0.5) / (2 * coefficient_x_squared)
        return (root1, root2) if root1 < root2 else (root2, root1)


# +
# 7


class CyrillicError(ValueError):
    """Error raised when the value contains non-Cyrillic letters."""

    pass


class CapitalError(ValueError):
    """Error raised when the value does not start with a capital letter or
    contains a capital letter not at the beginning."""

    pass


def name_validation(name: str) -> str:
    """Validate a Russian name."""
    if not isinstance(name, str):
        raise TypeError

    if not name.isalpha() or not all(
        "А" <= char <= "я" or char in "Ёё" for char in name
    ):
        raise CyrillicError

    if not name[0].isupper() or any(c.isupper() for c in name[1:]):
        raise CapitalError

    return name


# +
# 8


class BadCharacterError(ValueError):
    """Error if username contains invalid characters."""

    pass


class StartsWithDigitError(ValueError):
    """Error if username starts with a digit."""

    pass


def username_validation(username: str) -> str:
    """Validate a username."""
    if not isinstance(username, str):
        raise TypeError

    characters = "0123456789_abcdefghijklmnopqrstuvwxyz"

    if sum((char_val.lower() not in characters) for char_val in username):
        raise BadCharacterError

    if username[0].isdigit():
        raise StartsWithDigitError

    return username


# +
# 9


def user_validation(**kwargs: str) -> dict[str, str]:
    """Validate user data."""
    required_keys = {"last_name", "first_name", "username"}

    if set(kwargs.keys()) != required_keys:
        raise KeyError

    for key, value in kwargs.items():
        if not isinstance(value, str):
            raise TypeError

    return {
        "last_name": name_validation(kwargs["last_name"]),
        "first_name": name_validation(kwargs["first_name"]),
        "username": username_validation(kwargs["username"]),
    }


# +
# 10


class MinLengthError(ValueError):
    """Error if password is too short."""

    pass


class PossibleCharError(ValueError):
    """Error if password contains invalid characters."""

    pass


class NeedCharError(ValueError):
    """Error if password is missing required character type."""

    pass


def password_validation(
    password: str,
    min_length: int = 8,
    possible_chars: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    """Validate a password and return its hash."""
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if any(char not in possible_chars for char in password):
        raise PossibleCharError

    if not any(at_least_one(char) for char in password):
        raise NeedCharError

    return hashlib.sha256(password.encode()).hexdigest()
