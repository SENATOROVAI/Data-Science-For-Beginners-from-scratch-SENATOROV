"""Lists."""

# **This notebook is an exercise in the [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/intro-to-lists).**
#
# ---
#

# In the tutorial, you learned how to define and modify Python lists.  In this exercise, you will use your new knowledge to solve several problems.
#
# # Set up the notebook
#
# Run the next code cell without changes to set up the notebook.

# +
# fmt: off
from learntools.core import binder
from learntools.intro_to_programming.ex5 import *  # pylint: disable=W0401

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # Question 1
#
# You own a restaurant with five food dishes, organized in the Python list `menu` below.  One day, you decide to:
# - remove bean soup (`'bean soup'`) from the menu, and
# - add roasted beet salad (`'roasted beet salad'`) to the menu.
#
# Implement this change to the list below.  While completing this task,
# - do not change the line that creates the `menu` list.
# - your answer should use `.remove()` and `.append()`.

# +
# Do not change: Initial menu for your restaurant
menu = [
    "stewed meat with onions",
    "bean soup",
    "risotto with trout and shrimp",
    "fish soup with cream and onion",
    "gyro",
]

# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu # pylint: disable=W0511
menu.remove("bean soup")
menu.append("roasted beet salad")

# Do not change: Check your answer
# q1.check()

# +
# Uncomment to see a hint
# q1.hint()

# Uncomment to see the solution
# q1.solution()
# -

# # Question 2
#
# The list `num_customers` contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days).  Fill in values for each of the following:
# - `avg_first_seven` - average number of customers who visited in the first seven days
# - `avg_last_seven` - average number of customers who visited in the last seven days
# - `max_month` - number of customers on the day that got the most customers in the last month
# - `min_month` - number of customers on the day that got the least customers in the last month
#
# Answer this question by writing code.  For instance, if you have to find the minimum value in a list, use `min()` instead of scanning for the smallest value and directly filling in a number.

# +
# Do not change: Number of customers each day for the last month
num_customers = [
    137,
    147,
    135,
    128,
    170,
    174,
    165,
    146,
    126,
    159,
    141,
    148,
    132,
    147,
    168,
    153,
    170,
    161,
    148,
    152,
    141,
    151,
    131,
    149,
    164,
    163,
    143,
    143,
    166,
    171,
]

# TODO: Fill in values for the variables below # pylint: disable=W0511

avg_first_seven = sum(num_customers[0:7]) / 7
avg_last_seven = sum(num_customers[len(num_customers) - 7 :]) / 7
max_month = max(num_customers)
min_month = min(num_customers)

# Do not change: Check your answer
# q2.check()

# +
# Uncomment to see a hint
# q2.hint()

# Uncomment to see the solution
# q2.solution()
# -

# # Question 3
#
# In the tutorial, we gave an example of a Python string with information that was better as a list.

flowers = """pink primrose,hard-leaved pocket orchid,canterbury 
bells,sweet pea,english marigold,tiger lily,moon orchid,bird 
of paradise,monkshood,globe thistle"""

# You can actually use Python to quickly turn this string into a list with `.split()`.  In the parentheses, we need to provide the character should be used to mark the end of one list item and the beginning of another, and enclose it in quotation marks.  In this case, that character is a comma.

print(flowers.split(","))

# Now it is your turn to try this out!  Create two Python lists:
# - `letters` should be a Python list where each entry is an uppercase letter of the English alphabet.  For instance, the first two entries should be `"A"` and `"B"`, and the final two entries should be `"Y"` and `"Z"`.  Use the string `alphabet` to create this list.
# - `address` should be a Python list where each row in `address` is a different item in the list.  Currently, each row in `address` is separated by a comma.

