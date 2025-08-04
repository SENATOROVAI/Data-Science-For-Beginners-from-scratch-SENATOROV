"""Recursion. Decorators. Generators."""

# +
# 1

from typing import Callable, Generator, Sequence, Union


def recursive_sum(*nums: int) -> int:
    """Calculate a sum of all positional arguments."""
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])


result_1 = recursive_sum(1, 2, 3)

print(result_1)

# +
# 2


def recursive_digit_sum(num: int) -> int:
    """Calculate a sum of all digits within given integer."""
    if num == 0:
        return 0
    last_digit = num % 10
    remaining_num = num // 10
    return last_digit + recursive_digit_sum(remaining_num)


result_2 = recursive_digit_sum(123)

print(result_2)

# +
# 3


def make_equation(*coefficients: int) -> str:
    """Build a string, representing N-th degree polynomial."""
    if len(coefficients) == 1:
        return str(coefficients[0])

    previous_terms = make_equation(*coefficients[:-1])
    last_coefficient = coefficients[-1]
    return f"({previous_terms}) * x + {last_coefficient}"


result_3 = make_equation(3, 2, 1)

print(result_3)

# +
# 4


def answer(
    func: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], int | str]:
    """Wrap function's output in string representation."""

    def inner(*args: int | str, **kwargs: int | str) -> str:
        return f"Результат функции: {func(*args, **kwargs)}"

    return inner


# @answer
# def get_letters(text: str) -> str:
#     """Adhere letters into a message."""
#     return "".join(sorted(set(filter(str.isalpha, text.lower()))))


# print(get_letters("Hello, world!"))
# print(get_letters("Декораторы это круто =)"))

# +
# 5


def result_accumulator(
    func: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], list[int | str] | None]:
    """Accumulate function's output in a list."""
    results = []

    def inner(
        *args: int | str, method: str = "accumulate", **kwargs: int | str
    ) -> list[int | str] | None:
        results.append(func(*args, **kwargs))

        if method == "drop":
            current_results = results.copy()
            results.clear()
            return current_results

        return None

    return inner


# @result_accumulator
# def a_plus_b(a: int, b: int) -> int:
#     """Calculate a sum of two integers"""
#     return a + b


# print(a_plus_b(3, 5, method="accumulate"))
# print(result_0)
# print(a_plus_b(7, 9))
# print(a_plus_b(-3, 5, method="drop"))
# print(a_plus_b(1, -7))
# print(a_plus_b(10, 35, method="drop"))

# +
# 6


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two lists into united sorted list."""
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def merge_sort(batch: list[int]) -> list[int]:
    """Sort a list, applying special approach."""
    if len(batch) <= 1:
        return batch

    mid_point = len(batch) // 2
    left_half = merge_sort(batch[:mid_point])
    right_half = merge_sort(batch[mid_point:])

    return merge(left_half, right_half)


result_4 = merge_sort([3, 2, 1])

print(result_4)

# +
# 7


InputType = Union[int, str]
OutputType = Union[int, str, bool]


def same_type(
    func: Callable[[InputType], OutputType],
) -> Callable[[InputType], OutputType]:
    """Check that all function's arguments belong to the same type."""

    def inner(*args: InputType) -> OutputType:
        arg_types = {type(arg) for arg in args}
        if len(arg_types) > 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)

    return inner


# @same_type
# def combine_text(*words):
#     """Make word combinations."""
#     return " ".join(words)


# print(combine_text("Hello,", "world!") or "Fail")
# print(combine_text(2, "+", 2, "=", 4) or "Fail")
# print(combine_text("Список из 30", 0, "можно получить так", [0] * 30) or "Fail")

# +
# 8


def fibonacci(value: int) -> Generator[int]:
    """Return given quantity of Fibonacci numbers."""
    num_1 = 0
    num_2 = 1
    for _ in range(value):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


print(*fibonacci(10), sep=", ")

# +
# 9


def cycle(batch: list[int]) -> Generator[int]:
    """Yield elements from a list."""
    while batch:
        yield from batch


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))

# +
# 10


def make_linear(batch: Sequence[Union[int, Sequence[int]]]) -> list[int]:
    """Return simple-structure list, rectifying multicomponent list."""
    result: list[int] = []
    for item in batch:
        if isinstance(item, list):
            result.extend(make_linear(item))
        elif isinstance(item, int):
            result.append(item)
    return result


result_5 = make_linear([1, 2, [3]])

print(result_5)
