"""How to create a plot in pandas?."""

# # Как строить график в pandas?

import matplotlib.pyplot as plt
import pandas as pd

# Для этого урока используются данные о качестве воздуха (наличие оксида озота в атмосфере). 
#
# <img src="https://openaq.org/assets/graphics/meta/default-meta-image.png" height="300px" width="500px">
#
# [Источник данных](https://openaq.org), для получения используется модуль [py-openaq](http://dhhagan.github.io/py-openaq/index.html).
#
# Набор данных `air_quality_no2.csv` содержит значения оксида озота ($NO_2$) для измерительных станций `FR04014`, `BETR801` и `London Westminster` соответственно в Париже, Антверпене и Лондоне.
#
# В России сведения не собирают, см. [карту](https://openaq.org/#/map?_k=6k578s)

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_no2.csv"
# -

air_quality = pd.read_csv(url, index_col=0, parse_dates=True)
air_quality.head()

# Использование параметров `index_col` и `parse_dates` функции `read_csv` для определения первого (0-го) столбца в качестве индекса `DataFrame` и преобразование значений индекса в объекты типа [`Timestamp`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#pandas.Timestamp) соотвественно.

#
# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/04_plot_overview.svg" >
# </div>

# Я хочу быстро получить визуальное представление данных:

air_quality.plot();

# По умолчанию создается один линейный график для каждого из столбцов таблицы с числовыми данными.

# Я хочу построить график только для столбцов с данными из Парижа:

air_quality["station_paris"].plot();

# Чтобы построить график для конкретного столбца таблицы, используйте методы выбора данных подмножеств в сочетании с методом [`plot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot). 
#
# `plot()` работает для `Series` и `DataFrame`.

# Я хочу визуально сопоставить значения $NO_2$ в Лондоне и Парижа.

# +
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.scatter.html

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5);
# -

# Помимо линейного графика по умолчанию при использовании функции `plot` существует ряд альтернатив. 
#
# Давайте используем стандартный Python, чтобы получить обзор доступных методов для построения графика:

print([
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
])

# В `jupyter notebook` используйте кнопку `TAB`, чтобы получить обзор доступных методов, например `air_quality.plot.+ TAB`.

# Пример [`DataFrame.plot.box()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.box.html#pandas.DataFrame.plot.box):

air_quality.plot.box();

# Для ознакомления с графиками, отличными от линейного, см. [Раздел руководства пользователя о поддерживаемых стилях графиков](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization-other).

# Я хочу, чтобы каждый из столбцов отображался в отдельном графике:

axs = air_quality.plot.area(figsize=(12, 4), subplots=True)

# Отдельные подграфики для каждого из столбцов данных поддерживаются аргументом `subplots` функции `plot`.

# Некоторые дополнительные параметры форматирования описаны в разделе [руководства пользователя по форматированию графиков](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization-formatting).

# Я хочу дополнительно настроить, расширить или сохранить полученный график:

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")

# Каждый из графических объектов, созданных `pandas`, является объектом [`matplotlib`](https://matplotlib.org/). Поскольку `Matplotlib` предоставляет множество опций для настройки графиков, прямая связь между `pandas` и `Matplotlib` позволяет использовать всю мощь `matplotlib` для графика. 

# Полный обзор представлен на страницах [визуализации в `pandas`](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization).
