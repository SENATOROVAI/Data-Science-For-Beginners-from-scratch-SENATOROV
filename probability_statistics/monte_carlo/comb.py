"""Сombinatorics."""

# ### Комбинаторика в Питоне

# #### `np.random.shuffle()` и `np.random.permutation()`

# +
# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable
# создадим массив и передадим его в функцию np.random.shuffle()
arr = np.array([1, 2, 3, 4, 5])

# сама функция выдала None, исходный массив при этом изменился
print(np.random.shuffle(arr), arr)

# +
# еще раз создадим массив
arr = np.array([1, 2, 3, 4, 5])

# передав его в np.random.permutation(),
# мы получим перемешанную копию и исходный массив без изменений
np.random.permutation(arr), arr


# -

# Функция для разделения на обучающую и тестовую выборки

# объявим функцию, которая принимает признаки X и целевую переменную y в формате
# массива Numpy или датафрейма
# дополнительно пропишем размер тестовой выборки с параметром по умолчанию 0,3
# и возможностью задать точку отсчета
def split_data(X, y, test_size = 0.3, random_state = None) -> tuple:
  """Split data into train and test sets."""
  # проверим, является ли X массивом Numpy с помощью функции isinstance()
  if isinstance(X, np.ndarray):
    # если да, превратим в датафрейм
    X = pd.DataFrame(X)
  # сделаем то же самое для y
  if isinstance(y, np.ndarray):
    y = pd.DataFrame(y)

  # еще один способ выполнить такую проверку
  # if type(X). __module__ == np. __name__:
  #   X = pd.DataFrame(X)
  # if type(y). __module__ == np. __name__:
  #   y = pd.DataFrame(y)

  # установим точку отсчета
  np.random.seed(random_state)

  # перемешаем индексы строк датасета X, не изменяя исходный массив
  indices = np.random.permutation(len(X))

  # определим количество строк, которые войдут в тестовую выборку
  # для этого умножим количество строк в X на долю тестовой выборки
  data_test_size = int(X.shape[0] * test_size)

  # начиная с этого количества (границы), будет обучающая выборка
  train_indices = indices[data_test_size:]
  # перед ним, тестовая
  test_indices = indices[:data_test_size]

  # с помощью метода .iloc() найдем в X все строки,
  # соответствующие индексам в переменных train_indices и test_indices
  X_train = X.iloc[train_indices]
  X_test = X.iloc[test_indices]

  # сделаем то же самое для y
  y_train = y.iloc[train_indices]
  y_test = y.iloc[test_indices]

  # выведем выборки в том порядке, в котором они выводятся в sklearn
  return X_train, X_test, y_train, y_test


# +
import pandas as pd

# импортируем данные о пациентах с диабетом
from sklearn.datasets import load_diabetes

# помещаем их в переменную data
data = load_diabetes()

# создаем два датафрейма
X = pd.DataFrame(data.data, columns = data.feature_names)
y = pd.DataFrame(data.target, columns = ['target'])

# для проверки работы функции можно также создать массивы Numpy
# X = data.data
# y = data.target
# -

# вызовем функцию split_data()
X_train, X_test, y_train, y_test = split_data(X, y, random_state = 42)

# посмотрим на индексы строк в переменной X_train
X_train.head(3)

# теперь посмотрим на y_train
y_train.head(3)

# #### Модуль itertools

# ##### Перестановки

# ###### Перестановки без замены

# 1. Перестановки без повторений

# +
# импортируем модуль math
import math

# передадим функции factorial() число 3
math.factorial(3)

# +
# импортируем модуль itertools
import itertools

# создадим строку из букв A, B, C
x = 'ABC'
# помимо строки можно использовать и список
# x = ['A', 'B', 'C']

# и передадим ее в функцию permutations()
# так как функция возвращает объект itertools.permutations,
# для вывода результата используем функцию list()
list(itertools.permutations(x))
# -

# чтобы узнать количество перестановок, можно использовать функцию len()
len(list(itertools.permutations(x)))

# +
# теперь элементов исходного множества шесть
x = 'ABCDEF'

# чтобы узнать, сколькими способами их можно разместить на трех местах,
# передадим параметр r = 3 и выведем первые пять элементов
list(itertools.permutations(x, r = 3))[:5]
# -

