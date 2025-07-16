"""ДЗ 1. Блок 2. Анализ и обработка данных. Раздел 3. Очистка данных.

Временная сложность алгоритма.
"""

# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable
# -

sns.set(rc = {'figure.figsize' : (10, 6)})


# # Дополнительные материалы

# ## Временная сложность алгоритма

# алгоритм линейного поиска
def linear(arr, x):
  """Search linearly."""
  # объявим счетчик количества операций
  counter = 0

  for i in range(len(arr)):

    # с каждой итерацией будем увеличивать счетчик на единицу
    counter += 1

    if arr[i] == x:
      return i, counter


# алгоритм бинарного поиска
def binary(arr, x):
  """Search binary."""
  # объявим счетчик количества операций
  counter = 0

  low, high = 0, len(arr) - 1

  while low <= high:

    # увеличиваем счетчик с каждой итерацией цикла
    counter += 1

    mid = low + (high - low) // 2

    if arr[mid] == x:
        return mid, counter

    elif arr[mid] < x:
        low = mid + 1

    else:
        high = mid - 1

  return -1


# +
# возьмем два массива из восьми и шестнадцати чисел
arr8 = np.array([3, 4, 7, 11, 13, 21, 23, 28])
arr16 = np.array([3, 4, 7, 11, 13, 21, 23, 28, 29, 30, 31, 33, 36, 37, 39, 42])

len(arr8), len(arr16)
# -

# найдем числа 28 и 42 с помощью линейного поиска
# первым результатом функции будет индекс искомого числа,
# вторым - количество операций сравнения
linear(arr8, 28), linear(arr16, 42)

# найдем эти же числа с помощью бинарного поиска
binary(arr8, 28), binary(arr16, 42)

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
  _, l = linear(np.arange(i), i - 1)
  _, b = binary(np.arange(i), i - 1)

  # запишем количество затраченных операций в соответствующий список
  ops_linear.append(l)
  ops_binary.append(b)

# +
# выведем зависимость количества операций от длины входного массива
plt.plot(input_arr, ops_linear, label = 'Линейный поиск')
plt.plot(input_arr, ops_binary, label = 'Бинарный поиск')

plt.title('Зависимость количества операций поиска от длины массива')
plt.xlabel('Длина входного массива')
plt.ylabel('Количество операций в худшем случае')

plt.legend();
# -

# ## Ещё одно сравнение методов заполнения пропусков

# ### Создание данных с пропусками

# +
# импортируем данные опухолей из модуля datasets библиотеки sklearn
from sklearn.datasets import load_breast_cancer

# выведем признаки и целевую переменную и поместим их в X_full и _ соответственно
X_full, _ = load_breast_cancer(return_X_y = True, as_frame = True)

from sklearn.preprocessing import StandardScaler

# масштабируем данные
X_full = pd.DataFrame(StandardScaler().fit_transform(X_full), columns = X_full.columns)

# +
# напишем функцию, которая будет случайным образом
# добавлять пропуски в выбранные нами признаки

# нам понадобится модуль random
import random

# на вход функция будет получать полный датафрейм, номера столбцов признаков,
# долю пропусков в каждом из столбцов и точку отсчета
def add_nan(x_full, features, nan_share = 0.2, random_state = None):
  """Add random nan values."""
  random.seed(random_state)

  # сделаем копию датафрейма
  x_nan = x_full.copy()

  # вначале запишем количество наблюдений и количество признаков
  n_samples, n_features = x_full.shape

  # посчитаем количество признаков в абсолютном выражении
  how_many = int(nan_share * n_samples)

  # в цикле пройдемся по номерам столбцов
  for f in range(n_features):
    # если столбец был указан в параметре features,
    if f in features:
      # случайным образом отберем необходимое количество индексов наблюдений (how_many)
      # из перечня, длиной с индекс (range(n_samples))
      mask = random.sample(range(n_samples), how_many)
      # заменим соответствующие значения столбца пропусками
      x_nan.iloc[mask, f] = np.nan

  # выведем датафрейм с пропусками
  return x_nan


# -

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
[random.choice(range(10)) for _ in range(5)]

# создадим 20 процентов пропусков в первом столбце
X_nan = add_nan(X_full,
                features = [0],
                nan_share = 0.2,
                random_state = 42)

# проверим результат
(X_nan.isna().sum() / len(X_nan)).round(2)

# ### Заполнение пропусков

# Заполнение константой

