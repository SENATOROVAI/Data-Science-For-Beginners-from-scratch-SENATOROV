"""Introduction to data visualization with Altair (part 3)."""

# # Введение в визуализацию данных с помощью Altair (часть 3)

# ## Изучение наборов данных
#
# Теперь, когда мы познакомились с основными частями *API Altair* (см. [часть 1](https://dfedorov.spb.ru/pandas/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Altair.html) и [часть 2](https://dfedorov.spb.ru/pandas/%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Altair%20(%D1%87%D0%B0%D1%81%D1%82%D1%8C%202).html)), пришло время попрактиковаться в его использовании для изучения нового набора данных.
#
# Выберите один из следующих четырех наборов данных, подробно описанных ниже.
#
# Изучая данные, вспомните о строительных блоках, которые мы обсуждали ранее:
#
# - различные метки: `mark_point()`, `mark_line()`, `mark_tick()`, `mark_bar()`, `mark_area()`, `mark_rect()` и т. д.
# - различные кодировки: `x`, `y`, `color`, `shape`, `size`, `row`, `column`, `text`, `tooltip` и т. д.
# - биннинг и агрегации: список доступных агрегаций можно найти в [документации *Altair*](https://altair-viz.github.io/user_guide/encoding.html#binning-and-aggregation)
# - наложение и наслоение (`alt.layer` <-> `+`, `alt.hconcat` <-> `|`, `alt.vconcat` <-> `&`)
#
# Начните с простого. Какие кодировки лучше всего работают с количественными данными? С категориальными данными? Что вы можете узнать о своем наборе данных с помощью этих инструментов?

import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

# ### Набор данных Погода в Сиэтле
#
# Эти данные включают суточные осадки (*daily precipitation*), диапазон температур (*temperature range*), скорость ветра (*wind speed*) и тип погоды в зависимости от даты в период с `2012` по `2015` год в Сиэтле.

weather = data.seattle_weather()
weather.head()

# ### Набор данных Gapminder
#
# Эти данные включают численность населения (*population*), рождаемости (*fertility*) и ожидаемой продолжительности жизни в ряде стран мира.
#
# *Обратите внимание: хотя у вас может возникнуть соблазн использовать временное кодирование для года, здесь год - это просто число, а не отметка даты, поэтому временное кодирование здесь не лучший выбор.*

gapminder = data.gapminder()
gapminder.head()

# ### Набор данных Население США
#
# Эти данные содержат информацию о населении США, разделенное по возрасту и полу каждое десятилетие с `1850` года до настоящего времени.
#
# *Обратите внимание: хотя у вас может возникнуть соблазн использовать временное кодирование для года, здесь год - это просто число, а не отметка даты, и поэтому временное кодирование - не лучший выбор.*

population = data.population()
population.head()

# ### Набор данных Фильмы
#
# Набор данных фильмов содержит данные о `3200` фильмах, включая дату выпуска, бюджет и рейтинги *IMDB* и [*Rotten Tomatoes*](https://www.rottentomatoes.com/).

# ## Интерактивность и выбор
#
# Интерактивность и грамматика выбора *Altair* - одна из его уникальных особенностей среди доступных графических библиотек. В этом разделе мы рассмотрим различные доступные типы выбора и начнем практиковаться в создании интерактивных диаграмм и информационных панелей (*dashboards*).
#
# Доступны три основных типа выбора:
#
# - Выбор интервала: `alt.selection_interval()`
# - Одиночный выбор: `alt.selection_single()`
# - Множественный выбор: `alt.selection_multi()`
#
# И расскажем о четырех основных вещах, которые вы можете делать с этими выборками.
#
# - Условные кодировки (*Conditional encodings*)
# - *Scales*
# - Фильтры (*Filters*)
# - Домены (*Domains*)

# ### Основные взаимодействия: панорамирование, масштабирование, всплывающие подсказки
#
# Основные взаимодействия, которые предоставляет *Altair*, - это панорамирование (*panning*), масштабирование (*zooming*) и всплывающие подсказки (*tooltips*). Это можно сделать на диаграмме без использования интерфейса выбора, используя метод `interactive()` и кодировку `tooltip`.
#
# Например, с нашим стандартным набором данных про автомобили мы можем сделать следующее:

cars = data.cars()
cars.head()

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin", tooltip="Name"
).interactive()

