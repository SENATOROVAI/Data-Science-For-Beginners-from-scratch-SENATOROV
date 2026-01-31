"""How to combine data from multiple tables?."""

# # Как объединить данные из нескольких таблиц?

import pandas as pd

# Для этого урока используется данные о качестве воздуха $NO_2$, данные предоставляются организацией [`openaq`](https://openaq.org/) и загружается с помощью модуля [`py-openaq`](http://dhhagan.github.io/py-openaq/index.html).
#
# <img src="https://newdaynews.ru/pict/arts1/66/19/661966_b.jpg" height="400px" width="500px" >
#
# Набор данных `air_quality_no2_long.csv` содержит значения $NO_2$ для измерительных станций `FR04014`, `BETR801` и `London Westminster` соответственно в Париже, Антверпене и Лондоне.

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_no2_long.csv"
# -

air_quality_no2 = pd.read_csv(url, parse_dates=True)

air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

air_quality_no2.head()

# Для этого урока также используются данные о качестве воздуха для твердых частиц размером менее 2,5 микрометров, данные предоставляются организацией [`openaq`](https://openaq.org/) и загружается с помощью модуля [`py-openaq`](http://dhhagan.github.io/py-openaq/index.html).
#
# см. [Частицы РМ2.5: что это, откуда и почему об этом все говорят](https://habr.com/ru/company/tion/blog/396111/)
#
# <img src="https://habrastorage.org/files/9b1/c66/b89/9b1c66b89f85464b8365b77c9ecbe781.jpg" height="500px" width="600px" >
#
# Набор данных `air_quality_pm25_long.csv` содержит значения $PM_{2.5}$ для измерительных станций `FR04014`, `BETR801` и `London Westminster` соответственно в Париже, Антверпене и Лондоне.

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_pm25_long.csv"
# -

air_quality_pm25 = pd.read_csv(url, parse_dates=True)

air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]

air_quality_pm25.head()

# ### Как объединить данные из нескольких таблиц? 

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/08_concat_row.svg" >
# </div>

# Я хочу объединить измерения $NO_2$ и $PM_{2.5}$ с похожей структурой в одну таблицу:

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

air_quality.head()

# Функция [`concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat) выполняет операцию конкатенации нескольких таблиц вдоль одной оси (по строкам или столбцам).

# По умолчанию конкатенация происходит вдоль `оси 0`, поэтому результирующая таблица объединяет строки входных таблиц. Давайте проверим форму исходных и составных таблиц, чтобы проверить операцию:

print("Shape of the `air_quality_pm25` table: ", air_quality_pm25.shape)

print("Shape of the `air_quality_no2` table: ", air_quality_no2.shape)

print("Shape of the resulting `air_quality` table: ", air_quality.shape)

# Следовательно, результирующая таблица имеет `3178 = 1110 + 2068` строк.

# Аргумент `axis` встречается в ряде методов, которые могут применяться вдоль оси. `DataFrame` имеет две соответствующие оси: первая, проходящая вертикально вниз по строкам (`ось 0`), и вторая, проходящая горизонтально по столбцам (`ось 1`). Большинство операций, таких как конкатенация или сводная статистика, по умолчанию выполняются по строкам (`ось 0`), но также могут применяться к столбцам.

# Сортировка таблицы по дате и времени иллюстрирует также комбинацию обеих таблиц, причем столбец `parameter` определяет источник таблицы (либо `no2` из таблицы `air_quality_no2`, либо `pm25` из таблицы `air_quality_pm25`):

air_quality = air_quality.sort_values("date.utc")

air_quality.head()

# В этом примере столбец `parameter`, позволяет идентифицировать каждую из исходных таблиц. Это не всегда так, функция `concat` предоставляет удобное решение с аргументом `keys`, добавляя дополнительный (иерархический) индекс строки. Например:

air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])

air_quality_.head()

# Существование нескольких индексов строк/столбцов одновременно не упоминалось ранее. Иерархическая индексация или `MultiIndex` - это продвинутая и мощная функция `pandas` для анализа многомерных данных.
#
# На данный момент помните, что функцию `reset_index` можно использовать для преобразования любого уровня индекса в столбец, например, 
#
# ```Python
# air_quality.reset_index(level=0)
# ```

# Не стесняйтесь погрузиться в мир мультииндексирования в [разделе руководства пользователя по расширенной индексации](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced).

# Дополнительные параметры конкатенации таблиц (с точки зрения строк и столбцов) и того, как `concat` можно использовать для определения логики (объединения или пересечения) индексов на других осях, представлены в [разделе о конкатенации объектов](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging-concat).

# ### Объединяйте таблицы, используя общий идентификатор

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/08_merge_left.svg">   
# </div>

# Координаты станции измерения качества воздуха хранятся в файле данных `air_quality_stations.csv`.

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_stations.csv"
# -

stations_coord = pd.read_csv(url)
stations_coord.head()

# Станции, используемые в этом примере (`FR04014`, `BETR801` и `London Westminster`) - это всего лишь три записи в таблице метаданных. Мы хотим добавить координаты этих станций в таблицу измерений, каждая из которых находится в соответствующих строках таблицы `air_quality`.

air_quality.head()

# Добавим координаты станции, предоставленные в таблице метаданных станций, в соответствующие строки таблицы измерений:

air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
air_quality.head()

# Используя функцию [`merge()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html#pandas.merge), для каждой строки таблицы `air_quality` добавляются соответствующие координаты из таблицы `air_quality_stations_coord`. Обе таблицы имеют общий столбец `location`, который используется в качестве ключа для объединения информации. Выбрав объединение `left`, в результирующей таблице `air_quality` окажутся только местоположения, доступные в (левой) таблице, например `FR04014`, `BETR801` и `London Westminster`. В функции merge поддерживает несколько опции, подобных операциям из базы данных.

# Добавим описание и имя параметра, предоставленные таблицей метаданных, в таблицу измерений:

# Метаданные параметров о качестве воздуха хранятся в файле `air_quality_parameters.csv`.

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_parameters.csv"
# -

air_quality_parameters = pd.read_csv(url)
air_quality_parameters.head()

air_quality = pd.merge(
    air_quality, air_quality_parameters, how="left", left_on="parameter", right_on="id"
)
air_quality.head()

# По сравнению с предыдущим примером нет общего имени столбца. Однако столбец parameter в таблице `air_quality` и `столбец id` в `air_quality_parameters` содержат переменную в общем формате. Аргументы `left_on` и `right_on` используются, чтобы сделать связь между двумя таблицами.

# pandas поддерживают внутренние, внешние и правые соединения. Более подробная информация о `join/merge` таблиц представлена в [разделе руководства пользователя по объединению таблиц в стиле базы данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging-join). Или взгляните на [страницу сравнения с SQL](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#compare-with-sql-join).

# См. Руководство пользователя для [полного описания различных средств для объединения таблиц данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging).
