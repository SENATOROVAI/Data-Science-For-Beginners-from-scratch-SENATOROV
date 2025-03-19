"""Arithmetic and variables."""

# **This notebook is an exercise in the [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/arithmetic-and-variables).**
#
# ---

# This exercise will get you started with running your own code.
#
# # Set up the notebook
#
# To begin, run the code in the next cell.
# - Begin by clicking inside the code cell.
# - Click on the triangle (in the shape of a "Play button") that appears to the left of the code cell.
# - If your code was run sucсessfully, you will see `Setup Complete` as output below the cell.
#
# Instead of clicking on the triangle, you can also run code by pressing Shift + Enter on your keyboard.  Try this now!  Nothing bad will happen if you run the code more than once.

# +
# Load the data from the titanic competition
# fmt: off
import pandas as pd
# Set up the exercise
from learntools.core import binder
from learntools.intro_to_programming.ex1 import *  # pylint: disable=W0401

# fmt: on

binder.bind(globals())

print("Setup complete.")
# -

# The code above sets up the notebook so that it can check your answers in this exercise.  You should never modify this code.  (Otherwise, the notebook won't be able to verify that you have successfully completed the exercise.)
#
# After finishing all of the questions below, you'll see the exercise marked as complete on the [course page](http://www.kaggle.com/learn/intro-to-programming).  Once you complete all of the lessons, you'll get a course completion certificate!
#
# # Question 1
#
# Next, you will run some code from the tutorial, so you can see how it works for yourself.  Run the next code cell without changes.

# +
print("Hello, world!")

# DO NOT REMOVE: Mark this question as completed
# q1.check()
# -

# You just ran code to print `Hello world!`, which you should see in the output above.
#
# The second line of code (`q1.check()`) checks your answer.  You should never modify this checking code; if you remove it, you won't get credit for completing the problem.
#
# # Question 2
#
# Now, you will print another message of your choosing.  To do this, change `print("Your message here!")` to use a different message.  For instance, you might like to change it to something like:
# - `print("Good morning!")`
# - `print("I am learning how to code :D")`
#
# Or, you might like to see what happens if you write something like `print("3+4")`.  Does it return 7, or does it just think of `"3+4"` as just another message?
#
# Make sure that your message is enclosed in quotation marks (`"`), and the message itself does not use quotation marks. For instance, this will throw an error: `print("She said "great job" and gave me a high-five!")` because the message contains quotation marks.  If you decide to take the Python course after completing this course, you will learn more about how to avoid this error in [Lesson 6](https://www.kaggle.com/colinmorris/strings-and-dictionaries).
#
# Feel free to try out multiple messages!

# +
# TODO: Change the message # pylint: disable=W0511
print("Good morning!")

# DO NOT REMOVE: Mark this question as completed
# q2.check()
# -

# # Question 3
#
# As you learned in the tutorial, a comment in Python has a pound sign (`#`) in front of it, which tells Python to ignore the text after it.
#
# Putting a pound sign in front of a line of code will make Python ignore that code.  For instance, this line would be ignored by Python, and nothing would appear in the output:
# ```python
# # print(1+2)
# ```
# Removing the pound sign will make it so that you can run the code again. When we remove the pound sign in front of a line of code, we call this **uncommenting**.
#
# In this problem, you will uncomment two lines in the code cell below and view the output:
# - Remove the `#` in front of `q3.hint()`.  To avoid errors, do NOT remove the `#` in front of `# Uncomment to view hint`.
# - Next, remove the `#` in front of `q3.solution()`.
#
# As in the previous questions, do not change the final line of code that marks your work as completed.

# +
# Uncomment to get a hint
# q3.hint()

# Uncomment to view solution
# q3.solution()

# DO NOT REMOVE: Check your answer
# q3.check()
# -

# In the next question, and in most of the exercises in this course, you will have the option to uncomment to view hints and solutions.  Once you feel comfortable with uncommenting, continue to the next question.

# # Question 4
#
# In the tutorial, you defined several variables to calculate the total number of seconds in a year.  Run the next code cell to do the calculation here.

# +
# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
secs_per_year = secs_per_min * mins_per_hour * hours_per_day * days_per_year
total_secs = secs_per_year * num_years

print(total_secs)
# -

