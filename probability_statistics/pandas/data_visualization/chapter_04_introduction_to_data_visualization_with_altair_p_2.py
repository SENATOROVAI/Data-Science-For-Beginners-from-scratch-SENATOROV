"""Introduction to data visualization with Altair (part 2)."""

# # Введение в визуализацию данных с помощью Altair (часть 2)

# ## Биннинг и агрегация
#
# В [первой части уроков](https://dfedorov.spb.ru/pandas/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Altair.html) мы обсудили **данные**, **метки**, **кодировки** и **типы кодирования**. Следующая важная часть *API Altair* - это подход к группированию и агрегированию данных.

import altair as alt
from vega_datasets import data

# +
# загрузили набор данных про машины
cars = data.cars()

cars.head()
# -

# ## Group-By в Pandas
#
# Одной из ключевых операций в исследовании данных является группировка (*group-by*), подробно описанная в [статье](https://dfedorov.spb.ru/pandas/%D0%9F%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE%D0%B5%20%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE%20%D0%BF%D0%BE%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5%20%D0%B8%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20pandas.html). Короче говоря, группировка разбивает данные в соответствии с некоторым условием, применяет некоторую агрегацию в этих группах, а затем объединяет данные обратно вместе:
#
# ![Split Apply Combine figure](https://jakevdp.github.io/PythonDataScienceHandbook/figures/03.08-split-apply-combine.png)
# [Источник картинки](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html)

# Что касается данных об автомобилях, вы можете разделить их по происхождению (`Origin`), вычислить среднее значение миль на галлон (*miles per gallon*), а затем объединить результаты.
#
# В *Pandas* операция выглядит так:

cars.groupby("Origin")["Miles_per_Gallon"].mean()

# В *Altair* такой вид "разделения-применения-комбинирования" (*split-apply-combine*) может быть выполнен путем передачи оператора агрегирования внутри строки в любую кодировку (*encoding*).
#
# Например, мы можем отобразить график, представляющий вышеуказанную агрегацию, следующим образом:

alt.Chart(cars).mark_bar().encode(y="Origin", x="mean(Miles_per_Gallon)")

# Обратите внимание, что группировка выполняется неявно внутри кодировок: здесь мы группируем только по происхождению (`Origin`), а затем вычисляем среднее значение по каждой группе.
#
# ## Одномерные биннинги: гистограммы
#
# Одно из наиболее распространенных применений биннинга - создание *гистограмм*. Например, вот гистограмма миль на галлон (*miles per gallon*):

alt.Chart(cars).mark_bar().encode(
    alt.X("Miles_per_Gallon", bin=True), alt.Y("count()"), alt.Color("Origin")
)

# Интересно то, что *декларативный подход Altair* позволяет присваивать эти значения разным кодировкам, чтобы увидеть другие представления тех же данных.
#
# Например, если мы присвоим цвету (`color`) количество миль на галлон (*miles per gallon*), то получим следующее представление данных:

alt.Chart(cars).mark_bar().encode(
    color=alt.Color("Miles_per_Gallon", bin=True), x="count()", y="Origin"
)

# Это дает лучшее представление о доле `MPG` (миль на галлон) в каждой стране.
#
# При желании мы можем нормализовать количество по оси `x`, чтобы напрямую сравнивать пропорции:

alt.Chart(cars).mark_bar().encode(
    color=alt.Color("Miles_per_Gallon", bin=True),
    x=alt.X("count()", stack="normalize"),
    y="Origin",
)

# Видим, что более половины автомобилей в США относятся к категории "с низким пробегом" (*low mileage*).
#
# Снова изменив кодировку (*encoding*), давайте сопоставим цвет с количеством `color='count()'`:

alt.Chart(cars).mark_rect().encode(
    x=alt.X("Miles_per_Gallon", bin=alt.Bin(maxbins=20)),
    color="count()",
    y="Origin",
)

# Видим набор данных, похожий на тепловую карту!
#
# Это одна из прекрасных особенностей *Altair*: через грамматику API он показывает отношения между разными типами диаграмм, например, двухмерная тепловая карта кодирует те же данные, что и гистограмма с накоплением (*stacked*)!
#
# ## Прочие агрегаты
#
# Агрегаты (aggregates) также могут использоваться с данными, которые неявно объединены в группы. Например, посмотрите на этот график `MPG` (миль на галлон) с течением времени:

alt.Chart(cars).mark_point().encode(x="Year:T", color="Origin", y="Miles_per_Gallon")