# скопируем датасет
fill_const = X_nan.copy()
# заполним пропуски нулем
fill_const.fillna(0, inplace = True)
# убедимся, что пропусков не осталось
fill_const.isnull().sum().sum()

# Заполнение медианой

# скопируем датасет
fill_median = X_nan.copy()
# заполним пропуски медианой
# по умолчанию, и .fillna(), и .median() работают со столбцами
fill_median.fillna(fill_median.median(), inplace = True)
# убедимся, что пропусков не осталось
fill_const.isnull().sum().sum()

# Заполнение линейной регрессией

from sklearn.linear_model import LinearRegression


# передадим функции датафрейм, а также название столбца с пропусками
def linreg_imputer(df, col):
  """Impute values by using linreg."""
  # обучающей выборкой будут строки без пропусков
  train = df.dropna().copy()
  # тестовой (или вернее выборкой для заполнения пропусков)
  # будут те строки, в которых пропуски есть
  test = df[df[col].isnull()].copy()

  # выясним индекс столбца с пропусками
  col_index = df.columns.get_loc(col)

  # разделим "целевую переменную" и "признаки"
  # обучающей выборки
  y_train = train[col]
  X_train = train.drop(col, axis = 1)

  # из "тестовой" выборки удалим столбец с пропусками
  test = test.drop(col, axis = 1)

  # обучим модель линейной регрессии
  model = LinearRegression()
  model.fit(X_train, y_train)

  # сделаем прогноз пропусков
  y_pred = model.predict(test)
  # вставим пропуски (value) на изначальное место (loc) столбца с пропусками (column)
  test.insert(loc = col_index, column = col, value = y_pred)

  # соединим датасеты и обновим индекс
  df = pd.concat([train, test])
  df.sort_index(inplace = True)

  return df


fill_linreg = X_nan.copy()
fill_linreg = linreg_imputer(X_nan, 'mean radius')
fill_linreg.isnull().sum().sum()

# MICE

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# +
fill_mice = X_nan.copy()
mice_imputer = IterativeImputer(initial_strategy = 'mean', # вначале заполним пропуски средним арифметическим
                                estimator = LinearRegression(), # в качестве модели используем линейную регрессию
                                random_state = 42 # добавим точку отсчета
                                )

# используем метод .fit_transform() для заполнения пропусков
fill_mice = pd.DataFrame(mice_imputer.fit_transform(fill_mice), columns = fill_mice.columns)
fill_linreg.isnull().sum().sum()
# -

# KNNImputer

from sklearn.impute import KNNImputer

# +
fill_knn = X_nan.copy()

# используем те же параметры, что и раньше: пять "соседей" с одинаковыми весами
knn_imputer = KNNImputer(n_neighbors = 5, weights = 'uniform')

fill_knn = pd.DataFrame(knn_imputer.fit_transform(fill_knn), columns = fill_knn.columns)
fill_knn.isnull().sum().sum()


# -

# ### Оценка качества

# напишем функцию, которая считает сумму квадратов отклонений
# заполненного значения от исходного
def nan_mse(X_full, X_nan):
  """Calculate MSE between values."""
  return ((X_full - X_nan) ** 2).sum().sum().round(2)


# создадим списки с датасетами и названиями методов
imputer = [fill_const, fill_median, fill_linreg, fill_mice, fill_knn]
name = ['constant', 'median', 'linreg', 'MICE', 'KNNImputer']

# в цикле оценим качество каждого из методов и выведем результат
for i, n in zip(imputer, name):
  score = nan_mse(X_full, i)
  print(n + ': ' + str(score))

# ## Сериализация и десериализация

# ### JSON

# #### Простой пример

# +
# импортируем модуль json,
import json
# функцию urlopen() из модуля для работы с URL-адресами,
from urllib.request import urlopen
# а также функцию pprint() одноименной библиотеки
from pprint import pprint

url = 'https://random-data-api.com/api/v2/banks'

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
# -

# #### dumps()/loads()

# +
# преобразуем вложенный словарь в JSON
# дополнительно укажем отступ (indent)
json_sales = json.dumps(sales, indent = 4)

print(json_sales)
print(type(json_sales))
# -

# восстановим словарь
sales = json.loads(json_sales)
print(sales)
print(type(sales))

# #### dump()/load()

# создадим файл students.json и откроем его для записи
with open('../content/students.json', 'w') as wf:
  # поместим туда students, преобразовав в JSON
  json.dump(students, wf, indent = 4)

