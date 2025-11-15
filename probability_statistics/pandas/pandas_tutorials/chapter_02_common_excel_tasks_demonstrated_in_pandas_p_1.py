"""Common Excel tasks, demonstrated in pandas (part 1)."""

# # Типичные задачи Excel, продемонстрированные в pandas (часть 1)

# ## Введение
#
# Цель этой статьи - показать ряд повседневных задач `Excel` и то, как они выполняются в `pandas`. Некоторые примеры тривиальны, но я думаю, важно представить как простые, так и более сложные функции. 
#
# В качестве дополнительного бонуса я собираюсь выполнить нечеткое сопоставление строк (`fuzzy string matching`), чтобы продемонстрировать, как `pandas` могут использовать модули `Python`. 
#
# > оригинал статьи Криса [тут](https://pbpython.com/excel-pandas-comp.html)
#
# Разберемся? Давайте начнем.

# ## Добавление суммы в строку 
#
# Первая задача, которую я покажу, - это суммирование нескольких столбцов для добавления итогового столбца.
#
# Начнем с импорта данных из `Excel` в кадр данных `pandas`:

# !pip install fuzzywuzzy

# +
# pylint: disable=line-too-long

from typing import Union

import numpy as np
import pandas as pd
from fuzzywuzzy import process

df = pd.read_excel(
    "https://github.com/dm-fedorov/pandas_basic/blob/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/excel-comp-data.xlsx?raw=True"
)
df.head()
# -

# Мы хотим добавить столбец с итогами, чтобы показать общие продажи за январь, февраль и март. Это просто сделать в `Excel` и в `pandas`. 
#
# Для `Excel` я добавил формулу `SUM(G2:I2)` в столбец `J`. 
#
# Вот как это выглядит:

# ![](https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/excel-1.png)      

# Далее, вот как это делается в `pandas`:

df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
df.head()

# Затем получим итоговые и некоторые другие значения за каждый месяц. 
#
# Пытаемся сделать в `Excel`:

![](https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/excel-2.png)

# Как видите, мы добавили `SUM(G2:G16)` в строку `17` в каждом столбце, чтобы получить итоги по месяцам. 
#
# В `pandas` легко выполнять анализ на уровне столбцов. Вот пара примеров:

print(df["Jan"].sum())
print(df["Jan"].mean())
print(df["Jan"].min())
print(df["Jan"].max())

# Теперь хотим в `pandas` сложить сумму по месяцам с итогом (`total`). 
#
# Здесь `pandas` и `Excel` немного расходятся. В `Excel` очень просто складывать итоги в ячейках за каждый месяц. 
#
# Поскольку `pandas` необходимо поддерживать целостность всего [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html), то придется добавить еще пару шагов.
#
# Сначала создайте сумму для столбцов по месяцам и итога (`total`).

sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()
sum_row

# Интуитивно понятно, если вы хотите добавить итоги в виде строки, то нужно проделать некоторые незначительные манипуляции.
#
# Для начала - транспонировать данные и преобразовать [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) в [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html), чтобы было проще объединить существующие данные. 
#
# Атрибут [`T`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.T.html) позволяет преобразовать данные из строк в столбцы.

df_sum = pd.DataFrame(data=sum_row).T
df_sum

# Последнее, что нужно сделать перед суммированием итогов, - это добавить недостающие столбцы. 
#
# Для этого используем функцию [`reindex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex.html). 
#
# Хитрость заключается в том, чтобы добавить все наши столбцы, а затем разрешить `pandas` заполнить отсутствующие значения.

df_sum = df_sum.reindex(columns=df.columns)
df_sum

# Теперь, когда у нас есть красиво отформатированный `DataFrame`, можем добавить его к существующему, используя метод [`append`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html):

df_final = pd.concat([df, df_sum], ignore_index=True)
df_final.tail(3)

# ## Дополнительные преобразования данных
#
# В качестве примера попробуем добавить к набору данных аббревиатуру штата.
#
# С точки зрения `Excel`, самый простой способ - это добавить новый столбец, выполнить `vlookup` ([ВПР](https://support.microsoft.com/ru-ru/office/%D0%B2%D0%BF%D1%80-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F-%D0%B2%D0%BF%D1%80-0bbc8083-26fe-4963-8ab8-93a18ad188a1)) по имени штата и заполнить аббревиатуру.
#
# Вот снимок того, как выглядят результаты:

# ![](https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/excel-3.png)

