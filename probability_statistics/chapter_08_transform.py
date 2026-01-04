"""Transformation of quantitative data."""

# # Преобразование количественных данных

# +
# pylint: disable=too-many-lines

import io
import os
import time

# напишем простой encoder
# будем передавать в функцию данные, столбец, который нужно кодировать,
# и схему кодирования (map)
import joblib
import matplotlib.pyplot as plt

# импортируем библиотеки
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from dotenv import load_dotenv
from joblib import Parallel, delayed

# fmt: off
from pandas import DataFrame

# создадим матрицу в формате сжатого хранения строкой
from scipy.sparse import csr_matrix

# рассчитаем предпоследнее значение с помощью библиотеки scipy
# построим графики нормальной вероятности
# импортируем необходимые функции
from scipy.stats import kurtosis, norm, probplot, skew
from sklearn.compose import ColumnTransformer

# импортируем данные о недвижимости в Калифорнии
from sklearn.datasets import fetch_california_housing

# создадим объекты преобразователей для количественных
from sklearn.impute import SimpleImputer

# создадим объект модели, которая будет использовать все признаки
# и создания модели линейной регрессии
from sklearn.linear_model import LinearRegression, LogisticRegression

# разделим данные на обучающую и тестовую выборки
from sklearn.model_selection import train_test_split

# ColumnTransformer позволяет применять разные преобразователи к разным столбцам
# импортируем класс Pipeline
# импортируем класс make_pipeline (упрощенный вариант класса Pipeline) из модуля pipeline
from sklearn.pipeline import Pipeline, make_pipeline

# выполним ту же операцию с помощью класса Normalizer
# применим MaxAbsScaler
# импортируем класс MinMaxScaler
# импортируем класс для стандартизации данных
# из модуля preprocessing импортируем класс StandardScaler
# наконец скачаем функцию степенного преобразования power_transform()
from sklearn.preprocessing import (
    FunctionTransformer,
    MaxAbsScaler,
    MinMaxScaler,
    Normalizer,
    OrdinalEncoder,
    PowerTransformer,
    QuantileTransformer,
    RobustScaler,
    StandardScaler,
    power_transform,
)

# и категориального признака
# -

# установим размер и стиль Seaborn для последующих графиков
sns.set(rc={"figure.figsize": (8, 5)})

# ### Подготовка данных

# +
load_dotenv()

boston_csv_url = os.environ.get("BOSTON_CSV_URL", "")
response = requests.get(boston_csv_url)

# возьмем признак LSTAT (процент населения с низким социальным статусом)
# и целевую переменную MEDV (медианная стоимость жилья)
boston = pd.read_csv(io.BytesIO(response.content))[["LSTAT", "MEDV"]]
boston.shape
# -

# посмотрим на данные с помощью гистограммы
boston.hist(bins=15, figsize=(10, 5));

# посмотрим на основные статистические показатели
boston.describe()

# #### Пример преобразований

# +
# создадим сетку подграфиков 1 x 3
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# на первом графике разместим изначальное распределение
sns.histplot(data=boston, x="LSTAT", bins=15, ax=ax[0])
ax[0].set_title("Изначальное распределение")

# на втором - данные после стандартизации
sns.histplot(
    x=(boston.LSTAT - np.mean(boston.LSTAT)) / np.std(boston.LSTAT),
    bins=15,
    color="green",
    ax=ax[1],
)
ax[1].set_title("Стандартизация")


# и на третьем графике покажем преобразование Бокса-Кокса
sns.histplot(
    x=power_transform(boston[["LSTAT"]], method="box-cox").flatten(),
    bins=12,
    color="orange",
    ax=ax[2],
)
ax[2].set(title="Степенное преобразование", xlabel="LSTAT")

plt.tight_layout()
plt.show()
# -

# #### Добавление выбросов

# +
# создадим два отличающихся наблюдения
outliers = pd.DataFrame({"LSTAT": [45, 50], "MEDV": [70, 72]})

# добавим их в исходный датафрейм
boston_outlier = pd.concat([boston, outliers], ignore_index=True)

# посмотрим на размерность нового датафрейма
boston_outlier.shape
# -

# убедимся, что наблюдения добавились
boston_outlier.tail()

# +
# fmt: off
# посмотрим на данные с выбросами и без
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

sns.scatterplot(
    data=boston, x='LSTAT', y='MEDV', ax=ax[0]
).set(title='Без выбросов')

sns.scatterplot(
    data=boston_outlier, x='LSTAT', y='MEDV', ax=ax[1]
).set(title='С выбросами')
# fmt: on
# -

# ## Линейные преобразования

# ### Стандартизация

# #### Стандартизация вручную

((boston - boston.mean()) / boston.std()).head(3)

# #### StandardScaler

# Преобразование данных

# создадим объект класса StandardScaler и применим метод .fit()
st_scaler = StandardScaler().fit(boston)
st_scaler

# в данном случае метод .fit() находит среднее арифметическое
st_scaler.mean_

# и СКО каждого столбца
st_scaler.scale_

# +
# метод .transform() возвращает массив Numpy с преобразованными значениями
boston_scaled = st_scaler.transform(boston)

# превратим массив в датафрейм с помощью функции pd.DataFrame()
pd.DataFrame(boston_scaled, columns=boston.columns).head(3)
# -

# метод .fit_transform() рассчитывает показатели среднего и СКО
# и одновременно преобразует данные
boston_scaled = pd.DataFrame(
    StandardScaler().fit_transform(boston), columns=boston.columns
)

boston_scaled.mean()

boston_scaled.std()

