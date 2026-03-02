"""Numpy."""

# ## Массив Numpy

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix

# ### Как создать массив Numpy

# #### Функция np.array()

# из массива
arr = np.array([0, 1, 2, 3, 4])
print(arr)

# из кортежа
arr = np.array((0, 1, 2, 3, 4))
print(arr)

# #### Функция np.arange()

# аналог range
arr = np.arange(10)
print(arr)

arr = np.arange(2, 10, 2)
print(arr)

# Этот код вызовет ошибку, так как нет встроенного перебора по вещ. числам:
# ```python
# print(list(range(2, 5.5, 0.5)))
# ```

print(np.arange(2, 5.5, 0.5))

# #### Тип данных элементов массива

arr_f = np.array([0, 1, 2, 3, 4, 5], float)
print(arr_f)
print(arr_f.dtype)

# #### Св-ва (атрибуты) массива

print(arr)

# кол-во измерений
print(arr.ndim)

# кол-во элементов в каждом измерении
print(arr.shape)

# тип
print(arr.dtype)

# размер в байтах одного элемента
arr.itemsize

# общий размер в байтах
arr.nbytes

# то же самое
arr.size * arr.itemsize

# ### Измерения массива

# #### Массив с нулевым измерением

arr_0d = np.array(42)
arr_0d

print(arr_0d.ndim)
print(arr_0d.shape)
print(arr_0d.size)

# #### Одномерный массив (вектор)

arr_1d = np.array([1, 2, 3])
arr_1d

print(arr_1d.ndim)
print(arr_1d.shape)
print(arr_1d.size)

# #### Двумерный массив (матрица)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d

print(arr_2d.ndim)
print(arr_2d.shape)
print(arr_2d.size)

column = np.array([[1], [2], [3]])
column

column.shape

row = np.array([[1, 2, 3]])
row

row.shape

# #### Трехмерный массив

# np.reshape - распределяет элементы по измерениям
arr5_3d = np.arange(12).reshape(2, 2, 3)
arr5_3d

print(arr5_3d.ndim)
print(arr5_3d.shape)
print(arr5_3d.size)

# #### Другие способы создания массивов

# Функция `np.zeros()`

np.zeros(5)

np.zeros((2, 3))

# Функция `np.ones()`

np.ones((2, 2, 3))

# Функция `np.full()`

np.full((2, 3), 4)

# Функция `np.empty()`

np.empty((3, 2))

# Функции `np.zeros_like()`, `np.ones_like()`, `np.full_like()`, `np.empty_like()`

tb1 = np.arange(1, 7).reshape(2, 3)

np.zeros_like(tb1)

np.ones_like(tb1)

np.full_like(tb1, 2)

np.empty_like(tb1)

# Функция `np.linspace`

# 10 точек начиная с 0 до 0.9 включительно
np.linspace(0, 0.9, 10)

# или через np.arange
np.arange(0, 1, 0.1)

# +
plt.figure(figsize=(8, 6))

x_vals = np.linspace(-5, 5, 5000)

y_vals = x_vals**2

plt.grid()
plt.plot(x_vals, y_vals)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.show()
# -

x_vals[10:]

# Функции `np.random.rand()` и `np.random.randint()`

# [0, 1)
np.random.rand(4, 3)

np.random.randint(-3, 3, size=(2, 3, 2))


# `np.fromfunction()`


def power(idx1: int, idx2: int) -> int:
    """Сумма индексов.

    Args:
        idx1 (int): Индекс первого элемента
        idx2 (int): Индекс второго элемента

    Returns:
        int: Итоговый индекс
    """
    return idx1 + idx2


np.fromfunction(power, (3, 3))

np.fromfunction(lambda i, j: i == j, (3, 3))

# Матрица в формате csr и метод .toarray()

tb2 = np.array([[2, 0, 0, 1, 0, 0, 0], [0, 0, 3, 0, 0, 2, 0], [0, 0, 0, 1, 0, 0, 0]])
tb2

# доля ненулевых значений
print(1.0 - np.count_nonzero(tb2) / tb2.size)

tb3 = csr_matrix(tb2)
print(tb3)

tb4 = tb3.toarray()
tb4

