"""Additional materials."""

# +
# импортируем модуль json,
import json
import pickle

# нам понадобится модуль random
import random

# а также функцию pprint() одноименной библиотеки
from pprint import pprint

# создадим файл students.p
# и откроем его для записи в бинарном формате (wb)
# алгоритм бинарного поиска
from typing import Optional, Sequence, Union, cast

# функцию urlopen() из модуля для работы с URL-адресами,
from urllib.request import urlopen

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# импортируем датасет и преобразуем в датафрейм
# импортируем данные опухолей из модуля datasets библиотеки sklearn
from sklearn.datasets import load_breast_cancer

# from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, KNNImputer

# класс логистической регрессии
from sklearn.linear_model import LinearRegression, LogisticRegression

# импортируем функцию для создания матрицы ошибок
from sklearn.metrics import accuracy_score, confusion_matrix

# функцию для разделения выборки на обучающую и тестовую части,
from sklearn.model_selection import train_test_split

# импортируем класс для масштабирования данных,
from sklearn.preprocessing import MinMaxScaler, StandardScaler
# -

sns.set(rc={"figure.figsize": (10, 6)})

# # Дополнительные материалы

# ## Временная сложность алгоритма

# +
# алгоритм линейного поиска
IntLike = Union[int, np.integer]
ArrayLike = Union[Sequence[IntLike], np.ndarray]


def linear(arr: ArrayLike, a_var: IntLike) -> tuple[int, int]:
    """Perform linear search in a list."""
    # объявим счетчик количества операций
    counter = 0

    for i_var, value in enumerate(arr):

        # с каждой итерацией будем увеличивать счетчик на единицу
        counter += 1

        if value == a_var:
            return i_var, counter
    return -1, counter


# +
# алгоритм бинарного поиска
IntLike = Union[int, np.integer]  # type: ignore[misc]
ArrayLike = Union[Sequence[IntLike], np.ndarray]  # type: ignore[misc]


def binary(arr: ArrayLike, b_var: IntLike) -> tuple[int, int]:
    """Perform binary search in a sorted list."""
    # объявим счетчик количества операций
    counter = 0

    low, high = 0, len(arr) - 1

    while low <= high:

        # увеличиваем счетчик с каждой итерацией цикла
        counter += 1

        mid = low + (high - low) // 2

        if arr[mid] == b_var:
            return mid, counter

        if arr[mid] < b_var:
            low = mid + 1

        else:
            high = mid - 1

    return -1, counter


# +
# возьмем два массива из восьми и шестнадцати чисел
arr8 = np.array([3, 4, 7, 11, 13, 21, 23, 28])
arr16 = np.array([3, 4, 7, 11, 13, 21, 23, 28, 29, 30, 31, 33, 36, 37, 39, 42])

print(len(arr8), len(arr16))
# -

# найдем числа 28 и 42 с помощью линейного поиска
# первым результатом функции будет индекс искомого числа,
# вторым - количество операций сравнения
print(linear(arr8, 28), linear(arr16, 42))

# найдем эти же числа с помощью бинарного поиска
print(binary(arr8, 28), binary(arr16, 42))

# +
# посчитаем количество операций для входных массивов разной длины
# создадим списки, куда будем записывать количество затраченных итераций
ops_linear, ops_binary = [], []

# будет 100 входных массивов длиной от 1 до 100 элементов
input_arr = np.arange(1, 101)

# на каждой итерации будем работать с массивом определенной длины
for i in input_arr:

    # внутри функций поиска создадим массив из текущего количества элементов
    # и попросим найти последний элемент i - 1
    _, c_var = linear(np.arange(i), i - 1)
    _, d_var = binary(np.arange(i), i - 1)

    # запишем количество затраченных операций в соответствующий список
    ops_linear.append(c_var)
    ops_binary.append(d_var)

# +
# выведем зависимость количества операций от длины входного массива
plt.plot(input_arr, ops_linear, label="Линейный поиск")
plt.plot(input_arr, ops_binary, label="Бинарный поиск")

plt.title("Зависимость количества операций поиска от длины массива")
plt.xlabel("Длина входного массива")
plt.ylabel("Количество операций в худшем случае")

