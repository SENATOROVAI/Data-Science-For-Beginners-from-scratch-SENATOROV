"""How to easily process time series data?."""

# # Как легко обрабатывать данные временных рядов?   

import matplotlib.pyplot as plt
import pandas as pd

# Для этого урока используется набор данных `air_quality_no2_long.csv`.

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_no2_long.csv"
# -

air_quality = pd.read_csv(url)

air_quality = air_quality.rename(columns={"date.utc": "datetime"})

air_quality.head()

air_quality.city.unique()

# ### Использование свойств даты и времени 

# Я хочу работать с датами в столбце `datetime` как объектами даты и времени вместо простого текста:

air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

air_quality["datetime"]

# Первоначально значения в `datetime` являются символьными строками и не предоставляют никаких операций даты и времени (например, извлечение года, дня недели и т.д.). Применяя функцию [`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html), pandas интерпретирует строки и преобразует их в объекты `datetime` (т.е. `datetime64[ns, UTC]`). В `pandas` мы называем эти объекты аналогично стандартной библиотеке [`datetime.datetime pandas.Timestamp`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#pandas.Timestamp).

# Поскольку многие наборы данных содержат информацию в формате `datetime` в одном из столбцов, функции [`pandas.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv) и [`pandas.read_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html#pandas.read_json) могут выполнить преобразование к датам в момент чтения данных через использование параметра `parse_dates`:
#
# ```Python
# pd.read_csv("../data/air_quality_no2_long.csv", parse_dates=["datetime"])
# ```

# Какая польза от объектов [`pandas.Timestamp`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#pandas.Timestamp)?
#
# С какой даты начинается и оканчивается набор данных?

print(air_quality["datetime"].min(), air_quality["datetime"].max())

# Использование [`pandas.Timestamp`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#pandas.Timestamp) для `datetime` позволяет нам производить расчеты с информацией о дате. Следовательно, мы можем использовать этот тип данных, чтобы получить длину временного ряда:

print(air_quality["datetime"].max() - air_quality["datetime"].min())

# В результате получается объект [`pandas.Timedelta`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#pandas.Timestamp), аналогичный `datetime.timedelta` в стандартной библиотеке Python и определяющий продолжительность времени.

# Различные концепции времени, поддерживаемые `pandas`, объясняются в разделе [руководства пользователя о концепциях, связанных со временем](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-overview).

# Я хочу добавить новый столбец, содержащий только месяц измерения:

air_quality["month"] = air_quality["datetime"].dt.month

air_quality.head()

# Используя объекты `Timestamp`, появляются многие связанные со временем свойства. Например `month`, `year`, `weekofyear`, `quarter`... Все эти свойства доступны по [аксессору `dt`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html).

# Обзор существующих свойств даты приведен в [таблице](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-components). 

# Какая средняя концентрация $NO_2$ для каждого дня недели и для каждого места измерения?

air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()

# Здесь мы хотим вычислить статистику для каждого дня недели и для каждого места измерения. Для группировки по рабочим дням мы используем свойство `weekday` (с `Monday=0` и `Sunday=6`) для `Timestamp`, которое также доступно через `dt`. Группировка по местоположениям и по дням недели выполняется, чтобы разделить вычисление среднего значения для каждой из этих комбинаций.

# Типичный график для $NO_2$ в течение дня для всех станций. Другими словами, каково среднее значение для каждого часа дня?

# +
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
    kind="bar", rot=0, ax=axs
)

plt.xlabel("Hour of the day")
# произвольная метка для оси x
plt.ylabel("$NO_2 (µg/m^3)$");
# -

# Как и в предыдущем случае, мы хотим вычислить данную статистику (например, среднее $NO_2$) для каждого часа дня, мы снова можем использовать [groupby метод разделения-применения-объединения](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html). 

# ### Datetime как индекс 

# В блокноте [Как изменить раскладку таблиц](http://dfedorov.spb.ru/pandas/) [`pivot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot.html#pandas.pivot) использовался, чтобы изменить таблицу данных с каждым из мест измерения в качестве отдельной колонки:

no_2 = air_quality.pivot(index="datetime", columns="location", values="value")

no_2.head()

# Поворачивая данные, информация о дате и времени стала индексом таблицы. Установка столбца в качестве индекса может быть достигнута функцией [`set_index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html).

# Работа с индексом `datetime` (т.е. `DatetimeIndex`) обеспечивает мощные возможности. Например, нам не нужен метод `dt` для получения свойств временного ряда, но эти свойства доступны непосредственно в индексе:

no_2.index = pd.to_datetime(no_2.index)
no_2.index.year, no_2.index.weekday

# Существуют другие преимущества: удобное подмножество периода времени или адаптированный масштаб времени на графиках. Давайте применим это к нашим данным.

# Построим график показаний $NO_2$ на разных станциях с 20 мая до конца 21 мая:

no_2["2019-05-20":"2019-05-21"].plot()  # type: ignore

# Предоставляя строку, которая анализирует дату и время, можно выбрать конкретное подмножество данных в `DatetimeIndex`.

# Более подробная информация о `DatetimeIndex` приведена в [разделе, посвященном индексированию временных рядов](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-datetimeindex).

# ### Измените временной ряд на другую частоту

# Объедините текущие значения часовых временных рядов с максимальным месячным значением на каждой из станций с помощью метода [resample](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html).

monthly_max = no_2.resample("M").max()

monthly_max

# Очень мощный метод для временных рядов с индексом `datetime` - это возможность создавать повторную выборку [`resample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.resample.html#pandas.Series.resample) временных рядов с другой частотой (например, преобразовывать данные в секундах в данные за 5 минут).

# Метод [`resample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.resample.html#pandas.Series.resample) похож на операцию `GroupBy`:
#
# - он обеспечивает группировку на основе времени, используя строку (например `M`, `5H`...), что определяет целевую частоту
# - он требует функции агрегации, таких как `mean`, `max`...
#
# Обзор псевдонимов, используемых для определения частот временных рядов, приведен в [таблице обзора псевдонимов смещения](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases).

# Когда определено, частота временного ряда обеспечена атрибутом `freq`:

monthly_max.index = pd.to_datetime(monthly_max.index)
monthly_max.index.freq

# Постройте график ежедневной медианы значений $NO_2$ для каждой из станций.

no_2.resample("D").mean().plot(style="-o", figsize=(10, 5));

# Более подробная информация о силе временных рядов resampling приведена в разделе [инструкции пользователя на передискретизацию](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-resampling).

# Полный обзор временных рядов приведен на страницах, посвященных [временным рядам и функциям дат](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries).