# В этот момент при наведении курсора на точку появится всплывающая подсказка с названием модели автомобиля, а нажатие/перетаскивание/прокрутка приведет к панорамированию и масштабированию графика.
#
# ### Более сложное взаимодействие: выбор
#
# #### Пример основного выбора: интервал
#
# В качестве примера выбора (*selection*) давайте добавим интервальное выделение на график.
#
# Начнем с классического графика рассеяния (*scatter plot*):

cars = data.cars()
cars.head()

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin"
)

# Чтобы добавить поведение выбора к диаграмме, мы создаем объект выбора и используем метод `add_selection`:

# +
interval = alt.selection_interval()

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin"
).add_selection(interval)
# -

# Это добавляет к графику взаимодействие, которое позволяет выбирать точки на графике; возможно, наиболее распространенное использование выделения - это выделение точек путем определения их цвета в зависимости от результата выбора.
#
# Это можно сделать с помощью `alt.condition`:

# +
interval = alt.selection_interval()

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(interval, "Origin", alt.value("lightgray")),
).add_selection(interval)
# -

# Функция `alt.condition` принимает *три аргумента*: объект выбора, значение, которое будет применяться к точкам внутри выделения, и значение, которое будет применено к точкам вне выделения. Здесь мы используем `alt.value('lightgray')`, чтобы убедиться, что цвет обрабатывается как фактический цвет, а не как имя столбца данных.
#
# #### Настройка выбора интервала
#
# Функция `alt.selection_interval()` принимает ряд дополнительных аргументов; например, задавая `encodings`, мы можем контролировать, охватывает ли выделение `x`, `y` или обе оси:

# +
interval = alt.selection_interval(encodings=["x"])

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(interval, "Origin", alt.value("lightgray")),
).add_selection(interval)

# +
interval = alt.selection_interval(encodings=["y"])

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(interval, "Origin", alt.value("lightgray")),
).add_selection(interval)
# -

# `empty` (пустой) аргумент позволяет нам контролировать, будут ли пустые выделения содержать *все* значения или ни одно из значений; с `empty='none'` точки по умолчанию неактивны:

# +
interval = alt.selection_interval(empty="none")

alt.Chart(cars).mark_point().encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(interval, "Origin", alt.value("lightgray")),
).add_selection(interval)
# -

# ### Одиночный выбор
#
# Функция `alt.selection_single()` позволяет пользователю кликать на отдельные объекты диаграммы, чтобы выбрать их по одному. Мы сделаем точки немного больше, чтобы их было легче нажимать:

# +
single = alt.selection_single()

alt.Chart(cars).mark_circle(size=100).encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(single, "Origin", alt.value("lightgray")),
).add_selection(single)
# -

# Единичный выбор позволяет задать и другое поведение; например, мы можем установить `nearest=True` и `on='mouseover'`, чтобы обновлять выделение до ближайшей точки при перемещении мыши:

# +
single = alt.selection_single(on="mouseover", nearest=True)

alt.Chart(cars).mark_circle(size=100).encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(single, "Origin", alt.value("lightgray")),
).add_selection(single)
# -

# ### Множественный выбор
#
# Функция `alt.selection_multi()` очень похожа на функцию `single`, за исключением того, что она позволяет выбрать несколько точек одновременно, удерживая клавишу `Shift`:

# +
multi = alt.selection_multi()

alt.Chart(cars).mark_circle(size=100).encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(multi, "Origin", alt.value("lightgray")),
).add_selection(multi)
# -

# Такие опции, как `on` и `nearest`, также работают для множественного выбора:

# +
multi = alt.selection_multi(on="mouseover", nearest=True)

alt.Chart(cars).mark_circle(size=100).encode(
    x="Horsepower:Q",
    y="Miles_per_Gallon:Q",
    color=alt.condition(multi, "Origin", alt.value("lightgray")),
).add_selection(multi)
# -

# ### Привязка выделения
#
# Выше мы увидели, как `alt.condition` можно использовать для привязки выделения к различным аспектам диаграммы. Давайте рассмотрим еще несколько способов использования выделения:
#
# #### Привязка Scales
#
# Для выбора интервала еще одна вещь, которую вы можете сделать с выделением, - это привязать область выбора к шкалам диаграммы:

# +
bind = alt.selection_interval(bind="scales")

