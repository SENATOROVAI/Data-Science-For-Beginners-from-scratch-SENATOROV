"""Booleans and conditionals."""

# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/booleans-and-conditionals).**
#
# ---
#

# In this exercise, you'll put to work what you have learned about booleans and conditionals.
#
# To get started, **run the setup code below** before writing your own code (and if you leave this notebook and come back later, don't forget to run the setup code again).

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
# Many programming languages have [`sign`](https://en.wikipedia.org/wiki/Sign_function) available as a built-in function. Python doesn't, but we can define our own!
#
# In the cell below, define a function called `sign` which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

# +
# Your code goes here. Define a function called 'sign'

# Check your answer
# q1.check()

# +
# q1.solution()
# -

# # 2.
#
# We've decided to add "logging" to our `to_smash` function from the previous exercise.


# +
def to_smash(total_candies: int) -> int:
    """Return the number of leftover candies that must be smashed."""
    print("Splitting", total_candies, "candies")
    return total_candies % 3


to_smash(91)
# -

# What happens if we call it with `total_candies = 1`?

to_smash(1)


# That isn't great grammar!
#
# Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies")


# +
def to_smash_v2(total_candies: int) -> int:
    """Return the number of leftover candies that must be smashed."""
    postfix = "candy" if total_candies == 1 else "candies"
    print("Splitting", total_candies, postfix)
    return total_candies % 3


to_smash_v2(91)
to_smash_v2(1)


# -

# To get credit for completing this problem, and to see the official answer, run the code cell below.

# +
# Check your answer (Run this code cell to receive credit!)
# q2.solution()
# -

# # 3. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
#
# In the tutorial, we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...
# - I have an umbrella...
# - or if the rain isn't too heavy and I have a hood...
# - otherwise, I'm still fine unless it's raining *and* it's a workday
#
# The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?
#
# To prove that `prepared_for_weather` is buggy, come up with a set of inputs where either:
# - the function returns `False` (but should have returned `True`), or
# - the function returned `True` (but should have returned `False`).
#
# To get credit for completing this question, your code should return a <font color='#33cc33'>Correct</font> result.

# # 4.
#
# The function `is_negative` below is implemented correctly - it returns True if the given number is negative and False otherwise.
#
# However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by *75%* while keeping the same behaviour.
#
# See if you can come up with an equivalent body that uses just **one line** of code, and put it in the function `concise_is_negative`. (HINT: you don't even need Python's ternary syntax)


# +
def is_negative(number: float) -> bool:
    """Return True if number is negative, False otherwise."""
    if number < 0:
        return True
    return False


def is_concise_is_negative(number: float) -> bool:
    """Return True if number is negative, False otherwise."""
    return number < 0


# Check your answer
# q4.check()

# +
# q4.hint()
# q4.solution()
# -

# # 5a.
#
# The boolean variables `ketchup`, `mustard` and `onion` represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:


def is_onionless(ketchup: bool, mustard: bool, onion: bool) -> bool:
    """Return whether the customer doesn't want onions."""
    # pylint: disable=unused-argument
    return not onion


# +
def is_wants_all_toppings(ketchup: bool, mustard: bool, onion: bool) -> bool:
    """Return whether the customer wants "the works" (all 3 toppings)."""
    return ketchup and mustard and onion


# Check your answer
# q5.a.check()

# +
# q5.a.hint()
# q5.a.solution()
# -

# # 5b.
#
# For the next function, fill in the body to match the English description in the docstring.


# +
def is_wants_plain_hotdog(ketchup: bool, mustard: bool, onion: bool) -> bool:
    """Return whether the customer wants a plain hot dog with no toppings."""
    return not ketchup and not mustard and not onion


# Check your answer
# q5.b.check()

# +
# q5.b.hint()
# q5.b.solution()
# -

# # 5c.
#
# You know what to do: for the next function, fill in the body to match the English description in the docstring.


# +
def is_exactly_one_sauce(ketchup: bool, mustard: bool, onion: bool) -> bool:
    """Return whether a customer wants either ketchup or mustard, not both."""
    # pylint: disable=unused-argument
    return (ketchup or mustard) and not (ketchup and mustard)


# Check your answer
# q5.c.check()

# +
# q5.c.hint()
# q5.c.solution()
# -

# # 6. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
#
# We’ve seen that calling `bool()` on an integer returns `False` if it’s equal to 0 and `True` otherwise. What happens if we call `int()` on a bool? Try it out in the notebook cell below.
#
# Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?


# +
def is_exactly_one_topping(ketchup: bool, mustard: bool, onion: bool) -> bool:
    """Return whether the customer wants exactly one of the three toppings."""
    return len([val for val in [ketchup, mustard, onion] if val is True]) == 1


# Check your answer
# q6.check()

# +
# q6.hint()
# q6.solution()
# -

# # 7. <span title="A bit spicy" style="color: darkgreen ">🌶️</span> (Optional)
#
# In this problem we'll be working with a simplified version of [blackjack](https://en.wikipedia.org/wiki/Blackjack) (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:
#
# - The player is dealt two face-up cards. The dealer is dealt one face-up card.
# - The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
# - The dealer then deals additional cards to himself until either:
#     - the sum of the dealer's cards exceeds 21, in which case the player wins the round
#     - the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
#
# When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)
#
# For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:

# fmt:off
def is_should_hit(
    dealer_total: int,
    player_total: int,
    player_low_aces: int,
    player_high_aces: int
) -> bool:
    """Decides whether the player should hit in a blackjack game."""
    # pylint: disable=unused-argument
    if player_total <= 11:
        return True

    if player_total == 17 and player_high_aces > 0:
        return True

    if player_total < 17 and dealer_total >= 7:
        return True

    if player_total >= 12 and dealer_total <= 6:
        return False

    return player_total < 17
# fmt: on


# This very conservative agent *always* sticks with the hand of two cards that they're dealt.
#
# We'll be simulating games between your player agent and our own dealer agent by calling your function.
#
# Try running the function below to see an example of a simulated game:

# +
# q7.simulate_one_game()
# -

# The real test of your agent's mettle is their average win rate over many games. Try calling the function below to simulate 50000 games of blackjack (it may take a couple seconds):

# +
# q7.simulate(n_games=50000)
# -

# Our dumb agent that completely ignores the game state still manages to win shockingly often!
#
# Try adding some more smarts to the `should_hit` function and see how it affects the results.

# +
# fmt: off
def is_should_hit_v2(
    dealer_total: int,
    player_total: int,
    player_low_aces: int,
    player_high_aces: int
) -> bool:
    """Return whether the player should hit based on strategy."""
    # pylint: disable=unused-argument,too-many-return-statements
    if player_total <= 11:
        return True

    if player_high_aces > 0:
        if player_total <= 16:
            return True
        if player_total == 17:
            return dealer_total >= 7
        if player_total == 18:
            return dealer_total in [9, 10, 11]
        return False

    if player_total >= 17:
        return False

    if player_total < 17 and dealer_total >= 7:
        return True

    if player_total >= 12 and dealer_total <= 6:
        return False

    return True

# fmt: on
# q7.simulate(n_games=50000)
# -

# # Keep Going
#
# Learn about **[lists and tuples](https://www.kaggle.com/colinmorris/lists)** to handle multiple items of data in a systematic way.

# ---
#
#
#
#
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
