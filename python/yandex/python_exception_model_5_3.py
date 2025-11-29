"""Модель исключений Python. Try, except, else, finally. Модули.

В этом параграфе вы разберётесь, как Python позволяет  обрабатывать ошибки во время
выполнения программ. Вы  узнаете, что такое исключения и как они устроены,  научитесь
использовать конструкции try, except, else  и finally, чтобы перехватывать и обрабатывать
ошибки.  Также рассмотрите два подхода к управлению ошибками и  научитесь создавать
собственные классы исключений. В  завершение вы познакомитесь с понятием модуля в Python и
узнаете, как правильно организовывать и импортировать  код в разных частях программы.
"""

# ## Обработка ошибок.
#
# - Вашему решению будет предоставлена функция func, которая не имеет параметров и результата. Однако во время её исполнения может произойти одна из ошибок: ValueError, TypeError или SystemError.
# - Вызовите её, обработайте ошибку и выведите её название.
# - Если ошибка не произойдёт, выведите сообщение "No Exceptions".

# +
import hashlib
import math
import re
import string
from collections.abc import Iterable
from numbers import Real
from typing import (  # pylint: disable=unused-import
    TYPE_CHECKING,
    Callable,
    Dict,
    Protocol,
    Tuple,
    TypeGuard,
    cast,
)

if TYPE_CHECKING:

    def func() -> None:
        """Platform-provided function: no params, no return."""


def task_1() -> None:
    """Call provided func and print exception name or 'No Exceptions'."""
    try:
        func()  # pylint: disable=used-before-assignment
        print("No Exceptions")
    except (ValueError, TypeError, SystemError) as error:
        print(error.__class__.__name__)


task_1()


# -

# ## Ломать — не строить.
#
# - Давайте немного поиграем в «багоюзеров».
# - Вашему решению будет предоставлена функция func, которая принимает два позиционных параметра и производит с ними некую математическую операцию.
# - Предложите вызов функции, который гарантированно породит ошибку внутри функции.
# - Примечание
# - Если ошибка произойдёт внутри функции, то она будет перехвачена и обработана.
# - Если же она произойдет в вашем коде, то программа будет завершена с ошибкой.


# +
def task_2() -> None:
    """Trigger an error inside func using invalid operands."""
    func_ref: object = globals()["func"]
    two_arg_func = cast(Callable[[object, object], object], func_ref)
    two_arg_func(None, None)


task_2()


# -

# ## Ломать — не строить 2.
#
# - Вашему решению будет предоставлена функция func, которая на этот раз принимает неограниченное число позиционных параметров и производит с ними некую операцию приведения типа.
# - Предложите вызов функции, который гарантированно породит ошибку внутри функции.
# - Примечание
# - Если ошибка произойдёт внутри функции, то она будет перехвачена и обработана.
# - Если же она произойдет в вашем коде, то программа будет завершена с ошибкой.


# +
class BadValue:
    """Object that raises on string or repr conversion."""

    def __str__(self) -> str:
        """Raise TypeError on str()."""
        raise TypeError("string conversion disabled")

    def __repr__(self) -> str:
        """Raise TypeError on repr()."""
        raise TypeError("repr conversion disabled")


def task_3() -> None:
    """Trigger an error inside func via type conversion."""
    bad_value = BadValue()
    func_ref: object = globals()["func"]
    three_arg_func = cast(
        Callable[[object, object, object], object],
        func_ref,
    )
    three_arg_func(bad_value, bad_value, bad_value)


task_3()


# -

# ## Контроль параметров.
#
# - апишите функцию only_positive_even_sum, которая принимает два параметра и возвращает их сумму.
# - Если один из параметров не является целым числом, то следует вызвать исключение TypeError.
# - Если один из параметров не является положительным чётным числом, то следует вызвать исключение ValueError.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


# +
def _is_positive_even(number: int) -> bool:
    """Return True if number is a positive even integer."""
    return number > 0 and number % 2 == 0


