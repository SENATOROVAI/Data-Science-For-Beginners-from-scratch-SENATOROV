"""Outliers."""

# # Выбросы в данных

# +
import os

import h2o
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import scipy.stats as st
import seaborn as sns

# импортируем класс Extended Isolation Forest
from h2o.estimators import H2OExtendedIsolationForestEstimator
from scipy import stats  # pylint: disable=W0404
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.ensemble import IsolationForest
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# -

sns.set(rc={"figure.figsize": (10, 10)})

# ## Влияние выбросов

# ### Статистический тест

np.random.seed(42)
height = list(np.round(np.random.normal(180, 10, 1000)))
print(height)

t_statistic, p_value = st.ttest_1samp(height, 182)
p_value

# +
height.append(1000)

t_statistic, p_value = st.ttest_1samp(height, 182)
p_value
# -

# ### Линейная регрессия

# +
import io
from dotenv import load_dotenv
import requests

load_dotenv()

anscombe_json_url = os.environ.get("ANSCOMBE_JSON_URL", "")
response = requests.get(anscombe_json_url)
anscombe = pd.read_json(io.BytesIO(response.content))
anscombe = anscombe[anscombe.Series == "III"]
anscombe.head()
# -

a_var, b_var = anscombe.X, anscombe.Y

# +
plt.scatter(a_var, b_var)

slope, intercept = np.polyfit(a_var, b_var, deg=1)

x_vals = np.linspace(0, 20, num=1000)
y_vals = intercept + slope * x_vals
plt.plot(x_vals, y_vals, "r")

plt.show()
# -

print(np.corrcoef(a_var, b_var)[0][1])

# будем считать выбросом наблюдение с индексом 24
a_var.drop(index=24, inplace=True)
b_var.drop(index=24, inplace=True)

# +
plt.scatter(a_var, b_var)

slope, intercept = np.polyfit(a_var, b_var, deg=1)

x_vals = np.linspace(0, 20, num=1000)
y_vals = intercept + slope * x_vals
plt.plot(x_vals, y_vals, "r")

plt.show()
# -

print(np.corrcoef(a_var, b_var)[0][1])

# ## Статистические методы

# +
import io
from dotenv import load_dotenv
import requests

load_dotenv()

boston_csv_url = os.environ.get("BOSTON_CSV_URL", "")
response = requests.get(boston_csv_url)
boston = pd.read_csv(io.BytesIO(response.content))
# -

# ### boxplot

# усы имеют длину Q1 - 1.5 * IQR и Q3 + 1.5 * IQR
sns.boxplot(a_var=boston.RM);

# ### scatter plot

sns.scatterplot(a_var=boston.RM, b_var=boston.MEDV);

# ### z-score

# посмотрим на сколько СКО значение отклоняется от среднего
c_var = stats.zscore(boston)
c_var_df = pd.DataFrame(c_var, columns=boston.columns)
c_var_df.head()

# Найдем выбросы в датафрейме

# найдем те значения, которые отклоняются больше, чем на три СКО
# технически, метод .any() выводит True для тех строк (axis = 1),
# где хотя бы одно значение True (т.е. > 3)
boston[(np.abs(c_var) > 3).any(axis=1)].head()

# Удалим выбросы в столбце

# +
# выведем True там, где в столбце RM значение меньше трех СКО
col_mask = np.abs(c_var[:, boston.columns.get_loc("RM")]) < 3

# применяем маску к датафрейму
print(boston.loc[col_mask, "RM"].head())
# -

# Удалим выбросы во всем датафрейме

# +
# если в строке (axis = 1) есть хотя бы один False как следствие условия np.abs(z) < 3,
# метод .all() вернет логический массив, который можно использовать как фильтр
z_mask = (np.abs(c_var) < 3).all(axis=1)

boston_z = boston[z_mask]
boston_z.shape
# -

boston[["RM", "MEDV"]].corr()

boston_z[["RM", "MEDV"]].corr()

# ### Измененный z-score

# +
# рассчитаем MAD
median = boston.median()
dev_median = boston - (boston.median())
abs_dev_median = np.abs(dev_median)
MAD = abs_dev_median.median()

# рассчитаем измененный z-score
# добавим константу, чтобы избежать деления на ноль
zmod = (0.6745 * (boston - boston.median())) / (MAD + 1e-5)

# создадим фильтр
zmod_mask = (np.abs(zmod) < 3.5).all(axis=1)

# выведем результат
boston_zmod = boston[zmod_mask]
boston_zmod.shape
# -

