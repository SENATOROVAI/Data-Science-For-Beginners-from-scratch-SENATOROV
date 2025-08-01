"""Positional and named arguments. Higher-order functions. Lambda functions."""

# +
# 1


from typing import Sequence, Union


def make_list(length: int, value: int = 0) -> list[int]:
    """Return a list of given length, filled with specified value."""
    return [value for _ in range(length)]


result_1 = make_list(5, 1)

print(result_1)


# +
# 2

# fmt: off

def make_matrix(
    size: int | tuple[int, int], 
    value: int = 0
) -> list[list[int]]:
    """Return generated 2D matrix, filled with a given value."""
    if isinstance(size, int):
        rows = cols = size
    elif isinstance(size, tuple) and len(size) == 2:
        cols, rows = size
    else:
        raise ValueError("size must be int or a tuple of two integers")

    return [[value for _ in range(cols)] for _ in range(rows)]


result_2 = make_matrix((4, 2), 1)

print(result_2)

# +
# 3


def gcd(*values: int) -> int:
    """Return calculated GCD for number sequence."""
    result, *rest = values
    for current in rest:
        while current:
            result, current = current, result % current
    return result


result_3 = gcd(36, 48, 156, 100500)

print(result_3)

# +
# 4


def month(number: int, lang: str = "ru") -> str | None:
    """Return a name of a month in specified language ("ru" or "en")."""
    months = {
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
    }

    if lang in months and 1 <= number <= 12:
        return months[lang][number - 1]
    return None


result_4 = month(1, "en")

print(result_4)

# +
# 5


def to_string(
    *data: Union[int, float, str, tuple[object, ...], Sequence[object]],
    sep: str = " ",
    end: str = "\n"
) -> str:
    """Convert input data into string representation."""
    str_items = [str(item) for item in data]
    return sep.join(str_items) + end

# +
# 6


in_stock: dict[str, int] = {}


def order(*drinks: str) -> str:
    """Process an order, considering ingredients in hands."""
    recipes = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }

    for drink in drinks:
        if drink in recipes:
            required_ingredients = recipes[drink]

            sufficient = True
            for ingredient, amount in required_ingredients.items():
                if in_stock.get(ingredient, 0) < amount:
                    sufficient = False
                    break

            if sufficient:
                for ingredient, amount in required_ingredients.items():
                    in_stock[ingredient] -= amount
                return drink

    return "К сожалению, не можем предложить Вам напиток"


in_stock = {"coffee": 1, "milk": 2, "cream": 3}

print(
    order(
        "Эспрессо",
        "Капучино",
        "Макиато",
        "Кофе по-венски",
        "Латте Макиато",
        "Кон Панна",
    )
)
print(
    order(
        "Эспрессо",
        "Капучино",
        "Макиато",
        "Кофе по-венски",
        "Латте Макиато",
        "Кон Панна",
    )
)

# +
# 7


_stats = {"evens_sum": 0, "odds_sum": 0, "evens_count": 0, "odds_count": 0}


def enter_results(*numbers: int) -> None:
    """Renew a statistics on even and odd numbers."""
    global _stats  # pylint: disable=global-statement
    updated_stats = {
        "evens_sum": _stats["evens_sum"],
        "odds_sum": _stats["odds_sum"],
        "evens_count": _stats["evens_count"],
        "odds_count": _stats["odds_count"],
    }

    is_even = True

    for number in numbers:
        if is_even:
            updated_stats["evens_sum"] += number
            updated_stats["evens_count"] += 1
        else:
            updated_stats["odds_sum"] += number
            updated_stats["odds_count"] += 1
        is_even = not is_even

    _stats = updated_stats


def get_sum() -> tuple[float, ...]:
    """Return rounded sums of even and odd numbers."""
    return round(_stats["evens_sum"], 2), round(_stats["odds_sum"], 2)


def get_average() -> tuple[float, ...]:
    """Return average values for even and odd numbers."""
    even_avg = (
        _stats["evens_sum"] / _stats["evens_count"] if _stats["evens_count"] else 0.0
    )
    odd_avg = _stats["odds_sum"] / _stats["odds_count"] if _stats["odds_count"] else 0.0
    return round(even_avg, 2), round(odd_avg, 2)


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())

# +
# 8


string = "мама мыла раму"
print(sorted(string.split(), key=lambda word: (len(word), word.lower())))

# +
# 9


print(*filter(lambda nmb: not sum(map(int, str(nmb))) % 2, (1, 2, 4, 5)))

# +
# 10


def secret_replace(text: str, **code: tuple[str, ...]) -> str:
    """Substitute symbols in a text in accordance with given rules."""
    new_text = []
    replacements = {k: list(v) for k, v in code.items()}

    for char in text:
        if char in replacements:
            new_text.append(replacements[char][0])
            replacements[char] = replacements[char][1:] + [replacements[char][0]]
        else:
            new_text.append(char)

    return "".join(new_text)


result_6 = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))

print(result_6)
