"""Макаров.

Словарь в Питоне
"""

# ## Словарь в Питоне

# ### Понятие словаря

# #### Создание словаря

# +
# пустой словарь можно создать с помощью {} или функции dict()
# импортируем класс Counter
from collections import Counter

# импортируем функцию pprint() из модуля pprint
# некоторые структуры данных она выводит лучше, чем обычная print()
from pprint import pprint

import numpy as np

dict_1: dict[str, str] = {}
dict_2: dict[str, str] = dict()  # pylint: disable=R1735
print(dict_1, dict_2)
# -

# словарь можно сразу заполнить ключами и значениями
company: dict[str, str | int] = {
    "name": "Toyota",
    "founded": 1937,
    "founder": "Kiichiro Toyoda",
}
company

# словарь можно создать из вложенных списков
tickers: dict[str, str] = dict([["TYO", "Toyota"], ["TSLA", "Tesla"], ["F", "Ford"]])
tickers

# +
# если поместить ключи в кортеж
keys: tuple[str, ...] = ("k1", "k2", "k3")
# и задать значение
value_global = 0

# то с помощью метода .fromkeys() можно создать словарь
# с этими ключами и заданным значением для каждого из них
empty_values = dict.fromkeys(keys, value_global)
empty_values
# -

# #### Ключи и значения словаря

# Виды значений словаря

# +
# приведем пример того, какими могут быть значения словаря
value_types: dict[str, int | str | bool | None | list[int] | object | float] = {
    "k1": 123,
    "k2": "string",
    "k3": np.nan,  # тип "Пропущенное значение"
    "k4": True,  # логическое значение
    "k5": None,
    "k6": [1, 2, 3],
    "k7": np.array([1, 2, 3]),
    "k8": {1: "v1", 2: "v2", 3: "v3"},
}

value_types
# -

# Методы .keys(), .values() и .items()

# создадим несложный словарь с информацией о сотруднике
person: dict[str, str | int | list[str]] = {
    "first name": "Иван",
    "last name": "Иванов",
    "born": 1980,
    "dept": "IT",
}

# посмотрим на ключи и
print(person.keys())

# значения
print(person.values())

# а также на пары ключ-значение в виде списка из кортежей
print(person.items())

# Использование цикла for

# ключи и значения можно вывести в цикле for
for key, value_p in person.items():
    print(key, value_p)

# Доступ по ключу и метод .get()

# значение можно посмотреть по ключу
person["last name"]

# +
# если такого ключа нет, Питон выдаст ошибку
# person['education'] --> Error
# -

# чтобы этого не произошло, можно использовать метод .get()
# по умолчанию при отсутствии ключа он выводит значение None
print(person.get("education"))

# если ключ все-таки есть, .get() выведет соответствующее значение
print(person.get("born"))

# Проверка вхождения ключа и значения в словарь

# проверим есть ли такой ключ
print("born" in person)

# и такое значение
print(1980 in person.values())

# можно также проверить наличие и ключа, и значения одновременно
print(("born", 1980) in person.items())

# ### Операции со словарями

# #### Добавление и изменение элементов

# добавить элемент можно, передав новому ключу новое значение
# обратите внимание, в данном случае новое значение - это список
person["languages"] = ["Python", "C++"]
person

# изменить элемент можно, передав существующему ключу новое значение,
# значение - это по-прежнему список, но из одного элемента
person["languages"] = ["Python"]
person

# +
# возьмем еще один словарь
new_elements: dict[str, str | int] = {"job": "программист", "experience": 7}

# и присоединим его к существующему словарю с помощью метода .update()
person.update(new_elements)
person
# -

# метод .setdefault() проверит есть ли ключ в словаре,
# если "да", значение не изменится
person.setdefault("last name", "Петров")
person

# если нет, будет добавлен новый ключ и соответствующее значение
person.setdefault("f_languages", ["русский", "английский"])
person

# #### Удаление элементов

# метод .pop() удаляет элемент по ключу и выводит удаляемое значение
print(person.pop("dept"))

# мы видим, что пары 'dept' : 'IT' больше нет
person

# ключевое слово del также удаляет элемент по ключу
# удаляемое значение не выводится
del person["born"]

# метод .popitem() удаляет последний добавленный элемент и выводит его
person.popitem()

# метод .clear() удаляет все элементы словаря
person.clear()
person

# ключевое слово del также позволяет удалить словарь целиком
del person

# убедимся, что такого словаря больше нет
person

# #### Сортировка словарей

# возьмем несложный словарь
dict_to_sort: dict[str, int] = {"k2": 30, "k1": 20, "k3": 10}

# отсортируем ключи
sorted(dict_to_sort)

# и значения
sorted(dict_to_sort.values())

# посмотрим на пары ключ : значение
dict_to_sort.items()

# для их сортировки по ключу (индекс [0])
# воспользуемся методом .items() и lambda-функцией
sorted(dict_to_sort.items(), key=lambda item: item[0])

# сортировка по значению выполняется так же, однако
# lambda-функции мы передаем индекс [1]
sorted(dict_to_sort.items(), key=lambda item: item[1])

