"""Tidy data in Python."""

# # Аккуратные данные в Python

# Недавно я наткнулся на статью Хэдли Уикхэма (*Hadley Wickham*) под названием [*Tidy Data*](http://vita.had.co.nz/papers/tidy-data.pdf) (Аккуратные Данные).
#
# Документ, опубликованный еще в 2014 году, посвящен одному аспекту очистки данных, упорядочиванию: структурированию наборов данных для упрощения анализа. В документе Уикхэм демонстрирует, как любой набор данных может быть структурирован до проведения анализа. Он подробно описывает различные типы наборов данных и способы их преобразования в стандартный формат.
#
# Очистка данных - одна из самых частых задач в области науки о данных. Независимо от того, с какими данными вы имеете дело или какой анализ вы выполняете, в какой-то момент вам придется очистить данные. Приведение данных в порядок упрощает работу в будущем.
#
# > Библиотеки для построения графиков [`Altair`](https://dfedorov.spb.ru/pandas/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Altair.html) и `Plotly` на входе принимают фреймы данных в аккуратном формате.
#
# В этой заметке я обобщу некоторые примеры наведения порядка, которые Уикхэм использует в своей статье, и продемонстрирую, как это сделать с помощью *Python* и  *pandas*.
#
# ## Определение аккуратных данных
# Структура, которую Уикхэм определяет как аккуратная (*tidy*), имеет следующие атрибуты:
#
# - Каждая переменная (`variable`) образует столбец и содержит значения (`values`).
# - Каждое наблюдение (`observation`) образует строку.
# - Каждый объект наблюдения (`observational unit`) составляет таблицу.
#
# Несколько определений:
#
# - *Переменная*: измерение или атрибут. Рост, вес, пол и т. д.
# - *Значение*: фактическое измерение или атрибут. 152 см, 80 кг, самка и др.
# - *Наблюдение*: все значения измеряются на одном объекте. Каждый человек.
#
# Пример беспорядочного набора данных (*messy dataset*):
#
# ![](https://github.com/dm-fedorov/pandas_basic/blob/master/pic/not_tidy.jpg?raw=true)
#
# Пример аккуратного набора данных (*tidy dataset*):
#
# ![](https://github.com/dm-fedorov/pandas_basic/blob/master/pic/tidy.jpg?raw=true)
#
# ## Убираем беспорядочные наборы данных
# С помощью следующих примеров, взятых из статьи Уикхема, мы преобразуем беспорядочные наборы данных в аккуратный формат. Цель здесь не в том, чтобы проанализировать наборы данных, а, скорее, в их стандартизированной подготовке перед анализом.
#
# Рассмотрим пять типов беспорядочных наборов данных:
#
#     1) Заголовки столбцов - это значения, а не имена переменных.
#     2) Несколько переменных хранятся в одном столбце.
#     3) Переменные хранятся как в строках, так и в столбцах.
#     4) В одной таблице хранятся несколько единиц объектов наблюдения (observational units).
#     5) Одна единица наблюдения хранится в нескольких таблицах.
#
# ### Заголовки столбцов - это значения, а не имена переменных
#
# **Набор данных Pew Research Center**
#
# Этот набор данных исследует взаимосвязь между доходом и религией.
#
# Проблема: заголовки столбцов состоят из возможных значений дохода.

# +
# import datetime

# from os import listdir
# from os.path import isfile, join
import glob
import re

import pandas as pd

# +
# pylint: disable=line-too-long

df = pd.read_csv(
    "https://github.com/dm-fedorov/pandas_basic/blob/master/data/tidy_data/pew-raw.csv?raw=True"
)
df.head()
# -

# Аккуратная версия этого набора данных - та, в которой значения дохода будут не заголовками столбцов, а значениями в столбце дохода. Чтобы привести в порядок этот набор данных, нам нужно его растопить (*melt*).
#
# В библиотеке *pandas* есть встроенная функция [`melt`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html), которая позволяет это сделать.
#
# Она "переворачивает" (*unpivots*) фрейм данных (*DataFrame*) из широкого формата (*wide format*) в длинный (*long format*).

# +
formatted_df = pd.melt(df, ["religion"], var_name="income", value_name="freq")
formatted_df = formatted_df.sort_values(by=["religion"])

# выводим аккуратную версию набора данных:
formatted_df.head()
# -

# **Набор данных Billboard Top 100**
#
# Этот набор данных представляет собой еженедельный рейтинг песен с момента их попадания в [*Billboard Top 100*](https://ru.wikipedia.org/wiki/Billboard_Hot_100) до последующих 75 недель.
#
# Проблемы:
#
# - Заголовки столбцов состоят из значений: номер недели (`x1st.week`,…)
# - Если песня находится в Топ-100 менее 75 недель, оставшиеся столбцы заполняются пропущенными значениями.

