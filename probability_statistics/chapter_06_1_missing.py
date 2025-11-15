"""Missing."""

# # Пропущенные значения

# +
import io
import os

import matplotlib.pyplot as plt

# импортируем библиотеку missingno с псевдонимом msno
import missingno as msno
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from dotenv import load_dotenv
from numpy.typing import ArrayLike

# в цикле пройдемся по датасетам с заполненными пропусками
# и списком названий соответствующих методов
from sklearn.base import accuracy_score

# создадим объект класса StandardScaler
# сделаем копию датасета
from sklearn.discriminant_analysis import StandardScaler

# создадим объект этого класса с параметрами:
# пять соседей и однаковым весом каждого из них
# fmt: off
# создадим объект класса SimpleImputer с параметром strategy = 'median'
# (для заполнения средним арифметическим используйте strategy = 'mean')
# сделаем копию датасета
# затем импортировать его
from sklearn.impute import IterativeImputer, KNNImputer, SimpleImputer

# теперь импортируем классы моделей, которые мы можем использовать в MICE
from sklearn.linear_model import LinearRegression, LogisticRegression

# from sklearn.ensemble import RandomForestRegressor

# предварительно нам нужно "включить" класс IterativeImputer,
# from sklearn.experimental import enable_iterative_imputer
# from sklearn.linear_model import BayesianRidge

# +
load_dotenv()

train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
response = requests.get(train_csv_url)

# импортируем датасет Титаник
titanic = pd.read_csv(io.BytesIO(response.content))
# -

# ## Выявление пропусков

# ### Базовые методы

# #### Метод `.info()`

# метод .info() соотносит максимальное количество записей
# с количеством записей в каждом столбце
titanic.info()

# +
# попробуем преобразовать Age в int
# titanic.Age.astype('int')
# -

# #### Методы `.isna()` и `.sum()`

# .isna() выдает True или 1, если есть пропуск,
# .sum() суммирует единицы по столбцам
titanic.isna().sum()

# пропущенные значения в процентах
print((titanic.isna().sum() / len(titanic)).round(4) * 100)

# ### Библиотека missingno

# сделаем стиль графиков seaborn основным
sns.set()

# #### Столбчатая диаграмма пропусков

msno.bar(titanic);

# #### Матрица пропущенных значений

msno.matrix(titanic);

# #### Матрица корреляции пропусков

# рассчитаем матрицу корреляции, когда известно в каких столбцах были пропуски
(titanic[["Age", "Cabin", "Embarked"]].isnull().corr())

# код для случаев, когда столбцы с пропусками неизвестны
df = titanic.iloc[
    :, [i for i, n in enumerate(np.var(titanic.isnull(), axis="rows")) if n > 0]
]
df.isnull().corr()  # type: ignore

msno.heatmap(titanic);

# ## Удаление пропусков

# ### Удаление строк

# удаление строк обозначим через axis = 'index'
# subset = ['Embarked'] говорит о том, что мы ищем пропуски только в столбце Embarked
titanic.dropna(axis="index", subset=["Embarked"], inplace=True)

# убедимся, что в Embarked действительно не осталось пропусков
titanic.Embarked.isna().sum()

# ### Удаление столбцов

# передадим в параметр columns тот столбец, который хотим удалить
titanic.drop(columns=["Cabin"], inplace=True)

# убедимся, что такого столбца больше нет
titanic.columns

# ### Pairwise deletion

# рассчитаем количество мужчик и женщин по каждому из признаков
sex_g = titanic.groupby("Sex").count()
sex_g

# сравним количество пассажиров в столбце Age и столбце PassengerId
# мы видим, что метод .count() игнорировал пропуски
print(sex_g["PassengerId"].sum(), sex_g["Age"].sum())

# метод .mean() также игнорирует пропуски и не выдает ошибки
titanic["Age"].mean()

# то же можно сказать про метод .corr()
titanic[["Age", "Fare"]].corr()

# ## Заполнение пропусков

# Подготовка данных

# +
train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
response = requests.get(train_csv_url)

# еще раз загрузим датасет "Титаник", в котором снова будут пропущенные значения
titanic = pd.read_csv(io.BytesIO(response.content))

# возьмем лишь некоторые из столбцов
titanic = titanic[["Pclass", "Sex", "SibSp", "Parch", "Fare", "Age", "Embarked"]]

# закодируем столбец Sex с помощью числовых значений
map_dict = {"male": 0, "female": 1}
titanic["Sex"] = titanic["Sex"].map(map_dict)

# посмотрим на результат
titanic.head()
# -

# ### Одномерные методы

# #### Заполнение константой

