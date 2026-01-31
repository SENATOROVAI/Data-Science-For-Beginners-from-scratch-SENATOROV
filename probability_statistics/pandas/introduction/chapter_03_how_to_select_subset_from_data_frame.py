"""How to select a subset from a DataFrame?."""

# # Как выбрать подмножество из DataFrame?

import pandas as pd

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"
# -

titanic = pd.read_csv(url)

# ### Как выбрать определенные столбцы из DataFrame?

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/03_subset_columns.svg">
# </div>

# Меня интересует возраст пассажиров:

ages = titanic["Age"]
ages

# Чтобы выбрать один столбец, используйте квадратные скобки `[]` с именем интересующего столбца.

# Каждый столбец в [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) является [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series). 
#
# Поскольку выбран один столбец, то возвращаемый объект является `Series`. 
#
# Мы можем проверить это:

type(titanic["Age"])

# Посмотрим на результат обращения к атрибуту `shape`:

titanic["Age"].shape

# [`DataFrame.shape`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape) является атрибутом `Series` и `DataFrame` и содержит количество строк и столбцов `(nrows, ncolumns)`. 
#
# Серия является одномерной, поэтому возвращается только количество строк.

# Меня интересует возраст и пол пассажиров:

age_sex = titanic[["Age", "Sex"]]

age_sex.head()

# Чтобы выбрать несколько столбцов, используйте список имен столбцов в квадратных скобках `[]`.

# Внутренние квадратные скобки определяют [список Python](https://docs.python.org/3/tutorial/datastructures.html#tut-morelists) с именами столбцов, тогда как внешние квадратные скобки используются для выбора данных.

# Возвращаемый тип данных - `DataFrame`:

type(titanic[["Age", "Sex"]])

titanic[["Age", "Sex"]].shape

# Видим, что `DataFrame` содержит 891 строк и 2 столбца. 

# Для получения информации об индексации см. [Раздел руководства пользователя по индексированию и выбору данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-basics).

# ### Как отфильтровать определенные строки из DataFrame?
#
# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/03_subset_rows.svg">
# </div>

# Меня интересуют пассажиры старше 35 лет:

above_35 = titanic[titanic["Age"] > 35]

above_35.head()

# Условие внутри скобок проверяет, для каких строк столбец имеет значение больше 35:

titanic["Age"] > 35

# Вывод условного выражения (`>`, но также будут работать `==`, `!=`, `<`, `<=`, ... ) является `Series` булевых значений (`True` или `False`) с тем же числом строк, что и в оригинальном `DataFrame`. 
#
# Подобный `Series` может быть использован для фильтрации `DataFrame`, помещая его внутрь скобок выбора `[]`. 
#
# Будут выбраны только те строки, для которых это значение `True`.
#
# Давайте посмотрим на количество строк, которые удовлетворяют условию, проверив атрибут `shape` полученного `DataFrame`:

above_35.shape

# Меня интересуют пассажиры из кают класса `2` и `3`:

class_23 = titanic[titanic["Pclass"].isin([2, 3])]

# Подобно условному выражению, [`isin()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin) возвращает `True` для каждой строки, значения которой находятся в предоставленном списке. 
#
# Чтобы отфильтровать строки на основе такой функции, используйте функцию внутри скобок `[]`. 
#
# Вышесказанное эквивалентно фильтрации по строкам, для которых класс равен `2` или `3`, и объединению двух операторов с помощью (или) `|` :

class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]

class_23.head()

# См. Специальный раздел в [руководстве пользователя о булевой индексации](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-boolean).

# Я хочу работать с данными о пассажирах, для которых известен возраст:

age_no_na = titanic[titanic["Age"].notna()]

age_no_na.head()

# [`notna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.notna.html#pandas.Series.notna) возвращает `True` для каждой строки, значение которой отлично от `NA` (`np.NaN`). 

# Проверим, изменилась ли форма:

age_no_na.shape

# ### Как выбрать определенные строки и столбцы из DataFrame?

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/03_subset_columns_rows.svg">
# </div>

# Меня интересуют имена пассажиров старше `35` лет:

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

adult_names.head()

# В этом случае подмножество строк и столбцов создается за один раз, и просто использование скобок выбора `[]` больше не достаточно. 
#
# Операторы `loc` / `iloc` требуются перед скобками`[]`. 
#
# При использовании `loc` / `iloc` часть перед запятой - это строки, которые вы хотите выбрать, а часть после запятой - это столбцы.

# При использовании имен столбцов, меток строк или условных выражений используйте оператор `loc` перед скобками выбора `[]`. 
#
# Как для части до, так и после запятой можно использовать одну метку, список меток, часть меток, условное выражение или двоеточие. 
#
# Используя особенности двоеточия, если хотите выбрать все строки или столбцы.

# Меня интересуют строки с `9` по `24` и столбцы с `2` по `4`:

titanic.iloc[9:25, 2:5]

# Опять же, подмножество строк и столбцов создается за один раз, и просто использование скобок выбора `[]` больше не достаточно. 
#
# Если вас интересуют определенные строки и/или столбцы в зависимости от их положения в таблице, используйте оператор `iloc` перед `[]`.

# При выборе определенных строк и/или столбцов с помощью `loc` или `iloc`, новым значениям могут быть назначены выбранные данные. 
#
# Например, чтобы присвоить имя anonymous первым `3` элементам третьего столбца:

titanic.iloc[0:3, 3] = "anonymous"

titanic.head()

# Обратитесь к разделу [руководства пользователя по различным вариантам индексации](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-choice), чтобы получить более полное представление об использовании `loc` и `iloc`.

# Полный обзор индексации представлен в [руководстве пользователя по индексированию и выбору данных](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing).
