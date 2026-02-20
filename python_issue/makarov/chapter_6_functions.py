"""Functions in Python."""

# ## Функции в Питоне

# ### Встроенные функции
#

# +
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
height: list[np.float64] = list(np.round(np.random.normal(180, 10, 1000)))
height
# -

# ### Параметры и аргументы функции
#

plt.hist(height, bins=10)
plt.show()

plt.hist(bins=10, x=height)
plt.show()

plt.hist(height)
plt.show()

print("first string")
print()
print("second string")

# ### Функции и методы
#

some_string: str = "machine learning"
some_string.title()


# +
# some_list: list[str] = ["machine", "learning"]
# some_list.title() -> wrong
# -

# ### Собственные функции в Питоне

# ### Объявление и вызов функции
#


# +
def double(x_var: int | float) -> int | float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    res_var: int | float = x_var * 2
    return res_var


double(2)
# -

# ### Пустое тело функции
#

# +
# def only_return():
#    """
#    Temporary training function used to practice Python syntax,

#    typing, and code style. Not intended for production use.
#    """
#    return


# only_return()

# print(only_return())

# +
# def only_pass():
#    """
#    Temporary training function used to practice Python syntax,

#    typing, and code style. Not intended for production use.
#    """
#    pass


# only_pass()
# -

# ### Функция print() вместо return
#


def double_print(x_var_1: int | float) -> None:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    res: int | float = x_var_1 * 2
    print(res)


double_print(5)


# #### Параметры собственных функций
#


def calc_sum(x_var_2: int | float, y_var_2: int | float) -> int | float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return x_var_2 + y_var_2


calc_sum(1, y_var_2=2)


# +
def calc_sum_default(x_var_3: int | float = 1, y_var_3: int | float = 2) -> int | float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return x_var_3 + y_var_3


calc_sum_default()


# +
def print_string() -> None:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    print("some string")


print_string()


# -

# ### Аннотация функции
#
#


# +
def f(x_var_4: float = 3.5) -> int:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return int(x_var_4)


f.__annotations__

f()


# +
def f_1(x_var_5: float) -> float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return float(x_var_5)


f_1(3)
# -

# ### Дополнительные возможности
#

print(calc_sum(1, 2) * 2)
print(calc_sum(1, 2) > 2)


# +
def first_letter() -> str:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return "Python"


print(first_letter()[0])


# +
def use_input() -> int:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    user_input: int = int(input("Введите число: "))
    result: int = user_input**2
    return result


use_input()


# -

# ### Результат вызова функции
#


# +
def create_list(x_var_6: int) -> list[int]:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    list_var_3: list[int] = []
    for i in range(x_var_6):
        list_var_3.append(i)

    return list_var_3


create_list(5)


# +
def tuple_f() -> tuple[str, int]:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    string_var_7: str = "Python"
    x_var_7: int = 42
    return (string_var_7, x_var_7)


(a_var_7, b_var_7) = tuple_f()

print(a_var_7, b_var_7)
print(type(a_var_7), type(b_var_7))

# +
c_var_7: tuple[str, int] = tuple_f()

print(type(c_var_7))
print(c_var_7)


# +
def is_divisible(x_var_8: int) -> bool:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return x_var_8 % 2 == 0


is_divisible(10)


# -

# ### Использование библиотек
#


# +
def mean_f(x_var_9: list[int]) -> float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    mean_val: float = float(np.mean(x_var_9))
    return mean_val + 1.0


x_var_10: list[int] = [1, 2, 3]
mean_f(x_var_10)
# -

# ### Глобальные и локальные переменные
#

# +
global_name: str = "Петр"


def show_name() -> None:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    print(global_name)


show_name()


# +
def show_local_name() -> None:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    local_name_1: str = "Алена"
    print(local_name_1)


show_local_name()
# local_name вне функции не существует

# +
# def make_global():
#    """
#    Temporary training function used to practice Python syntax, typing, and code style.
#
#    Not intended for production use.
#    """
#
#    global local_name
#    local_name: str = "Алена"
#    print(local_name)


