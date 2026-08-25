"""Numpy array."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix

# ## Массив Numpy

# ### Как создать массив Numpy

# #### Функция np.array()
#
#

arr_list = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(arr_list)

arr_tuple = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
print(arr_tuple)

# #### Функция np.arange()
#

arr_range_full = np.arange(10)
print(arr_range_full)

arr_main = np.arange(2, 10, 2)
print(arr_main)

# в arange() тип float  допускается
print(np.arange(2, 5.5, 0.5))

# #### Тип данных элементов массива
#

# Можно указать явно тип данных массива
arr_f = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0), float)
print(arr_f)
print(arr_f.dtype)

# ### Свойства (атрибуты) массива
#

print(arr_main)

# #### Количество измерений
#

print(arr_main.ndim)

# #### Количество элементов в каждом измерении
#

print(arr_main.shape)

# #### Общее количество элементов во всех измерениях
#

print(arr_main.size)

# #### Tип данных массива
#

print(arr_main.dtype)

print(arr_main.nbytes)

print(arr_main.size * arr_main.itemsize)

# ### Измерения массива
#
#

# #### Массив с нулевым измерением

arr_0d_scalar = np.array(42)
print(arr_0d_scalar.ndim)
print(arr_0d_scalar.shape)
print(arr_0d_scalar.size)

# #### Одномерный массив (вектор)
#

arr_1d_vector = np.array([42, 15, 52, 63, 94])
print(arr_1d_vector.ndim)
print(arr_1d_vector.shape)
print(arr_1d_vector.size)

# #### Двумерный массив (матрица)
#

arr_2d_matrix = np.array([[42, 15, 52, 63], [94, 22, 53, 15]])
print(arr_2d_matrix.ndim)
print(arr_2d_matrix.shape)
print(arr_2d_matrix.size)

# такая матрица имеет три строки с один элементом в каждой
column = np.array([[1], [2], [3]])
print(column)

print(column.shape)

# такая матрица имеет три строки с один элементом в каждой
row = np.array([[1, 2, 3]])
print(row)

print(row.shape)

# #### Трехмерный массив
#

arr_3d_info = np.arange(12).reshape(2, 2, 3)
print(arr_3d_info)

print(arr_3d_info.ndim)
print(arr_3d_info.shape)
print(arr_3d_info.size)

# ### Другие способы создания массивов
#
#

# #### Функция np.zeros()

print(np.zeros(5))

print(np.zeros((2, 3)))

# #### Функция np.ones()
#

print(np.ones((2, 3)))

# #### Функция np.full()
#

print(np.full((2, 3), 4))

# Функция np.empty()
print(np.empty((3, 2)))

# #### Функции np.zeros_like(), np.ones_like(), np.full_like(), np.empty_like()
#

base_matrix = np.arange(1, 7).reshape(2, 3)
print(base_matrix)

print(np.zeros_like(base_matrix))

print(np.ones_like(base_matrix))

print(np.full_like(base_matrix, 10))

print(np.empty_like(base_matrix))

# #### Функция np.linspspace()
#

print(np.linspace(0, 0.9, 10))

print(np.arange(0, 1, 0.1))

# +
plt.figure(figsize=(8, 6))

x_line = np.linspace(-5, 5, 5000)
y_parabola = x_line**2

plt.grid()

plt.plot(x_line, y_parabola)

plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.show()

print(x_line[:10])
# -

# #### Функции np.random.rand() и np.random.randint()
#

print(np.random.rand(4, 3))

print(np.random.randint(-3, 3, size=(2, 3, 2)))


# #### np.fromfunction()
#


# +
def power(base_val: float, exp_val: float) -> float:
    """Temporary training function."""
    return float(base_val**exp_val)


print(np.fromfunction(power, (3, 3)))
# -

print(np.fromfunction(lambda row_idx, col_idx: row_idx == col_idx, (3, 3)))

# ### Матрица в формате csr и метод .toarray()
#

matrix_sparse_data = np.array(
    [[2, 0, 0, 1, 0, 0, 0], [0, 0, 3, 0, 0, 2, 0], [0, 0, 0, 1, 0, 0, 0]]
)
print(matrix_sparse_data)

# #### Доля нулевых значений
#

print(1.0 - np.count_nonzero(matrix_sparse_data) / matrix_sparse_data.size)

# +
csr_matrix_data: csr_matrix = csr_matrix(matrix_sparse_data)

print(csr_matrix_data)
# -

dense_data = csr_matrix_data.toarray()
print(dense_data)

# ### Индексы и срезы
#
#

# #### Индекс элемента массива

matrix_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_2x3)
print(matrix_2x3.shape)
print(matrix_2x3[0])
print(matrix_2x3[0][0])
print(matrix_2x3[0][1])

# ### Срез массива
#
#

# #### Массив 1D

vector_1_to_8 = np.arange(1, 9)
print(vector_1_to_8)

print(vector_1_to_8[1:6:2])

# #### Массив 2D
#

matrix_2x4 = np.arange(1, 9).reshape(2, 4)
print(matrix_2x4)

print(matrix_2x4[0, :2])
print(matrix_2x4[:, 1])
print(matrix_2x4[0, 0])
print(matrix_2x4[-1, -1])
print(matrix_2x4[1, ::2])

# #### Массив 3D
#

tensor_4x2x2 = np.arange(16).reshape(4, 2, -1)
print(tensor_4x2x2)

print(tensor_4x2x2[2][1][0])
print()
print(tensor_4x2x2[2:, 1, :])
print()
print(tensor_4x2x2[:2])
print()
print(tensor_4x2x2[:, 0, :])

# ### Оси массива
#
#

# #### Массив 2D

arr_2d_sum = np.array([[1, 2], [3, 4]])
print(arr_2d_sum)
print(arr_2d_sum.shape)

# Сложение вдоль первой оси (axis = 0)
print(np.sum(arr_2d_sum, axis=0))

# Сложение вдоль второй оси (axis = 1)
print(np.sum(arr_2d_sum, axis=1))

# Сложение вдоль обеих осей (axis = (0, 1))
print(np.sum(arr_2d_sum, axis=(0, 1)))
print(np.sum(arr_2d_sum))
print(np.sum(arr_2d_sum, axis=None))

# Отрицательные значения в параметре axis
print(np.sum(arr_2d_sum, axis=-1))
print(np.sum(arr_2d_sum, axis=-2))

# ### Массив 3D
#

arr_3d_sum = np.arange(12).reshape(2, 2, 3)
print(arr_3d_sum)

# применим np.sum() с параметром axis = 0
print(np.sum(arr_3d_sum, axis=0))  # ==
print()
print(arr_3d_sum[0])
print()
print(arr_3d_sum[1])
print()
print(arr_3d_sum[0] + arr_3d_sum[1])  # ==

# +
sum_axis0 = np.zeros((2, 3))

for row_idx in range(2):
    sum_axis0 += arr_3d_sum[row_idx]

print(sum_axis0)
# -

# Сложение вдоль второй оси (axis = 1)
print(np.sum(arr_3d_sum, axis=1))

print(arr_3d_sum[0][0] + arr_3d_sum[0][1])

print(arr_3d_sum[1][0] + arr_3d_sum[1][1])

# +
sum_axis1 = np.zeros((2, 3))

for row_idx in range(2):
    for col_idx in range(2):
        sum_axis1[row_idx] += arr_3d_sum[row_idx][col_idx]

print(sum_axis1)
# -

# Сложение вдоль третьей оси (axis = 2)
print(np.sum(arr_3d_sum, axis=2))

print(arr_3d_sum[0][0][0] + arr_3d_sum[0][0][1] + arr_3d_sum[0][0][2])
print(arr_3d_sum[0][1][0] + arr_3d_sum[0][1][1] + arr_3d_sum[0][1][2])
print(arr_3d_sum[1][0][0] + arr_3d_sum[1][0][1] + arr_3d_sum[1][0][2])
print(arr_3d_sum[1][1][0] + arr_3d_sum[1][1][1] + arr_3d_sum[1][1][2])

# +
sum_axis2 = np.zeros((2, 2))

for plane_idx in range(2):
    for row_idx in range(2):
        for value in arr_3d_sum[plane_idx][row_idx]:
            sum_axis2[plane_idx][row_idx] += value

print(sum_axis2)
# -

print(arr_3d_sum)

# Сложение вдоль первой и второй осей (axis = (0, 1))
print(np.sum(arr_3d_sum, axis=(0, 1)))  # ==

# +
sum_axes0_1 = np.zeros((2, 3))

for plane_idx in range(2):
    sum_axes0_1 += arr_3d_sum[plane_idx]

print(sum_axes0_1)

# +
sum_axis0_after = np.zeros(3)

for row_idx in range(2):
    sum_axis0_after += sum_axes0_1[row_idx]

print(sum_axis0_after)

# +
sum_axis_all = np.zeros(3)

for plane_idx in range(2):
    for row_idx in range(2):
        sum_axis_all += arr_3d_sum[plane_idx][row_idx]

print(sum_axis_all)
# -

# Сложение вдоль всех трех осей (axis = (0, 1, 2))
print(np.sum(arr_3d_sum, axis=(0, 1, 2)))  # ==
print(np.sum(arr_3d_sum))  # ==

# +
sum_axis_all_int: int = 0

for plane_idx in range(2):
    for row_idx in range(2):
        for depth_idx in range(3):
            sum_axis_all_int += arr_3d_sum[plane_idx][row_idx][depth_idx]

print(sum_axis_all_int)
# -

# ### Операции с массивами
#
#

# #### Функция len()

arr_3d_reshape = np.arange(12).reshape(2, 2, -1)
print(arr_3d_reshape)

print(len(arr_3d_reshape))

print(len(arr_3d_reshape[0][0]))

# #### Вхождение в массив
#

print(3 in arr_3d_reshape)

print(11 not in arr_3d_reshape)

# #### Распаковка массива
#

matrix_3x9 = np.arange(1, 28).reshape(3, 9)
print(matrix_3x9)

# +
first_row, second_row, third_row = matrix_3x9

print(first_row)
print(second_row)
print(third_row)

# +
first_value, *middle_values, last_value = matrix_3x9[0]

print(first_value)
print(middle_values)
print(last_value)
# -

# ### Изменение элементов массива
#

arr_2d_mutable = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d_mutable)

# заменим первый элемент первой строки по его индексу
arr_2d_mutable[0][0] = 2
print(arr_2d_mutable)

# запишем значение 1 в первую строку
arr_2d_mutable[0] = 1
print(arr_2d_mutable)

# запишем 0 в третий столбец массива
arr_2d_mutable[:, 2] = 0
print(arr_2d_mutable)

arr_3d_filled = np.arange(12).reshape(2, 2, 3)
print(arr_3d_filled)

# при такой операции размер среза должен совпадать
# с количеством передаваемых значений
arr_3d_filled[1, :, 1] = [0, 1]
print(arr_3d_filled)

# заменим все элементы массива на число семь
arr_3d_filled.fill(7)
print(arr_3d_filled)

# ### Сортировка массива и обратный порядок его элементов
#
#

# #### Функция np.sort()

matrix_sort = np.array([[4, 8, 2], [2, 3, 1]])
print(matrix_sort)

print(np.sort(matrix_sort))

print(np.sort(matrix_sort, axis=1))

print(np.sort(matrix_sort, axis=0))

print(np.sort(matrix_sort, axis=None))

# Обратный порядок элементов массива через оператор среза
print(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[::-1])

print(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[-3:3:-1])

matrix_slice = np.array([[4, 8, 2], [2, 3, 1], [1, 7, 2]])
print(matrix_slice)

print(matrix_slice[::-1, ::-1])

print(matrix_slice[::-1])

print(matrix_slice[:, ::-1])

# Обратный порядок через функцию np.flip()
print(np.flip(matrix_slice))

print(np.flip(matrix_slice, axis=0))

print(np.flip(matrix_slice, axis=1))

# #### Сортировка в убывающем порядке
#

vector_sort = np.array([4, 2, 6, 1, 7, 3, 5])
# мы можем последовательно применить np.sort() и оператор среза
vector_sort.sort()
print(vector_sort[::-1])

# изменение стало постоянным
vector_sort.sort()
print(vector_sort[::-1])

# ### Изменение размерности
#
#

# #### Метод .reshape()

arr_3d_resize = np.arange(12).reshape(2, 2, 3)
print(arr_3d_resize)

arr_2d_resize = arr_3d_resize.reshape(2, 6)
print(arr_2d_resize)

# #### Функция np.resize() и метод .resize()
#

print(np.resize(arr_2d_resize, (3, 6)))

# +
arr_2d_copy = arr_2d_resize.copy()

print(arr_2d_copy.resize(4, 6))
print(arr_2d_copy)
# -

# #### Методы .flatten() и .ravel()
#

# .flatten() переводит ("вытягивает") массив в одно измерение и
# создает копию исходного массива (как метод .copy())
print(arr_3d_resize.flatten())

# .ravel() делает то же самое,
# но не создает копию исходного массива и поэтому быстрее чем .flatten()
print(arr_3d_resize.ravel())

# #### np.newaxis - добавляет измерение в массиве
#

vector_expand = np.array([1, 2, 3])
print(vector_expand.shape)

row_expanded = vector_expand[np.newaxis, :]
print(row_expanded)
print(row_expanded.shape)

col_expanded = vector_expand[:, np.newaxis]
print(col_expanded)
print(col_expanded.shape)

# #### Функция np.expand_dims() - добавляет измерение по параметру axis
#

matrix_expand = np.arange(1, 5).reshape(2, 2)
print(matrix_expand)

print(np.expand_dims(matrix_expand, axis=0))

print(np.expand_dims(matrix_expand, axis=1))

print(np.expand_dims(matrix_expand, axis=2))

# #### Функция np.squeeze() - сжимает первое и последнее измерение, удаляет по сути
#

arr_4d_squeeze = np.arange(9).reshape(1, 3, 3, 1)
print(arr_4d_squeeze)

print(np.squeeze(arr_4d_squeeze))

print(np.squeeze(arr_4d_squeeze).shape)

# ### Объединение массивов
#
#

# #### Функция np.concatenate()

# +
mat_a = np.arange(4).reshape(2, 2)
mat_b = np.arange(4, 8).reshape(2, 2)

print(mat_a)
print(mat_b)
# -

print(np.concatenate((mat_a, mat_b), axis=0))

print(np.concatenate((mat_a, mat_b), axis=1))

# #### Функция np.stack()

# Отличие функции np.stack() от np.concatenate() в том,
# что при объединении массивов мы добавляем новое измерение
print(np.stack((mat_a, mat_b), axis=0))

print(np.stack((mat_a, mat_b), axis=1))

print(np.stack((mat_a, mat_b), axis=2))

# ### Фильтр (маска) массива
#
#

# #### Логическая маска (Boolean mask)

vector_mask = np.array([1, 3, -2, -5, 4, -10, 11])

print(vector_mask > 0)

# применим маску к исходному массиву
print(vector_mask[vector_mask > 0])

# отфильтрованные значения можно заполнить, например, нулями
vector_mask[vector_mask < 0] = 0
print(vector_mask)

# ## Документация
#

# +
# вывод справки по функции с помощью знака вопроса
# print? или ?print
# -

help(print)

# +
# поиск по ключевому слову в документации библиотеки Numpy
# результаты отсортированы по важности
# np.lookfor('randint')
