# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/working-with-external-libraries).**
#
# ---

"""External libraries."""

# # Try It Yourself
#
# There are only three problems in this last set of exercises, but they're all pretty tricky, so be on guard!
#
# Run the setup code below before working on the questions.

# +
# fmt: off
from learntools.core import binder
from learntools.intro_to_programming.ex5 import *  # pylint: disable=W0401
# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

binder.bind(globals())
print('Setup complete.')
# fmt: on
# -

# # 1.
#
# After completing the exercises on lists and tuples, Jimmy noticed that, according to his `estimate_average_slot_payout` function, the slot machines at the Learn Python Casino are actually rigged *against* the house, and are profitable to play in the long run.
#
# Starting with $200 in his pocket, Jimmy has played the slots 500 times, recording his new balance in a list after each spin. He used Python's `matplotlib` library to make a graph of his balance over time:

# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph


# As you can see, he's hit a bit of bad luck recently. He wants to tweet this along with some choice emojis, but, as it looks right now, his followers will probably find it confusing. He's asked if you can help him make the following changes:
#
# 1. Add the title "Results of 500 slot machine pulls"
# 2. Make the y-axis start at 0.
# 3. Add the label "Balance" to the y-axis
#
# After calling `type(graph)` you see that Jimmy's graph is of type `matplotlib.axes._subplots.AxesSubplot`. Hm, that's a new one. By calling `dir(graph)`, you find three methods that seem like they'll be useful: `.set_title()`, `.set_ylim()`, and `.set_ylabel()`.
#
# Use these methods to complete the function `prettify_graph` according to Jimmy's requests. We've already checked off the first request for you (setting a title).
#
# (Remember: if you don't know what these methods do, use the `help()` function!)


# +
def prettify_graph(graph_val) -> None:  # type: ignore
    """Format a matplotlib graph with title, labels and dollar amounts."""
    graph_val.set_title("Results of 500 slot machine pulls")
    # Make the y-axis begin at 0
    graph_val.set_ylim(bottom=0)
    # Label the y-axis
    graph_val.set_ylabel("Balance")
    # Bonus: format the numbers on the y-axis as dollar amounts
    # An array of the values displayed on the y-axis (150, 175, 200, etc.)
    ticks = graph_val.get_yticks()
    # Format those values into strings beginning with dollar sign
    new_labels = [f"${int(amt)}" for amt in ticks]
    # Set the new labels
    graph_val.set_yticklabels(new_labels)


graph_view = jimmy_slots.get_graph()
prettify_graph(graph_view)
graph_view


# -

# **Bonus:** Can you format the numbers on the y-axis so they look like dollar amounts? e.g. $200 instead of just 200.
#
# (We're not going to tell you what method(s) to use here. You'll need to go digging yourself with `dir(graph)` and/or `help(graph)`.)

# # 2. <span title="Spicy" style="color: coral">🌶️🌶️</span>
#
# This is a very challenging problem.  Don't forget that you can receive a hint!
#
# Luigi is trying to perform an analysis to determine the best items for winning races on the Mario Kart circuit. He has some data in the form of lists of dictionaries that look like...
#
#     [
#         {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
#         {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
#         # Sometimes the racer's name wasn't recorded
#         {'name': None, 'items': ['mushroom',], 'finish': 2},
#         {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
#     ]
#
# `'items'` is a list of all the power-up items the racer picked up in that race, and `'finish'` was their placement in the race (1 for first place, 3 for third, etc.).
#
# He wrote the function below to take a list like this and return a dictionary mapping each item to how many times it was picked up by first-place finishers.


def best_items(racers):  # type: ignore
    """Count items picked up by first place racers."""
    winner_item_counts = {}
    for i, racer in enumerate(racers):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer["finish"] == 1:
            for i in racer["items"]:
                # Add one to the count for this item
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name
        # set. We'll take care of it later.
        if racer["name"] is None:
            warning = """
                WARNING: Encountered racer with unknown name on iteration
            """
            print(f"{warning} {i + 1}/{len(racers)} (racer = {racer['name']})")

    return winner_item_counts


# He tried it on a small example list above and it seemed to work correctly:

sample = [
    {
        "name": "Peach",
        "items": [
            "green shell",
            "banana",
            "green shell",
        ],
        "finish": 3,
    },
    {
        "name": "Bowser",
        "items": [
            "green shell",
        ],
        "finish": 1,
    },
    {
        "name": None,
        "items": [
            "mushroom",
        ],
        "finish": 2,
    },
    {"name": "Toad", "items": ["green shell", "mushroom"], "finish": 1},
]
best_items(sample)  # type: ignore

# However, when he tried running it on his full dataset, the program crashed with a `TypeError`.
#
# Can you guess why? Try running the code cell below to see the error message Luigi is getting. Once you've identified the bug, fix it in the cell below (so that it runs without any errors).
#
# Hint: Luigi's bug is similar to one we encountered in the [tutorial](https://www.kaggle.com/colinmorris/working-with-external-libraries) when we talked about star imports.

# +
# Fixed version


def best_items_v2(racers):  # type: ignore
    """Count items used by winners in a racing game."""
    winner_item_counts = {}
    for idx, racer in enumerate(racers):
        racer = racers[idx]

        if racer["finish"] == 1:
            for item in racer["items"]:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        if racer["name"] is None:
            warning = """
                WARNING: Encountered racer with unknown name on iteration
            """
            print(f"{warning} {idx + 1}/{len(racers)} (racer = {racer})")

    return winner_item_counts


best_items_v2(full_dataset)  # type: ignore


# +
# q2.hint()

# +
# Check your answer (Run this code cell to receive credit!)
# q2.solution()
# -

# # 3. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
#
# Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with this type is overload the comparison operators like `>` and `<=` so that we could use them to check whether one hand beats another. e.g. it'd be cool if we could do this:
#
# ```python
# hand1 = BlackjackHand(["K", "A"])
# hand2 = BlackjackHand(["7", "10", "A"])
# hand1 > hand2
# ```
#
# Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these lessons), but the code we're asking you to write in the function below is very similar to what we'd have to write if we were defining our own `BlackjackHand` class. (We'd put it in the `__gt__` magic method to define our custom behaviour for `>`.)
#
# Fill in the body of the `blackjack_hand_greater_than` function according to the docstring.


# +
def hand_total(hand: list[str]) -> int:
    """Calculate total points of a blackjack hand."""
    total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            aces += 1
        else:
            total += int(card)

    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total


def is_blackjack_hand_greater_than(h_1: list[str], h_2: list[str]) -> bool:
    """Compare two blackjack hands and return if first hand beats."""
    total_1 = hand_total(h_1)
    total_2 = hand_total(h_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)


# Check your answer
# q3.check()

# +
# q3.hint()
# q3.solution()
# -

# # The End
#
# You've finished the Python course. Congrats!
#
# You probably didn't put in all these hours of learning Python just to play silly games of chance, right? If you're interested in applying your newfound Python skills to some data science tasks, we strongly recommend **[this tutorial](https://www.kaggle.com/alexisbcook/titanic-tutorial)**, which will teach you how to make your very first submission to a Kaggle competition.
#
# You can also check out some of our other **[Kaggle Courses](https://www.kaggle.com/learn/overview)**. Some good next steps are:
#
# 1. [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
# 2. [Pandas for data manipulation](https://www.kaggle.com/learn/pandas)
# 3. [Data Visualization](https://www.kaggle.com/learn/data-visualization)
#
# Happy Pythoning!

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