def only_positive_even_sum(first_value: int, second_value: int) -> int:
    """Return sum of two positive even ints or raise typed errors."""
    are_ints: bool = isinstance(first_value, int) and isinstance(second_value, int)
    if not are_ints:
        raise TypeError
    are_positive_even: bool = _is_positive_even(first_value) and _is_positive_even(
        second_value
    )
    if not are_positive_even:
        raise ValueError
    return first_value + second_value


# -

# ## Слияние с проверкой.
#
# - Когда-то вы уже писали функцию merge, которая производит слияние двух отсортированных кортежей.
# - Давай-те её немного переработаем.
# - Введём систему проверок:
# - если один из параметров не является итерируемым объектом, то вызовите исключение StopIteration;
# - если значения входных параметров содержат «неоднородные» данные, то вызовите исключение TypeError;
# - если один из параметров не отсортирован, то вызовите исключение ValueError.
# - Проверки следует проводить в указанном порядке.
# - Если параметры прошли все проверки, верните итерируемый объект, являющийся слиянием двух переданных.
# - Примечание
# - В решении не должно быть вызовов требуемых функций.


# +
class Ordered(Protocol):
    """Protocol for values supporting the <= operator."""

    def __le__(self, other: "Ordered") -> bool:
        """Return True if self is less than or equal to other."""


def _is_iterable(value: object) -> TypeGuard[Iterable[object]]:
    """Return True if value is iterable."""
    return isinstance(value, Iterable)


def _ensure_iterable(data: object) -> tuple[object, ...]:
    """Return data as tuple or raise StopIteration if not iterable."""
    if not _is_iterable(data):
        raise StopIteration
    return tuple(data)


def _is_homogeneous(
    values_left: tuple[object, ...],
    values_right: tuple[object, ...],
) -> bool:
    """Return True if all element types across both are the same."""
    left_types = {type(item) for item in values_left}
    right_types = {type(item) for item in values_right}
    return len(left_types | right_types) <= 1


def _is_non_decreasing(values: tuple[Ordered, ...]) -> bool:
    """Return True if sequence is sorted in non-decreasing order."""
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def merge(left: object, right: object) -> tuple[object, ...]:
    """Merge two sorted iterables with validations."""
    left_seq = _ensure_iterable(left)
    right_seq = _ensure_iterable(right)

    if not _is_homogeneous(left_seq, right_seq):
        raise TypeError

    left_ord = cast(tuple[Ordered, ...], left_seq)
    right_ord = cast(tuple[Ordered, ...], right_seq)
    if not (_is_non_decreasing(left_ord) and _is_non_decreasing(right_ord)):
        raise ValueError

    result: list[Ordered] = []
    index_left = 0
    index_right = 0
    while index_left < len(left_ord) and index_right < len(right_ord):
        if left_ord[index_left] <= right_ord[index_right]:
            result.append(left_ord[index_left])
            index_left += 1
        else:
            result.append(right_ord[index_right])
            index_right += 1

    if index_left < len(left_ord):
        result.extend(left_ord[index_left:])
    if index_right < len(right_ord):
        result.extend(right_ord[index_right:])
    return tuple(result)


# -

# ## Корень зла 2.
#
# - В одной из первых лекций вы уже решали задачу о поиске корней квадратного уравнения. Давайте модернизируем её.
# - Напишите функцию find_roots, принимающую три параметра: коэффициенты уравнения и возвращающую его корни в виде кортежа из двух значений.
# - Так же создайте два собственных исключения NoSolutionsError и InfiniteSolutionsError, которые будут вызваны в случае отсутствия и бесконечного количества решений уравнения соответственно.
# - Если переданные коэффициенты не являются рациональными числами, вызовите исключение TypeError.
# - Примечание
# - В решении не должно быть вызовов требуемых функций.


# +
class NoSolutionsError(Exception):
    """Raised when the equation has no real solutions."""


class InfiniteSolutionsError(Exception):
    """Raised when the equation has infinitely many solutions."""