# Метод `.fillna()`

# Количественные данные

# +
# вначале сделаем копию датасета
fillna_const = titanic.copy()

# заполним пропуски в столбце Age нулями, передав методу .fillna() словарь,
# где ключами будут названия столбцов, а значениями - константы для заполнения пропусков
fillna_const.fillna({"Age": 0}, inplace=True)
# -

# посмотрим, как такое заполнение отразилось на данных
print(
    "titanic.Age.median():",
    titanic.Age.median(),
    " | fillna_const.Age.median():",
    fillna_const.Age.median(),
)

# Категориальные данные

# +
train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
response = requests.get(train_csv_url)

# найдем пассажиров с неизвестным портом посадки
# для этого создадим маску по столбцу Embarked и применим ее к исходным данным
missing_embarked = pd.read_csv(io.BytesIO(response.content))
print(missing_embarked[missing_embarked.Embarked.isnull()])
# -

# метод .fillna() можно применить к одному столбцу
# два пропущенных значения в столбце Embarked заполним буквой S (Southampton)
fillna_const["Embarked"] = fillna_const.Embarked.fillna("S")

# убедимся, что в столбцах Age и Embarked не осталось пропущенных значений
fillna_const[["Age", "Embarked"]].isna().sum()

# SimpleImputer

# +
const_imputer = titanic.copy()


# создадим объект этого класса, указав,
# что мы будем заполнять константой strategy = 'constant', а именно нулем fill_value = 0
imp_const = SimpleImputer(strategy="constant", fill_value=0)

# и обучим модель на столбце Age
# мы используем двойные скобки, потому что метод .fit() на вход принимает двумерный массив
imp_const.fit(const_imputer[["Age"]])

# +
# также используем двойные скобки с методом .transform()
const_imputer["Age"] = imp_const.transform(const_imputer[["Age"]])

# убедимся, что пропусков не осталось и посчитаем количество нулевых значений
print(
    "Пустых значений Age:",
    const_imputer.Age.isna().sum(),
    "| Кол-во замен на 0:",
    (const_imputer["Age"] == 0).sum(),
)

# +
# для дальнейшей работы столбец Embarked нам не понадобится, удалим его
const_imputer.drop(columns=["Embarked"], inplace=True)

# посмотрим на размер получившегося датафрейма
const_imputer.shape
# -

# посмотрим на результат
const_imputer.head(3)

# #### Заполнение средним арифметическим или медианой

# Метод `.fillna()`

# +
# fmt: off
# сделаем копию датафрейма
fillna_median = titanic.copy()

# заполним пропуски в столбце Age медианным значением возраста,
# можно заполнить и средним арифметическим через метод .mean()
fillna_median["Age"] = fillna_median["Age"].fillna(
    fillna_median["Age"].median()
)

# убедимся, что пропусков не осталось
fillna_median.Age.isna().sum()
# fmt: on
# -

# SimpleImputer

# +
# изменим размер последующих графиков
sns.set(rc={"figure.figsize": (10, 6)})

# скопируем датафрейм
median_imputer = titanic.copy()

# посмотрим на распределение возраста до заполнения пропусков
sns.histplot(median_imputer["Age"], bins=20)
plt.title("Распределение Age до заполнения пропусков");
# -

# посмотрим на среднее арифметическое и медиану
# median_imputer["Age"].mean().round(1), median_imputer["Age"].median()
print(round(median_imputer["Age"].mean(), 1), median_imputer["Age"].median())

# +
imp_median = SimpleImputer(strategy="median")

# применим метод .fit_transform() для одновременного обучения
# модели и заполнения пропусков
median_imputer["Age"] = imp_median.fit_transform(median_imputer[["Age"]])

# убедимся, что пропущенных значений не осталось
median_imputer.Age.isna().sum()
# fmt: on
# -

# посмотрим на распределение после заполнения пропусков
sns.histplot(median_imputer["Age"], bins=20)
plt.title("Распределение Age после заполнения медианой");

# посмотрим на метрики после заполнения медианой
# median_imputer["Age"].mean().round(1), median_imputer["Age"].median()
print(round(median_imputer["Age"].mean(), 1), median_imputer["Age"].median())

# +
# столбец Embarked нам опять же не понадобится
median_imputer.drop(columns=["Embarked"], inplace=True)

# посмотрим на размеры получившегося датафрейма
median_imputer.shape
# -

# #### Заполнение внутригрупповым значением

# скопируем датафрейм
median_imputer_bins = titanic.copy()

