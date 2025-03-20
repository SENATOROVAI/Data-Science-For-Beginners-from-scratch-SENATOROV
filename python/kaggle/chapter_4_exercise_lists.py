"""Lists."""

# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/lists).**
#
# ---
#

# Things get more interesting with lists. You'll apply your new knowledge to solve the questions below. Remember to run the following cell first.

# +
from learntools.core import binder
# fmt: off
from learntools.python.ex3 import *  # pylint: disable=W0401

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # 1.
#
# Complete the function below according to its docstring.


# +
def select_second(list_val: list[int]) -> int | None:
    """Return the second element of the given list, else None."""
    return list_val[1] if len(list_val) > 2 else None


# Check your answer
# q1.check()

# +
# q1.hint()
# q1.solution()
# -

# # 2.
#
# You are analyzing sports teams.  Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that.
# These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.  Complete the function below to select the **captain** of the worst team.


# +
def losing_team_captain(teams: list[list[str]]) -> str:
    """Return the 2nd player (captain) from the last listed team."""
    return teams[-1][1]


# Check your answer
# q2.check()

# +
# q2.hint()
# q2.solution()
# -

# # 3.
#
# The next iteration of Mario Kart will feature an extra-infuriating new item, the *Purple Shell*. When used, it warps the last place racer into first place and the first place racer into last place. Complete the function below to implement the Purple Shell's effect.


# +
def purple_shell(racers: list[str]) -> None:
    """Given a list of racers, set the first place racer to last."""
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp


# Check your answer
# q3.check()

# +
# q3.hint()
# q3.solution()
# -

# # 4.
#
# What are the lengths of the following lists? Fill in the variable `lengths` with your predictions. (Try to make a prediction for each list *without* just calling `len()` on it.)

# +
a_val = [1, 2, 3]
b_val = [1, [2, 3]]
c_val: list[int] = []
d_val = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

# Check your answer
# q4.check()

# +
# line below provides some explanation
# q4.solution()
# -

# # 5. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
#
# We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:
#
#     party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
#
# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
#
# Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.


# +
def is_fashionably_late(arrivals: list[str], name: str) -> bool:
    """Return whether the guest with that name was fashionably late."""
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


# Check your answer
# q5.check()

# +
# q5.hint()
# q5.solution()
# -

# # Keep Going
#
# That's it for lists and tuples! Now you have the baseline knowledge to **[learn about loops](https://www.kaggle.com/colinmorris/loops-and-list-comprehensions)**, which is where lists and tuples get really interesting.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
