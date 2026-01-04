"""Pivot table in pandas."""

# # Сводная таблица в pandas

# *Сводная таблица* - это мощный инструмент для обобщения и представления данных. 
#
# В Pandas есть функция [`DataFrame.pivot_table()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot_table.html), которая позволяет быстро преобразовать [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) в сводную таблицу.

# Обобщенная схема работы функции `pivot_table`:

# <img src="https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/pivot_table_pandas.png" >

# Эта функция очень полезна, но иногда бывает сложно запомнить, как ее использовать для форматирования данных нужным вам способом.
#
# В этом Блокноте рассказывается, как использовать `pivot_table`.
#
# Полный текст оригинальной статьи находится [здесь](http://pbpython.com/pandas-pivot-table-explained.html).

# В этом сценарии я собираюсь отслеживать воронку (план) продаж (также называемую воронкой, funnel). Основная проблема заключается в том, что некоторые циклы продаж очень длинные (например, "корпоративное программное обеспечение", капитальное оборудование и т.д.), и руководство хочет отслеживать их детально в течение года.
#
# Типичные вопросы, относящиеся к таким данным, включают:
#
# Какой доход находится в воронке (плане продаж)?
# Какие продукты находятся в воронке?
# У кого какие продукты на каком этапе?
# Насколько вероятно, что мы закроем сделки к концу года?

import numpy as np
import pandas as pd

# Прочтите данные о нашей воронке продаж в `DataFrame`:

# +
# pylint: disable=line-too-long

df = pd.read_excel(
    "https://github.com/dm-fedorov/pandas_basic/raw/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/salesfunnel.xlsx"
)
df.head()
# Счет, Название компании, Представитель компании, Менеджер по продажам, Продукт, Кол-во, Стоимость, Статус сделки
# -

# Для удобства давайте представим столбец `Status` как [категориальную переменную](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html) (`category`) и установим порядок, в котором хотим просматривать.
#
# Это не является строго обязательным, но помогает поддерживать желаемый порядок при работе с данными.

df["Status"] = df["Status"].astype("category")
df["Status"] = df["Status"].cat.set_categories(
    ["Ordered", "Shipped", "Delivered", "Returned"]
)

df.info()

# # Поворот данных

# Создавать сводную таблицу (`pivot table`) проще всего последовательно. Добавляйте элементы по одному и проверяйте каждый шаг, чтобы убедиться, что вы получаете ожидаемые результаты.
#
# Самая простая сводная таблица должна иметь `DataFrame` и индекс (`index`). В этом примере давайте использовать `Name` в качестве индекса:

numeric_cols = df.select_dtypes(include=["number"]).columns
pd.pivot_table(df, index=["Name"], values=numeric_cols)   # type: ignore[call-overload]

# У вас может быть несколько индексов. Фактически, большинство аргументов pivot_table могут принимать несколько значений в качестве элементов списка:

pd.pivot_table(
    df,
    index=["Name", "Rep", "Manager"],
    values=df.select_dtypes(include="number").columns.tolist(),
)

# Это интересно, но не особо полезно. 
#
# Мы хотим посмотреть на эти данные со стороны менеджера (`Manager`) и директора (`Director`). Это достаточно просто сделать, изменив индекс:

pd.pivot_table(
    df,
    index=["Manager", "Rep"],
    values=df.select_dtypes(include="number").columns.tolist(),
)

# Вы могли заметить, что сводная таблица достаточно умна, чтобы начать агрегирование данных и их обобщение, группируя представителей (`Rep`) с их менеджерами (`Manager`). Теперь мы начинаем понимать, что может сделать для нас сводная таблица.
#
# Давайте удалим счет (`Account`) и количество (`Quantity`), явно определив столбцы, которые нам нужны, с помощью параметра `values`:

pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"])

# Столбец цен (`price`) по умолчанию усредняет данные, но мы можем произвести подсчет количества или суммы. Добавить их можно с помощью параметра `aggfunc`:

pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=np.sum)

# `aggfunc` может принимать список функций. 
#
# Давайте попробуем узнать среднее значение и количество:

pd.pivot_table(df, index=["Manager", "Rep"], values=["Price"], aggfunc=[np.mean, len])