# посмотрим на корреляцию
boston_zmod[["RM", "MEDV"]].corr().iloc[0, 1].round(3)

# ### IQR

# +
# в стандартном нормальном распределении
# соотношение z-score и Q1, Q3:
q1 = -0.6745
q3 = 0.6745

iqr = q3 - q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

# тогда lower_bound и upper_bound почти равны трем СКО от среднего
# (было бы точнее, если использовать 1.75)
print(lower_bound, upper_bound)
# -

# Удаление выбросов в столбце

# +
# найдем границы 1.5 * IQR
q1 = boston.RM.quantile(0.25)
q3 = boston.RM.quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print(lower_bound, upper_bound)
# -

# применим эти границы, чтобы найти выбросы в столбце RM
boston[(boston.RM < lower_bound) | (boston.RM > upper_bound)].head()

# найдем значения без выбросов (переворачиваем маску)
boston[~(boston.RM < lower_bound) | (boston.RM > upper_bound)].head()

# Удаление выбросов в датафрейме

# +
# найдем границы 1.5 * IQR по каждому столбцу
Q1 = boston.quantile(0.25)
Q3 = boston.quantile(0.75)
IQR = Q3 - Q1
lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

# создадим маску для выбросов
# если хотя бы один выброс в строке (True), метод .any() сделает всю строку True
mask_out = ((boston < lower) | (boston > upper)).any(axis=1)
# -

# найдем выбросы во всем датафрейме
boston[mask_out].shape

# возьмем датафрейм без выбросов
boston[~mask_out].shape

# обратное условие, если все значения по всем строкам внутри границ
# метод .all() выдаст True
mask_no_out = ((boston >= lower) & (boston <= upper)).all(axis=1)

# выведем датафрейм без выбросов
boston[mask_no_out].shape

# выведем выбросы
boston[~mask_no_out].shape

# сохраним результат
boston_iqr = boston[mask_no_out]

boston_iqr[["RM", "MEDV"]].corr()

# ## Методы, основанные на модели

# ### Isolation Forest

# #### Принцип изолирующего дерева

# +
# рассмотрим пример классификации с помощью решающего дерева


iris = load_iris()

df = pd.DataFrame(iris.data[:, [2, 3]], columns=["petal_l", "petal_w"])
df["target"] = iris.target

d_var = df[["petal_l", "petal_w"]]
e_var = df.target


D_train, D_test, e_train, e_test = train_test_split(
    d_var, e_var, test_size=1 / 3, random_state=42
)


clf = DecisionTreeClassifier(criterion="entropy", max_leaf_nodes=4, random_state=42)

clf.fit(D_train, e_train)

plt.figure(figsize=(6, 6))
tree.plot_tree(clf)
plt.show()

# +
plt.figure(figsize=(8, 8))
ax = plt.axes()

sns.scatterplot(
    x=D_train.petal_l,  # noqa: VNE001
    y=D_train.petal_w,  # noqa: VNE001
    hue=df.target,
    palette="bright",
    s=60,
)

ax.vlines(
    x=2.45,  # noqa: VNE001
    ymin=0,
    ymax=2.5,
    linewidth=1,
    color="k",
    linestyles="--",
)
ax.text(
    1, 1.5, "X[0] <= 2.45", fontsize=12, bbox={"facecolor": "none", "edgecolor": "k"}
)

ax.hlines(
    y=1.75, xmin=2.45, xmax=7, linewidth=1, color="b", linestyles="--"  # noqa: VNE001
)
ax.text(
    3,
    2.3,
    "X[0] > 2.45 \nX[1] > 1.75",
    fontsize=12,
    bbox={"facecolor": "none", "edgecolor": "k"},
)

ax.vlines(x=5.35, ymin=0, ymax=1.75, linewidth=1, color="r", linestyles="--")
ax.text(
    3,
    0.5,
    "X[0] > 2.45 \nX[1] <= 1.75 \nX[0] <= 5.35",
    fontsize=12,
    bbox={"facecolor": "none", "edgecolor": "k"},
)
ax.text(
    5.5,
    0.5,
    "X[0] > 2.45 \nX[1] <= 1.75 \nX[0] > 5.35",
    fontsize=12,
    bbox={"facecolor": "none", "edgecolor": "k"},
)

plt.xlim([0.5, 7])
plt.ylim([0, 2.6])

plt.xlabel("X[0]")
plt.ylabel("X[1]")

plt.show()
# -

# #### iForest в sklearn

# ##### Пример из sklearn

