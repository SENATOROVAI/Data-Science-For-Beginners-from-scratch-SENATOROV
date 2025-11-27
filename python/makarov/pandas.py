"""Pandas."""

# +
# # Способ 2. Подключение к базе данных SQL
# # импортируем модуль sqlite3 для работы с базой данных SQL
# import sqlite3 as sql

# # Способ 3. Создание датафрейма из словаря
# import numpy as np

# # создадим пустой словарь
# # Создание датафрейма
# # Способ 1. Создание датафрейма из файла
# import pandas as pd

# # испортируем файл из папки content и выведем первые три строки
# csv_zip = pd.read_csv("/content/train.zip")
# csv_zip.head(3)

# +
# # импортируем данные в формате Excel, указав номер листа, который хотим использовать
# excel_data = pd.read_excel("/content/iris.xlsx", sheet_name=0)
# excel_data.head(3)

# +
# # передадим соответствующую ссылку в функцию pd.read_html()
# # в параметре match укажем ключевые слова, которые помогут найти нужную таблицу
# html_data = pd.read_html(
#     "https://en.wikipedia.org/wiki/World_population", match="World population"
# )
# # мы получили пять результатов
# len(html_data)

# +
# # создадим соединение с базой данных chinook
# conn = sql.connect("/content/chinook.db")

# # выберем все строки из таблицы tracks
# sql_data = pd.read_sql("SELECT * FROM tracks", conn)  # vs. read_sql_query

# # посмотрим на результат
# sql_data.head(3)

# +
# # создадим несколько списков и массивов Numpy с информацией о семи странах мира
# country = np.array(
#     [
#         "China",
#         "Vietnam",
#         "United Kingdom",
#         "Russia",
#         "Argentina",
#         "Bolivia",
#         "South Africa",
#     ]
# )
# capital = ["Beijing", "Hanoi", "London", "Moscow", "Buenos Aires", "Sucre", "Pretoria"]
# population = [1400, 97, 67, 144, 45, 12, 59]  # млн. человек
# area = [9.6, 0.3, 0.2, 17.1, 2.8, 1.1, 1.2]  # млн. кв. км.
# sea = [1] * 5 + [0, 1]  # выход к морю (в этом списке его нет только у Боливии)

# +
# countries_dict = {}
# # превратим эти списки в значения словаря,
# # одновременно снабдив необходимыми ключами
# countries_dict["country"] = country
# countries_dict["capital"] = capital
# countries_dict["popilation"] = population
# countries_dict["area"] = area
# countries_dict["sea"] = sea
# countries = pd.DataFrame(countries_dict)

# +
# # Способ 4. Создание датафрейма из 2D массива Numpy
# # внешнее измерение будет столбцами, внутренее - строками
# arr = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# pd.DataFrame(arr)

# +
# countries.columns

# +
# countries.index

# +
# countries.values

# +
# countries.axes[0]

# +
# countries.ndim, countries.shape, countries.size

# +
# countries.dtypes

# +
# countries.memory_usage()

# +
# # Индекс датафрейма
# # создадим список с кодами стран
# custom_index = ["CN", "VN", "GB", "RU", "AR", "BO", "ZA"]

# countries = pd.DataFrame(countries_dict, index=custom_index)
# countries

# +
# # при этом параметр inplace = True сделает изменения постоянными
# countries.reset_index(inplace=True)
# countries

# +
# # передадим методу название столбца, который хотим сделать индексом
# countries.set_index("index", inplace=True)
# countries

# +
# countries.reset_index(drop=True, inplace=True)
# countries

# +
# countries.index = custom_index
# countries

# +
# # Многоуровневый индекс
# # создадим список из кортежей с названием континента и кодом страны
# rows = [
#     ("Asia", "CN"),
#     ("Asia", "VN"),
#     ("Europe", "GB"),
#     ("Europe", "RU"),
#     ("S. America", "AR"),
#     ("S. America", "BO"),
#     ("Africa", "ZA"),
# ]

# +
# # в столбцах название страны и столицы мы объединим в категорию names
# # а размер населения, площадь и выход к морю в data
# cols = [
#     ("names", "country"),
#     ("names", "capital"),
#     ("data", "population"),
#     ("data", "area"),
#     ("data", "sea"),
# ]

# +
# # создадим многоуровневый индекс для строк
# # индексам присвоим названия через names = ['region', 'code']
# custom_multindex = pd.MultiIndex.from_tuples(rows, names=["region", "code"])

# # сделаем то же самое для столбцов
# custom_multicols = pd.MultiIndex.from_tuples(cols)

