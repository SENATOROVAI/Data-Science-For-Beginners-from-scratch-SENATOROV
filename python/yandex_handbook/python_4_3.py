"""Yandex handbook "Python Basics" answers."""

# +
from typing import Callable, Generator, Sequence, Union


# 1
def recursive_sum(*numbers: int) -> int:
    """Вычисляет сумму всех переданных аргументов."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(*numbers[1:])


calculation_result_1 = recursive_sum(1, 2, 3)

print(calculation_result_1)


# +
# 2
def recursive_digit_sum(number: int) -> int:
    """Вычисляет сумму всех цифр в заданном целом числе."""
    if number == 0:
        return 0
    last_digit = number % 10
    remaining_number = number // 10
    return last_digit + recursive_digit_sum(remaining_number)


calculation_result_2 = recursive_digit_sum(123)

print(calculation_result_2)


# +
# 3
def make_equation(*coefficients: int) -> str:
    """Строит строку, представляющую полином N-ной степени."""
    if len(coefficients) == 1:
        return str(coefficients[0])

    previous_terms = make_equation(*coefficients[:-1])
    last_coefficient = coefficients[-1]
    return f"({previous_terms}) * x + {last_coefficient}"


equation_result_3 = make_equation(3, 2, 1)

print(equation_result_3)


# -

# 4
def answer(
    function: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], int | str]:
    """Обертывает вывод функции в строковое представление."""

    def inner(*args: int | str, **kwargs: int | str) -> str:
        return f"Результат функции: {function(*args, **kwargs)}"

    return inner


# 5
def result_accumulator(
    function: Callable[[int | str, int | str], int | str],
) -> Callable[[int | str, int | str], list[int | str] | None]:
    """Накопляет вывод функции в списке."""
    accumulated_results: list[int | str] = []

    def inner(
        *args: int | str, method: str = "accumulate", **kwargs: int | str
    ) -> list[int | str] | None:
        accumulated_results.append(function(*args, **kwargs))

        if method == "drop":
            current_results = accumulated_results.copy()
            accumulated_results.clear()
            return current_results

        return None

    return inner


# +
# 6
def merge(left_part: list[int], right_part: list[int]) -> list[int]:
    """Объединяет два списка в один отсортированный список."""
    merged_result: list[int] = []
    left_index = right_index = 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            merged_result.append(left_part[left_index])
            left_index += 1
        else:
            merged_result.append(right_part[right_index])
            right_index += 1

    merged_result.extend(left_part[left_index:])
    merged_result.extend(right_part[right_index:])

    return merged_result


def merge_sort(collection: list[int]) -> list[int]:
    """Сортирует список, применяя специальный подход."""
    if len(collection) <= 1:
        return collection

    mid_point = len(collection) // 2
    left_half = merge_sort(collection[:mid_point])
    right_half = merge_sort(collection[mid_point:])

    return merge(left_half, right_half)


sorting_result_4 = merge_sort([3, 2, 1])

print(sorting_result_4)

# +
# 7
# 7

InputType = Union[int, str]
OutputType = Union[int, str, bool]


def same_type(
    function: Callable[[InputType], OutputType],
) -> Callable[[InputType], OutputType]:
    """Проверяет, что все аргументы функции принадлежат одному типу."""

    def inner(*args: InputType) -> OutputType:
        argument_types = {type(arg) for arg in args}
        if len(argument_types) > 1:
            print("Обнаружены различные типы данных")
            return False
        return function(*args)

    return inner


# +
# 8
def fibonacci(number_count: int) -> Generator[int]:
    """Возвращает заданное количество чисел Фибоначчи."""
    first_number, second_number = 0, 1
    for _ in range(number_count):
        yield first_number
        first_number, second_number = (
            second_number, first_number + second_number
        )


fibonacci_sequence_8 = fibonacci(10)

print(*fibonacci_sequence_8, sep=", ")


# +
# 9
def cycle(iterable_collection: list[int]) -> Generator[int]:
    """Возвращает элементы из списка по циклу."""
    while iterable_collection:
        yield from iterable_collection


cycled_elements_9 = (x for _, x in zip(range(5), cycle([1, 2, 3])))

print(*cycled_elements_9)


# +
# 10
def make_linear(
    nested_collection: Sequence[Union[int, Sequence[int]]]
) -> list[int]:
    """Возвращает список простой структуры,
    выпрямляя многокомпонентный список."""
    linear_result: list[int] = []
    for element in nested_collection:
        if isinstance(element, list):
            linear_result.extend(make_linear(element))
        elif isinstance(element, int):
            linear_result.append(element)
    return linear_result


flatten_result_5 = make_linear([1, 2, [3]])

print(flatten_result_5)
