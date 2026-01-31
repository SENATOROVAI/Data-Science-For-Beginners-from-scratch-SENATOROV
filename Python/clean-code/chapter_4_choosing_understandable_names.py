"""Chapter 4 - Choosing understandable names."""

# **Casing styles**
#
# Since Python identifiers are case-sensitive and cannot contain spaces, programmers use different naming styles to represent multiple words in an identifier:
#
# - Snake case: Words are separated with an underscores (_), which looks like a flat snake in between each word
# (e.g., my_variable_name). All letters are lowercase, while constants are commonly written in upper snake case style
# (e.g., MAX_CONNECTIONS).
# - Camel case: Words are divided by capitalizing the first letter of each word after the initial one. Typically, the first word starts with a lowercase letter, and the capital letters in the middle mimic a camel’s humps
# (e.g., myVariableName).
# - Pascal case (PascalCase): Similar to camel case, but the first word also begins with a capital letter. This style is named after the Pascal programming language (e.g., MyClassName).
#
# Snake case and camel case are the most widely used styles. Although any naming convention can be selected, it’s important to stick to one consistently throughout a project.

# **PEP 8’s Naming Conventions:**
#
# - All letters should be standard ASCII characters — both uppercase and lowercase English letters without accent marks.
# - Module names should be short and written in all lowercase letters.
# - Class names should follow PascalCase formatting.
# - Constant variables should be written using uppercase letters in SNAKE_CASE.
# - Names for functions, methods, and variables should use lowercase snake_case.
# - The first parameter in instance methods should always be named self (in lowercase).
# - The first parameter in class methods should always be named cls (in lowercase).
# - Private attributes in classes should always start with a single underscore (_).
# - Public attributes in classes should never start with an underscore.

# **Best Practices and Useful Tips on Naming in Python**
#
# - Avoid using names that are too short (like h or aux) or unclear (such as start).
# - Prefer longer, descriptive names that make the code easier to read (for example, totalAnnualRevenue).
# - Short names are acceptable for loop counters (m, n, p) and coordinates (lat, lon).
# - Don’t use unnecessary prefixes — use attribute access directly (for instance, Dog.age instead of dogAge).
# - Avoid Hungarian notation (such as strTitle or bIsActive).
# - For boolean values, use prefixes like is_ or has_ (e.g., is_valid, has_access()).
# - Add units to variable names where relevant to avoid confusion (for example, distance_miles).

# **Hold off on Overwriting Built-in Names in Python**
#
# - Don’t use Python’s built-in names (like list, input, max, id, etc.) for your variables.
# - To check if a name is built-in, type it in the Python shell and see if it returns a function or object.
# - Avoid giving your .py files the same name as existing modules (for example, naming a file json.py can shadow the real json module).
# - If you encounter an unexpected AttributeError, it might be a sign that a built-in name was accidentally overwritten.