# выберем столбец 'Age'
# заполним пропуски в столбце 'Age', выполнив группировку по 'Sex','Pclass' и
# применив функцию 'median' через метод .transform()
median_imputer_bins["Age"] = median_imputer_bins["Age"].fillna(
    median_imputer_bins.groupby(["Sex", "Pclass"])["Age"].transform("median")
)

# проверим пропуски в столбце Age
median_imputer_bins.Age.isna().sum()

# +
# столбец Embarked нам опять же не понадобится
median_imputer_bins.drop(columns=["Embarked"], inplace=True)

# посмотрим на размеры получившегося датафрейма
median_imputer_bins.shape
# -

sns.histplot(median_imputer_bins["Age"], bins=20)
plt.title("Распределение Age после заполнения внутригрупповой медианой");

# #### Заполнение наиболее частотным значением

# +
# скопируем датафрейм
titanic_mode = titanic.copy()

# посмотрим на распределение пассажиров по порту посадки до заполнения пропусков
titanic_mode.groupby("Embarked")["Sex"].count()
# -

# создадим объект класса SimpleImputer с параметром strategy = 'most_frequent'
imp_most_freq = SimpleImputer(strategy="most_frequent")

# применим метод .fit_transform() к столбцу Embarked
titanic_mode["Embarked"] = imp_most_freq.fit_transform(
    titanic_mode[["Embarked"]]
).ravel()

# убедимся, что пропусков не осталось
titanic_mode.Embarked.isna().sum()

# проверим результат
# количество пассажиров в категории S должно увеличиться на два
titanic_mode.groupby("Embarked")["Sex"].count()

# найти моду можно также так
print(titanic.Embarked.value_counts().index[0])

# или так
imp_most_freq.statistics_

# для работы с последующими методами столбец Embarked нам уже не нужен
titanic.drop(columns=["Embarked"], inplace=True)

# ### Многомерные методы

# #### Линейная регрессия

# ##### Детерминированный подход

# Подготовка данных

# +
lr = titanic.copy()


# создаем объект этого класса
scaler = StandardScaler()

# применяем метод .fit_transform() и сразу помещаем результат в датафрейм
lr = pd.DataFrame(scaler.fit_transform(lr), columns=lr.columns)

# посмотрим на результат
lr.head(3)
# -

# поместим в датафрейм test те строки, в которых в столбце Age есть пропуски
test = lr[lr["Age"].isnull()].copy()
test.head(3)

# посмотрим на количество таких строк
test.shape

# +
# в train напротив окажутся те строки, где в Age пропусков нет
train = lr.dropna().copy()

# оценим их количество
train.shape
# -

# вместе train + test должны давать 891 строку
print(len(train) + len(test))

# +
# из датафрейма train выделим столбец Age, это будет наша целевая переменная
y_train = train["Age"]

# из датафрейма признаков столбец Age нужно удалить
X_train = train.drop("Age", axis=1)

# в test столбец Age в принципе не нужен
X_test = test.drop("Age", axis=1)
# -

# оценим результаты
X_train.head(3)

y_train.head(3)

X_test.head(3)

# Обучение модели и заполнение пропусков

# +
# создадим объект этого класса
lr_model = LinearRegression()

# обучим модель
lr_model.fit(X_train, y_train)

# применим обученную модель к данным, в которых были пропуски в столбце Age
y_pred = lr_model.predict(X_test)

# посмотрим на первые три прогнозных значения
y_pred[:3]
# -

# присоединим прогнозные значения возраста к датафрейму test
test["Age"] = y_pred
test.head(3)

# в train столбец Age присутствовал изначально
train.head(3)

# соединим датафреймы методом "один на другой"
lr = pd.concat([train, test])
lr.head(7)

# соединим датафреймы методом "один на другой"
lr = pd.concat([train, test])
lr.head(7)

# восстановим изначальный порядок строк, отсортировав их по индексу
lr.sort_index(inplace=True)
lr.head(7)

# +
# вернем исходный масштаб с помощью метода .inverse_transform()
lr = pd.DataFrame(scaler.inverse_transform(lr), columns=lr.columns)

# округлим столбец Age и выведем результат
lr.Age = lr.Age.round(1)
lr.head(7)
# -

# восстановив значение возраста первого наблюдения вручную
# (-0.530377 * titanic.Age.std() + titanic.Age.mean()).round()
round(-0.530377 * titanic.Age.std() + titanic.Age.mean())

# убедимся в отсутствии пропусков и посмотрим на размеры получившегося датафрейма
print("Пропусков в Age:", lr.Age.isna().sum(), "| Размер датафрейма:", lr.shape)

# посмотрим на распределение возраста после заполнения пропусков
sns.histplot(lr["Age"], bins=20)
plt.title("Распределение Age после заполнения с помощью линейной регрессии (дет.)");