alt.Chart(cars).mark_circle(size=100).encode(
    x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin:N"
).add_selection(bind)
# -

# По сути, это то, что делает метод `chart.interactive()` под капотом.
#
# #### Привязка scales к другим доменам
#
# Также можно привязать шкалы к другим доменам (*domain*).

weather = data.seattle_weather()
weather.head()

# +
base = (
    alt.Chart(weather)
    .mark_rule()
    .encode(x="date:T", y="temp_min:Q", y2="temp_max:Q", color="weather:N")
)

base

# +
chart = base.properties(width=800, height=300)

view = chart.properties(width=800, height=50)

chart & view
# -

# Давайте добавим выбор интервала к нижнему графику, который будет контролировать домен верхнего графика:

# +
interval = alt.selection_interval(encodings=["x"])

base = (
    alt.Chart(weather)
    .mark_rule(size=2)
    .encode(x="date:T", y="temp_min:Q", y2="temp_max:Q", color="weather:N")
)

chart = base.encode(
    x=alt.X("date:T", scale=alt.Scale(domain=interval.ref()))
).properties(width=800, height=300)

view = base.add_selection(interval).properties(
    width=800,
    height=50,
)

chart & view
# -

# ### Фильтрация по выделению
#
# В многопанельных диаграммах мы можем использовать результат выбора для фильтрации других представлений данных. Например, вот диаграмма рассеяния вместе с гистограммой:

# +
interval = alt.selection_interval()

scatter = (
    alt.Chart(cars)
    .mark_point()
    .encode(
        x="Horsepower:Q",
        y="Miles_per_Gallon:Q",
        color=alt.condition(interval, "Origin:N", alt.value("lightgray")),
    )
    .add_selection(interval)
)

hist = (
    alt.Chart(cars)
    .mark_bar()
    .encode(x="count()", y="Origin", color="Origin")
    .transform_filter(interval)
)

scatter & hist
# -

# Точно так же вы можете использовать множественный выбор, чтобы пойти другим путем (разрешите кликнуть на гистограмму, чтобы отфильтровать содержимое диаграммы рассеяния.
#
# Добавим эту возможность к предыдущей диаграмме:

# +
click = alt.selection_multi(encodings=["color"])

