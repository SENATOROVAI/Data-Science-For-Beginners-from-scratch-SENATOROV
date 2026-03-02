"""Условные операторы и циклы в python."""

# ## Условия и циклы. Продолжение

# ### Еще раз про условия с if

# Множественные условия (multi-way decisions)

import numpy as np

# +
# напишем программу, которая разобьет все числа на малые, средние и большие
number_size: int = 42

# и пропишем условия (не забывайте про двоеточие и отступ)
if number_size < 10:  # noqa: F841
    print("Small")
elif number_size < 100:
    print("Medium")
else:
    print("Large")

# +
# запросим число у пользователя
user_input_1: str = input("Введите число: ")

# преобразуем в тип int
number_user: int = int(user_input_1)

# и наконец классифицируем
if number_user < 10:
    print("Small")
elif number_user < 100:
    print("Medium")
else:
    print("Large")
# -

# Вложенные условия (nested decisions)

# +
# запрашиваем число
user_input_2: str = input("Введите число: ")  # noqa: F811

# проверяем первое условие (не пустая ли строка), если оно выполняется
if len(user_input_2) != 0:

    # преобразуем в тип int
    number_nested: int = int(user_input_2)  # noqa: F811

    # и классифицируем
    if 10 <= number_nested < 100:
        print("Medium")
    elif number_nested < 10:
        print("Small")
    else:
        print("Large")

# в противном, говорим, что ввод пустой
else:
    print("Ввод пустой")
# -

# Несколько условий в одном выражении с операторами and или or

# +
# пример с and (логическим И)
number_and: int = 42  # noqa: F811

# если number больше 10 и одновременно меньше 100
if 10 < number_and < 100:

    # у нас среднее число
    print("Medium")

# в противном случае оно либо маленькое либо большое
else:
    print("Small or Large")

# +
# пример с or (логическим ИЛИ)
number_or: int = 2  # noqa: F811

# если number меньше 10 или больше 100
if number_or < 10 or number_or > 100:

    # оно либо маленькое либо большое
    print("Small or Large")

# в противном случае оно среднее
else:
    print("Medium")
# -

# Проверка вхождения элемента в объект с in / not in

# +
# можно проверить вхождение слова в строку
sentence: str = "To be, or not to be, that is the question"
word: str = "question"

if word in sentence:
    print("Слово найдено")

# +
# или отсутствие элемента в списке
number_list_check: list[int] = [2, 3, 4, 6, 7]
number_check: int = 5

if number_check not in number_list_check:
    print("Такого числа в списке нет")

# +
# кроме того, можно проверить вхождение ключа и значения в словарь

# возьмем очень простой словарь
products: dict[str, int] = {"apple": 3, "tomato": 6, "carrot": 2}
# -

# вначале поищем яблоки среди ключей словаря
if "apple" in products:
    print("Нашлись")

# а затем посмотрим, нет ли числа 6 среди его значений
# с помощью метода .values()
if 6 in products.values():
    print("Есть")

# ### Циклы в Питоне

# #### Цикл for

# Основные операции

# +
# поочередно выведем элементы списка
number_list_for: list[int] = [1, 2, 3]  # noqa: F811

# не забывая про двоеточие и отступ
for number in number_list_for:
    print(number)
# -

# создадим словарь, значениями которого будут списки из двух элементов
products_list: dict[str, list[str | int]] = {
    "apple": [3, "kg"],
    "tomato": [6, "pcs"],
    "carrot": [2, "kg"],
}

# затем создадим две переменные-контейнера и применим метод .items()
for product_name, product_info in products_list.items():
    print(product_name, product_info)

# возьмем только одну переменную и применим метод .values()
for product_info in products_list.values():
    # значение представляет собой список, выведем его первый элемент с индексом [0]
    print(product_info[0])

# +
# создадим массив и поместим в переменную number_array
number_array: list[int] = list(np.array([1, 2, 3]))

# пройдемся по нему с помощью цикла for
for number in number_array:
    print(number)
# -