# +
# зададим количество обычных наблюдений и выбросов
n_samples, n_outliers = 120, 40
rng = np.random.RandomState(0)


# создадим вытянутое (за счет умножения на covariance)
covariance = np.array([[0.5, -0.1], [0.7, 0.4]])
# и сдвинутое вверх вправо
shift = np.array([2, 2])
# облако объектов
cluster_1 = 0.4 * rng.randn(n_samples, 2) @ covariance + shift

# создадим сферическое и сдвинутое вниз влево облако объектов
cluster_2 = 0.3 * rng.randn(n_samples, 2) + np.array([-2, -2])

# создадим выбросы
outliers = rng.uniform(low=-4, high=4, size=(n_outliers, 2))

# создадим пространство из двух признаков
h_var = np.concatenate([cluster_1, cluster_2, outliers])

# а также целевую переменную (1 для обычных наблюдений, -1 для выбросов)
i_var = np.concatenate(
    [np.ones((2 * n_samples), dtype=int), -np.ones((n_outliers), dtype=int)]
)

scatter = plt.scatter(
    h_var[:, 0], h_var[:, 1], c=i_var, cmap="Paired", s=20, edgecolor="k"
)

plt.title("Обычные наблюдения распределены нормально, \nвыбросы - равномерно")

plt.show()

# +
# разделим выборку
D_train, D_test, e_train, e_test = train_test_split(
    h_var, i_var, stratify=i_var, random_state=42
)

# параметр stratify сделает так, что и в тестовой, и в обучающей выборке
# будет одинаковая доля выбросов
_, y_train_counts = np.unique(e_train, return_counts=True)
_, y_test_counts = np.unique(e_test, return_counts=True)

print(
    np.round(y_train_counts / len(e_train), 2), np.round(y_test_counts / len(e_test), 2)
)
# -

# обучим алгоритм
isof = IsolationForest(max_samples=len(D_train), random_state=0)
isof.fit(D_train)

# +
# сделаем прогноз на тесте и посмотрим результат
y_pred = isof.predict(D_test)


accuracy_score(e_test, y_pred)
# -

disp = DecisionBoundaryDisplay.from_estimator(
    isof,
    h_var,
    response_method="predict",
    alpha=0.5,
)
disp.ax_.scatter(h_var[:, 0], h_var[:, 1], c=i_var, s=20, edgecolor="k")
disp.ax_.set_title("Решающая граница изолирующего дерева")
plt.show()

# ##### Настройка гиперпараметров

X_ = [[-1], [2], [3], [5], [7], [10], [12], [20], [30], [100]]

clf = IsolationForest(contamination="auto", random_state=42).fit(X_)
print(clf.predict(X_))
print(clf.decision_function(X_))

clf = IsolationForest(contamination=0.1, random_state=42).fit(X_)
print(clf.predict(X_))
print(clf.decision_function(X_))

clf = IsolationForest(contamination=0.2, random_state=42).fit(X_)
print(clf.predict(X_))
print(clf.decision_function(X_))

# ##### Датасет boston

# +
X_boston = boston.drop(columns="MEDV")
y_boston = boston.MEDV

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_boston)

# создадим столбец с anomaly_score
boston["scores"] = clf.decision_function(X_boston)
# и результатом (выброс (-1) или нет (1))
boston["anomaly"] = clf.predict(X_boston)

# посмотрим на количество выбросов
boston[boston.anomaly == -1].shape[0]
# -

boston_ifor = boston[boston.anomaly == 1]
sns.scatterplot(x=boston_ifor.RM, y=boston_ifor.MEDV);

boston_ifor[["RM", "MEDV"]].corr()

# ##### Недостаток алгоритма

