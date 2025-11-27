"""Словарь."""

# +
# # импортируем класс Counter
# from collections import Counter
# from pprint import pprint

# # ключи мы поместим в кортеж
# # Словарь — неупорядоченный набор элементов с доступом по ключу.
# # Пустой словарь можно инициализировать через
# фигурные скобки {} или функцию dict().
# from typing import Any, Dict, List, Tuple

# import numpy as np

# dict_1: Dict
# dict_2: Dict
# dict_1, dict_2 = {}, dict()
# print(dict_1, dict_2)

# +
# company: Dict[str, str | int]
# company = {"name": "Toyota", "founded": 1937, "founder": "Kiichiro Toyoda"}
# company

# +
# tickers: Dict[str, str]
# tickers = dict([["TYO", "Toyota"], ["TSLA", "Tesla"], ["F", "Ford"]])
# tickers

# +
# keys: Tuple[str]
# keys = ("k1", "k2", "k3")

# # значением каждого ключа будет 0,
# # если ничего не указывать, ключи получат значение None
# value = 0

# empty_k = dict.fromkeys(keys, value)
# empty_k

# +
# value_types: Dict[str, Any]

# value_types = {
#     "k1": 123,
#     "k2": "string",
#     "k3": np.NaN,  # тип "Пропущенное значение"
#     "k4": True,  # логическое значение
#     "k5": None,
#     "k6": [1, 2, 3],
#     "k7": np.array([1, 2, 3]),
#     "k8": {1: "v1", 2: "v2", 3: "v3"},
# }

# value_types

# +
# person: Dict[str, Any]
# person = {"first name": "Иван", "last name":
# "Иванов", "born": 1980, "dept": "IT"}

# +
# person.keys()

# +
# person.values()

# +
# person.items()

# +
# for k, v in person.items():
#     print(k, v)

# +
# person["last name"]

# +
# "born" in person

# +
# 1980 in person.values()

# +
# # обратите внимание, в данном случае новое значение -
# это список
# person["languages"] = ["Python", "C++"]
# person

# +
# # возьмем еще один словарь
# new_elements: Dict[str, str | int]
# new_elements = {"job": "программист", "experience": 7}

# # и присоединим его к существующему словарю с
# помощью метода .update()
# person.update(new_elements)
# person

# +
# person.setdefault("last name", "Петров")
# person

# +
# person.setdefault("f_languages", ["русский", "английский"])
# person

# +
# person.pop("dept")

# +
# # удаляемое значение не выводится
# del person["born"]

# +
# person.popitem()

# +
# person.clear()
# person

# +
# # возьмем несложный словарь
# dict_to_sort: Dict[str, int]
# dict_to_sort = {"k2": 30, "k1": 20, "k3": 10}

# +
# sorted(dict_to_sort)

# +
# # создадим исходный словарь с количеством студентов
# на первом и втором курсах университета
# original: Dict[str, int]
# original = {"Первый курс": 174, "Второй курс": 131}

# +
# # создадим копию исходного словаря
# с помощью метода .copy()
# new_1 = original.copy()

# # добавим информацию о третьем
# курсе в новый словарь
# new_1["Третий курс"] = 117

# # выведем исходный и новый словари
# print(original)
# print(new_1)

# +
# # передадим исходный словарь
# в новую переменную
# new_2 = original

# # удалим элементы нового словаря
# new_2.clear()

# # выведем исходный и новый словари
# print(original)
# print(new_2)

# +
# # создадим словарь,
# some_dict: Dict[str, int]
# some_dict = {"k": 1}

# # передадим его в функцию dir() и
# # выведем первые 11 элементов
# dir(some_dict)

# +
# # Dict comprehension
# # создадим еще один словарь
# source_dict: Dict[str, int]
# source_dict = {"k1": 2, "k2": 4, "k3": 6}

# +
# {k: v * 2 for (k, v) in source_dict.items()}

# +
# {k.upper(): v for (k, v) in source_dict.items()}

# +
# new_dict: Dict
# new_dict = {}

# for k, v in source_dict.items():
#     if v > 2 and v < 6:

# # если условия верны, записываем
# ключ и значение в новый словарь
#         new_dict[k] = v

# new_dict

# +
# words: List[str]
# words = ["apple", "banana", "fig", "blackberry"]

# +
# length = list(map(lambda word: len(word), words))
# length

# +
# dict(zip(words, length))

# +
# height_feet: Dict[str, float]
# height_feet = {"Alex": 6.1, "Jerry": 5.4, "Ben": 5.8}

# +
# # один фут равен 0,3048 метра
# metres: List[float]

# metres = list(map(lambda m: m * 0.3048, height_feet.values()))
# metres

# +
# employees = {
#     "id1": {
#         "first name": "Александр",
#         "last name": "Иванов",
#         "age": 30,
#         "job": "программист",
#     },
#     "id2": {
#         "first name": "Ольга",
#         "last name": "Петрова",
#         "age": 35,
#         "job": "ML-engineer",
#     },
# }

# +
# for v in employees.values():
#     print(v)

# +
# # первый ключ - нужный нам сотрудник,
# второй - элемент с информацией о нем
# employees["id1"]["age"]

# +
# # добавим информацию о новом сотруднике
# employees["id3"] = {
#     "first name": "Дарья",
#     "last name": "Некрасова",
#     "age": 27,
#     "job": "веб-дизайнер",
# }

# # и выведем обновленный словарь с
# помощью функции pprint()
# pprint(employees)

# +
# для этого вначале пройдемся по вложенным словарям,
# т.е. по значениям info внешнего словаря employees
# for info in employees.values():

# затем по ключам и значениям вложенного словаря info
#     for k, v in info.items():

# если ключ совпадет со словом 'age'
#         if k == "age":

# преобразуем значение в тип float
#           info[k] = float(v)

# pprint(employees)

# +
# corpus: str
# corpus = "When we were in Paris we
# visited a lot of museums. We first went
# to the Louvre, the largest art museum in the world.
# I have always been
# interested in art so I spent many hours there.
# The museum is enormous, so a week there would not be enough."

# +
# words = corpus.split()
# print(words)

# +
# words: List[str]
# words = [word.strip(".").strip(",").lower() for word in words]
# print(words)

# +
# создадим пустой словарь для мешка слов bow
# bow_1: Dict
# bow_1 = {}

# пройдемся по словам текста
# for word in words:

# если нам встретилось слово,
# которое уже есть в словаре
#     if word in bow_1:

#
# увеличим его значение (частоту) на 1
#         bow_1[word] = bow_1[word] + 1

#
# в противном случае,
# если слово встречается впервые
#     else:

#         # зададим ему значение 1
#         bow_1[word] = 1

# отсортируем словарь по
# значению в убываюем порядке (reverse = True)
# и выведем шесть
# наиболее частотных слов
# sorted(bow_1.items(), key=lambda x: x[1], reverse=True)[:6]

# +
# bow_2: Dict
# bow_2 = {}

# for word in words:
#     bow_2[word] = bow_2.get(word, 0) + 1

# sorted(bow_2.items(), key=lambda x: x[1], reverse=True)[:6]

# +
# # создадим объект этого класса,
# передав ему список слов
# bow_3 = Counter(words)

# # выведем шесть наиболее часто
# встречающихся слов с помощью метода .most_common()
# bow_3.most_common(6)
