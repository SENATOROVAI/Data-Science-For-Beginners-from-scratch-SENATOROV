"""Functions."""

# **This notebook is an exercise in the [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/functions).**
#
# ---
#

# In the tutorial, you learned about functions. In this exercise, you'll write some of your own!
#
# # Set up the notebook
#
# Run the next code cell without changes to set up the notebook.

# +
# Set up the exercise
# fmt: off
import math

from learntools.core import binder
from learntools.intro_to_programming.ex2 import *  # pylint: disable=W0401

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # Question 1
#
# In the [House Prices - Advanced Regression Techniques competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview), you need to use information like the number of bedrooms and bathrooms to predict the price of a house.  Inspired by this competition, you'll write your own function to do this.
#
# In the next code cell, create a function `get_expected_cost()` that has two arguments:
# - `beds` - number of bedrooms
# - `baths` - number of bathrooms
#
# It should return the expected cost of a house with that number of bedrooms and bathrooms.  Assume that:
# - the expected cost for a house with 0 bedrooms and 0 bathrooms is `80000`.
# - each bedroom adds `30000` to the expected cost
# - each bathroom adds `10000` to the expected cost.
#
# For instance,
# - a house with 1 bedroom and 1 bathroom has an expected cost of `120000`, and
# - a house with 2 bedrooms and 1 bathroom has an expected cost of `150000`.

# +
# TODO: Complete the function # pylint: disable=W0511


def get_expected_cost(beds: int, baths: int) -> int:
    """Calculate expected house cost based on number of beds and baths."""
    value = 80000 + beds * 30000 + baths * 10000
    return value


# Check your answer
# q1.check()

# +
# Uncomment to see a hint
# q1.hint()

# Uncomment to view the solution
# q1.solution()
# -

# # Question 2
#
# You are thinking about buying a home and want to get an idea of how much you will spend, based on the number of bedrooms and bathrooms.  You are trying to decide between four different options:
# - Option 1: house with two bedrooms and three bathrooms
# - Option 2: house with three bedrooms and two bathrooms
# - Option 3: house with three bedrooms and three bathrooms
# - Option 4: house with three bedrooms and four bathrooms
#
# Use the `get_expected_cost()` function you defined in question 1 to set `option_1`, `option_2`, `option_3`, and `option_4` to the expected cost of each option.

# +
# TODO: Use the get_expected_cost function to fill in each value # pylint: disable=W0511
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Check your answer
# q2.check()

# +
# Uncomment to see a hint
# q2.hint()

# Uncomment to view the solution
# q2.solution()
# -

# # Question 3
#
# You're a home decorator, and you'd like to use Python to streamline some of your work.  Specifically, you're creating a tool that you intend to use to calculate the cost of painting a room.
#
# As a first step, define a function `get_cost()` that takes as input:
# - `sqft_walls` = total square feet of walls to be painted
# - `sqft_ceiling` = square feet of ceiling to be painted
# - `sqft_per_gallon` = number of square feet that you can cover with one gallon of paint
# - `cost_per_gallon` = cost (in dollars) of one gallon of paint
#
# It should return the cost (in dollars) of putting one coat of paint on all walls and the ceiling.  Assume you can buy the exact amount of paint that you need, so you can buy partial gallons (e.g., if you need 7.523 gallons, you can buy that exact amount, instead of needing to buy 8 gallons and waste some paint).  Do not round your answer.

# +
# TODO: Finish defining the function # pylint: disable=W0511


# fmt: off
def get_cost(
    sqft_walls: int,
    sqft_ceiling: int,
    sqft_per_gallon: int,
    cost_per_gallon: int
) -> float:
    """Calculate total cost of paint needed for walls and ceiling."""
    return ((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
# fmt: on

# Check your answer
# q3.check()


# +
# Uncomment to see a hint
# q3.hint()

# Uncomment to view the solution
# q3.solution()
# -

# # Question 4
#
# Use the `get_cost()` function you defined in Question 3 to calculate the cost of applying one coat of paint to a room with:
# - 432 square feet of walls, and
# - 144 square feet of ceiling.
#
# Assume that one gallon of paint covers 400 square feet and costs $15.  As in Question 3, assume you can buy partial gallons of paint.  Do not round your answer.

# +
# TODO: Set the project_cost variable to the cost of the project # pylint: disable=W0511
project_cost = get_cost(432, 144, 400, 15)

# Check your answer
# q4.check()

# +
# Uncomment to see a hint
# q4.hint()

# Uncomment to view the solution
# q4.solution()
# -


# # 🌶️ Question 5
#
# Now say you can no longer buy fractions of a gallon.  (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)
#
# With this new scenario, you will create a new function `get_actual_cost` that uses the same inputs and calculates the cost of your project.
#
# One function that you'll need to use to do this is `math.ceil()`.  We demonstrate usage of this function in the code cell below.  It takes as a number as input and rounds the number up to the nearest integer.
#
# Run the next code cell to test this function for yourself.  Feel free to change the value of `test_value` and make sure `math.ceil()` returns the number you expect.

# +
test_value = 2.17

rounded_value = math.ceil(test_value)
print(rounded_value)


# -

# Use the next code cell to define the function `get_actual_cost()`.  You'll need to use the `math.ceil()` function to do this.
#
# When answering this question, note that it's completely valid to define a function that makes use of another function.  For instance, we can define a function `round_up_and_divide_by_three` that makes use of the `math.ceil` function:
# ```
# def round_up_and_divide_by_three(num):
#     new_value = math.ceil(num)
#     final_value = new_value / 3
#     return final_value
# ```

# +
# fmt: off
def get_actual_cost(
    sqft_walls: int,
    sqft_ceiling: int,
    sqft_per_gallon: int,
    cost_per_gallon: int
) -> int:
    """Calculate total paint cost, rounding up gallons to nearest number."""
    sqft_total = sqft_walls + sqft_ceiling
    cost = math.ceil(sqft_total / sqft_per_gallon) * cost_per_gallon
    return cost
# fmt: on

# Check your answer
# q5.check()


# +
# Uncomment to see a hint
# q5.hint()

# Uncomment to view the solution
# q5.solution()
# -

# Once your function is verified as correct, run the next code cell to calculate the updated cost of your project.

get_actual_cost(432, 144, 400, 15)

# Say you're working with a slightly larger room.  Run the next code cell to calculate the cost of the project.

get_actual_cost(594, 288, 400, 15)

# # Keep going
#
# Continue to learn about **[data types](https://www.kaggle.com/alexisbcook/data-types)**.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*
