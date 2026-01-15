"""How to calculate summary statistics?."""

# # Как рассчитать сводную статистику?

import pandas as pd

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"
# -

titanic = pd.read_csv(url)
titanic

# ### Сводная статистика 

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/06_aggregate.svg" >
# </div>

# Каков средний возраст пассажиров?

titanic["Age"].mean()

# В `pandas` доступны различные статистические данные, которые могут быть применены к столбцам с числовыми значениями. 
#
# Операции исключают отсутствующие данные и по умолчанию работают со строками в таблице.

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/06_reduction.svg">
# </div>

# Каков средний возраст и стоимость билета для пассажиров?

titanic[["Age", "Fare"]].median()

# <img src="https://upload.wikimedia.org/wikipedia/commons/5/59/Titanic_surviving_officers.jpg" width="250" height="200">
# На фото четыре спасшихся во время крушения офицера "Титаника"

# Статистика, примененная к нескольким столбцам `DataFrame`, рассчитывается для каждого из числовых столбцов.

# Агрегирующая статистика может быть рассчитана для нескольких столбцов одновременно:

titanic[["Age", "Fare"]].describe()

# С помощью метода [`DataFrame.agg()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg) могут быть определены комбинации статистики для заданных столбцов:

titanic.agg(
    {"Age": ["min", "max", "median", "skew"], "Fare": ["min", "max", "median", "mean"]}
)

# Подробная информация об описательной статистике представлена в [разделе руководства пользователя по описательной статистике](https://pandas.pydata.org/docs/user_guide/basics.html?highlight=describe#descriptive-statistics).

# ### Агрегирование статистических данных, сгруппированных по категориям

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/06_groupby.svg">
# </div>

# Каков средний возраст мужчин и женщин пассажиров?

titanic[["Sex", "Age"]].groupby("Sex").mean()

# Поскольку интерес представляет средний возраст для каждого пола, сначала делается выборка по этим двум столбцам: `titanic[["Sex", "Age"]]`.
#
# Затем метод [`groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby) применяется к столбцу `Sex` для создания группы по категориям. 
#
# Затем рассчитывается и возвращается средний возраст для каждого пола.

# Вычисление заданной статистики (например, `mean` для возраста) для каждой категории в столбце (например, `male`/`female` в столбце `Sex`) является обычной моделью. Метод `groupby` используется для поддержки этого типа операций. В более общем плане это соответствует схеме `split-apply-combine`:
#
# - **Разделить** данные на группы
# - **Применить** функцию независимо к каждой группе 
# - **Объединить** результаты в структуру данных
#
# Этапы применения и объединения обычно выполняются в `pandas` вместе.
#
# В предыдущем примере мы сначала явно выбрали `2` столбца. Если нет, то метод `mean` применяется к каждому столбцу, содержащему числа:

# titanic.groupby("Sex").mean()
titanic.groupby("Sex").mean(numeric_only=True)

# Не имеет смысла получать среднее значение для столбца `Pclass` (тип каюты). 
#
# Если нас интересует только средний возраст для каждого пола, то выбор столбцов поддерживается и для сгруппированных данных:

titanic.groupby("Sex")["Age"].mean()

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/06_groupby_select_detail.svg" >
# </div>

# Столбец `Pclass` содержит числовые данные, но на самом деле представляет собой `3` категории (или фактора), соответственно метки `"1"`, `"2"` и `"3"`. Расчет статистики по ним не имеет большого смысла. 
# `pandas` предоставляет тип данных `Categorical` для обработки подобных значений. Более подробная информация представлена в руководстве пользователя в разделе [Категориальные данные](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#categorical).

# Какова средняя цена билета для каждой комбинации пола и типа каюты?

titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

# Группировка может выполняться по нескольким столбцам одновременно. Укажите имена столбцов в виде списка для метода [`groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby).

# Полное описание подхода разделения-применения-объединения приведено в разделе [руководства пользователя по групповым операциям](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby).

# ### Подсчитать количество записей по категориям

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/06_valuecounts.svg" >
# </div>

# Какое количество пассажиров в каждом из типов кают?

titanic["Pclass"].value_counts()

# Метод [`value_counts()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts) подсчитывает количество записей для каждой категории в колонке.

# На самом деле, за этой функцией скрывается групповая операция в сочетании с подсчетом количества записей в каждой группе:

titanic.groupby("Pclass")["Pclass"].count()

# <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/B-58.jpg" width="250" height="200">
#
# На фото каюта Титаника "В-58"

# В сочетании с `groupby` могут быть использованы `size` и `count`. 
#
# В то время как `size` включает в себя `NaN` значения и просто предоставляет количество строк (размер таблицы), `count` исключает отсутствующие значения. 
#
# В методе `value_counts` используйте `dropna` аргумент для включения или исключения `NaN` значений.

# *В* руководстве пользователя есть специальный раздел `value_counts`, см. [Страницу о дискретизации](https://pandas.pydata.org/docs/user_guide/basics.html#basics-discretization).

# Полное описание `подхода разделения-применения-объединения` приведено на страницах [руководства пользователя по групповым операциям](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby).
