"""Loops."""

# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/loops-and-list-comprehensions).**
#
# ---
#

# With all you've learned, you can start writing much more interesting programs. See if you can solve the problems below.
#
# As always, run the setup code below before working on the questions.

# +
# fmt: off
from learntools.core import binder
from learntools.intro_to_programming.ex5 import *  # pylint: disable=W0401

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # 1.
#
# Have you ever felt debugging involved a bit of luck? The following program has a bug. Try to identify the bug and fix it.


def has_lucky_number(nums: list[int]) -> bool:
    """Return whether the given list of numbers is lucky."""
    for num in nums:
        return num % 7 == 0
    return False


# Try to identify the bug and fix it in the cell below:

# +
# q1.hint()
# q1.solution()
# -

# # 2.
# Look at the Python expression below. What do you think we'll get when we run it? When you've made your prediction, uncomment the code and run the cell to see if you were right.

# +
# [1, 2, 3, 4] > 2
# -

# R and Python have some libraries (like numpy and pandas) compare each element of the list to 2 (i.e. do an 'element-wise' comparison) and give us a list of booleans like `[False, False, True, True]`.
#
# Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.


# +
def elementwise_greater_than(list_val: list[int], thresh: int) -> list[bool]:
    """Return a list with comparison results."""
    return [val > thresh for val in list_val]


# Check your answer
# q2.check()

# +
# q2.solution()
# -

# # 3.
#
# Complete the body of the function below according to its docstring.


# +
def is_menu_boring(meals: list[str]) -> bool:
    """Return True if meal is been served 2 times in a row."""
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False


# Check your answer
# q3.check()

# +
# q3.hint()
# q3.solution()
# -

# # 4. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
#
# Next to the Blackjack table, the Python Challenge Casino has a slot machine. You can get a result from the slot machine by calling `play_slot_machine()`. The number it returns is your winnings in dollars. Usually it returns 0.  But sometimes you'll get lucky and get a big payday. Try running it below:

# +
# play_slot_machine()
# -

# By the way, did we mention that each play costs $1? Don't worry, we'll send you the bill later.
#
# On average, how much money can you expect to gain (or lose) every time you play the machine?  The casino keeps it a secret, but you can estimate the average value of each pull using a technique called the **Monte Carlo method**. To estimate the average outcome, we simulate the scenario many times, and return the average result.
#
# Complete the following function to calculate the average value per play of the slot machine.

# +
# def estimate_average_slot_payout(n_runs: int) -> float:
#     # Play slot machine n_runs times, calculate payout of each
#     payouts = [play_slot_machine() - 1 for i in range(n_runs)]
#     # Calculate the average value
#     avg_payout = sum(payouts) / n_runs
#     return avg_payout
# -

# When you think you know the expected value per spin, run the code cell below to view the solution and get credit for answering the question.

# +
# Check your answer (Run this code cell to receive credit!)
# q4.solution()
# -

# # Keep Going
#
# Many programmers report that dictionaries are their favorite data structure. You'll get to **[learn about them](https://www.kaggle.com/colinmorris/strings-and-dictionaries)** (as well as strings) in the next lesson.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
