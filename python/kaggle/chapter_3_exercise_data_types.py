"""Data Types."""

# **This notebook is an exercise in the [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/data-types).**
#
# ---
#

# In the tutorial, you learned about four different data types: floats, integers, strings, and booleans.  In this exercise, you'll experiment with them.
#
# # Set up the notebook
#
# Run the next code cell without changes to set up the notebook.

# +
# Set up the exercise
# fmt: off
from learntools.core import binder
from learntools.intro_to_programming.ex3 import *  # pylint: disable=W0401

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # Question 1
#
# You have seen how to convert a float to an integer with the `int` function.  Try this out yourself by running the code cell below.

# +
# Define a float
y_val = 1.0
print(y_val)
print(type(y_val))

# Convert float to integer with the int function
z_val = int(y_val)
print(z_val)
print(type(z_val))
# -

# In this case, the float you are using has no numbers after the decimal.
# - But what happens when you try to convert a float with a fractional part to an integer?
# - How does the outcome of the `int` function change for positive and negative numbers?
#
# Use the next code cell to investigate and answer these questions.  Feel free to add or remove any lines of code -- it is your workspace!

# Uncomment and run this code to get started!
print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

# Once you have an answer, run the code cell below to see the solution.  Viewing the solution will give you credit for answering the problem.

# +
# Check your answer (Run this code cell to receive credit!)
# q1.check()
# -

# # Question 2
#
# In the tutorial, you learned about booleans (which can take a value of `True` or `False`), in addition to integers, floats, and strings.  For this question, your goal is to determine what happens when you multiply a boolean by any of these data types.  Specifically,
# - What happens when you multiply an integer or float by `True`?  What happens when you multiply them by `False`?  How does the answer change if the numbers are positive or negative?
# - What happens when you multiply a string by `True`?  By `False`?
#
# Use the next code cell for your investigation.

# Uncomment and run this code to get started!
print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))


# Once you have an answer, run the code cell below to see the solution.  Viewing the solution will give you credit for answering the problem.

# +
# Check your answer (Run this code cell to receive credit!)
# q2.check()
# -

# # Question 3
#
# In this question, you will build off your work from the previous exercise to write a function that estimates the value of a house.
#
# Use the next code cell to create a function `get_expected_cost` that takes as input three variables:
# - `beds` - number of bedrooms (data type float)
# - `baths` - number of bathrooms (data type float)
# - `has_basement` - whether or not the house has a basement (data type boolean)
#
# It should return the expected cost of a house with those characteristics. Assume that:
# - the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
# - each bedroom adds 30000 to the expected cost,
# - each bathroom adds 10000 to the expected cost, and
# - a basement adds 40000 to the expected cost.
#
# For instance,
# - a house with 1 bedroom, 1 bathroom, and no basement has an expected cost of 80000 + 30000 + 10000 = 120000.  This value will be calculated with `get_expected_cost(1, 1, False)`.
# - a house with 2 bedrooms, 1 bathroom, and a basement has an expected cost of 80000 + 2*30000 + 10000 + 40000 = 190000.  This value will be calculated with `get_expected_cost(2, 1, True)`.
#
# Remember you can always get a hint by uncommenting `q3.hint()` in the code cell following the next!


# +
def get_expected_cost(beds: int, baths: int, has_basement: bool) -> float:
    """Calculate house cost based on bedrooms, bathrooms and basement."""
    basement_cost = 40000 if has_basement else 0
    value = 80000 + beds * 30000 + baths * 10000 + basement_cost
    return value


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
# We'll continue our study of boolean arithmetic.  For this question, your task is to provide a description of what happens when you add booleans.
#
# Use the next code cell for your investigation.  Feel free to add or remove any lines of code - use it as your workspace!

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)


# Once you have an answer, run the code cell below to see the solution.  Viewing the solution will give you credit for answering the problem.

# +
# Check your answer (Run this code cell to receive credit!)
# q4.check()
# -

# # 🌶️ Question 5
#
# You own an online shop where you sell rings with custom engravings.  You offer both gold plated and solid gold rings.
# - Gold plated rings have a base cost of \\$50, and you charge \\$7 per engraved unit.
# - Solid gold rings have a base cost of \\$100, and you charge \\$10 per engraved unit.
# - Spaces and punctuation are counted as engraved units.
#
# Write a function `cost_of_project()` that takes two arguments:
# - `engraving` - a Python string with the text of the engraving
# - `solid_gold` - a Boolean that indicates whether the ring is solid gold
#
# It should return the cost of the project.  This question should be fairly challenging, and you may need a hint.


# +
def cost_of_project(engraving: str, solid_gold: bool) -> int:
    """Calculate ring cost based on engraving length and gold type."""
    base_cost = 100 if solid_gold else 50
    cost_per_unit = 10 if solid_gold else 7
    engraving_cost = len(engraving) * cost_per_unit
    return base_cost + engraving_cost


# Check your answer
# q5.check()

# +
# Uncomment to see a hint
# q5.hint()

# Uncomment to view the solution
# q5.solution()
# -

# Run the next code cell to calculate the cost of engraving `Charlie+Denver` on a solid gold ring.

project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

# Use the next code cell to calculate the cost of engraving `08/10/2000` on a gold plated ring.

project_two = cost_of_project("08/10/2000", False)
print(project_two)

# # Keep going
#
# Continue to the next lesson to **[learn about conditions and conditional statements](https://www.kaggle.com/alexisbcook/conditions-and-conditional-statements)**.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*