# +
# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = """Mr. H. Potter,The cupboard under 
the Stairs,4 Privet Drive,Little Whinging,Surrey"""

# TODO: Convert strings into Python lists # pylint: disable=W0511
letters = alphabet.split(".")
formatted_address = address.split(",")

# Do not change: Check your answer
# q3.check()

# +
# Uncomment to see a hint
# q3.hint()

# Uncomment to see the solution
# q3.solution()
# -

# # Question 4
#
# In the Python course, you'll learn all about **list comprehensions**, which allow you to create a list based on the values in another list.  In this question, you'll get a brief preview of how they work.
#
# Say we're working with the list below.

test_ratings = [1, 2, 3, 4, 5]

# Then we can use this list (`test_ratings`) to create a new list (`test_liked`) where each item has been turned into a boolean, depending on whether or not the item is greater than or equal to four.

test_liked = [i >= 4 for i in test_ratings]
print(test_liked)


# In this question, you'll use this list comprehension to define a function `percentage_liked()` that takes one argument as input:
# - `ratings`: list of ratings that people gave to a movie, where each rating is a number between 1-5, inclusive
#
# We say someone liked the movie, if they gave a rating of either 4 or 5.  Your function should return the percentage of people who liked the movie.
#
# For instance, if we supply a value of `[1, 2, 3, 4, 5, 4, 5, 1]`, then 50% (4/8) of the people liked the movie, and the function should return `0.5`.
#
# Part of the function has already been completed for you.  You need only use `list_liked` to calculate `percentage_liked`.


# +
def percentage_liked(ratings: list[int]) -> float:
    """Calculate percentage of ratings that are 4 or higher."""
    list_liked = [i >= 4 for i in ratings if i >= 4]
    # TODO: Complete the function
    result = len(list_liked) / len(ratings)
    return result


# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

# Do not change: Check your answer
# q4.check()

# +
# Uncomment to see a hint
# q4.hint()

# Uncomment to see the solution
# q4.solution()
# -

# # 🌶️ Question 5
#
# Say you're doing analytics for a website.  You need to write a function that returns the percentage growth in the total number of users relative to a specified number of years ago.
#
# Your function `percentage_growth()` should take two arguments as input:
# - `num_users` = Python list with the total number of users each year.  So `num_users[0]` is the total number of users in the first year, `num_users[1]` is the total number of users in the second year, and so on.  The final entry in the list gives the total number of users in the most recently completed year.
# - `yrs_ago` = number of years to go back in time when calculating the growth percentage
#
# For instance, say `num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]`.
# - if `yrs_ago = 1`, we want the function to return a value of about `0.036`. This corresponds to a percentage growth of approximately 3.6%, calculated as (2001078 - 1930992)/1930992.
# - if `years_ago = 7`, we would want to return approximately `0.66`.  This corresponds to a percentage growth of approximately 66%, calculated as (2001078 - 1204334)/1204334.
#
# Your coworker sent you a draft of a function, but it doesn't seem to be doing the correct calculation.  Can you figure out what has gone wrong and make the needed changes?

# +
# TODO: Edit the function # pylint: disable=W0511


def percentage_growth(num_users: list[int], yrs_ago: int) -> float:
    """Calculate percentage growth in users compared to specified years ago."""
    recent = num_users[-1]
    past = num_users[-1 - yrs_ago]
    growth = (recent - past) / past
    return growth


# Do not change: Variable for calculating some test examples
num_users_test = [
    920344,
    1043553,
    1204334,
    1458996,
    1503323,
    1593432,
    1623463,
    1843064,
    1930992,
    2001078,
]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))

# Do not change: Check your answer
# q5.check()

# +
# Uncomment to see a hint
# q5.hint()

# Uncomment to see the solution
# q5.solution()
# -

# # Congratulations!
#
# Congratulations for finishing the Intro to Programming course!  You should be proud of your very first steps with learning programming.  As next steps, we recommend taking:
# - the **[Python course](http://www.kaggle.com/learn/python)**, and
# - the **[Intro to Machine Learning course](https://www.kaggle.com/learn/intro-to-machine-learning)**.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*