scatter = (
    alt.Chart(cars)
    .mark_point()
    .encode(x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin:N")
    .transform_filter(click)
)

hist = (
    alt.Chart(cars)
    .mark_bar()
    .encode(
        x="count()",
        y="Origin",
        color=alt.condition(click, "Origin", alt.value("lightgray")),
    )
    .add_selection(click)
)

scatter & hist
# -

# ### Сводная информация по выбору в Altair
#
# **Типы выбора:**
#
# - `selection_interval()`
# - `selection_single()`
# - `selection_multi()`
#
# **Привязки:**
#
# - привязать масштабы: перетащите и прокрутите, чтобы взаимодействовать с графиком
# - привязать шкалы к другому графику
# - условные кодировки (например, цвет, размер)
# - фильтровать данные

# ### Упражнение: выбор в Altair
#
# Теперь у вас есть возможность попробовать построить графики самостоятельно! Выберите один или несколько из следующих интерактивных примеров:
#
# 1. Используя данные об автомобилях, создайте диаграмму рассеяния (*scatter-plot*), на которой *размер* (*size*) точек становится больше при наведении на них курсора.
#
# 2. Используя данные об автомобилях, создайте двухпанельную (*two-panel*) гистограмму (скажем, количество миль на галлон на одной панели, количество лошадиных сил на другой), где вы можете перетащить мышь, чтобы выбрать данные на левой панели, чтобы отфильтровать данные на второй панели.
#
# 3. Измените приведенный выше пример диаграммы разброса и гистограммы, чтобы
#
# - панорамировать и увеличивать диаграмму рассеяния;
# - гистограмма отражала только те точки, которые видны в данный момент.
#
# 4. Попробуй что-нибудь новое!

# ## Преобразования
#
# Важным элементом конвейера визуализации является преобразование данных (*data transformation*).
#
# С *Altair* у вас есть два возможных пути преобразования данных, а именно:
#
# 1. предварительное преобразование в *Python*
# 2. трансформация в *Altair/Vega-Lite*

# ### Вычисление преобразования
#
# В качестве примера рассмотрим преобразование входных данных о населении. В наборе данных перечислены агрегированные данные переписи США по годам, полу и возрасту, но пол указан как `1` и `2`, что делает надписи на диаграммах мало понятными:

population = data.population()

population.head()

alt.Chart(population).mark_bar().encode(x="year:O", y="sum(people):Q", color="sex:N")

# Один из способов решить эту проблему с помощью *Python* - использовать инструменты *Pandas* для переназначения имен столбцов, например:

# +
population["men_women"] = population["sex"].map({1: "Men", 2: "Women"})

alt.Chart(population).mark_bar().encode(
    x="year:O", y="sum(people):Q", color="men_women:N"
)
# -

# Но *Altair* предназначен для использования с данными, доступными по URL, в которых такая предварительная обработка недоступна. В таких ситуациях лучше сделать преобразование частью спецификации графика.
#
# Это можно сделать с помощью метода `transform_calculate`, принимающего [*Vega-выражение*](https://vega.github.io/vega/docs/expressions/), которое по сути представляет собой строку, которая может содержать небольшое подмножество операций *JavaScript*:

# отменить добавление столбца выше...
population = population.drop("men_women", axis=1)

alt.Chart(population).mark_bar().encode(
    x="year:O", y="sum(people):Q", color="men_women:N"
).transform_calculate(men_women='datum.sex == 1 ? "Men" : "Women"')

# Одна потенциально сбивающая с толку часть - это наличие слова `datum`: это просто соглашение, по которому *Vega-выражения* ссылаются на строку данных.
#
# Если вы предпочитаете создавать эти выражения на *Python*, то *Altair* предоставляет для этого облегченный API:

alt.Chart(population).mark_bar().encode(
    x="year:O", y="sum(people):Q", color="men_women:N"
).transform_calculate(men_women="datum.sex == 1 ? 'Men' : 'Women'")

# ### Преобразование фильтра
#
# Преобразование фильтра аналогично. Например, предположим, что вы хотите создать диаграмму, состоящую только из мужского населения из записей переписи. Как и выше, это можно сделать в *Pandas*, но полезно, чтобы эта операция была доступна и в спецификации диаграммы. Это можно сделать с помощью метода `transform_filter()`:

alt.Chart(population).mark_bar().encode(
    x="year:O",
    y="sum(people):Q",
).transform_filter("datum.sex == 1")

# Мы уже встречали метод `transform_filter` раньше, когда выполняли фильтрацию на основе результата выбора.

# ### Другие преобразования
#
# Доступны и другие методы преобразования, и хотя мы не будем их здесь демонстрировать, примеры можно найти в [документации *Altair Transform*](https://altair-viz.github.io/user_guide/transform/index.html).
#
# *Altair* предоставляет ряд полезных преобразований. Некоторые будут вам знакомы:
#
# - `transform_aggregate()`
# - `transform_bin()`
# - `transform_timeunit()`
#
# Эти три преобразования приводят к созданию нового именованного значения, на которое можно ссылаться в нескольких местах на диаграмме.
#
# Также существует множество других преобразований, таких как:
#
# - `transform_lookup()`: позволяет выполнять одностороннее объединение нескольких наборов данных и часто используется, например, в географических визуализациях, где вы объединяете данные (например, безработица в пределах штатов) с данными о географических регионах, используемых для представления этих данных.
# - `transform_window()`: позволяет выполнять агрегирование по скользящим окнам, например, вычисляя локальные средние (*local means*) данных. Он был недавно добавлен в *Vega-Lite*, поэтому *API Altair* для этого преобразования пока не очень удобен.
#
# Посетите [документацию по *Transform*](https://altair-viz.github.io/user_guide/transform/index.html) для получения более полного списка.

# ## Упражнение
#
# Возьмем следующие данные:

x_var = pd.DataFrame({"x_var": np.linspace(-5, 5)})

# 1. Создайте диаграмму на основе этих данных и постройте кривые синуса и косинуса с помощью `transform_calculate`.
#
# 2. Используйте `transform_filter` на этой диаграмме и удалите области графика, где значение кривой косинуса меньше значения кривой синуса.

# ## Конфигурация диаграммы
#
# *Altair* предоставляет несколько хуков для настройки внешнего вида диаграммы; у нас нет времени подробно описывать здесь все доступные параметры, но полезно знать, где и как можно получить доступ и изучить такие параметры.
#
# Как правило, есть два или три места, где можно управлять видом диаграммы, каждое из которых имеет больший приоритет, чем предыдущее.
#
# 1. **Конфигурация диаграммы верхнего уровня**. На верхнем уровне диаграммы *Altair* вы можете указать параметры конфигурации, которые будут применяться к каждой панели или слою на диаграмме.
#
# 2. **Параметры локальной конфигурации**. Параметры верхнего уровня можно переопределить локально, указав локальную конфигурацию.
#
# 3. **Значения кодирования**. Если указано значение кодировки, оно будет иметь наивысший приоритет и переопределять другие параметры.
#
# Посмотрим на пример.

# +
np.random.seed(42)

df = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])
# -