print(1.0 - np.count_nonzero(tb4) / tb3.size)

# ### Индексы и срезы

# #### Индекс элемента массива

tb5 = np.array([[1, 2, 3], [4, 5, 6]])
tb5

tb5.shape

tb5[0]

tb5[0][0]

# #### Срез массива

# Массив 1D

tb6 = np.array([1, 2, 3, 4, 5, 6])
tb6

tb6[1:6:2]

# Массив 2D

tb7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
tb7

tb7[0, :2]

tb7[:, 1]

tb7[0, 0]

tb7[-1, -1]

tb7[1, ::2]

# Массив 3D

tb8 = np.arange(16).reshape(4, 2, -1)
tb8

tb8[2][1][0]

tb8[2:, 1, :]

tb8[:2]

tb8[:, 0, :]

# ### Оси массива

# #### Массив 2D

arr2_2d = np.array([[1, 2], [3, 4]])
arr2_2d

arr2_2d.shape

# Сложение вдоль первой оси (axis = 0)

np.sum(arr2_2d, axis=0)

# Сложение вдоль второй оси (axis = 1)

np.sum(arr2_2d, axis=1)

# Сложение вдоль обеих осей (axis = (0, 1))

# сумма будет сначала рассчитана вдоль оси 0, затем вдоль оси 1
np.sum(arr2_2d, axis=(0, 1))

# тоже по всем элементам
np.sum(arr2_2d)

# тоже
np.sum(arr2_2d, axis=None)

# Отрицательные значения в параметре axis

# axis = -1 соответствует последней оси массива, в данном случае, axis = 1
np.sum(arr2_2d, axis=-1)

# axis = -2 указывает на первую ось, то есть axis = 0
np.sum(arr2_2d, axis=-2)

# #### Массив 3D

arr2_3d = np.arange(12).reshape(2, 2, 3)
arr2_3d

# Сложение вдоль первой оси (axis = 0)

np.sum(arr2_3d, axis=0)

arr2_3d[0]

arr2_3d[1]

arr2_3d[0] + arr2_3d[1]

# +
# через цикл for
total = np.zeros((2, 3))
for i in range(2):
    total += arr2_3d[i]

total
# -

# Сложение вдоль второй оси (axis = 1)

np.sum(arr2_3d, axis=1)

arr2_3d[0][0] + arr2_3d[0][1]

arr2_3d[1][0] + arr2_3d[1][1]

total1 = np.zeros((2, 3))
for i in range(2):
    for value in range(2):
        total1[i] += arr2_3d[i][value]
total1

# Сложение вдоль третей оси (axis = 2)

np.sum(arr2_3d, axis=2)

arr2_3d[0][0][0] + arr2_3d[0][0][1] + arr2_3d[0][0][2]

arr2_3d[0][1][0] + arr2_3d[0][1][1] + arr2_3d[0][1][2]

arr2_3d[1][0][0] + arr2_3d[1][0][1] + arr2_3d[1][0][2]

arr2_3d[1][1][0] + arr2_3d[1][1][1] + arr2_3d[1][1][2]

total2 = np.zeros((2, 2))
for i in range(2):
    for val0 in range(2):
        for val1 in arr2_3d[i][val0]:
            total2[i][val0] += val1
total2

# Сложение вдоль первой и второй осей (axis = (0, 1))

np.sum(arr2_3d, axis=(0, 1))

total_0 = np.zeros((2, 3))
for i in range(2):
    total_0 += arr2_3d[i]
total_0

total_1 = np.zeros(3)
for i in range(2):
    total_1 += total_0[i]
total_1

total3 = np.zeros(3)
for i in range(2):
    for val0 in range(2):
        total3 += arr2_3d[i][val0]
total3

# Сложение вдоль всех трёх осей (axis = (0, 1, 2))

np.sum(arr2_3d, axis=(0, 1, 2))

np.sum(arr2_3d)

total4 = 0
for i in range(2):
    for val1 in range(2):
        for val2 in range(3):
            total4 += arr2_3d[i][val1][val2]
total4

# ### Операции с массивами

# #### Функция len()

arr3_3d = np.arange(12).reshape(2, 2, 3)
arr3_3d

len(arr3_3d)

len(arr3_3d[0][0])

