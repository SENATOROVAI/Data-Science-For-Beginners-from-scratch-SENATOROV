"""Yandex handbook "Python Basics" answers."""

# +
import re
from datetime import datetime
from typing import Callable, Protocol, Sequence, TypeVar

# 1


def make_list_1(length_1: int, value_1: int = 0) -> list[int]:
    """Создает список заданной длины с заданным значением."""
    result_list_1: list[int] = []
    for _ in range(length_1):
        result_list_1.append(value_1)
    return result_list_1

# +
# 2


def make_matrix_2(
    size_2: int | tuple[int, int], value_2: int = 0
) -> list[list[int]]:
    """Создает матрицу заданного размера с заданным значением."""
    m_2: int
    n_2: int
    if isinstance(size_2, tuple):
        m_2, n_2 = size_2
    else:
        m_2 = n_2 = size_2

    matrix_2: list[list[int]] = []
    for _ in range(n_2):
        row_2: list[int] = []
        for _ in range(m_2):
            row_2.append(value_2)
        matrix_2.append(row_2)
    return matrix_2

# +
# 3


def gcd_3(*values_3: int) -> int:
    """Вычисляет НОД для произвольного количества чисел."""
    numbers_3: list[int] = list(values_3)
    if not numbers_3:
        return 0
    result_3: int = numbers_3[0]
    for i_3 in range(1, len(numbers_3)):
        current_3: int = numbers_3[i_3]
        while current_3:
            result_3, current_3 = current_3, result_3 % current_3
    return result_3

# +
# 4


def month_4(number_4: int, lang_4: str = "ru") -> str:
    """Возвращает название месяца по номеру и языку."""
    months_4: dict[str, list[str]] = {
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
    return months_4[lang_4][number_4 - 1]

# +
# 5


def to_string_5(*args_5: object, sep_5: str = " ", end_5: str = "\n") -> str:
    """Преобразует аргументы в строку с разделителями."""
    parts_5: list[str] = []
    for arg_5 in args_5:
        parts_5.append(str(arg_5))
    result_5: str = sep_5.join(parts_5) + end_5
    return result_5

# +
# 6


def get_operator_6(op_6: str) -> Callable[[int, int], int]:
    """Возвращает функцию-оператор по строковому представлению."""
    operators_6: dict[str, Callable[[int, int], int]] = {
        "+": lambda x_6, y_6: x_6 + y_6,
        "-": lambda x_6, y_6: x_6 - y_6,
        "*": lambda x_6, y_6: x_6 * y_6,
        "//": lambda x_6, y_6: x_6 // y_6,
        "**": lambda x_6, y_6: x_6**y_6,
    }
    return operators_6[op_6]

# +
# 7


class FormatterProtocol(Protocol):
    """Протокол для функции форматирования."""

    def __call__(self, *args: object) -> str:
        """Форматирует переданные аргументы."""
        ...  # pylint: disable=unnecessary-ellipsis


def get_formatter_7(sep_7: str = " ", end_7: str = "") -> FormatterProtocol:
    """Возвращает функцию форматирования с заданными разделителями."""

    def formatter_7(*args_7: object) -> str:
        """Форматирует переданные аргументы."""
        parts_7: list[str] = []
        for arg_7 in args_7:
            parts_7.append(str(arg_7))
        result_7: str = sep_7.join(parts_7) + end_7
        return result_7

    return formatter_7

# +
# 8


def grow_8(*args_8: int, **kwargs_8: int) -> tuple[int, ...]:
    """Увеличивает элементы по условию."""
    result_list_8: list[int] = []
    for arg_8 in args_8:
        result_list_8.append(arg_8)
    for param_name_8, param_value_8 in kwargs_8.items():
        name_length_8: int = len(param_name_8)
        for i_8, arg_val_8 in enumerate(args_8):
            if arg_val_8 % name_length_8 == 0:
                result_list_8[i_8] += param_value_8
    return tuple(result_list_8)

# +
# 9


def product_9(*args_9: object, **kwargs_9: int) -> tuple[int, ...]:
    """Вычисляет произведение значений параметров для строк."""
    result_list_9: list[int] = []
    for arg_9 in args_9:
        if isinstance(arg_9, str):
            product_value_9: int = 1
            found_params_9: bool = False
            for param_name_9, param_value_9 in kwargs_9.items():
                if param_name_9 in arg_9:
                    product_value_9 *= param_value_9
                    found_params_9 = True
            if found_params_9:
                result_list_9.append(product_value_9)
    return tuple(result_list_9)

# +
# 10


def choice_10(
    *args_10: int, **kwargs_10: Callable[[int], int | float]
) -> int | float:
    """Применяет функцию min или max к результатам."""
    if "min" in kwargs_10:
        func_10: Callable[[int], int | float] = kwargs_10["min"]
        results_10: list[int | float] = []
        for arg_10 in args_10:
            results_10.append(func_10(arg_10))
        return min(results_10)

    if "max" in kwargs_10:
        func_10 = kwargs_10["max"]
        results_10 = []
        for arg_10 in args_10:
            results_10.append(func_10(arg_10))
        return max(results_10)

    return args_10[0] if args_10 else 0


# +
# 11
in_stock_11: dict[str, int] = {}


def order_11(*drinks_11: str) -> str:
    """Обрабатывает заказы напитков."""
    recipes_11: dict[str, dict[str, int]] = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }
    for drink_11 in drinks_11:
        if drink_11 in recipes_11:
            required_ingredients_11: dict[str, int]
            required_ingredients_11 = recipes_11[drink_11]
            sufficient_11: bool = True
            for (
                ingredient_11,
                amount_11,
            ) in required_ingredients_11.items():
                if in_stock_11.get(ingredient_11, 0) < amount_11:
                    sufficient_11 = False
                    break
            if sufficient_11:
                for (
                    ingredient_11,
                    amount_11,
                ) in required_ingredients_11.items():
                    current_amount: int
                    current_amount = in_stock_11.get(ingredient_11, 0)
                    in_stock_11[ingredient_11] = current_amount - amount_11
                return drink_11
    return "К сожалению, не можем предложить Вам напиток"


