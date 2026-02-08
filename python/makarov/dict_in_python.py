"""Словарь в питоне."""

# ### Понятие словаря

# #### Создание словаря

# +
from collections import Counter
from pprint import pprint

import numpy as np

dict_1: dict[str, str] = {}
print(dict_1)
# -

company = {"name": "Toyota", "founded": 1937, "founder": "Kiichiro Toyoda"}
company

# из вложенных списков
tickers = dict([["TYO", "Toyota"], ["TSLA", "Tesla"], ["F", "Ford"]])
tickers

# +
# словарь с одинаковыми значениями и заданными ключами
keys = ("k1", "k2", "k3")
value0 = 0

empty_values = dict.fromkeys(keys, value0)
empty_values
# -

# #### Ключи и значения словаря

# Виды значений словаря

value_types = {
    "k1": 123,
    "k2": "string",
    # "k3": np.NaN,
    "k4": True,
    "k5": None,
    "k6": [1, 2, 3],
    "k7": np.array([1, 2, 3]),
    "k8": {1: "v1", 2: "v2", 3: "v3"},
}
value_types

# Методы .keys(), .values() и .items()

person: dict[str, str] = {
    "first name": "Иван",
    "last name": "Иванов",
    "born": "1980",
    "dept": "IT",
}

person.keys()

person.values()

person.items()

# Использование цикла for

for key, value in person.items():
    print(key, value)

# Доступ по ключу и метод .get()

person["last name"]

person["education"]

print(person.get("education"))

person.get("born")

# Проверка вхождения ключа и значения в словарь
"born" in person

# ### Операции со словарями

# #### Добавление и изменение элементов

person["languages"] = "Python"
person

# +
# присоединение словарей
new_elements = {"job": "программист", "experience": "7"}

person.update(new_elements)
person
# -

# метод .setdefault проверит есть ли ключ в словаре
# если "да", значение не изменится
person.setdefault("last name", "Петров")
person

# если нет, то будет добавлен ключ
# и соответствующее значение
person.setdefault("f_languages", "русский")
person

# Удаление элементов

# метод удаляет значение по ключу и выводит его
person.pop("dept")

person

del person["born"]

# удаляет последний добавленный элемент и выводит его
person.popitem()

# удаляет все элементы словаря
person.clear()
person

del person

person

# Сортировка словарей

dict_to_sort = {"k1": 30, "k2": 20, "k3": 10}

sorted(dict_to_sort)

sorted(dict_to_sort.values())

# cортировка по ключу
sorted(dict_to_sort.items(), key=lambda x: x[0])

# сортировка по значению
sorted(dict_to_sort.items(), key=lambda x: x[1])

# #### Копирование словарей

original = {"Первый курс": 174, "Второй курс": 131}

# Копирование с помощью метода .copy()

# +
new_1 = original.copy()
new_1["Третий курс"] = 117

print(original)
print(new_1)
# -

# Копирование через оператор присваивание `=`, две переменные указывают на один адрес

new_2 = original
new_2.clear()
print(original)
print(new_2)

# #### Функция `dir()`

some_dict = {"k": 1}
print(dir(some_dict)[:11])

print(some_dict)

print(str(some_dict))  # внутренний вызов __str__

print(dir(some_dict)[-11:])

# ### Dict comprehension

source_dict = {"k1": 2, "k2": 4, "k3": 6}

print({k: v * 2 for k, v in source_dict.items()})

print({k.upper(): v for k, v in source_dict.items()})

print({k: v for k, v in source_dict.items() if v > 2 if v < 6})

print({k: ("odd" if v % 2 else "even") for k, v in source_dict.items()})

# ### Дополнительные примеры

# #### lambda-функции, функции `map()` и `zip()`

# Пример со списком

words = ["apple", "banana", "fig", "blackberry"]

length = list(map(lambda word: len(word) - 1, words))
length

dict(zip(words, length))

dict(zip(words, [len(word) for word in words]))

# Пример со словарем

height_feet = {"Alex": 6.1, "Jerry": 5.4, "Ben": 5.8}

metres = list(map(lambda height_in_feet: height_in_feet * 0.3048, height_feet.values()))
metres

dict(zip(height_feet.keys(), np.round(metres, 2)))

print({k: np.round(v * 0.3048, 2) for k, v in height_feet.items()})

# #### Вложенные словари

employees: dict[str, dict[str, str]] = {
    "id1": {
        "first name": "Александр",
        "last name": "Иванов",
        "age": "30",
        "job": "программист",
    },
    "id2": {
        "first name": "Ольга",
        "last name": "Петрова",
        "age": "35",
        "job": "ML-engineer",
    },
}

for employee_info in employees.values():
    print(employee_info)

# Базовые операции

employees["id1"]["age"]

# +
# для лучшего вывода словарей

# +
employees["id3"] = {
    "first name": "Дарья",
    "last name": "Некрасова",
    "age": "27",
    "job": "веб-дизайнер",
}

# и выведем обновленный словарь с помощью функции pprint()
pprint(employees)
# -

employees["id3"]["age"] = "26"
pprint(employees)

# Циклы `for`

# +
for info in employees.values():
    info["age"] = str(float(info["age"]) + 1)

pprint(employees)
# -

# Вложенные словари и dict comprehension

pprint(
    {
        id: {k: (int(v) if k == "age" else v) for k, v in info.items()}
        for id, info in employees.items()
    }
)

# #### Частота слов в тексте

# возьмем знакомый нам текст
corpus = "When we were in Paris we visited a lot of museums. We first went"

words = corpus.split()
print(words)

# с помощью list comprehension удалим точки, запятые и переведем все слова в нижний регистр
words = [word.strip(".").strip(",").lower() for word in words]
print(words)

# Способ 1. Условие if-else

# +
bow_1: dict[str, int] = {}
for word in words:
    if word in bow_1:
        bow_1[word] += 1
    else:
        bow_1[word] = 1

print(sorted(bow_1.items(), key=lambda x: x[1], reverse=True)[:6])

# +
bow_2: dict[str, int] = {}

for word in words:
    bow_2[word] = bow_2.get(word, 0) + 1

print(sorted(bow_2.items(), key=lambda x: x[1], reverse=True)[:6])

# +
bow_3 = Counter(words)

bow_3.most_common(6)
# -

# ### Дополнительные материалы

# #### Изменяемые и неизменяемые типы данных

# Неизменяемый тип данных

string = "Python"
print(id(string), type(string), string)

string += " is cool"
print(id(string), type(string), string)

# Изменяемый тип данных

lst = [1, 2, 3]
print(id(lst), type(lst), lst)

lst.append(4)
print(id(lst), type(lst), lst)

# Копирование объектов

string = "Python"
string2 = string
string2 += " is cool"
print(string, string2)

# оператор == сравнивает значения (values)
# оператор is сравнивает identities
string == string2, string is string2

lst = [1, 2, 3]
lst2 = lst
lst2.append(4)
lst, lst2

lst == lst2, lst is lst2

lst = [1, 2, 3]
lst2 = lst.copy()
lst2.append(4)
lst, lst2

lst.append(4)
lst, lst2, lst == lst2, lst is lst2
