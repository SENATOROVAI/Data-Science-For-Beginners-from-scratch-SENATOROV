# %%
"""Answers about commit types and Conventional Commits examples."""

# %% [markdown]
# Question 1 - Describe in your own words the purpose of each of these commit types.
#
# - **feat** — adds a new feature or functionality to the project
# - **fix** — fixes a bug in existing code
# - **docs** — changes only to documentation (README, comments, docstrings)
# - **style** — formatting changes (indentation, spaces, semicolons) that don't affect logic
# - **refactor** — restructuring code without changing its behavior or fixing a bug
# - **test** — adding or correcting tests
# - **build** — changes to the build system or external dependencies
# - **ci** — changes to CI configuration files and scripts
# - **perf** — a code change that improves performance
# - **chore** — routine maintenance tasks that don't touch source or tests
#

# %% [markdown]
# Question 2 - Imagine that you fixed a bug in a function that rounds numbers incorrectly. Make a fictional commit and write a message for it in accordance with Conventional Commits (using the type fix).
#
# git commit -m "fix: correct rounding logic in number formatting function" -m "The function rounded 2.5 down to 2 instead of up to 3. Updated to apply standard half-up rounding."

# %% [markdown]
# Question 3 - Adding new functionality: Suppose you implemented a new generateReport function in the project. Make a fictional commit with the type feat, reflecting the addition of this functionality.
#
# git commit -m "feat: add generateReport function" -m "Implements report generation that aggregates project data and outputs a formatted summary."

# %% [markdown]
# Question 4 - Modifying code format or styles: Imagine that you fixed the indentation and formatting across the whole project without changing the code logic. Make a fictional commit with the type style.
#
# git commit -m "style: fix indentation and formatting across project" -m "Adjusted indentation and whitespace for consistency. No changes to code logic."

# %% [markdown]
# Question 5 - Documentation and testing:
#     Make a fictional commit with the type docs, adding or improving documentation for your new function.
#
# git commit -m "docs: add documentation for generateReport function" -m "Added docstring and usage description explaining the function's parameters and output."
#
#     Make a fictional commit with the type test, adding tests for that same function.
#
# git commit -m "test: add tests for generateReport function" -m "Added unit tests covering normal input, empty input, and edge cases."
#
#