print(np.ptp(boston_scaled.LSTAT), np.ptp(boston_scaled.MEDV))

# аналогичным образом стандиртизируем данные с выбросами
boston_outlier_scaled = pd.DataFrame(
    StandardScaler().fit_transform(boston_outlier), columns=boston_outlier.columns
)

print(np.ptp(boston_outlier_scaled.LSTAT), np.ptp(boston_outlier_scaled.MEDV))

# Визуализация преобразования

# +
# первая функция будет принимать на вход четыре датафрейма
# и визуализировать изменения с помощью точечной диаграммы


def scatter_plots(
    df: DataFrame,
    df_outlier: DataFrame,
    df_scaled: DataFrame,
    df_outlier_scaled: DataFrame,
    title: str,
) -> None:
    """Create scatter plots to visualizion need."""
    fig_p, ax_2 = plt.subplots(2, 2, figsize=(12, 12))  # pylint: disable=W0612

    sns.scatterplot(data=df, x="LSTAT", y="MEDV", ax=ax_2[0, 0])
    ax_2[0, 0].set_title("Изначальный без выбросов")

    sns.scatterplot(data=df_outlier, x="LSTAT", y="MEDV", color="green", ax=ax_2[0, 1])
    ax_2[0, 1].set_title("Изначальный с выбросами")

    sns.scatterplot(data=df_scaled, x="LSTAT", y="MEDV", ax=ax_2[1, 0])
    ax_2[1, 0].set_title("Преобразование без выбросов")

    sns.scatterplot(
        data=df_outlier_scaled,
        x="LSTAT",
        y="MEDV",
        color="green",
        ax=ax_2[1, 1],
    )
    ax_2[1, 1].set_title("Преобразование с выбросами")

    plt.suptitle(title)
    plt.show()
    # fmt: on


# -

# fmt: off
# вторая функция будет визуализировать изменения с помощью гистограммы
def hist_plots(
    df: DataFrame,
    df_outlier: DataFrame,
    df_scaled: DataFrame,
    df_outlier_scaled: DataFrame,
    title: str,
) -> None:
    """Create histogram plots for visualizion purpose."""
    fig_s, ax_3 = plt.subplots(2, 2, figsize=(12, 12))  # pylint: disable=W0612

    sns.histplot(data=df, x="LSTAT", ax=ax_3[0, 0])
    ax_3[0, 0].set_title("Изначальный без выбросов")

    sns.histplot(data=df_outlier, x="LSTAT", color="green", ax=ax_3[0, 1])
    ax_3[0, 1].set_title("Изначальный с выбросами")

    sns.histplot(data=df_scaled, x="LSTAT", ax=ax_3[1, 0])
    ax_3[1, 0].set_title("Преобразование без выбросов")

    sns.histplot(
        data=df_outlier_scaled,
        x="LSTAT",
        color="green",
        ax=ax_3[1, 1],
    )
    ax_3[1, 1].set_title("Преобразование с выбросами")

    plt.suptitle(title)
    plt.show()
    # fmt: on


# применим эти функции
scatter_plots(
    boston,
    boston_outlier,
    boston_scaled,
    boston_outlier_scaled,
    title="Стандартизация данных",
)

hist_plots(boston,
           boston_outlier,
           boston_scaled,
           boston_outlier_scaled,
           title='Стандартизация данных')

# Обратное преобразование

# вернем исходный масштаб данных
boston_inverse = pd.DataFrame(st_scaler.inverse_transform(boston_scaled),
                              columns=boston.columns)

# используем метод .equals(), чтобы выяснить, одинаковы ли датафреймы
boston.equals(boston_inverse)

# вычтем значения одного датафрейма из значений другого
(boston - boston_inverse).head(3)

# оценить приблизительное равенство можно так
np.all(np.isclose(boston.to_numpy(), boston_inverse.to_numpy()))

# #### Проблема утечки данных

# +
# при return_X_y = True вместо объекта Bunch возвращаются признаки (X) 
# и целевая переменная (y)
# параметр as_frame = True возвращает датафрейм и Series вместо массивов 
# Numpy
a_var, b_var = fetch_california_housing(return_X_y=True, as_frame=True)

# убедимся, что данные в нужном нам формате
print(type(a_var), type(b_var))
# -

# посмотрим на признаки
a_var.head(3)

X_train, X_test, y_train, y_test = train_test_split(a_var, b_var,
                                                    random_state=42)

# создадим объект класса StandardScaler
scaler = StandardScaler()
scaler

# +
# масштабируем признаки обучающей выборки
X_train_scaled = scaler.fit_transform(X_train)

# убедимся, что объект scaler запомнил значения среднего и СКО
# для каждого признака
scaler.mean_, scaler.scale_
# -

# применим масштабированные данные для обучения модели линейной регрессии
model = LinearRegression().fit(X_train_scaled, y_train)
model

# +
# преобразуем тестовые данные с использованием среднего и СКО, рассчитанных на 
# обучающей выборке
# так тестовые данные не повляют на обучение модели, и мы избежим утечки данных
X_test_scaled = scaler.transform(X_test)

# сделаем прогноз на стандартизированных тестовых данных
y_pred = model.predict(X_test_scaled)
y_pred[:5]
# -

# и оценим R-квадрат (метрика (score) по умолчанию для класса LinearRegression)
model.score(X_test_scaled, y_test)

# #### Применение пайплайна

# ##### Класс make_pipeline

# создадим объект pipe, в который поместим объекты классов StandardScaler 
# и LinearRegression
pipe = make_pipeline(StandardScaler(), LinearRegression())
pipe

