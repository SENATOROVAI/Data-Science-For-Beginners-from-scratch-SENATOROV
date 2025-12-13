"""Numpy arrays."""

# +
# again import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# importing function csr_matrix()
from scipy.sparse import csr_matrix

# -

# ####  np.array()

# creating array from list
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr

# array from tuple
arr = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
arr

# ####  np.arange()

# like range function but for arrays
# upper limit (not included in the sequence) is a mandatory parameter
arr = np.arange(10)
arr

# +
# stop and step its not mandatory parameters
arr = np.arange(2, 10, 2)

# When using the print() function, commas disappear.
arr
# -

# range() differs in that the float type is not allowed.
list(range(2, 5.5, 0.5))  # type: ignore[call-overload]

np.arange(2, 5.5, 0.5)

# #### Numpy arrays data types

# +
# Although Numpy selects the data type itself it can be specified manually
arr_f = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], float)

print(arr_f)

# and also look at the data type of an individual element using dtype
print(arr_f.dtype)
# -

# ### Properties (attributes) of an array

arr

# ndim allows you to find out the dimensions of the array
arr.ndim

# shape outputs the number of elements in each dimension
arr.shape

# total number of elements in all dimensions
arr.size

# data type of an individual element
# in our case, it is a 64-bit integer
arr.dtype

# size in bytes (8 bits) of one element
# 64 / 8 bits = 8 bytes
arr.itemsize

# total size of the array in bytes (4 elements x 8 bytes)
arr.nbytes

# #### Array dimensions

# #### Zero-dimensional array

# An array with zero dimension is
# a number (square brackets are not needed).
arr_0d = np.array(42)
arr_0d

# Let's display the measurements,
# the elements in each of them,
# and the total number of elements.
print(arr_0d.ndim)
print(arr_0d.shape)
print(arr_0d.size)

# #### One-dimensional array (vector)

# # To create  a vector you need square brackets.
arr_1d = np.array([1, 2, 3])
arr_1d

# lets display its measurements
print(arr_1d.ndim)
print(arr_1d.shape)
print(arr_1d.size)

# #### Two-dimensional array (matrix)

# A two-dimensional array (matrix) is
# a one-dimensional array
# enclosed in a second set of square brackets.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d

# +
print(arr_2d.ndim)
print(arr_2d.shape)

# in this case, two elements of one dimension are
# multiplied by three elements of the second
print(arr_2d.size)
# -

# such a matrix has three rows with one element in each
column = np.array([[1], [2], [3]])
column

# lets look at its shape
column.shape

# in this one there is only one line with three elements
row = np.array([[1, 2, 3]])
row

row.shape

# #### Three-dimensional array

# np.arange() creates a one-dimensional array,
# а np.reshape() distribute elements by measurements
arr_3d = np.arange(12).reshape(2, 2, 3)
arr_3d

# lets look at its attributes
print(arr_3d.ndim)
print(arr_3d.shape)
print(arr_3d.size)

# ### Another ways to create array

# np.zeros()

# we can pass a single value to create a
# one-dimensional array,
# filled with zeros
np.zeros(5)

# or a tuple of numbers
# to indicate the number
# of zeros in each dimension
np.zeros((2, 3))

# np.ones()

# Similarly, you can create an array filled with ones.
np.ones((2, 2, 3))

# np.full()

# Let's create a 2 x 3 matrix
# and fill it with the number four.
np.full((2, 3), 4)

# np.empty()

# Let's create an empty 3 x 2 matrix.
np.empty((3, 2))

# np.zeros_like(), np.ones_like(), np.full_like(), np.empty_like()

# creating a 2 x 3 array with numbers from 1 to 6.
arr = np.arange(1, 7).reshape(2, 3)
arr

# convert it to an array of zeros
np.zeros_like(arr)

# ones array with the same shape as arr
np.ones_like(arr)

# fill it with twos
np.full_like(arr, 2)

# and empty values
np.empty_like(arr)

# np.linspspace()

# create a range from 0 to 0.9 and
# divide it into ten points, including 0 and 0.9
np.linspace(0, 0.9, 10)

# +
# compare with np.arange (here we specify the step)

np.arange(0, 1, 0.1)

# +
# set the graph size in inches
plt.figure(figsize=(8, 6))

# Let's set an interval, for example, from -5 to 5,
# and generate 5000 points on it.
# These will be our coordinates on the x-axis.
x_val = np.linspace(-5, 5, 5000)

# On the y-axis, we will plot a square of these points.
y_val = x_val**2

# let's create a grid
plt.grid()

# let's plot the curve and add labels to the graph
plt.plot(x_val, y_val)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

# the result will be a parabola
plt.show()
# -

