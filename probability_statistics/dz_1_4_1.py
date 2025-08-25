"""ДЗ 1. Блок 4. Основы линейной алгебры и матана для машинного обучения.

Курс ня Яндекс "Линейная алгебра".
"""

# +
import numpy as np
import pandas as pd

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# +
# 4.2 Задача A
import sys


# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    lines = input.split('\n')
    ptr = 0
    
    # Чтение количества векторов и коэффициентов
    input = lines[0]
    # k = int(input[ptr])
    k = int(input[0])
    # print(f'k={k}')
    ptr += 1
    
    # Чтение коэффициентов
    # lambdas = list(map(float, input[ptr:ptr+k]))
    input   = lines[1]
    input_l = input.split(' ')
    lambdas = list(map(float, input_l[0:0+k]))
    # print(f'lambdas={lambdas}')
    ptr += k
    
    # Чтение векторов
    vectors = []
    n = None  # размерность векторов
    for vector_i in range(k):
        input   = lines[1 + vector_i + 1]
        input_l = input.split(' ')

        n = len(input_l)
        # vector = list(map(float, input[ptr:ptr + len(input)]))  # временно читаем все оставшиеся данные
        vector = list(map(float, input_l[0:0 + n]))  # временно читаем все оставшиеся данные
        # if n is None:
        #     # Определяем размерность по первому вектору
        #     n = len(vector)
        #     ptr += n
        # else:
        #     ptr += n
        vectors.append(vector[:n])  # берем только первые n элементов
    
    # print(f'[DEBUG] vectors={vectors}')

    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    # Вычисление линейной комбинации
    result = [0.0] * n
    for i in range(k):
        for j in range(n):
            result[j] += lambdas[i] * vectors[i][j]
    
    # Форматирование вывода с точностью до 2 знаков после запятой
    print(' '.join([f"{x:.2f}" for x in result]))


if __name__ == '__main__':
    # main()
    
    input = '3' + '\n' + \
            '1.5 -2 0.5' + '\n' + \
            '1 2 3' + '\n' + \
            '4 5 6' + '\n' + \
            '7 8 9'
    main(input)

# +
# 4.2 Задача B
import sys

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    line = input_1[0].split(' ')
    
    # Чтение количества векторов и коэффициентов
    n = int(line[0])
    
    # Чтение векторов
    vectors = []
    for vector_i in range(2):
        line = input_1[vector_i + 1].split(' ')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    # Вычисление ортогональности через dot product
    result = 0
    v_1 = vectors[0]
    v_2 = vectors[1]
    for i in range(n):
        result += v_1[i] * v_2[i]
    
    res_str = None
    if result == 0:
        res_str = 'ORTHOGONAL'
    else:
        res_str = 'NON-ORTHOGONAL'

    # Форматирование вывода с точностью до 2 знаков после запятой
    print(f'{res_str}')


if __name__ == '__main__':
    # main()
    
    input = '2' + '\n' + \
            '1 0' + '\n' + \
            '0 1'
    main(input)

# +
# 4.2 Задача C
import sys

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    
    # Чтение векторов
    n = 2
    
    vectors = []
    for vector_i in range(3):
        line = input_1[vector_i].split(' ')
        # print(f'[DEBUG] {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    # Вычисление ортогональности через dot product
    result = 0
    v1 = vectors[0]
    v2 = vectors[1]
    v3 = vectors[2]

    # Метод Крамера
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    
    # Вычисляем определитель матрицы коэффициентов
    determinant = x1 * y2 - x2 * y1

    if determinant == 0:
        # Если определитель равен 0, векторы v1 и v2 коллинеарны.
        # v3 может быть их комбинацией только если он тоже коллинеарен им.
        # Это происходит, если v3 = k * v1 для некоторого k, или v3 = k * v2.
        # Проверим, является ли v3 нулевым вектором.
        if x3 == 0 and y3 == 0:
            # print("possible")
            print("0 0")
            return

            if x1 == 0 and y1 == 0:
                # v1 - нулевой вектор.
                if x2 == 0 and y2 == 0:
                    # Оба вектора v1 и v2 нулевые.
                    if x3 == 0 and y3 == 0:
                        # print("possible")
                        print("0 0")
                    else:
                        print("NO_SOLUTION")
    else:
        # Вычисляем числители для λ1 и λ2 по правилу Крамера
        det_lambda1 = x3 * y2 - x2 * y3
        det_lambda2 = x1 * y3 - x3 * y1

        # Проверяем, являются ли решения целочисленными
        if det_lambda1 % determinant == 0 and det_lambda2 % determinant == 0:
            lambda1 = det_lambda1 // determinant
            lambda2 = det_lambda2 // determinant

            # print(f"[DEBUG] check {lambda1 * x1 + lambda2 * x2} {lambda1 * y1 + lambda2 * y2}")
            # Проверяем, что найденные коэффициенты действительно дают v3
            if lambda1 * x1 + lambda2 * x2 == x3 and lambda1 * y1 + lambda2 * y2 == y3:
                # print("possible")
                print(f"{lambda1:.0f} {lambda2:.0f}")
            else:
                print("NO_SOLUTION")
        else:
            print("NO_SOLUTION")


