"""How to change the table layout?."""

# # Как изменить раскладку таблиц?

import pandas as pd

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"
# -

titanic = pd.read_csv(url)
titanic.head()

# <img src="http://loveopium.ru/content/2012/04/titanic/06.jpg" width="250" height="200">

# ### Сортировать строки таблицы

# Я хочу отсортировать данные по возрасту пассажиров:

titanic.sort_values(by="Age").head()

# Я хочу отсортировать данные по классу каюты и возрасту в порядке убывания:

titanic.sort_values(by=["Pclass", "Age"], ascending=False).head()

# [`Series.sort_values()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values) приводит к тому, что строки в таблице сортируются в соответствии с определенными столбцами. Индекс будет следовать порядку строк.

# Более подробная информация о сортировке таблиц приведена в разделе [руководства по использованию для сортировки данных](https://pandas.pydata.org/docs/user_guide/basics.html#basics-sorting).

# ### Перевод таблицы из длинного формата в широкий  

# Этот блокнот использует данные о содержании в воздухе $NO_2$ и твердых частиц размером менее 2,5 микрометров, предоставленные организацией [`openaq`](https://openaq.org/) и использующие модуль [`py-openaq`](http://dhhagan.github.io/py-openaq/index.html). 
#
# см. [Частицы РМ2.5: что это, откуда и почему об этом все говорят](https://habr.com/ru/company/tion/blog/396111/)
#
# см. [Города и взвеси: концентрация вредных частиц в Москве повысилась](https://iz.ru/825489/vitalii-volovatov/goroda-i-vzvesi-kontcentratciia-vrednykh-chastitc-v-moskve-povysilas)
#
# Набор данных `air_quality_long.csv` содержит значения $NO_2$ и $PM_{2.5}$ для измерительных станций `FR04014`, `BETR801` и `London Westminster` соответственно в Париже, Антверпене и Лондоне.
#
# Набор данных о качестве воздуха имеет следующие столбцы:
#
# - *city*: город, в котором используется датчик (Париж, Антверпен или Лондон)
# - *country*: страна, в которой используется датчик (FR, BE или GB)
# - *location*: идентификатор датчика (FR04014 , BETR801 или Лондон Вестминстер)
# - *parameter*: параметр, измеряемый датчиком ($NO_2$ или твердые частицы)
# - *value*: измеренное значение
# - *unit*: единица измеряемого параметра, в данном случае $мкг/м^3$ и индекс в виде datetime.
#
# Данные о качестве воздуха предоставляются в длинном формате (`long format`), где каждое наблюдение находится в отдельной строке, а каждая переменная - в отдельном столбце таблицы данных. `long/narrow` формат также известен как [формат аккуратных данных (`tidy data format`)](https://www.jstatsoft.org/article/view/v059i10).

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_long.csv"
# -

air_quality = pd.read_csv(url, index_col="date.utc", parse_dates=True)
air_quality.head()

# Давайте использовать небольшое подмножество данных о качестве воздуха. Мы ориентируемся на данные $NO_2$ и используем только первые два измерения каждого местоположения (т.е. заголовок каждой группы). Подмножество данных будет называться `no2_subset`:

# filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# +
# use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html
# -

no2_subset

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/07_pivot.svg" >
# </div>

# Функция [`pivot_table()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html#pandas.pivot_table) изменяет форму данных: требуется одно значение для каждой комбинации индекса/столбца.

# Я хочу, чтобы значения для трех станций были отдельными столбцами рядом друг с другом.

no2_subset.pivot(columns="location", values="value")

# Поскольку `pandas` поддерживает построение графика для нескольких столбцов, преобразование из длинного (`long`) формата таблицы в широкий (`wide`) позволяет одновременно отображать различные временные ряды:

no2.head()

no2.pivot(columns="location", values="value").plot();

# Если параметр `index` не определен, используется существующий индекс (метки строк).

# Для получения дополнительной информации о функции [`pivot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot) см. [Раздел руководства пользователя по повороту объектов DataFrame](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-reshaping).

# ### Сводная таблица

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/07_pivot_table.svg">
# </div>

# Я хочу узнать среднюю концентрацию $NO_2$ и $PM_{2.5}$ для каждой из станций в виде таблицы:

air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)

# В случае [`pivot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot) данные только переставляются. 
#
# Когда необходимо агрегировать несколько значений (в данном конкретном случае значения на разных временных шагах) [`pivot_table()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table) предоставляет функцию агрегации (например, `mean`), объединяющую эти значения.

# Сводная таблица является хорошо известной концепцией в программах для работы с электронными таблицами. Если вас интересуют сводные столбцы для каждой переменной в отдельности, задайте параметр `margins=True`:

air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean", margins=True
)

# Для получения дополнительной информации о [`pivot_table()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table) см. [Раздел руководства пользователя по сводным таблицам](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-pivot).

# [`pivot_table()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table) напрямую связан с [`groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby). Тот же результат может быть получен путем группировки `parameter` и `location`:
# ```Python
# air_quality.groupby(["parameter", "location"]).mean()
# ```

# Посмотрите [`groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby) в сочетании с [`unstack()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack) в [руководстве пользователя](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-combine-with-groupby).

# ### От широкого к длинному формату

# Начинем с широкоформатной (`wide`) таблицы, созданной в предыдущем разделе:

# +
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
# -

no2_pivoted.head()

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/07_melt.svg" >
# </div>

# Я хочу собрать все измерения качества воздуха $NO_2$  в одном столбце (`long format`):

no_2 = no2_pivoted.melt(id_vars="date.utc")

no_2.head()

# Метод [`pandas.melt()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html#pandas.melt) преобразует таблицу данных из широкого формата в длинный формат. Заголовки столбцов становятся именами переменных во вновь созданном столбце.
#
# <img src="https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D1%81%D0%BB%D0%BE%D0%B6%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D0%BC%D1%8B%20pandas/pic/melt.png">

# Решение является краткой версией применения [`pandas.melt()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html#pandas.melt). Метод будет растворять все столбцы, не упомянутые в `id_vars` вместе в две колонки: колонки `A` с именами заголовков столбцов и столбца с самим значениями. Последний столбец получает имя по умолчанию `value`.
#
# Метод `pandas.melt()` более подробно:

no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)

no_2.head()

# Результат такой же, но более детально определенный:
#
# - `value_vars` - четко определяет, какие столбцы смешивать вместе;
# - `value_name` - предоставляет настраиваемое имя столбца для столбца значений вместо имени столбца по умолчанию `value`;
# - `var_name` - предоставляет настраиваемое имя столбца для столбцов, собирающих имена заголовков столбцов. В противном случае он принимает имя индекса или значение по умолчанию `variable`.
#
# Следовательно, аргументы `value_name` и `var_name` являются просто пользовательскими именами для двух сгенерированных столбцов. Столбцы для растворения определяются параметрами `id_vars` и `value_vars`.

# Преобразование из широкого формата в длинный с `pandas.melt()` объясняется в разделе [руководства пользователя по изменению формы расплавом](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-melt).

# Полный обзор доступен в [руководстве пользователя на страницах об изменении формы и повороте](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping).