# одновременно применим масштабирование и создание модели регрессии на обучающей выборке
pipe.fit(X_train, y_train)

# теперь масштабируем тестовые данные (используя среднее и СКО обучающей части)
# и сделаем прогноз
pipe.predict(X_test)

# метод .score() выполнит масштабирование, обучит модель, сделает прогноз 
# и посчитает R-квадрат
pipe.score(X_test, y_test)

# сделать прогноз можно в одну строчку
make_pipeline(StandardScaler(), LinearRegression()).fit(X_train, y_train).predict(X_test)

# fmt: off
# как и посчитать R-квадрат
make_pipeline(
    StandardScaler(),
    LinearRegression(),
).fit(X_train, y_train).score(
    X_test,
    y_test,
)
# fmt: on

# под капотом мы создали объект класса Pipeline
type(pipe)

# ##### Класс Pipeline

# задаем названия и создаем объекты используемых классов
pipe = Pipeline(
    steps=[("scaler", StandardScaler()), ("lr", LinearRegression())], verbose=True
)

# рассчитаем коэффициент детерминации
pipe.fit(X_train, y_train).score(X_test, y_test)

# ### Приведение к диапазону

# #### MinMaxScaler

# создаем объект этого класса,
# в параметре feature_range оставим диапазон по умолчанию
minmax = MinMaxScaler(feature_range=(0, 1))
minmax

# +
# применим метод .fit() и
minmax.fit(boston)

# найдем минимальные и максимальные значения
minmax.data_min_, minmax.data_max_

# +
# приведем данные без выбросов (достаточно метода .transform())
boston_scaled = minmax.transform(boston)
# и с выбросами к заданному диапазону
boston_outlier_scaled = minmax.fit_transform(boston_outlier)

# преобразуем результаты в датафрейм
boston_scaled = pd.DataFrame(boston_scaled, columns=boston.columns)
boston_outlier_scaled = pd.DataFrame(boston_outlier_scaled, columns=boston.columns)
# -

# построим точечные диаграммы
scatter_plots(
    boston, boston_outlier, boston_scaled, boston_outlier_scaled, title="MinMaxScaler"
)

# и гистограммы
hist_plots(
    boston, boston_outlier, boston_scaled, boston_outlier_scaled, title="MinMaxScaler"
)

# #### MaxAbsScaler

# Стандартизация разреженной матрицы

# +
# создадим разреженную матрицу с пятью признаками
sparse_dict: dict[str, list[float]] = {}

sparse_dict["F1"] = [0, 0, 1.25, 0, 2.15, 0, 0, 0, 0, 0, 0, 0]
sparse_dict["F2"] = [0, 0, 0, 0.45, 0, 1.20, 0, 0, 0, 1.28, 0, 0]
sparse_dict["F3"] = [0, 0, 0, 0, 2.15, 0, 0, 0, 0.33, 0, 0, 0]
sparse_dict["F4"] = [0, -6.5, 0, 0, 0, 0, 8.25, 0, 0, 0, 0, 0]
sparse_dict["F5"] = [0, 0, 0, 0, 0, 3.17, 0, 0, 0, 0, 0, -1.85]

sparse_data = pd.DataFrame(sparse_dict)
sparse_data
# -

# стандартизируем эти данные
pd.DataFrame(
    StandardScaler().fit_transform(sparse_data), columns=sparse_data.columns
).round(2)

# Простой пример

# создадим двумерный массив
arr = np.array([[1.0, -1.0, -2.0], [2.0, 0.0, 0.0], [0.0, 1.0, 1.0]])

# +
maxabs = MaxAbsScaler()

maxabs.fit_transform(arr)
# -

# выведем модуль максимального значения каждого столбца
maxabs.scale_

pd.DataFrame(
    MaxAbsScaler().fit_transform(sparse_data), columns=sparse_data.columns
).round(2)

# Матрица csr и MaxAbsScaler

csr_data = csr_matrix(sparse_data.values)
print(csr_data)

# применим MaxAbsScaler
csr_data_scaled = MaxAbsScaler().fit_transform(csr_data)
print(csr_data_scaled)

# восстановим плотную матрицу
csr_data_scaled.todense().round(2)

# ### Robust scaling

# +
boston_scaled = RobustScaler().fit_transform(boston)
boston_outlier_scaled = RobustScaler().fit_transform(boston_outlier)

boston_scaled = pd.DataFrame(boston_scaled, columns=boston.columns)
boston_outlier_scaled = pd.DataFrame(boston_outlier_scaled, columns=boston.columns)
# -

scatter_plots(
    boston, boston_outlier, boston_scaled, boston_outlier_scaled, title="RobustScaler"
)

hist_plots(
    boston, boston_outlier, boston_scaled, boston_outlier_scaled, title="RobustScaler"
)

# ### Класс Normalizer

# #### Норма вектора

# +
# возьмем вектор с координатами [4, 3]
c_var = np.array([4, 3])

# и найдем его длину или L2 норму
l2norm = np.sqrt(c_var[0] ** 2 + c_var[1] ** 2)
l2norm
# -

# разделим каждый компонент вектора на его норму
v_normalized = c_var / l2norm
v_normalized

# +
# выведем оба вектора на графике
plt.figure(figsize=(6, 6))

ax = plt.axes()

plt.xlim([-0.07, 4.5])
plt.ylim([-0.07, 4.5])