# +
# 12
numbers_12: tuple[float, ...] = ()


def enter_results_12(*args_12: float) -> None:
    """Добавляет результаты измерений."""
    global numbers_12  # pylint: disable=global-statement
    numbers_12 += args_12


def get_sum_12() -> tuple[float, float]:
    """Возвращает суммы четных и нечетных измерений."""
    sum_even_12: float = 0.0
    sum_odd_12: float = 0.0
    for i_12 in range(0, len(numbers_12), 2):
        sum_even_12 += numbers_12[i_12]
    for i_12 in range(1, len(numbers_12), 2):
        sum_odd_12 += numbers_12[i_12]
    return round(sum_even_12, 2), round(sum_odd_12, 2)


def get_average_12() -> tuple[float, float]:
    """Возвращает средние значения четных и нечетных измерений."""
    if not numbers_12:
        return (0.0, 0.0)
    sum_even_12: float
    sum_odd_12: float
    sum_even_12, sum_odd_12 = get_sum_12()
    avg_even_12: float = round(2 * sum_even_12 / len(numbers_12), 2)
    avg_odd_12: float = round(2 * sum_odd_12 / len(numbers_12), 2)
    return avg_even_12, avg_odd_12

# +
# 13


def sorter_13(x_13: str) -> tuple[int, str]:
    """Сортирует строки по длине и в нижнем регистре."""
    return (len(x_13), x_13.lower())

# +
# 14


def has_even_digit_sum_14(x_14: int) -> bool:
    """Проверяет, является ли сумма цифр числа четной."""
    total: int = 0
    for digit_char in str(x_14):
        total += int(digit_char)
    return total % 2 == 0


# +
# 15
T = TypeVar("T")


def get_repeater_15(
    func_15: Callable[[T], T], count_15: int
) -> Callable[[T], T]:
    """Возвращает функцию, применяющую func count раз."""

    def repeater_15(x_15: T) -> T:
        """Применяет функцию count_15 раз."""
        result_15: T = x_15
        for _ in range(count_15):
            result_15 = func_15(result_15)
        return result_15

    return repeater_15

# +
# 16


def login_16(
    name_16: str,
    password_16: str,
    success_16: Callable[[str], None],
    error_16: Callable[[str], None],
) -> None:
    """Проверяет логин и пароль, вызывает соответствующий callback."""
    total_16: int = 0
    for ch_16 in name_16:
        total_16 += ord(ch_16)
    val_16: int = total_16 * len(name_16)
    hex_str_16: str = f"{val_16:x}"
    if hex_str_16[::-1].lower() == password_16.lower():
        success_16(name_16)
    else:
        error_16(name_16)

# +
# 17


