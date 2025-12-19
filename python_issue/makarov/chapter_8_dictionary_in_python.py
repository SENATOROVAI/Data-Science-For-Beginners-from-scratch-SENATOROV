"""Dictionary in Python."""

# ## Словарь в Питоне

# ### Понятие словаря

# #### Создание словаря
#

# +
# Способ 3. Модуль collections
from collections import Counter
from pprint import pprint

import numpy as np

dict_1: dict[str, int] = {}
dict_2: dict[str, int] = {}
print(dict_1, dict_2)
# -

company = {"name": "Tayota", "founded": 1937, "founder": "Kiichiro Toyoda"}
company

tickers = dict([["TYO", "Toyota"], ["TSLA", "Tesla"], ["f", "Ford"]])
tickers

# +
keys = ("k1", "k2", "k3")
value = 0

empty_values = dict.fromkeys(keys, value)
empty_values
# -

# ### Ключи и значения словаря

# #### Виды значений словаря
#

# +
value_types = {
    "k1": 123,
    "k2": "string",
    "k3": np.nan,
    "k4": True,
    "k5": None,
    "k6": [1, 2, 3],
    "k7": np.array([1, 2, 3]),
    "k8": {1: "v1", 2: "v2", 3: "v3"},
}

value_types
# -

# #### Методы .keys(), .values() и .items()
#

# +
person = {"first name": "Ivan", "last name": "Ivanov", "born": 1980, "dept": "IT"}

print(person.keys())
print(person.values())
print(person.items())
# -

# #### Использование цикла for
#

for k_var, v_var in person.items():
    print(k_var, v_var)

# #### Доступ по ключу и метод .get()
#

person["last name"]

# +
# если такого ключа нет, Питон выдаст ошибку
# person['education']
# -

print(person.get("education"))

person.get("born")

# #### Проверка вхождения ключа и значения в словарь
#

print("born" in person)

print(1980 in person.values())

print(("born", 1980) in person.items())

# ### Операции со словарями

# #### Добавление и изменение элементов
#

person["languages"] = ["Python", "C++"]
person

person["languages"] = ["Python"]
person

# +
new_elements = {"job": "programmer", "experience": 7}

person.update(new_elements)
person
# -

person.setdefault("last name", "Petrov")
person

person.setdefault("f_languages", ["Russian", "English"])
person

# #### Удаление элементов
#

person.pop("dept")

person

del person["born"]

person.popitem()

person.clear()
person

del person

# +
# убедимся, что такого словаря больше нет
# person
# -

# #### Сортировка словарей
#

# +
dict_to_sort = {"k2": 30, "k1": 20, "k3": 10}

sorted(dict_to_sort)
# -

sorted(dict_to_sort.values())

dict_to_sort.items()

sorted(dict_to_sort.items(), key=lambda x: x[0])

sorted(dict_to_sort.items(), key=lambda x: x[1])

# ### Копирование словарей
#

original = {"first course": 174, "second course": 131}

# #### Копирование с помощью метода .copy()
#

# +
new_1 = original.copy()
new_1["Third course"] = 117

print(original)
print(new_1)
# -

# #### Копирование через оператор присваивания = (так делать не стоит!)
#

# +
new_2 = original

new_2.clear()

# из исходного словаря данные также удалились
print(original)
print(new_2)
# -

# ### Функция dir()
#

# +
some_dict = {"k": 1}

print(dir(some_dict)[:11])
# -

print(some_dict)  # ==
# some_dict.__str__()  # ==

# в большинстве случаев нас будут интересовать методы без '__'
print(dir(some_dict)[-11:])

# ### Dict comprehension
#

# +
source_dict = {"k1": 2, "k2": 4, "k3": 6}

print({k_var_1: v_var_1 * 2 for (k_var_1, v_var_1) in source_dict.items()})
# -

print({k_var_2.upper(): v_var_2 for (k_var_2, v_var_2) in source_dict.items()})

print(
    {k_var_3: v_var_3 for (k_var_3, v_var_3) in source_dict.items() if 2 < v_var_3 < 6}
)

# +
new_dict = {}

for k_var_4, v_var_4 in source_dict.items():
    if 2 < v_var_4 < 6:
        new_dict[k_var_4] = v_var_4