if __name__ == '__main__':
    # main()
    
    input = '2 3' + '\n' + \
            '4 -1' + '\n' + \
            '16 3'
    main(input)

# +
# 4.2 Задача D
import sys
import math


def dot_product(v1, v2):    
    """Скалярное произведение двух векторов."""
    return sum(x * y for x, y in zip(v1, v2))

def magnitude(v):
    """Длина (норма) вектора."""
    return math.sqrt(sum(x**2 for x in v))

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    
    line = input_1[0].split(' ')
    
    # Чтение количества векторов
    n = int(line[0])
    
    vectors = []
    for vector_i in range(2):
        line = input_1[1 + vector_i].split(' ')
        # print(f'[DEBUG] {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    # Вычисление ортогональности через dot product
    result = 0
    v1 = vectors[0]
    v2 = vectors[1]

    # скалярное произведение
    dot_p = dot_product(v1, v2)

    # длины векторов
    mag_v1 = magnitude(v1)
    mag_v2 = magnitude(v2)
    
    # Вычисляем косинус угла
    # Используем clamp для избежания ошибок из-за малой погрешности
    # при вычислениях с плавающей точкой, которые могут привести
    # к значениям cos(theta) > 1 или cos(theta) < -1.
    cos_theta = dot_p / (mag_v1 * mag_v2)

    # Вычисляем угол в радианах
    theta_rad = math.acos(cos_theta)

    # Переводим угол в градусы
    theta_deg = math.degrees(theta_rad)

    # Округляем до целого числа, отбрасывая дробную часть
    print(int(theta_deg))


if __name__ == '__main__':
    # main()
    
    input = '2' + '\n' + \
            '1 0' + '\n' + \
            '0 1'
    main(input)

# +
# 4.2 Задача E
import sys
import math


def rank_of_matrix(matrix):
    """Вычисляет ранг матрицы с использованием метода Гаусса."""
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])

    rank = 0
    pivot_row = 0
    for j in range(cols):
        if pivot_row >= rows:
            break
        
        # Находим строку с ненулевым элементом в текущем столбце
        i = pivot_row
        while i < rows and matrix[i][j] == 0:
            i += 1
        
        # Если нашли, меняем строки местами
        if i < rows:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
            
            # Приводим ведущий элемент к 1 (необязательно, но упрощает)
            # pivot_value = matrix[pivot_row][j]
            # for k in range(j, cols):
            #     matrix[pivot_row][k] /= pivot_value
            
            # Обнуляем элементы под ведущим
            for i in range(rows):
                if i != pivot_row:
                    factor = matrix[i][j] / matrix[pivot_row][j]
                    for k in range(j, cols):
                        matrix[i][k] -= factor * matrix[pivot_row][k]
            
            pivot_row += 1
            rank += 1
    
    return rank

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    
    line = input_1[0].split(' ')
    
    # m - количества векторов, n - размерность
    m = int(line[0])
    n = int(line[1])
    
    vectors = []
    for vector_i in range(m):
        line = input_1[1 + vector_i].split(' ')
        # print(f'[DEBUG] {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    # Векторы - это строки матрицы
    matrix = vectors

    # Вычисляем ранг
    matrix_copy = [row[:] for row in matrix] # Создаем копию, чтобы не изменять исходные данные
    
    # Учитываем, что может быть разная размерность m и n
    effective_rank = rank_of_matrix(matrix_copy)
    
    # Если количество векторов (строк) больше их размерности (столбцов),
    # они всегда линейно зависимы.
    if m > n:
        print("LINEARLY_DEPENDENT")
        return
    
    # Сравниваем ранг с количеством векторов (m)
    if effective_rank == m:
        print("LINEARLY_INDEPENDENT")
    else:
        print("LINEARLY_DEPENDENT")


