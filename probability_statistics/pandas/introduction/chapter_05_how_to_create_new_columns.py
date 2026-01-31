"""How to create new columns?."""

# # Как создать новые столбцы?

import pandas as pd

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/air_quality_no2.csv"
# -

air_quality = pd.read_csv(url, index_col=0, parse_dates=True)
air_quality.head()

# ### Как создать новые столбцы, полученные из существующих столбцов?

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/pandas-docs/stable/_images/05_newcolumn_1.svg">
# </div>

# Я хочу выразить концентрацию $NO_2$ в Лондоне в $мг/м^3$. Если мы примем температуру 25 градусов по Цельсию и давление `1013 гПа`, то коэффициент преобразования составит `1,882`.

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

air_quality.head()

# Чтобы создать новый столбец, используйте скобки `[]` с новым именем столбца в левой части присваивания.

# Расчет значений осуществляется по элементам. Это означает, что все значения в данном столбце умножаются на `1.882` за один раз. Вам не нужно использовать цикл для итерации по каждой строке!

# <div style="background-color: #ffffff; padding: 20px; text-align: center;">
#     <img src="https://pandas.pydata.org/docs/_images/05_newcolumn_2.svg">
# </div>

# Я хочу проверить соотношение значений в Париже и Антверпене и сохранить результат в новом столбце:

air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)

air_quality.head()

# Расчет снова поэлементный, поэтому `/` применяется в каждой строки.

# Также другие математические операторы (`+`, `-`, `*`, `/`) или логические операторы (`<`, `>`, `=`, …) работают по элементам. 

# Я хочу переименовать столбцы данных в соответствующие идентификаторы станций, используемые сообществом openAQ.

air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

air_quality_renamed.head()

# Функция [`rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename) может быть использована как для меток строк и названий столбцов.

# Отображение не должно ограничиваться только фиксированными именами, но может быть функцией отображения.
#
# Например, преобразование имен столбцов в строчные буквы также можно выполнить с помощью функции:

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)

air_quality_renamed.head()

# Подробная информация о [переименовании меток](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename) столбцов или строк приведена в разделе руководства пользователя по [переименованию меток](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename).

# Руководство пользователя содержит отдельный раздел о [добавлении и удалении столбцов](https://pandas.pydata.org/docs/user_guide/dsintro.html#basics-dataframe-sel-add-del).