# #### Копирование словарей

# создадим исходный словарь с количеством студентов на первом и втором курсах университета
original: dict[str, int] = {"Первый курс": 174, "Второй курс": 131}

# Копирование с помощью метода .copy()

# +
# создадим копию этого словаря с помощью метода .copy()
new_1 = original.copy()

# добавим информацию о третьем курсе в новый словарь
new_1["Третий курс"] = 117

# исходный словарь не изменился
print(original)
print(new_1)
# -

# Копирование через оператор присваивания `=` (так делать не стоит!)

# +
# передадим исходный словарь в новую переменную
new_2 = original

# удалим элементы нового словаря
new_2.clear()

# из исходного словаря данные также удалились
print(original)
print(new_2)
# -

# ### Функция `dir()`

# +
# функция dir() возвращает все методы передаваемого ей объекта
some_dict = {"k": 1}

# вначале идут специальные методы,
# они начинаются и заканчиваются символом '__'
# выведем первые 11 элементов
print(dir(some_dict)[:11])
# -

# когда мы передаем наш словарь функции print(),
print(some_dict)

# на самом деле мы применяем к объекту метод .__str__()
some_dict.__str__()  # pylint: disable=C2801

# +
# в большинстве случаев нас будут интересовать методы без '__'
methods = dir(some_dict)[-11:]

print(methods)
# -

# ### Dict comprehension

# создадим еще один несложный словарь
source_dict: dict[str, int] = {"k1": 2, "k2": 4, "k3": 6}

# с помощью dict comprehension умножим каждое значение на два
new_source_dict = {key: value * 2 for (key, value) in source_dict.items()}

# сделаем символы всех ключей заглавными
new_source_dict = {key.upper(): value for (key, value) in source_dict.items()}

# +
# добавим условие, что значение должно быть больше двух И меньше шести
new_dict_1 = {
    key: value for (key, value) in source_dict.items() if value > 2 if value < 6
}

print(new_dict_1)

# +
new_dict: dict[str, int] = {}

# при решении этой же задачи в цикле for
for key, value in source_dict.items():

    # мы бы использовали логическое И (and)
    if 2 < value < 6:

        # если условия верны, записываем ключ и значение в новый словарь
        new_dict[key] = value

new_dict
# -

# условие с if-else ставится в самом начале схемы dict comprehension
# заменим значение на слово even, если оно четное, и odd, если нечетное
even_odd_dict: dict[str, str] = {
    key: ("even" if value % 2 == 0 else "odd") for (key, value) in source_dict.items()
}

# +
# dict comprehension можно использовать вместо метода .fromkeys()
keys = ("k1", "k2", "k3")

# передадим словарю ключи из кортежа keys и зададим значение 0 каждому из них
zeros_dict = {key: 0 for key in keys}
# -

# ### Дополнительные примеры

# #### lambda-функции, функции `map()` и `zip()`

# Пример со списком

# возьмем список слов
words: list[str] = ["apple", "banana", "fig", "blackberry"]

# создадим lambda-функцию, которая посчитает длину передаваемого ей слова
# с помощью функции map() применим lambda-функцию
# к каждому элементу списка words
# и поместим длины слов в новый список length с помощью функции list()
length = list(map(len, words))
length

# с помощью функции zip() поэлементно соединим оба списка и
# преобразуем в словарь
from_zip_dict = dict(zip(words, length))

# то же самое можно сделать с помощью функции zip() и list comprehension
zip_length_dict = dict(zip(words, [len(word) for word in words]))

# Пример со словарем

# возьмем словарь с ростом людей в футах
height_feet: dict[str, float] = {"Alex": 6.1, "Jerry": 5.4, "Ben": 5.8}

# для преобразования футов в метры создадим lambda-функцию lambda m: m * 0.3048
# применим эту функцию к значениям словаря с помощью функции map()
# преобразуем в список
metres = list(map(lambda m: m * 0.3048, height_feet.values()))
metres

# с помощью функции zip() соединим ключи исходного словаря с элементами списка metres
dict(zip(height_feet.keys(), np.round(metres, 2)))

# то же самое можно выполнить с помощью dict comprehensions
# всего в одну строчку
# мы просто преобразуем значения словаря в метры
students_heights_dict = {
    key: np.round(value * 0.3048, 2) for (key, value) in height_feet.items()
}

# #### Вложенные словари

# возьмем словарь, ключами которого будут id сотрудников
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

# а значениями - вложенные словари с информацией о них
for value_e in employees.values():
    print(value_e)

# ##### Базовый операции

# для того чтобы вывести значение элемента вложенного словаря,
# воспользуемся двойным ключом
print(employees["id1"]["age"])

# +
# добавим информацию о новом сотруднике
employees["id3"] = {
    "first name": "Дарья",
    "last name": "Некрасова",
    "age": 27,
    "job": "веб-дизайнер",
}

# и выведем обновленный словарь с помощью функции pprint()
pprint(employees)
# -