if __name__ == '__main__':
    # main()
    
    input = '2 2' + '\n' + \
            '1 0' + '\n' + \
            '0 1'
    main(input)

# +
# 4.3 Задача A
import sys


def is_diagonal(matrix):
    """Проверка диагональная ли М."""
    result = True

    for row_i in range(len(matrix)):
        row = matrix[row_i]
        for column_i in range(len(row)):
            row_n = row_i+1
            column_n = column_i+1
            cell_value = row[column_i]
            
            # print(f'{(row_i+1),column_i+1} {cell_value}')

            is_diagonal_cell = False
            if row_n == column_n:
                is_diagonal_cell = True
            
            if not is_diagonal_cell:
                if cell_value != 0:
                    result = False

    return result
    
def is_upper_tr(matrix):
    """Проверка верхнетреугольная ли М."""
    result = True

    for row_i in range(len(matrix)):
        row = matrix[row_i]
        for column_i in range(len(row)):
            row_n = row_i+1
            column_n = column_i+1
            cell_value = row[column_i]
            
            # print(f'{(row_i+1),column_i+1} {cell_value}')

            is_down_tr_cell = False
            if row_n > column_n:
                is_down_tr_cell = True
            
            if is_down_tr_cell:
                if cell_value != 0:
                    result = False

    return result
    
def is_lower_tr(matrix):
    """Проверка нижнетреугольная ли М."""
    result = True

    for row_i in range(len(matrix)):
        row = matrix[row_i]
        for column_i in range(len(row)):
            row_n = row_i+1
            column_n = column_i+1
            cell_value = row[column_i]
            
            # print(f'{(row_i+1),column_i+1} {cell_value}')

            is_up_tr_cell = False
            if row_n < column_n:
                is_up_tr_cell = True
            
            if is_up_tr_cell:
                if cell_value != 0:
                    result = False

    return result


# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    
    line = input_1[0].split(' ')
    
    # n - размер М
    n = int(line[0])
    
    vectors = []
    for vector_i in range(n):
        line = input_1[1 + vector_i].split(' ')
        # print(f'[DEBUG] {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    # Векторы - это строки матрицы
    matrix = vectors

    is_diagonal_M = is_diagonal(matrix)
    is_upper_tr_M = is_upper_tr(matrix)
    is_lower_tr_M = is_lower_tr(matrix)
    
    # Если количество векторов (строк) больше их размерности (столбцов),
    # они всегда линейно зависимы.
    if is_diagonal_M:
        print("DIAGONAL")
        return
        
    if is_upper_tr_M:
        print("UPPER_TRIANGULAR")
        return
        
    if is_lower_tr_M:
        print("LOWER_TRIANGULAR")
        return

    print("OTHER")


if __name__ == '__main__':
    # main()
    input = '2' + '\n' + \
            '1 0' + '\n' + \
            '0 1'
    main(input)

    print()
    input = '3' + '\n' + \
            '5 3 4' + '\n' + \
            '0 2 9' + '\n' + \
            '0 0 7'
    main(input)

    print()
    input = '3' + '\n' + \
            '5 0 0' + '\n' + \
            '3 2 0' + '\n' + \
            '4 5 7'
    main(input)

    print()
    input = '2' + '\n' + \
            '1 4' + '\n' + \
            '4 1'
    main(input)

# +
# 4.3 Задача B
import sys