# Если мы хотим увидеть продажи с разбивкой по продуктам (`Product`), переменная `columns` позволяет нам определить один или несколько столбцов.

# Я думаю, что одна из сложностей `pivot_table` - это использование столбцов (`columns`) и значений (`values`). 
#
# Помните, что столбцы необязательны - они предоставляют дополнительный способ сегментировать актуальные значения, которые вам нужны. 
#
# Функции агрегирования применяются к перечисленным значениям (`values`):

pd.pivot_table(
    df,
    index=["Manager", "Rep"],
    values=["Price"],
    columns=["Product"],
    aggfunc=[np.sum],
)

# Значения `NaN` немного отвлекают. Если мы хотим их убрать, то можем использовать параметр `fill_value`, чтобы установить в `0`.

pd.pivot_table(
    df,
    index=["Manager", "Rep"],
    values=["Price"],
    columns=["Product"],
    aggfunc=[np.sum],
    fill_value=0,
)

# Думаю, было бы полезно добавить количество (`Quantity`). 
#
# Добавьте количество (`Quantity`) в список значений `values`:

pd.pivot_table(
    df,
    index=["Manager", "Rep"],
    values=["Price", "Quantity"],
    columns=["Product"],
    aggfunc=[np.sum],
    fill_value=0,
)

# Что интересно, вы можете добавлять элементы в индекс, чтобы получить другое визуальное представление. 
#
# Добавим товары (`Products`) в индекс.

pd.pivot_table(
    df,
    index=["Manager", "Rep", "Product"],
    values=["Price", "Quantity"],
    aggfunc=[np.sum],
    fill_value=0,
)

# Для этого набора данных такое представление имеет больше смысла. 
#
# А что, если я хочу увидеть некоторые итоги? `margins=True` делает это за нас.

pd.pivot_table(
    df,
    index=["Manager", "Rep", "Product"],
    values=["Price", "Quantity"],
    aggfunc=[np.sum, np.mean],
    fill_value=0,
    margins=True,
)

# Давайте переместим анализ на уровень выше и посмотрим на наш план продаж (воронку) на уровне менеджера.
#
# Обратите внимание на то, как статус упорядочен на основе нашего предыдущего определения категории.

pd.pivot_table(
    df,
    index=["Manager", "Status"],
    values=["Price"],
    aggfunc=[np.sum],
    fill_value=0,
    margins=True,
)

# Очень удобно передать словарь в качестве `aggfunc`, чтобы вы могли выполнять разные функции с каждым из выбранных значений. Это имеет побочный эффект - названия становятся немного чище:

pd.pivot_table(
    df,
    index=["Manager", "Status"],
    columns=["Product"],
    values=["Quantity", "Price"],
    aggfunc={"Quantity": len, "Price": np.sum},
    fill_value=0,
)

# Вы также можете предоставить список агрегированных функций (aggfunctions), которые будут применяться к каждому значению:

table = pd.pivot_table(
    df,
    index=["Manager", "Status"],
    columns=["Product"],
    values=["Quantity", "Price"],
    aggfunc={"Quantity": len, "Price": [np.sum, np.mean]},  # type: ignore
    fill_value=0,
)

# table

# Может показаться сложным собрать все это сразу, но как только вы начнете играть с данными и медленно добавлять элементы, то почувствуете, как это работает.
#
# Мое общее практическое правило заключается в том, что после использования нескольких группировок (`grouby`) вы должны оценить, является ли сводная таблица (`pivot table`) полезным подходом.

# # Расширенная фильтрация сводной таблицы

# После того, как вы сгенерировали свои данные, они находятся в `DataFrame`, поэтому можно фильтровать их, используя обычные методы `DataFrame`.

# Если вы хотите посмотреть только на одного менеджера:

# +
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html

table.query('Manager == ["Debra Henley"]')
# -

# Мы можем просмотреть все незавершенные (`pending`) и выигранные (`won`) сделки:

table.query('Status == ["pending", "won"]')

# Я надеюсь, что этот пример показал вам, как использовать сводные таблицы в собственных наборах данных.

# # Шпаргалка

# Схема с примером из Блокнота:

# <img src="https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/pivot-table-datasheet.png" >