# изменить значение вложенного словаря можно также с помощью двойного ключа
employees["id3"]["age"] = 26
pprint(employees)

# ##### Циклы `for`

# +
# заменим тип данных в информации о возрасте с int на float

# для этого вначале пройдемся по вложенным словарям,
# т.е. по значениям info внешнего словаря employees
for info in employees.values():

    # затем по ключам и значениям вложенного словаря info
    for key_info, value_info in info.items():

        # если ключ совпадет со словом 'age'
        if key_info == "age":

            # преобразуем значение в тип float
            info[key_info] = float(value_info)

pprint(employees)
# -

# ##### Вложенные словари и dict comprehension

# преоразуем обратно из float в int, но уже через dict comprehension
# для начала просто выведем словарь employees без изменений
pprint({id: info for id, info in employees.items()})

# а затем заменим значение внешнего словаря info (т.е. вложенный словарь)
# на еще один dict comprehension с условием if-else
pprint(
    {
        id: {
            key: (int(value_i) if key == "age" else value_i)
            for key, value_i in info.items()
        }
        for id, info in employees.items()
    }
)

# #### Частота слов в тексте

# возьмем знакомый нам текст
corpus = (
    "When we were in Paris we visited a lot of museums. "
    "We first went to the Louvre, the largest art museum in the world."
    "I have always been interested in art so I spent many hours there. "
    "The museum is enormous, so a week there would not be enough."
)

# ##### Предварительная обработка текста

# разделим его на слова
words = corpus.split()
print(words)

# с помощью list comprehension удалим точки, запятые
# и переведем все слова в нижний регистр
words = [word.strip(".").strip(",").lower() for word in words]
print(words)

# ##### Способ 1. Условие if-else

# +
# создадим пустой словарь для мешка слов bow
bow_1: dict[str, int] = {}

# пройдемся по словам текста
for word in words:

    # если нам встретилось слово, которое уже есть в словаре
    if word in bow_1:

        # увеличим его значение (частоту) на 1
        bow_1[word] = bow_1[word] + 1

    # в противном случае, если слово встречается впервые
    else:

        # зададим ему значение 1
        bow_1[word] = 1

# отсортируем словарь по значению в убываюем порядке (reverse = True)
# и выведем шесть наиболее частотных слов
print(sorted(bow_1.items(), key=lambda item: item[1], reverse=True)[:6])
# -

# ##### Способ 2. Метод .get()

# +
bow_2: dict[str, int] = {}

# снова пройдемся в цикле по словам
for word in words:

    # если слова еще нет в словаре, .get() выведет значение 0,
    # к которому мы прибавим единицу
    # если слово есть, метод .get() выведет существующее значение,
    # например, 2 или 3,
    # и мы также увеличим счетчик на 1
    bow_2[word] = bow_2.get(word, 0) + 1

# выведем наиболее популярные слова
print(sorted(bow_2.items(), key=lambda item: item[1], reverse=True)[:6])
# -

# ##### Способ 3. Модуль collections

# +
# создадим объект этого класса, передав ему список слов
bow_3 = Counter(words)

# выведем шесть наиболее часто встречающихся слов с помощью метода .most_common()
bow_3.most_common(6)
# -

# ### Дополнительные материалы

# #### Изменяемые и неизменяемые типы данных

# Неизменяемый тип данных

# +
# создадим строковый объект
string = "Python"

# посмотрим на identity, type и value
# функция id() выводит адрес объекта в памяти компьютера
print(id(string), type(string), string)

# +
# попробуем изменить этот объект
string = string + " is cool"

# посмотрим на identity, type и value
print(id(string), type(string), string)
# -

# Изменяемый тип данных

# +
# создадим список
lst: list[int] = [1, 2, 3]

# посмотрим на identity, type и value
print(id(lst), type(lst), lst)

# +
# добавим элемент в список
lst.append(4)

# снова выведем identity, type и value
print(id(lst), type(lst), lst)
# -

# Копирование объектов

# +
# вновь создадим строку
string = "Python"

# скопируем через присваивание
string2 = string

# изменим копию
string2 = string2 + " is cool"

# посмотрим на результат
print(string, string2)
# -

# оператор == сравнивает значения (values)
# оператор is сравнивает identities
print(string == string2, string is string2)

# +
# создадим список
lst = [1, 2, 3]

# скопируем его в новую переменную через присваивание
lst2 = lst

# добавим новый элемент в скопированный список
lst2.append(4)

# выведем исходный список и копию
print(lst, lst2)
# -

# убедимся, что речь идет об одном и том же объекте
print(lst == lst2, lst is lst2)

# +
# вновь создадим список
lst = [1, 2, 3]

# скопируем с помощью метода .copy()
lst2 = lst.copy()

# добавим новый элемент в скопированный список
lst2.append(4)

# выведем исходный список и копию
print(lst, lst2)

# +
# теперь сделаем значения списков одинаковыми
lst.append(4)

# и убедимся, что это по-прежнему разные объекты
print(lst, lst2, lst == lst2, lst is lst2)
# -