ax.arrow(
    0,
    0,
    c_var[0],
    c_var[1],
    width=0.02,
    head_width=0.1,
    head_length=0.2,
    length_includes_head=True,
    fc="r",
    ec="r",
)
ax.arrow(
    0,
    0,
    v_normalized[0],
    v_normalized[1],
    width=0.02,
    head_width=0.1,
    head_length=0.2,
    length_includes_head=True,
    fc="g",
    ec="g",
)

plt.show()
# -

# #### L2 нормализация

# возьмем простой двумерный массив (каждая строка - это вектор)
arr = np.array([[45, 30], [12, -340], [-125, 4]])

# найдем L2 норму первого вектора
np.sqrt(arr[0][0] ** 2 + arr[0][1] ** 2)

# в цикле пройдемся по строкам
for row in arr:
    # найдем L2 норму каждого вектора-строки
    l2norm = np.sqrt(row[0] ** 2 + row[1] ** 2)
    # и разделим на нее каждый из компонентов вектора
    print((row[0] / l2norm).round(8), (row[1] / l2norm).round(8))

# убедимся, что L2 нормализация выполнена верно,
# подставив в формулу Евклидова расстояния новые координаты
np.sqrt(0.83205029**2 + 0.5547002**2).round(3)

Normalizer().fit_transform(arr)

# +
# fmt: off
plt.figure(figsize=(6, 6))

ax = plt.axes()

# в цикле нормализуем каждый из векторов
for d_var in Normalizer().fit_transform(arr):
    # и выведем его на графике в виде стрелки
    ax.arrow(
        0,
        0,
        d_var[0],
        d_var[1],
        width=0.01,
        head_width=0.05,
        head_length=0.05,
        length_includes_head=True,
        fc="g",
        ec="g",
    )

# добавим единичную окружность
circ = plt.Circle(
    (0, 0),
    radius=1,
    edgecolor="b",
    facecolor="None",
    linestyle="--",
)
ax.add_patch(circ)

plt.xlim([-1.2, 1.2])
plt.ylim([-1.2, 1.2])

plt.title('L2 нормализация')

plt.show()
# fmt: on
# -

# Опасность нормализации по строкам

# данные о росте, весе и возрасте людей
people = np.array([[180, 80, 50], [170, 73, 50]])

# получается, что у них разный возраст
Normalizer().fit_transform(people)

# #### L1 нормализация

# возьмем тот же массив
arr

# рассчитаем L1 норму для первой строки
print(np.abs(arr[0][0]) + np.abs(arr[0][1]))

# вновь пройдемся по каждому вектору
for row in arr:
    # найдем соответствующую L1 норму
    l1norm = np.abs(row[0]) + np.abs(row[1])
    # и нормализуем векторы
    print((row[0] / l1norm).round(8), (row[1] / l1norm).round(8))

# убедимся в том, что вторая вектор-строка имеет единичную
# L1 норму
print(np.abs(0.03409091) + np.abs(-0.96590909))

# через параметр norm = 'l1' укажем,
# что хотим провести L1 нормализацию
Normalizer(norm="l1").fit_transform(arr)

# +
plt.figure(figsize=(6, 6))
ax = plt.axes()

# выведем L1 нормализованные векторы
for e_var in Normalizer(norm="l1").fit_transform(arr):
    ax.arrow(
        0,
        0,
        e_var[0],
        e_var[1],
        width=0.01,
        head_width=0.05,
        head_length=0.05,
        length_includes_head=True,
        fc="g",
        ec="g",
    )

# то, как рассчитывалось расстояние до первого вектора
ax.arrow(
    0,
    0,
    0.6,
    0,
    width=0.005,
    head_width=0.03,
    head_length=0.05,
    length_includes_head=True,
    fc="k",
    ec="k",
    linestyle="--",
)
ax.arrow(
    0.6,
    0,
    0,
    0.4,
    width=0.005,
    head_width=0.03,
    head_length=0.05,
    length_includes_head=True,
    fc="r",
    ec="r",
    linestyle="--",
)

# а также границы единичных векторов при L1 нормализации
points = [[1, 0], [0, 1], [-1, 0], [0, -1]]
polygon = plt.Polygon(points, fill=None, edgecolor="b", linestyle="--")
ax.add_patch(polygon)

plt.xlim([-1.2, 1.2])
plt.ylim([-1.2, 1.2])

plt.title("L1 нормализация")

plt.show()
# -

# #### Нормализация Чебышёва

arr

# найдем расстояние Чебышёва для первого вектора
max(np.abs(arr[0][0]), np.abs(arr[0][1]))

# теперь для всего массива
for row in arr:
    # найдем соответствующую норму Чебышёва
    l_inf = max(np.abs(row[0]), np.abs(row[1]))
    # и нормализуем векторы
    print((row[0] / l_inf).round(8), (row[1] / l_inf).round(8))

# сделаем то же самое с помощью класс Normalizer
Normalizer(norm="max").fit_transform(arr)

# +
plt.figure(figsize=(6, 6))
ax = plt.axes()

# выведем нормализованные по расстоянию Чебышёва векторы,
for f_var in Normalizer(norm="max").fit_transform(arr):
    ax.arrow(
        0,
        0,
        f_var[0],
        f_var[1],
        width=0.01,
        head_width=0.05,
        head_length=0.05,
        length_includes_head=True,
        fc="g",
        ec="g",
    )

# а также границы единичных векторов при такой нормализации
points = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
polygon = plt.Polygon(points, fill=None, edgecolor="b", linestyle="--")
ax.add_patch(polygon)

plt.xlim([-1.2, 1.2])
plt.ylim([-1.2, 1.2])

plt.title("Нормализация Чебышёва")

plt.show()
# -

# ## Нелинейные преобразования

# +
load_dotenv()

