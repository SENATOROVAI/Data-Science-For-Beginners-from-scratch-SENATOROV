"""Conditional statements."""

# **This notebook is an exercise in the [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/conditions-and-conditional-statements).**
#
# ---
#

# In the tutorial, you learned about conditions and conditional statements. In this exercise, you will use what you learned to answer several questions.
#
# # Set up the notebook
#
# Run the next code cell without changes to set up the notebook.

# +
# fmt: off
from learntools.core import binder
from learntools.intro_to_programming.ex4 import *  # pylint: disable=W0401
# import functions needed to make get_labels work
from learntools.intro_to_programming.ex4q5 import (excess_calories,
                                                   excess_saturated_fat,
                                                   excess_sodium, excess_sugar,
                                                   excess_trans_fat)

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # Question 1
#
# You work at a college admissions office.  When inspecting a dataset of college applicants, you notice that some students have represented their grades with letters (`"A"`, `"B"`, `"C"`, `"D"`, `"F"`), whereas others have represented their grades with a number between 0 and 100.
#
# You realize that for consistency, all of the grades should be formatted in the same way, and you decide to format them all as letters.  For the conversion, you decide to assign:
# - `"A"` - any grade 90-100, inclusive
# - `"B"` - any grade 80-89, inclusive
# - `"C"` - any grade 70-79, inclusive
# - `"D"` - any grade 60-69, inclusive
# - `"F"` - any grade <60
#
# Write a function `get_grade()` that takes as input:
# - `score` - an integer 0-100 corresponding to a numerical grade
#
# It should return a Python string with the letter grade that it corresponds to.  For instance,
# - A score of 85 corresponds to a B grade.  In other words, `get_grade(85)` should return `"B"`.
# - A score of 49 corresponds to an F grade.  In other words, `get_grade(49)` should return `"F"`.
#
# Make sure that when supplying the grade that is returned by the function, it is enclosed in quotes.  (For instance, if you want to return `"A"`, you should write `return "A"` and not `return A`.)


# +
def get_grade(score: int) -> str:
    """Convert numerical score (0-100) to letter grade (A-F)."""
    if 90 <= score <= 100:
        return "A"
    if 80 <= score <= 89:
        return "B"
    if 70 <= score <= 79:
        return "C"
    if 60 <= score <= 69:
        return "D"
    return "F"


# Check your answer
# q1.check()

# +
# Uncomment to see a hint
# q1.hint()

# Uncomment to see the solution
# q1.solution()
# -

# # Question 2
#
# In the exercise for the previous lesson, you wrote a function `cost_of_project()` that estimated the price of rings for an online shop that sells rings with custom engravings.  This function did not use conditional statements.  In this exercise, you will rewrite the function to use conditional statements.  Recall that the online shop has the following price structure:
# - Gold plated rings have a base cost of \\$50, and you charge \\$7 per engraved unit.
# - Solid gold rings have a base cost of \\$100, and you charge \\$10 per engraved unit.
# - Spaces and punctuation are counted as engraved units.
#
# Your function `cost_of_project()` takes two arguments:
# - `engraving` - a Python string with the text of the engraving
# - `solid_gold` - a Boolean that indicates whether the ring is solid gold
#
# It should return the cost of the project.
#
# The function has been partially completed for you, and you need to fill in the blanks to complete the function.


# +
def cost_of_project(engraving: str, solid_gold: bool) -> float:
    """Calculate cost of ring with engraving based on material type."""
    if solid_gold is True:
        cost = 100 + (10 * len(engraving))
    else:
        cost = 50 + (7 * len(engraving))
    return cost


# Check your answer
# q2.check()

# +
# Uncomment to see a hint
# q2.hint()

# Uncomment to see the solution
# q2.solution()
# -

