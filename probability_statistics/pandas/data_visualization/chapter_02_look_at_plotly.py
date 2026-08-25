"""A look at Plotly."""

# # Взгляд на Plotly

# <img src="https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/pyviz.jpg" height="600px" width="800px" >
#
# [*Источник картинки*](https://pyviz.org/overviews/index.html)

# В этой статье мы обсудим некоторые из последних изменений в *Plotly*, в чем заключаются преимущества и почему *Plotly* стоит рассмотреть для визуализации данных.
#
# > Оригинал статьи Криса [здесь](https://pbpython.com/plotly-look.html)
#
# В марте 2019 года *Plotly* [выпустила *Plotly Express*](https://medium.com/plotly/introducing-plotly-express-808df010143d). Эта новая высокоуровневая библиотека решила многие мои опасения по поводу питонической природы *Plotly API*, о которых я расскажу в этой статье.

# ## Согласованный API
#
# Когда я создаю визуализации, то перебираю множество разных подходов. Для меня важно, что я могу легко переключать подходы к визуализации с минимальными изменениями кода.
#
# > Подход *Plotly Express* в чем-то похож на *seaborn*.
#
# Для демонстрации будем использовать [данные о злаках](https://www.kaggle.com/crawford/80-cereals), которые я очистил для ясности:

# # устанавливаем последнюю версию plotly - это важно для работы примеров:

# !pip install plotly==4.14.3

# +
# pylint: disable=line-too-long

import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True"
)
# -

# Данные содержат некоторые характеристики различных злаков:

df.head()

# Если мы хотим посмотреть на взаимосвязь между `rating` и `sugars` и включить название злака в виде ярлыка при наведении курсора:

fig = px.scatter(
    df, x="sugars", y="rating", hover_name="name", title="Cereal ratings vs. sugars"
)
fig.show()

# Используя этот подход, легко переключать типы диаграмм, изменяя вызов функции.
#
# Например, довольно очевидно, что будет делать каждый из следующих типов диаграмм:
#
# - [`px.scatter()`](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html#plotly.express.scatter)
# - [`px.line()`](https://plotly.com/python-api-reference/generated/plotly.express.line.html#plotly.express.line)
# - [`px.bar()`](https://plotly.com/python-api-reference/generated/plotly.express.bar.html#plotly.express.bar)
# - [`px.histogram()`](https://plotly.com/python-api-reference/generated/plotly.express.histogram.html#plotly.express.histogram)
# - [`px.box()`](https://plotly.com/python-api-reference/generated/plotly.express.box.html#plotly.express.box)
# - [`px.violin()`](https://plotly.com/python-api-reference/generated/plotly.express.violin.html#plotly.express.violin)
# - [`px.strip()`](https://plotly.com/python-api-reference/generated/plotly.express.strip.html#plotly.express.strip)
#
# > Полный список функций *Plotly Express* доступен по [ссылке](https://plotly.com/python-api-reference/plotly.express.html)
#
# Для моей работы эти типы диаграмм покрывают 80-90% того, что я делаю изо дня в день.
#
# Другой пример. На этот раз - статическая гистограмма:

fig = px.histogram(df, x="rating", title="Rating distribution")
fig.show()

# В дополнение к различным типам диаграмм большинство типов поддерживают одну и ту же базовую сигнатуру функции, поэтому вы можете легко ограничивать (*facet*) данные или изменять цвета/размеры на основе значений в вашем фрейме:

fig = px.scatter(
    df,
    x="sugars",
    y="rating",
    color="mfr",
    size="calories",
    facet_row="shelf",
    facet_col="type",
    hover_name="name",
    category_orders={"shelf": ["Top", "Middle", "Bottom"]},
)
fig.show()

