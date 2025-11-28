"""DataFrame."""

# # Преобразование датафрейма

# +
import io
import os
from typing import Union, cast

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv

# pylint: disable=too-many-lines
# -

# ## Изменение датафрейма

# Вернемся к датафрейму из предыдущего занятия

# +
# fmt: off
# создадим несколько списков и массивов Numpy с информацией о семи странах мира
country = np.array(
    [
        "China",
        "Vietnam",
        "United Kingdom",
        "Russia",
        "Argentina",
        "Bolivia",
        "South Africa",
    ]
)
capital = np.array(
    [
        "Beijing",
        "Hanoi", 
        "London", 
        "Moscow", 
        "Buenos Aires", 
        "Sucre", 
        "Pretoria"
    ]
)
population = np.array([1400, 97, 67, 144, 45, 12, 59])  # млн. человек
area = np.array([9.6, 0.3, 0.2, 17.1, 2.8, 1.1, 1.2])  # млн. кв. км.
sea = np.array([1] * 5 + [0, 1])  # выход к морю (в этом списке его нет только у Боливии)

# кроме того создадим список кодов стран, которые станут индексом датафрейма
custom_index = ["CN", "VN", "GB", "RU", "AR", "BO", "ZA"]

# создадим пустой словарь
countries_dict = {}

# превратим эти списки в значения словаря,
# одновременно снабдив необходимыми ключами
countries_dict["country"] = country
countries_dict["capital"] = capital
countries_dict["population"] = population
countries_dict["area"] = area
countries_dict["sea"] = sea

# создадим датафрейм
countries = pd.DataFrame(countries_dict, index=custom_index)
countries
# fmt: on
# -

# ### Копирование датафрейма

# #### Метод `.copy()`

# поместим датафрейм в новую переменную
countries_new = countries

# +
# удалим запись про Аргентину и сохраним результат
countries_new.drop(labels="AR", axis=0, inplace=True)

# выведем исходный датафрейм
countries

# +
# в первую очередь вернем Аргентину в исходный датафрейм countries
countries = pd.DataFrame(countries_dict, index=custom_index)

# создадим копию, на этот раз с помощью метода .copy()
countries_new = countries.copy()

# вновь удалим запись про Аргентину
countries_new.drop(labels="AR", axis=0, inplace=True)

# выведем исходный датафрейм
countries
# -

# #### Про параметр `inplace`

# +
# создадим несложный датафрейм
df = pd.DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=["A", "B", "C"])

df
# -

# если метод выдает датафрейм, изменение не сохраняется
df.drop(labels=["A"], axis=1)

# проверим это
df

# если метод выдает None, изменение постоянно
print(df.drop(labels=["A"], axis=1, inplace=True))

# проверим
df

# +
# по этой причине нельзя использовать inplace = True
# и записывать в переменную одновременно
df.drop(labels=["B"], axis=1, inplace=True)

# в этом случае мы записываем None в переменную df
print(df)
# -

# ### Столбцы датафрейма

# Именование столбцов при создании датафрейма

# +
# создадим список с названиями столбцов на кириллице
custom_columns = ["страна", "столица", "население", "площадь", "море"]

# и транспонированный массив Numpy с данными о странах
arr = np.array([country, capital, population, area, sea]).T
arr

# +
# создадим датафрейм, передав в параметр columns названия столбцов на кириллице
countries = pd.DataFrame(data=arr, index=custom_index, columns=custom_columns)

countries
# -

# вернем прежние названия столбцов
countries.columns = ["country", "capital", "population", "area", "sea"]

# Переименование столбцов

# переименуем столбец capital на city
countries.rename(columns={"capital": "city"}, inplace=True)
countries

# ### Тип данных в столбце

# Просмотр типа данных в столбце

# в одном столбце содержится один тип данных
# посмотрим на тип данных каждого из столбцов
countries.dtypes

# Изменение типа данных

# преобразуем тип данных столбца population в int
countries.population = countries.population.astype("int")

# изменим тип данных в столбцах area и sea
countries = countries.astype({"area": "float", "sea": "category"})

# посмотрим на результат
countries.dtypes

# Тип данных category

# тип category похож на фактор в R
countries.sea

