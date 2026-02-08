"""Pandas."""

# ## Библиотека Pandas

# +
# Подключение к базе данных SQL
import sqlite3 as sql

import numpy as np
import pandas as pd
import requests
from pandas import Index

# -

# ### Объекты DataFrame и Series

# #### Создание датафрейма

# из архива .zip, который содержит только один файл
csv_zip = pd.read_csv("./content/train.zip")
csv_zip.head(3)

# из excel-файла
excel_data = pd.read_excel("./content/iris.xlsx", sheet_name=0)
excel_data.head(3)

# +
# из элементов (таблицы) на web-странице
# используем requests с правильными заголовками для обхода блокировки
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(
    "https://en.wikipedia.org/wiki/World_population", headers=headers
)

html_data = pd.read_html(response.text, match="World population")
# -

len(html_data)

html_data[0]

# +
# подключение
conn = sql.connect("./content/chinook.db")

# выберем все строки из таблицы tracks
sql_data = pd.read_sql("SELECT * FROM tracks;", conn)

sql_data.head(3)
# -

# #### Создание датафрейма из словаря

# создадим несколько списков и массивов Numpy
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
    ["Beijing", "Hanoi", "London", "Moscow", "Buenos Aires", "Sucre", "Pretoria"]
)
population = np.array([1400, 97, 67, 144, 45, 12, 59])  # млн. человек
area = np.array([9.6, 0.3, 0.2, 17.1, 2.8, 1.1, 1.2])  # млн. кв. км.
sea = np.array([1] * 5 + [0, 1])

# +
countries_dict = {}

countries_dict["country"] = country
countries_dict["capital"] = capital
countries_dict["population"] = population
countries_dict["area"] = area
countries_dict["sea"] = sea

countries_dict
# -

# создадим датафрейм
countries = pd.DataFrame(countries_dict)
countries

# #### Создание датафрейма из 2D массива Numpy

arr = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
pd.DataFrame(arr)

# ### Структура и свойства датафрейма

# названия столбцов
countries.columns

# способ идентификации строк
countries.index

# значения
countries.values

# выведем описание индекса датафрейма через атрибус axes[0]
countries.axes[0]

# axes[1] выводит названия столбцов
countries.axes[1]

# количество измерений
print(countries.ndim)
# размерность
print(countries.shape)
# общее кол-во элементов
print(countries.size)

# типы каждого столбца
countries.dtypes

# объем занимаемой памяти по столбцам
countries.memory_usage()

# ### Индекс

# #### Присвоение индекса

# в датафейме можно задать собственный индекс
# например коды стран
custom_index: "Index[str]" = pd.Index(
    ["CN", "VN", "GB", "RU", "AR", "BO", "ZA"], dtype="string"
)

countries = pd.DataFrame(countries_dict, index=custom_index)
countries

# сброс индекса
# параметр inplace = True сохраняет изменения
countries.reset_index(inplace=True)
countries

# прошлый индекс стал отдельным столбцом
# чтобы снова сделать индексом .set_index
countries.set_index("index", inplace=True)
countries

# снова сбросим но без сохранения
countries.reset_index(drop=True, inplace=True)
countries

# собственный индекс
countries.index = custom_index
countries

# #### Многоуровневые индекс и названия столбцов

# +
multiple_rows = [
    ("Asia", "CN"),
    ("Asia", "VN"),
    ("Europe", "GB"),
    ("Europe", "RU"),
    ("S. America", "AR"),
    ("S. America", "BO"),
    ("Africa", "ZA"),
]

multiple_cols = [
    ("names", "country"),
    ("names", "capital"),
    ("data", "population"),
    ("data", "area"),
    ("data", "sea"),
]

# мульти-индексы из кортежей
custom_multindex = pd.MultiIndex.from_tuples(multiple_rows, names=["region", "code"])

# мульти-столбцы из кортежей
custom_multicols = pd.MultiIndex.from_tuples(multiple_cols)

# передадим в датафрейм
countries.index = custom_multindex
countries.columns = custom_multicols

countries
# -

# вернемся к обычному индексу и названиям столбцов
custom_cols1: "Index[str]" = pd.Index(
    ["country", "capital", "population", "area", "sea"], dtype="string"
)

countries.index = custom_index

countries.columns = custom_cols1

print(countries)

# ### Преобразование в другие форматы

# в словарь
print(countries.to_dict())

# Numpy=array
countries.to_numpy()

# файл
# index = False, чтобы не сохранять индекс
countries.to_csv("./content/countries.csv", index=False)

# Series в список
print(countries.country.to_list())

# ### Создание Series

# #### Создание Series из списка

country_list = [
    "China",
    "South Africa",
    "United Kingdom",
    "Russia",
    "Argentina",
    "Vietnam",
    "Australia",
]

country_series = pd.Series(country_list)
country_series

# доступ к элементам по индексу
country_series[0]

# #### Создание Series из словаря

country_dict = {
    "CN": "China",
    "ZA": "South Africa",
    "GB": "United Kingdom",
    "RU": "Russia",
    "AR": "Argentina",
    "VN": "Vietnam",
    "AU": "Australia",
}

country_series = pd.Series(country_dict)
country_series

# теперь для доступа к элементам можно использовать индекс
# которым у нас являются коды стран
country_series["AU"]

# ## Доступ к строкам и столбцам

# ### Циклы в датафрейме

for columns in countries:
    print(columns)

# .iterrows() - Series с индексом каждой строки и её значением
for index, row in countries.iterrows():
    print(index)
    print(row)
    print("...")
    print(type(row))
    break

