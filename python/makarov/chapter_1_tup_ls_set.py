"""Списки, кортежи и множества."""

# +
# # создадим одно пустое
# # возьмем уже знакомый нам по вводному курсу словарь с овощами
# # создадим две переменные и поместим в них пустые кортежи
# # создадим список из букв
# from typing import Dict, List, Set, Tuple, Union

# some_list_1: list
# some_list_2: list
# some_list_1 = []
# some_list_2 = list()

# print(some_list_1, some_list_2)

# +
# number_three: List[Union[int, str, List[str], Dict[str, int]]]
# number_three = [3, "число три", ["число", "три"], {"число": 3}]
# number_three

# +
# len(number_three)

# +
# abc_list: List[str] = ["a", "b", "c", "d", "e"]
# # выведем первый и последний элементы
# print(abc_list[0], abc_list[-1])

# +
# salary_list: List[List[Union[str, int]]]
# salary_list = [["Анна", 90000], ["Игорь", 85000], ["Алексей", 95000]]
# salary_list[1][0]

# +
# abc_list.index("c")

# +
# days_list: List[str]
# days_list = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
# days_list[1:5]

# +
# # начнем с Пн и будем брать дни через один вплоть до, но не включая, Сб [5]
# days_list[:5:2]

# +
# weekdays: List[str]
# weekdays = ["Понедельник", "Вторник"]

# weekdays.append("Четверг")
# weekdays

# +
# # для этого методу .insert() мы передаем желаемый индекс нового элемента
# # и сам этот элемент
# weekdays.insert(2, "Среда")
# weekdays

# +
# weekdays[3] = "Пятница"
# weekdays

# +
# # для удаления по названию можно использовать метод .remove()
# weekdays.remove("Пятница")
# weekdays

# +
# # ключевое слово del удаляет элемент по индексу
# del weekdays[2]
# weekdays

# +
# # метод .pop() не просто удаляет элемент по индексу,
# # но и выводит удаляемый элемент
# weekdays.pop(1)

# +
# # добавим к списку, в котором есть только понедельник, остальные дни
# more_weekdays: List[str]
# more_weekdays = ["Вторник", "Среда", "Четверг", "Пятница"]

# weekdays.extend(more_weekdays)
# weekdays

# +
# # прибавим выходные
# weekend: List[str]
# weekend = ["Суббота", "Воскресенье"]
# print(weekdays + weekend)

# +
# # заново создадим список с днями недели
# week: List[str]
# week = [
#     "Понедельник",
#     "Вторник",
#     "Среда",
#     "Четверг",
#     "Пятница",
#     "Суббота",
#     "Воскресенье",
# ]

# +
# Mon = week[0]
# Mon

# +
# # количество переменных должно быть равно количеству элементов среза
# Mon, Tue, Wed = week[:3]
# Mon, Tue, Wed

# +
# # отсортируем список по возрастанию
# nums: List[int]
# nums = [25, 10, 30, 20, 5, 15]
# sorted(nums)

# +
# # с помощью параметра reverse = True сортируем список по убыванию
# nums.sort(reverse=True)
# nums

# +
# nums.reverse()
# nums

# +
# list(reversed(nums))

# +
# str_list: List[str]
# str_list = ["P", "y", "t", "h", "o", "n"]

# +
# joined_str = "".join(str_list)
# joined_str

# +
# nums_: List[int]
# nums_ = [3, 2, 1, 4, 5, 12, 3, 3, 7, 9, 11, 15]

# +
# print(min(nums_), max(nums_), sum(nums_))

# +
# names: List[str]
# names = ["Артем", "Антон", "Александр", "Борис", "Виктор", "Геннадий"]

# +
# # создадим пустой список a_names
# a_names: List
# a_names = []

# # пройдемся по списку имен
# for name in names:

#     # если имя начинается с 'А'
#     if name.startswith("А"):

#         # добавим его в список a_names
#         a_names.append(name)

# # посмотрим на результат
# a_names

# +
# a_names: List[str]
# a_names = [name for name in names if name.startswith("А")]
# a_names