# Фильтр столбцов по типу данных

# выберем только типы данных int и float
countries.select_dtypes(include=["int64", "float64"])

# выберем все типы данных, кроме object и category
countries.select_dtypes(exclude=["object", "category"])

# ### Добавление строк и столбцов

# #### Добавление строк

# Метод ._append() + словарь

# +
# создадим словарь с данными Канады и добавим его в датафрейм
dict_ = {
    "country": "Canada",
    "city": "Ottawa",
    "population": 38,
    "area": 10,
    "sea": "1",
}

# словарь можно добавлять только если ignore_index = True
# countries = countries._append(dict_, ignore_index=True)
countries = pd.concat([countries, pd.DataFrame([dict_])], ignore_index=True)
countries
# -

# Метод ._append() + другой датафрейм

# новая строка может также содержаться в другом датафрейме
# обратите внимание, что числовые значения мы помещаем в списки
peru = pd.DataFrame(
    {"country": "Peru", "city": "Lima", "population": [33], "area": [1.3], "sea": [1]}
)
peru

# перед добавлением выберем первую строку с помощью метода .iloc[]
# countries._append(peru.iloc[0], ignore_index=True)
countries = pd.concat([countries, peru.iloc[[0]]], ignore_index=True)

# Использование `.iloc[]`

# ни Испания, ни Нидерланды, ни Перу не сохранились
countries

# +
# добавим данные об этих странах на постоянной основе с помощью метода .iloc[]
countries.iloc[5:7] = pd.DataFrame(
    [
        ["Spain", "Madrid", 47, 0.5, 1],
        ["Netherlands", "Amsterdam", 17, 0.04, 1],
    ],
    columns=countries.columns,
    index=[5, 6],
)

# такой способ поместил строки на нужный нам индекс,
# заменив (!) существующие данные
countries
# -

# #### Добавление столбцов

# Объявление нового столбца

# новый столбец датафрейма можно просто объявить
# и сразу добавить в него необходимые данные
# например, добавим данные о плотности населения
countries["pop_density"] = [153, 49, 281, 9, 17, 94, 508, 26] + [np.nan]
countries

# добавим столбец с кодами стран
countries.insert(
    loc=1,  # это будет второй по счету столбец
    column="code",  # название столбца
    value=["CN", "VN", "GB", "RU", "AR", "ES", "NL", "PE"] + [np.nan],
)  # значения столбца

# изменения сразу сохраняются в датафрейме
countries

# Метод `.assign()`

# создадим столбец area_miles, переведя площадь в мили
countries = countries.assign(area_miles=countries.area / 2.59).round(2)
countries

# удалим этот столбец, чтобы рассмотреть другие методы
countries.drop(labels="area_miles", axis=1, inplace=True)

# Можно проще

# объявим новый столбец и присвоим ему нужное нам значение
countries["area_miles"] = (countries.area / 2.59).round(2)
countries

# ### Удаление строк и столбцов

# #### Удаление строк

# для удаления строк можно использовать метод .drop()
# с параметрами labels (индекс удаляемых строк) и axis = 0
countries.drop(labels=[0, 1], axis=0)

# кроме того, можно использовать метод .drop() с единственным параметром index
countries.drop(index=[5, 7])

# передадим индекс датафрейма через атрибут index и удалим четвертую строку
countries.drop(index=countries.index[4])

# с атрубутом датафрейма index мы можем делать срезы
# удалим каждую вторую строку, начиная с четвертой с конца
countries.drop(index=countries.index[-4::2])

# #### Удаление столбцов

# используем параметры labels и axis = 1 метода .drop() для удаления столбцов
countries.drop(labels=["area_miles", "code"], axis=1)

# используем параметр columns для удаления столбцов
countries.drop(columns=["area_miles", "code"])

# через атрибут датафрейма columns мы можем передавать номера удаляемых столбцов
countries.drop(columns=countries.columns[-1])

# наконец удалим пятую строку и несколько столбцов и сохраним изменения
countries.drop(index=4, inplace=True)
countries.drop(columns=["code", "pop_density", "area_miles"], inplace=True)
countries

# #### Удаление по многоуровневому индексу