# # Question 3
#
# You are a programmer at a water agency.  Recently, you have been tasked to write a function `get_water_bill()` that takes as input:
# - `num_gallons` = the number of gallons of water that a customer used that month.  (This will always be an integer with no decimal part.)
#
# It should output the water bill.
#
# The water agency uses this pricing structure:
# <table style="width: 100%;">
# <tbody>
# <tr><th><b>Tier</b></th><th><b>Amount in gallons</b></th><th><b>Price per 1000 gallons</b></th></tr>
# <tr>
# <td>Tier 1</td>
# <td>0 - 8,000</td>
# <td>\$5</td>
# </tr>
# <tr>
# <td>Tier 2</td>
# <td>8,001 - 22,000</td>
# <td>\$6</td>
# </tr>
# <tr>
# <td>Tier 3</td>
# <td>22,001 - 30,000</td>
# <td>\$7</td>
# </tr>
# <tr>
# <td>Tier 4</td>
# <td>30,001+</td>
# <td>\$10</td>
# </tr>
# </tbody>
# </table>
#
# For example:
# - Someone who uses 10,000 gallons of water in a month is placed in Tier 2, and needs to pay a water bill of \\$6 * 10 = \\$60.  In other words, `get_water_bill(10000)` should return `60.0`.
# - Someone who uses 25,000 gallons of water in a month is placed in Tier 3, and needs to pay a water bill of \\$7 * 25 = \\$175.  In other words, `get_water_bill(25000)` should return `175.0`.
#
# **Do not round your answer.**  So, your answer might return fractions of a penny.


# +
def get_water_bill(num_gallons: int) -> float:
    """Calculate water bill based on gallons used."""
    if num_gallons <= 8000:
        bill = (num_gallons / 1000) * 5
    elif num_gallons <= 22000:
        bill = (num_gallons / 1000) * 6
    elif num_gallons <= 30000:
        bill = (num_gallons / 1000) * 7
    else:
        bill = (num_gallons / 1000) * 10

    return bill


# Check your answer
# q3.check()

# +
# Uncomment to see a hint
# q3.hint()

# Uncomment to see the solution
# q3.solution()
# -

# # Question 4
#
# You work for a company that provides data services.  For \\$100/month, your company provides 15 gigabytes (GB) of data.  Then, any additional data is billed at \\$0.10/MB (or \\$100/GB, since 1,000 MB are in 1 GB).
#
# Use the next code cell to write a function `get_phone_bill()` that takes as input:
# - `gb` = number of GB that the customer used in a month
#
# It should return the customer's total phone bill.
#
# For instance:
# - A customer who uses 10 GB of data in one month is billed only \\$100, since the usage stayed under 15 GB.  In other words, `get_phone_bill(10)` should return `100`.
# - A customer who uses 15.1 GB (or 15 GB + 100 MB) of data in one month has gone over by .1 GB, so they must pay \\$100 (cost of plan), plus \\$0.10 * 100 = \\$10, for a total bill of \\$110.  In other words, `get_phone_bill(15.1)` should return `110`.
#
# Do not round your answer.


# +
# TODO: Edit the function to return the correct bill for different # pylint: disable=W0511
# values of GB
def get_phone_bill(gb: float) -> float:
    """Calculate phone bill based on GB used."""
    base_cost = 100
    if gb > 15:
        extra_gb = gb - 15
        extra_cost = extra_gb * 100
        return base_cost + extra_cost
    return base_cost


# Check your answer
# q4.check()

# +
# Uncomment to see a hint
# q4.hint()

# Uncomment to see the solution
# q4.solution()
# -

# # 🌶️ Question 5
#
# In Mexico, foods and beverages that are high in saturated fat, trans fat, sugar, sodium, and/or calories appear with warning labels that are designed to help consumers make healthy food choices.
#
# For instance, the [box of cookies](https://world.openfoodfacts.org/product/7501000673209/florentinas-gamesa) in the image below appears with two labels (in the upper right corner):
# - EXCESO CALORÍAS (in English, EXCESS CALORIES)
# - EXCESO AZÚCARES (in English, EXCESS SUGAR)
#
# <center><img src="https://storage.googleapis.com/kaggle-media/learn/images/VXYKHnM.png" alt="drawing" width="500"/></center>
#
# In this question, you'll work with a function `get_labels()` that takes the nutritional details about a food item and prints the needed warning labels.  This function takes several inputs:
# - `food_type` = one of `"solid"` or `"liquid"`
# - `serving_size` = size of one serving (if solid, in grams; if liquid, in milliliters)
# - `calories_per_serving` = calories in one serving
# - `saturated_fat_g` = grams of saturated fat in one serving
# - `trans_fat_g` = grams of trans fat in one serving
# - `sodium_mg` = mg of sodium in one serving
# - `sugars_g` = grams of sugar in one serving
#
# Note that some of the code here should feel unfamiliar to you, since we have not shared the details of how some of the functions like `excess_sugar()` or `excess_saturated_fat()` work.  But at a high level, these are functions that return a value of `True` if the food is deemed to have an excess of sugar or saturated fat, respectively.  These functions are used within the `get_labels()` function, and whenever there is an excess (of sugar or saturated fat, but also of trans fat, sodium, or calories), it prints the corresponding label.