def read_M(input_1, start_i):
    """Чтение М."""
    line = input_1[start_i + 0].split(' ')
        
    # m - строк, n - столбцов
    m = int(line[0])
    n = int(line[1])
    
    vectors = []
    for vector_i in range(m):
        line = input_1[start_i + 1 + vector_i].split(' ')
        # print(f'[DEBUG] {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    return vectors

def shape(matrix):
    """Размер М."""
    row_n    = len(matrix)
    column_n = len(matrix[0])

    return (row_n, column_n)

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    
    # Векторы - это строки матрицы
    matrix_A = read_M(input_1, 0)
    matrix_B = read_M(input_1, 1+len(matrix_A))
    
    shape_A = shape(matrix_A)
    shape_B = shape(matrix_B)

    # Проверка: согласованы ли по размерам
    if shape_A[1] != shape_B[0]:
        print("NOT_DEFINED")
        return
    
    matrix_C = []
    for row_n in range(1, shape_A[0]+1):
        row = []

        for column_n in range(1, shape_B[1]+1):
            cell_value = 0
            
            for t in range(1, shape_A[1]+1):
                cell_value += \
                        matrix_A[row_n-1][t-1] * \
                        matrix_B[t-1][column_n-1]
                
            row.append(cell_value)            
            # print(f'{row_n},{column_n}: {cell_value}')
        matrix_C.append(row)

    # print C
    shape_C = shape(matrix_C)
    for row_n in range(1, shape_C[0]+1):
        row = []

        row_s = ''
        for column_n in range(1, shape_C[1]+1):
            cell_value = matrix_C[row_n-1][column_n-1]

            row_s += str(int(cell_value)) + ' '
        
        print(row_s)


if __name__ == '__main__':
    # main()
    input = '2 2' + '\n' + \
            '1 0' + '\n' + \
            '0 1' + '\n' + \
            '2 3' + '\n' + \
            '1 0 3' + '\n' + \
            '0 1 0'
    main(input)

# +
# 4.3 Задача С
import sys
import numpy as np


def read_M_sq(input_1, start_i):
    """Чтение квадратной М."""
    line = input_1[start_i + 0].split(' ')
        
    # n - столбцов
    n = int(line[0])
    
    vectors = []
    for vector_i in range(n):
        line = input_1[start_i + 1 + vector_i].split(' ')
        # print(f'[DEBUG] {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    return vectors

def shape(matrix):
    """Размер М."""
    row_n    = len(matrix)
    column_n = len(matrix[0])

    return (row_n, column_n)
    
# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')

    matrix_A = read_M_sq(input_1, 0)
    shape_A = shape(matrix_A)

    n = shape_A[0]
    
    A = np.array(matrix_A)
    
    # print(f'A {matrix_A}')
    
    # Если матрица уже нулевая, то k=1
    if np.allclose(A, 0):
        print(1)
        return
    
    k = 1
    current_power = A.copy()
    
    # Максимальное k не превышает n
    while k <= n:
        k += 1
        current_power = current_power @ A
        if np.allclose(current_power, 0):
            print(k)
            return
            
    # Если дошли до n+1 и не нашли нулевую степень, то матрица не нильпотентна
    print("Матрица не является нильпотентной")


if __name__ == '__main__':
    # main()
    
    input = '2' + '\n' + \
            '0 1' + '\n' + \
            '0 0'
    main(input)

# +
# 4.3 Задача D
import sys
import numpy as np


def read_M(input_1, start_i):
    """Чтение М."""
    line = input_1[start_i + 0].split(' ')
        
    # m - строк, n - столбцов
    m = int(line[0])
    n = int(line[1])
    
    vectors = []
    for vector_i in range(m):
        line = input_1[start_i + 1 + vector_i].split(' ')
        # print(f'[DEBUG] line {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    return vectors

def shape(matrix):
    """Размер М."""
    row_n    = len(matrix)
    column_n = len(matrix[0])

    return (row_n, column_n)