# #### Вхождение в массив

3 in arr3_3d

11 not in arr3_3d

# #### Распаковка массива

tb9 = np.arange(1, 28).reshape(3, 9)
tb9

# каждая строчка в переменной
row1, row2, row3 = tb9
row1

# первый, последний и остальные элементы первой строки
row1, *row2, row3 = tb9[0]
print(row1)
print(row2)
print(row3)

# #### Изменение элементов массива

arr1_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr1_2d

arr1_2d[0, 0] = 2
arr1_2d

arr1_2d[0] = 1
arr1_2d

arr_2d[:, 2] = 0
arr_2d

arr1_3d = np.arange(12).reshape(2, 2, 3)
arr1_3d

arr1_3d[1, :, 1] = [0, 1]
arr1_3d

arr1_3d.fill(7)
arr1_3d

# #### Сортировка массива и обратный порядок его элементов

# Функция `np.sort()`

tb10 = np.array([[4, 8, 2], [2, 3, 1]])
tb10

# по умолчанию axis = -1
np.sort(tb10)

np.sort(tb10, axis=1)

np.sort(tb10, axis=0)

# axis = None возвращает одномерный массив,
# а затем сортирует
np.sort(tb10, axis=None)

# Обратный порядок элементов массива через оператор среза

print(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[::-1])

print(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[-3:3:-1])

tb11 = np.array([[4, 8, 2], [2, 3, 1], [1, 7, 2]])
tb11

tb11[::-1, ::-1]

tb11[::-1]

tb11[:, ::-1]

# Обратный порядок через функцию np.flip()

np.flip(tb11)

np.flip(tb11, axis=0)

np.flip(tb11, axis=1)

# Сортировка в убывающем порядке

tb12 = np.array([4, 2, 6, 1, 7, 3, 5])

print(np.sort(tb12)[::-1])

tb12

tb12[::-1].sort()

tb12

# #### Изменение размерности

# Метод `.reshape()`

arr4_3d = np.arange(12).reshape(2, 2, 3)
arr4_3d

arr4_3d.size

# меняем размерность при сохранении общего кол-ва элементов
arr3_2d = arr4_3d.reshape(2, 6)
arr3_2d

# Функция `np.resize()` и метод `.resize()`

# функция np.resize() позволяет не сохранять прежнее кол-во элементов
# существующие элементы копируются в новые ячейки
np.resize(arr3_2d, (3, 6))

arr3_2d_copy = arr3_2d.copy()
arr3_2d_copy.resize(4, 6)
arr3_2d_copy

# Методы `.flatten()` и `.ravel()`

# вытягивание массива в одно измерение
# создает копию как .copy()
arr4_3d.flatten()

# без создания копии
arr4_3d.ravel()

# `np.newaxis`

# np.newaxis добавляет измерение в массиве
tb13 = np.array([1, 2, 3])
tb13.shape

# +
tb14 = tb13[np.newaxis, :]

print(tb14)
print(tb14.shape)

# +
tb15 = tb13[:, np.newaxis]

print(tb15)
print(tb15.shape)
# -

# Функция `np.expand_dims()`

tb16 = np.array([[1, 2], [3, 4]])
tb16

# добавим внешнее измерение
np.expand_dims(tb16, axis=0)

# добавим измерение "по середине"
np.expand_dims(tb16, axis=1)

# добавим внутреннее измерение
np.expand_dims(tb16, axis=2)

# Функция `np.squeeze()`

arr_4d = np.arange(9).reshape(1, 3, 3, 1)
arr_4d

# удаление измерений
np.squeeze(arr_4d)

print(np.squeeze(arr_4d).shape)

# #### Объединение массивов

# Функция `np.concatenate()`

tb17 = np.arange(4).reshape(2, 2)
tb17

tb18 = np.arange(4, 8).reshape(2, 2)
tb18

np.concatenate((tb17, tb18), axis=0)

np.concatenate((tb17, tb18), axis=1)

# Функция `np.stack()`

# создается новая ось
np.stack((tb17, tb18), axis=0)

np.stack((tb17, tb18), axis=1)

np.stack((tb17, tb18), axis=2)

# ### Документация

# +
# print?
# -

# ?print

help(print)