# As an example, let's display the first ten points created
# by the np.linspace() function.
x_val[:10]

# np.random.rand() и np.random.randint()

# create an array of a given dimension,
# filled with numbers
# in the interval [0, 1)
np.random.rand(4, 3)

# create an array of integers in a given range
# (the upper limit is not included)
# and with a given dimension
np.random.randint(-3, 3, size=(2, 3, 2))

# np.fromfunction()

# +
# Let's create our own function that takes two numbers
# and raises the first number to the power of the second.


def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base**exponent  # type: ignore[no-any-return]


# -

# apply this function to each cell of the 3 x 3 array
np.fromfunction(power, (3, 3))

# You can also pass a lambda function that
# checks whether two numbers are equal.
np.fromfunction(lambda i, j: i == j, (3, 3))

# Matrix in csr format and the .toarray() method

# Let's create a matrix with predominantly zero values.
arr = np.array([[2, 0, 0, 1, 0, 0, 0], [0, 0, 3, 0, 0, 2, 0], [0, 0, 0, 1, 0, 0, 0]])
arr

# calculate the proportion of zero values
zero_proportion = 1.0 - np.count_nonzero(arr) / arr.size
zero_proportion

# +
# It is convenient to store matrix A in csr format.
b_arr = csr_matrix(arr)

# where the position of the non-zero value and
# the value itself are specified
print(b_arr)
# -

# You can restore a Numpy array using the .toarray() method.
c_arr = b_arr.toarray()
c_arr

# ### Indexing and Slicing

# #### Array element index

# Let's consider a two-dimensional array.
a_arr = np.array([[1, 2, 3], [4, 5, 6]])
a_arr

# The first value of the shape attribute refers
# to the external dimension.
# The second refers to the internal dimension.
a_arr.shape

# let's display the first element of the external dimension
a_arr[0]

# The second index [0] allows you to access
# the elements of the inner dimension.
a_arr[0][0]

# let's display the value six
a_arr[1][2]

# #### Array slicing

# Array 1D

# Let's start with a one-dimensional array
b_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b_arr

# take every second element
# in the range from the 1st to the 6th index
b_arr[1:6:2]

# Array 2D

# Now let's take a two-dimensional array
c_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
c_arr

# let's slice from the first row and the first two columns
c_arr[0, :2]

# Now take both lines in the second column.
c_arr[:, 1]

# display the element in the first row and first column
c_arr[0, 0]

# display the element in the last row and last column
c_arr[-1, -1]

# take every second element from the second row
c_arr[1, ::2]

# 3D array

# create a three-dimensional array
d_arr = np.arange(16).reshape(4, 2, -1)
d_arr

# we will display the value 10
d_arr[2][1][0]

# Let's display the third and fourth matrices [2:]
# and in them the second row [1] and all columns [:]
d_arr[2:, 1, :]

# print the first two matrices of the array.
d_arr[:2]

# display the first rows of each matrix
d_arr[:, 0, :]

# ### Array axes

# #### 2D array

# Let's turn to a two-dimensional array
arr_2d = np.array([[1, 2], [3, 4]])
arr_2d

arr_2d.shape

# Addition along the first axis (axis = 0)

# find the sum across columns (along the 0 axis)
np.sum(arr_2d, axis=0)

# Addition along the second axis (axis = 1)

# and the sum along the lines (along axis 1)
np.sum(arr_2d, axis=1)

# Addition along both axes (axis = (0, 1))

# if you pass a tuple specifying both axes (0, 1)
# the sum will be calculated first along axis 0,
# then along axis 1
np.sum(arr_2d, axis=(0, 1))

# if nothing is specified, the sum will also be calculated
# for all elements of the array
np.sum(arr_2d)

# in this case, the default value
# axis = None is used under the hood
np.sum(arr_2d, axis=None)

# Negative values in the axis parameter

# axis = -1 corresponds to the last axis of the array,
# in this case, axis = 1
np.sum(arr_2d, axis=-1)

# axis = -2 indicates the first axis, i.e. axis = 0
np.sum(arr_2d, axis=-2)

# #### 3D array

arr_3d = np.arange(12).reshape(2, 2, 3)
arr_3d

# Addition along the first axis (axis = 0)

# apply np.sum() with the parameter axis = 0
np.sum(arr_3d, axis=0)

# lets take the first matrix
arr_3d[0]

# second matrix
arr_3d[1]

# and add them up piece by piece
arr_3d[0] + arr_3d[1]

# +
# same thing can be done using a for loop

# create a zero matrix of size 2 x 3
total = np.zeros((2, 3))