plt.legend();
# -

# ## Ещё одно сравнение методов заполнения пропусков

# ### Создание данных с пропусками

# +
# выведем признаки и целевую переменную и поместим их в X_full и _ соответственно
X_full, _ = load_breast_cancer(return_X_y=True, as_frame=True)

# масштабируем данные
X_full = pd.DataFrame(StandardScaler().fit_transform(X_full), columns=X_full.columns)


# +
# fmt: off
# напишем функцию, которая будет случайным образом
# добавлять пропуски в выбранные нами признаки

# на вход функция будет получать полный датафрейм, номера столбцов признаков,
# долю пропусков в каждом из столбцов и точку отсчета
def add_nan(
    x_full: pd.DataFrame, 
    features: list[int], 
    nan_share: float = 0.2, 
    random_state: Optional[int] = None
) -> pd.DataFrame:
    """Generate random NaN entries."""
    random.seed(random_state)

    # сделаем копию датафрейма
    x_nan = x_full.copy()

    # вначале запишем количество наблюдений и количество признаков
    n_samples, n_features = x_full.shape

    # посчитаем количество признаков в абсолютном выражении
    how_many = int(nan_share * n_samples)

    # в цикле пройдемся по номерам столбцов
    for e_var in range(n_features):
        # если столбец был указан в параметре features,
        if e_var in features:
            # случайным образом отберем необходимое количество индексов
            # наблюдений (how_many)
            # из перечня, длиной с индекс (range(n_samples))
            mask = random.sample(range(n_samples), how_many)
            # заменим соответствующие значения столбца пропусками
            x_nan.iloc[mask, e_var] = np.nan

    # выведем датафрейм с пропусками
    return x_nan
# fmt: on


# -

# выведем пять чисел от 0 до 9
random.seed(42)
# с функцией random.sample() повторов не будет
random.sample(range(10), 5)

# выведем пять чисел от 0 до 9
random.seed(42)
# с функцией random.sample() повторов не будет
random.sample(range(10), 5)

# если использовать np.random.randint() будут повторы
np.random.seed(42)
# выберем случайным образом пять чисел от 0 до 9
np.random.randint(0, 10, 5)

# то же самое с функцией random.choice()
random.seed(42)
# выберем пять случайных чисел от 0 до 9
print([random.choice(range(10)) for _ in range(5)])

# создадим 20 процентов пропусков в первом столбце
X_nan = add_nan(X_full, features=[0], nan_share=0.2, random_state=42)

# проверим результат
(X_nan.isna().sum() / len(X_nan)).round(2)

# ### Заполнение пропусков

# Заполнение константой

# скопируем датасет
fill_const = X_nan.copy()
# заполним пропуски нулем
fill_const.fillna(0, inplace=True)
# убедимся, что пропусков не осталось
fill_const.isnull().sum().sum()

# Заполнение медианой

# скопируем датасет
fill_median = X_nan.copy()
# заполним пропуски медианой
# по умолчанию, и .fillna(), и .median() работают со столбцами
fill_median.fillna(fill_median.median(), inplace=True)
# убедимся, что пропусков не осталось
fill_const.isnull().sum().sum()


# Заполнение линейной регрессией

# передадим функции датафрейм, а также название столбца с пропусками
def linreg_imputer(df: pd.DataFrame, col: Union[str, int]) -> pd.DataFrame:
    """Impute missing values in a specified column using linear regression."""
    # обучающей выборкой будут строки без пропусков
    train = df.dropna().copy()
    # тестовой (или вернее выборкой для заполнения пропусков)
    # будут те строки, в которых пропуски есть
    test = df[df[col].isnull()].copy()

    # выясним индекс столбца с пропусками
    col_index = cast(int, df.columns.get_loc(col))

    # разделим "целевую переменную" и "признаки"
    # обучающей выборки
    ys_train = train[col]
    x_train = train.drop(col, axis=1)

    # из "тестовой" выборки удалим столбец с пропусками
    test = test.drop(col, axis=1)

    # обучим модель линейной регрессии
    model_s = LinearRegression()
    model_s.fit(x_train, ys_train)

    # сделаем прогноз пропусков
    ys_pred = model_s.predict(test)
    # вставим пропуски (value) на изначальное место (loc) столбца с пропусками (column)
    test.insert(loc=col_index, column=col, value=ys_pred)

    # соединим датасеты и обновим индекс
    df = pd.concat([train, test])
    df.sort_index(inplace=True)

    return df