def _is_real_number(value: object) -> bool:
    """Return True if value is a non-bool real number."""
    return isinstance(value, Real) and not isinstance(value, bool)


def _validate_coefficients(
    coefficient_a: object,
    coefficient_b: object,
    coefficient_c: object,
) -> None:
    """Raise TypeError if any coefficient is not a real number."""
    are_valid = all(
        (
            _is_real_number(coefficient_a),
            _is_real_number(coefficient_b),
            _is_real_number(coefficient_c),
        )
    )
    if not are_valid:
        raise TypeError


def find_roots(
    coefficient_a: Real,
    coefficient_b: Real,
    coefficient_c: Real,
) -> tuple[float, float]:
    """Return two roots for ax^2+bx+c or raise custom errors."""
    _validate_coefficients(coefficient_a, coefficient_b, coefficient_c)

    if coefficient_a == 0:
        if coefficient_b == 0:
            if coefficient_c == 0:
                raise InfiniteSolutionsError
            raise NoSolutionsError
        single_root = -float(coefficient_c) / float(coefficient_b)
        return single_root, single_root

    discriminant = float(coefficient_b) * float(coefficient_b) - 4.0 * float(
        coefficient_a
    ) * float(coefficient_c)
    if discriminant < 0.0:
        raise NoSolutionsError

    sqrt_discriminant = math.sqrt(discriminant)
    denominator = 2.0 * float(coefficient_a)
    root_first = (-float(coefficient_b) - sqrt_discriminant) / denominator
    root_second = (-float(coefficient_b) + sqrt_discriminant) / denominator
    return root_first, root_second


# -

# ## Валидация имени.
#
# - При регистрации в различных сервисах пользователи вводят большое количество информации. Правильное заполнение полей — важная часть работы программы, поэтому формы снабжают системами валидации данных.
# - Напишите функцию name_validation, которая принимает один позиционный аргумент — фамилию или имя.
# - Если параметр не является строкой, то вызовите исключение TypeError.
# - А также разработайте собственные ошибки:
# - CyrillicError — вызывается, если значение не состоит только из кириллических букв;
# - CapitalError — вызывается, если значение не начинается с заглавной буквы или найдена заглавная буква не в начале значения.
# - Обработка ошибок должна происходить в порядке, указанном в задании.
# - В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.


# +
class CyrillicError(Exception):
    """Raised when value contains non-Cyrillic characters."""


class CapitalError(Exception):
    """Raised when capitalization rules are violated."""


def name_validation(personal_name: str) -> str:
    """Validate Cyrillic-only name with proper capitalization."""
    if not isinstance(personal_name, str):
        raise TypeError

    if not re.fullmatch(r"[А-Яа-яЁё]+", personal_name):
        raise CyrillicError

    starts_with_capital: bool = personal_name[0].isupper()
    has_inner_capitals: bool = any(char.isupper() for char in personal_name[1:])
    if not starts_with_capital or has_inner_capitals:
        raise CapitalError

    return personal_name


# -

# ## Валидация имени пользователя.
#
# - Продолжим реализацию системы валидации.
# - Напишите функцию username_validation, которая принимает один позиционный аргумент — имя пользователя:
# - Если параметр не является строкой, то вызовите исключение TypeError.
# - А также разработайте собственные ошибки:
# - BadCharacterError — вызывается, если значение состоит не только из латинских букв, цифр и символа нижнего подчёркивания;
# - StartsWithDigitError — вызывается, если значение начинается с цифры.
# - Обработка ошибок должна происходить в порядке, указанном в задании.
# - В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.
# - Примечание
# - В решении не должно быть вызовов требуемых функций.


# +
class BadCharacterError(Exception):
    """Raised when username has characters outside [A-Za-z0-9_]."""


class StartsWithDigitError(Exception):
    """Raised when username starts with a digit."""


