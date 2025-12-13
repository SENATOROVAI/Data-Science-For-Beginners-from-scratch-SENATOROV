"""Chapter 6 functions."""

# ## Functions in Python

# ### Built-in functions

# +
from collections.abc import ItemsView
from typing import Callable

# import libraries for data visualization
import matplotlib.pyplot as plt

# Before calling the function, you must remember to import
# the appropriate library
import numpy as np

# set the reference point for random number generation
np.random.seed(42)
# and generate the growth data for 1000 people
height = list(np.round(np.random.normal(180, 10, 1000)))
# -

# #### Function parameters and arguments

# A parameter is what a function requests when called (for example, bins, the number of intervals).
# An argument is the value of this parameter (in our case, 10).

# now build a histogram by passing it two parameters,
# growth data and the number of intervals
# the first parameter is positional, the second is named.
plt.hist(height, bins=10)
plt.show()

# the first parameter can also be named (the data is denoted by x)
# and then the order of the parameters can be changed
plt.hist(bins=10, x=height)
plt.show()

# the bins parameter has a default argument (exactly 10 intervals),
# which means that this parameter can be omitted
plt.hist(height)
plt.show()

# It is worth noting that a function can accept one, two, or several parameters, or accept none at all. For example, if no parameters are specified, the  `print()` function returns an empty string.

# the function may not request parameters
print("First line")
print()
print("Third line")

# #### Functions and methods

# Some functions are called methods. Methods are functions that can only be applied to a specific object.

# +
some_string = "machine learning"

# apply the .title() method to the string
some_string.title()


# -

# ### User-defined functions

# #### Defining and calling a function


# lets define our own function double
def double(x_arg: int) -> int:
    """Multiple transferred number by 2."""
    res = x_arg * 2
    return res


# and call it by passing the number 2
double(2)

# #### Empty function body

# +
# function body cannot be empty


def only_return() -> None:
    """Return the input value."""
    # you must either specify the return keyword
    return


# -

only_return()


# #### Function print() instead of return


def double_print(x_arg: int) -> None:
    """Multiple passed number by 2 and output result."""
    res = x_arg * 2
    print(res)


double_print(5)

# #### Parameters of user-defined functions

# +
# define  a function with parameters x and y


def calc_sum(x_arg: int, y_arg: int) -> int:
    """Add two numbers."""
    # and return their sum
    return x_arg + y_arg


# -

# call this function with one positional and one named parameter
calc_sum(1, y_arg=2)

# +
# function parameters can be given default arguments


def calc_sum_default(x_arg: int = 1, y_arg: int = 2) -> int:
    """Add two integers."""
    return x_arg + y_arg


# and then you don't have to specify them on the call
calc_sum_default()

# +
# function may have no parameters


def print_string() -> None:
    """Output the 'Some string' string."""
    print("Some string")


print_string()
# -

# #### Function annotation
#
# Function annotation allows you to explicitly specify the data type of parameters (parameter annotation) and return values (return annotation).

# +
# let's specify that the function takes float type as input and returns int
# the value 3.5 is the default value of the x parameter


def f(x_arg: float = 3.5) -> int:
    """Convert the passed float-argument to integer type."""
    return int(x_arg)


# -

# the desired data type can be viewed via the __annotations__ attribute
f.__annotations__

# call the function without parameters
f()

# #### Additional features

# function calls can be combined with arithmetic operations
result = calc_sum(1, 2) * 2
result

# and logical operations
result = calc_sum(1, 2) > 2
result


# +
def first_letter() -> str:
    """Return the string 'Python'."""
    return "Python"


print(first_letter()[0])

# +
# function may take no parameters, but use input()


def use_input() -> int:
    """Square the entered number."""
    # request a number from the user and convert it to the int data type
    user_inpt = int(input("Введите число: "))

    # square the number
    result_pow = user_inpt**2

    # return the result
    return result_pow


# call the function
use_input()
# -

# #### Function call result

# +
# The function can also return a list, tuple, dictionary, etc..


# define a function that receives a number as input,
def create_list(x_arg: int) -> list[int]:
    """Create a list filled with numbers from 0 to x_arg."""
    # empty list
    my_list: list[int] = []

    # in the for loop create a sequence
    for index in range(x_arg):

        # and put it on the list
        my_list.append(index)

    return my_list


# the result of calling this function will be a list of
create_list(5)

# +
# function can return two values at once


