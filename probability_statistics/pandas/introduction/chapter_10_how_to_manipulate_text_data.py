"""How to manipulate text data?."""

# # Как манипулировать текстовыми данными?    

import pandas as pd

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"
# -

titanic = pd.read_csv(url)
titanic.head()

# Сделаем все имена символов строчными:

titanic["Name"].str.lower()

# Чтобы перевести каждую строку в столбце `Name` в нижний регистр, необходимо выбрать столбец `Name`, добавить метод `str` и применить метод [`lower`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.lower.html). Таким образом, каждая строка преобразуется поэлементно.

# Подобно объектам `datetime`, имеющим средство доступа `dt`, при использовании `str` доступно несколько специальных строковых методов. Эти методы имеют совпадающие имена с эквивалентными встроенными строковыми методами для отдельных элементов, но применяются поэлементно для каждого из значений столбцов.

# Создадим новый столбец `Surname`, содержащий фамилию пассажиров, извлекая часть перед запятой:

titanic["Name"].str.split(",")

# Используя метод [`Series.str.split()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html#pandas.Series.str.split), каждое из значений возвращается в виде списка из 2 элементов. Первый элемент - это часть перед запятой, а второй элемент - часть после запятой.

titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)

titanic["Surname"]

# Поскольку нас интересует только первая часть, представляющая фамилию (элемент `0`), мы можем снова использовать `str`  и применить метод [`Series.str.get()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.get.html#pandas.Series.str.get) для извлечения соответствующей части.

# Дополнительная информация об извлечении частей строк доступна в разделе [руководства пользователя по разделению и замене строк](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-split).

# Получим данные о графине на борту Титаника:

titanic["Name"].str.contains("Countess")

print(titanic[titanic["Name"].str.contains("Countess")])

# История в [Википедии](https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D1%8D%D0%BB%D1%8C_%D0%9B%D0%B5%D1%81%D0%BB%D0%B8,_%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BD%D1%8F_%D0%A0%D0%BE%D1%82%D0%B5%D1%81).
#
# <img src="https://m.media-amazon.com/images/M/MV5BZTMxZmY2YzYtNDNjOS00OGE0LWFjMjQtZGRkNGU3OGMyNTQzXkEyXkFqcGdeQXVyMTk4MzEzMDY@._V1_SY1000_CR0,0,676,1000_AL_.jpg" height="300px" width="200px" >
#
# На фото Люси Ноэль Марта Лесли, графиня Ротес, одна из выживших пассажиров затонувшего лайнера «Титаник»

# Строковый метод [`Series.str.contains()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains) проверяет каждое из значений в столбце, содержит ли строка слово `Countess` и возвращает `True` (если `Countess` является частью имени) или `False` (`Countess` не является частью имени). Полученные данные могут быть использованы для фильтрации с использованием условного (логического) индексирования. Поскольку на Титанике была только 1 графиня, в результате мы получаем один ряд.
#
# Методы [`Series.str.contains()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains) и [`Series.str.extract()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract) поддерживают механизм [`регулярных выражений`](https://docs.python.org/3/library/re.html).

# Дополнительная информация об извлечении частей строк доступна в разделе [руководства пользователя по сопоставлению и извлечению строк](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-extract).

# Определим, у какого пассажира самое длинное имя?

titanic["Name"].str.len()

# Чтобы получить самое длинное имя, сначала мы должны узнать длину каждого из имен в столбце `Name`, используя строковые методы `pandas`. Функция [`Series.str.len()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.len.html#pandas.Series.str.len) применяется к каждому имени отдельно (поэлементно).

titanic["Name"].str.len().idxmax()

# Затем необходимо получить соответствующее местоположение, желательно метку индекса в таблице, для которой длина имени самая большая. Метод [`idxmax()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html) не строковый, он применяется к целым числам, поэтому не используется `str`.

print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])

# Основываясь на индексном имени `row` (`307`) и столбце (`Name`), мы можем сделать выбор, используя оператор `loc`.Основываясь на индексном имени `row` (`307`) и столбце (`Name`), мы можем сделать выбор, используя оператор `loc`.

# В столбце `Sex` замените значения `male` на `M`, а `female` - на `F`.

titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})

titanic["Sex_short"]

# В `pandas` метод [`replace()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html#pandas.Series.replace) предоставляет удобный способ использования отображений или словарей для замены определенных значений.

# Полный обзор представлен на страницах [руководства пользователя по работе с текстовыми данными](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text).
