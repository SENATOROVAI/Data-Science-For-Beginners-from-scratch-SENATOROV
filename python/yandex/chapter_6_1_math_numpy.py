"""Math and numpy modules."""

# # Math library
#
# ### Combinatorial and Number Theory Functions
#
# - `math.comb(n, k)`: Returns the number of ways to choose `k` elements from `n` elements without repetition and order.
#
#   $$
#   \binom{n}{k} = \frac{n!}{k!(n-k)!}
#   $$
#
#   ```python
#   import math
#
#   print(math.comb(12, 3))  # 220
#   ```
#
# - `math.factorial(x)`: Computes the factorial of a non-negative integer `x`.
#
# $$
# x! = x \times (x - 1) \times (x - 2) \times \dots \times 2 \times 1
# $$
#   ```python
#   print(math.factorial(5))  # 120
#   ```
#
# - `math.gcd(*integers)`: Returns the greatest common divisor (GCD) of given numbers (available from Python 3.9).
#
# $$
# \gcd(a, b) =
# \begin{cases}
# b, & \text{if } a \mod b = 0 \\
# \gcd(b, a \mod b), & \text{otherwise}
# \end{cases}
# $$
#   ```python
#   print(math.gcd(120, 210, 360))  # 30
#   ```
#
# - `math.lcm(*integers)`: Returns the least common multiple (LCM) of given numbers (available from Python 3.9).
#
# $$
# \operatorname{lcm}(a, b) = \frac{|a \times b|}{\gcd(a, b)}
# $$
#   ```python
#   print(math.lcm(10, 20, 30, 40))  # 120
#   ```
#
# - `math.perm(n, k=None)`: Returns the number of permutations of `n` elements taken `k` at a time.
#
# $$
# P(n, k) = \frac{n!}{(n - k)!}
# $$
#
#   ```python
#   print(math.perm(4, 2))  # 12
#   print(math.perm(4))  # 24
#   ```
#
# - `math.prod(iterable, start=1)`: Computes the product of elements in an iterable.
#   ```python
#   print(math.prod(range(10, 21)))  # 6704425728000
#   ```
#
# ### Exponential and Logarithmic Functions
#
# - `math.exp(x)`: Returns `e^x`.
#   ```python
#   print(math.exp(3.5))  # 33.11545195869231
#   ```
#
# - `math.log(x, base)`: Computes logarithm of `x` to a given base. Defaults to natural logarithm if `base` is not provided.
#   ```python
#   print(math.log(10))  # 2.302585092994046
#   print(math.log(10, 2))  # 3.3219280948873626
#   ```
#
# - `math.pow(x, y)`: Computes `x^y`, converting arguments to float.
#   ```python
#   print(math.pow(2, 10))  # 1024.0
#   print(math.pow(4.5, 3.7))  # 261.1477575641718
#   ```
#
# ### Trigonometric Functions
#
# Available functions:
# - `math.sin(x)`, `math.cos(x)`, `math.tan(x)`
# - `math.asin(x)`, `math.acos(x)`, `math.atan(x)`
#
# - `math.dist(p, q)`: Computes the Euclidean distance between points `p` and `q`.
#
# $$
# \operatorname{dist}(p, q) = \sqrt{(q_1 - p_1)^2 + (q_2 - p_2)^2 + \dots + (q_n - p_n)^2}
# $$
#   ```python
#   print(math.dist((0, 0, 0), (1, 1, 1)))  # 1.7320508075688772
#   ```
#
# - `math.hypot(*coordinates)`: Computes the length of a vector with given coordinates.
#
# $$
# c = \sqrt{a^2 + b^2}
# $$
#   ```python
#   print(math.hypot(1, 1, 1))  # 1.7320508075688772
#   print(math.hypot(3, 4))  # 5.0
#   ```
#
# ### Angle Conversion Functions
#
# - `math.degrees(x)`: Converts radians to degrees.
#   ```python
#   print(round(math.degrees(math.asin(0.5)), 1))  # 30.0
#   ```
#
# - `math.radians(x)`: Converts degrees to radians.
#   ```python
#   print(round(math.sin(math.radians(30)), 1))  # 0.5
#   ```
#
# ### Hyperbolic Functions
#
# Available functions:
# - `math.acosh(x)`, `math.asinh(x)`, `math.atanh(x)`
# - `math.cosh(x)`, `math.sinh(x)`, `math.tanh(x)`
#
# ### Special Functions
#
# - `math.gamma(x)`: Computes the Gamma function, which generalizes the factorial function.
#
# $$
# \Gamma(n) = (n - 1)!
# $$
#   ```python
#   print(math.gamma(3))  # 2.0
#   print(math.gamma(3.5))  # 3.323350970447842
#   print(math.gamma(4))  # 6.0
#   ```
#
# ### Constants
#
# - `math.pi`: The mathematical constant π.
# - `math.e`: The mathematical constant e.
#
#
# # numpy
#
# ### Create an array
#
# ```python
# import numpy as np
#
# a = np.array([1, 2, 3, 4])
# b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print(f"a[0] = {a[0]}")
# print(f"b[0] = {b[0]}")
# ```
#
# #### **Understanding Dimensions and Axes**
# - **Array `a` (1D):**
#   - Has **one axis** (`axis 0`) of length **4**.
#   - Example: `[1, 2, 3, 4]`
#
# - **Array `b` (2D):**
#   - Has **two axes**:
#     - **Axis 0 (rows)**: length **4**
#     - **Axis 1 (columns)**: length **2**
#   - Example:
#     ```
#     [[1 2]
#      [3 4]
#      [5 6]
#      [7 8]]
#     ```
#
# In NumPy, arrays are instances of the **`ndarray` (N-dimensional array) class**. The most important attributes of `ndarray` include:
#
# ### *Key Attributes of `ndarray`**
#
# `ndarray.ndim` – Number of Dimensions (Axes)
# - Represents the **number of axes (dimensions)** of the array.
# - Also known as the **rank** of the array.
#
# ```python
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a.ndim)  # Output: 2 (2D array)
# ```
#
# ---
#
# `ndarray.shape` – Shape of the Array
# - A **tuple** that contains the number of elements along each axis.
# - The length of `shape` corresponds to the **number of dimensions (`ndim`)**.
#
# **Example:**
# ```python
# print(a.shape)  # Output: (2, 3) → 2 rows, 3 columns
# ```
#
# `ndarray.size` – Total Number of Elements
# - Returns the **total number of elements** in the array.
# - Computed as the **product of all shape dimensions**.
#
# **Example:**
# ```python
# print(a.size)  # Output: 6 (since 2 * 3 = 6)
# ```
#
# `ndarray.dtype` – Data Type of Elements
# - Specifies the **data type** of array elements (e.g., `int32`, `float64`, etc.).
#
# **Example:**
# ```python
# print(a.dtype)  # Output: int32
# ```
#
#
# `ndarray.itemsize` – Memory Size of One Element (Bytes)
# - Returns the **size of each element** in bytes.
#
# **Example:**
# ```python
# print(a.itemsize)  # Output: 8
# ```
#
#
# NumPy provides **built-in data types** that are similar to **C programming language types**.
# These data types define how many bytes each element in an array occupies in memory and determine the **range of values** that can be stored.
#
#
# `np.zeros()` - Create arrays filled with zeros. It takes a **shape tuple** and an optional **data type**.
#
# ```python
# import numpy as np
#
# # 4x3 array of zeros (default: float64)
# a = np.zeros((4, 3))
# print(a)
#
# # 4x3 array of integer zeros
# a = np.zeros((4, 3), dtype="int32")
# print(a)
# ```
#
# **Output**
# ```
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
#
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]
#  [0 0 0]]
# ```
#
# `np.ones()` - Create an array filled with ones. It works similarly to `np.zeros()` but fills the array with **1s** instead of **0s**.
# `np.eye()`  - Create an **identity matrix**, meaning a square matrix with **1s on the main diagonal** and **0s elsewhere**.
#
#
# `np.arange()` - Generates an array with values in a specified range. It is similar to Python's built-in `range()` function but **returns a NumPy array** and supports **floating-point** values.
#
# The function **takes up to three parameters**:
# - `start` → The starting value (inclusive).
# - `stop` → The stopping value (exclusive).
# - `step` → The increment (optional, default is `1`).
#
# ```python
# import numpy as np
#
# # Create an array from 1 to 9 (default step = 1)
# a = np.arange(1, 10)
# print(a)
#
# # Create an array from 1 to 5 with a step of 0.4 (supports floating-point steps)
# a = np.arange(1, 5, 0.4)
# print(a)
# ```
#
# **Output**
# ```
# [1 2 3 4 5 6 7 8 9]
#
# [1.  1.4 1.8 2.2 2.6 3.  3.4 3.8 4.2 4.6]
# ```
#
# `np.linspace()` - Generates an array of evenly spaced values over a specified range. Unlike `np.arange()`, which requires a step size, `np.linspace()` lets you specify the **number of values**.
#
#
# The function takes the following parameters:
# - `start` → The starting value (inclusive).
# - `stop` → The ending value (inclusive).
# - `num` → The number of values to generate (default is `50`).
#
#
# ```python
# import numpy as np
#
# # Create an array of 10 evenly spaced values from 1 to 5
# a = np.linspace(1, 5, 10)
# print(a)
# ```
#
# **Output**
# ```
# [1.  1.44444444 1.88888889 2.33333333 2.77777778 3.22222222 3.66666667 4.11111111 4.55555556 5.]
# ```
#
# `np.reshape()` - Allow changing the shape of an array **without changing its total number of elements**. The function returns a new array with the specified shape.
#
#
# The function takes a **tuple** specifying the new shape.
#
# ### **Example Code**
# ```python
# import numpy as np
#
# # Create a 4x3 array of zeros
# a = np.zeros((4, 3), dtype="uint8")
# print(a)
#
# print()
#
# # Reshape into a 2x6 array
# a = a.reshape((2, 6))
# print(a)
# ```
#
# **Output**
# ```
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]
#  [0 0 0]]
#
# [[0 0 0 0 0 0]
#  [0 0 0 0 0 0]]
# ```
#
# `resize()` - Modifies the original array's shape, **unlike `reshape()`**, which returns a new array.
#
# The `resize()` method **directly changes the shape** of the array in place.
#
# - **Modifies the original array in place**.
# - If the new size is **larger**, new elements are **filled with zeros**.
# - If the new size is **smaller**, excess elements are **discarded**.
#
# ```python
# import numpy as np
#
# # Create a 4x3 array of zeros
# a = np.zeros((4, 3), dtype="uint8")
# print(a)
#
# print()
#
# # Resize into a 3D shape (2x2x3)
# a.resize((2, 2, 3))
# print(a)
# ```
#
# **Output**
# ```
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]
#  [0 0 0]]
#
# [[[0 0 0]
#   [0 0 0]]
#
#  [[0 0 0]
#   [0 0 0]]]
# ```
#
# When `-1` is used, NumPy calculates the missing dimension based on the total number of elements.
#
# NumPy provides **element-wise** mathematical operations on arrays, including **arithmetic, trigonometric, and exponential functions**. When performing operations, the **dimensions of the arrays must match** or be **broadcastable**.
#
# ```
# import numpy as np
#
# a = np.array([9, 8, 7])
# b = np.array([1, 2, 3])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# ```
#
# In NumPy, **matrix multiplication** can be performed using the **`@` operator** or the **`np.dot()`**
#
# ```
# import numpy as np
#
# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# b = np.array([[0, 0, 1],
#               [0, 1, 0],
#               [1, 0, 0]])
# print(a @ b)
# ```
#
#
# Transpose (`np.transpose()` or `.T`)
#
# Swaps rows and columns.
#
# ```python
# import numpy as np
#
# A = np.array([[1, 2, 3], [4, 5, 6]])
# print(A.T)  # Same as np.transpose(A)
# ```
# **Output:**
# ```
# [[1 4]
#  [2 5]
#  [3 6]]
# ```
#
# ---
#
# Rotate (`np.rot90()`)
#
# Rotate the matrix **90° counterclockwise** (default).
#
# ```python
# print(np.rot90(A))  # Rotate 90° CCW
# print(np.rot90(A, k=2))  # Rotate 180°
# print(np.rot90(A, k=-1))  # Rotate 90° CW
# ```
#
# Functions for calculating the sum of array elements, finding the minimum and maximum elements, and many others by default operate on all elements of the array, ignoring its dimensionality:
#
# ```python
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a.sum())  # Sum of all elements
# print(a.min())  # Minimum element
# print(a.max())  # Maximum element
# ```
#
# This Python code demonstrates the use of NumPy functions with the `axis` parameter, allowing calculations along specific dimensions of a 2D array.
#
# Key Concepts:
# - The `axis=0` parameter performs operations along columns (vertically).
# - The `axis=1` parameter performs operations along rows (horizontally).
#
# Code Breakdown:
# ```python
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# print(a.sum(axis=0))  # Sum of numbers in each column
# print(a.sum(axis=1))  # Sum of numbers in each row
# print(a.min(axis=0))  # Minimum value in each column
# print(a.max(axis=1))  # Maximum value in each row
# ```
#
# This Python script demonstrates how to perform slicing operations on NumPy arrays.
# Slicing in NumPy allows extracting specific sections of an array by specifying row and column ranges.
#
#
# **Key Concepts:**
# - In **1D arrays**, slicing works like standard Python lists.
# - In **2D arrays**, slicing can be applied separately for rows and columns using the format:
# array[row_start:row_end, col_start:col_end]
#
#
# ```
# mport numpy as np
#
# # Creating a 3x4 array with values from 1 to 12
# a = np.arange(1, 13).reshape(3, 4)
#
# print(a)  # Printing the full array
# print()
#
# # Selecting the first two rows and last two columns
# print(a[:2, 2:])
# print()
#
# # Selecting all rows and every second column
# print(a[:, ::2])
# ```
#
# n NumPy, the flat attribute is used to iterate over a multidimensional array as if it were a 1D array. This allows easy access to each element sequentially

