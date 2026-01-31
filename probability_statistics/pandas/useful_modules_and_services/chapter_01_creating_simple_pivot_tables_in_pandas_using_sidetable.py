"""Creating simple pivot tables in pandas using sidetable."""

# # Создание простых сводных таблиц в pandas с помощью sidetable

# Крис Моффитт, редактор [сайта](https://pbpython.com/sidetable.html) об автоматизации бизнес-задач на Python, разработал модуль [sidetable](https://github.com/chris1610/sidetable).
#
# Со слов автора новый модуль расширяет возможности [`value_counts()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) и использует [`API pandas`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html) для регистрации собственных методов.
#
# Давайте разбираться, как он работает.
#
# Для начала установим модуль:

# +
# pip install sidetable
# -

# Рассмотрим пример с [грантами для школ США](https://catalog.data.gov/dataset/school-improvement-2010-grants), если кратко: Конгресс еще при Обаме выделил 4 миллиарда у.е. для реформы образования, для получения гранта школе надо выбрать одну из моделей реформирования (`Model Selected`).

# Начинаем, как обычно, с импорта модулей:

# +
import pandas as pd

# import sidetable

# +
# pylint: disable=line-too-long

df = pd.read_csv(
    "https://github.com/chris1610/pbpython/blob/master/data/school_transform.csv?raw=True",
    index_col=0,
)
df.head()
# -

# В результате импорта модуля `sidetable` у `DataFrame` появился новый метод `stb`.
#
# Вызов `stb.freq()` позволяет построить сводную таблицу частот по штатам:

df.stb.freq(["State"]).head()

# Этот пример показывает, что `CA` (California) встречается 92 раза и составляет `12,15%` от общего количества школ. Если включить в подсчеты `FL` (Florida), то будет 163 школы, что составляет `21,5%` от общего числа школ, участвующих в грантах.
#
# Можно сравнить этот результат с выводом стандартного метода [`value_counts()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html).
#
# При установке `normalize` в `True` возвращаемый объект будет содержать относительные частоты уникальных значений:

print(df["State"].value_counts(normalize=True)[:10])

# Хм... разница заметна, даже невооруженным глазом.
#
# Можно составить список штатов, которые составляют около `50%` от общего числа с помощью аргумента `thresh` (рус. «молотить») и сгруппировать все остальные штаты в категорию `Others`:

df.stb.freq(["State"], thresh=50)

# Теперь видим, что 8 штатов составляют практически `50%` от общего количества.
#
# Можем для симпатичности переименовать категорию `Others`, используя ключевой аргумент `other_label`:

df.stb.freq(["State"], thresh=50, other_label="Остальные штаты")

# `sidetable` позволяет группировать столбцы для лучшего понимания распределения.
#
# Посмотрим, как различные *Модели трансформации* (`Model Selected`) применяются в разных регионах?

df.stb.freq(["Region", "Model Selected"])

# `sidetable` позволяет передавать значение `value`, по которому можно суммировать (вместо подсчета вхождений).

df.stb.freq(["Region"], value="Award_Amount")

# Узнали, что `Northeast` (Северо-Восток) затратил наименьшее количество средств на реформу, а `37%` от общих расходов было потрачено на школы в `South` (Южном) регионе.
#
# Посмотрим на типы выбранных моделей и определим разбиение `80/20` для выделенных средств:

df.stb.freq(
    ["Region", "Model Selected"],
    value="Award_Amount",
    thresh=82,
    other_label="Remaining",
)

# Можем сравнить с кросс-таблицей [`crosstab`](https://pbpython.com/pandas-crosstab.html) в pandas:

pd.crosstab(
    df["Region"], df["Model Selected"], values=df["Award_Amount"], aggfunc="sum"
)

# Сравните с:

df.stb.freq(["Region", "Model Selected"], value="Award_Amount")

# Можно улучшить [читабельность данных](https://pbpython.com/styling-pandas.html) в pandas за счет добавления форматирования столбцов `Percentage` и `Amount`.
#
# Укажем для этого ключевой аргумент `style=True`:

df.stb.freq(["Region"], value="Award_Amount", style=True)

# Пример построения таблицы пропущенных значений:

df.stb.missing()

# Видим 10 пропущенных значений в столбце `Region`, что составляет чуть менее `1,3%` от общего значения в этом столбце.
#
# Похожий результат можно получить с помощью [`info()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html):

df.info()

# [Ссылка](https://github.com/chris1610/sidetable/blob/master/README.md) на остальную документацию для модуля `sidetable`.
#
# Для визуализации пропущенных значений см. модуль [`missingno`](https://github.com/ResidentMario/missingno).