def tuple_f() -> tuple[str, int]:
    """Return a tuple ('python', 42)."""
    string = "Python"
    x_arg = 42
    return string, x_arg


# call the function
tuple_f()

# +
# if you use two variables to receive the result of the function,
# then the returned tuple will be unpacked into these variables
a_var, b_var = tuple_f()

# the output is a string and a integer
print(a_var, b_var)
print(type(a_var), type(b_var))

# +
# if one variable is used to receive the result,
# then the result will be a tuple
c_var = tuple_f()

print(c_var)
print(type(c_var))

# +
# the output can be a logical value (True or False)


def is_divisible(x_arg: int) -> bool:
    """Check if the number is even."""
    # if the remainder of division by two is zero
    if x_arg % 2 == 0:
        return True

    # otherwise False
    return False


is_divisible(10)
# -

# #### Using libraries
#
# Additional Python libraries can be used within functions. For example, we can apply the `mean()` function from the Numpy library to calculate the arithmetic mean.

# +
# apply the mean() function of the Numpy library
# to calculate the arithmetic average


# as input our function will take a list or array x,
def mean_f(x_arg: list[int]) -> float:
    """Calculate the average and adds 1 to the result."""
    return float(np.mean(x_arg) + 1)


# +
# prepare data
x_var: list[int] = [1, 2, 3]

mean_f(x_var)
# -

# #### Global and local variables
#
# Some variables exist (or, as they say, are visible) only within a function, while others exist throughout the entire program. In the first case, we talk about local variables, and in the second, global variables.

# +
# create a global variable outside the function
global_name = "Peter"

# and then use it inside a new function


def show_name() -> None:
    """Return the global variable global_name to the console."""
    print(global_name)


# -

show_name()

# +
# and now let's first create a function,
# within which we declare a local variable


def show_local_name() -> None:
    """Return 'Alena' to the console."""
    local_name_1 = "Alena"
    print(local_name_1)


# -

show_local_name()

# The function was called without any problems. However, if we try to access the local_name variable outside this function, Python will return an error.

# +
# it is possible to return a local variable to a global variable
# via the global keyword
local_name = "Tatyana"


def make_global() -> None:
    """Create a global variable local_name and outputs it to the console."""
    global local_name  # pylint: disable=W0603
    local_name = "Alena"
    print(local_name)


# -

make_global()

# +
# define a global variable
global_number = 5


def print_number() -> None:
    """Return the value of the local variable local_number to the console."""
    # then define a local variable
    local_number = 10
    print("Local number:", local_number)
    print("Global number:", global_number)


# -

# the function will always "prefer" a local variable"
print_number()

# the value of the global variable will not change for the rest of the code
print("Global number:", global_number)

# ### Lambda-functions
#
# Convenient to use in cases where the use of the normal function is excessive.

# +
# create a function that takes two numbers and multiplies them
lf: Callable[[int, int], int] = lambda a_arg, b_arg: a_arg * b_arg

# call the function and pass numbers 2 and 3 to it
lf(2, 3)

# +
# the same functionality can be placed in an ordinary function


def normal_f(a_arg: int, b_arg: int) -> int:
    """Return the product of the passed arguments."""
    return a_arg * b_arg


normal_f(2, 3)
# -

# #### Lambda function inside the filter() function
#
#
# The `filter()` function takes two parameters:
#
# First, another function that acts as a criterion; it returns `True` if the element should be kept, and `False` if it should be removed.
# Second, a set of elements to be filtered in the form of a `list`, `tuple`, or `set`.

# +
nums_list: list[int] = [15, 27, 9, 18, 3, 1, 4]

# write a lambda function that will print True,
# if the number is greater than 10, and False if it is less than 10.
is_more_then_10: Callable[[int], bool] = lambda n_arg: n_arg > 10

# put the list and lambda-function into the filter() function
# and convert the result to a list
list(filter(is_more_then_10, nums_list))
# -

# you can write it all down in one line
list(filter(lambda n_arg: n_arg > 10, nums_list))

# And that's the beauty of lambda functions: you don't need to declare them in advance. Using a regular function, the code would look like this.

# +
# the same problem can be solved using a normal function,
# but you have to write more code


def is_more_then_10_2(n_arg: int) -> bool:
    """Check if the passed number is greater than 10."""
    if n_arg > 10:
        return True

    return False


list(filter(is_more_then_10_2, nums_list))
# -

# #### Lambda function inside the sorted() function