# прочитаем файл из сессионного хранилища
with open('../content/students.json', "rb") as rf:
  # и преобразуем обратно в список из словарей
  students_out = json.load(rf)

students_out

# обратите внимание, результат десериализации - это новый объект
print(students == students_out)
print(students is students_out)

# #### JSON и Pandas

# +
# импортируем датасет и преобразуем в датафрейм
from sklearn.datasets import load_breast_cancer
cancer, _ = load_breast_cancer(return_X_y = True, as_frame = True)

# создадим JSON-файл, поместим его в сессионное хранилище
cancer.to_json('../content/cancer.json')

# и сразу импортируем его и создадим датафрейм
pd.read_json('../content/cancer.json').head(3)
# -

# ### pickle

import pickle

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
with open('../content/students.p', 'wb') as wf:
  # поместим туда объект pickle
  pickle.dump(students, wf)

# достанем этот файл из сессионного хранилища
# и откроем для чтения в бинарном формате (rb)
with open('../content/students.p', 'rb') as rf:
  students_out = pickle.load(rf)

# выведем результат
students_out


# #### Собственные объекты

# Функции

# +
# создадим функцию, которая будет выводить надпись "Some function!"
def foo():
  """Print value."""
  print('Some function!')

# преобразуем эту функцию в объект Pickle
foo_pickle = pickle.dumps(foo)

# десериализуем и
foo_out = pickle.loads(foo_pickle)

# вызовем ее
foo_out()


# -

# Классы

# +
# создадим класс и объект этого класса
class CatClass:
  """Definition of Cat class."""

  def __init__(self, color):
    """Initialize default parameters."""
    self.color = color
    self.type_ = 'cat'

Matroskin = CatClass('gray')
# -

# сериализуем класс в объект Pickle и поместим в файл
with open('cat_instance.pkl', 'wb') as wf:
  pickle.dump(Matroskin, wf)

# достанем из файла и десериализуем
with open('cat_instance.pkl', 'rb') as rf:
  Matroskin_out = pickle.load(rf)

# выведем атрибуты созданного нами объекта класса
Matroskin_out.color, Matroskin_out.type_

# ### Сохраняемость ML-модели

# +
# импортируем датасет о раке груди
X, y = load_breast_cancer(return_X_y = True, as_frame = True)

# импортируем класс для масштабирования данных,
from sklearn.preprocessing import MinMaxScaler
# функцию для разделения выборки на обучающую и тестовую части,
from sklearn.model_selection import train_test_split
# класс логистической регрессии
from sklearn.linear_model import LogisticRegression

# разделим выборку
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.30,
                                                    random_state = 42)

# создадим объект класса MinMaxScaler
scaler = MinMaxScaler()

# масштабируем обучающую выборку
X_train_scaled = scaler.fit_transform(X_train)

# обучим модель на масштабированных train данных
model = LogisticRegression(random_state = 42).fit(X_train_scaled, y_train)

# используем минимальное и максимальное значения
# обучающей выборки для масштабирования тестовых данных
X_test_scaled = scaler.transform(X_test)

# сделаем прогноз
y_pred = model.predict(X_test_scaled)

# +
# импортируем функцию для создания матрицы ошибок
from sklearn.metrics import confusion_matrix

# передадим матрице тестовые и прогнозные значения
# поменяем порядок так, чтобы злокачественные опухоли были положительным классом
model_matrix = confusion_matrix(y_test, y_pred, labels = [1,0])

# для удобства создадим датафрейм
model_matrix_df = pd.DataFrame(model_matrix)
model_matrix_df

# +
from sklearn.metrics import accuracy_score

# рассчитаем accuracy
np.round(accuracy_score(y_test, y_pred), 2)
# -

# сериализуем и
with open('model.pickle', 'wb') as wf:
  pickle.dump(model, wf)

# десериализуем модель
with open('model.pickle', 'rb') as rf:
  model_out = pickle.load(rf)

# +
# сделаем прогноз на десериализованной модели
# (напомню, это другой объект)
y_pred_out = model_out.predict(X_test_scaled)

# убедимся, что десериализованная модель покажет такой же результат
model_matrix = confusion_matrix(y_test, y_pred_out, labels = [1,0])

model_matrix_df = pd.DataFrame(model_matrix)
model_matrix_df
# -

np.round(accuracy_score(y_test, y_pred), 2)
