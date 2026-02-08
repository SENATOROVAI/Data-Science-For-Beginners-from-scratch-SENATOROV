"""Списки, кортежи и множества."""

# ## Списки, кортежи и мн-ва

# ### Списки

# #### Основы работы со списками

# +
# пустой список можно создать через [] или функции list()
some_list_1: list[int] = []

print(some_list_1)
# -

# элементами списки могут, в частности, быть числа, строки, другие списки и словари
number_three = [3, "число три", ["число", "три"], {"три": 3}]
number_three

len(number_three)

# #### Индекс и срез списков

# у списка есть положительный и отрицательный индексы
abc_list = ["a", "b", "c", "d", "e"]
# воспользуемся ими для вывода первого и последнего элементов
print(abc_list[0], abc_list[-1])

# +
# при работе с вложенным списком
salary_list = [["Иван", 100000], ["Петр", 200000], ["Сидор", 300000]]

salary_list[1][0]
# -

# индекс можно узнать с помощью метода .index()
abc_list.index("b")

days_list = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
days_list[1:5]

# каждый второй
days_list[:5:2]
"Пн" in days_list

if "Вт" in days_list:
    print("Такое слово есть")

# #### Добавление, замена и удаление элементов списка

# создадим список
weekdays = ["Понедельник", "Вторник"]

# добавим один элемент в конец
weekdays.append("Четверг")
weekdays

# в определённую позицию
weekdays.insert(2, "Среда")
weekdays

# изменить элемент
weekdays[0] = "Понедельник"
weekdays

# удалить элемент по значению
weekdays.remove("Понедельник")
weekdays

# удалить по индексу
del weekdays[0]
weekdays.pop(1)

weekdays

# #### Сложение списков

# +
more_weekdays = ["Вторник", "Понедельник", "Пятница"]
weekdays.extend(more_weekdays)

weekdays

# +
weekend = ["Суббота", "Воскресенье"]

weekend + weekdays
# -

["Понедельник"] * 2

# выражения
["Понедельник"] * 2 + ["Вторник"] * 2

# #### Распаковка списков

# дан список
week = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенью",
]

mon_dow = week[0]
mon_dow

# +
mon_dow, tue_dow, wed_dow = week[:3]

mon_dow, tue_dow, wed_dow
# -

mon_dow, *_ = week
mon_dow

mon_dow, *days, sun_dow = week
mon_dow, sun_dow

days

# #### Сортировка списков

nums = [25, 10, 30, 20, 5, 15]

sorted(nums)

nums

sorted(nums, reverse=True)

nums.sort(reverse=True)
nums

nums.reverse()
nums

reversed(nums)

list(reversed(nums))

nums

# #### Преобразование списка в строку

str_list = ["P", "y", "t", "h", "o", "n"]
" ".join(str_list)

# #### Арифметика в списках

nums = [1, 2, 3, 4, 5]

nums.count(3)

print(max(nums), min(nums), sum(nums))

# #### List comprehension

names = ["Артём", "Антон", "Александр", "Борис", "Виктор", "Геннадий"]

# +
# имена начинающиеся на 'A'

a_names = []
for name in names:
    if name.startswith("А"):
        a_names.append(name)
a_names
# -

# намного короче используя list comprehension
print([name for name in names if name.startswith("А")])

replace_name = [name if name != "Виктор" else "Вадим" for name in names]
replace_name

# ### Кортежи

# #### Основы работы с кортежами

tuple_1 = ()
tuple_2: tuple[int, ...] = tuple([1])
print(tuple_1, tuple_2)

letters = ("a", "b", "c")
letters[0]

# Этот код выдаст ошибку, так как кортеж неизменяемый тип:
# ```python
# letters[0] = d
# ```

# чтобы создать кортеж с одним элементом - запятая
let_a = ("A",)

# #### Функция enumerate()

# +
companies = ["Microsoft", "Apple", "Tesla"]

for company in enumerate(companies):
    print(company, type(company))
# -

# #### Просмотр элементов словаря

# +
shopping_list = {"огурцы": 2, "помидоры": 1, "лук": 3}

for item in shopping_list.items():
    print(item)
# -

# #### Распаковка кортежей

val1, val2, val3 = ("a", "b", "c")
print(val1, val2, val3)

# +
companies = ["Microsoft", "Apple", "Tesla"]

for i, company1 in enumerate(companies):
    print(i, company1)
# -

for key, value in shopping_list.items():
    print(key, value)

# #### Функция zip

# +
names = ["Артём", "Антон", "Александр", "Борис", "Виктор", "Геннадий"]
income = [97000, 11000, 95000, 84000, 140000, 120000]

list(zip(names, income))
# -

# ### Множества

# #### Создание множеств

set_1: set[int] = set()
set_2 = {"a", "b", "c"}
set_3 = {"a", "b", "c"}
print(set_1, set_2, set_3)

# #### Добавление и удаление элементов

vowels = {"а", "о", "е", "ё"}

vowels.add("я")
vowels

vowels.remove("я")

# #### Теория множеств в питоне

# множества равны по элементам без учета порядка
{"a", "b", "c"} == {"b", "c", "a"}

# мощность мн-ва
len({"a", "b", "c"})
"a" in {"a", "b", "c"}

# +
# проверка на подмножество
set_a = {"a", "b", "c"}
set_b = {"a", "b", "c", "d", "e", "f"}

set_a.issubset(set_b)
# -

# надмножество
set_a.issuperset(set_b)

nlp = {"Анна", "Николай", "Павел", "Оксана"}
cv = {"Николай", "Евгений", "Ольга", "Оксана"}

nlp | cv

nlp & cv

nlp - cv

cv - nlp

# XOR
nlp ^ cv
