"""Math and numpy modules."""

# +
# 1


import math
import sys
from math import cos, sin, sqrt

import numpy as np
from numpy.typing import NDArray  # type: ignore


def compute_expression(x_var: float) -> float:
    """Compute a custom mathematical expression based on x_var."""
    try:
        term1: float = math.log(x_var ** (3 / 16), 32)
        term2: float = x_var ** math.cos((math.pi * x_var) / (2 * math.e))
        term3: float = math.sin(x_var / math.pi) ** 2
        return term1 + term2 - term3
    except (ValueError, ZeroDivisionError) as e:
        print(f"Computation error: {e}")
        return float("nan")


def main() -> None:
    """Handle user input and prints the computed result."""
    try:
        y_var: float = float(input("Enter y_var value: "))
        result: float = compute_expression(y_var)
        print(result)
    except ValueError:
        print("Error: please enter a valid number.")


if __name__ == "__main__":
    main()

# +
# 2


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    a_var = int(parts[0])

    for i in range(1, len(parts)):
        b_var = int(parts[i])

        while b_var != 0:
            a_var, b_var = b_var, a_var % b_var

    print(a_var)

# +
# 3


N_var, M_var = map(int, input().split())


def binomial_coefficient(n_var: int, k_var: int) -> int:
    """Return C(n, k) — number of combinations."""
    if 0 <= k_var <= n_var:
        return math.factorial(n_var) // (
            math.factorial(k_var) * math.factorial(n_var - k_var)
        )
    return 0


comb1 = binomial_coefficient(N_var - 1, M_var - 1)
comb2 = binomial_coefficient(N_var, M_var)


print(comb1, comb2)

# +
# 4


inputs_str = input().split()
inputs_val = []

for item in inputs_str:
    inputs_val.append(float(item))

product = 1.0
for num in inputs_val:
    product *= num

geometric_mean = product ** (1 / len(inputs_val))


print(geometric_mean)

# +
# 5


deca_input = input().split()
deca_x = float(deca_input[0])
deca_y = float(deca_input[1])

pola_input = input().split()
pola_r = float(pola_input[0])
pola_f = float(pola_input[1])

pola_x = pola_r * cos(pola_f)
pola_y = pola_r * sin(pola_f)

dx = deca_x - pola_x
dy = deca_y - pola_y
distance = sqrt(dx * dx + dy * dy)


print(distance)

# +
# 6


def multiplication_matrix(size: int) -> NDArray[np.int64]:
    """Generate a size x size multiplication table matrix."""
    row = np.arange(1, size + 1)
    col = row[:, np.newaxis]
    return row * col


print(multiplication_matrix(3))

# +
# 7


def make_board(size: int) -> NDArray[np.int8]:
    """Generate an n x n chessboard pattern as a matrix of 0s and 1s."""
    indices = np.indices((size, size))
    board = (indices[0] + indices[1]) % 2
    rotated_board = np.rot90(board)
    return rotated_board.astype(np.int8)


print(make_board(4))

# +
# 8


def snake(width: int, height: int, direction: str = "H") -> NDArray[np.int16]:
    """Generate a matrix filled in a snake-like pattern."""
    matrix = np.zeros((height, width), dtype=np.int16)

    if direction == "H":
        for row in range(height):
            start = row * width + 1
            end = (row + 1) * width + 1
            values: NDArray[np.int16]
            values = np.arange(start, end, dtype=np.int16)
            if row % 2 != 0:
                values = np.ascontiguousarray(values[::-1])
            matrix[row] = values

    elif direction == "V":
        for col in range(width):
            start = col * height + 1
            end = (col + 1) * height + 1
            values = np.arange(start, end, dtype=np.int16)
            if col % 2 != 0:
                values = np.ascontiguousarray(values[::-1])
            matrix[:, col] = values

    return matrix


print(snake(5, 3))

# +
# 9


def rotate(matrix: NDArray[np.int64], angle: int) -> NDArray[np.int64]:
    """Rotate a matrix by a given angle in degrees (clockwise)."""
    k_var = (360 - angle) // 90
    return np.rot90(matrix, k_var)


print(rotate(np.arange(12).reshape(3, 4), 90))

# +
# 10


def stairs(vector: NDArray[np.int64]) -> NDArray[np.int64]:
    """Create a matrix with a row as a vector shifted right by its index."""
    size = len(vector)
    result = np.zeros((size, size), dtype=vector.dtype)

    for row in range(size):
        result[row] = np.roll(vector, row)

    return result


print(stairs(np.arange(3)))