disp = DecisionBoundaryDisplay.from_estimator(
    isof,
    h_var,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(h_var[:, 0], h_var[:, 1], c=i_var, s=20, edgecolor="k")
disp.ax_.set_title("Anomaly score")
plt.show()

# ### Extended Isolation Forest

# #### Установка h2o

# !pip install h2o

print(os.environ.get("JAVA_HOME"))
print(os.environ.get("PATH"))

# # ! apt-get install default-jre
# !java -version

h2o.init()

# #### Обучение алгоритмов

# +
# зададим основные параметры алгоритмов
ntrees = 400
sample_size = len(h_var)
seed = 42

# создадим специальный h2o датафрейм
training_frame = h2o.H2OFrame(h_var)

# создадим класс обычного изолирующего леса
IF_h2o = H2OExtendedIsolationForestEstimator(
    model_id="isolation_forest",
    ntrees=ntrees,
    sample_size=sample_size,
    extension_level=0,
    seed=seed,
)

# обучим модель
IF_h2o.train(training_frame=training_frame)

# создадим класс расширенного изолирующего леса
EIF_h2o = H2OExtendedIsolationForestEstimator(
    model_id="extended_isolation_forest",
    ntrees=ntrees,
    sample_size=sample_size,
    extension_level=1,
    seed=seed,
)

# обучим модель
EIF_h2o.train(training_frame=training_frame)

# выведем статистику по каждой из моделей
print(IF_h2o)
print(EIF_h2o)
# -

# #### Сравнение алгоритмов

# ##### Обычный алгоритм

# +
# рассчитаем anomaly_score для обычного алгоритма
h2o_anomaly_score_if = IF_h2o.predict(training_frame)

# преобразуем результат в датафрейм
h2o_anomaly_score_if_df = h2o_anomaly_score_if.as_data_frame(
    use_pandas=True, header=True, use_multi_thread=True
)
# -

# посмотрим на результат
h2o_anomaly_score_if_df.head()

data = pd.DataFrame(h_var, columns=["x1", "x2"])
data["target"] = i_var

# +
# выберем количество наблюдений
sample = 60

# для наглядности рассчитаем долю от общего числа наблюдений
print(sample / len(h_var))
# -

if_df = pd.concat([data, h2o_anomaly_score_if_df], axis=1)
if_df.sort_values(by="anomaly_score", ascending=False, inplace=True)
np.unique(if_df.iloc[:sample, 2], return_counts=True)

# ##### Расширенный алгоритм

# +
h2o_anomaly_score_eif = EIF_h2o.predict(training_frame)
h2o_anomaly_score_eif_df = h2o_anomaly_score_eif.as_data_frame(
    use_pandas=True, header=True, use_multi_thread=True
)

eif_df = pd.concat([data, h2o_anomaly_score_eif_df], axis=1)
eif_df.sort_values(by="anomaly_score", ascending=False, inplace=True)
np.unique(eif_df.iloc[:sample, 2], return_counts=True)
# -

# #### Визуализация

# +
granularity = 50

# сформируем данные для прогноза
xx, yy = np.meshgrid(np.linspace(-5, 5, granularity), np.linspace(-5, 5, granularity))
hf_heatmap = h2o.H2OFrame(np.c_[xx.ravel(), yy.ravel()])

# сделаем прогноз с помощью двух алгоритмов
h2o_anomaly_score_if = IF_h2o.predict(hf_heatmap)
h2o_anomaly_score_df_if = h2o_anomaly_score_if.as_data_frame(
    use_pandas=True, header=True, use_multi_thread=True
)

heatmap_h2o_if = np.array(h2o_anomaly_score_df_if["anomaly_score"]).reshape(xx.shape)

h2o_anomaly_score_eif = EIF_h2o.predict(hf_heatmap)
h2o_anomaly_score_df_eif = h2o_anomaly_score_eif.as_data_frame(
    use_pandas=True, header=True, use_multi_thread=True
)

heatmap_h2o_eif = np.array(h2o_anomaly_score_df_eif["anomaly_score"]).reshape(xx.shape)

# +
j_var = plt.figure(figsize=(24, 9))

# объявим функцию для вывода подграфиков


def plot_heatmap(heatmap_data: np.ndarray, subplot: int, title: str) -> None:
    """Plot a heatmap with contour levels and scatter points."""
    ax1 = j_var.add_subplot(subplot)
    levels = np.linspace(0, 1, 10, endpoint=True)
    k_var = np.linspace(0, 1, 12, endpoint=True)
    k_var = np.around(k_var, decimals=1)
    c_s = ax1.contourf(xx, yy, heatmap_data, levels, cmap=plt.cm.YlOrRd)
    cbar = plt.colorbar(c_s, ticks=k_var)
    cbar.ax.set_ylabel("Anomaly score", fontsize=25)
    cbar.ax.tick_params(labelsize=15)
    ax1.set_xlabel("x1", fontsize=25)
    ax1.set_ylabel("x2", fontsize=25)
    plt.tick_params(labelsize=30)
    plt.scatter(h_var[:, 0], h_var[:, 1], s=15, c="None", edgecolor="k")
    plt.axis("equal")
    plt.title(title, fontsize=32)


# выведем тепловые карты
plot_heatmap(heatmap_h2o_if, 121, "Isolation Forest")
plot_heatmap(heatmap_h2o_eif, 122, "Extended Isolation Forest")

plt.show()
