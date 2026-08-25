"""Data cleaning and preparation."""

# # Очистка и подготовка данных

# Путь к данным из Титаника:

# +
# pylint: disable=line-too-long
import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"
# -

# Перевод данных из .csv в DataFrame:

df = pd.read_csv(url)
df.head(3)

df.info()

# Удаляем лишние столбцы:

df.drop(["PassengerId", "Name", "Ticket"], axis=1, inplace=True)

df.head(3)

# Округляем стоимость билета до двух знаков после запятой (так красиво):

df["Fare"] = round(df["Fare"], 2)

df.head(3)

# Определяем проблемные столбцы (обратите внимание на большое число пропусков в столбце Age):

df.isna().sum()

# Можно настраивать и изменять способ удаления данных, например с помощью параметра thresh=2, который оставит строки с более, чем с 2 непустыми значениями:

# +
# df.dropna()
#
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
# -

# # Что делать с пропусками?

# ## Что делать с пропусками?
# Способ 1

# Заменить пропущенные значения на константу (в данном случае нам он не подходит):

# +
# df['Age'].fillna(25)
# -

# ## Способ 2

# Заменить пропущенные значения на cреднее арифметическее по столбцу:

df["Age"].fillna(df["Age"].mean())

# ## Способ 3

#
# Заменить пропущенные значения на среднее арифметические в зависимости от класса каюты (Pclass).
#
# Вычисляем среднее арифметические в зависимости от класса каюты:

df.query("Pclass == 1").Age.mean()

df.sample(15)


# Пишем функцию, которая принимает на входе строку и просматривает необходимые столбцы:

def fill_age(row: pd.Series) -> float:  # type: ignore
    """Заполняет пропущенный возраст среднего возраста пассажиров."""
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:  # type: ignore[unreachable]
            return df.query("Pclass == 1")["Age"].mean()
        if row["Pclass"] == 2:
            return df.query("Pclass == 2")["Age"].mean()
        if row["Pclass"] == 3:
            return df.query("Pclass == 3")["Age"].mean()
    return row["Age"]  # type: ignore[unreachable]


# Самый важный момент - применение функции `apply`, которая заполняет пропущенные значения указанными в функции fill_age:

df.apply(fill_age, axis="columns")

# ## Способ 4

# Эквивалентен способу 3, но менее очевиден и более короткий:

df.groupby("Pclass", group_keys=True)["Age"].apply(lambda x: x.fillna(x.mean()))

# Проверяем эквивалентность способовов 3 и 4:

(df.apply(fill_age, axis=1)).equals(
    df.groupby("Pclass", group_keys=True)["Age"].apply(lambda x: x.fillna(x.mean()))
)


# # Создаем новый столбец с информацией о том, был ли пассажир на борту один или с родственниками

# Столбец должен содержать значение "alone", если он был на борту один (без супруга/супруги, братьев, сестер, детей и родителей) и значение "not alone", если пассажир путешествовал с кем-то из родственников.
#
# - SibSp - Количество братьев и сестер / супругов на борту
# - Parch - число родителей / детей на борту

# ## Способ 1:
# с помощью функции и apply:

# +
def alone_check(row: pd.Series) -> str:  # type: ignore
    """Определяет, путешествует ли пассажир один."""
    if row["SibSp"] > 0 or row["Parch"] > 0:
        return "not_alone"
    return "alone"


df["Alone"] = df.apply(alone_check, axis=1)
# -

# ## Способ 2
# с помощью lambda-функции:

df["Alone"] = df.apply(
    lambda x: "not_alone" if x["SibSp"] or x["Parch"] > 0 else "alone", axis=1
)
df