def print_M(matrix):
    """Печать М."""
    shape_M = shape(matrix)
    for row_n in range(1, shape_M[0]+1):
        row = []

        row_s = ''
        for column_n in range(1, shape_M[1]+1):
            cell_value = matrix[row_n-1][column_n-1]

            row_s += str(int(cell_value)) + ' '
        
        print(row_s)

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')

    matrix_A = read_M(input_1, 0)
    shape_A = shape(matrix_A)
    # print(f'matrix_A {matrix_A}')

    A_T = []
    
    for row_n in range(1, shape_A[1]+1):
        row = []
        
        for column_n in range(1, shape_A[0]+1):
            cell_value = matrix_A[column_n-1][row_n-1]

            row.append(cell_value)
            # print(f'{row_n},{column_n}: {cell_value}')

        A_T.append(row)

    print_M(A_T)

if __name__ == '__main__':
    # main()
    
    input = '2 2' + '\n' + \
            '0 1' + '\n' + \
            '0 0'
    main(input)

# +
# 4.3 Задача E
import sys
import numpy as np


def read_M(input_1, start_i):
    """Чтение М."""
    line = input_1[start_i + 0].split(' ')
        
    # m - строк, n - столбцов
    m = int(line[0])
    n = int(line[1])
    
    vectors = []
    for vector_i in range(m):
        # line = input_1[start_i + 1 + vector_i].split(' ')
        line = input_1[start_i + 1 + vector_i].split()
        # print(f'[DEBUG] line {line}')
        vector = list(map(float, line[0:0 + n]))
        vectors.append(vector)
    
    # Проверка корректности данных
    if any(len(v) != n for v in vectors):
        print("[ERROR] все векторы должны иметь одинаковую размерность")
        return
    
    return vectors

def shape(matrix):
    """Размер М."""
    row_n    = len(matrix)
    column_n = len(matrix[0])

    return (row_n, column_n)

def print_M(matrix):
    """Печать М."""
    shape_M = shape(matrix)
    for row_n in range(1, shape_M[0]+1):
        row = []

        row_s = ''
        for column_n in range(1, shape_M[1]+1):
            cell_value = matrix[row_n-1][column_n-1]

            row_s += str(int(cell_value)) + ' '
        
        print(row_s)

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')

    matrix_A = read_M(input_1, 0)
    shape_A = shape(matrix_A)
    # print(f'matrix_A {matrix_A}')
    # print(f'shape_A {shape_A}')
    # print('')

    A_z = []
    
    for row_n in range(1, shape_A[0]+1):
        row = []
        
        for column_n in range(1, shape_A[1]+1):
            # print(f'[DEBUG] {row_n},{column_n}')
            
            # 1. МО
            cell_value_sum = 0
            
            for row_2_n in range(1, shape_A[0]+1):
                cell_value = matrix_A[row_2_n-1][column_n-1]

                cell_value_sum += cell_value
                # print(f'[mean] {row_2_n},{column_n}: {cell_value}')
            cell_value_mean = cell_value_sum/shape_A[0]

            # 2. СКО
            cell_value_rest_sum = 0
            
            for row_2_n in range(1, shape_A[0]+1):
                cell_value = matrix_A[row_2_n-1][column_n-1]

                # cell_value_rest_sum += (cell_value - cell_value_mean)^2
                cell_value_rest_sum += (cell_value - cell_value_mean)**2
            cell_value_rest = cell_value_rest_sum/shape_A[0]
            cell_value_rest_sko = np.sqrt(cell_value_rest)

            cell_value = matrix_A[row_n-1][column_n-1]
            z_score = (cell_value - cell_value_mean) / cell_value_rest_sko
            cell_value = int(z_score)
            
            row.append(cell_value)
            # print(f'{row_n},{column_n}: {cell_value} mean {cell_value_mean} sko {cell_value_rest_sko}')

        A_z.append(row)

    print_M(A_z)

if __name__ == '__main__':
    # main()
    
    input = '2 1' + '\n' + \
            '1' + '\n' + \
            '2'
    main(input)

    print()
    input = '3 1' + '\n' + \
            '2' + '\n' + \
            '5' + '\n' + \
            '1'
    main(input)

    print()
    input = '3 3' + '\n' + \
            '2  2 -2' + '\n' + \
            '5  1 -3' + '\n' + \
            '1  5 -3'
    main(input)
