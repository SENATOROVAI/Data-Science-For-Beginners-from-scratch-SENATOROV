"""Функции в Питоне."""

# +
# # import matplotlib.pyplot as plt
# import numpy as np

# +
# данные в этой функции обозначаются через x
# plt.hist(bins = 10, x = height)
# plt.show()

# +
# у параметра bins есть аргумент по умолчанию (как раз 10 интервалов)
# а значит, этот параметр можно не указывать
# plt.hist(height)
# plt.show()

# +
# print("Первая строка")
# print()
# print("Третья строка")

# +
# # создаем строковый объект и
# some_string: str = "machine learning"

# # применяем к нему метод .title()
# some_string.title()
# print(some_string)

# +
# some_list: list[str] = ["machine", "learning"]
# # some_list.title()
# print(some_list)

# +
# # создадим функцию, которая удваивает
# # любое передаваемое ей значение
# def double(x_1: int) -> int:
#     """Удваиваем значение"""
#     res_1 = x_1 * 2
#     return res_1


# print(double(2))

# +
# тело функции не может быть пустым
# def only_return():
#
#
# нужно либо указать ключевое слово return
#  return

# +
# only_return()

# +
# # либо оператор pass
# def only_pass() -> None:
#     """pass."""
#     pass

# +
# print(only_return())

# +
# # объявим функцию с параметрами x и y,
# def calc_sum(x_2: int, y_2: int) -> int:
#     """возвращает сумму."""
#     return x_2 + y_2

# +
# print(calc_sum(1, y_2=2))

# +
# def calc_sum_default(x_3: int = 1, y_3: int = 2) -> int:
#     """Сумма двух."""
#     return x_3 + y_3


# print(calc_sum_default())

# +
# # эта функция просто выводит текст 'Some string'
# def print_string() -> None:
#     """эта функция просто выводит текст 'Some string'."""
#     print("Some string")


# print_string()

# +
# # укажем, что на входе функция принимает тип float, а возвращает int
# # значение 3,5 - это значение параметра x по умолчанию
# def f_4(x_4: float = 3.5) -> int:
#     """Возвращаем целое число."""
#     return int(x_4)

# +
# # желаемый тип данных можно посмотреть через атрибут __annotations__
# f_4.__annotations__

# +
# сохраним аннотации, но изменим суть функции
# def f_5(x_5: float) -> int:
#    """теперь вместо int она будет возвращать float."""
#    return float(x)

# +
# # вызовем объявленную выше функцию и умножим ее вывод на два
# print(calc_sum(1, 2) * 2)

# +
# def first_letter():
#  return 'Python'
#
# обратимся к первой букве слова Python
# first_letter()[0]

# +
# def use_input() -> int:
#     """запросим у пользователя число и переведем его в тип данных int."""
#     user_inp = int(input("Введите число: "))

#     # возведем число в квадрат
#     result_5: int = user_inp**2

#     # вернем результат
#     return result_5


# # вызовем функцию
# print(use_input())

# +
# # объявим функцию, которая на входе получает число,
# # а на выходе формирует список чисел от 0 до числа,
# # предшествующего заданному
# def create_list(x_6: int) -> list[int]:
#     """на выходе формирует список чисел от 0 до числа"""

#     # создадим пустой список
#     l_6: list[int] = []

#     # в цикле for создадим последовательность
#     for i_6 in range(x_6):
#         # и поместим ее в список
#         l_6.append(i_6)

#     return l_6


# # результатом вызова этой функции будет список
# print(create_list(5))

# +
# def tuple_f() -> tuple[str, int]:
#     """Кортеж строка/число."""
#     string_8: str = "Python"
#     x_8: int = 42
#     return string_8, x_8


# print(tuple_f())

# +
# a_9, b_9 = tuple_f()
# print(a_9, b_9)
# print(type(a_9), type(b_9))

# +
# c_10 = tuple_f()
# print(c_10)
# print(type(c_10))

# +
# # проверим равен ли нулю остаток от деления на два
# def if_divisible(x_11: int) -> bool:
#     """Остаток от деления на 2."""
#     if x_11 % 2 == 0:
#         return True
#     return False


# # попробуем с числом 10
# print(if_divisible(10))

# +
# # на входе функция примет список или массив x,
# def mean_f(x_12: list[int] = [1, 2, 3]) -> np.float64:
#     """СА."""

#     # рассчитает среднее арифметическое и прибавит единицу
#     return np.mean(x_12) + 1


# print(mean_f([1, 2, 3]))

# +
# # создадим глобальную переменную ВНЕ функции
# global_name: str = "Петр"

# # а затем используем ее внутри новой функции


# def show_name() -> None:
#     """Выводим глобальную переменную."""
#     print(global_name)


# show_name()

# +
# # а теперь вначале создадим функцию,
# # внутри которой объявим локальную переменную
# def show_local_name() -> None:
#     """Локальная переменная."""
#     local_name: str = "Алена"
#     print(local_name)


# show_local_name()

# +
# def make_global():
#  global local_name
#  local_name = 'Алена'
#  print(local_name)

# +
# # объявим глобальную переменную
# global_number_10: int = 5


# def print_number() -> None:
#     """Принтуем переменную global_number_10."""
#     # затем объявим локальную переменную
#     local_number: int = 10
#     print("Local number:", local_number)


# print_number()

# +
# создадим функцию, которая принимает два числа и перемножает их
# lf_20 = lambda a, b: a * b

# вызовем функцию и передадим ей числа 2 и 3
# lf_20(2, 3)

# +
# nums_21: list[int] = [15, 27, 9, 18, 3, 1, 4]

# +
# # буквально мы пишем:
# # "для каждого n, выдай True, если число больше 10, иначе - False"
# criterion = lambda n_20: True if (n_20 > 10) else False

# +
# print(list(filter(criterion, nums_21)))

# +
# print(list(filter(lambda n_21: True if (n_21 > 10) else False, nums_21)))

# +
# # обратите внимание на использование скобок
# print((lambda x: x * x)(10))

# +
# # объявим функцию
# def mean_22(a_22: int, b_22: int) -> float:
#     """СА 2."""

#     return (a_22 + b_22) / 2


# # и передадим ей числа 1 и 2
# print(mean_22(1, 2))

# +
# объявим функцию, которой нужно передать список
# def mean(list_):
#
#  # зададим переменную для суммы,
#  total = 0
#
#  # в цикле сложим все числа из списка
#  for i in list_:
#    total += i

# и разделим на количество элементов
#  return total / len(list_)

# +
# создадим список
# list_ = [1, 2, 3, 4]

# и передадим его в новую функцию
# mean(list_)

# +
# объявим функцию с *args
# def mean(*nums):
#  total = 0
#  for i in nums:
#    total += i
#  return total / len(nums)

# +
# def f(**kwargs):
#  return kwargs.items()
# -