boston_csv_url = os.environ.get("BOSTON_CSV_URL", "")
response = requests.get(boston_csv_url)

# вновь подгрузим полный датасет boston
boston = pd.read_csv(io.BytesIO(response.content))
# -

# #### Логарифмическое преобразование

# ##### Смысл логарифмического преобразования

# +
# построим график логарифмической функции
x = np.linspace(0.05, 100, 100)  # noqa
y = np.log(x)  # noqa

ax = plt.axes()

plt.xlim([-5, 105])
plt.ylim([-1, 5])

ax.hlines(y=0, xmin=-5, xmax=105, linewidth=1, color="k")
ax.vlines(x=0, ymin=-1, ymax=5, linewidth=1, color="k")

plt.plot(x, y)

# и посмотрим, как она поступает с промежутками между небольшими
ax.vlines(x=2, ymin=0, ymax=np.log(2), linewidth=2, color="g", linestyles="--")
ax.vlines(x=4, ymin=0, ymax=np.log(4), linewidth=2, color="g", linestyles="--")
ax.hlines(y=np.log(2), xmin=0, xmax=2, linewidth=2, color="g", linestyles="--")
ax.hlines(y=np.log(4), xmin=0, xmax=4, linewidth=2, color="g", linestyles="--")

# и большими значениями
ax.vlines(x=60, ymin=0, ymax=np.log(60), linewidth=2, color="g", linestyles="--")
ax.vlines(x=80, ymin=0, ymax=np.log(80), linewidth=2, color="g", linestyles="--")
ax.hlines(y=np.log(60), xmin=0, xmax=60, linewidth=2, color="g", linestyles="--")
ax.hlines(y=np.log(80), xmin=0, xmax=80, linewidth=2, color="g", linestyles="--")

plt.title("y = log(x)")

plt.show()
# -

# ##### Скошенное вправо распределение

# +
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.histplot(x=boston.LSTAT, bins=15, ax=ax[0])
ax[0].set_title("Скошенное вправо распределение")

sns.histplot(x=np.log(boston.LSTAT), bins=15, color="green", ax=ax[1])
ax[1].set_title("Log transformation")

plt.tight_layout()
plt.show()
# -

# рассчитаем ассиметричность до и после преобразования
print(skew(boston.LSTAT), skew(np.log(boston.LSTAT)))

# рассчитаем коэффициент эксцесса до и после преобразования
print(kurtosis(boston.LSTAT), kurtosis(np.log(boston.LSTAT)))

# +
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

probplot(boston.LSTAT, dist="norm", plot=ax[0])
ax[0].set_title("Скошенное вправо распределение")

probplot(np.log(boston.LSTAT), dist="norm", plot=ax[1])
ax[1].set_title("Log transformation")

plt.tight_layout()
plt.show()
# -

# Влияние логарифмического преобразования на выбросы

# +
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

sns.scatterplot(x=boston_outlier.LSTAT, y=boston_outlier.MEDV, ax=ax[0]).set(
    title="Исходные данные с выбросами"
)
sns.scatterplot(
    x=np.log(boston_outlier.LSTAT), y=np.log(boston_outlier.MEDV), ax=ax[1]
).set(title="Log transformation");
# -

# ##### Скошенное влево распределение

# +
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.histplot(x=boston.AGE, bins=15, ax=ax[0])
ax[0].set_title("Скошенное влево распределение")

sns.histplot(x=np.log(boston.AGE), bins=15, color="green", ax=ax[1])
ax[1].set_title("Log transformation")

plt.tight_layout()
plt.show()
# -

print(skew(boston.AGE), skew(np.log(boston.AGE)))

print(kurtosis(boston.AGE), kurtosis(np.log(boston.AGE)))

# +
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

probplot(boston.AGE, dist="norm", plot=ax[0])
ax[0].set_title("Скошенное влево распределение")

probplot(np.log(boston.AGE), dist="norm", plot=ax[1])
ax[1].set_title("Log transformation")

plt.tight_layout()
plt.show()
# -

# ##### Логарифм нуля и отрицательных значений

# в переменной ZN есть нулевые значения
# добавим к переменной небольшую константу
print(np.log(boston.ZN + 0.0001)[:5])  # type: ignore[index]

# можно использовать преобразование обратного гиперболического синуса
print(np.log(boston.ZN + np.sqrt(boston.ZN**2 + 1))[:5])  # type: ignore[index]

np.log(-10 + np.sqrt((-10) ** 2 + 1))

# ##### Основание логарифма

# +
i_var = np.linspace(0.05, 100, 500)
y_2 = np.log2(i_var)
y_ln = np.log(i_var)
y_10 = np.log10(i_var)

plt.plot(i_var, y_2, label="log2")
plt.plot(i_var, y_ln, label="ln")
plt.plot(i_var, y_10, label="log10")

plt.legend()

plt.show()
# -

# ##### Линейная взаимосвязь

# +
# визуально оценим "выпрямление" данных
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.scatterplot(x=boston.LSTAT, y=boston.MEDV, ax=ax[0])
ax[0].set_title("Изначальное распределение")

sns.scatterplot(x=np.log(boston.LSTAT), y=boston.MEDV, ax=ax[1])
ax[1].set_title("Log transformation")

plt.tight_layout()

plt.show()

# +
# посмотрим, как изменится корреляция, если преобразовать
# одну, вторую или сразу обе переменные
boston["LSTAT_log"] = np.log(boston["LSTAT"])
boston["MEDV_log"] = np.log(boston["MEDV"])

boston[["LSTAT", "LSTAT_log", "MEDV", "MEDV_log"]].corr()
# -

