"""Dot product."""

# +
import numpy as np

# предположим мы записали данные
# роста, веса и обхвата шеи одного человека в список
data = [1.72, 54, 36.2]

# убедимся, что это список с помощью функции type()
type(data)
# -

# преобразуем список в массив Numpy
data_numpy = np.array(data)
data_numpy

# если у нас несколько наблюдений, то нужна матрица, т.е.
# по сути, несколько векторов
data_matrix = np.array([[1.72, 54, 36.2], [1.74, 58, 36.3], [1.68, 52, 32.9]])
data_matrix

# мы можем посмотреть размерность матрицы (количество строк и столбцов)
data_matrix.shape

# +
# даны два вектора в виде массивов Numpy

a_val = np.array([1.72, 54])  # вектор данных
w_val = np.array([19.86, 0.05])  # вектор весов

# перемножим их вручную
1.72 * 19.86 + 54 * 0.05
# -

# используем скалярное произведение векторов
np.dot(a_val, w_val)

# +
# # np.dot?

#  2-D arrays [[1,2,3]] matrix multiplication a@b
#  1-D [1,2,3]

# - If both `a` and `b` are 1-D arrays, it is inner product of vectors
#   (without complex conjugation).

# - If both `a` and `b` are 2-D arrays, it is matrix multiplication,
#   but using :func:`matmul` or ``a @ b`` is preferred.

# - If either `a` or `b` is 0-D (scalar), it is equivalent to
#   :func:`multiply` and using ``numpy.multiply(a, b)`` or ``a * b`` is
#   preferred.

# - If `a` is an N-D array and `b` is a 1-D array, it is a sum product over
#   the last axis of `a` and `b`.

# - If `a` is an N-D array and `b` is an M-D array (where ``M>=2``), it is a
#   sum product over the last axis of `a` and the second-to-last axis of
#   `b`::

# +
# даны два вектора (данные двух человек)
# нужно понять, насколько они схожи
b_val = np.array([1.72, 54, 36.2])
c_val = np.array([1.56, 47, 30.0])

# вначале выполним операции в числителе формулы
numerator = np.dot(b_val, c_val)

# теперь займемся знаменателем и
# (1) рассчитаем длины (по большому счету, это теорема Пифагора)
b_len = np.linalg.norm(b_val)
c_len = np.linalg.norm(c_val)

# (2) перемножим их
denominator = b_len * c_len

# посмотрим, чему равен косинус угла между векторами
cosine = numerator / denominator
cosine

# +
# для этого вначале вычислим угол в радианах
angle_radians = np.arccos(cosine)

# затем в градусах
angle_degrees = angle_radians * 360 / 2 / np.pi
angle_degrees
# угол чрезвычайно мал, а значит векторы очень близки друг к другу.
# при построении рекомендательных систем для сопутствующих
# товаров в интернет-магазине.