# +
# lower_names: List[str]
# lower_names = [name.lower() for name in names]
# lower_names

# +
# replace_name: List[str]
# replace_name = [name if name != "Виктор" else "Вадим" for name in names]
# replace_name

# +
# tuple_1: Tuple[()]
# tuple_2: Tuple[()]
# tuple_1, tuple_2 = (), tuple()
# print(tuple_1, tuple_2)

# +
# # создадим кортеж
# letters: Tuple[str, ...]
# letters = ("a", "b", "c")

# # и выведем его первый элемент
# letters[0]

# +
# # преобразуем кортеж в список через функцию list()
# letters: List[str]
# letters = list(letters)

# # теперь элементы можно изменять
# letters[0] = "d"
# letters

# +
# # создадим список с названием трех компаний
# companies: List[str]
# companies = ["Microsoft", "Apple", "Tesla"]

# # и в цикле поместим результат работы функции enumerate()
# # в одну переменную company
# for company in enumerate(companies):
#     print(company, type(company))

# +
# shopping_dict: Dict[str, int]
# shopping_dict = {"огурцы": 2, "помидоры": 3, "лук": 1, "картофель": 2}

# +
# # пройдемся по ключам и значениям с помощью метода .items(),
# # но поместим результат в одну переменную item
# for item in shopping_dict.items():
#     print(item)

# +
# # если в кортеже три элемента, то и переменных должно быть три

# a, b, c = ("a", "b", "c")

# # выведем переменную a
# print(a)

# +
# # снова возьмем список компаний
# companies: List[str]
# companies = ["Microsoft", "Apple", "Tesla"]

# # однако с функцией enumerate() используем две переменные
# for i, company in enumerate(companies):
#     print(i, company)

# +
# shopping_dict: Dict[str, int]
# shopping_dict = {"огурцы": 2, "помидоры": 3, "лук": 1, "картофель": 2}

# # используем две переменные с методом .items()
# for k, v in shopping_dict.items():
#     print(k, v)

# +
# # создадим два списка: список имен и список доходов
# names: List[str]
# income: List[str]
# names = ["Артем", "Антон", "Александр", "Борис", "Виктор", "Геннадий"]
# income = [97000, 110000, 95000, 84000, 140000, 120000]

# # передадим эти списки функции zip()
# zip(names, income)

# +
# list(zip(names, income))

# +
# set_1: Set
# set_2: Set[str]
# set_3: Set[str]
# set_1 = set()

# # и два непустых множества с повторяющимся элементом 'c'
# set_2 = {"a", "b", "c", "c"}
# set_3 = {"a", "b", "c", "c"}

# print(set_1, set_2, set_3)

# +
# not_a_set = {}
# type(not_a_set)

# +
# vowels: Set[str]
# vowels = {"а", "о", "э", "е", "у", "ё", "ю"}

# +
# vowels.add("я")
# vowels

# +
# # передадим методу .update() список из двух гласных букв
# vowels.update(["и", "ы"])
# vowels

# +
# vowels.add("щ")
# vowels

# +
# vowels.remove("щ")
# vowels

# +
# {"a", "b", "c"} == {"c", "b", "a"}

# +
# "a" in {"a", "b", "c"}

# +
# "a" in {"a", "b", "c"}

# +
# set_A: Set[str]
# set_B: Set[str]
# set_A = {"a", "b", "c"}
# set_B = {"a", "b", "c", "d", "e", "f"}

# set_A.issubset(set_B)

# +
# set_B.issuperset(set_A)

# +
# nlp: Set[str]
# cv: Set[str]
# nlp = {"Анна", "Николай", "Павел", "Оксана"}
# cv = {"Николай", "Евгений", "Ольга", "Оксана"}

# +
# print(nlp.union(cv))
# print(nlp | cv)

# +
# print(nlp.intersection(cv))
# print(nlp & cv)

# +
# print(nlp.difference(cv))
# print(nlp - cv)

# +
# print(cv.difference(nlp))
# print(cv - nlp)

# +
# print(nlp.symmetric_difference(cv))
# print(nlp ^ cv)