# make_global()
# local_name

# +
local_number: int = 5


# def print_number():
#    """
#    Temporary training function used to practice Python syntax,
#    typing, and code style. Not intended for production use.
#    """
#    local_number = 10
#    print("Local number =", local_number)


# print_number()
print("Global number =", local_number)


# -

# ### Lambda-функции
#

# +
# lf = lambda a_var_10, b_var_10: a_var_10 * b_var_10

# lf(2, 3)


# +
def normal_f(a_var_11: int, b_var_11: int) -> int:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return a_var_11 * b_var_11


normal_f(2, 3)
# -

# #### Lambda-функция внутри функции filter()
#

# +
nums: list[int] = [15, 27, 17, 9, 19, 2, 1, 4]

# criterion = lambda n_var_11: True if (n_var_11 > 10) else False

# list(filter(criterion, nums))

# +
# list(filter(lambda n_var_12: True if (n_var_12 > 10) else False, nums))


# +
def is_criterion_2(n_var_13: int) -> bool:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return n_var_13 > 10


list(filter(is_criterion_2, nums))
# -

# #### Lambda-функция внутри функции sorted()
#

# +
indices_distances: list[tuple[int, float]] = [
    (901, 0.0),
    (1002, 0.2298440568634488),
    (442, 0.25401128310081567),
]


def key_var(x_var_11: tuple[int, float]) -> float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return x_var_11[1]


sorted(indices_distances, key=key_var, reverse=False)


# -

# #### Немедленно вызываемые функции
#


# +
def square(x_var_12: int | float) -> int | float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return x_var_12 * x_var_12


print(square(10))


# -

# ### *args и **kwargs

# #### *args
#


# +
def mean(a_var_14: int, b_var_14: int) -> float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    return (a_var_14 + b_var_14) / 2


mean(1, 2)


# +
def mean_1(list_1: list[int]) -> float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    total: int = 0
    for i in list_1:
        total += i

    return total / len(list_1)


list_var_1: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]

mean_1(list_var_1)


# +
# mean(1, 2) -> WRONG, only lists


# +
def mean_2(*nums_var_1: int) -> float:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    total_var_1: int = 0
    for i in nums_var_1:
        total_var_1 += i

    return total_var_1 / len(nums_var_1)


list_var_2: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]

mean_2(1, 2, 3, 4, 5)
mean_2(*[3, 4, 7, 8, 11, 22])


# +
def test_type(*nums_var: int | float) -> None:
    """Temporary training function used to practice Python syntax and
    typing."""
    for num in nums_var:
        print(type(num))


test_type(1, 3, 5, 12)
test_type(*list_var_2)
# -

a_var_15: list[int] = [1, 2, 3, 4]
b_var_15: list[int] = [*a_var_15, 4, 5, 6, 7]
b_var_15


# #### **kwargs
#


# +
def f_3(**kwargs: int) -> dict[str, int]:
    """Temporary training function used to practice Python syntax and
    typing."""
    return kwargs


f_3(a=1, b=2)


# +
def simple_stats(*nums_var_3: int | float, **params: bool) -> None:
    """Temporary training function used to practice Python syntax, typing, and
    code style.

    Not intended for production use.
    """
    if "mean" in params and params["mean"]:
        print(f"mean: \t{np.round(np.mean(nums_var_3), 3)}")

    if "std" in params and params["std"]:
        print(f"std: \t{np.round(np.std(nums_var_3), 3)}")


simple_stats(5, 10, 15, 20, mean=True, std=True)
print()
simple_stats(5, 20, 10, 11, mean=True, std=False)

# +
list_var: list[int] = [5, 12, 18, 22]
settings: dict[str, bool] = {"mean": True, "std": True}

simple_stats(*list_var, **settings)
# -

simple_stats(5, 10, 14, 19, 25, 22, mean=True, std=True, median=True)
