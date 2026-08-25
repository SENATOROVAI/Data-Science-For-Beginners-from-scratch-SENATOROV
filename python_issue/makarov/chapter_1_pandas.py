"""Pandas library."""

# ## Библиотека Pandas
#

# +
import sqlite3 as sql

import numpy as np
import pandas as pd

# -

# ## Объекты DataFrame и Series
# ### Создание датафрейма
# #### Способ 1. Создание датафрейма из файла

csv_zip = pd.read_csv("/Users/dayal/Downloads/train.csv")
csv_zip.head(3)

excel_data = pd.read_excel("/Users/dayal/Downloads/iris.xlsx", sheet_name=0)
excel_data.head(3)

html_data = pd.read_html(
    "https://en.wikipedia.org/wiki/World_population",
    storage_options={"User-Agent": "Mozilla/5.0"},
)
html_data[0]

len(excel_data)

html_data[0]

# #### Способ 2. Подключение к базе данных SQL
#

# +
conn = sql.connect("/Users/dayal/Downloads/chinook.db")

sql_data = pd.read_sql("SELECT * FROM tracks;", conn)

sql_data.head(3)
# -

# #### Способ 3. Создание датафрейма из словаря
#

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
capital: list[str] = [
    "Beijing",
    "Hanoi",
    "London",
    "Moscow",
    "Buenos Aires",
    "Sucre",
    "Pretoria",
]
population: list[int] = [1400, 97, 67, 144, 45, 12, 59]
area: list[float] = [9.6, 0.3, 0.2, 17.1, 2.8, 1.1, 1.2]
sea: list[int] = [1] * 5 + [0, 1]

# +
countries_dict: dict[str, list[str] | list[int] | list[float]] = {}

countries_dict["country"] = list(country)
countries_dict["capital"] = capital
countries_dict["population"] = population
countries_dict["area"] = area
countries_dict["sea"] = sea
# -

countries = pd.DataFrame(countries_dict)
countries

# #### Способ 4. Создание датафрейма из 2D массива Numpy
#

# +
arr = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

pd.DataFrame(arr)
# -

# ## Структура и свойства датафрейма
#

countries.columns

countries.index

countries.values

countries.axes[0]

countries.axes[1]

countries.ndim, countries.shape, countries.size

countries.dtypes

countries.memory_usage()

# ## Индекс
# ### Присвоение индекса
#

custom_index: list[str] = ["CN", "VN", "GB", "RU", "AR", "BO", "ZA"]

countries = pd.DataFrame(countries_dict, index=custom_index)
countries

countries.reset_index(inplace=True)
countries

countries.set_index("index", inplace=True)
countries

countries.reset_index(drop=True, inplace=True)
countries

countries.index = pd.Index(custom_index)
countries

# ## Многоуровневый индекс
#

# +
rows: list[tuple[str, str]] = [
    ("Asia", "CN"),
    ("Asia", "VN"),
    ("Europe", "GB"),
    ("Europe", "RU"),
    ("S. America", "AR"),
    ("S. America", "BO"),
    ("Africa", "ZA"),
]

cols: list[tuple[str, str]] = [
    ("names", "country"),
    ("names", "capital"),
    ("data", "population"),
    ("data", "area"),
    ("data", "sea"),
]

custom_multindex = pd.MultiIndex.from_tuples(rows, names=["region", "code"])
custom_multicols = pd.MultiIndex.from_tuples(cols)

countries.index = pd.Index(custom_multindex)
countries.columns = custom_multicols

countries

# +
custom_cols = ["country", "capital", "population", "area", "sea"]

countries.index = pd.Index(custom_index)
custom_cols_int = custom_cols
custom_cols_list_str: list[str] = [str(col) for col in custom_cols_int]

countries
# -

# ## Преобразование в другие форматы
#

print(countries.to_dict())

countries.to_numpy()

countries.to_csv("countries.csv", index=False)

