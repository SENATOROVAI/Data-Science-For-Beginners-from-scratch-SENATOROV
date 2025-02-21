"""Chapter 4 - Choose the right name."""

# In Python, identifiers are case-sensitive and cannot contain spaces, so programmers use different naming conventions for multi-word identifiers.
#
# - Snake case (snake_case): Words are separated by underscores (_), resembling a snake slithering between words. All letters are lowercase, while constants are often written in UPPER_SNAKE_CASE.
# - Camel case (camelCase): The first word is in lowercase, while subsequent words start with an uppercase letter, resembling camel humps.
# - Pascal case (PascalCase): Similar to camel case, but the first word also starts with an uppercase letter. It is named after the Pascal programming language.
#
# Snake case and camel case are the most commonly used. While any convention can be chosen, only one should be used consistently within a project.

# **PEP 8 (Chapter 3) provides guidelines for naming in Python:**
#
# - Use ASCII letters (uppercase and lowercase) without diacritics.
# - Module names should be short and in lowercase.
# - Class names should follow PascalCase.
# - Constants should be in UPPER_SNAKE_CASE.
# - Functions, methods, and variable names should be in snake_case.
# - The first argument of instance methods should always be self (lowercase).
# - The first argument of class methods should always be cls (lowercase).
# - Private class attributes should start with an underscore (_).
# - Public class attributes should not start with an underscore.
#

# **Python Naming Best Practices**
#
# - Avoid names that are too short (g, mon) or unclear (start).
# - Longer, meaningful names improve readability (salesClientMonthlyPayment).
# - Loop indices (i, j, k) and coordinates (x, y) are acceptable short names.
# - No unnecessary prefixes (Cat.weight, not catWeight).
# - Avoid Hungarian notation (strName, iVacationDays).
# - Use is_ / has_ for booleans (is_vehicle, has_key()).
# - Include units (weight_kg) to prevent errors.

# **Avoid Overwriting Built-in Names in Python**
#
# - Do not use built-in names (list, set, open, sum, etc.) for variables.
# - Check if a name is built-in by typing it in the Python shell.
# - Avoid naming .py files after existing modules, e.g., pyperclip.py, as it may override the actual module.
# - Unexpected AttributeError can indicate accidental overwriting.
