"""Модули math и numpy."""

# +
from __future__ import annotations
import numpy as np
import math
import sys
from math import cos, sin, sqrt


# 1
def compute_expression_1(x_val: float) -> float:
    """Вычисляет пользовательское математическое выражение на основе x_val."""
    try:
        term1: float = math.log(x_val ** (3 / 16), 32)
        term2: float = x_val ** math.cos((math.pi * x_val) / (2 * math.e))
        term3: float = math.sin(x_val / math.pi) ** 2
        return term1 + term2 - term3
    except (ValueError, ZeroDivisionError):
        return float("nan")


# -

# 2
def process_gcd_2() -> None:
    """Обрабатывает ввод и вычисляет НОД для каждой строки."""
    for line in sys.stdin:
        line_clean = line.strip()
        if not line_clean:
            continue

        parts = line_clean.split()
        current_gcd = int(parts[0])

        for i in range(1, len(parts)):
            next_num = int(parts[i])
            while next_num != 0:
                current_gcd, next_num = next_num, current_gcd % next_num


# 3
def binomial_coefficient_3(n_val: int, k_val: int) -> int:
    """Возвращает C(n, k) — количество комбинаций."""
    if 0 <= k_val <= n_val:
        numerator = math.factorial(n_val)
        denominator = math.factorial(k_val) * math.factorial(n_val - k_val)
        return numerator // denominator
    return 0


# 4
def geometric_mean_4(numbers: list[float]) -> float:
    """Вычисляет среднее геометрическое чисел."""
    product = 1.0
    for num in numbers:
        product *= num
    
    result: float = product ** (1 / len(numbers))
    return result


# +
# 5
def polar_to_cartesian_5(radius: float, angle: float) -> tuple[float, float]:
    """Преобразует полярные координаты в декартовы."""
    x_coord = radius * cos(angle)
    y_coord = radius * sin(angle)
    return x_coord, y_coord


def distance_between_points_5(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    """Вычисляет расстояние между двумя точками."""
    delta_x = x1 - x2
    delta_y = y1 - y2
    return sqrt(delta_x * delta_x + delta_y * delta_y)


# -

# 6
def multiplication_matrix_6(size: int) -> np.ndarray:
    """Генерирует матрицу таблицы умножения размером size x size."""
    row_vector = np.arange(1, size + 1)
    column_vector = row_vector[:, np.newaxis]
    result: np.ndarray = row_vector * column_vector
    return result


# 7
def make_board_7(size: int) -> np.ndarray:
    """Генерирует шахматную доску размером n x n в виде матрицы 0 и 1."""
    indices = np.indices((size, size))
    board_pattern = (indices[0] + indices[1]) % 2
    rotated_board = np.rot90(board_pattern)
    result: np.ndarray = rotated_board.astype(np.int8)
    return result


# 8
def snake_8(
    width: int, 
    height: int, 
    direction: str = "H"
) -> np.ndarray:
    """Генерирует матрицу, заполненную в змеевидном порядке."""
    matrix = np.zeros((height, width), dtype=np.int16)

    if direction == "H":
        for row_index in range(height):
            start_val = row_index * width + 1
            end_val = (row_index + 1) * width + 1
            row_values = np.arange(start_val, end_val, dtype=np.int16)
            if row_index % 2 != 0:
                row_values = np.ascontiguousarray(row_values[::-1])
            matrix[row_index] = row_values

    elif direction == "V":
        for col_index in range(width):
            start_val = col_index * height + 1
            end_val = (col_index + 1) * height + 1
            col_values = np.arange(start_val, end_val, dtype=np.int16)
            if col_index % 2 != 0:
                col_values = np.ascontiguousarray(col_values[::-1])
            matrix[:, col_index] = col_values

    return matrix


# 9
def rotate_9(matrix: np.ndarray, angle: int) -> np.ndarray:
    """Поворачивает матрицу на заданный угол в градусах (по часовой стрелке)."""
    rotations_count = (360 - angle) // 90
    result: np.ndarray = np.rot90(matrix, rotations_count)
    return result


# 10
def stairs_10(vector: np.ndarray) -> np.ndarray:
    """Создает матрицу со строками как вектор, сдвинутый вправо по индексу."""
    size = len(vector)
    result_matrix = np.zeros((size, size), dtype=vector.dtype)

    for row_index in range(size):
        result_matrix[row_index] = np.roll(vector, row_index)

    return result_matrix