countries.country.tolist()

# ## Создание Series
# ### Создание Series из списка
#

# +
country_list: list[str] = [
    "China",
    "South Africa",
    "United Kingdom",
    "Russia",
    "Argentina",
    "Vietnam",
    "Australia",
]

country_series = pd.Series(country_list, dtype=str)
country_series
# -

country_series.iloc[0]

# ## Создание Series из словаря
#

country_dict: dict[str, str] = {
    "CN": "China",
    "ZA": "South Africa",
    "GB": "United Kingdom",
    "RU": "Russia",
    "AR": "Argentina",
    "VN": "Vietnam",
    "AU": "Australia",
}

country_series_2: pd.Series[float] = pd.Series(country_dict)
country_series_2

country_series_2.loc["RU"]

# ## Доступ к строкам и столбцам
# ### Циклы в датафрейме
#

for column in countries:
    print(column)

for index, row in countries.iterrows():
    print(index)
    print(row)
    print("...")
    print(type(row))
    break

for _, row in countries.iterrows():
    print(row["capital"] + " is the capital if " + row["country"])
    break

# ## Доступ к столбцам
#

countries["capital"]

countries.capital

type(countries.capital)

countries[["capital"]]

countries[["capital", "area"]]

countries.filter(items=["capital", "population"])

# ## Доступ к строкам
#

countries[1:5]

# ## Методы .loc[] и .iloc[]
# ### Метод .loc[]
#

countries.loc[["CN", "RU", "VN"], ["capital", "population", "area"]]

countries.loc[:, ["capital", "population", "area"]]

countries.loc[:, [False, False, False, False, True]]

# ## Метод .get_loc()
#

countries.index.get_loc("RU")

countries.columns.get_loc("country")

# ## Метод .iloc[]
#

countries.iloc[[0, 3, 5], [0, 1, 2]]

countries.iloc[:3, -2:]

countries[["population", "area"]].iloc[[0, 3]]

# ## Доступ по многоуровневому индексу
#

# +
countries.index = pd.Index(custom_multindex)
countries.columns = custom_multicols

countries
# -

print(countries.loc["Asia", "CN"])

print(
    countries.loc[
        ("Asia", "CN"), [("data", "population"), ("data", "area"), ("data", "sea")]
    ]
)

countries.loc[("Asia", ["CN", "VN"]), :]

countries.loc["Asia", :]

print(countries.loc[:, [("names", "country"), ("data", "population")]])

print(countries.iloc[3, [2, 3, 4]])

print(countries.xs("Europe", level="region", axis=0))

print(countries.xs(("names", "country"), axis=1))

print(countries.xs("Europe", axis=0).loc[:, ("names", slice(None))])

# +
countries.index = pd.Index(custom_index)

countries
# -

# ## Метод .at[]
#

countries.at["CN", "capital"]

# ## Фильтры
# ### Логическая маска
#

countries.population > 1000

countries[countries.population > 1000]

countries[(countries.population > 50) & (countries.area < 2)]

# +
population_mask = countries.population > 70
area_mask: pd.Series[bool] = countries.population < 50

mask: pd.Series[bool] = population_mask | area_mask

countries[mask]
# -

# ## Метод .query()
#

countries.query("population > 50 and area < 2")

countries.query('country == "United Kingdom"')

# ## Другие способы фильтрации
#

# +
keyword_list = ["Beijing", "Moscow", "Hanoi"]

print(countries[countries.capital.isin(keyword_list)])
# -

print(countries[~countries.country.str.startswith("A")])

countries.nlargest(3, "population")

countries.area.argmax()

print(countries.iloc[[countries.area.argmax()]])

countries.loc[countries.population > 90, :]

countries.filter(like="ZA", axis=0)

# ## Сортировка
#

countries.sort_values(by="population", inplace=False, ascending=True)

countries.sort_values(by=["area", "population"], inplace=False, ascending=False)

countries.sort_index()