# +
# countries.index = custom_multindex
# countries.columns = custom_multicols

# countries

# +
# # вернемся к обычному индексу и названиям столбцов
# custom_cols = ["country", "capital", "population", "area", "sea"]

# countries.index = custom_index
# countries.columns = custom_cols

# countries

# +
# # Преобразование в другие форматы
# print(countries.to_dict())

# +
# countries.to_numpy()

# +
# # Создание Series
# country_list = [
#     "China",
#     "South Africa",
#     "United Kingdom",
#     "Russia",
#     "Argentina",
#     "Vietnam",
#     "Australia",
# ]

# +
# country_series = pd.Series(country_list)
# country_series

# +
# # Создание Series из словаря
# country_dict = {
#     "CN": "China",
#     "ZA": "South Africa",
#     "GB": "United Kingdom",
#     "RU": "Russia",
#     "AR": "Argentina",
#     "VN": "Vietnam",
#     "AU": "Australia",
# }

# country_Series = pd.Series(country_dict)
# country_Series

# +
# # Доступ к строкам, столбцам и элементам
# for column in countries:
#     print(column)

# +
# # прервем цикл после первой итерации с помощью break
# for index, row in countries.iterrows():
#     print(index)
#     print(row)

# +
# for _, row in countries.iterrows():
#     # например, сформируем вот такое предложение
#     print(row["capital"] + " is the capital of " + row["country"])
#     break

# +
# # Доступ к столбцам

# # выведем столбец capital датафрейма countries
# countries["capital"]

# +
# # однако в этом случае название не должно содержать пробелов
# countries.capital

# +
# countries[["capital", "area"]]

# +
# countries.filter(items=["capital", "population"])

# +
# # Доступ к строкам
# # выведем строки со второй по пятую (не включительно)
# countries[1:5]

# +
# # Методы .loc[] и .iloc[]
# # для этого передадим методу .loc[] два списка:
# # с индексами строк и названиями столбцов
# countries.loc[["CN", "RU", "VN"], ["capital", "population", "area"]]

# +
# # например, выведем все строки датафрейма
# countries.loc[:, ["capital", "population", "area"]]

# +
# # Метод .loc[] также поддерживает значения Boolean.
# # например, выведем все строки и только последний столбец,
# # передав список соответствующих логических значений
# countries.loc[:, [False, False, False, False, True]]

# +
# позволяет узнать порядковый номер
# (начиная с нуля) строки или столбца
# по их индексу и названию соответственно.
# # выведем номер строки с индексом RU
# countries.index.get_loc("RU")

# +
# # теперь в списки мы передаем номера строк и столбцов,
# # нумерация начинается с нуля
# countries.iloc[[0, 3, 5], [0, 1, 2]]

# +
# countries.iloc[:3, -2:]

# +
# countries[["population", "area"]].iloc[[0, 3]]

# +
# # Многоуровневый индекс и методы .loc[] и .iloc[]
# # вновь создадим датафрейм с многоуровневым индексом по строкам и столбцам
# countries.index = custom_multindex
# countries.columns = custom_multicols

# countries

# +
# countries.loc["Asia", "CN"]

# +
# # выведем первую строку и столбцы с числовыми данными
# countries.loc[
#     ("Asia", "CN"), [("data", "population"), ("data", "area"), ("data", "sea")]
# ]

# +
# # например, выведем только азиатские страны
# countries.loc[("Asia", ["CN", "VN"]), :]

# +
# # Метод .xs()
# # выберем Европу из уровня region
# # axis = 0 указывает, что мы берем строки
# countries.xs("Europe", level="region", axis=0)

# +
# # levels указывает, на каких уровнях искать названия столбцов
# # параметр axis = 1 говорит о том, что мы имеем дело со столбцами
# countries.xs(("names", "country"), level=[0, 1], axis=1)

# +
# # обновим атрибуты index и columns
# countries.index = custom_index
# countries.columns = custom_cols

# # посмотрим на исходный датафрейм
# countries

# +
# # Метод .at[]
# countries.at["CN", "capital"]

# +
# # создадим логическую маску для стран с населением больше миллиарда человек
# countries.population > 1000

# +
# # применим логическую маску к исходному датафрейму
# countries[countries.population > 1000]

# +
# # отфильтруем датафрейм по критериям численности населения и площади
# countries[(countries.population > 50) & (countries.area < 2)]

# +
# # Метод .query() позволяет задавать условие фильтрации «своими словами».
# # например, выберем страны с населением более 50 млн. человек И
# # площадью менее двух млн. кв. километров
# countries.query("population > 50 and area < 2")