# and create a loop of two iterations
for i in range(2):

    # In the first iteration, we will
    # write the first matrix to the zero array,
    # and then add the second matrix to it.
    total += arr_3d[i]

total
# -

# Addition along the second axis (axis = 1)

# apply np.sum()
np.sum(arr_3d, axis=1)

# add up the columns of the first
arr_3d[0][0] + arr_3d[0][1]

# and the second matrix
arr_3d[1][0] + arr_3d[1][1]

# +
# Let's create a zero 2 x 3 matrix
total = np.zeros((2, 3))

# First, let's go through the matrices.
for i in range(2):
    # then along the rows of each matrix
    for row_index in range(2):
        # and in the first row of total, we write the
        # sum of the columns of the first matrix arr_3D,
        # and in the second row, we write
        # the sum of the columns of the second matrix
        total[i] += arr_3d[i][row_index]

total
# -

# Addition along the third axis (axis = 2)

# apply np.sum()
np.sum(arr_3d, axis=2)

# add up the elements of the first row of the first matrix
arr_3d[0][0][0] + arr_3d[0][0][1] + arr_3d[0][0][2]

# second row of the first matrix
arr_3d[0][1][0] + arr_3d[0][1][1] + arr_3d[0][1][2]

# first row of the second matrix
arr_3d[1][0][0] + arr_3d[1][0][1] + arr_3d[1][0][2]

# second row of the second matrix
arr_3d[1][1][0] + arr_3d[1][1][1] + arr_3d[1][1][2]

# +
# Let's create a zero-based 2 x 2 array to record the results
total = np.zeros((2, 2))

# let's go through the matrices
for matrix_idx in range(2):

    # by rows of the matrix
    for row_idx in range(2):

        # and by columns (iterate values of the row)
        for value in arr_3d[matrix_idx][row_idx]:

            # indices matrix_idx, row_idx will record the result of adding
            # the elements of each row into a 2 x 2 result matrix
            total[matrix_idx][row_idx] += value

total
# -

# Addition along the first and second axes (axis = (0, 1))

# apply the np.sum() function
np.sum(arr_3d, axis=(0, 1))

# +
# when using two cycles, we first add the matrices together
total_0 = np.zeros((2, 3))

for i in range(2):
    total_0 += arr_3d[i]

total_0

# +
# and then the columns of these matrices
total_1 = np.zeros(3)

for i in range(2):
    total_1 += total_0[i]

total_1

# +
total = np.zeros(3)

# In two cycles, we will go through the rows of each matrix.
for row_idx in range(2):
    for col_idx in range(2):

        # and add them up piece by piece
        total += arr_3d[row_idx][col_idx]

total
# -

# Addition along all three axes (axis = (0, 1, 2))

np.sum(arr_3d, axis=(0, 1, 2))

np.sum(arr_3d)

# ### Operations with arrays

# #### Function len()

# lets take a three-dimensional array
arr_3d = np.arange(12).reshape(2, 2, 3)
arr_3d

# By default, the len() function outputs the
# length of the external dimension.
# these are outer brackets containing two matrices
len(arr_3d)

# To display the length of the internal
# measurement, i.e., a vector of three elements,
# you need to use indexes.
len(arr_3d[0][0])

# #### Entering an array

# Let's check if the value 3 is included in the arr_3D array.
3 in arr_3d

# Let's check if the value 11 is in the arr_3D array.
11 not in arr_3d

# #### Unpacking an array

# Let's take a_val matrix with three rows and nine columns.
a_val = np.arange(1, 28).reshape(3, 9)
a_val

# +
# each line can be unpacked into a separate variable
x_val, y_val, z_val = a_val

# выведем первую переменную (строку)
x_val

# +
# Now let's unpack the first, last, and remaining elements
# of the first line into separate variables
x_val, *y_val, z_val = a_val[0]

# выведем каждую переменную
print(x_val)
print(y_val)
print(z_val)
# -

# #### Changing array elements

# Let's turn to a two-dimensional array.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d

# replace the first element of the first row by its index
arr_2d[0, 0] = 2
arr_2d

# write the value 1 in the first row
arr_2d[0] = 1
arr_2d

# Write 0 in the third column of the array.
arr_2d[:, 2] = 0
arr_2d

# let's turn to the three-dimensional array
arr_3d = np.arange(12).reshape(2, 2, 3)
arr_3d

# +
# select the second column of the second matrix and
# replace the values in columns 7 and 10 with 0 and 1
arr_3d[1, :, 1] = [0, 1]

# in such an operation, the cut size must match
# the number of values being transferred
arr_3d
# -

# replace all elements of the array with the number seven
arr_3d.fill(7)
arr_3d

# #### Sorting an array and reversing the order of its elements

