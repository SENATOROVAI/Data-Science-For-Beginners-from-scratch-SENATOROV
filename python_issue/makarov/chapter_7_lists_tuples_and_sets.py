"""Lists, tuples, and sets."""

# # Списки, кортежи и множества

# ## Списки

# ### Основы работы со списками
#

# +
from nltk import PorterStemmer

some_list_1: list[str] = []
some_list_2: list[str] = []

print(some_list_1, some_list_2)

number_three: list[int | str | list[str] | dict[str, int]] = [
    3,
    "number three",
    ["number", "three"],
    {"number": 3},
]
print(number_three)

len(number_three)
# -

# ### Индекс и срез списка
#

# +
abc_list: list[str] = ["a", "b", "c", "d", "e"]

print(abc_list[0], abc_list[-1])

# +
salary_list: list[list[str | int]] = [
    ["Anna", 90000],
    ["Igor", 85000],
    ["Alex", 95000],
]

salary_list[1][0]
# -

abc_list.index("c")

salary_list[0].index(90000)

# +
days_list: list[str] = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days_list[1:5]
# -

days_list[:5:2]
"Mon" in days_list

if "Tue" in days_list:
    print("Такое слово есть")

# ### Добавление, замена и удаление элементов списка
#

# +
weekdays: list[str] = ["Monday", "Tuesday"]

weekdays.append("Thursday")
weekdays
# -

weekdays.insert(2, "Wednesday")
weekdays

weekdays[3] = "Friday"
weekdays

weekdays.remove("Friday")
weekdays

del weekdays[2]
weekdays

weekdays.pop(1)

weekdays

# ### Сложение списков
#

# +
more_weekdays: list[str] = ["Tuesday", "Wednesday", "Thursday", "Friday"]

weekdays.extend(more_weekdays)
weekdays

# +
weekend: list[str] = ["Saturday", "Sunday"]

print(weekdays + weekend)
# -

["Monday"] * 2

["Monday"] * 2 + ["Tuesday"] * 2

# ### Распаковка списков

# +
week: list[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

mon = week[0]
mon
# -

mon_1, tue_1, wed_1 = week[0:3]
mon_1, tue_1, wed_1

mon_1, *_ = week
mon_1

mon_1, *days, sun_1 = week
mon_1, sun_1

days

# ### Сортировка списков
#

nums: list[int] = [25, 10, 30, 20, 5, 15]
sorted(nums)

sorted_nums: list[int] = sorted(nums)
sorted_nums

nums.sort(reverse=True)
nums

print(nums)
nums.reverse()
print(nums)

# #### Переменная не изменяется при этом
#

reversed(nums)

list(reversed(nums))

# ### Преобразование списка в строку
#

str_list: list[str] = ["P", "y", "t", "h", "o", "n"]
joined_str: str = "".join(str_list)
joined_str

joined_str_: str = "_".join(str_list)
joined_str_

# ### Арифметика в списках
#

# +
nums_: list[int] = [3, 2, 1, 4, 5, 12, 3, 3, 7, 9, 11, 15]

nums_.count(3)
# -

print(min(nums_), max(nums_), sum(nums_))

# ### List comprehension
#

# +
names: list[str] = [
    "Arthur",
    "Anton",
    "Alex",
    "Boris",
    "Victor",
    "Eugene",
]
a_names_var: list[str] = []

for name in names:
    if name.startswith("a"):
        a_names_var.append(name)

a_names_var
# -

a_names: list[str] = [name for name in names if name.startswith("a")]
a_names

lower_names: list[str] = [name.lower() for name in names]
lower_names

# +
# replace_name: list[str] =
# ["Vlad" if name == "Victor" else name for name in names]
# replace_name

# +
lemmatized: list[str] = [
    "paris",
    "visited",
    "lot",
    "museum",
    "first",
    "went",
    "louvre",
    "largest",
    "art",
    "museum",
    "world",
    "always",
    "interested",
    "art",
    "spent",
    "many",
    "hour",
    "museum",
    "enormous",
    "week",
    "would",
    "enough",
]


porter: PorterStemmer = PorterStemmer()

stemmed_p: list[str] = [porter.stem(s) for s in lemmatized]
print(stemmed_p)
print(type(porter))
# -

# ## Кортежи

# ### Основы работы с кортежами
#

tuple_1: tuple[()] = ()
tuple_2: tuple[()] = ()
print(tuple_1, tuple_2)

letters_tuple: tuple[str, str, str] = ("a", "b", "c")
print(letters_tuple[0])
# letters[0] = 'd' -> WRONG

letters_list: list[str] = list(letters_tuple)
letters_list[0] = "d"
print(letters_list)

let_a_tuple: tuple[str] = ("a",)
print(type(let_a_tuple))

let_a_str: str = "a"
print(type(let_a_str))

# #### Функция enumerate()
#

# +
companies: list[str] = ["Microsoft", "Apple", "Tesla"]

for company in enumerate(companies):
    print(company, type(company))
# -

# #### Просмотр элементов словаря
#

# +
shopping_dict: dict[str, int] = {
    "cucumber": 3,
    "tomato": 2,
    "onion": 1,
    "potato": 2,
}

for item in shopping_dict.items():
    print(item)
# -

# #### Распаковка кортежей
#

a_var, b_var, c_var = ("a", "b", "c")
print(a_var)

for index_value, company_name in enumerate(companies):
    print(index_value, company_name)

for k_var, v_var in shopping_dict.items():
    print(k_var, v_var)

# #### Функция zip()
#

# +
names_list: list[str] = [
    "Arthur",
    "Anton",
    "Alex",
    "Boris",
    "Victor",
    "Eugene",
]
income: list[int] = [97000, 110000, 95000, 84000, 140000, 120000]

zip(names_list, income)
# -

list(zip(names_list, income))

# ### Множества
#

# ### Создание множества

set_1: set[str] = set()
set_2: set[str] = {"a", "b", "c"}
set_3: set[str] = {"a", "b", "c", "d", "e", "f"}
print(set_1, set_2, set_3)

not_a_set: dict[str | int, str | int] = {}
print(type(not_a_set))

# #### Добавление и удаление элементов
#

# +
vowels: set[str] = {"a", "o", "ie", "e", "y", "io", "iu"}

vowels.add("ia")
print(vowels)
# -

vowels.update({"i", "ii"})
print(vowels)

# +
vowels.add("cha")
print(vowels)

vowels.discard("cha")
print(vowels)
# -

# #### Теория множеств в Питоне
#

# равны если имеют одинаковые элементы, порядок не важен
{"a", "b", "c"} == {"c", "a", "b"}

# #### Мощность множества
#

len({"a", "b", "c"})

# #### Проверка есть ли элемент в множестве
#

a_var in {"a", "b", "c"}

# или наоборот
a_var not in {"a", "b", "c"}

# +
set_a: set[str] = {"a", "b", "c"}
set_b: set[str] = {"a", "b", "c", "d", "e"}

set_a.issubset(set_b)
# -

set_b.issuperset(set_a)

nlp: set[str] = {"Анна", "Николай", "Павел", "Оксана"}
cv: set[str] = {"Николай", "Евгений", "Ольга", "Оксана"}

# Все участники
print(nlp.union(cv))
print(nlp | cv)

# И там и там
print(nlp.intersection(cv))
print(nlp & cv)

# Только nlp или и там и там
print(nlp.difference(cv))
print(nlp - cv)

# Или там или там но не одновременно везде
print(nlp.symmetric_difference(cv))
print(nlp ^ cv)
