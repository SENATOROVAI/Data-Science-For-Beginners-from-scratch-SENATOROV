"""Functions."""

# +
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

# -

# Встроенные функции

# +
# импортируем библиотеки

# установим точку отсчета
np.random.seed(42)
# и снова сгенерируем данные о росте (как мы делали на восьмом занятии вводного курса)
height = list(np.round(np.random.normal(180, 10, 1000)))
# -

# теперь построим гистограмму передав ей два параметра, данные о росте и количество интервалов
# первый параметр у нас позиционный, второй - именованный
plt.hist(height, bins=10)
plt.show()

# первый параметр можно также сделать именованным (данные обозначаются через x)
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

# Функции и методы

# +
# дана строка
some_string = "machine learning"

# применим метод .title()
some_string.title()

# +
# к списку
some_list = ["machine", "learning"]

# этот метод не применить
some_list.title()  # type: ignore[attr-defined]


# -

# Собственные функции в Питоне


# +
# создадим функцию, которая удваивает любое передаваемое ей значение


def double(number: float) -> float:
    """Удвоить переданное число."""
    res = number * 2
    return res


# и вызовем ее, передав число 2
double(2)


# -

# Параметры собственных функций


# +
# объявим функцию с параметрами num1 и num2


def calc_sum(num1: float, num2: float) -> float:
    """Вернуть сумму двух чисел."""
    # и выведем их сумму
    return num1 + num2


# вызовем эту функцию с одним позиционным и одним именованным параметром
calc_sum(1, num2=2)

# +
# параметрам функции можно задать аргументы по умолчанию


def calc_sum_default(num1: float = 1, num2: float = 2) -> float:
    """Вернуть сумму двух чисел со значениями по умолчанию."""
    return num1 + num2


# и при вызове тогда их указывать не обязательно
calc_sum_default()

# +
# укажем, что на входе функция принимает тип float, а возвращает int
# значение 3,5 - это значение параметра value по умолчанию


def f(value: float = 3.5) -> int:
    """Привести значение к типу int."""
    return int(value)


# желаемый тип данных можно посмотреть через атрибут __annotations__
f.__annotations__


# +
# функция может возвращать также список, кортеж, словарь и др.


# объявим функцию, которая на входе получает число,
# а на выходе формирует список чисел от 0 и до числа, предшествующего заданному
def create_list(count: int) -> list[int]:
    """Создать список чисел от 0 до count не включительно."""
    # создадим пустой список
    numbers = []

    # в цикле for создадим последовательность
    for i in range(count):

        # и поместим ее в список
        numbers.append(i)

    return numbers


# результатом вызова этой функции будет список
create_list(5)


# -

# Использование библиотек

# +
# применим функцию mean() библиотеки Numpy для расчета среднего арифметического


# на входе наша функция примет список или массив чисел,
def mean_f(values: list[float]) -> float:
    """Рассчитать среднее арифметическое и прибавить единицу."""
    # рассчитает среднее арифметическое и прибавит единицу
    return float(np.mean(values)) + 1


# перед вызовом функции нужно не забыть импортировать соответствующую библиотеку

# и подготовить данные
sample_values: list[float] = [1, 2, 3]

mean_f(sample_values)
# -

# Глобальные и локальные переменные

# +
# создадим глобальную переменную вне функции
global_name = "Петр"


# а затем используем ее внутри новой функции
def show_name() -> None:
    """Вывести значение глобальной переменной global_name."""
    print(global_name)


show_name()

# +
# а теперь вначале создадим функцию,
# внутри которой объявим локальную переменную


def show_local_name() -> None:
    """Вывести значение локальной переменной local_name."""
    local_name = "Алена"  # pylint: disable=redefined-outer-name
    print(local_name)


show_local_name()
# -

# при попытке обратиться к переменной вне функции мы получим ошибку
local_name  # type: ignore[name-defined]  # pylint: disable=used-before-assignment

# +
# превратить локальную переменную в глобальную можно через ключевое слово global


def make_global() -> None:
    """Объявить local_name глобальной переменной."""
    global local_name  # pylint: disable=global-variable-undefined
    local_name = "Алена"  # type: ignore[name-defined]
    print(local_name)  # type: ignore[name-defined]


# -

make_global()

# теперь ошибки быть не должно
local_name  # type: ignore[name-defined]

# Lambda-функции

# +
# создадим функцию, которая принимает два числа и перемножает их
lf: Callable[[float, float], float] = (
    lambda a, b: a * b
)  # noqa: E731  # pylint: disable=unnecessary-lambda-assignment

# вызовем функцию и передадим ей числа 2 и 3
lf(2, 3)

# +
# этот же функционал можно поместить в обычную функцию


def normal_f(num1: float, num2: float) -> float:
    """Перемножить два числа."""
    return num1 * num2


normal_f(2, 3)
# -

# Lambda-функция внутри функции filter()

# создадим список
numbers_list = [15, 27, 9, 18, 3, 1, 4]
# напишем lambda-функцию, которая выведет True, если число больше 10, и False, если меньше
list(filter(lambda n: n > 10, numbers_list))

# Lambda-функция внутри функции sorted()

# +
# мы создали список из кортежей,
# и в каждом кортеже был индекс фильма и расстояние до него
indices_distances = [
    (901, 0.0),
    (1002, 0.22982440568634488),
    (442, 0.25401128310081567),
]

# lambda-функция возьмет каждый кортеж и вернет второй [1] его элемент
# передав эту функцию через параметр key, мы отсортируем список по расстоянию
sorted(indices_distances, key=lambda x: x[1], reverse=False)


# -

# *args и **kwargs


# +
# напишем функцию для расчета среднего арифметического двух чисел


def mean_two(num1: float, num2: float) -> float:
    """Рассчитать среднее арифметическое двух чисел."""
    return (num1 + num2) / 2


# +
# объявим функцию с *args для любого количетсва чисел


def mean(*nums: float) -> float:
    """Рассчитать среднее арифметическое произвольного количества чисел."""
    # в данном случае мы складываем элементы кортежа
    total = 0.0
    for i in nums:
        total += i

    return total / len(nums)


# -

mean(1, 2, 3, 4)

mean(*[1, 2, 3])

# +
# *nums превращается в кортеж, **params - в словарь


def simple_stats(*nums: float, **params: bool) -> None:
    """Вывести среднее арифметическое и/или стандартное отклонение чисел."""
    # если ключ 'mean' есть в словаре params и его значение == True
    if "mean" in params and params["mean"] is True:

        # рассчитаем среднее арифметическое и округлим
        # \t - это символ табуляции
        print(f"mean: \t{np.round(np.mean(nums), 3)}")

    # если ключ 'std' есть в словаре params и его значение == True
    if "std" in params and params["std"] is True:

        # рассчитаем СКО и округлим
        print(f"std: \t{np.round(np.std(nums), 3)}")


# -

# вызовем функцию simple_stats() и передадим ей числа и именованные аргументы
simple_stats(5, 10, 15, 20, mean=True, std=True)

# если для одного из параметров задать значение False,
# функция не выведет соответствующую метрику
simple_stats(5, 10, 15, 20, mean=True, std=False)

# +
# если мы хотим передать параметры списком и словарем,
list_ = [5, 10, 15, 20]
settings = {"mean": True, "std": True}

# то нам нужно использовать операторы распаковки * и ** соответственно
simple_stats(*list_, **settings)