# Тот факт, что точки пересекаются, затрудняет просмотр важных частей данных; мы можем сделать его более ясным, построив среднее значение в каждой группе (здесь *среднее значение каждой комбинации Год/Страна*):

alt.Chart(cars).mark_line().encode(
    x="Year:T", color="Origin", y="mean(Miles_per_Gallon)"
)

# Однако совокупное среднее значение (*mean*) отражает лишь часть истории: *Altair* также предоставляет встроенные инструменты для вычисления нижней и верхней границ доверительных интервалов для среднего.
#
# Мы можем использовать здесь `mark_area()` и указать нижнюю и верхнюю границы области, используя `y` и `y2`:

alt.Chart(cars).mark_area(opacity=0.3).encode(
    x="Year:T", color="Origin", y="ci0(Miles_per_Gallon)", y2="ci1(Miles_per_Gallon)"
)

# ## Временной биннинг
#
# Одним из особых видов биннинга является группировка временных значений по аспектам даты: например, месяц года или день месяца. Чтобы изучить это, давайте посмотрим на простой набор данных, состоящий из средних температур в Сиэтле:

temps = data.seattle_temps()
temps.head()

# Если мы попытаемся построить график по этим данным с помощью *Altair*, то получим ошибку `MaxRowsError`:

# ```Python
# alt.Chart(temps).mark_line().encode(
#     x='date:T',
#     y='temp:Q'
# )
# ```
# ```Python
# ---------------------------------------------------------------------------
# MaxRowsError                              Traceback (most recent call last)
# ```

len(temps)

# ## Как Altair кодирует данные
#
# > Мы решили возбудить исключение `MaxRowsError` для наборов данных размером более `5000` строк из-за наших наблюдений за учащимися, использующими *Altair*, потому что, если вы не задумаетесь о том, как представлены данные, то довольно легко получить **очень** большие Jupyter блокноты, в которых снизится производительность.
#
# Когда вы передаете фрейм данных *pandas* в диаграмму *Altair*, то в результате данные преобразуются в JSON формат и сохраняются в спецификации диаграммы. Затем эта спецификация встраивается в выходные данные Jupyter блокнота, и если вы сделаете таким образом несколько десятков диаграмм с достаточно большим набором данных, то это может значительно замедлить работу вашей машины.

# Так как же обойти эту ошибку? Есть несколько способов:
#
# 1) Используйте меньший набор данных. Например, мы могли бы использовать *Pandas* для суммирования дневных температур:
#
#    ```python
#    import pandas as pd
#
#    temps = temps.groupby(pd.DatetimeIndex(temps.date).date).mean().reset_index()
#    ```

# 2) Отключите `MaxRowsError`, используя   
#
#    ```python
#    alt.data_transformers.enable("default", max_rows=None)
#    ```
#
# Но учтите, что это может привести к **очень** большим Jupyter блокнотам, если вы не будете осторожны.  

# 3) Обслуживайте свои данные с локального поточного сервера. [Пакет сервера данных altair](https://github.com/altair-viz/altair_data_server) упрощает это.
#
#    ```python
#    alt.data_transformers.enable("data_server")
#    ```
#   
# Обратите внимание, что этот подход может не работать с некоторыми облачными сервисами для Jupyter ноутбуков.    

# 4) Используйте URL-адрес, указывающий на источник данных. Создание [*gist*](https://gist.github.com/) - это быстрый и простой способ хранить часто используемые данные.

# +
# pylint: disable=line-too-long


temps = "https://raw.githubusercontent.com/altair-viz/vega_datasets/master/vega_datasets/_data/seattle-temps.csv"
# -

alt.Chart(temps).mark_line().to_dict()

# Обратите внимание, что *вместо включения всего набора данных используется только URL-адрес*.
#
# Теперь давайте попробуем еще раз с нашим графиком:

alt.Chart(temps).mark_line().encode(x="date:T", y="temp:Q")

# Эти данные явно переполнены. Предположим, что мы хотим отсортировать данные по месяцам. Сделаем это с помощью `TimeUnit Transform` на дату:

alt.Chart(temps).mark_point().encode(x=alt.X("month(date):T"), y="temp:Q")

# Станет понятнее, если мы просуммируем температуры:

alt.Chart(temps).mark_bar().encode(x=alt.X("month(date):O"), y="mean(temp):Q")