# +
# подготовим данные для многоуровневого индекса строк
rows = [
    ("Asia", "CN"),
    ("Asia", "VN"),
    ("Europe", "GB"),
    ("Europe", "RU"),
    ("Europe", "ES"),
    ("Europe", "NL"),
    ("S. America", "PE"),
]

# и столбцов
cols = [
    ("names", "country"),
    ("names", "city"),
    ("data", "population"),
    ("data", "area"),
    ("data", "sea"),
]

countries = cast(pd.DataFrame, countries.iloc[: len(rows), : len(cols)])

# создадим многоуровневый (иерархический) индекс
# для индекса строк добавим названия столбцов индекса через параметр names
custom_multindex = pd.MultiIndex.from_tuples(rows, names=["region", "code"])
custom_multicols = pd.MultiIndex.from_tuples(cols)

# поместим индексы в атрибуты index и columns датафрейма
countries.index = custom_multindex
countries.columns = custom_multicols

# посмотрим на результат
countries
# -

# Удаление строк

# удалим регион Asia указав соответствующий label, axis = 0, level = 0
countries.drop(labels="Asia", axis=0, level=0)

# мы также можем удалять строки через параметр index с указанием нужного level
countries.drop(index="RU", level=1)

# Удаление столбцов

# удалим все столбцы в разделе names на нулевом уровне индекса столбцов
countries.drop(labels="names", level=0, axis=1)

# для удаления столбцов можно использовать параметр columns
# с указанием соответствующего уровня индекса (level) столбцов
countries.drop(columns=["city", "area"], level=1)

# ### Применение функций

# +
# создадим новый датафрейм с данными нескольких человек
people = pd.DataFrame(
    {
        "name": ["Алексей", "Иван", "Анна", "Ольга", "Николай"],
        "gender": [1, 1, 0, 2, 1],
        "age": [35, 20, 13, 28, 16],
        "height": [180.46, 182.26, 165.12, 168.04, 178.68],
        "weight": [73.61, 75.34, 50.22, 52.14, 69.72],
    }
)

people
# -

# #### Метод `.map()`

# +
# создадим карту (map) того, как преобразовать существующие значения в новые
# такая карта представляет собой питоновский словарь,
# где ключи - это старые данные, а значения - новые
gender_map = {0: "female", 1: "male"}

# применим эту карту к нужному нам столбцу
people["gender"] = people["gender"].map(gender_map)
people
# -

# в метод .map() мы можем передать и lambda-функцию
# например, для того, чтобы выявить совершеннолетних и несовершеннолетних людей
people["age_group"] = people["age"].map(lambda x: "adult" if x >= 18 else "minor")
people

# удалим только что созданный столбец age_group
people.drop(labels="age_group", axis=1, inplace=True)

# +
# сделаем то же самое с помощью собственной функции
# обратите внимание, такая функция не допускает дополнительных параметров,
# только те данные, которые нужно преобразовать (age)


def get_age_group_1(age: int) -> str:
    """Classify a person as 'adult' or 'minor' based on age threshold (18)."""
    # например, мы не можем сделать threshold произвольным параметром
    threshold = 18

    if age >= threshold:
        age_group = "adult"

    else:
        age_group = "minor"

    return age_group


# -

# применим эту функцию к столбцу age
people["age_group"] = people["age"].map(get_age_group_1)
people

# снова удалим созданный столбец
people.drop(labels="age_group", axis=1, inplace=True)

# #### Функция `np.where()`

# внутри функции np.where() три параметра: (1) условие,
# (2) значение, если условие выдает True, (3) и значение, если условие выдает False
people["age_group"] = np.where(people["age"] >= 18, "adult", "minor")
people

# удалим созданный столбец
people.drop(labels="age_group", axis=1, inplace=True)

# #### Метод `.where()`

# Пример 1.

# заменим возраст тех, кому меньше 18, на NaN
people.age.where(people.age >= 18, other=np.nan)

# Пример 2.

# +
# создадим матрицу из вложенных списков
nums_matrix = [[-13, 7, 1], [4, -2, 25], [45, -3, 8]]

# преобразуем в датафрейм
# (матрица не обязательно должна быть массивом Numpy (!))
nums = pd.DataFrame(nums_matrix)
nums
# -