# +
# pylint: disable=line-too-long


df = pd.read_csv(
    "https://github.com/dm-fedorov/pandas_basic/blob/master/data/tidy_data/billboard.csv?raw=True",
    encoding="mac_latin2",
)
df.head()
# -

df.columns

# Для приведения этих данных к аккуратным мы снова растопим (*melt*) столбцы недель в один столбец `date`.
#
# Создадим одну строку в неделю для каждой записи. Если данных за данную неделю нет, то строку создавать не будем.

# +
# Melting
id_vars = [
    "year",
    "artist.inverted",
    "track",
    "time",
    "genre",
    "date.entered",
    "date.peaked",
]

df = pd.melt(frame=df, id_vars=id_vars, var_name="week", value_name="rank_")
df.head()
# -

df["week"]

# Форматирование
df["week"] = df["week"].str.extract(r"(\d+)", expand=False).astype(int)

# Удаление ненужных строк
df = df.dropna()

# +
# Создаем столбцы "date"

# df["date"] = (
#     pd.to_datetime(df["date.entered"])
#     + pd.to_timedelta(df["week"], unit="w")
#     - pd.DateOffset(weeks=1)
# )
# -

df = df[["year", "artist.inverted", "track", "time", "genre", "week", "rank_", "date"]]
df = df.sort_values(
    ascending=True, by=["year", "artist.inverted", "track", "week", "rank_"]
)

df["rank"] = df["rank_"].astype(int)

df = df.drop(["rank_"], axis=1)

# Назначение аккуратного набора данных переменной billboard для использования в будущем
billboard = df

df.head()

# По-прежнему часто повторяются детали песни: `track`, `time` и `genre`.
#
# По этой причине набор данных все еще не совсем аккуратный в соответствии с определением Уикхема. Мы рассмотрим его снова в следующем примере.

# ### Несколько типов в одной таблице
#
# Следуя за набором данных *Billboard*, рассмотрим проблему повторения из предыдущей таблицы.
#
# Проблемы:
#
# - Несколько единиц наблюдения (`track` и ее `rank`) в одной таблице.
#
# Сначала создадим таблицу песен, которая будет содержать сведения о каждой песне:

songs_cols = ["year", "artist.inverted", "track", "time", "genre"]
songs = billboard[songs_cols].drop_duplicates()
songs = songs.reset_index(drop=True)
songs["song_id"] = songs.index

songs.head()

# Затем создадим таблицу `ranks`, которая будет содержать только `song_id`, `date` и `rank`.

ranks = pd.merge(
    billboard, songs, on=["year", "artist.inverted", "track", "time", "genre"]
)
ranks = ranks[["song_id", "date", "rank"]]
ranks.head()

# ### Несколько переменных хранятся в одном столбце
#
# **Записи по туберкулёзу от Всемирной организации здравоохранения**
#
# Этот набор данных документирует количество подтвержденных случаев туберкулеза по странам, годам, возрасту и полу.
#
# Проблемы:
#
# - Некоторые столбцы содержат несколько значений: пол (`m` или `f`) и возраст (`0–14`, `15–24`, `25–34`, `45–54`, `55–64`, `65`, `unknown`).
# - Смесь нулей и пропущенных значений `NaN`. Это связано с процессом сбора данных, и для этого набора данных важно различие.

# +
# pylint: disable=line-too-long

df = pd.read_csv(
    "https://github.com/dm-fedorov/pandas_basic/blob/master/data/tidy_data/tb-raw.csv?raw=True"
)
df.head()
# -

# Чтобы привести в порядок этот набор данных, нужно удалить значения из заголовка и преобразовать их в строки.
#
# Сначала нужно расплавить (*melt*) столбцы, содержащие пол и возраст. Как только у нас будет единственный столбец, мы получим из него три столбца: `sex`, `age_lower` и `age_upper`.
#
# Затем с их помощью сможем правильно построить аккуратный набор данных.

# +
df = pd.melt(
    df, id_vars=["country", "year"], value_name="cases", var_name="sex_and_age"
)

# Извлечь пол, нижнюю границу возраста и группу верхней границы возраста
tmp_df = df["sex_and_age"].str.extract(r"(\D)(\d+)(\d{2})", expand=False)

# Столбцы имени
tmp_df.columns = ["sex", "age_lower", "age_upper"]

# Создайте столбец age на основе age_lower и age_upper
tmp_df["age"] = tmp_df["age_lower"] + "-" + tmp_df["age_upper"]