fill_linreg = X_nan.copy()
fill_linreg = linreg_imputer(X_nan, "mean radius")
fill_linreg.isnull().sum().sum()

# MICE

# +
fill_mice = X_nan.copy()
mice_imputer = IterativeImputer(
    initial_strategy="mean",  # вначале заполним пропуски средним арифметическим
    estimator=LinearRegression(),  # в качестве модели используем линейную регрессию
    random_state=42,  # добавим точку отсчета
)

# используем метод .fit_transform() для заполнения пропусков
fill_mice = pd.DataFrame(
    mice_imputer.fit_transform(fill_mice), columns=fill_mice.columns
)
fill_linreg.isnull().sum().sum()
# -

# KNNImputer

# +
fill_knn = X_nan.copy()

# используем те же параметры, что и раньше: пять "соседей" с одинаковыми весами
knn_imputer = KNNImputer(n_neighbors=5, weights="uniform")

fill_knn = pd.DataFrame(knn_imputer.fit_transform(fill_knn), columns=fill_knn.columns)
fill_knn.isnull().sum().sum()


# -

# ### Оценка качества

# напишем функцию, которая считает сумму квадратов отклонений
# заполненного значения от исходного
def nan_mse(x_full: pd.DataFrame, x_nan: pd.DataFrame) -> float:
    """Compute the sum of squared deviations."""
    mse_sum = ((x_full - x_nan) ** 2).sum().sum()
    return round(float(mse_sum), 2)


# создадим списки с датасетами и названиями методов
imputer = [fill_const, fill_median, fill_linreg, fill_mice, fill_knn]
name = ["constant", "median", "linreg", "MICE", "KNNImputer"]

# в цикле оценим качество каждого из методов и выведем результат
for f_var, g_var in zip(imputer, name):
    score = nan_mse(X_full, f_var)
    print(g_var + ": " + str(score))

# ## Сериализация и десериализация

# ### JSON

# #### Простой пример

# +
url = "https://random-data-api.com/api/v2/banks"

# получаем ответ (response) в формате JSON
with urlopen(url) as response:
    # считываем его и закрываем объект response
    data = response.read()

# данные пришли в виде последовательности байтов
print(type(data))
print()
# выполняем десериализацию
output = json.loads(data)
pprint(output)
print()
# и смотрим на получившийся формат
print(type(output))
# -

# #### Вложенный словарь и список словарей

# +
# fmt: off
# создадим вложенные словари
sales = {
    'PC' : {
        'Lenovo' : 3,
        'Apple'  : 2
    },
    'Phone' : {
        'Apple': 2,
        'Samsung': 5
    }
}

# и список из словарей
students = [
    {
        'id': 1,
        'name': 'Alex',
        'math': 5,
        'computer science': 4
    },
    {
        'id': 2,
        'name': 'Mike',
        'math': 4,
        'computer science': 5
    }
]
# fmt: on
# -

# #### dumps()/loads()

# +
# преобразуем вложенный словарь в JSON
# дополнительно укажем отступ (indent)
json_sales = json.dumps(sales, indent=4)

print(json_sales)
print(type(json_sales))
# -

# восстановим словарь
sales = json.loads(json_sales)
print(sales)
print(type(sales))

# #### dump()/load()

# создадим файл students.json и откроем его для записи
with open("students.json", "w", encoding="utf-8") as wf:
    # поместим туда students, преобразовав в JSON
    json.dump(students, wf, indent=4)

# прочитаем файл из сессионного хранилища
with open("students.json", "rb") as rf:
    # и преобразуем обратно в список из словарей
    students_out = json.load(rf)

students_out

# обратите внимание, результат десериализации - это новый объект
print(students == students_out)
print(students is students_out)

# #### JSON и Pandas

# +
cancer, _ = load_breast_cancer(return_X_y=True, as_frame=True)

# создадим JSON-файл, поместим его в сессионное хранилище
cancer.to_json("cancer.json")

