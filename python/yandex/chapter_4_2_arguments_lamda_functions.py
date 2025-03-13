"""Positional and named arguments.

Higher-order functions. Lambda functions.
"""

# +
# 1


def make_list(length: int, value: int = 0) -> list[int]:
    """Create a list with specified length."""
    return [value] * length


# +
# 2


def make_matrix(sz: int | tuple[int, int], vl: int = 0) -> list[list[int]]:
    """Create a 2D matrix filled with a specified value."""
    if isinstance(sz, tuple):
        rows = [vl for _ in range(sz[0])]
        print(rows)
        return [rows for _ in range(sz[1])]
    return [[vl for _ in range(sz)] for _ in range(sz)]


# +
# 3


def gcd(*args: int) -> int:
    """Calculate GCD for a number sequence."""
    if not args:
        return 0

    current_gcd = args[0]

    for num in args[1:]:
        num_1, num_2 = current_gcd, num
        while num_2:
            num_1, num_2 = num_2, num_1 % num_2
        current_gcd = num_1

    return current_gcd


# +
# 4


def month(nmb: int, lang: str = "ru") -> str | None:
    """Возвращает название месяца на указанном языке."""
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

    return months.get(lang, months["ru"])[nmb - 1] if 1 <= nmb <= 12 else None


# +
# 5


def to_string(*args: int, sep: str = " ", end: str = "\n") -> str:
    """Forms a string from the given arguments."""
    return sep.join(map(str, args)) + end


# +
# 6


in_stock: dict[str, int] = {}


def order(*preferences: str) -> str:
    """Process an order based on available ingredients."""
    recipes = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }

    for preference in preferences:
        if preference in recipes:
            required_ingredients = recipes[preference]

            if all(
                in_stock.get(ingredient, 0) >= amount
                for ingredient, amount in required_ingredients.items()
            ):
                for ingredient, amount in required_ingredients.items():
                    in_stock[ingredient] -= amount
                return preference

    return "К сожалению, не можем предложить Вам напиток"


# +
# 7

numbers: tuple[int, ...] = tuple()


def enter_results(*new_values: int) -> None:
    """Add new experiment's values."""
    global numbers  # pylint: disable=global-statement
    numbers += new_values


def get_sum() -> tuple[float, ...]:
    """Compute the sum of experiment's result."""
    return round(sum(numbers[::2]), 2), round(sum(numbers[1::2]), 2)


def get_average() -> tuple[float, ...]:
    """Compute the average of experiment's result."""
    total_even_sum, total_odd_sum = get_sum()
    if len(numbers) == 0:
        return 0.0, 0.0
    return round(2 * total_even_sum / len(numbers), 2), round(
        2 * total_odd_sum / len(numbers), 2
    )


# -

# 8
string = "мама мыла раму"
print(sorted(string.split(), key=lambda word: (len(word), word.lower())))

# +
# 9

print(*filter(lambda number: not sum(map(int, str(number))) % 2, (1, 2, 4, 5)))

# +
# 10


def secret_replace(text: str, **replaces: str) -> str:
    """Return encrypted text."""
    replace_indices = {key: 0 for key in replaces}

    text_list = list(text)

    for i, char in enumerate(text_list):
        if char in replaces:
            index = replace_indices[char]
            replacement = replaces[char][index % len(replaces[char])]
            text_list[i] = replacement
            replace_indices[char] += 1

    return "".join(text_list)
