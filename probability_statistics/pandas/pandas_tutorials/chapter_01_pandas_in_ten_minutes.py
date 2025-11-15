"""Pandas in ten minutes."""

# # Pandas за десять минут

# Это короткое введение в мир pandas, ориентированное в основном на новых пользователей. Более сложные рецепты можно найти в [Поваренной книге](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook).

# Обычно импорт выглядит так и к нему все привыкли:

import numpy as np
import pandas as pd

# ## Создание объекта

# Подробнее см. [Введение в структуры данных pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dsintro)

# Создание `Серии` ([`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series)) путем передачи питоновского списка позволет pandas создать целочисленный индекс по умолчанию:

s_var = pd.Series([1, 3, 5, np.nan, 6, 8])
s_var

# Создание `Кадра данных` ([`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame)) путем передачи массива NumPy с временнЫм индексом и помеченными столбцами:

# указываем начало временнОго периода и число повторений (дни по умолчанию)
dates = pd.date_range("20130101", periods=6)
dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

# Создать [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) можно путем передачи питоновского словаря объектов, которые можно преобразовать в серию.

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),  # временнАя метка
        "C": pd.Series(
            1, index=list(range(4)), dtype="float32"
        ),  # Серия на основе списка
        "D": np.array([3] * 4, dtype="int32"),  # массив целых чисел NumPy
        "E": pd.Categorical(["test", "train", "test", "train"]),  # категории
        "F": "foo",
    }
)
df2

# Столбцы итогового [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) имеют разные [типы данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes).

df2.dtypes

# Столбцы итогового [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) имеют разные [типы данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes).

df2.dtypes

# Если вы используете `IPython` или `Jupyter (Lab) Notebook (Colab)`, то по нажатию TAB после точки отобразятся публичные атрибуты объекта (в данном случае `DataFrame`): 

# +
# Попробуйте убрать комментарий и нажать TAB
# df2.<TAB>
# -

# ## Просмотр данных

# Подробнее см. [Документацию по базовой функциональности](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics).

# Просмотрим верхние и нижние строки полученного кадра данных:

df.head()

df.tail(3)  # вывести последние три строки

# Отобразим индекс и столбцы:

df.index

df.columns

# Метод [`DataFrame.to_numpy()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy) представляет данные в виде массива NumPy, на котором строится DataFrame. 

df.to_numpy()

# Обратите внимание, что эта операция может занять много времени, если ваш `DataFrame` имеет столбцы с разными типами данных, что сводится к фундаментальному различию между pandas и `NumPy`: массивы `NumPy` имеют один тип данных для всего массива, тогда как `DataFrames` в pandas имеет один тип данных для каждого столбца. Когда вы вызываете `DataFrame.to_numpy()`, pandas определит тип данных `NumPy`, который может содержать все типы данных `DataFrame`. Этот тип данных может в конечном итоге оказаться объектом (`object`, т.е. строкой), что потребует приведения каждого значения к объекту Python.
#
# Наш `DataFrame` содержит значения с плавающей точкой, поэтому `DataFrame.to_numpy()` сработает быстро и не требует копирования данных.

# Для df2, который содержит несколько типов данных, вызов `DataFrame.to_numpy()` является относительно дорогостоящим:

df2.to_numpy()

# Обратите внимание, что `DataFrame.to_numpy()` не включает в вывод метки индекса или столбцов.

# Метод [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe) показывает краткую статистическую сводку для данных:

df.describe()

#
# Транспонируем данные:

df.T

# Сортировка по столбцам, см. [`sort_index()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html):

df.sort_index(
    axis=1, ascending=False
)  # по умолчанию axis=0, т.е. сортировка по строкам

# Сортировка по значениям, см. [`sort_values()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values):

df.sort_values(by="B")  # по умолчанию сортировка по индексу, выбрали столбец 'B'