# посмотрим на общее количество таких перестановок
len(list(itertools.permutations(x, r = 3)))

# 2. Перестановки с повторениями

# +
# импортируем необходимые библиотеки
import itertools
import numpy as np
import math

# объявим функцию permutations_w_repetition(), которая будет принимать два параметра
# x - строка, список или массив Numpy
# r - количество мест в перестановке, по умолчанию равно количеству элементов в x
def permutations_w_repetition(x, r = len(x)) -> int:
  """Calculate number of permutations with repetition for given sequence."""
  # если передается строка,
  if isinstance(x, str):
    # превращаем ее в список
    x = list(x)

  # в числителе рассчитаем количество перестановок без повторений
  numerator = len(list(itertools.permutations(x, r = r)))

  # для того чтобы рассчитать знаменатель найдем,
  # сколько раз повторяется каждый из элементов
  _, counts = np.unique(x, return_counts = True)

  # объявим переменную для знаменателя
  denominator = 1

  # и в цикле будем помещать туда произведение факториалов
  # повторяющихся элементов
  for c in counts:

      # для этого проверим повторяется ли элемент
      if c > 1:

        # и если да, умножим знаменатель на факториал повторяющегося элемента
        denominator *= math.factorial(c)

  # разделим числитель на знаменатель
  # деление дает тип float, поэтому используем функцию int(),
  # чтобы результат был целым числом
  return int(numerator/denominator)


# +
# создадим строку со словом "молоко"
x = 'МОЛОКО'

# вызовем функцию
permutations_w_repetition(x)
# -

# ###### Перестановки с заменой

# посмотрим, сколькими способами можно выбрать два сорта мороженого
list(itertools.product(['Ваниль', 'Клубника'], repeat = 2))

# посмотрим на способы переставить с заменой два элемента из четырех
list(itertools.product('ABCD', repeat = 2))

# убедимся, что таких способов 16
len(list(itertools.product('ABCD', repeat = 2)))

# ##### Сочетания

# +
# возьмем пять элементов
x = 'ABCDE'

# и найдем способ переставить два элемента из этих пяти
list(itertools.permutations(x, r = 2))
# -

# уменьшим на количество перестановок каждого типа r!
int(len(list(itertools.permutations(x, r = 2)))/math.factorial(2))

# то же самое можно рассчитать с помощью функции combinations()
list(itertools.combinations(x, 2))

# посмотрим на количество сочетаний
len(list(itertools.combinations(x, 2)))

# Сочетания с заменой

# сколькими способами с заменой можно выбрать два элемента из двух
list(itertools.combinations_with_replacement('AB', 2))

# очевидно, что без замены есть только один такой способ
list(itertools.combinations('AB', 2))

# Биномиальные коэффициенты

# дерево вероятностей можно построить с помощью декартовой степени
list(itertools.product('HT', repeat = 3))

# посмотрим, в скольких комбинациях выпадет две решки при трех бросках
comb = len(list(itertools.combinations('ABC', 2)))
comb

# вычислим вероятность выпадения двух орлов в трех бросках
# при вероятности выпадения орла 0,7
round(comb * (0.7 ** 2 * (1 - 0.7)** (3 - 2)), 3)

# +
from scipy.stats import binom

# то же самое можно вычислить с помощью функции вероятности (probability mass function, pmf)
# биномиального распределения библиотеки scipy
binom.pmf(k = 2, n = 3, p = 0.7).round(3)
# -

# ### Дополнительные примеры

# #### Матожадание и среднеее значение

# Математическое ожидание

# +
# с помощью библиотеки scipy
from scipy.stats import binom

# для биномиального распределения со следующими параметрами
n, p = 3, 0.7

# рассчитаем матожидание и ожидаемую дисперсию
expected_value, variance = binom.stats(n, p, moments='mv')
expected_value, variance
# -

# Фактическое среднее значение

# +
# теперь с помощью модуля random
import numpy as np

# проведем миллион биномиальных экспрериментов
res = np.random.binomial(n = 3, p = 0.7, size = 1000000)

# и посмотрим на фактическое среднее значение и фактическую дисперсию
np.mean(res), np.var(res)
