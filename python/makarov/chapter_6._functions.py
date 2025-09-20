"""Functions."""

# ## Функции в Питоне

# ### Встроенные функции

from collections.abc import ItemsView

# fmt: off
from typing import Callable

# #### Параметры и аргументы функции

# функция может не принимать параметров
print("Первая строка")
print()
print("Третья строка")

# #### Функции и методы

# +
# дана строка
some_string = "machine learning"

# применим метод .title()
some_string.title()
# -

# к списку
some_list = ["machine", "learning"]

# ### Собственные функции в Питоне

# #### Объявление и вызов функции

# +
# создадим функцию, которая удваивает любое передаваемое ей значение


def double(x_val: float) -> float:
    """Return the input value multiplied by 2."""
    res = x_val * 2
    return res


# -

# и вызовем ее, передав число 2
double(2)

# #### Пустое тело функции

# +
# тело функции не может быть пустым


def only_return() -> None:
    """Return None as an example of empty function body."""
    # нужно либо указать ключевое слово return
    return


# -

only_return()

# +
# такая функция вернет тип данных None (отсутствие значения)
# print(only_return())
# -

# #### Функция print() вместо return

# +
# можно использовать print(), но есть нюансы (см. на странице урока)


def double_print(x_val: float) -> None:
    """Print double of input value."""
    res = x_val * 2
    print(res)


# -

double_print(5)

# #### Параметры собственных функций

# +
# объявим функцию с параметрами x и y


def calc_sum(x_val: float, y_val: float) -> float:
    """Return sum of two numbers."""
    # и выведем их сумму
    return x_val + y_val


# -

# вызовем эту функцию с одним позиционным и одним именованным параметром
calc_sum(1, y_val=2)

# +
# параметрам функции можно задать аргументы по умолчанию


def calc_sum_default(x_val: float = 1, y_val: float = 2) -> float:
    """Return sum of two numbers with default values."""
    return x_val + y_val


# и при вызове тогда их указывать не обязательно
calc_sum_default()

# +
# функция может не иметь параметров


def print_string() -> None:
    """Print a predefined string."""
    print("Some string")


print_string()


# -

# #### Аннотация функции

def f_to_int(x_val: float = 3.5) -> int:
    """Convert float number to integer."""
    return int(x_val)


# желаемый тип данных можно посмотреть через атрибут __annotations__
f_to_int.__annotations__

# вызовем функцию без параметров
f_to_int()

# #### Дополнительные возможности

# вызов функции можно совмещать с арифметическими
print(calc_sum(1, 2) * 2)

# и логическими операциями
print(calc_sum(1, 2) > 2)

# +
# можно и так


def first_letter() -> str:
    """Return first letter of 'Python'."""
    return "Python"


print(first_letter()[0])

# +
# функция может не принимать параметров, но использовать input()


def use_input() -> int:
    """Return squared inputs."""
    # запросим у пользователя число и переведем его в тип данных int
    user_inp = int(input("Введите число: "))

    # возведем число в квадрат
    result = user_inp**2

    # вернем результат
    return result


# вызовем функцию
use_input()
# -

# #### Результат вызова функции

# +
# функция может возвращать также список, кортеж, словарь и др.


# объявим функцию, которая на входе получает число,
# а на выходе формирует список чисел от 0 и до числа, предшествующего заданному
def create_list(x_val: int) -> list[int]:
    """Create list of integers from 0 to x-1."""
    # создадим пустой список
    ls = []

    # в цикле for создадим последовательность
    for i in range(x_val):

        # и поместим ее в список
        ls.append(i)

    return ls


# результатом вызова этой функции будет список
create_list(5)

# +
# функция может возвращать сразу два значения


def tuple_f() -> tuple[str, int]:
    """Return tuple with string 'Python' and integer 42."""
    string = "Python"
    x_val = 42
    return string, x_val


# +
# если использовать две переменные
a_val, b_val = tuple_f()

# на выходе мы получим строку и число
print(a_val, b_val)
print(type(a_val), type(b_val))

# +
# если одну
c_val = tuple_f()

# получится кортеж
print(c_val)
print(type(c_val))

# +
# выводом может быть логическое значение (True или False)


def is_divisible(x_val: int) -> bool:
    """Check if number is divisible by 2."""
    return x_val % 2 == 0


is_divisible(10)
# -

