"""Словарь."""

# +
# dict_1, dict_2 = {}, dict()
# print(dict_1, dict_2)

# +
# company = {'name': 'Toyota', 'founded' : 1937, 'founder': 'Kiichiro Toyoda'}
# company

# +
# tickers = dict([['TYO', 'Toyota'], ['TSLA', 'Tesla'], ['F', 'Ford']])
# tickers

# +
# # ключи мы поместим в кортеж
# keys = ('k1', 'k2', 'k3')

# # значением каждого ключа будет 0,
# # если ничего не указывать, ключи получат значение None
# value = 0

# empty_k = dict.fromkeys(keys, value)
# empty_k

# +
# import numpy as np

# value_types = {'k1' : 123,
#                'k2' : 'string',
#                'k3' : np.NaN, # тип "Пропущенное значение"
#                'k4' : True, # логическое значение
#                'k5' : None,
#                'k6' : [1, 2, 3],
#                'k7' : np.array([1, 2, 3]),
#                'k8' : {1 : 'v1', 2 : 'v2', 3 : 'v3'}}

# value_types

# +
# person = {'first name' : 'Иван',
#           'last name' : 'Иванов',
#           'born' : 1980,
#           'dept' : 'IT'}

# +
# # обратите внимание, в данном случае новое значение - это список
# person['languages'] = ['Python', 'C++']
# person

# +
# # значение - это по-прежнему список, но из одного элемента
# person['languages'] = ['Python']
# person

# +
# # возьмем еще один словарь
# new_elements = {'job' : 'программист', 'experience' : 7}

# # и присоединим его к существующему словарю с помощью метода .update()
# person.update(new_elements)
# person

# +
# # удаляемое значение не выводится
# del(person['born'])

# +
# # возьмем несложный словарь
# dict_to_sort = {'k2' : 30, 'k1' : 20, 'k3' : 10}

# +
# sorted(dict_to_sort)

# +
# # создадим исходный словарь с 
# количеством студентов на первом и втором курсах университета
# original = {'Первый курс' : 174, 'Второй курс' : 131}

# +
# # создадим копию исходного словаря с помощью метода .copy()
# new_1 = original.copy()

# # добавим информацию о третьем курсе в новый словарь
# new_1['Третий курс'] = 117

# # выведем исходный и новый словари
# print(original)
# print(new_1)

# +
# # создадим словарь,
# some_dict = {'k': 1}

# # передадим его в функцию dir() и
# # выведем первые 11 элементов
# dir(some_dict)

# +
# # создадим еще один словарь
# source_dict = {'k1' : 2, 'k2' : 4, 'k3' : 6}

# +
# {k : v * 2 for (k, v) in source_dict.items()}

# +
# new_dict = {}

# for k, v in source_dict.items():
#   if v > 2 and v < 6:

#     # если условия верны, записываем ключ и значение в новый словарь
#     new_dict[k] = v

# new_dict

# +
# # один фут равен 0,3048 метра
# metres = list(map(lambda m: m * 0.3048, height_feet.values()))
# metres

# +
# dict(zip(height_feet.keys(), np.round(metres, 2)))

# +
# # мы просто преобразуем значения словаря в метры
# {k : np.round(v * 0.3048, 2) for (k, v) in height_feet.items()}

# +
# employees = {
#     'id1': {
#         'first name': 'Александр',
#     'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#     'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#             }
# }

# +
# for v in employees.values():
#   print(v)

# +
# # добавим информацию о новом сотруднике
# employees['id3'] = {'first name':
# 'Дарья', 'last name' : 'Некрасова',
# 'age': 27, 'job' : 'веб-дизайнер' }

# # и выведем обновленный словарь с помощью функции pprint()
# pprint(employees)

# +
# employees['id3']['age'] = 26
# pprint(employees)

# +
# # для этого вначале пройдемся по вложенным словарям,
# # т.е. по значениям info внешнего словаря employees
# for info in employees.values():

#   # затем по ключам и значениям вложенного словаря info
#   for k, v in info.items():

#     # если ключ совпадет со словом 'age'
#     if k == 'age':

#       # преобразуем значение в тип float
#       info[k] = float(v)

# pprint(employees)

# +
# # создадим пустой словарь для мешка слов bow
# bow_1 = {}

# # пройдемся по словам текста
# for word in words:

#   # если нам встретилось слово, которое уже есть в словаре
#   if word in bow_1:

#     # увеличим его значение (частоту) на 1
#     bow_1[word] = bow_1[word] + 1

#   # в противном случае, если слово встречается впервые
#   else:

#     # зададим ему значение 1
#     bow_1[word] = 1

# # отсортируем словарь по значению в убываюем порядке (reverse = True)
# # и выведем шесть наиболее частотных слов
# sorted(bow_1.items(), key = lambda x : x[1], reverse = True)[:6]

# +
# bow_2 = {}

# for word in words:
#   bow_2[word] = bow_2.get(word, 0) + 1

# sorted(bow_2.items(), key = lambda x : x[1], reverse = True)[:6]

# +
# # импортируем класс Counter
# from collections import Counter

# # создадим объект этого класса, передав ему список слов
# bow_3 = Counter(words)

# # выведем шесть наиболее часто встречающихся слов с помощью метода .most_common()
# bow_3.most_common(6)
# -


