"""Dictionaries."""

# +
from collections import Counter
from pprint import pprint

import numpy as np

# -

# пустой словарь можно создать с помощью {} или функции dict()
dict_1: dict[object, object] = {}
dict_2: dict[object, object] = dict()  # pylint: disable=use-dict-literal
print(dict_1, dict_2)

# словарь можно сразу заполнить ключами и значениями
company = {"name": "Toyota", "founded": 1937, "founder": "Kiichiro Toyoda"}
print(company)
# словарь можно создать из вложенных списков
tickers = dict([["TYO", "Toyota"], ["TSLA", "Tesla"], ["F", "Ford"]])
print(tickers)

# +
# если поместить ключи в кортеж
keys = ("k1", "k2", "k3")
# и задать значение
value = 0

# то с помощью метода .fromkeys() можно создать словарь
# с этими ключами и заданным значением для каждого из них
empty_values = dict.fromkeys(keys, value)
empty_values
# -

# создадим несложный словарь с информацией о сотруднике
person = {"first name": "Иван", "last name": "Иванов", "born": 1980, "dept": "IT"}

# посмотрим на ключи и значения
print(person.keys())
print(person.values())
# а также на пары ключ-значение в виде списка из кортежей
print(person.items())

# +
# Использование цикла for

# ключи и значения можно вывести в цикле for
for key, person_value in person.items():
    print(key, person_value)
# -

# значение можно посмотреть по ключу
person["last name"]

# если такого ключа нет, Питон выдаст ошибку
person["education"]

# чтобы этого не произошло, можно использовать метод .get()
# по умолчанию при отсутствии ключа он выводит значение None
print(person.get("education"))
# если ключ все-таки есть, .get() выведет соответствующее значение
person.get("born")

# проверим есть ли такой ключ
print("born" in person)
# и такое значение
print(1980 in person.values())
# можно также проверить наличие и ключа, и значения одновременно
print(("born", 1980) in person.items())

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
new_elements = {"job": "программист", "experience": 7}

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

# метод .pop() удаляет элемент по ключу и выводит удаляемое значение
person.pop("dept")

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
print(person)  # type: ignore[misc]  # pylint: disable=used-before-assignment

dict_to_sort = {"k2": 30, "k1": 20, "k3": 10}
# отсортируем ключи
print(sorted(dict_to_sort))
# и значения
print(sorted(dict_to_sort.values()))

# посмотрим на пары ключ : значение
print(dict_to_sort.items())
# для их сортировки по ключу (индекс [0])
# воспользуемся методом .items() и lambda-функцией
print(sorted(dict_to_sort.items(), key=lambda x: x[0]))
# сортировка по значению выполняется так же, однако
# lambda-функции мы передаем индекс [1]
print(sorted(dict_to_sort.items(), key=lambda x: x[1]))

# Dict comprehension

# +
source_dict = {"k1": 2, "k2": 4, "k3": 6}

# с помощью dict comprehension умножим каждое значение на два
print({key: val * 2 for (key, val) in source_dict.items()})
# -

# сделаем символы всех ключей заглавными
print({key.upper(): val for (key, val) in source_dict.items()})

# добавим условие, что значение должно быть больше двух И меньше шести
print({key: val for (key, val) in source_dict.items() if val > 2 if val < 6})

# условие с if-else ставится в самом начале схемы dict comprehension
# заменим значение на слово even, если оно четное, и odd, если нечетное
print({key: ("even" if val % 2 == 0 else "odd") for (key, val) in source_dict.items()})

words = ["apple", "banana", "fig", "blackberry"]
# создадим lambda-функцию, которая посчитает длину передаваемого ей слова
# с помощью функции map() применим lambda-функцию к каждому элементу списка words
# и поместим длины слов в новый список length с помощью функции list()
length = list(map(len, words))
length

# с помощью функции zip() поэлементно соединим оба списка и преобразуем в словарь
dict(zip(words, length))

# то же самое можно сделать с помощью функции zip() и list comprehension
dict(zip(words, [len(word) for word in words]))

# возьмем словарь с ростом людей в футах
height_feet = {"Alex": 6.1, "Jerry": 5.4, "Ben": 5.8}
# для преобразования футов в метры m * 0.3048
# мы просто преобразуем значения словаря в метры
print({key: np.round(val * 0.3048, 2) for (key, val) in height_feet.items()})


# +
# Вложенные словари

# возьмем словарь, ключами которого будут id сотрудников
employees = {
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
for employee_info in employees.values():
    print(employee_info)
# -

# для того чтобы вывести значение элемента вложенного словаря,
# воспользуемся двойным ключом
employees["id1"]["age"]

# +
# импортируем функцию pprint() из модуля pprint
# некоторые структуры данных она выводит лучше, чем обычная print()
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

# Частота слов в тексте

# возьмем знакомый нам текст
corpus = (
    "When we were in Paris we visited a lot of museums. "
    "We first went to the Louvre, the largest art museum in the world. "
    "I have always been interested in art so I spent many hours there. "
    "The museum is enormous, so a week there would not be enough."
)

# разделим его на слова
words = corpus.split()
print(words)

# с помощью list comprehension удалим точки, запятые и переведем все слова в нижний регистр
words = [word.strip(".").strip(",").lower() for word in words]
print(words)

# +
# Способ 1. Условие if-else


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
print(sorted(bow_1.items(), key=lambda x: x[1], reverse=True)[:6])

# +
# Способ 2. Метод .get()


bow_2: dict[str, int] = {}

# снова пройдемся в цикле по словам
for word in words:

    # если слова еще нет в словаре, .get() выведет значение 0, к которому мы прибавим единицу
    # если слово есть, метод .get() выведет существующее значение, например, 2 или 3,
    # и мы также увеличим счетчик на 1
    bow_2[word] = bow_2.get(word, 0) + 1

# выведем наиболее популярные слова
print(sorted(bow_2.items(), key=lambda x: x[1], reverse=True)[:6])

# +
# Способ 3. Модуль collections


# импортируем класс Counter

# создадим объект этого класса, передав ему список слов
bow_3 = Counter(words)

# выведем шесть наиболее часто встречающихся слов с помощью метода .most_common()
bow_3.most_common(6)