def get_labels(food_info: dict[str, float | str]) -> None:
    """Print warning labels for food items based on nutritional content."""
    # Map fields from dict
    sugars = food_info["sugars_g"]
    calories = food_info["calories_per_serving"]
    saturated_fat = food_info["saturated_fat_g"]
    trans_fat = food_info["trans_fat_g"]
    sodium = food_info["sodium_mg"]
    food_type = food_info["food_type"]
    serving_size = food_info["serving_size"]

    # Print messages based on findings
    if excess_sugar(sugars, calories) is True:
        print("EXCESO AZÚCARES / EXCESS SUGAR")
    if excess_saturated_fat(saturated_fat, calories) is True:
        print("EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT")
    if excess_trans_fat(trans_fat, calories) is True:
        print("EXCESO GRASAS TRANS / EXCESS TRANS FAT")
    if excess_sodium(calories, sodium) is True:
        print("EXCESO SODIO / EXCESS SODIUM")
    if excess_calories(food_type, calories, serving_size) is True:
        print("EXCESO CALORÍAS / EXCESS CALORIES")


# The next code cell demonstrates how to use `get_labels()` to get the warning labels that the food item should contain.  We begin with [bologna](https://world.openfoodfacts.org/product/4099100179378/bologna).  Here is [an image](https://storage.googleapis.com/kaggle-media/learn/images/Cfcx72e.png) with all of the nutritional information.  Note that for this food,
# - `food_type = "solid"` (because bologna is a solid and not a liquid)
# - `serving_size = 32` (the serving size is 32 grams)
# - `calories_per_serving = 110` (there are 110 calories per serving)
# - `saturated_fat_g = 2.5` (there are 2.5 grams of saturated fat per serving)
# - `trans_fat_g = 0` (there are 0 grams of trans fat per serving)
# - `sodium_mg = 400` (there are 400 mg of sodium per serving)
# - `sugars_g = 1` (the nutrition facts say <1g, but we will round it up to 1 gram per serving to be safe)
#
# By supplying all of these values to the function, we can print the warning labels.

# bologna https://world.openfoodfacts.org/product/4099100179378/bologna
get_labels(
    {
        "food_type": "solid",
        "serving_size": 40,
        "calories_per_serving": 150,
        "saturated_fat_g": 0,
        "trans_fat_g": 0,
        "sodium_mg": 150,
        "sugars_g": 16,
    }
)

# This bologna has three labels, printed in the output above.
#
# For the rest of this question, you will use the same `get_labels()` function to determine the labels for more foods.  This question is designed to help you get practice with feeling comfortable with code that other people have written, and where you don't have time to review every single line of code before interacting with it.  For instance, when you take the [Intro to Machine Learning course](http://www.kaggle.com/learn/intro-to-machine-learning), you'll work with a Python package called "scikit-learn", which is a large collection of code that you'll learn how to run without reviewing all of the code in detail (as it would take too long, and you can trust that it was implemented correctly).
#
# In general, as you continue coding in Python, you will often be running code that other people have written.  This is common practice for advanced programmers.
#
# In the next code cell, fill in the values for [this cereal](https://world.openfoodfacts.org/product/7501008023624/zucaritas-kellogg-s).  Here is [an image](https://storage.googleapis.com/kaggle-media/learn/images/MUxzHVU.png) with all of the nutritional information.
#
# **Note**: running the line of code below as-is will return an error.  You have to fill in the nutritional values first.

# zucaritas cereal
# https://world.openfoodfacts.org/product/7501008023624/zucaritas-kellogg-s
# TODO: Uncomment the line below, fill in the values, and run the function # pylint: disable=W0511
get_labels(
    {
        "food_type": "solid",
        "serving_size": 32,
        "calories_per_serving": 110,
        "saturated_fat_g": 2.5,
        "trans_fat_g": 0,
        "sodium_mg": 400,
        "sugars_g": 1,
    }
)

# Next, try [these mozzarella sticks](https://world-es.openfoodfacts.org/producto/0062325540104/mozzarella-cheese-sticks).  Here is [an image](https://storage.googleapis.com/kaggle-media/learn/images/rcdB7VH.png) with all of the nutritional information.

# +
# Get credit for completing the problem
# q5.check()
# -

# # Keep going
#
# Continue to the next lesson to **[learn about Python lists](https://www.kaggle.com/alexisbcook/intro-to-lists)**.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*