def username_validation(user_name: str) -> str:
    """Validate username by alphabet and first char rules."""
    if not isinstance(user_name, str):
        raise TypeError

    is_valid_alphabet: bool = bool(re.fullmatch(r"[A-Za-z0-9_]+", user_name))
    if not is_valid_alphabet:
        raise BadCharacterError

    starts_with_digit: bool = user_name[0].isdigit()
    if starts_with_digit:
        raise StartsWithDigitError

    return user_name


# -

# ## Валидация пользователя.
#
# - Используйте две предыдущих функции валидации и напишите функцию user_validation, которая принимает именованные аргументы:
# - last_name — фамилия;
# - first_name — имя;
# - username — имя пользователя.
# - Если функции был передан неизвестный параметр или не передан один из обязательных, то вызовите исключение KeyError.
# - Если один из параметров не является строкой, то вызовите исключение TypeError.
# - Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.
# - Если поле заполнено верно, функция возвращает словарь с данными пользователя.
# - Примечание
# - В решении не должно быть вызовов требуемых функций.


# +
def _are_strs(values: tuple[object, ...]) -> TypeGuard[tuple[str, ...]]:
    """Return True if all items are strings."""
    return all(isinstance(item, str) for item in values)


def user_validation(**user_params: object) -> dict[str, str]:
    """Validate last_name, first_name, username and return dict."""
    required_keys = {"last_name", "first_name", "username"}
    if set(user_params.keys()) != required_keys:
        raise KeyError

    values_tuple: tuple[object, object, object] = (
        user_params["last_name"],
        user_params["first_name"],
        user_params["username"],
    )
    if not _are_strs(values_tuple):
        raise TypeError

    last_name, first_name, username = values_tuple
    valid_last_name: str = name_validation(last_name)
    valid_first_name: str = name_validation(first_name)
    valid_username: str = username_validation(username)

    return {
        "last_name": valid_last_name,
        "first_name": valid_first_name,
        "username": valid_username,
    }


# -

# ## Валидация пароля.
#
# - После того, как пользователь ввёл свои данные в требуемом формате, можно позаботиться и о пароле.
# - Напишите функцию password_validation, которая принимает один позиционный параметр — пароль, и следующие именованные параметры:
# - min_length — минимальная длина пароля, по умолчанию 8;
# - possible_chars — строка символов, которые могут быть в пароле, по умолчанию латинские буквы и цифры;
# - at_least_one — функция возвращающая логическое значение, по умолчанию str.isdigit.
# - Если переданный позиционный параметр не является строкой, вызовите исключение TypeError.
# - А так же реализуйте собственные исключения:
# - MinLengthError — вызывается, если пароль меньше заданной длины;
# - PossibleCharError — вызывается, если в пароле используется недопустимый символ;
# - NeedCharError — вызывается, если в пароле не найдено ни одного обязательного символа.
# - Проверка условий должна происходить в порядке указанном в задании.
# - Так как, хороший разработчик никогда не хранит пароли в открытом виде, функция, в случае успешного завершения, возвращает хеш пароля. Для этого воспользуйтесь функцией sha256 из пакета hashlib и верните его шестнадцатеричное представление.
# - Примечание
# - В решении не должно быть вызовов требуемых функций.


# +
class MinLengthError(Exception):
    """Raised when password length is less than required."""


class PossibleCharError(Exception):
    """Raised when password contains a forbidden character."""


class NeedCharError(Exception):
    """Raised when password lacks a required character."""


DEFAULT_POSSIBLE_CHARS: str = string.ascii_letters + string.digits


def password_validation(
    password_value: str,
    *,
    min_length: int = 8,
    possible_chars: str = DEFAULT_POSSIBLE_CHARS,
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    """Validate password and return its SHA-256 hex digest."""
    if not isinstance(password_value, str):
        raise TypeError

    if len(password_value) < min_length:
        raise MinLengthError

    invalid_chars = set(password_value) - set(possible_chars)
    if invalid_chars:
        raise PossibleCharError

    has_required: bool = any(map(at_least_one, password_value))
    if not has_required:
        raise NeedCharError

    return hashlib.sha256(password_value.encode()).hexdigest()