# если число положительное (nums < 0 == True), оставим его без изменений
# если отрицательное (False), заменим на обратное (т.е. сделаем положительным)
nums.where(nums > 0, other=-nums)

# #### Метод `.apply()`

# Применение функции с аргументами

# +
# в отличие от .map(), метод .apply() позволяет передавать аргументы в применяемую функцию
# объявим функцию, которой можно передать не только значение возраста, но и порог,
# при котором мы будем считать человека совершеннолетним


def get_age_group_2(age: int, threshold: int) -> str:
    """Classify a person based on a given age threshold."""
    if age >= int(threshold):
        age_group = "adult"
    else:
        age_group = "minor"

    return age_group


# +
# применим эту функцию к столбцу age, выбрав в качестве порогового значения 21 год
people["age_group"] = people["age"].apply(get_age_group_2, threshold=21)

# посмотрим на результат
people
# -

# Применение к столбцам

# заменим значения в столбцах height и weight на медиану по столбцам
people.iloc[:, 3:5] = people.iloc[:, 3:5].apply(np.median, axis=0)
people

# Применение к строкам

# создадим исходный датафрейм
people = pd.DataFrame(
    {
        "name": ["Алексей", "Иван", "Анна", "Ольга", "Николай"],
        "gender": [1, 1, 0, 2, 1],
        "age": [35, 20, 13, 28, 16],
        "height": [180.0, 182.0, 165.0, 168.0, 179.0],
        "weight": [74.0, 75.0, 50.0, 52.0, 70.0],
    }
)

# +
# создадим функцию, которая рассчитает индекс массы тела


def get_bmi(x_var: dict[str, Union[int, float]]) -> float:
    """Calculate Body Mass Index from a row containing weight and height."""
    bmi: float = float(x_var["weight"]) / (float(x_var["height"]) / 100) ** 2
    return bmi


# -

# применим ее к каждой строке (человеку) и сохраним результат в новом столбце
people["bmi"] = people.apply(get_bmi, axis=1).round(2)
people

# #### Метод `.pipe()`

# +
# вновь создадим исходный датафрейм
people = pd.DataFrame(
    {
        "name": ["Алексей", "Иван", "Анна", "Ольга", "Николай"],
        "gender": [1, 1, 0, 2, 1],
        "age": [35, 20, 13, 28, 16],
        "height": [180.46, 182.26, 165.12, 168.04, 178.68],
        "weight": [73.61, 75.34, 50.22, 52.14, 69.72],
    }
)

people

# +
# создадим несколько функций


