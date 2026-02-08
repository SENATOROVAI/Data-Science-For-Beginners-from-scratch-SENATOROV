"""Функции в python."""

# #### Встроенные функции

# +
# импортируем библиотеки
import matplotlib.pyplot as plt
import numpy as np

# установим точку отсчёта
np.random.seed(42)
# и снова сгенерируем данные о росте (как мы делали на восьмом занятии вводного курса)
height = list(np.round(np.random.normal(180, 10, 1000)))
# -

# #### Параметры и аргументы фукнции

# теперь построим гистограмму передав ей два параметра,
# данные о росте и количество интервалов
# первый параметр у нас позиционный, второй - именованный
plt.hist(height, bins=10)
plt.show()

# первый параметр можно также сделать именованным
# (данные обозначаются через x)
# и тогда порядок параметров можно менять
plt.hist(bins=10, x=height)
plt.show()

# у параметра bins есть аргумент по умолчанию (как раз 10 интервалов),
# а значит, этот параметр можно не указывать
plt.hist(height)
plt.show()

# функция может не принимать параметров
print("Первая строка")
print()
print("Третья строка")

# #### Функции и методы

# +
# дана строка
some_string = "machine learning"

# применим метод .title()
print(some_string.title())


# -

# Этот код вызовет ошибку:
# ```python
# # к списку
# some_list = ["machine", "learning"]
#
# # этот метод не применить
# print(some_list.title())
# ```

# #### Объявление и вызов функции


def double(value: int | float) -> int | float:
    """Возведение в квадрат."""
    res = value * 2
    return res


print(double(2))


# #### Пустое тело функции


def only_return() -> None:
    """Пустая функция."""
    return


print(only_return is None)


def only_pass() -> None:
    """Пустая функция."""


print(only_pass is None)

# такая функция вернёт тип данных None
print(only_return is None)


# #### Функция print() вместо return


def double_print(value: int | float) -> None:
    """Удвоение и вывод."""
    res = value * 2
    print(res)


double_print(5)


# #### Параметры собственных функций


def calc_sum(value_1: int | float, value_2: int | float) -> int | float:
    """Сумма."""
    return value_1 + value_2


# Этот код вызовет ошибку:
# ```python
# print(calc_sum(1, y=2))
# ```


# +
def calc_sum_default(value_1: float | int = 1, value_2: float | int = 2) -> float | int:
    """Сумма."""
    return value_1 + value_2


print(calc_sum_default())


# -


def print_string() -> None:
    """Вывод строки."""
    print("Some string")


# #### Аннотация функции


def f_to_int(value: float = 3.5) -> int:
    """К целому числу."""
    return int(value)


print(f_to_int())


# +
def f_to_float(value: int) -> float:
    """К вещественному числу."""
    return float(value)


print(f_to_float(3))
# -

# #### Дополнительные возможности

print(calc_sum(1, 2) * 2)

print(calc_sum(1, 2) > 2)


# +
def first_letter() -> str:
    """Возвращает строку."""
    return "Python"


print(first_letter()[0])


# +
def use_input() -> int:
    """Ввод и возведение в квадрат."""
    user_inp = int(input("Введите число: "))
    result = user_inp**2
    return result


print(use_input())


# -

# #### Результат вызова функции


# +
def create_list(count: int) -> list[int]:
    """Создание списка."""
    result_list = []
    for index_value in range(count):
        result_list.append(index_value)
    return result_list


print(create_list(5))


# -


def tuple_f() -> tuple[str, int]:
    """Создание кортежа."""
    string = "Python"
    value = 42
    return (string, value)


# +
string_value, number_value = tuple_f()

print(string_value, number_value)
print(type(string_value), type(number_value))

# +
tuple_value = tuple_f()

print(tuple_value)
print(type(tuple_value))


# +
def is_divisible(value: int) -> bool:
    """Проверка на чётность."""
    return value % 2 == 0


print(is_divisible(10))


# -

# #### Использование библиотек


def mean_f(number_list: list[int]) -> float:
    """Среднее."""
    return float(np.mean(number_list)) + 1