# сравним исходный датасет и лог-преобразование + обратную операцию
# (округлим значения, чтобы ошибка округления не мешала сравнению)
boston.MEDV.round(2).equals(np.exp(np.log(boston.MEDV)).round(2))

# #### Преобразование квадратного корня

# +
j_var = np.linspace(0, 30, 300)
k_var = np.sqrt(j_var)

plt.plot(j_var, k_var);

# +
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.histplot(x=boston.LSTAT, bins=15, ax=ax[0])
ax[0].set_title("Изначальное распределение")

sns.histplot(x=np.sqrt(boston.LSTAT), bins=15, color="green", ax=ax[1])
ax[1].set_title("Square root transformation")

plt.tight_layout()
plt.show()
# -

print(skew(np.sqrt(boston.LSTAT)), kurtosis(np.sqrt(boston.LSTAT)))

# +
boston["LSTAT_sqrt"] = np.sqrt(boston["LSTAT"])
boston["MEDV_sqrt"] = np.sqrt(boston["MEDV"])

boston[["LSTAT", "LSTAT_sqrt", "MEDV", "MEDV_sqrt"]].corr()
# -

# #### Лестница степеней Тьюки

# +
l_var = np.linspace(0.05, 30, 300)

y0 = l_var
y1 = l_var ** (-1)
y2 = -(l_var ** (-1))

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

ax[0].plot(l_var, y0)
ax[0].set_title("Изначальное распределение")

ax[1].plot(l_var, y1)
ax[1].set_title("Negative lambda")

ax[2].plot(l_var, y2)
ax[2].set_title("Solution")

plt.tight_layout()

plt.show()


# -

def tukey(
    m_var: pd.Series[float],
    n_var: pd.Series[float],
) -> tuple[float, float]:
    """Compute Tukey's transformation to maximize certain correlation."""
    m_arr, n_arr = m_var.to_numpy(), n_var.to_numpy()

    # в lambdas поместим возможные степени
    lambdas = [-2, -1, -0.5, 0, 0.5, 1, 2]
    # в corrs будем записывать получающиеся корреляции
    corrs: list[float] = []

    # в цикле последовательно применим каждую lambda
    for o_var in lambdas:
        if o_var < 0:
            # рассчитаем коэффициент корреляции Пирсона и добавим результат в corrs
            corrs.append(np.corrcoef(m_arr**o_var, n_arr**o_var)[0, 1])

        elif o_var == 0:
            corrs.append(
                np.corrcoef(
                    np.log(m_arr + np.sqrt(m_arr**2 + 1)),
                    np.log(n_arr + np.sqrt(n_arr**2 + 1)),
                )[0, 1]
            )

        else:
            corrs.append(np.corrcoef(-(m_arr**o_var), -(n_arr**o_var))[0, 1])

    # теперь найдем индекс наибольшего значения корреляции
    idx = int(np.argmax(np.abs(corrs)))

    # выведем оптимальную lambda и соответствующую корреляцию
    return lambdas[idx], float(np.round(corrs[idx], 3))


# найдем оптимальную lambda для LSTAT
tukey(boston.LSTAT, boston.MEDV)

# найдем оптимальные lambda для каждого признака
for col in boston[
    ["CRIM", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "LSTAT"]
]:
    print(str(col) + "\t" + str(tukey(boston[col], boston.MEDV)))

# рассчитаем корреляцию признаков до преобразования с целевой переменной
boston[
    ["CRIM", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "LSTAT", "MEDV"]
].corr().MEDV.round(2)

# +
# создадим датафрейм с преобразованными данными
# boston_transformed = {}

# boston_transformed["RM"] = boston.RM**2
# boston_transformed["PTRATIO"] = np.sqrt(boston.PTRATIO)
# boston_transformed["LSTAT"] = np.log(boston.LSTAT)
# boston_transformed["MEDV"] = boston.MEDV

# boston_transformed = pd.DataFrame(
#     boston_transformed, columns=["RM", "PTRATIO", "LSTAT", "MEDV"]
# )

boston_transformed = pd.DataFrame(
    {
        "RM": boston.RM**2,
        "PTRATIO": np.sqrt(boston.PTRATIO.to_numpy()),
        "LSTAT": np.log(boston.LSTAT.to_numpy()),
        "MEDV": boston.MEDV,
    }
)


boston_transformed.head()
# -

model = LinearRegression()
model.fit(boston[["RM", "PTRATIO", "LSTAT"]], boston.MEDV)
model.score(boston[["RM", "PTRATIO", "LSTAT"]], boston.MEDV)

model = LinearRegression()
model.fit(boston_transformed[["RM", "PTRATIO", "LSTAT"]], boston_transformed.MEDV)
model.score(boston_transformed[["RM", "PTRATIO", "LSTAT"]], boston_transformed.MEDV)

# #### Преобразование Бокса-Кокса

# +
pt = PowerTransformer(method="box-cox")

# найдем оптимальный параметр лямбда
pt.fit(boston[["LSTAT"]])

pt.lambdas_

# +
# преобразуем данные
bc_pt = pt.transform(boston[["LSTAT"]])

# метод .transform() возвращает двумерный массив
bc_pt.shape

# +
# сравним изначальное распределение и распределение после преобразования Бокса-Кокса
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.histplot(x=boston.LSTAT, bins=15, ax=ax[0])
ax[0].set_title("Изначальное распределение")

# так как на выходе метод .transform() выдает двумерный массив,
# его необходимо преобразовать в одномерный
sns.histplot(x=bc_pt.flatten(), bins=15, color="green", ax=ax[1])
ax[1].set_title("Box-Cox transformation")