# Function np.sort()

# lets take a two-dimensional array
a_arr = np.array([[4, 8, 2], [2, 3, 1]])
a_arr

# By default, sorting is performed with the parameter axis = -1
np.sort(a_arr)

# for a two-dimensional array, this is axis 1
np.sort(a_arr, axis=1)

# Let's look at sorting along the 0 axis.
np.sort(a_arr, axis=0)

# axis = None initially returns a
# one-dimensional array,
# and then sorts it
np.sort(a_arr, axis=None)

# Reversing the order of array elements using the slice operator

# slice operator with step parameter -1
# sets the reverse order of array elements
reversed_arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[::-1]
reversed_arr

# The reverse order can be combined with cuts.
reverse_slice = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[-3:3:-1]
reverse_slice

# in two-dimensional array
a_arr = np.array([[4, 8, 2], [2, 3, 1], [1, 7, 2]])
a_arr

# you can set the reverse order for
# two dimensions (axis = (0, 1))
a_arr[::-1, ::-1]

# reverse order by external (axis = 0)
a_arr[::-1]

# and internal dimension (axis = 1)
a_arr[:, ::-1]

# Reverse order using the np.flip() function

# by default, sets the reverse order for two dimensions
# same as axis = (0, 1)
np.flip(a_arr)

# you can also set the reverse order by external
np.flip(a_arr, axis=0)

# and internal measurements
np.flip(a_arr, axis=1)

# Sorting in descending order

# to sort an array in descending order
a_arr = np.array([4, 2, 6, 1, 7, 3, 5])

# we can sequentially apply np.sort() and the slice operator
sorted_desc = np.sort(a_arr)[::-1]
sorted_desc

# the original array has not changed
a_arr

# You can do it in reverse order, but using the .sort() method.
a_arr[::-1].sort()

# the change has become permanent
a_arr

# #### Change in dimension

# .reshape()

# lets take a three-dimensional array
arr_3d = np.arange(12).reshape(2, 2, 3)
arr_3d

# it has 12 elements
arr_3d.size

# change the dimension while keeping the total number
# of elements the same
arr_2d = arr_3d.reshape(2, 6)
arr_2d

# np.resize() and .resize()

# The np.resize() function allows you
# to not keep the previous number of elements.
# Existing elements are copied to new cells.
np.resize(arr_2d, (3, 6))

# +
# arr_2D refers to another array, so you first need to make a copy of it
arr_2d_copy = arr_2d.copy()

# The .resize() method will make a copy, change the dimensions,
# and fill in the gaps with zeros.
arr_2d_copy.resize(4, 6)
arr_2d_copy
# -

# .flatten() and .ravel()

# .flatten() converts ("flattens") an array into
# a one-dimensional array and
# creates a copy of the original array
# (like the .copy() method).
arr_3d.flatten()

# .ravel() does the same thing,
# but does not create a copy of the original
# array and is therefore faster than .flatten().
arr_3d.ravel()

# np.newaxis

# np.newaxis adds a dimension to the array
a_arr = np.array([1, 2, 3])
a_arr.shape

# +
# add the first dimension
b_arr = a_arr[np.newaxis, :]

print(b_arr)
print(b_arr.shape)

# +
# добавим второе измерение
c_arr = a_arr[:, np.newaxis]

print(c_arr)
print(c_arr.shape)
# -

# np.expand_dims()

# lets take a two-dimensional array
a_arr = np.array([[1, 2], [3, 4]])
a_arr

# add an external dimension
np.expand_dims(a_arr, axis=0)

# add a "middle" measurement
np.expand_dims(a_arr, axis=1)

# add internal dimension
np.expand_dims(a_arr, axis=2)

# np.squeeze()

# Let's take a 4D array in which
# the first and last dimensions contain one element each.
arr_4d = np.arange(9).reshape(1, 3, 3, 1)
arr_4d

# Remove these measurements using the np.squeeze() function.
np.squeeze(arr_4d)

# the new array has only two dimensions
squeezed_shape = np.squeeze(arr_4d).shape
squeezed_shape

# #### Merging arrays

# np.concatenate()

# Let's create two square arrays.
a_arr = np.arange(4).reshape(2, 2)
a_arr

b_arr = np.arange(4, 8).reshape(2, 2)
b_arr

# Merging arrays
np.concatenate((a_arr, b_arr), axis=0)

# the same along axis 1
np.concatenate((a_arr, b_arr), axis=1)

# np.stack()

# The difference here is that we are
# adding a new axis (dimension).
np.stack((a_arr, b_arr), axis=0)

np.stack((a_arr, b_arr), axis=1)

np.stack((a_arr, b_arr), axis=2)
