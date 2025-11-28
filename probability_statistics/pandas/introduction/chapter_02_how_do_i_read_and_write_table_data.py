"""How do I read and write table data?."""

# # Как мне читать и записывать табличные данные?

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/02_io_readwrite.svg" >
# </div>
#
# <a href="https://t.me/init_python"><img src="https://dfedorov.spb.ru/pandas/logo-telegram.png" width="35" height="35" alt="telegram" align="left"></a>

# Проведём анализ данных о пассажирах. Данные доступны в виде файла в формате CSV.

import pandas as pd

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"
# -

titanic = pd.read_csv(url)

# `Pandas` предоставляет функцию [`read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv) для чтения данных, хранящихся в виде CSV-файла, и преобразования их в `DataFrame`. 
#
# `Pandas` поддерживает множество различных форматов файлов или источников данных (`csv`, `excel`, `sql`, `json`…), каждый из которых имеет префикс `read_*`.

# В первую очередь, проверяйте данные после прочтения!
#
# При отображении DataFrame по умолчанию отображаются первые и последней 5 строк:

titanic

# Первые 8 строк DataFrame:

titanic.head(8)

# `pandas` содержит метод [`tail()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail) для отображения последних N строк. 
#
# Например, `titanic.tail(10)` вернет последние 10 строк таблицы.

# С помощью обращения к атрибуту `dtypes` можно проверить, какие типы данных хранятся в столбцах таблицы:

titanic.dtypes

# Типы данных в этом `DataFrame` - целые числа (`int64`), числа с плавающей точкой (`float63`) и строки (`object`).

# При запросе `dtypes` скобки не используются! `dtypes` является атрибутом `DataFrame` и `Series`. Атрибуты представляют собой характеристику `DataFrame` / `Series`, тогда как метод (для которого требуются скобки) что-то делает с `DataFrame` / `Series`. 

# Сохраним данные в виде электронной таблицы:

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

# В то время как `read_*` функции используются для чтения данных, `to_*` методы используются для сохранения данных. 
#
# [`to_excel()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel) сохраняет данные в виде файла `Excel`. 
#
# В приведенном примере `sheet_name` задает имя листа. При настройке `index=False` индексные метки не сохраняются в электронной таблице.

# Эквивалентная функция для чтения [`read_excel()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html#pandas.read_excel) загрузит данные в `DataFrame`:

titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

titanic.head()

# Техническом детали `DataFrame`:

titanic.info()

# Метод [`info()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info) предоставляет техническую информацию о `DataFrame`, поэтому объясним вывод более подробно:
#
# - Это действительно `DataFrame`.
# - Всего 891 запись, т.е. 891 строка.
# - У каждой строки есть метка строки (она же `index``) со значениями от 0 до 890.
# - Таблица имеет 12 столбцов. Большинство столбцов имеют значение для каждой из строк (все 891 значения `non-null`). Некоторые столбцы имеют пропущенные значения и менее 891 `non-null` значений.
# - Столбцы `Name`, `Sex`, `Cabin` и `Embarked` состоят из текстовых данных (`object`). Другие столбцы представляют собой числовые данные, некоторые из которых являются целыми числами (`integer`), а другие - действительными числами (`float`).
# - Тип данных (символы, целые числа, ...) в разных столбцах суммируется путем перечисления `dtypes`.
# - Приводится приблизительный объем оперативной памяти, используемой для хранения `DataFrame`.