# Use the next code cell to:
# - Define a variable `births_per_min` and set it to 250.  (There are on average 250 babies born each minute.)
# - Define a variable `births_per_day` that contains the average number of babies born each day.  (To set the value of this variable, you should use `births_per_min` and some of the variables from the previous code cell.)
#
# Remember you can always get a hint if you need it!

# +
# TODO: Set the value of the births_per_min variable # pylint: disable=W0511
births_per_min = 250

# TODO: Set the value of the births_per_day variable # pylint: disable=W0511
births_per_day = births_per_min * hours_per_day * mins_per_hour

# DO NOT REMOVE: Check your answer
# q4.check()

# +
# Uncomment to get a hint
# q4.hint()

# Uncomment to view solution
# q4.solution()
# -

# # 🌶️ Question 5
#
# (Questions marked with a 🌶️ will be a little bit more challenging than the others!  Remember you can always get a hint or view the solution.)
#
# The [Titanic competition](https://www.kaggle.com/c/titanic) is Kaggle's most famous data science competition. In this competition, participants are challenged to build a machine learning model that can predict whether or not passengers survived the Titanic shipwreck, based on information like age, sex, family size, and ticket number.
#
# Run the next code cell without changes to load and preview the titanic data.
#
# Don't worry about the details of the code for now - the end result is just that the all of the titanic data has been loaded in a variable named `titanic_data`.  (In order to learn how to write this code yourself, you can take the [Python course](https://www.kaggle.com/learn/python) and then the [Pandas course](https://www.kaggle.com/learn/pandas).)

# +
titanic_data = pd.read_csv("../input/titanic/train.csv")

# Show the first five rows of the data
titanic_data.head()
# -

# The data has a different row for each passenger.
#
# The next code cell defines and prints the values of three variables:
# - `total` = total number of passengers who boarded the ship
# - `survived` = number of passengers who survived the shipwreck
# - `minors` = number of passengers under 18 years of age
#
# Run the code cell without changes.  (Don't worry about the details of how these variables are calculated for now.  You can learn more about how to calculate these values in the [Pandas course](https://www.kaggle.com/learn/pandas).)

# +
# Number of total passengers
total = len(titanic_data)
print(total)

# Number of passengers who survived
survived = (titanic_data.Survived == 1).sum()
print(survived)

# Number of passengers under 18
minors = (titanic_data.Age < 18).sum()
print(minors)
# -

# So,
# - `total = 891` (there were 891 passengers on board the Titanic),
# - `survived = 342` (342 passengers survived), and
# - `minors = 113` (113 passengers were under the age of 18).
#
# In the code cell below, replace the underlines (`____`) with code to calculate the values for two more variables:
# - `survived_fraction` should be set to the fraction of passengers who survived the Titanic disaster.
# - `minors_fraction` should be the fraction of passengers who were minors (under the age of 18).
#
# For each variable, your answer should be a number between 0 and 1.
#
# If you need a hint or want to view the solution, you can skip to the next code cell and uncomment the appropriate lines of code (`q5.hint()` and `q5.solution()`).

# +
# TODO: Fill in the value of the survived_fraction variable # pylint: disable=W0511
survived_fraction = 342 / 891

# Print the value of the variable
print(survived_fraction)

# TODO: Fill in the value of the minors_fraction variable # pylint: disable=W0511
minors_fraction = 113 / 891

# Print the value of the variable
print(minors_fraction)

# DO NOT REMOVE: Check your answer
# q5.check()

# +
# Uncomment to receive a hint
# q5.hint()

# Uncomment to view the solution
# q5.solution()
# -

# # Bonus Exercise
#
# As an **optional** next step, you're encouraged to make a submission to the Titanic competition.
# > To do this, follow the instructions in the **[notebook here](https://www.kaggle.com/alexisbcook/titanic-tutorial)**.
#
# The notebook is beginner-friendly and does not assume you have any experience with coding.  At the same time, you'll learn how to author your own notebooks on Kaggle, and it gives you a great idea of what you'll be able to do if you continue to learn data science!
#
# # Keep going
#
# Congratulations!  You have just finished the first exercise in the Intro to Programming course!
#
# You are now ready to learn how to **[organize your code with functions](https://www.kaggle.com/alexisbcook/functions)**.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*