numbers = [1, 2, 3]
print(mean_f(numbers))

# #### Глобальные и локальные переменные

# +
global_name = "Петр"


def show_name() -> None:
    """Вывод глобальной переменной."""
    print(global_name)


show_name()


# +
def show_local_name() -> None:
    """Вывод локальной переменной."""
    name = "Алена"
    print(name)


show_local_name()
# -

# Этот код вызовет ошибку:
# ```python
# print(local_name)
# ```

local_name = "Алена"
print(local_name)

print(local_name)

# +
global_number = 5


def print_number() -> None:
    """Вывод числа."""
    local_number = 10
    print("Local number:", local_number)


# -

print_number()


# #### Lambda-функции


# +
def multiply_numbers(value_1: int | float, value_2: int | float) -> int | float:
    """Умножение."""
    return value_1 * value_2


print(multiply_numbers(2, 3))


# +
def normal_f(value_1: int | float, value_2: int | float) -> int | float:
    """Умножение."""
    return value_1 * value_2


print(normal_f(2, 3))
# -

# #### Lambda-функция внутри функции filter()

# +
nums = [15, 27, 9, 18, 3, 1, 4]


def is_greater_than_ten(value: int | float) -> bool:
    """Проверка числа больше 10."""
    return value > 10


print(list(filter(is_greater_than_ten, nums)))
# -

print(list(filter(is_greater_than_ten, nums)))


# +
def is_criterion_2(value: int | float) -> bool:
    """Проверка."""
    if value > 10:
        return True
    return False


print(list(filter(is_criterion_2, nums)))
# -

# #### Lambda-функция внутри функции sorted()

# +
indices_distances = [
    (901, 0.0),
    (1002, 0.22982440568634488),
    (442, 0.25401128310081567),
]

print(sorted(indices_distances, key=lambda pair: pair[1], reverse=False))


# -

# #### Немедленно вызываемые функции


# +
def square(value: int | float) -> int | float:
    """Квадрат числа."""
    return value * value


print(square(10))


# -

# #### *args


# +
def mean1(value_1: int | float, value_2: int | float) -> int | float:
    """Среднее."""
    return (value_1 + value_2) / 2


mean1(1, 2)


# -


def mean2(list0_: list[int]) -> int | float:
    """Среднее от списка."""
    total = 0
    for value in list0_:
        total += value
    return total / len(list0_)


# +
list_ = [1, 2, 3, 4]

mean2(list_)


# -

# Этот код вызовет ошибку:
# ```python
# mean2(1, 2)
# ```


def mean3(*list_of_nums: int) -> int | float:
    """Среднее."""
    total = 0
    for value in list_of_nums:
        total += value
    return total / len(list_of_nums)


mean3(1, 2, 3, 4)

mean3(*list_)


# +
def print_type(*list_of_nums: int | float) -> None:
    """Проверка типа."""
    print(list_of_nums, type(list_of_nums))


print_type(1, 2, 3, 4)
# -

print_type(*list_)

base_list = [1, 2, 3]
extended_list = [*base_list, 4, 5, 6]
print(extended_list)


# #### **kwargs


def print_args(**kwargs: int) -> list[tuple[str, int]]:
    """Вывод именованных аргументов."""
    return list(kwargs.items())


print(print_args(a=1, b=2))


def simple_stats(*list_of_nums: int, **params: bool) -> None:
    """Вывод основных статистик."""
    if "mean" in params and params["mean"]:
        print(f"mean: \t{np.round(np.mean(list_of_nums), 3)}")
    if "std" in params and params["std"]:
        print(f"std: \t{np.round(np.std(list_of_nums), 3)}")


simple_stats(5, 10, 15, 20, mean=True, std=True)

simple_stats(5, 10, 15, 20, mean=True, std=False)

# +
list1_ = [5, 10, 15, 20]
settings = {"mean": True, "std": True}

simple_stats(*list1_, **settings)
# -

simple_stats(5, 10, 15, 20, mean=True, std=True, median=True)