plt.tight_layout()
plt.show()

# +
# оценим изменение взаимосвязи после преобразования Бокса-Кокса
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.scatterplot(x=boston.LSTAT, y=boston.MEDV, ax=ax[0])
ax[0].set_title("Изначальное распределение")

# можно использовать функцию power_transform(),
# она действует аналогично классу, но без estimator
sns.scatterplot(
    x=power_transform(boston[["LSTAT"]], method="box-cox").flatten(),
    y=power_transform(boston[["MEDV"]], method="box-cox").flatten(),
    ax=ax[1],
)
ax[1].set_title("Box-Cox transformation")

plt.tight_layout()

plt.show()
# -

# посмотрим на достигнутый коэффициент корреляции
pd.DataFrame(
    power_transform(boston[["LSTAT", "MEDV"]], method="box-cox"),
    columns=[["LSTAT", "MEDV"]],
).corr()

# +
# сравним корреляцию признаков с целевой переменной
# после преобразования Бокса-Кокса
MEDV_bc = power_transform(boston[["MEDV"]], method="box-cox").flatten()

# for col in boston[
#     ["CRIM", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "LSTAT"]
# ]:
#     col_bc = power_transform(boston[[col]], method="box-cox").flatten()
#     print(col + "\t" + str(np.round(np.corrcoef(col_bc, MEDV_bc)[0][1], 3)))

for col in ["CRIM", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "LSTAT"]:
    col_bc = power_transform(boston[[col]], method="box-cox").flatten()
    print(f"{col}\t{np.round(np.corrcoef(col_bc, MEDV_bc)[0][1], 3)}")

# +
# возьмем признаки RM, PTRATIO, LSTAT и целевую переменную MEDV
# и применим преобразование
pt = PowerTransformer(method="box-cox")
boston_bc = pt.fit_transform(boston[["RM", "PTRATIO", "LSTAT", "MEDV"]])
boston_bc = pd.DataFrame(boston_bc, columns=["RM", "PTRATIO", "LSTAT", "MEDV"])

# построим линейную регрессию
# в данном случае показатель чуть хуже, чем при лестнице Тьюки
model = LinearRegression()
model.fit(boston_bc[["RM", "PTRATIO", "LSTAT"]], boston_bc.MEDV)
model.score(boston_bc[["RM", "PTRATIO", "LSTAT"]], boston_bc.MEDV)
# -

# посмотрим на лямбды
pt.lambdas_

# выполним обратное преобразование
pd.DataFrame(
    pt.inverse_transform(boston_bc), columns=["RM", "PTRATIO", "LSTAT", "MEDV"]
).head()

# #### Преобразование Йео-Джонсона

# +
# попробуем преобразование Йео-Джонсона
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.histplot(x=boston_outlier.LSTAT, bins=15, ax=ax[0])
ax[0].set_title("Изначальное распределение")

sns.histplot(
    x=power_transform(boston[["LSTAT"]], method="yeo-johnson").flatten(),
    bins=15,
    color="green",
    ax=ax[1],
)
ax[1].set_title("Yeo–Johnson transformation")

plt.tight_layout()
plt.show()

# +
# посмотрим, как изменится линейность взаимосвязи
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.scatterplot(x=boston.LSTAT, y=boston.MEDV, ax=ax[0])
ax[0].set_title("Изначальное распределение")

sns.scatterplot(
    x=power_transform(boston[["LSTAT"]], method="yeo-johnson").flatten(),
    y=power_transform(boston[["MEDV"]], method="yeo-johnson").flatten(),
    ax=ax[1],
)
ax[1].set_title("Yeo–Johnson transformation")

plt.tight_layout()

plt.show()

# +
# возьмем те же признаки и целевую переменную, преобразуем их
# преобразование Йео-Джонсона является методом по умолчанию
pt = PowerTransformer()
boston_yj = pt.fit_transform(boston[["RM", "PTRATIO", "LSTAT", "MEDV"]])
boston_yj = pd.DataFrame(boston_yj, columns=["RM", "PTRATIO", "LSTAT", "MEDV"])

# построим модель
model = LinearRegression()
model.fit(boston_yj.iloc[:, :3], boston_yj.iloc[:, -1])
model.score(boston_yj.iloc[:, :3], boston_yj.iloc[:, -1])
# -

# #### QuantileTransformer

# +
# приведем переменные с выбросами (!) к нормальному распределению
# с помощью квантиль-функции
qt = QuantileTransformer(
    n_quantiles=len(boston_outlier), output_distribution="normal", random_state=42
)

# для каждого из столбцов вычислим квантили нормального распределения,
# соответствующие заданному выше количеству квантилей (n_quantiles)
# и преобразуем (map) данные к нормальному распределению
boston_qt = pd.DataFrame(
    qt.fit_transform(boston_outlier), columns=boston_outlier.columns
)

# посмотрим на значения, на основе которых будут рассчитаны квантили
qt.quantiles_[-5:]
# -

# посмотрим на соответствующие им квантили нормального распределения
qt.references_[-5:]

norm.ppf(0.99802761, loc=0, scale=1)

# сравним с преобразованными значениями
print(boston_qt.LSTAT.sort_values()[-5:])

# +
# выведем результат
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

sns.histplot(x=boston_outlier.LSTAT, bins=15, ax=ax[0])
ax[0].set_title("Изначальное распределение")

sns.histplot(x=boston_qt.LSTAT, bins=15, color="green", ax=ax[1])
ax[1].set_title("QuantileTransformer")

