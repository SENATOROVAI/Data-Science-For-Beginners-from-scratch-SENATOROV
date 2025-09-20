"""4.3 Reqursion."""

from collections.abc import Generator
from typing import Callable, Union

# +
# Рекурсивный сумматор


def recursive_sum(*args: int) -> int:
    """Рекурсивный сумматорю."""
    if len(args) == 1:
        return args[0]

    return args[0] + recursive_sum(*args[1:])


# +
# Рекурсивный сумматор цифр


def recursive_digit_sum(number: int) -> int:
    """Рекурсивно находит сумму цифр."""
    str_number = str(number)
    if len(str_number) == 1:
        return number

    return int(str_number[0]) + recursive_digit_sum(int(str_number[1:]))


# +
# Многочлен N-ой степени


def make_equation(*args: int) -> str:
    """Формирует выражение."""
    if len(args) == 1:
        return str(args[0])

    return "(" + make_equation(*args[:-1]) + ")" + " * x" + f" + {args[-1]}"


# +
# Декор результата


def answer(func: Callable[[int, int], str]) -> Callable[[int, int], str]:
    """Декоратор."""

    def wrapper(*args: int, **kwargs: int) -> str:
        """Функция декоратора."""
        return f"Результат функции: {func(*args, **kwargs)}"

    return wrapper


# +
# Накопление результата


def result_accumulator(
    func: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], list[int | str] | None]:
    """Декоратор напопитель."""
    dec_queue: list[int | str] = []

    def wrapper(*args: int | str, method: str = "accumulate") -> list[int | str] | None:
        """Функция декоратора."""
        func_res = func(*args)
        dec_queue.append(func_res)

        if method == "drop":
            res_for_return = dec_queue[:]
            dec_queue.clear()
            return res_for_return

        return None

    return wrapper


# +
def merge_sort(lst: list[int]) -> list[int]:
    """Сортировка слиянием."""
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Слияние двух отсортированных списков."""
    result = []
    ind1 = ind2 = 0

    while ind1 < len(left) and ind2 < len(right):
        if left[ind1] <= right[ind2]:
            result.append(left[ind1])
            ind1 += 1
        else:
            result.append(right[ind2])
            ind2 += 1

    result.extend(left[ind1:])
    result.extend(right[ind2:])

    return result


# +
# Однотипность не порок


def same_type(
    func: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], int | str | None]:
    """Декоратор-проверятор."""

    def wrapper(*args: int | str) -> int | str | None:
        """Функция декоратора."""
        if len(set(map(type, args))) != 1:
            print("Обнаружены различные типы данных")
            return None

        return func(*args)

    return wrapper


# +
# Генератор Фибоначчи


def fibonacci(number: int) -> Generator[int, None, None]:
    """Генератор Фибоначи."""
    number0, number1 = 0, 1
    for _ in range(number):
        yield number0
        number0, number1 = number1, number1 + number0


# +
# Циклический генератор


def cycle(arr: list[int]) -> Generator[int, None, None]:
    """Цикличный генератор."""
    index = 0
    while True:
        yield arr[index]
        index = (index + 1) % len(arr)


# +
# Определяем рекурсивный тип для вложенных списков
NestedIntList = Union[int, list["NestedIntList"]]


def make_linear(lst: list[NestedIntList]) -> list[int]:
    """Линеаризует список."""
    res_lst: list[int] = []

    for el in lst:
        if isinstance(el, list):
            res_lst += make_linear(el)
        else:
            res_lst += [el]  # здесь el гарантированно int

    return res_lst
