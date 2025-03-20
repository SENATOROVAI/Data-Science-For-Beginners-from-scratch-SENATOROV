"""String and dictionaries."""

# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/strings-and-dictionaries).**
#
# ---
#

# You are almost done with the course. Nice job!
#
# We have a couple more interesting problems for you before you go.
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

# Let's start with a string lightning round to warm up. What are the lengths of the strings below?
#
# For each of the five strings below, predict what `len()` would return when passed that string. Use the variable `length` to record your answer, then run the cell to check whether you were right.
#
# # 0a.

a_val = ""
length = len(a_val)
# q0.a.check()

# # 0b.

b_val = "it's ok"
length = len(b_val)
# q0.b.check()

# # 0c.

c_val = "it's ok"
length = len(c_val)
# q0.c.check()

# # 0d.

d_val = """hey"""
length = len(d_val)
# q0.d.check()

# # 0e.

e_val = "\n"
length = len(e_val)
# q0.e.check()

# # 1.
#
# There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.
#
# HINT: `str` has a method that will be useful here. Use `help(str)` to review a list of string methods.


# +
def is_valid_zip(zip_code: str) -> bool:
    """Return whether the input string is a valid (5 digit) zip code."""
    return len(zip_code) == 5 and zip_code.isdigit()


# Check your answer
# q1.check()

# +
# q1.hint()
# q1.solution()
# -

# # 2.
#
# A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.
#
# Your function should meet the following criteria:
#
# - Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
# - She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
# - Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.


# +
def word_search(doc_list: list[str], keyword: str) -> list[int]:
    """Return indices of documents containing the exact keyword."""
    indices = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip(".,").lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


# Check your answer
# q2.check()

# +
# q2.hint()
# q2.solution()
# -

# # 3.
#
# Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.
#
# (You're encouraged to use the `word_search` function you just wrote when implementing this function. Reusing code in this way makes your programs more robust and readable - and it saves typing!)


# +
def multi_word_search(
    documents: list[str], keywords: list[str]
) -> dict[str, list[int]]:
    """Return dict mapping each keyword to list of document indices."""
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices


# Check your answer
# q3.check()

# +
# q3.solution()
# -

# # Keep Going
#
# You've learned a lot. But even the best programmers rely heavily on "libraries" of code from other programmers. You'll learn about that in **[the last lesson](https://www.kaggle.com/colinmorris/working-with-external-libraries)**.
#

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