# Merge
df = pd.concat([df, tmp_df], axis=1)

# Удалите ненужные столбцы и строки
df = df.drop(["sex_and_age", "age_lower", "age_upper"], axis=1)
df = df.dropna()
df = df.sort_values(ascending=True, by=["country", "year", "sex", "age"])

# В результате получается аккуратный набор данных
df.head()
# -

# ### Переменные хранятся как в строках, так и в столбцах
# **Набор сетевых данных по глобальной исторической климатологии (Global Historical Climatology Network Dataset)**
#
# Этот набор данных представляет собой ежедневные записи погоды для метеостанции (*MX17004*) в Мексике за пять месяцев в 2010 году.
#
# Проблемы:
#
# - Переменные хранятся как в строках (`tmin`, `tmax`), так и в столбцах (`days`).

# +
# pylint: disable=line-too-long

df = pd.read_csv(
    "https://github.com/dm-fedorov/pandas_basic/blob/master/data/tidy_data/weather-raw.csv?raw=True"
)
df.head()
# -

df = pd.melt(df, id_vars=["id", "year", "month", "element"], var_name="day_raw")
df.head()

# Чтобы упорядочить этот набор данных, мы хотим переместить три неуместных переменных (`tmin`, `tmax` и `days`) в виде трех отдельных столбцов: `tmin`, `tmax` и `date`.

# Извлекаем день
df["day"] = df["day_raw"].str.extract(r"d(\d+)", expand=False)
df["id"] = "MX17004"

# К числовым значениям
df[["year", "month", "day"]] = df[["year", "month", "day"]].apply(
    lambda x: pd.to_numeric(x, errors="ignore")  # type: ignore[call-overload]
)

# +
# Создание даты из разных столбцов


# def create_date_from_year_month_day(row: pd.Series) -> datetime.datetime:
#     """Создать объект даты из столбцов 'year', 'month' и 'day'.

#     Принимает строку DataFrame (pandas.Series) с полями 'year', 'month' и 'day',
#     создаёт и возвращает объект datetime.datetime.
#     """
#     return datetime.datetime(year=row["year"], month=int(row["month"]), day=row["day"])

# +
# df["date"] = df.apply(lambda row: create_date_from_year_month_day(row), axis=1)
# -

df = df.drop(["year", "month", "day", "day_raw"], axis=1)
df = df.dropna()

# Unmelting столбец "element"
df = df.pivot_table(index=["id", "date"], columns="element", values="value")
df.reset_index(drop=False, inplace=True)

df.head()


# ### Один тип в нескольких таблицах
# **Набор данных: имена мальчиков в штате Иллинойс за 2014/15 годы**
#
# Проблемы:
#
# - Данные распределены по нескольким таблицам/файлам.
# - В имени файла присутствует переменная `year`.
#
# Чтобы загрузить разные файлы в один `DataFrame`, мы можем запустить собственный скрипт, который будет добавлять файлы вместе. Кроме того, нам нужно будет извлечь переменную `year` из имени файла.

# > Следующий пример подразумевает наличие двух файлов в корневой директории: `2015-baby-names-illinois.csv` и `2014-baby-names-illinois.csv`

# !curl -L -o 2015-baby-names-illinois.csv https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/tidy_data/2015-baby-names-illinois.csv

# !curl -L -o 2014-baby-names-illinois.csv https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/tidy_data/2015-baby-names-illinois.csv

def extract_year(string: str) -> int | None:
    """Извлечь год из строки.

    Функция ищет первую последовательность из четырёх цифр (например, 2024)
    и возвращает значение года как целое число. Если год не найден, возвращает None.
    """
    match = re.match(r".*(\d{4})", string)
    if match is not None:
        return int(match.group(1)) - 1
    return None


# +
path = "."  # текущая директория

all_files = glob.glob(path + "/201*-baby-names-illinois.csv")

frame = pd.DataFrame()
df_list = []

for file_ in all_files:
    df = pd.read_csv(file_, index_col=None, header=0)
    df.columns = map(str.lower, df.columns)  # type: ignore
    df["year"] = extract_year(file_)
    df_list.append(df)
# -

df = pd.concat(df_list)
df.head()

# ## Заключительные мысли
#
# В этой заметке я сосредоточился только на одном аспекте статьи Уикхема, а именно на части манипулирования данными. Моей главной целью было продемонстрировать манипуляции с данными в Python. Важно отметить, что в [статье Уикхема](http://vita.had.co.nz/papers/tidy-data.pdf) есть значительный раздел, посвященный инструментам и визуализациям, с помощью которых вы можете извлечь пользу, приведя в порядок свой набор данных.
