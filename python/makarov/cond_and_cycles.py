"""Условия и циклы."""

# ### Условия

# Множественные условия (multi-way decisions)

# +
import numpy as np

number_value = 25

if number_value < 10:
    print("Small")
elif number_value < 100:
    print("Medium")
else:
    print("Large")

# +
user_input = input("Введите число: ")

number_value = int(user_input)
if number_value < 10:
    print("Small")
elif number_value < 100:
    print("Medium")
else:
    print("Large")
# -

# Вложенные условия (nested decisions)

# +
user_input = input("Введите число: ")

if len(user_input) != 0:
    number_value = int(user_input)

    if number_value < 10:
        print("Small")
    elif number_value < 100:
        print("Medium")
    else:
        print("Large")
else:
    print("Ввод пустой")
# -

# Несколько условий в одном выражении с операторами and или or

# +
number_value = 42

if 10 < number_value < 100:
    print("Medium")
else:
    print("Small or Large")

# +
number_value = 2

if number_value < 10 or number_value > 100:
    print("Small or Large")
else:
    print("Medium")
# -

# Проверка вхождения элемента в объект с in/not in

# +
sentence = "To be, or not to be, that is the question"
word = "question"

if word in sentence:
    print("Слово найдено")

# +
number_list = [2, 3, 4, 6, 7]
number = 5

if number not in number_list:
    print("Такого числа в списке нет")
# -

fruit_counts = {"apple": 3, "tomato": 6, "carrot": 2}

if "apple" in fruit_counts:
    print("Нашлись")

if 6 in fruit_counts.values():
    print("Есть")

# ### Циклы в Python

# Основные операции

# +
number_list = [1, 2, 3]

for number in number_list:
    print(number)
# -

products = {"apple": [3, "kg"], "tomato": [6, "pcs"], "carrot": [2, "kg"]}

for key, value in products.items():
    print(key, value)

for product_info in products.values():
    print(product_info[0])

# +
number_array = np.array([1, 2, 3])

for number in number_array:
    print(number)
# -

# Функция range()

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 6, 2):
    print(i)

# +
months = [
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

sales = [47, 75, 79, 94, 123, 209, 233, 214, 197, 130, 87, 55]

for month, sale in zip(months, sales):
    print(month, sale)
# -

# ### Последовательность в обратном порядке#

# Функция reversed()

# +
my_list = [0, 1, 2, 3, 4]

for i in reversed(my_list):
    print(i)
# -

for i in reversed(range(5)):
    print(i)

# Указать -1 в качестве параметров шага

for i in range(4, 0, -1):
    print(i)

for i in range(4, -1, -1):
    print(i)

# Функция sorted()

# +
range_value = range(5)

sorted_values = sorted(range_value, reverse=True)
for i in sorted_values:
    print(i)
# -

# Функция enumerate

# +
days = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]

for i, day in enumerate(days):
    print(i, day)
# -

for i, day in enumerate(days, 1):
    print(i, day)

# Цикл while

# +
i = 0

while i < 3:
    print("Текущее значение счётчика: " + str(i))
    i += 1
    print("Новое значение: " + str(i))

# +
i = 0

while i < 3:
    print(i)
    i += 1
# -

# ### Break, continue

# Оператор break

# +
clients = {
    1: {"name": "Анна", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Илья", "age": 18, "sex": "female", "revenue": 8000},
}

for client_id, info in clients.items():
    print(client_id, info)
    break
# -

number_value = 6
while number_value != 0:
    print(number_value)
    number_value -= 1
    if number_value == 3:
        break

# Оператор continue

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Форматирование строк через f-строки и метод .format()

# +
days = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]

Monday = days[0]
Monday
# -

print(f"{Monday} - день тяжелый")

# ### Ответы на вопросы

# Можно ли использовать цикл while с функцией range()?

# да но не оптимально
i = 1
while i in range(1, 11):
    print("Значение счётчика ", i)
    i += 1

# более оптимальный вид
for i in range(1, 11):
    print("Значение счётчика ", i)

# Можно ли обойтись без оператора continue в приведенном на занятии примере?

# да
for i in range(2, 11, 2):
    print(i)
