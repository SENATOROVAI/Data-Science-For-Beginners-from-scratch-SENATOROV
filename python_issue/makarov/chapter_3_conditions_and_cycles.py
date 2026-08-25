"""Conditions and cycles."""

# ## Условия и циклы. Продолжение

# #### Множественные условия (multi-way decisions)
#

# +
import numpy as np

x_var: int = 42

if x_var < 10:
    print("Small")
elif x_var < 100:
    print("Medium")
else:
    print("Large")

# +
x_var_1: str = input()

x_int = int(x_var_1)

if x_int < 10:
    print("Small")
elif x_int < 100:
    print("Medium")
else:
    print("Large")
# -

# #### Вложенные условия (nested decisions)
#

# +
y_var: str = input("Введите число: ")

if len(y_var) != 0:
    y_int = int(y_var)
    if y_int < 10:
        print("Small")
    elif y_int < 100:
        print("Medium")
    else:
        print("Large")
else:
    print("Ввод пустой")
# -

# #### Несколько условий в одном выражении с операторами and или or

# +
z_var: int = 42

if 10 < z_var < 100:
    print("Medium")
else:
    print("Small or Large")

# +
z_var_1: int = 2

if z_var_1 < 10 or z_var_1 > 100:
    print("Small or Large")
else:
    print("Medium")
# -

# #### Проверка вхождения элемента в объект с in / not in
#

# +
sentence: str = "To be, or not to be, that is the question"
word: str = "question"

if word in sentence:
    print("Слово найдено")
# -

# ## Циклы в Питоне

# ### Цикл for  Основные операции
#

# +
number_list: list[int] = [2, 3, 4, 6, 7]
number: int = 5

if number not in number_list:
    print("Такого числа в списке нет")

# +
d_var: dict[str, int] = {"apple": 3, "tomato": 6, "carrot": 2}

if "apple" in d_var:
    print("Нашлись")

if 6 in d_var.values():
    print("Есть")

# +
number_list_1: list[int] = [1, 2, 3]

for number in number_list_1:
    print(number)

# +
d_var_1: dict[str, list[int | str]] = {
    "apple": [3, "kg"],
    "tomato": [6, "pcs"],
    "carrot": [2, "kg"],
}

for k_var_1, v_var_1 in d_var_1.items():
    print(k_var_1, v_var_1)

for v_var_2 in d_var_1.values():
    print(v_var_2[0])

# +
number_array = np.array([1, 2, 3])

for number in number_array:
    print(number)

# +
clients_1: dict[int, dict[str, int | str]] = {
    1: {"name": "Анна", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Илья", "age": 18, "sex": "female", "revenue": 8000},
}

for id_var_1, info in clients_1.items():

    print("client ID:" + str(id_var_1))

    for k_var, v_var in info.items():
        print(k_var + ": " + str(v_var))

    print()
# -

# #### Функция range()
#

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 6, 2):
    print(i)

# +
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
sales: list[int] = [47, 75, 79, 94, 123, 209, 233, 214, 197, 130, 87, 55]

for i, month in enumerate(months):
    print(month, sales[i])
# -

# ### Последовательность в обратном порядке
#

# +
my_list: list[int] = [0, 1, 2, 3, 4]

for i in reversed(my_list):
    print(i)
# -

for i in reversed(range(5)):
    print(i)

for i in range(4, 0, -1):
    print(i)

# +
r_var: range = range(5)

sorted_values: list[int] = sorted(r_var, reverse=True)

for i in sorted_values:
    print(i)
# -

# #### Функция enumerate()
#

# +
days: list[str] = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

for i, day in enumerate(days):
    print(i, day)

for i, day in enumerate(days, 1):
    print(i, day)
# -

# ### Цикл while
#

# +
i_var: int = 0

while i_var < 3:
    print("Текущее значение счетчика: " + str(i))
    i_var = i_var + 1
    print("Новое значение счетчика :" + str(i))
    print()

# +
i_var_1: int = 0

while i_var_1 < 3:
    print(i_var_1)
    i_var_1 += 1
# -

# ### Break, continue
#

# +
clients_1_var: dict[int, dict[str, int | str]] = {
    1: {"name": "Анна", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Илья", "age": 18, "sex": "female", "revenue": 8000},
}

for id_var, info in clients_1_var.items():
    print(id_var, info)
    break

# +
x_var_2: int = 6

while x_var_2 != 0:
    print(x_var_2)
    x_var_2 -= 1
    if x_var_2 == 3:
        break
# -

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

# ### Форматирование строк через f-строки и метод .format()
#

# +
days_1: list[str] = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

monday: str = days_1[0]
print(monday)

print(f"{monday} - день тяжелый")