# чтобы возраст был только положительным,
# установим минимальное значение на уровне 0,5
lr["Age"] = lr.Age.clip(lower=0.5)

# посмотрим, как изменились среднее арифметическое и медиана
print("Среднее Age:", lr.Age.mean().round(1), "| Медиана Age:", lr.Age.median())

# Особенность детерминированного подхода

# +
# fmt: off
# сделаем копию датафрейма, которую используем для визуализации
lr_viz = lr.copy()

# создадим столбец Age_type, в который запишем значение actual, 
# если индекс наблюдения есть в train,
# и imputed, если нет (т.е. он есть в test)
lr_viz["Age_type"] = np.where(
    lr.index.isin(train.index),
    "actual",
    "imputed",
)

# вновь "обрежем" нулевые значения
lr_viz["Age"] = lr_viz.Age.clip(lower=0.5)

# посмотрим на результат
lr_viz.head(7)
# fmt: on
# -

# создадим график, где по оси x будет индекс датафрейма,
# по оси y - возраст, а цветом мы обозначим изначальное это значение, или заполненное
sns.scatterplot(data=lr_viz, x=lr_viz.index, y="Age", hue="Age_type")
plt.title(
    "Распределение изначальных и заполненных значений (лин. регрессия, дет. подход)"
)
plt.xlabel("Наблюдения");

# рассчитаем СКО для исходных и заполненных значений
print(
    "STD actual:",
    np.round(lr_viz[lr_viz["Age_type"] == "actual"].Age.std(), 2),
    "| STD imputed:",
    np.round(lr_viz[lr_viz["Age_type"] == "imputed"].Age.std(), 2),
)

# ##### Стохастический подход

# +
# объявим функцию для создания гауссовского шума
# на входе эта функция будет принимать некоторый массив значений x,
# среднее значение mu, СКО std и точку отсчета для воспроизводимости результата


def gaussian_noise(
    x_var: ArrayLike, mu: float = 0.0, std: float = 1.0, random_state: int = 42
) -> np.ndarray:
    """Return values with added gaussian noise."""
    # вначале создадим объект, который позволит получать воспроизводимые результаты
    arr = np.asarray(x_var, dtype=np.float64)

    rs = np.random.RandomState(random_state)

    # применим метод .normal() к этому объекту для создания гауссовского шума
    noise = rs.normal(mu, std, size=arr.shape)

    # добавим шум к исходному массиву
    result: np.ndarray = arr + noise
    return result


# +
# заменим заполненные значения теми же значениями, но с добавлением шума
test["Age"] = gaussian_noise(x_var=test["Age"])

# посмотрим, как изменились заполненные значения
test.head(3)

# +
# fmt: off
# соединим датасеты и обновим индекс
lr_stochastic = pd.concat([train, test])
lr_stochastic.sort_index(inplace=True)

# вернем исходный масштаб с помощью метода .inverse_transform()
lr_stochastic = pd.DataFrame(
    scaler.inverse_transform(lr_stochastic),
    columns=lr_stochastic.columns
)

# округлим столбец Age и выведем результат
lr_stochastic.Age = lr_stochastic.Age.round(1)
lr_stochastic.head(7)
# fmt: on
# -

# посмотрим на распределение возраста
# после заполнения пропусков с помощью стохастического подхода
sns.histplot(lr_stochastic["Age"], bins=20)
plt.title("Распределение Age после заполнения с помощью линейной регрессии (стох.)");

# обрежем нулевые и отрицательные значения
lr_stochastic["Age"] = lr_stochastic.Age.clip(lower=0.5)

# посмотрим на среднее арифметическое и медиану
print(lr_stochastic.Age.mean().round(1), lr_stochastic.Age.median())

# +
# сделаем копию датафрейма, которую используем для визуализации
lr_st_viz = lr_stochastic.copy()

# создадим столбец Age_type, в который запишем actual, если индекс
# наблюдения # есть в train, и imputed, если нет (т.е. он есть в test)
lr_st_viz["Age_type"] = np.where(
    lr_stochastic.index.isin(train.index), "actual", "imputed"
)

# вновь "обрежем" нулевые значения
lr_st_viz["Age"] = lr_st_viz.Age.clip(lower=0.5)

# создадим график, где по оси x будет индекс датафрейма,
# по оси y - возраст, а цветом мы обозначим изначальное это значение, или заполненное
sns.scatterplot(data=lr_st_viz, x=lr_st_viz.index, y="Age", hue="Age_type")
plt.title(
    "Распределение изначальных и заполненных значений (лин. регрессия, стох. подход)"
)
plt.xlabel("Наблюдения");
# -