# +
import math
from math import cos, dist, sin
from sys import stdin

import numpy as np
from numpy.typing import NDArray  # type: ignore

# ! pip install --upgrade numpy

# +
# 1


x_val = float(input())

# fmt: off
result = (
    math.log(math.pow(x_val, 3 / 16), 32) +  # noqa: W504
    math.pow(x_val, math.cos((math.pi * x_val) / (2 * math.e))) -  # noqa: W504
    math.pow(math.sin(x_val / math.pi), 2)
)
# fmt: on

print(result)

# +
# 2


for line in stdin:
    numbers = map(int, line.split())
    print(math.gcd(*numbers))

# +
# 3

N_val, M_val = map(int, input().split())
print(math.comb(N_val - 1, M_val - 1), math.comb(N_val, M_val))

# +
# 4


inputs_val = list(map(float, input().split()))

geometric_mean = math.pow(math.prod(inputs_val), 1 / len(inputs_val))
print(geometric_mean)

# +
# 5


deca_x, deca_y = map(float, input().split())
pola_r, pola_f = map(float, input().split())
pola_x = pola_r * cos(pola_f)
pola_y = pola_r * sin(pola_f)
print(dist((deca_x, deca_y), (pola_x, pola_y)))

# +
# 6


def multiplication_matrix(size: int) -> NDArray[np.int64]:
    """Create an n x n multiplication table matrix."""
    matrix = np.arange(1, size + 1)
    return matrix * matrix.reshape(-1, 1)