# ### Пример 1: Управление свойствами маркера
#
# Предположим, вы хотите контролировать *цвет маркеров* на диаграмме рассеяния: давайте посмотрим на каждый из трех вариантов для этого. Мы будем использовать простые наборы данных нормально распределенных точек:

alt.Chart(df).mark_point().encode(x="x:Q", y="y:Q")

# ### Конфигурация верхнего уровня
#
# На верхнем уровне у *Altair* есть метод `configure_mark()`, который позволяет настраивать большое количество параметров конфигурации для меток в целом, а также свойство `configure_point()`, которое специально настраивает свойства точек.
#
# Вы можете увидеть доступные параметры в строке документации Jupyter, доступ к которой осуществляется через вопросительный знак:

# +
# # alt.Chart.configure_point?
# -

# Эту конфигурацию верхнего уровня следует рассматривать как тему диаграммы: они являются настройками по умолчанию для эстетики всех элементов диаграммы. Давайте воспользуемся `configure_point`, чтобы установить некоторые свойства точек:

alt.Chart(df).mark_point().encode(x="x:Q", y="y:Q").configure_point(
    size=200, color="red", filled=True
)

# Доступно множество локальных конфигураций; вы можете использовать функцию автозавершения табуляции и справочные функции Jupyter, чтобы изучить их
#
# ```python
# alt.Chart.configure_  # затем нажмите клавишу TAB, чтобы увидеть доступные конфигурации
# ```

# ### Конфигурация локальной метки
#
# В методе `mark_point()` вы можете передавать локальные конфигурации, которые переопределяют параметры конфигурации верхнего уровня. Аргументы такие же, как у `configure_mark`.

alt.Chart(df).mark_point(color="green", filled=False).encode(
    x="x:Q", y="y:Q"
).configure_point(size=200, color="red", filled=True)

# Обратите внимание, что конфигурации `color` и `fill` переопределяются локальными конфигурациями, но `size` остается таким же, как и раньше.
#
# ### Конфигурация кодирования
#
# Наконец, самый высокий приоритет - это параметр `encoding`. Здесь давайте установим цвет `Steelblue` в кодировке:

alt.Chart(df).mark_point(color="green", filled=False).encode(
    x="x:Q", y="y:Q", color=alt.value("steelblue")
).configure_point(size=200, color="red", filled=True)

# Это немного надуманный пример, но он полезен, чтобы помочь понять различные места, в которых могут быть установлены свойства меток.
#
# ### Пример 2: заголовки диаграммы и осей
#
# Названия диаграмм и осей устанавливаются автоматически в зависимости от источника данных, но иногда бывает полезно их изменить. Например, вот гистограмма приведенных выше данных:

alt.Chart(df).mark_bar().encode(x=alt.X("x", bin=True), y=alt.Y("count()"))

# Мы можем явно установить заголовки осей, используя аргумент `title` для кодировки:

alt.Chart(df).mark_bar().encode(
    x=alt.X("x", bin=True, title="binned x values"),
    y=alt.Y("count()", title="counts in x"),
)

# Точно так же мы можем установить свойство `title` диаграммы в свойствах диаграммы:

alt.Chart(df).mark_bar().encode(
    x=alt.X("x", bin=True, title="binned x values"),
    y=alt.Y("count()", title="counts in x"),
).properties(title="A histogram")

# ### Пример 3: Свойства оси
#
# Если вы хотите установить свойства осей, включая линии сетки, вы можете использовать аргумент кодировки `axis`.

alt.Chart(df).mark_bar().encode(
    x=alt.X("x", bin=True, axis=alt.Axis(labelAngle=45)),
    y=alt.Y("count()", axis=alt.Axis(labels=False, ticks=False, title=None)),
)

