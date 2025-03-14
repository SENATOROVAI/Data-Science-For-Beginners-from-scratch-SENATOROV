"""Recursion.

Decorator. Generator.
"""

# ### Change recursion limit
#
# ```python
# from sys import setrecursionlimit
#
# setrecursionlimit(2000)
# ```
#
# ### Apply memoization
#
# ```python
# from timeit import timeit
# from functools import lru_cache
#
#
# @lru_cache(maxsize=1000)
# def fib(n):
#     if n in (0, 1):
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(
#     f"Среднее время вычисления: "
#     f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 6)} с."
# )
# ```
#
#
# ### Decorator
#
# A decorator is an object that enhances a function's capabilities \
# without modifying its original code. In Python, decorators are often implemented as functions.
#
# Here’s how a decorator works:
#
# - It takes a function as an argument.
# - It defines a new function that extends the behavior of the original function.
# - It returns this new function as an object.
#
# ```python
# def count(f):
#     total = 0
#
#     # Объявляем функцию, которая расширяет функционал f
#     def decorated(*args, **kwargs):
#         # Переменная total объявлена нелокальной для доступа из внутренней функции
#         nonlocal total
#         total += 1
#         # Возвращаем значение исходной функции и дополнительно total
#         return f(*args, **kwargs), total
#
#     # Возвращаем новую функцию как объект
#     return decorated
#
#
# @count
# def hello(name):
#     return f"Привет, {name}!"
#
#
# print(hello("Пользователь_1"))
# print(hello("Пользователь_2"))
# ```
#
# ### Generator
#
# A generator stores only the current value in memory and can return the next value when the __next__() method is called.
#
# To create a generator function, instead of using return, you use the yield statement.
#
# - yield pauses the function’s execution and returns a value.
# - When __next__() is called (e.g., in a loop), execution resumes from where it was paused.
#
# ```python
# def fib(n):
#     n_1, n_2 = 1, 1
#     for i in range(n):
#         yield n_1
#         n_1, n_2 = n_2, n_1 + n_2
#
#
# print(", ".join(str(x) for x in fib(10)))
# ```

# +
# 1

# fmt: off
from collections.abc import Generator, Sequence
from typing import Callable, Union

# fmt: on


def recursive_sum(*args: int) -> int:
    """Recursively sums a variable number of integer arguments."""
    if not args:
        return 0
    return args[-1] + recursive_sum(*args[:-1])


# +
# 2


def recursive_digit_sum(nmb: int) -> int:
    """Recursively sums the digits of a given integer."""
    if nmb // 10 > 0:
        return nmb % 10 + recursive_digit_sum(nmb // 10)
    return nmb % 10


# +
# 3


def make_equation(*coeffs: int) -> str:
    """Recursively creates a string representation of a polynomial equation."""
    if len(coeffs) == 1:
        return str(coeffs[0])
    line = ") * x " + ("- " if coeffs[-1] < 0 else "+ ") + str(coeffs[-1])
    return "(" + make_equation(*coeffs[:-1]) + line


# +
# 4


def answer(
    func: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], int | str]:
    """Decorate that wraps function result in a formatted string."""

    def decorated(*args: int | str, **kwargs: int | str) -> str:
        return f"Результат функции: {func(*args, **kwargs)}"

    return decorated


# +
# 5


def result_accumulator(
    func: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], list[int | str] | None]:
    """Decorate that accumulates function results in a list."""
    acc: list[int | str] = []

    def decorated(
        *args: int | str, method: str = "accumulate"
    ) -> list[int | str] | None:
        nonlocal acc
        result = func(*args)
        acc.append(result)

        if method == "drop":
            accumulated_results = acc[:]
            acc.clear()
            return accumulated_results

        return None

    return decorated


# +
# 6


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list."""
    result: list[int] = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


def merge_sort(arr: list[int]) -> list[int]:
    """Sorts a list using merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    middle: int = int(len(arr) / 2)
    left: list[int] = merge_sort(arr[:middle])
    right: list[int] = merge_sort(arr[middle:])
    return merge(left, right)


# +
# 7


OutputType = Union[int, str, bool]


def same_type(
    func: Callable[[int | str], OutputType],
) -> Callable[[int | str], OutputType]:
    """Ensure all arguments passed to the function are of the same type."""

    def decorated(*args: int | str) -> OutputType:
        if len(set(map(type, args))) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)

    return decorated


# +
# 8


def fibonacci(value: int) -> Generator[int]:
    """Decorate that yields the first n numbers in the Fibonacci sequence."""
    n_1, n_2 = 0, 1
    for _ in range(value):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2


# +
# 9


def cycle(arr: list[int]) -> Generator[list[int]]:
    """Decorate that infinitely yields elements from the list."""
    while arr:
        yield arr


# +
# 10


def make_linear(arr: Sequence[Union[int, Sequence[int]]]) -> list[int]:
    """Flattens a nested list structure into a single linear list."""
    result: list[int] = []

    for el in arr:
        if isinstance(el, Sequence):
            result.extend(make_linear(el))
        else:
            result.append(el)

    return result