# Можем разделить даты двумя разными способами, чтобы получить интересное представление данных, например:

alt.Chart(temps).mark_rect().encode(
    x=alt.X("date(date):O"), y=alt.Y("month(date):O"), color="mean(temp):Q"
)

# Или можем посмотреть на среднечасовую температуру как функцию месяца:

alt.Chart(temps).mark_rect().encode(
    x=alt.X("hours(date):O"), y=alt.Y("month(date):O"), color="mean(temp):Q"
)

# Этот вид преобразования может оказаться полезным при работе с временными данными.
#
# Дополнительная информация о `TimeUnit Transform` доступна [здесь](https://altair-viz.github.io/user_guide/transform/timeunit.html#user-guide-timeunit-transform)

# ## Составные диаграммы
#
# *Altair* предоставляет краткий API для создания многопанельных и многоуровневых диаграмм, таких как:
#
# - Наслоение (*Layering*)
# - Горизонтальная конкатенация (*Horizontal Concatenation*)
# - Вертикальная конкатенация (*Vertical Concatenation*)
# - Повторить графики (*Repeat Charts*)
#
# Мы кратко рассмотрим их далее.

# ### Наслоение
#
# Наслоение (*layering*) позволяет размещать несколько меток (*marks*) на одной диаграмме. Один из распространенных примеров - создание графика с точками и линиями, представляющими одни и те же данные.
#
# Давайте использовать данные об акциях (*stocks*) для этого примера:

stocks = data.stocks()
stocks.head()

# Вот простой линейный график данных по акциям:

alt.Chart(stocks).mark_line().encode(x="date:T", y="price:Q", color="symbol:N")

# А вот тот же график с кружком (*circle mark*):

alt.Chart(stocks).mark_circle().encode(x="date:T", y="price:Q", color="symbol:N")

# Можем наложить эти два графика вместе с помощью оператора `+`:

# +
lines = alt.Chart(stocks).mark_line().encode(x="date:T", y="price:Q", color="symbol:N")

points = (
    alt.Chart(stocks).mark_circle().encode(x="date:T", y="price:Q", color="symbol:N")
)

lines + points
# -

# Оператор `+` всего лишь сокращение для функции `alt.layer()`, которая делает то же самое:

alt.layer(lines, points)

# Один из шаблонов, который мы будем часто использовать, - это создать базовую диаграмму с общими элементами и сложить две копии с одним изменением:

# +
base = alt.Chart(stocks).encode(x="date:T", y="price:Q", color="symbol:N")

print(base.mark_line() + base.mark_circle())
# -

# ### Горизонтальная конкатенация
#
# Так же, как мы можем накладывать диаграммы друг на друга, мы можем объединить их по горизонтали, используя `alt.hconcat` или, что то же самое, оператор `|`:

print(base.mark_line() | base.mark_circle())

alt.hconcat(base.mark_line(), base.mark_circle())

# Это может пригодиться для создания многопанельных представлений, например, вот набор данных `iris`:

iris = data.iris()
iris.head()

# +
base = (
    alt.Chart(iris)
    .mark_point()
    .encode(x="petalWidth", y="petalLength", color="species")
)

print(base | base.encode(x="sepalWidth"))
# -

# ### Вертикальная конкатенация
#
# Вертикальная конкатенация (*vertical concatenation*) очень похожа на горизонтальную, но с использованием либо функции `alt.hconcat()`, либо оператора `&`:

print(base & base.encode(y="sepalWidth"))

# ### Повторить диаграмму
#
# Поскольку это очень распространенный шаблон для объединения диаграмм по горизонтали и вертикали при изменении одной кодировки, *Altair* предлагает для этого сокращение, используя оператор `repeat()`.

# +
iris = data.iris()

fields = ["petalLength", "petalWidth", "sepalLength", "sepalWidth"]

alt.Chart(iris).mark_point().encode(
    alt.X(alt.repeat("column"), type="quantitative"),
    alt.Y(alt.repeat("row"), type="quantitative"),
    color="species",
).properties(width=200, height=200).repeat(
    row=fields, column=fields[::-1]
).interactive()
# -

# Этот API все еще не так оптимизирован, как мог бы, но мы будем над этим работать.

# **читать далее [Часть 3 в CoLab](https://colab.research.google.com/github/dm-fedorov/pandas_basic/blob/master/быстрое%20введение%20в%20pandas/Визуализация%20данных%20с%20помощью%20Altair%20(часть%203).ipynb)**