# +
# Remind me that we've created a list of tuples,
# and each tuple had a movie index and a distance to the movie #
indices_distances = [
    (901, 0.0),
    (1002, 0.22982440568634488),
    (442, 0.25401128310081567),
]

# lambda function will take each tuple and return the second [1] element of it
# passing this function with a key parameter will sort the list by distance
sorted(indices_distances, key=lambda x_arg: x_arg[1], reverse=False)
# -

# #### Immediately callable functions
#
#
# Lambda functions are what we call immediately invoked function expressions (IIFE). This means we can declare and call such a function at the same time.

# lambda function can be called immediately at the time of declaration
(lambda x_arg: x_arg * x_arg)(10)  # pylint: disable=C3002

# ### \*args and \**kwargs

# #### \*args
#
# Suppose we have a simple function that takes two numbers and calculates their arithmetic mean.

# +
# write a function to calculate the arithmetic mean of two numbers


def mean_simple(a_arg: int, b_arg: int) -> float:
    """Calculate the arithmetic mean."""
    return (a_arg + b_arg) / 2


# -

mean_simple(1, 2)

# Everything works fine, but we cannot pass more than two numbers to this function. A possible solution would be a function that initially accepts a list as an argument.

# +
# declare a function to which we want to pass the list


def mean_1(list_arg: list[int]) -> float:
    """Calculate the arithmetic mean of the passed array of numbers."""
    # set a variable for the sum,
    total = 0

    # in the loop add all numbers from the list
    for num in list_arg:
        total += num

    # and divide by the number of elements
    return total / len(list_arg)


# +
# create a list of numbers
list_: list[int] = [1, 2, 3, 4]

# and pass it to a new function
mean_1(list_)
# -

# *args allows you to pass an arbitrary number of individual numbers to a function.

# +
# declare a function with *args


def mean_2(*nums: int) -> float:
    """Calculate the arithmetic mean of the passed array of numbers."""
    # in this case we add up the elements of the tuple
    total = 0
    for num in nums:
        total += num

    return total / len(nums)


# -

# now we can pass individual numbers to the function
mean_2(1, 2, 3, 4)

# or list
mean_2(*list_)

# +
# we make sure that the unpack operator * forms a tuple


def test_type(*nums: int) -> None:
    """Check the type of argument *nums."""
    print(nums, type(nums))


test_type(1, 2, 3, 4)
# -

# the same thing happens with the list
test_type(*list_)

# +
# for illustrative purposes, here is another example
a_list: list[int] = [1, 2, 3]
b_list: list[int] = [*a_list, 4, 5, 6]

print(b_list)
# -

# #### \**kwargs

# +
# **kwargs converts named parameters into a dictionary


def fn(**kwargs: int) -> ItemsView[str, int]:
    """Return a list of key/value pairs of named parameters."""
    return kwargs.items()


# -

fn(a=1, b=2)

# +
# *nums becomes a tuple, **params becomes a dictionary


def simple_stats(*nums: int, **params: bool) -> None:
    """Calculate the arithmetic mean and RMS."""
    # if the 'mean' key is in the params dictionary and its value == True
    if "mean" in params and params["mean"] is True:

        # calculate the arithmetic mean and round up
        # \t is a tab character
        print(f"mean: \t{np.round(np.mean(nums), 3)}")

    # if the 'std' key is in the params dictionary and its value == True
    if "std" in params and params["std"] is True:

        # calculate the RMS and round up
        print(f"std: \t{np.round(np.std(nums), 3)}")


# -

# call the simple_stats() function and pass it numbers and named arguments
simple_stats(5, 10, 15, 20, mean=True, std=True)

# if one of the parameters is set to False,
# the function will not output the corresponding metric
simple_stats(5, 10, 15, 20, mean=True, std=False)

# +
# if we want to pass parameters by list and dictionary,
list_nums: list[int] = [5, 10, 15, 20]
settings: dict[str, bool] = {"mean": True, "std": True}

# then we need to use the unpacking operators * and ** respectively
simple_stats(*list_nums, **settings)
# -

# there's nothing stopping us from adding another parameter
simple_stats(5, 10, 15, 20, mean=True, std=True, median=True)

# In conclusion, I would like to note that all of the above examples are educational, and it is certainly possible to do without *args and **kwargs here. In practice, they are used in more complex constructions, such as so-called decorators, but this topic is beyond the scope of today's lesson.