# рассчитаем СКО для исходных и заполненных значений
print(
    np.round(lr_st_viz[lr_st_viz["Age_type"] == "actual"].Age.std(), 2),
    np.round(lr_st_viz[lr_st_viz["Age_type"] == "imputed"].Age.std(), 2),
)

# #### MICE / IterativeImputer

# сделаем копию датасета для работы с методом MICE
mice = titanic.copy()

# +
scaler = StandardScaler()

# стандартизируем данные и сразу поместим их в датафрейм
mice = pd.DataFrame(scaler.fit_transform(mice), columns=mice.columns)

# +
# создадим объект класса IterativeImputer и укажем необходимые параметры
mice_imputer = IterativeImputer(
    initial_strategy="mean",  # вначале заполним пропуски средним значением
    estimator=LinearRegression(),  # в качестве модели используем линейную регрессию
    random_state=42,  # добавим точку отсчета
)

# используем метод .fit_transform() для заполнения пропусков в датасете mice
mice = mice_imputer.fit_transform(mice)

# вернем данные к исходному масштабу и округлим столбец Age
mice = pd.DataFrame(scaler.inverse_transform(mice), columns=titanic.columns)
mice.Age = mice.Age.round(1)
mice.head(7)
# -

# убедимся, что пропусков не осталось
print(mice.Age.isna().sum(), mice.shape)

# посмотрим на гистограмму возраста после заполнения пропусков
sns.histplot(mice["Age"], bins=20)
plt.title("Распределение Age после заполнения с помощью MICE");

# обрежем нулевые и отрицательные значения
mice["Age"] = mice.Age.clip(lower=0.5)

# оценим среднее арифметическое и медиану
print(mice.Age.mean().round(1), mice.Age.median())

# сравним СКО исходного датасета и данных после алгоритма MICE
print(np.round(titanic.Age.std(), 2), np.round(mice.Age.std(), 2))

# #### KNN Imputation

# ##### Sklearn KNNImputer

# +
# сделаем копию датафрейма
knn = titanic.copy()

# создадим объект класса StandardScaler
scaler = StandardScaler()

# масштабируем данные и сразу преобразуем их обратно в датафрейм
knn = pd.DataFrame(scaler.fit_transform(knn), columns=knn.columns)

# +
knn_imputer = KNNImputer(n_neighbors=5, weights="uniform")

# заполним пропуски в столбце Age
knn = pd.DataFrame(knn_imputer.fit_transform(knn), columns=knn.columns)

# проверим отсутствие пропусков и размеры получившегося датафрейма
print(knn.Age.isna().sum(), knn.shape)

# +
# вернем исходный масштаб
knn = pd.DataFrame(scaler.inverse_transform(knn), columns=knn.columns)

# округлим значение возраста
knn.Age = knn.Age.round(1)

# посмотрим на результат
knn.head(7)
# -

# посмотрим на распределение возраста после заполнения пропусков
sns.histplot(knn["Age"], bins=20)
plt.title("Распределение Age после заполнения с помощью KNNImputer");

# #### Сравнение методов

# +
# создадим два списка, в первый поместим датасеты с заполненными значениями
datasets = [
    const_imputer,
    median_imputer,
    median_imputer_bins,
    lr,
    lr_stochastic,
    mice,
    knn,
]

# во второй, названия методов
methods = [
    "constant",
    "median",
    "binned median",
    "linear regression",
    "stochastic linear regression",
    "MICE",
    "KNNImputer",
]

# +
train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
response = requests.get(train_csv_url)

# возьмем целевую переменную из исходного файла
y_var = pd.read_csv(io.BytesIO(response.content))["Survived"]
# -

for X_smpl, method in zip(datasets, methods):

    # масштабируем признаки
    X_smpl = StandardScaler().fit_transform(X_smpl)

    # для каждого датасета построим и обучим модель логистической регрессии
    model = LogisticRegression()
    model.fit(X_smpl, y_var)

    # сделаем прогноз
    y_pred = model.predict(X_smpl)

    # выведем название использованного метода и достигнутую точность
    print(f"Method: {method}, accuracy: {np.round(accuracy_score(y_var, y_pred), 3)}")

# ## Ответы на вопросы

# **Вопрос**. Что делать, если пропуски заполнены каким-либо символом, а не NaN? Например, знаком вопроса.

# +
df_smpl: pd.DataFrame = pd.DataFrame([[1, 2, 3], ["?", 5, 6], [7, "?", 9]])

df_smpl
# -

df[df == "?"] = np.nan
df
