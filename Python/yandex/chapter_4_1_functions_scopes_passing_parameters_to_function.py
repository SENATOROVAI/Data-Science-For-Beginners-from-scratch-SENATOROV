"""Functions. Scopes. Passing parameters to a function."""

# +
# 1


def print_hello(name: str) -> None:
    """Return greeting statement."""
    print(f"Hello, {name}!")


print_hello("Ruslan")

# +
# 2


def gcd(nat_number1: int, nat_number2: int) -> int:
    """Calculate greater common divisor."""
    while nat_number2:
        nat_number1, nat_number2 = nat_number2, nat_number1 % nat_number2
    return nat_number1


result_1 = gcd(12, 45)

print(result_1)

# +
# 3


def number_length(number: int) -> int:
    """Return a length of an integer."""
    if number != 0:
        length = 0
    else:
        length = 1
    while number != 0:
        number = int(number / 10)
        length += 1
    return length


result_2 = number_length(12345)

print(result_2)

# +
# 4


def month(num: int, lang: str) -> str | None:
    """Return a name of given month."""
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

    return months[lang][num - 1]


result_3 = month(1, "en")

print(result_3)

# +
# 5


def split_numbers(string_1: str) -> tuple[int, ...]:
    """Return a tuple of integers."""
    result = []
    for number in string_1.split():
        result.append(int(number))
    return tuple(result)


result_4 = split_numbers("1 2 3 4 5")

print(result_4)

# +
# 6


records: list[str] = []


def modern_print(string_2: str) -> None:
    """Print only non-duplicate strings."""
    if string_2 not in records:
        records.append(string_2)
        print(string_2)


modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")

# +
# 7


def can_eat(knight: tuple[int, int], cell: tuple[int, int]) -> bool:
    """Check whether a knight can hit chess piece, located at the given position."""
    x_cell = knight[0] - cell[0]
    if x_cell < 0:
        x_cell = -x_cell

    y_cell = knight[1] - cell[1]
    if y_cell < 0:
        y_cell = -y_cell

    return sorted([x_cell, y_cell]) == [1, 2]


print(can_eat((5, 5), (6, 6)))

# +
# 8


def is_palindrome(test: int | str | list[int] | tuple[int, ...] | float) -> bool:
    """Check whether input data is a palindrome."""
    if isinstance(test, (int, float)):
        if test < 0:
            test = -test
        test = str(test)
    return test == test[::-1]


result_5 = is_palindrome(123)

print(result_5)

# +
# 9


def is_prime(number: int) -> bool:
    """Check if a number is a prime number."""
    if number < 2:
        return False
    for divider in range(2, int(number**0.5) + 1):
        if number % divider == 0:
            return False
    return True


result_6 = is_prime(1001459)

print(result_6)

# +
# 10


def merge(tuple_1: tuple[int, ...], tuple_2: tuple[int, ...]) -> tuple[int, ...]:
    """Return merged tuple."""
    turn_1 = list(tuple_1)
    turn_2 = list(tuple_2)
    result = []
    while turn_1 and turn_2:
        if turn_1[0] > turn_2[0]:
            result.append(turn_2.pop(0))
        else:
            result.append(turn_1.pop(0))
    result.extend(turn_1)
    result.extend(turn_2)
    return tuple(result)

result_7 = merge((1, 2), (3, 4, 5))

print(result_7)
