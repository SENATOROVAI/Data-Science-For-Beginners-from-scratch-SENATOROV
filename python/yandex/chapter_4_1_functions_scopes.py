"""Functions.

Scopes. Passing parameters to functions.
"""

# +
# 1


def print_hello(name: str) -> None:
    """Return Greeting statement."""
    print(f"Hello, {name}!")


# +
# 2


def gcd(number1: int, number2: int) -> int:
    """Calculate GCD."""
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


# +
# 3


def number_length(number_input: int) -> int:
    """Return input length."""
    return len(str(abs(number_input)))


# +
# 4


def month(mn: int, lang: str) -> str | None:
    """Return month in specified locale."""
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
    return months[lang][mn - 1] if 1 <= mn <= 12 and lang in months else None


# +
# 5


def split_numbers(numbers_string: str) -> tuple[int, ...]:
    """Return tuple of split numbers."""
    return tuple(int(nmb) for nmb in numbers_string.split())


# +
# 6


outputs: list[str] = []


def modern_print(line: str) -> None:
    """Print only new lines."""
    if line not in outputs:
        outputs.append(line)
        print(line)


# +
# 7


def can_eat(knight: tuple[int, int], piece: tuple[int, int]) -> bool:
    """Determine if a knight can capture a given piece in a game of chess."""
    x1_c, y1_c = knight
    x2_c, y2_c = piece
    return (abs(x1_c - x2_c), abs(y1_c - y2_c)) in [(2, 1), (1, 2)]


# +
# 8

# fmt: off
def is_palindrome(
    value: int | str | list[int] | tuple[int, ...] | float
) -> bool:
    """Check if input value is a palindrome."""
    if isinstance(value, (int, str, list, tuple)):
        value_str = str(value) if isinstance(value, int) else value
        return value_str == value_str[::-1]
    return False
# fmt: on

# +
# 9


def is_prime(nmb: int) -> bool:
    """Check if input value is prime."""
    if nmb < 2:
        return False
    for i in range(2, int(nmb**0.5) + 1):
        if nmb % i == 0:
            return False
    return True


# +
# 10


def merge(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple[int, ...]:
    """Merge and return two tuples."""
    result = []
    i_val, j_val = 0, 0
    for _ in range(len(tuple1) + len(tuple2)):
        if i_val < len(tuple1) and (
            j_val >= len(tuple2) or tuple1[i_val] < tuple2[j_val]
        ):
            result.append(tuple1[i_val])
            i_val += 1
        else:
            result.append(tuple2[j_val])
            j_val += 1
    return tuple(result)