# Вы заметите, что после выполнения `vlookup` ряд значений отображаются неправильно. Это потому, что мы неправильно написали некоторые штаты. Обработать это в `Excel` для больших наборов данных сложно.
#
# В `pandas` у нас есть вся мощь экосистемы `Python`. Размышляя о том, как решить эту проблему с грязными данными, я подумал о попытке сопоставления нечеткого текста (`fuzzy text matching`), чтобы определить правильное значение.

# К счастью, кто-то проделал большую работу в этом направлении. 
#
# В библиотеке [`fuzzy wuzzy`](https://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/) есть несколько довольно полезных функций для таких ситуаций.
#
# > fuzzywuzzy использует [расстояние Левенштейна](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5_%D0%9B%D0%B5%D0%B2%D0%B5%D0%BD%D1%88%D1%82%D0%B5%D0%B9%D0%BD%D0%B0) для вычисления различий между последовательностями.
#
# > см. [Применение библиотеки FuzzyWuzzy для нечёткого сравнения в Python](https://habr.com/ru/post/491448/) на Хабре

# +
# pip3 install fuzzywuzzy(!)

# +
# pip install python-Levenshtein(!)
# -

# Начнем с импорта соответствующих нечетких функций:

# Другой фрагмент кода, который нам нужен, - это отображение имени штата в аббревиатуру. Вместо того, чтобы пытаться напечатать его самостоятельно, небольшой поиск в Google подсказал следующий код:

state_to_code = {
    "VERMONT": "VT",
    "GEORGIA": "GA",
    "IOWA": "IA",
    "Armed Forces Pacific": "AP",
    "GUAM": "GU",
    "KANSAS": "KS",
    "FLORIDA": "FL",
    "AMERICAN SAMOA": "AS",
    "NORTH CAROLINA": "NC",
    "HAWAII": "HI",
    "NEW YORK": "NY",
    "CALIFORNIA": "CA",
    "ALABAMA": "AL",
    "IDAHO": "ID",
    "FEDERATED STATES OF MICRONESIA": "FM",
    "Armed Forces Americas": "AA",
    "DELAWARE": "DE",
    "ALASKA": "AK",
    "ILLINOIS": "IL",
    "Armed Forces Africa": "AE",
    "SOUTH DAKOTA": "SD",
    "CONNECTICUT": "CT",
    "MONTANA": "MT",
    "MASSACHUSETTS": "MA",
    "PUERTO RICO": "PR",
    "Armed Forces Canada": "AE",
    "NEW HAMPSHIRE": "NH",
    "MARYLAND": "MD",
    "NEW MEXICO": "NM",
    "MISSISSIPPI": "MS",
    "TENNESSEE": "TN",
    "PALAU": "PW",
    "COLORADO": "CO",
    "Armed Forces Middle East": "AE",
    "NEW JERSEY": "NJ",
    "UTAH": "UT",
    "MICHIGAN": "MI",
    "WEST VIRGINIA": "WV",
    "WASHINGTON": "WA",
    "MINNESOTA": "MN",
    "OREGON": "OR",
    "VIRGINIA": "VA",
    "VIRGIN ISLANDS": "VI",
    "MARSHALL ISLANDS": "MH",
    "WYOMING": "WY",
    "OHIO": "OH",
    "SOUTH CAROLINA": "SC",
    "INDIANA": "IN",
    "NEVADA": "NV",
    "LOUISIANA": "LA",
    "NORTHERN MARIANA ISLANDS": "MP",
    "NEBRASKA": "NE",
    "ARIZONA": "AZ",
    "WISCONSIN": "WI",
    "NORTH DAKOTA": "ND",
    "Armed Forces Europe": "AE",
    "PENNSYLVANIA": "PA",
    "OKLAHOMA": "OK",
    "KENTUCKY": "KY",
    "RHODE ISLAND": "RI",
    "DISTRICT OF COLUMBIA": "DC",
    "ARKANSAS": "AR",
    "MISSOURI": "MO",
    "TEXAS": "TX",
    "MAINE": "ME",
}

# Вот несколько примеров того, как работает функция сопоставления нечеткого текста:

# +
process.extractOne("Minnesotta", choices=state_to_code.keys())

# ('результат', индекс сходства)
# -

process.extractOne("AlaBAMMazzz", choices=state_to_code.keys(), score_cutoff=80)