# использование данных определённой строки
for _, row in countries.iterrows():
    print(row["capital"] + " is the capital of " + row["country"])
    break

# ### Доступ к столбцам

# +
# в отличие от Series, в датафрейме через квадратные скобки
# происходит доступ к столбцам

countries["capital"]

# +
# также можно через точку, но без пробелов

countries.capital

# +
# отдельные столбцы - Series

print(type(countries.capital))
print(type(countries["capital"]))
# -

# внутренние скобки - список столбцов
# внешние скобки - сам оператор индексации
# поэтому на выходи получится DataFrame, а не Series
countries[["capital"]]

# к нескольким столбцам
countries[["capital", "area"]]

# через метод .filter()
# с параметром items
countries.filter(items=["capital", "population"])

# ### Доступ к строкам

# доступ к строкам с помощью индекса
# не включая верхнюю границу
countries[1:5]

# ### Методы `.loc[]` и `iloc[]`

# #### Метод `.loc[]`

# label-based location
# метод .loc[] позволяет получить доступ
# к строкам и столбцам по их названиям
countries.loc[["CN", "RU", "VN"], ["capital", "population", "area"]]

# через : можно вывести все столбцы/строки
countries.loc[:, ["capital", "population", "area"]]

# также можно передавать значения Boolean
# чтобы фильтровать данные по условию
countries.loc[:, [False, False, False, False, True]]

# #### Метод `.get_loc()`

# атрибут index и метод .get_loc
# позволяют вывести порядковый номер
# строки по индексу (начиная с нуля)
countries.index.get_loc("RU")

# атрибут columns и метод .get_loc
# позволяют вывести порядковый номер
# столбца по названию (начиная с нуля)
countries.columns.get_loc("country")

# Метод `.iloc[]`

# integer-based location
# метод .iloc[] позволяет получить доступ
# к строкам и столбцам по числовому индексу
countries.iloc[[0, 3, 5], [0, 1, 2]]

# можно использовать срезы
countries.iloc[:3, -2:]

# удобно использовать доступ
# с помощью квадратных скобок
# и метода .iloc[]
countries[["population", "area"]].iloc[[0, 3]]

# #### Доступ по многоуровневому индексу

# +
countries.index = custom_multindex
countries.columns = custom_multicols

countries
# -

# доступ к первой строке
# с помощью двойного индекса
# и метода .loc[]
countries.loc["Asia", "CN"]

# также можно передавать значения в
# форме кортежей для строк и столбцов
countries.loc[
    ("Asia", "CN"),  # мульти-индексы
    [
        ("data", "population"),  # мульти-названия столбцов
        ("data", "area"),
        ("data", "sea"),
    ],
]

# доступ к строкам можно получить,
# указав внутри кортежа название региона,
# список с кодами стран
countries.loc[("Asia", ["CN", "VN"]), :]

# можно указать только регион
# тогда мы получим все страны,
# которые в него входят
countries.loc[("Asia"), :]

# аналогично можно получить доступ к столбцам
countries.loc[:, [("names", "country"), ("data", "population")]]

# метод .iloc[] игнорирует структуру многоуровневого индекса
# и использует простой числовой индекс
countries.iloc[3, [2, 3, 4]]

# ### Метод `.xs()`

# cross-secton
# позволяет получить доступ к определённому уровню
# многоуровневого индекса
# на уровне 'r
# axis = 0, чтобы отбирались строки
countries.xs("Europe", level="region", axis=0)

# на первом уровне выберем 'names'
# на втором уровне выберем 'country'
# axis = 1, чтобы отбирались столбцы
countries.xs(("names", "country"), level=(0, 1), axis=1)

# можно разбить на два xs
# чтобы не использовать level
countries.xs("names", axis=1, level=0).xs("Europe", axis=0)

# +
# вернём одноуровневость
countries.index = custom_index
countries.columns = custom_cols1

countries
# -

# ### Метод `.at[]`

# только для одной ячейки
countries.at["CN", "capital"]

# ### Фильтры

# #### Логическая маска

# создадим логическую маску
countries.population > 1000

# применим логическую маску
countries[countries.population > 1000]

# & - логическое И
countries[(countries.population > 50) & (countries.area < 2)]

# +
# | - логическое ИЛИ
population_mask = countries.population > 70
area_mask = countries.population < 50

mask = population_mask | area_mask
countries[mask]
# -

# ### Метод `.query()`

# условия дословно
countries.query("population > 50 and area < 2")

# использование кавычек
countries.query("country == 'United Kingdom'")

# ### Другие способы фильтрации

# +
# проверка вхождения
keyword_list = ["Beijing", "Moscow", "Hanoi"]

print(countries[countries.capital.isin(keyword_list)])
# -

# строка начинается с ...
# ~ - логическое НЕ
print(countries[~countries.country.str.startswith("A")])

# n наибольших
countries.nlargest(3, "population")

# n наименьших
countries.nsmallest(3, "population")

# argmax() индекс наибольшей
# argmin() индекс наименьшей
countries.area.argmax()

# соответствующая страна
print(countries.iloc[[int(countries.area.argmax())]])

# логические маски можно использовать с loc
countries.loc[countries.population > 90, :]

# .filter с параметром like позволяет искать совпадения в
# индексе (axis = 0) или столбцах (axis = 1)
countries.filter(like="ZA", axis=0)

# ### Сортировка

countries.sort_values(by="population", inplace=False, ascending=True)  # восходящий

countries.sort_values(
    by=["area", "population"], inplace=False, ascending=False  # нисходящий
)

# сортировка по индексу
countries.sort_index()