new_dict
# -

print(
    {
        k_var_5: ("even" if v_var_5 % 2 else "odd")
        for (k_var_5, v_var_5) in source_dict.items()
    }
)

# +
source_dict = {"k1": 2, "k2": 4, "k3": 6}

{k: 0 for k in keys}
# -

# ## Дополнительные примеры

# ### lambda-функции, функции map() и zip()

# #### Пример со списком

words = ["apple", "banana", "fig", "blackberry"]

length = list(map(len, words))
length

dict(zip(words, length))  # ==

dict(zip(words, [len(word) for word in words]))

# #### Пример со словарем
#

height_feet = {"Alex": 6.1, "Jerry": 5.4, "Ben": 5.8}

metres = list(map(lambda x: x * 0.3048, height_feet.values()))
metres

dict(zip(height_feet.keys(), np.round(metres, 2)))  # ==

print(
    {
        k_var_10: np.round(v_var_10 * 0.3048, 2)
        for (k_var_10, v_var_10) in height_feet.items()
    }
)
# ==

# #### Вложенные словари
#

employees: dict[str, dict[str, str | int | float]] = {
    "id1": {
        "first name": "Александр",
        "last name": "Иванов",
        "age": 30,
        "job": "программист",
    },
    "id2": {
        "first name": "Ольга",
        "last name": "Петрова",
        "age": 35,
        "job": "ML-engineer",
    },
}

for v_var_7 in employees.values():
    print(v_var_7)

# #### Базовый операции

# +
employees["id3"] = {
    "first name": "Дарья",
    "last name": "Некрасова",
    "age": 27,
    "job": "веб-дизайнер",
}

pprint(employees)

# +
employees["id3"]["age"] = 26

pprint(employees)
# -

# ### Циклы for

# +
for info in employees.values():
    for k_var_6, v_var_6 in info.items():
        if k_var_6 == "age":
            info[k_var_6] = float(v_var_6)

pprint(employees)
# -

# #### Вложенные словари и dict comprehension
#

pprint({id: info for id, info in employees.items()})

pprint(
    {
        emp_id: {
            k_var_7: (int(v_var_7) if k_var_7 == "age" else v_var_7)
            for k_var_7, v_var_7 in info.items()
        }
        for emp_id, info in employees.items()
    }
)

# #### Частота слов в тексте
#

corpus = """When we were in Paris we visited a lot of museums. We first went to 
            the Louvre, the largest art museum in the world. I have always been 
            interested in art so I spent many hours 
            there. The museum is enormous, so a week there would not be enough."""

# #### Предварительная обработка текста

words = corpus.split()
print(words)

words = [word.strip(",").strip(".").lower() for word in words]
words

# +
# Способ 1. Условие if-else
bow_1: dict[str, int] = {}

for word in words:
    if word in bow_1:
        bow_1[word] += 1
    else:
        bow_1[word] = 1

print(sorted(bow_1.items(), key=lambda x: x[1], reverse=True)[:6])

# +
# Способ 2. Метод .get()
bow_2: dict[str, int] = {}

for word in words:
    bow_2[word] = bow_2.get(word, 0) + 1

print(sorted(bow_2.items(), key=lambda x: x[1], reverse=True)[:6])
# -

bow_3 = Counter(words)
bow_3.most_common(6)

# ## Изменяемые и неизменяемые типы данных
#

# ### Неизменяемый тип данных
#

string = "Python"
print(id(string), type(string), string)

string = string + " is cool"
print(id(string), type(string), string)

# ### Изменяемый тип данных
#

lst = [1, 2, 3]
print(id(lst), type(lst), lst)

lst.append(4)
print(id(lst), type(lst), lst)

# #### Копирование объектов
#

# +
string = "python"
string2 = string
string2 = string2 + " is cool"

string2, string
# -

string == string2, string is string2

# +
lst = [1, 2, 3]

lst2 = lst
lst2.append(4)

lst, lst2
# -

lst == lst2, lst is lst2

# +
lst = [1, 2, 3]
lst2 = lst.copy()

lst2.append(4)

lst, lst2

# +
lst.append(4)

lst, lst2, lst == lst2, lst is lst2