# предположим, что у нас есть следующая база данных клиентов
clients_db: dict[int, dict[str, str | int]] = {
    1: {"name": "Анна", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Илья", "age": 18, "sex": "female", "revenue": 8000},
}

# в первом цикле for поместим client_id и информацию о клиентах в переменные
for client_id, client_info in clients_db.items():

    # выведем id клиента
    print(f"client ID: {client_id}")

    # во втором цикле возьмем информацию об этом клиенте (это тоже словарь)
    for key, value in client_info.items():

        # и выведем каждый ключ (название поля) и значение (саму информацию)
        print(f"{key}: {value}")

    # добавим пустую строку после того, как выведем информацию об одном клиенте
    print()

# создадим последовательность от 0 до 4
for index in range(5):
    print(index)

# от 1 до 5
for index in range(1, 6):
    print(index)

# и от 0 до 5 с шагом 2 (то есть будем выводить числа через одно)
for index in range(0, 6, 2):
    print(index)

# +
# возьмем месяцы года
months: list[str] = [
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
]

# и продажи мороженого в тыс. рублей в каждый из месяцев
sales: list[int] = [47, 75, 79, 94, 123, 209, 233, 214, 197, 130, 87, 55]

# задав последовательность через enumerate(),
for month, sale in zip(months, sales):

    # мы можем вывести каждый из элементов обоих списков в одном цикле
    print(month, sale)
# -

# Последовательность в обратном порядке

# **Способ 1.** Функция reversed()

# +
# создадим список
my_list: list[int] = [0, 1, 2, 3, 4]

# передадим его функции reversed() и
# выведем каждый из элементов списка с помощью цикла for
for value in reversed(my_list):
    print(value)
# -

for value in reversed(range(5)):
    print(value)

# **Способ 2**. Указать $-1$ в качестве параметра шага

# первым параметром укажем конечный элемент списка,
# а вторым - начальный
for value in range(4, 0, -1):
    print(value)

# чтобы вывести 0, вторым параметром нужно указать -1
for value in range(4, -1, -1):
    print(value)

# **Способ 3**. Функция sorted()

# +
# создадим последовательность от 0 до 4
sequence: range = range(5)

# отсортируем ее по убыванию
sorted_values: list[int] = sorted(sequence, reverse=True)

# выведем элементы отсортированной последовательности
for value in sorted_values:
    print(value)
# -

# ##### Функция enumerate()

# +
# пусть дан список с днями недели
days_enum: list[str] = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

# выведем индекс (i) и сами элементы списка (day)
for index, day in enumerate(days_enum):
    print(index, day)
# -

# так же выведем индекс и элементы списка, но начнем с 1
for index, day in enumerate(days_enum, 1):
    print(index, day)

# #### Цикл while

# +
# зададим начальное значение счетчика
counter_1: int = 0  # noqa: F811

# пока счетчик меньше трех
while counter_1 < 3:

    # в каждом цикле будем выводить его текущее значение
    print(f"Текущее значение счетчика:  {counter_1}")

    # внутри цикла не забудем "нарастить" счетчик
    counter_1 = counter_1 + 1

    # и выведем новое значение
    print(f"Новое значение счетчика:    {counter_1}")

    # добавим пустую строку
    print()

# +
# тот же код можно упростить
counter_2: int = 0  # noqa: F811

while counter_2 < 3:
    print(counter_2)
    # в частности, оператор += сразу увеличивает и присваивает новое значение
    counter_2 += 1
# -

# #### Break, continue

# Оператор break

# +
# вновь возьмем словарь clients
clients_break: dict[int, dict[str, str | int]] = {
    1: {"name": "Анна", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Илья", "age": 18, "sex": "female", "revenue": 8000},
}  # noqa: F811

# в цикле пройдемся по ключам и значениям словаря
for client_id, client_info in clients_break.items():

    # и выведем их
    print(client_id, client_info)

    # однако уже после первого исполнения цикла, прервем его
    break

# +
# начальное значение счетчика
countdown: int = 6

# будем исполнять цикл пока countdown не равен нулю
while countdown != 0:

    # выведем текущее значение счетчика
    print(countdown)

    # и уменьшим (!) его на 1
    countdown -= 1

    # если значение счетчика станет равным 3, прервем цикл
    if countdown == 3:
        break
# -

# Оператор continue

# +
# выведем все четные числа в диапазоне от 1 до 10 включительно.

# с помощью функции range() создадим последовательность от 1 до 10
for number in range(1, 11):

    # если остаток от деления на два не равен нулю (то есть число нечетное)
    if number % 2 != 0:

        # идем к следующему числу последовательности
        continue

    # в противном случае выводим число
    print(number)
# -

# #### Форматирование строк через f-строки и метод .format()

# +
# снова возьмем список с днями недели
days_format: list[str] = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

# и для простоты поместим слово "Понедельник" в переменную monday
monday: str = days_format[0]
monday
# -

# теперь напишем фразу "Понедельник - день тяжелый" следующим образом
print(f"{monday} - день тяжелый")

# +
# то же самое можно вывести с помощью метода .format()
# print("{} - день тяжелый".format(monday))
# -

# ### Ответы на вопросы к занятию

# **Вопрос**. Можно ли использовать цикл while с функцией range()?

# +
# с функцией range() можно использовать цикл while, но такое решение не оптимально
# приведем пример с while

counter_range: int = 1  # noqa: F811

while counter_range in range(1, 11):
    print("Значение счетчика ", counter_range)
    counter_range += 1
# -

# более оптимальный код
for counter_opt in range(1, 11):
    print("Значение счетчика ", counter_opt)

for number_even in range(1, 11):
    # если число четное, выведем его
    if number_even % 2 == 0:
        print(number_even)