# Обратите внимание, что некоторые из этих значений также можно настроить в конфигурации верхнего уровня, если вы хотите, чтобы они применялись к диаграмме в целом. Например:

alt.Chart(df).mark_bar().encode(
    x=alt.X("x:Q", bin=True),
    y=alt.Y("count()", axis=alt.Axis(labels=False, ticks=False, title=None)),
).configure_axisX(labelAngle=45)

# ### Пример 4: Масштабировать свойства и пределы оси
#
# Каждая кодировка также имеет `scale` (масштаб), который позволяет настраивать такие параметры, как пределы оси и другие свойства масштаба.

alt.Chart(df).mark_point().encode(
    x=alt.X("x:Q", scale=alt.Scale(domain=[-5, 5])),
    y=alt.Y("y:Q", scale=alt.Scale(domain=[-5, 5])),
)
x_var = alt.X("x:Q", bin=True)

# Обратите внимание, что если вы уменьшите масштаб до меньшего размера, чем диапазон данных, данные по умолчанию будут выходить за пределы шкалы:

alt.Chart(df).mark_point().encode(
    x=alt.X("x:Q", scale=alt.Scale(domain=[-3, 1])),
    y=alt.Y("y:Q", scale=alt.Scale(domain=[-3, 1])),
)

# Отсутствие скрытия данных - полезный вариант по умолчанию при исследовательской визуализации, поскольку он предотвращает непреднамеренное отсутствие точек данных.
#
# Если вы хотите, чтобы маркеры были обрезаны за пределами диапазона шкал, вы можете установить свойство `clip` для маркеров:

alt.Chart(df).mark_point(clip=True).encode(
    x=alt.X("x:Q", scale=alt.Scale(domain=[-3, 1])),
    y=alt.Y("y:Q", scale=alt.Scale(domain=[-3, 1])),
)

# Другой полезный подход - вместо этого "зажимать" данные до крайних значений шкалы, сохраняя их видимыми, даже когда они находятся вне диапазона:

alt.Chart(df).mark_point().encode(
    x=alt.X("x:Q", scale=alt.Scale(domain=[-3, 1], clamp=True)),
    y=alt.Y("y:Q", scale=alt.Scale(domain=[-3, 1], clamp=True)),
).interactive()

# ### Пример 5: Цветовые шкалы
#
# Иногда полезно вручную настроить используемую цветовую шкалу.

weather = data.seattle_weather()
weather.head()

alt.Chart(weather).mark_point().encode(x="date:T", y="temp_max:Q", color="weather:N")

# Вы можете изменить цветовую схему с помощью свойства цветовой шкалы из [цветовых схем *Vega*](https://vega.github.io/vega/docs/schemes/#reference):

alt.Chart(weather).mark_point().encode(
    x="date:T",
    y="temp_max:Q",
    color=alt.Color("weather:N", scale=alt.Scale(scheme="dark2")),
)

# Как вариант, вы можете создать свою собственную цветовую схему, указав цветовую область и диапазон:

# +
colorscale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["goldenrod", "gray", "lightblue", "steelblue", "midnightblue"],
)

alt.Chart(weather).mark_point().encode(
    x="date:T", y="temp_max:Q", color=alt.Color("weather:N", scale=colorscale)
)
# -

# ### Упражнение: корректировка графиков
#
# Потратьте около 10 минут и попрактикуйтесь в корректировке эстетики ваших графиков.
#
# Используйте любимую визуализацию из предыдущего упражнения и настройте эстетику графика:
#
# - настроить вид меток (`size`, `strokewidth` и т. д.)
# - изменить оси и названия графика
# - изменить пределы `x` и `y`
#
# Используйте завершение табуляции в `alt.Chart.configure_`, чтобы увидеть различные параметры конфигурации, затем используйте `?`, чтобы увидеть документацию по функциям.

# ## Географические графики
#
# В *Altair 2.0* добавлена возможность построения географических данных.
#
# Эта функциональность все еще немного сырая (например, не все взаимодействия или выборки работают должным образом с проецируемыми данными), но ее относительно просто использовать.
#
# Мы покажем здесь несколько примеров.

# ### Диаграммы рассеяния в географических координатах
#
# Сначала мы покажем пример построения данных широты/долготы с использованием картографической проекции. Мы загрузим набор данных, состоящий из широты/долготы каждого аэропорта США:

airports = data.airports()
airports.head()

# График очень похож на стандартный график рассеяния с некоторыми отличиями:
#
# - мы указываем кодировки `latitude` и `longitude` вместо `x` и `y`
# - мы указываем проекции (*projection*), который будет использоваться для данных
#
# Для данных, охватывающих только США, полезна проекция `albersUsa` (Альберса):
#
# > *Проекция Альберса* — картографическая проекция, разработанная в 1805 году немецким картографом Хейнрихом Альберсом. Используется для изображения регионов, вытянутых в широтном направлении. Проекция коническая, сохраняющая площадь объектов, но искажающая углы и форму контуров (из [Вики](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%86%D0%B8%D1%8F_%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D1%80%D1%81%D0%B0)).

alt.Chart(airports).mark_circle().encode(
    longitude="longitude:Q", latitude="latitude:Q", size=alt.value(10), tooltip="name"
).project("albersUsa").properties(width=500, height=400)

# Доступные проекции перечислены в [документации *Vega*](https://vega.github.io/vega/docs/projections/).
#
# ## Карты хороплетов (фоновая картограмма)
#
# Если вы хотите нанести географические границы, такие как штаты и страны, то должны загрузить данные географической формы для отображения в *Altair*. Для этого требуется немного шаблонов (*boilerplate*) (мы думаем о том, как оптимизировать эту типичную конструкцию в будущих выпусках) и использовать маркер `geoshape`.
#
# Например, вот государственные границы:

# +
states = alt.topo_feature(data.us_10m.url, feature="states")

alt.Chart(states).mark_geoshape(fill="lightgray", stroke="white").project(
    "albersUsa"
).properties(width=500, height=300)
# -

# А вот и границы стран:

# +
countries = alt.topo_feature(data.world_110m.url, "countries")

alt.Chart(countries).mark_geoshape(fill="lightgray", stroke="white").project(
    "equirectangular"
).properties(width=500, height=300)
# -

# Вы можете посмотреть, что произойдет, если попробуете другие типы проекций, например, можете попробовать `mercator`, `orthographic`, `albers` или `gnomonic`.

# Вы можете посмотреть, что произойдет, если попробуете другие типы проекций, например, можете попробовать `mercator`, `orthographic`, `albers` или `gnomonic`.

# +
states = alt.topo_feature(data.us_10m.url, feature="states")
airports = data.airports()

background = (
    alt.Chart(states)
    .mark_geoshape(fill="lightgray", stroke="white")
    .project("albersUsa")
    .properties(width=500, height=300)
)

points = (
    alt.Chart(airports)
    .mark_circle()
    .encode(
        longitude="longitude:Q",
        latitude="latitude:Q",
        size=alt.value(10),
        tooltip="name",
    )
)

background + points
# -

# Обратите внимание, что нам нужно указать проекцию и размер диаграммы только один раз.

# ## Цветные хороплеты
#
# Самый сложный тип диаграммы - это диаграмма, в которой регионы карты окрашены, чтобы отразить лежащие в основе данные. Причина, по которой это сложно, заключается в том, что это часто связано с объединением двух разных наборов данных с помощью преобразования поиска (*lookup transform*).
#
# Опять же, это часть API, которую мы надеемся улучшить в будущем.
#
# В качестве примера, вот диаграмма, представляющая общее население каждого штата:

pop = data.population_engineers_hurricanes()
pop.head()

# +
states = alt.topo_feature(data.us_10m.url, "states")

variable_list = ["population", "engineers", "hurricanes"]

alt.Chart(states).mark_geoshape().encode(color="population:Q").transform_lookup(
    lookup="id", from_=alt.LookupData(pop, "id", list(pop.columns))
).properties(width=500, height=300).project(type="albersUsa")
# -

# Обратите внимание на ключевой момент: данные хороплет имеют столбец `id`, который соответствует столбцу `id` в данных о населении. Мы используем его как ключ поиска, чтобы объединить два набора данных вместе и построить их соответствующим образом.
#
# Чтобы увидеть больше примеров географических визуализаций, см. [галерею *Altair*](https://altair-viz.github.io/gallery/index.html#maps) и имейте в виду, что это область *Altair* и *Vega-Lite*, которая постоянно улучшается!

# Успехов!