# #### Глобальные и локальные переменные

# +
# создадим глобальную переменную вне функции
global_name = "Петр"

# а затем используем ее внутри новой функции


def show_name() -> None:
    """Print global name variable."""
    print(global_name)


# -

show_name()

# +
# а теперь вначале создадим функцию,
# внутри которой объявим локальную переменную


def show_local_name() -> None:
    """Print local name variable."""
    local_name_val = "Алена"
    print(local_name_val)


# -

show_local_name()

# +
# превратить локальную переменную в глобальную можно через global

local_name: str = ""


def make_global() -> None:
    """Create global variable local_name and print it."""
    # pylint: disable=global-statement
    global local_name
    local_name = "Алена"
    print(local_name)


# -

make_global()

# +
# объявим глобальную переменную
global_number: int = 5


def print_number() -> None:
    """Print local number variable."""
    # затем объявим локальную переменную
    local_number: int = 10
    print("Local number:", local_number)


# -

# функция всегда "предпочтет" локальную переменную
print_number()

# при этом значение глобальной переменной для остального кода не изменится
print("Global number:", global_number)

# ### Lambda-функции

lf: Callable[[int, int], int] = lambda z_val, b_val: z_val * b_val

# +
# этот же функционал можно поместить в обычную функцию


def normal_f(p_val: int, j_val: int) -> int:
    """Multiply two numbers."""
    return p_val * j_val


normal_f(2, 3)
# -

# #### Lambda-функция внутри функции filter()

# +
nums = [15, 27, 9, 18, 3, 1, 4]

list(filter(lambda n_val: n_val > 10, nums))

# +
# ту же задачу можно решить через обычную функцию,
# но придется написать больше кода


def is_greater_10(n_val: int) -> bool:
    """Return True if number is greater than 10, False otherwise."""
    if n_val > 10:
        return True
    return False


list(filter(is_greater_10, nums))
# -

# #### Lambda-функция внутри функции sorted()

# +
# напомню, что мы создали список из кортежей,
# и в каждом кортеже был индекс фильма и расстояние до него
indices_distances = [
    (901, 0.0),
    (1002, 0.22982440568634488),
    (442, 0.25401128310081567),
]

# lambda-функция возьмет каждый кортеж и вернет второй [1] его элемент
# передав эту функцию через параметр key, мы отсортируем список по расстоянию
sorted(indices_distances, key=lambda x_val: x_val[1], reverse=False)


# -

# #### Немедленно вызываемые функции

# +
# lambda-функцию можно вызвать сразу в момент объявления
# (lambda x_val: x_val * x_val)(10)
# -

# ### \*args и \**kwargs

# #### \*args

def mean(q_val: float, s_val: float) -> float:
    """Calculate arithmetic mean of two numbers."""
    return (q_val + s_val) / 2


mean(1, 2)


def mean_2(list_val: list[int]) -> float:
    """Calculate arithmetic mean of numbers in list."""
    # зададим переменную для суммы,
    total = 0

    # в цикле сложим все числа из списка
    for i_val in list_val:
        total += i_val

    # и разделим на количество элементов
    return total / len(list_val)


mean_2([1, 2, 3, 4])

# +
# объявим функцию с *args


def mean_3(*nums_val: int) -> float:
    """Calculate arithmetic mean of arbitrary number of numbers."""
    # в данном случае мы складываем элементы кортежа
    total = 0
    for i_val in nums_val:
        total += i_val

    return total / len(nums_val)


# -

# теперь мы можем передать функции отдельные числа
mean_3(1, 2, 3, 4)

# или список
mean_3(*[5, 10, 15, 20])

# +
# убедимся, что оператор распаковки * формирует кортеж


def test_type(*nums_val: float) -> None:
    """Print tuple of numbers and its type."""
    print(nums_val, type(nums_val))


test_type(1, 2, 3, 4)
# -

# со списком происходит то же самое
test_type(*[5, 10, 15, 20])

# +
# для наглядности приведем еще один пример
a_ls_val = [1, 2, 3]
b_ls_val = [*a_ls_val, 4, 5, 6]

print(b_ls_val)


# -

# #### \**kwargs

# +
def show_kwarguments(**kwargs: int) -> ItemsView[str, int]:
    """Convert keyword arguments into dictionary items."""
    return kwargs.items()


show_kwarguments(a=1, b=2)