# Теперь, когда мы знаем, как это работает, создаем функцию, которая берет столбец штата и преобразует его в допустимое сокращение. 
#
# Для этих данных используем *порог наилучшего результата совпадения* `score_cutoff=80`. Можете поиграть с этим значением, чтобы увидеть, какое число подходит для ваших данных. 
#
# В функции мы либо возвращаем допустимое сокращение, либо `np.nan`, чтобы у нас были допустимые значения в поле.

# +
# def convert_state(row: pd.Series) -> Union[str, float]:  # type: ignore
#     """Convert a state name to its abbreviation using fuzzy matching."""
#     state_value = row["state"]

#     if pd.isna(state_value):
#         return np.nan

#     abbrev = process.extractOne(
#         str(state_value), choices=list(state_to_code.keys()), score_cutoff=80
#     )

#     if abbrev:
#         return state_to_code[abbrev[0]]

#     return np.nan


# dummy version
def convert_state(row: pd.Series) -> Union[str, float]:  # type: ignore
    """Convert a state name to its abbreviation using fuzzy matching."""
    return row  # type: ignore


# -

# Добавьте столбец в нужном месте и заполните его значениями `NaN`:

df_final.insert(6, "abbrev", np.nan)
df_final.head()

# Теперь используем [`apply`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) для добавления сокращений в столбец `abbrev`:

# df_final["abbrev"] = df_final.apply(convert_state, axis=1)
df_final["abbrev"] = df_final["state"].map(state_to_code)
df_final.tail()

# Думаю, это круто!
#
# Мы разработали очень простой процесс для очистки данных. Очевидно, когда у вас 15 строк, это не имеет большого значения. Однако что, если бы у вас было 15 000?

# ## Промежуточные итоги
#
# В последнем разделе этой статьи давайте рассмотрим промежуточные итоги (`subtotal`) по штатам.
#
# В `Excel` мы бы использовали инструмент `subtotal`:

# ![](https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/excel-4.png)

# Результат будет выглядеть так:

# ![](https://pbpython.com/images/excel-5.png)

# Создание промежуточного итога в `pandas` выполняется с помощью метода [`groupby`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html):

df_sub: pd.DataFrame = (
    df_final[["abbrev", "Jan", "Feb", "Mar", "total"]].groupby("abbrev").sum()
)
df_sub


# Затем хотим отобразить данные с обозначением валюты, используя [`applymap`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.applymap.html) для всех значений в кадре данных:

# +
def money(x_var: Union[int, float]) -> str:
    """Format a numeric value as US currency."""
    return f"${x_var:,.0f}"


# formatted_df = df_sub.applymap(money)
formatted_df = df_sub.map(money)
formatted_df
# -

# Форматирование выглядит неплохо, теперь можем получить итоговые значения, как раньше:

sum_row = df_sub[["Jan", "Feb", "Mar", "total"]].sum()
sum_row

# Преобразуйте значения в столбцы и отформатируйте их:

df_sub_sum: pd.DataFrame = pd.DataFrame(data=sum_row).T
# df_sub_sum = df_sub_sum.applymap(money)
df_sub_sum = df_sub_sum.map(money)
df_sub_sum

# Наконец, добавьте итоговое значение в `DataFrame`:

# final_table = formatted_df.append(df_sub_sum)
final_table = pd.concat([formatted_df, df_sub_sum], ignore_index=True)
final_table

# Вы заметите, что для итоговой строки индекс равен `0`. 
#
# Можем изменить это с помощью метода [`rename`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html):

final_table = final_table.rename(index={0: "Total"})
final_table

# > Модуль [`sidetable`](https://dfedorov.spb.ru/pandas/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D1%85%20%D1%81%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D1%85%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%20%D0%B2%20pandas%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20sidetable.html) значительно упрощает этот процесс и делает его более надежным.

# ## Заключение
#
# К настоящему времени большинство людей знают, что `pandas` умеет выполнять множество сложных манипуляций с данными подобно `Excel`. Изучая `pandas`, я все еще пытаюсь вспомнить, как это сделать в `Excel`. Понимаю, что это сравнение может быть не совсем справедливым - это разные инструменты. Однако я надеюсь достучаться до людей, которые знают `Excel` и хотят узнать, какие существуют альтернативы для их потребностей в обработке данных. Надеюсь, эти примеры помогут почувствовать уверенность в том, что можно заменить множество бесполезных манипуляций с данными в `Excel` с помощью pandas.

# > В качестве бонуса рекомендую видео [Excel is Evil - Why it has no place in research](https://youtu.be/-NuTlczV72Q)