# и сразу импортируем его и создадим датафрейм
pd.read_json("cancer.json").head(3)
# -

# ### pickle

# #### dumps()/loads()

# +
# создадим объект pickle
sales_pickle = pickle.dumps(sales)

print(sales_pickle)
print(type(sales_pickle))

# +
# восстановим исходный тип данных
sales_out = pickle.loads(sales_pickle)

print(sales_out)
print(type(sales_out))
# -

# результат десериализации - также новый объект
print(sales == sales_out)
print(sales is sales_out)

# #### dump()/load()

# создадим файл students.p
# и откроем его для записи в бинарном формате (wb)
with open("students.p", "wb") as wf:  # type: ignore[assignment]
    # поместим туда объект pickle
    pickle.dump(students, wf)  # type: ignore[arg-type]

# достанем этот файл из сессионного хранилища
# и откроем для чтения в бинарном формате (rb)
with open("students.p", "rb") as rf:
    students_out = pickle.load(rf)

# выведем результат
students_out

# #### Собственные объекты

# Функции

# +
# создадим функцию, которая будет выводить надпись "Some function!"


def foo_() -> None:
    """Print a message."""
    print("Some function!")


# преобразуем эту функцию в объект Pickle
foo_pickle = pickle.dumps(foo_)

# десериализуем и
foo_out = pickle.loads(foo_pickle)

# вызовем ее
foo_out()


# -

# Классы

# +
# создадим класс и объект этого класса
class CatClass:
    """A class representing a cat with a color and type."""

    def __init__(self, color: str) -> None:
        """Initialize a CatClass instance."""
        self.color = color
        self.type_ = "cat"


Matroskin = CatClass("gray")
# -

# сериализуем класс в объект Pickle и поместим в файл
with open("cat_instance.pkl", "wb") as wf:  # type: ignore[assignment]
    pickle.dump(Matroskin, wf)  # type: ignore[arg-type]

# достанем из файла и десериализуем
with open("cat_instance.pkl", "rb") as rf:
    Matroskin_out = pickle.load(rf)

# выведем атрибуты созданного нами объекта класса
Matroskin_out.color, Matroskin_out.type_

# ### Сохраняемость ML-модели

# +
# импортируем датасет о раке груди
X_smpl, y_smpl = load_breast_cancer(return_X_y=True, as_frame=True)

# разделим выборку
X_train, X_test, y_train, y_test = train_test_split(
    X_smpl, y_smpl, test_size=0.30, random_state=42
)

# создадим объект класса MinMaxScaler
scaler = MinMaxScaler()

# масштабируем обучающую выборку
X_train_scaled = scaler.fit_transform(X_train)

# обучим модель на масштабированных train данных
model = LogisticRegression(random_state=42).fit(X_train_scaled, y_train)

# используем минимальное и максимальное значения
# обучающей выборки для масштабирования тестовых данных
X_test_scaled = scaler.transform(X_test)

# сделаем прогноз
y_pred = model.predict(X_test_scaled)

# +
# передадим матрице тестовые и прогнозные значения
# поменяем порядок так, чтобы злокачественные опухоли были положительным классом
model_matrix = confusion_matrix(y_test, y_pred, labels=[1, 0])

# для удобства создадим датафрейм
model_matrix_df = pd.DataFrame(model_matrix)
model_matrix_df
# -

# рассчитаем accuracy
np.round(accuracy_score(y_test, y_pred), 2)

# сериализуем и
with open("model.pickle", "wb") as wf:  # type: ignore[assignment]
    pickle.dump(model, wf)  # type: ignore[arg-type]

# десериализуем модель
with open("model.pickle", "rb") as rf:
    model_out = pickle.load(rf)

# +
# сделаем прогноз на десериализованной модели
# (напомню, это другой объект)
y_pred_out = model_out.predict(X_test_scaled)

# убедимся, что десериализованная модель покажет такой же результат
model_matrix = confusion_matrix(y_test, y_pred_out, labels=[1, 0])

model_matrix_df = pd.DataFrame(model_matrix)
model_matrix_df
# -

np.round(accuracy_score(y_test, y_pred), 2)