# Даже если вы никогда раньше не использовали *Plotly*, вы должны иметь общее представление о том, что делает [каждый из этих параметров](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html#plotly.express.scatter), и понимать, насколько полезным может быть отображение данных различными способами, внося незначительные изменения в вызовы функций.
#
# ## Множество типов диаграмм
#
# В дополнение к основным типам диаграмм, описанным выше, *Plotly* имеет несколько расширенных/специализированных диаграмм, таких как [`funnel_chart`](https://plotly.com/python/funnel-charts/), [`timeline`](https://plotly.com/python/gantt/), [`treemap`](https://plotly.com/python/treemaps/), [`sunburst`](https://plotly.com/python/sunburst-charts/) и [`geographic maps`](https://plotly.com/python/maps/).
#
# Я думаю, что базовые типы диаграмм должны быть отправной точкой для анализа, но иногда действительно эффективной может оказаться более сложная визуализация.
#
# Стоит потратить время и посмотреть [здесь](https://plotly.com/python/plotly-express/) все варианты. Никогда не знаешь, когда может понадобиться более сложный тип диаграммы.
#
# Например, древовидная карта (*treemap*) может быть полезной для понимания иерархической природы данных. Этот тип диаграммы обычно не доступен в других библиотеках визуализации *Python*, что является еще одним приятным плюсом для *Plotly*:

fig = px.treemap(
    df, path=["shelf", "mfr"], values="cereal", title="Cereals by shelf location"
)
fig.show()

# Вы можете поменять концепции и использовать диаграмму солнечных лучей (*sunburst*):

fig = px.sunburst(df, path=["mfr", "shelf"], values="cereal")
fig.show()

# > Официальное описание *Plotly Express* см. [здесь](https://plotly.com/python/plotly-express/)

# ## Сохранение изображений
#
# Удивительно, но одна из проблем многих библиотек построения графиков заключается в том, что непросто сохранять статические файлы `.png`, `.jpeg` или `.svg`. Это одна из областей, где *matplotlib* действительно сияет, и многие инструменты построения графиков на основе javascript испытывают трудности, особенно когда корпоративные системы заблокированы, а настройки межсетевого экрана вызывают проблемы. Я сделал достаточно снимков экрана и вставил изображений в PowerPoint.
#
# > см. [эффективное использование *Matplotlib*](https://dfedorov.spb.ru/pandas/%D0%AD%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20Matplotlib.html)
#
# Недавно компания *Plotly* выпустила приложение [`kaleido`](https://github.com/plotly/Kaleido), которое значительно упрощает сохранение статических изображений в нескольких форматах. В [анонсе](https://medium.com/plotly/introducing-kaleido-b03c4b7b1d81) более подробно рассказывается о проблемах разработки стабильного и быстрого решения для экспорта изображений. Я лично боролся с некоторыми из этих проблем.
#
# Например, если я хочу сохранить уменьшенную версию (`scale=.85`) диаграммы солнечных лучей (*sunburst chart*):

# !pip install -U kaleido

# +
# после установки kaleido его иногда не видит Colab, но на локальной машине со второго раза работает:
# -

fig.write_image("sunburst.png", scale=0.85, engine="kaleido")

# *Plotly* также поддерживает сохранение в виде отдельного HTML.

fig.write_html(
    "treemap.html", include_plotlyjs="cdn", full_html=False, include_mathjax="cdn"
)

# ## Работа с Pandas
#
# При работе с данными, я всегда получаю фрейм данных *pandas*, и большую часть времени он имеет [аккуратный (*tidy*) формат](https://dfedorov.spb.ru/pandas/%D0%90%D0%BA%D0%BA%D1%83%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B2%20Python.html). *Plotly* изначально понимает фрейм данных, поэтому вам не нужно дополнительное преобразование данных перед построением графика.
#
# > Все функции *Plotly Express* принимают в качестве входных данных ["аккуратный" фрейм](http://www.jeannicholashould.com/tidy-data-in-python.html).
#
# *Pandas* позволяют определять различные бэкэнды построения графиков (*plotting back ends*), и *Plotly* можно включить следующим образом:

pd.options.plotting.backend = "plotly"

# Это позволяет создавать визуализацию, используя комбинацию *pandas* и *Plotly API*. Вот пример гистограммы с использованием этой комбинации:

# +
fig = df[["sodium", "potass"]].plot(
    kind="hist",
    nbins=50,
    histnorm="probability density",
    opacity=0.75,
    marginal="box",
    title="Potassium and Sodium Distributions",
)

fig.show()
# -