# +
# 7


def make_board(num: int) -> NDArray[np.int8]:
    """Create a chessboard pattern matrix of size n x n."""
    matrix = np.indices((num, num)).sum(axis=0) % 2
    return np.array(np.rot90(matrix), dtype="int8")


# +
# 8


def snake(width: int, height: int, direction: str = "H") -> NDArray[np.int16]:
    """Create a snake pattern matrix of size N x M."""
    matrix = np.zeros((height, width), dtype=np.int16)

    if direction == "H":
        for i in range(height):
            if i % 2 == 0:
                matrix[i] = np.arange(i * width + 1, (i + 1) * width + 1)
            else:
                matrix[i] = np.arange((i + 1) * width, i * width, -1)
    elif direction == "V":
        for j_w in range(width):
            if j_w % 2 == 0:
                array_val = np.arange(j_w * height + 1, (j_w + 1) * height + 1)
                matrix[:, j_w] = array_val
            else:
                array_val = np.arange((j_w + 1) * height, j_w * height, -1)
                matrix[:, j_w] = array_val

    return matrix


# +
# 9


def rotate(matrix: NDArray[np.int64], angle: int) -> NDArray[np.int64]:
    """Rotate a matrix by the angle in degrees (must be multiple of 90)."""
    return np.rot90(matrix, (360 - angle) // 90)


# +
# 10


def stairs(vector: NDArray[np.int64]) -> NDArray[np.int64]:
    """Create a matrix where row is the vector shifted right by row index."""
    size = len(vector)
    matrix = np.zeros((size, size), dtype=vector.dtype)

    for i_val in range(size):
        matrix[i_val] = np.roll(vector, i_val)

    return matrix