# в первую очередь скопируем датафрейм
def copy_df(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the given DataFrame."""
    return dataframe.copy()


# заменим значения столбца на новые с помощью метода .map()


def map_column(
    dataframe: pd.DataFrame, column: str, label1: str, label2: str
) -> pd.DataFrame:
    """Map binary values {0,1} in a column to custom string labels."""
    labels_map = {0: label1, 1: label2}
    dataframe[column] = dataframe[column].map(labels_map)
    return dataframe


# кроме этого, создадим функцию для превращения количественной переменной
# в бинарную категориальную


# pylint: disable=R0913
# pylint: disable=R0917
def to_categorical(
    dataframe: pd.DataFrame,
    newcol: str,
    condcol: str,
    thres: float,
    cat1: str,
    cat2: str,
) -> pd.DataFrame:
    """Create a new categorical column based on a numeric condition."""
    dataframe[newcol] = np.where(dataframe[condcol] >= thres, cat1, cat2)
    return dataframe


# -

# последовательно применим эти функции с помощью нескольких методов .pipe()
people_processed = (
    people.pipe(copy_df)  # copy_df() применится ко всему датафрейму
    .pipe(map_column, "gender", "female", "male")  # map_column() к столбцу gender
    .pipe(to_categorical, "age_group", "age", 18, "adult", "minor")
)  # to_categorical() к age_group

# посмотрим на результат
people_processed

# убедимся, что исходный датафрейм не изменился
people

# ## Соединение датафреймов

# ### `pd.concat()`

# +
# создадим датафреймы с информацией о стоимости канцелярских товаров в двух магазинах
s1 = pd.DataFrame(
    {"item": ["карандаш", "ручка", "папка", "степлер"], "price": [220, 340, 200, 500]}
)

s2 = pd.DataFrame(
    {"item": ["клей", "корректор", "скрепка", "бумага"], "price": [200, 240, 100, 300]}
)
# -

# посмотрим на результат
s1

s2

# передадим в функцию pd.concat() список из соединяемых датафреймов,
# укажем параметр axis = 0 (значение по умолчанию)
pd.concat([s1, s2], axis=0)

# обновим индекс через параметр ignore_index = True
pd.concat([s1, s2], axis=0, ignore_index=True)

# создадим многоуровневый (иерархический) индекс
# передадим в параметр keys названия групп индекса,
# параметр names получим названия уровней индекса
by_shop = pd.concat([s1, s2], axis=0, keys=["s1", "s2"], names=["s", "id"])
by_shop

# посмотрим на созданный индекс
by_shop.index

# выведем первую запись в первой группе
by_shop.loc[("s1", 0)]

# датафреймы можно расположить рядом друг с другом (axis = 1)
# одновременно сразу создадим группы для многоуровневого индекса столбцов
pd.concat([s1, s2], axis=1, keys=["s1", "s2"])

# с помощью метода .iloc[] можно выбрать только вторую группу
print(pd.concat([s1, s2], axis=1, keys=["s1", "s2"]).loc[:, "s2"])

# полученный результат и в целом любой датафрейм можно транспонировать
print(pd.concat([s1, s2], axis=1, keys=["s1", "s2"]).T)

# ### `pd.merge()` и `.join()`

# +
# рассмотрим три несложных датафрейма
math_dict = {
    "name": ["Андрей", "Елена", "Антон", "Татьяна"],
    "math_score": [83, 84, 78, 80],
}

math_degree_dict = {"degree": ["B", "M", "B", "M"]}

cs_dict = {
    "name": ["Андрей", "Ольга", "Евгений", "Татьяна"],
    "cs_score": [87, 82, 77, 81],
}

math = pd.DataFrame(math_dict)
cs = pd.DataFrame(cs_dict)
math_degree = pd.DataFrame(math_degree_dict)
# -

# в первом содержатся оценки студентов ВУЗа по математике
math

# во втором указано, по какой программе (бакалавр или магистер) учатся студенты
math_degree

# в третьем содержатся данные об оценках по информатике
# имена некоторых студентов повторяются, других - нет
cs

# #### Left join

pd.merge(
    math,
    math_degree,  # выполним соединение двух датафреймов
    how="left",  # способом left join
    left_index=True,
    right_index=True,
)  # по индексам левого и правого датафрейма

# такой же результат можно получить с помощью метода .join()
# можно сказать, что .join() "заточен" под left join по индексу
math.join(math_degree)

# выполним left join по столбцу name
pd.merge(math, cs, how="left", on="name")

# #### Left excluding join

# выполним левое соединение и посмотрим, в каком из датафреймов указана та или иная строка
pd.merge(math, cs, how="left", on="name", indicator=True)

# выберем только записи из левого датафрейма и удалим столбец _merge
# все это можно сделать, применив несколько методов подряд
pd.merge(math, cs, how="left", on="name", indicator=True).query(
    '_merge == "left_only"'
).drop(columns="_merge")

# #### Right join

# выполним правое соединение с помощью параметра how = 'right'
pd.merge(math, cs, how="right", on="name")

# #### Right excluding join

# выполним правое соединение и посмотрим, в каком из датафреймов указана та
# или иная строка
pd.merge(math, cs, how="right", on="name", indicator=True)

# воспользуемся методом .query() и оставим записи, которые есть только в
# правом датафрейме
# после этого удалим столбец _merge
pd.merge(math, cs, how="right", on="name", indicator=True).query(
    '_merge == "right_only"'
).drop(columns="_merge")

# #### Outer join

# внешнее соединение сохраняет все строки обоих датафреймов
pd.merge(math, cs, how="outer", on="name")

# #### Full Excluding Join

# найдем какие записи есть только в левом датафрейме, только в правом и в обоих
pd.merge(math, cs, on="name", how="outer", indicator=True)

# оставим только те записи, которых нет в обоих датафреймах
pd.merge(math, cs, on="name", how="outer", indicator=True).query(
    '_merge != "both"'
).drop(columns="_merge")

# #### Inner join

# для внутреннего соединения используется параметр how = 'inner'
pd.merge(math, cs, how="inner", on="name")

# по умолчанию в pd.merge() стоит именно how = 'inner'
pd.merge(math, cs)

# #### Соединение датафреймов и дубликаты

# Пример 1.

# создадим два датафрейма: один с названием товара, другой - с ценой
product_data = pd.DataFrame(
    [[1, "холодильник"], [2, "телевизор"]], columns=["code", "product"]
)
price_data = pd.DataFrame([[1, 40000], [1, 60000]], columns=["code", "price"])

product_data

price_data

# левое соединение сохранит все имеющиеся данные
pd.merge(product_data, price_data, how="left", on="code")

# при правом соединении часть данных будет потеряна
pd.merge(product_data, price_data, how="right", on="code")

# Пример 2.

# +
# создадим два датафрейма
exams_dict = {
    "professor": ["Погорельцев", "Преображенский", "Архенгельский", "Дятлов", "Иванов"],
    "student": [101, 102, 103, 104, 101],
    "score": [83, 84, 78, 80, 82],
}

students_dict = {
    "student_id": [101, 102, 103, 104],
    "student": ["Андрей", "Елена", "Антон", "Татьяна"],
}

exams = pd.DataFrame(exams_dict)
students = pd.DataFrame(students_dict)
# -

# в первом датафрейме содержится информация о результатах экзамена
# с фамилией экзаменатора, идентификатором студента и оценкой
exams

# во втором, идентификатор студента и его или ее имя
students

# если строка повторяется, данные продублируются
# кроме того обратите внимание на суффиксы, их можно изменить через
# параметр suffixes = ('_x', '_y')
pd.merge(exams, students, left_on="student", right_on="student_id")

# #### Cross join

# создадим датафрейм со столбцом xy и двумя значениями (x и y)
df_xy = pd.DataFrame({"xy": ["x", "y"]})
df_xy

# создадим еще один датафрейм со столбцом 123 и тремя значениями (1, 2 и 3)
df_123 = pd.DataFrame({"123": [1, 2, 3]})
df_123

# поставим в соответствие каждому из элементов первого датафрейма
# элементы второго
pd.merge(df_xy, df_123, how="cross")

# для сравнения соединим датафреймы с помощью right join
pd.merge(df_xy, df_123, how="right", left_index=True, right_index=True)

# #### `pd.merge_asof()`

# +
# создадим два датафрейма
trades = pd.DataFrame(
    {
        "time": pd.to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.038",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
            ]
        ),
        "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
        "price": [51.95, 51.95, 720.77, 720.92, 98.00],
        "quantity": [75, 155, 100, 100, 100],
    },
    columns=["time", "ticker", "price", "quantity"],
)

quotes = pd.DataFrame(
    {
        "time": pd.to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.023",
                "20160525 13:30:00.030",
                "20160525 13:30:00.041",
                "20160525 13:30:00.048",
                "20160525 13:30:00.049",
                "20160525 13:30:00.072",
                "20160525 13:30:00.075",
            ]
        ),
        "ticker": ["GOOG", "MSFT", "MSFT", "MSFT", "GOOG", "AAPL", "GOOG", "MSFT"],
        "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
        "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03],
    },
    columns=["time", "ticker", "bid", "ask"],
)
# -

# в первом будет содержаться информация о сделках, совершенных с ценными
# бумагами
# (время сделки, тикер эмитента, цена и количество бумаг)
trades

# во втором, котировки ценных бумаг в определенный момент времени
quotes

# выполним левое соединение merge_asof
pd.merge_asof(
    trades,
    quotes,
    # по столбцу времени
    on="time",
    # но так, чтобы совпадало значение столбца ticker
    by="ticker",
    # совпадение по времени должно составлять менее 10 миллисекунд
    tolerance=pd.Timedelta("10ms"),
)

# еще раз выполним соединение merge_asof
pd.merge_asof(
    trades,
    quotes,
    on="time",
    by="ticker",
    # уменьшим интервал до пяти миллисекунд
    tolerance=pd.Timedelta("10ms"),
    # разрешив искать в предыдущих и будущих периодах
    direction="nearest",
)

# ## Группировка

# ### Метод `.groupby()`

# +
load_dotenv()

train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
response = requests.get(train_csv_url)
titanic = pd.read_csv(io.BytesIO(response.content))

# оставим только столбцы PassengerId, Name, Ticket и Cabin
titanic.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)

# посмотрим на результат
titanic.head()
# -

# посмотрим на размерность
print(titanic.shape)

# метод .groupby() создает объект DataFrameGroupBy
# выполним группировку по столбцу Sex
print(titanic.groupby("Sex"))

# посмотрим, сколько было создано групп
print(titanic.groupby("Sex").ngroups)

# атрибут groups выводит индекс наблюдений, отнесенных к каждой из групп
# выберем группу female (по ключу словаря) и
# выведем первые пять индексов (через срез списка), относящихся к этой группе
print(titanic.groupby("Sex").groups["female"][:5])

# метод .size() выдает количество элементов в каждой группе
titanic.groupby("Sex").size()

# метод .first() выдает первые встречающиеся наблюдения в каждой из групп
# можно использовать .last() для получения последних записей
titanic.groupby("Sex").first()

# метод .get_group() позволяет выбрать наблюдения только одной группы
# выберем наблюдения группы male и выведем первые пять строк датафрейма
titanic.groupby("Sex").get_group("male").head()

# ### Агрегирование данных

# #### Статистика по столбцам

# статистика по одному столбцу
# посчитаем медианный возраст мужчин и женщин
titanic.groupby("Sex").Age.median().round(1)

# статистика по нескольким столбцам
# рассчитаем среднее арифметическое по столбцам Age и Fare для каждого из классов
titanic.groupby("Pclass")[["Age", "Fare"]].mean().round(1)

# статистика по всем столбцам
# среднее арифметическое не получится рассчитать для категориальных признаков,
# их придется удалить
titanic.drop(columns=["Sex", "Embarked"]).groupby("Pclass").mean().round(1)

# выполним группировку по двум признакам (Pclass и Sex)
# с расчетом количества наблюдений в каждой подгруппе по каждому столбцу
titanic.groupby(["Pclass", "Sex"]).count()

# значение атрибута ngroups Pandas считает по подгруппам
print(titanic.groupby(["Pclass", "Sex"]).ngroups)

# #### Метод `.agg()`

# применим метод .agg() к одному столбцу (Sex) и сразу найдем
# максимальное и минимальное значения, количество наблюдений, а также
# медиану и среднее арифметическое
titanic.groupby("Sex").Age.agg(["max", "min", "count", "median", "mean"]).round(1)

# для удобства при группировке и расчете показателей столбцы можно
# переименовать
titanic.groupby("Sex").Age.agg(sex_max="max", sex_min="min")
# titanic.groupby("Sex").Age.agg({"sex_max": "max", "sex_min": "min"})

# ### Фильтрация

# найдем среднее арифметическое возраста внутри каждого из классов каюты
titanic.groupby("Pclass")[["Age"]].mean()

# выберем только те классы кают, в которых среднегрупповой возраст не менее 26 лет
# для этого применим метод .filter с lambda-функцией
titanic.groupby("Pclass").filter(lambda x: x["Age"].mean() >= 26).head()

# убедимся, что у нас осталось только два класса
# для этого из предыдущего результата возьмем столбец Pclass и применим метод .
# unique()
titanic.groupby("Pclass").filter(lambda x: x["Age"].mean() >= 26).Pclass.unique()

# ### Сводные таблицы

# +
cars_csv_url = os.environ.get("CARS_CSV_URL", "")
response = requests.get(cars_csv_url)
cars = pd.read_csv(io.BytesIO(response.content))

# удалим столбцы, которые нам не понадобятся
cars.drop(columns=["Unnamed: 0", "vin", "lot", "condition"], inplace=True)

# и посмотрим на результат
cars.head()
# -

# #### Группировка по строкам

# +
# для создания сводной таблицы необходимо указать данные
pd.pivot_table(
    cars,
    # по какому признаку проводить группировку
    index="brand",
    # и для каких признаков рассчитывать показатели
    values=["mileage", "price", "year"],
).round(2).head(10)

# по умолчанию будет рассчитано среднее арифметическое внутри каждой из групп
# -

# добавим параметры values - по каким столбцам считать статистику группы
# и пропишем aggfunc - какая именно статистика нас интересует
pd.pivot_table(
    cars,
    # сгруппируем по марке
    index="brand",
    # считать статистику будем по цене и пробегу
    values=["price", "mileage"],
    # для каждой группы найдем медиану и выведем первые 10 марок
    aggfunc="median",
).round(2).head(10)

# +
# в качестве несложного примера пропишем функцию, которая возвращает среднее
# арифметическое


def custom_mean(y_var: pd.Series[float]) -> float:
    """Return the average value of a numeric list."""
    return sum(y_var) / len(y_var)


# -

# применим как встроенную, так и собственную функцию к столбцу price
pd.pivot_table(
    cars, index="brand", values="price", aggfunc=["mean", custom_mean]
).round(2).head(10)

# сгруппируем данные по марке, а затем по цвету кузова
# для каждой подгруппы рассчитаем медиану и количество наблюдений (count)
pd.pivot_table(
    cars, index=["brand", "color"], values="price", aggfunc=["median", "count"]
).round(2).head(11)

# найдем медианную цену для каждой марки с разбивкой по категориям title_status
pd.pivot_table(
    cars, index="brand", columns="title_status", values="price", aggfunc="median"
).round(2).head()

# добавим метрику count и
# применим метод .transpose(), чтобы поменять строки и столбцы местами
pd.pivot_table(
    cars,
    index="brand",
    columns="title_status",
    values="price",
    aggfunc=["median", "count"],
).round().head().transpose()

# #### Дополнительные возможности

# метод .style.background_gradient() позволяет добавить цветовую маркировку
pd.pivot_table(
    cars, index=["brand", "color"], values="price", aggfunc=["median", "count"]
).round(2).head(11).style.background_gradient()

# для выделения пропущенных значений используется метод .style.highlight_null()
# цвет выбирается через параметр color
pd.pivot_table(
    cars, index="brand", columns="title_status", values="price", aggfunc="median"
).round(2).head(11).style.highlight_null(color="yellow")

# на основе сводных таблиц можно строить графики
# например, можно посмотреть количество автомобилей (aggfunc = 'count')
# со статусом clean и salvage (title_status),
# сгруппированных по маркам (index)
pd.pivot_table(
    cars, index="brand", columns="title_status", values="price", aggfunc="count"
).round(2).head(3).plot.barh(figsize=(10, 7), title="Clean vs. Salvage Counts");

# метод .unstack() как бы убирает второе измерение
# по сути, мы также группируем данные по нескольким признакам, но только по
# строкам
pd.pivot_table(
    cars, index="brand", columns="title_status", values="price", aggfunc="median"
).round(2).head().unstack()

# создадим маску для автомобилей "БМВ" и сделаем копию датафрейма
bmw = cars[cars["brand"] == "bmw"].copy()
# установим новый индекс, удалив при этом старый
bmw.reset_index(drop=True, inplace=True)
# удалим столбец brand, так как у нас осталась только одна марка
bmw.drop(columns="brand", inplace=True)
# посмотрим на результат
bmw.head()

# сгруппируем данные по штату и году выпуска, передав их в параметр index
# и найдем медианну цену
pd.pivot_table(bmw, index=["state", "year"], values="price", aggfunc="median").round(2)

# когда группировка выполняется только по строкам,
# мы можем получить аналогичный результат с помощью метода .groupby()
bmw.groupby(by=["state", "year"])[["price"]].agg("median")

# метод .query() позволяет отфильтровать данные
pd.pivot_table(bmw, index=["state", "year"], values="price", aggfunc="median").round(
    2
).query("price > 20000")

# применим метод .style.bar() и создадим встроенную горизонтальную столбчатую
# диаграмму
# цвет в параметр color можно, в частности, передавать в hex-формате
pd.pivot_table(bmw, index=["state", "year"], values="price", aggfunc="median").round(
    2
).style.bar(color="#d65f5f")