# Еще одно недавнее изменение в *Plotly Express* заключается в том, что он поддерживает "широкую форму" (*wide-form*), а также аккуратные (также известные как *long-form*) данные.
#
# Эта функция позволяет передавать несколько столбцов фрейма данных вместо того, чтобы пытаться преобразовать данные в правильный формат.
#
# Обратитесь к [документации за дополнительными примерами](https://plotly.com/python/wide-form/).

# ## Настройка рисунка
#
# *Plotly Express* поддерживает быстрые и простые модификации визуализаций. Однако бывают случаи, когда нужно выполнить точную настройку.
#
# > Каждая функция *Plotly Express* воплощает четкое сопоставление строк фрейма данных с отдельными или сгруппированными визуальными метками и имеет подпись, вдохновленную [Грамматикой графики](https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149).
#
# Вот цитата из [вводной статьи](https://medium.com/plotly/introducing-plotly-express-808df010143d) о *Plotly Express*:
#
# > *Plotly Express* для *Plotly.py* - это то же самое, что *Seaborn* для *matplotlib*: высокоуровневая оболочка, которая позволяет быстро создавать фигуры, а затем использовать возможности базового API и экосистемы для внесения изменений.
#
# Вы можете настроить окончательную диаграмму *Plotly Express*, используя `update_layout`, `add_shape`, `add_annotation`, `add_trace` или задав `template`. В [документации много подробных примеров](https://plotly.com/python/creating-and-updating-figures/#updating-figures).
#
# Вот пример настройки нескольких компонентов распределения натрия (`sodium`) и калия (`potass`):

# +
# fig = df[["sodium", "potass"]].plot(
#     kind="hist",
#     nbins=50,
#     opacity=0.75,
#     marginal="box",
#     title="Potassium and Sodium Distributions",
# )

# fig.update_layout(
#     title_text="Sodium and Potassium Distribution",  # название графика
#     xaxis_title_text="Grams",
#     yaxis_title_text="Count",
#     bargap=0.1,  # промежуток между полосами координат соседнего местоположения
#     template="simple_white",  # выберите один из предопределенных шаблонов
# )

# # Может вызывать update_layout несколько раз
# fig.update_layout(legend=dict(yanchor="top", y=0.74, xanchor="right", x=0.99))

# # добавить вертикальную "целевую" линию
# fig.add_shape(
#     type="line",
#     line_color="gold",
#     line_width=3,
#     opacity=1,
#     line_dash="dot",
#     x0=100,
#     x1=100,
#     xref="x",
#     y0=0,
#     y1=15,
#     yref="y",
# )

# # добавить текстовую выноску со стрелкой
# fig.add_annotation(
#     text="USDA Target", xanchor="right", x=100, y=12, arrowhead=1, showarrow=True
# )

# fig.show()  
# -

# Далее пример из [официального описания](https://medium.com/plotly/introducing-plotly-express-808df010143d), который показывает продолжительность жизни в сравнении с ВВП на душу населения по странам за 2007 г:

# +
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")
# -

# Возможно, вы хотите увидеть, как эта диаграмма развивалась с течением времени.
#
# Вы можете анимировать ее, установив `animation_frame="year"` и `animation_group="country"`, чтобы определить, какие круги соответствуют каким в кадрах.

# +
# px.scatter(
#     gapminder,
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     size_max=60,
#     color="continent",
#     hover_name="country",
#     animation_frame="year",
#     animation_group="country",
#     log_x=True,
#     range_x=[100, 100000],
#     range_y=[25, 90],
#     labels=dict(
#         pop="Population", gdpPercap="GDP per Capita", lifeExp="Life Expectancy"
#     ),
# )
# -

# Поскольку это географические данные, то можем представить их в виде анимированной карты:

px.choropleth(
    gapminder,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale=px.colors.sequential.Plasma,
    projection="natural earth",
)

# > [Dash](https://dash.plot.ly/) - это фреймворк *Plotly* с открытым исходным кодом для создания аналитических приложений и панелей мониторинга с диаграммами *Plotly.py*. Объекты, которые производит *Plotly Express*, на 100% совместимы с *Dash*.
#
# Синтаксис *Plotly* относительно прост, но может потребоваться некоторое время, чтобы проработать документацию и найти правильную комбинацию. Это одна из областей, где относительная молодость пакета означает, что существует не так много примеров настройки.