plt.tight_layout()
plt.show()
# -

# посмотрим, выправилась ли взаимосвязь
plt.scatter(boston_qt.LSTAT, boston_qt.MEDV);

# эффект выбросов сохранился
print(max(boston_qt.LSTAT), max(boston_qt.MEDV))

# сравним исходную корреляцию
print(boston_outlier[["LSTAT", "MEDV"]].corr().iloc[0, 1])

# с корреляцией после преобразования
print(boston_qt.corr().iloc[0, 1])

# ## Дополнительные материалы

# ### Pipeline и ColumnTransformer

# #### ColumnTransformer

# +
# создадим датасет с данными о клиентах банка
scoring_dict: dict[str, object] = {
    "Name": ["Иван", "Николай", "Алексей", "Александра", "Евгений", "Елена"],
    "Age": [35, 43, 21, 34, 24, 27],
    "Experience": [7, 13, 2, np.nan, 4, 12],
    "Salary": [95, 135, 73, 100, 78, 110],
    "Credit_score": ["Good", "Good", "Bad", "Medium", "Medium", "Good"],
    "Outcome": [1, 1, 0, 1, 0, 1],
}

scoring = pd.DataFrame(scoring_dict)
scoring

# +
# разобьем данные на признаки и целевую переменную
p_var = scoring.iloc[:, 1:-1]
q_var = scoring.Outcome

# поместим название количественных и категориальных признаков в списки
num_col = ["Age", "Experience", "Salary"]
cat_col = ["Credit_score"]


imputer = SimpleImputer(strategy="mean")


scaler = StandardScaler()


encoder = OrdinalEncoder(categories=[["Bad", "Medium", "Good"]])

# поместим их в отдельные пайплайны
num_transformer = make_pipeline(imputer, scaler)
cat_transformer = make_pipeline(encoder)

# поместим пайплайны в ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[("num", num_transformer, num_col), ("cat", cat_transformer, cat_col)]
)


model = LogisticRegression()

# создадим еще один пайплайн, который будет включать объект ColumnTransformer и
# объект модели
pipe = make_pipeline(preprocessor, model)

pipe.fit(p_var, q_var)

# сделаем прогноз
pipe.predict(p_var)
# -

# #### Библиотека joblib

# ##### Сохранение пайплайна

# +
# сохраним пайплайн в файл с расширением .joblib
joblib.dump(pipe, "pipe.joblib")

# импортируем из файла
new_pipe = joblib.load("pipe.joblib")

# обучим модель и сделаем прогноз
new_pipe.fit(p_var, q_var)
pipe.predict(p_var)
# -

# ##### Кэширование функции

# +
# напишем функцию, которая принимает список чисел
# и выдает их квадрат


def square_range(start_num: int, end_num: int) -> list[int]:
    """Return a list of squared numbers in the given range with delay."""
    res_3 = []
    # пройдемся по заданному перечню
    for i in range(start_num, end_num):
        res_3.append(i**2)
        # искусственно замедлим исполнение
        time.sleep(0.5)

    return res_3


start = time.time()
res_4 = square_range(1, 21)
end = time.time()

# посмотрим на время исполнения и финальный результат
print(end - start)
print(res_4)

# +
# определим, куда мы хотим сохранить кэш
location = "/content/"

# используем класс Memory
memory = joblib.Memory(location, verbose=0)


def square_range_cached(start_num: int, end_num: int) -> list[int]:
    """Return a list of squared numbers in the given range (slow version)."""
    res = []
    # пройдемся по заданному перечню
    for i in range(start_num, end_num):
        res.append(i**2)
        # искусственно замедлим исполнение
        time.sleep(0.5)

    return res


# поместим в кэш
square_range_cached = memory.cache(square_range_cached)

# при первом вызове функции время исполнения не изменится
start = time.time()
res_2 = square_range_cached(1, 21)
end = time.time()

print(end - start)
print(res_2)

# +
start = time.time()
res_2 = square_range_cached(1, 21)
end = time.time()

print(end - start)
print(res_2)
# -

# ##### Параллелизация

n_cpu = joblib.cpu_count()
n_cpu


def slow_square(r_var: int) -> int:
    """Return the square of a number with artificial delay."""
    time.sleep(1)
    return r_var**2


# %time [slow_square(i) for i in range(10)]

# +
# функция delayed() разделяет исполнение кода на несколько задач (функций)
delayed_funcs = [delayed(slow_square)(i) for i in range(10)]

# класс Parallel отвечает за параллелизацию
# если указать n_jobs = -1, будут использованы все доступные CPU
parallel_pool = Parallel(n_jobs=n_cpu)

# %time parallel_pool(delayed_funcs)
# -

# для наглядности выведем задачи, созданные функцией delayed()
delayed_funcs


# ### Встраивание функций и классов в sklearn

# #### FunctionTransformer

def encoder2(df: pd.DataFrame, col_2: str, map_dict: dict[str, int]) -> pd.DataFrame:
    """Return a copy of df with the given column encoded using map_dict."""
    df_map = df.copy()
    df_map[col_2] = df_map[col_2].map(map_dict)
    return df_map


map_dict_2 = {"Bad": 0, "Medium": 1, "Good": 2}

# поместим функцию в класс FunctionTransformer и создадим объект этого класса
# передадим параметры в виде словаря
encoder = FunctionTransformer(
    func=encoder2, kw_args={"col_2": "Credit_score", "map_dict": map_dict_2}
)

# FunctionTransformer автоматически создаст методы
# в частности, метод .fit_transform()
encoder.fit_transform(p_var)
