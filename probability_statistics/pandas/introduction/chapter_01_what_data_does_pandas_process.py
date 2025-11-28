"""What data does pandas process?."""

# # Какие данные обрабатывает pandas?

# Импортируем модуль pandas:

import pandas as pd

# В основе работы `pandas` лежит табличное представление данных:
#
# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/01_table_dataframe.svg">
# </div>

# В качестве примера рассмотрим данные о пассажирах Титаника. 
#
# <img src="https://avatars.mds.yandex.net/get-kinopoisk-post-img/1374145/6aae47e9a525adfb3c9c433be10e62df/1920x1080" height="300px" width="500px" >
#
# Для ряда пассажиров я знаю имя (символы), возраст (целые числа) и пол (мужской / женский).

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

df

# Полученная структура данных называется [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame).
#
# Напоминает обычные таблицы:

# <img src="https://pandas.pydata.org/pandas-docs/stable/_images/01_table_spreadsheet.png" height="200px" width="400px" >

# Каждый столбец в структуре `DataFrame` является типом [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series):
#
# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/01_table_series.svg">
# </div>

# Выбрать столбец из таблицы:

df["Age"]

# Внешне очень напоминает питоновский [словарь](https://docs.python.org/3/tutorial/datastructures.html#tut-dictionaries).

# Вы также можете создать `Series` с нуля:

ages = pd.Series([22, 35, 58], name="Age")

ages

# ### Сделайте что-нибудь с DataFrame или Series

# Я хочу узнать максимальный возраст пассажиров, применив функцию `max()` к столбцу таблицы:

df["Age"].max()

# или к типу данных `Series`:

ages.max()

# Помимо поиска максимального в `pandas` существует [большой набор функций](https://pandas.pydata.org/docs/user_guide/basics.html?highlight=describe#descriptive-statistics).

# Если интересует некоторая базовая статистика числовых данных:

df.describe()

# [`describe()`](https://pandas.pydata.org/docs/user_guide/basics.html?highlight=describe#summarizing-data-describe) метод обеспечивает краткий обзор численных данных в `DataFrame`. 
#
# Так как столбцы `Name` и `Sex` состоят из текстовых данных, то они не учитываются в `describe()`.
#
# Многие операции в `pandas` возвращают `DataFrame` или `Series`. 