def has_even_int_in_list_17(item_17: tuple[str, list[object]]) -> bool:
    """Проверяет второй элемент на наличие четных целых чисел."""
    has_even_int: bool = False
    for x_17 in item_17[1]:
        if isinstance(x_17, int) and x_17 % 2 == 0:
            has_even_int = True
            break
    return has_even_int

# +
# 18


def mapper_18(item_18: tuple[str, list[object]]) -> tuple[str, int]:
    """Преобразует ключ и значение для обработки."""
    key_part: str = "".join(
        ch_18 for ch_18 in str(item_18[0]).lower() if ch_18.isalpha()
    )

    value_part: list[object] = item_18[1]
    total: int = 0
    for x_18 in value_part:
        if isinstance(x_18, (int, float)):
            total += int(x_18)

    return key_part, total

# +
# 19


def secret_replace_19(text_19: str, **kwargs_19: Sequence[str]) -> str:
    """Заменяет символы в тексте по циклической схеме."""
    result_19: str = ""
    replacements_19: dict[str, tuple[Sequence[str], int]] = {}

    for key_19, value_19 in kwargs_19.items():
        replacements_19[key_19] = (value_19, 0)

    for char_19 in text_19:
        if char_19 in replacements_19:
            replace_list_19: Sequence[str]
            index_19: int
            replace_list_19, index_19 = replacements_19[char_19]
            result_19 += replace_list_19[index_19 % len(replace_list_19)]
            replacements_19[char_19] = (replace_list_19, index_19 + 1)
        else:
            result_19 += char_19

    return result_19


# +
# 20
database_20: list[dict[str, int | str]] = []


def insert_20(*users_20: dict[str, int | str]) -> None:
    """Добавляет пользователей в базу данных."""
    database_20.extend(users_20)


def _is_date_match(
    user_date: datetime, compare_date: datetime, operator: str
) -> bool:
    """Проверяет соответствие дат по оператору."""
    comparisons = {
        ">": user_date > compare_date,
        "<": user_date < compare_date,
        ">=": user_date >= compare_date,
        "<=": user_date <= compare_date,
        "==": user_date == compare_date,
        "!=": user_date != compare_date,
    }
    return comparisons.get(operator, False)


def _is_int_match(user_id: int, compare_value: int, operator: str) -> bool:
    """Проверяет соответствие целых чисел по оператору."""
    comparisons = {
        ">": user_id > compare_value,
        "<": user_id < compare_value,
        ">=": user_id >= compare_value,
        "<=": user_id <= compare_value,
        "==": user_id == compare_value,
        "!=": user_id != compare_value,
    }
    return comparisons.get(operator, False)


def _is_str_match(user_name: str, value: str, operator: str) -> bool:
    """Проверяет соответствие строк по оператору."""
    comparisons = {
        ">": user_name > value,
        "<": user_name < value,
        ">=": user_name >= value,
        "<=": user_name <= value,
        "==": user_name == value,
        "!=": user_name != value,
    }
    return comparisons.get(operator, False)


def select_20(condition_20: str = "") -> list[dict[str, int | str]]:
    """Выбирает пользователей по условию."""
    if not condition_20:
        return sorted(database_20, key=lambda x: x["id"])

    pattern_20: str = r"(\\w+)\\s*([<>=!]+)\\s*(.+)"
    match_20: re.Match[str] | None = re.match(pattern_20, condition_20)

    if not match_20:
        return sorted(database_20, key=lambda x: x["id"])

    field_20: str = match_20.group(1)
    operator_20: str = match_20.group(2)
    value_20: str = match_20.group(3).strip()

    result_20: list[dict[str, int | str]] = []

    for user_20 in database_20:
        user_value_20: int | str = user_20[field_20]

        if field_20 == "birth":
            user_date_20: datetime = datetime.strptime(
                str(user_value_20), "%d.%m.%Y")
            compare_date_20: datetime = datetime.strptime(value_20, "%d.%m.%Y")
            if _is_date_match(user_date_20, compare_date_20, operator_20):
                result_20.append(user_20)

        elif field_20 == "id":
            user_id: int = int(user_value_20)
            compare_value_20: int = int(value_20)
            if _is_int_match(user_id, compare_value_20, operator_20):
                result_20.append(user_20)

        elif field_20 == "name":
            user_name: str = str(user_value_20)
            if _is_str_match(user_name, value_20, operator_20):
                result_20.append(user_20)

    return sorted(result_20, key=lambda x: x["id"])
