"""Python basics."""

# ### MAIN PYTHON MANIPULATIONS

# ## Core number operations

# +
import sys

2 + 2
# -

3 - 5

8 / 5  # division always returns a floating point number

17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

# 5**2  # 5 squared

# ## Strings basics
#
# **\\** can be used to escape quotes

# ```python
# "python strings"  # single quotes
# ```

# ```python
# "doesn't"  # use \' to escape the single quote...
# ```

# ```python
# "doesn't"  # double quotes
# ```

# The print() function produces a more readable output, by omitting \
# the enclosing quotes and by printing escaped and special characters

# print('"Isn\'t," they said.')

# If you don't want characters prefaced by “\” to be interpreted as \
# special characters, you can use raw strings by adding an r before the \
# first quote

print("C:\\some\name")  # here \n means newline!

print(r"C:\some\name")  # note the r before the quote

# Concatenation and Repetition Strings can \
# be concatenated (glued together) with the + operator, \
# and repeated with *. To remember this, it is simple. + \
# operator adds, and * operator multiplies(see example)

print("a" + "b")
print("t" * 5)
print("no" * 3 + "dip")

# Two or more string literals (i.e. the ones enclosed between quotes) \
# next to each other are automatically concatenated.

# ```python
# "nil" "abh"
# ```

# Indexing Strings can be indexed
# (subscripted), with the first character having \
# index 0. There is no separate character type;
# a character is simply a string of size one.

word = "Python"
word[0]  # character in position 0

# Indices may also be negative numbers, to start counting from the
# right:

word[-4]

# Slicing In addition to indexing, slicing is also
# supported. While indexing is used to obtain \
# individual characters, slicing allows you to
# obtain substring:

word[0:2]  # characters from position 0 (included) to 2 (excluded)

# Python strings cannot be changed — they are immutable. Therefore, \
# assigning to an indexed position in the string results in an error So, if \
# you try to assign a new value in the string, it will give you an error.

# +
# word[2] = "l"
# -

# The built-in function len() returns the length of a string:
len(word)

# ### OTHER PYTHON-RELATED AFFAIRS

# Syntax of Code in Python Statement Instructions written in the \
# source code for execution are called statements.
# There are different types of statements in Python, \
# like Assignment statement, Conditional \
# statement, Looping statements, etc. These all help the user \
# to get the required output.
# For example, n = 20 is an assignment statement.
#
# Terminating a Statement In Python, the end of the line means \
# the end of the statement.
#
# Semicolon Can Optionally Terminate a Statement. Sometimes it can \
# be used to put multiple statements on a single line.\
# e.g. \
# Multiple Statements in one line, Declared using semicolons (;):

lag = 2
ropes = 3
pole = 4

# Variables and Assignment One of the most powerful features of a programming \
# language is the ability to manipulate variables. A variable is a \
# name that refers to a value. Please note that the variable only refers to the \
# value, to which it is assigned. It doesn't become equal to that value. The \
# moment it is assigned to another value, the old assignment becomes null and
# void automatically.
#
# Variable names can be of any length and can contain both alphabets \
# and numbers. They can be of uppercase or lowercase, but the same \
# name in different cases are different variables, as you must remember, \
# Python is case sensitive language
#
# Here’s a simple way to check which of the given variable names are invalid in Python:
#
# Summary of rules:
#
# * Must start with a letter or underscore (_).
# * Can contain letters, numbers, and underscores.
# * Cannot start with a number.
# * Cannot use Python keywords (reserved words).
# * Cannot contain spaces or special characters (*, @, %, etc.).
#

# ```python
# # Fibonacci series: # the sum of two elements defines the next
# a = 0
# b = 1
# while a < 10:
#     print(a)
#     a, b = b, a + b
# ```

# **Arguments** are anything that we pass in the function. \
# Like, string or variable are the arguments. \
# In Python, arguments are values passed to a function. \
# When the number of arguments is unknown, we use *args, \
# which allows passing multiple values as a tuple.
#
# **Keyword Arguments** in Python are the argument where you provide a name
# to the variable as you pass it into the function, like this: (key=value format), \
# making the function call more readable and flexible.
#
# Example with print():

print([3, 5], sep=" ", end="\n", file=sys.stdout, flush=False)

# **String formatting**

# ```Python
# a = 5
# b = 6
# ab = 5 * 6
# print(f"when {a} is multiplied by {b}, the result is {ab}".format(a, b, ab))
# ```

# **Troubleshooting** is essential when code doesn't work as expected. \
# Python provides informative error messages to help identify issues.
#
# **Major Types of Errors Which Occur Most Frequently:**
# - Syntax Errors – occur when when the correct Python Syntax \
# is not used (e.g., missing colons or parentheses).
# - Runtime Errors – take a place during program execution, frequently \
# in wake of invalid operations (e.g., an attempt to divide the number by zero or using \
# a variable before it was defined).
# - Semantic (Logic) Errors – occur in cases when the meaning of the program (its semantics) \
# is wrong, producing unexpected results.

# ## 3.8 Answers to the exercises
#
# ### 3.8.1
#
# 1.
# - Intelligent Code Assistance – Features like code completion, syntax highlighting, and debugging streamline development.
# - Variable Explorer – Provides an intuitive way to track and inspect data within the workspace.
# - IPython Console – Enables interactive execution and real-time code testing.
# - Integrated Debugger – Helps in efficiently identifying and fixing errors within the code.
# - Pre-installed Scientific Libraries – Comes with essential tools like NumPy, Pandas, and Matplotlib, reducing setup time.
# 2.
# - Addition (+) → a + b → Adds two numbers.
# - Subtraction (-) → a - b → Subtracts the second number from the first.
# - Multiplication (*) → a * b → Multiplies two numbers.
# - Division (/) → a / b → Performs division and always returns a float.
# - Floor Division (//) → a // b → Divides and returns the largest integer less than or equal to the result (rounds down).
# 3.
# - Multiplication (*) → a * b → Multiplies two numbers (e.g., 3 * 4 = 12).
# - Exponentiation ()** → a ** b → Raises the first number to the power of the second (e.g., 3 ** 4 = 81).
# 4. In Python, a statement is a single line of code that executes a specific action, defining the logic,        operations, or control flow within a program.
# 5. A variable in Python is a named reference that stores a value. The = operator is used to assign a value to a variable.
# 6. No, a variable cannot be named "import" in Python because "import" is a reserved keyword used for importing modules.
# 7. No, the statement is incorrect. Python is case-sensitive, meaning "math", "Math", and "MATH" are treated as distinct identifiers.
# 8. Use a comma to separate values, for instance:
#
#     ```python
#     flowers = ["chamomile", "rose", "tulip"]
#     x, y, z = flowers
#     ```
# 9. A syntax error occurs when the Python interpreter fails to understand the code due to structural issues, such as missing colons, parentheses, or incorrect indentation. In contrast, a semantic error happens when the code executes without crashing but produces incorrect or unintended results due to logical mistakes.
# 10.
# - The default separator (sep) in Python is a space (' '), which separates multiple arguments in the print() function.
# - The default end character (end) is a newline ('\n'), meaning the output moves to the next line after printing.
#
# ### 3.8.2
#
# 1. False;
# 2. True;
# 3. False;
# 4. False;
# 5. False;
# 6. False;
# 7. False;
# 8. True;
# 9. False;
# 10. True.

# ### 3.8.3

# +
# 1

first_name = "Ruslan"
last_name = "Kazmiryk"
print(first_name, last_name)
# -

# # 2
#
# length = 23
# height = 8
# area = length * height
# area

# +
# 3

square_32 = 32**2
cube_27 = 27**3

# +
# 4

# Assign values to variables
a_num = 3
b_num = 4

# Calculate both sides of the equation

# Left-hand side: (a + b)^2
lhs = (a_num + b_num) ** 2

# Right-hand side: a^2 + b^2 + 2ab
rhs = a_num**2 + b_num**2 + 2 * a_num * b_num

# Print results
print("LHS:", lhs)
print("RHS:", rhs)

# Verify if both sides are equal
print("Equation holds:", lhs == rhs)

# +
# 5

len("Ruslan")

# +
# 6

print("**********")
print("*        *")
print("*        *")
print("*        *")
print("**********")

# +
# 7

print("PPPPPP")
print("P     P")
print("P     P")
print("PPPPPP")
print("P")
print("P")
print("P")

# +
# 8

name = "Ruslan"
age = 44

print(f"My name is {name} and my age is {age}")

# +
# 9

words = ["cat", "window", "defenestrate"]
for word in words:
    print(word, len(word))

# +
# 10

a_num, b_num = 0, 1
while a_num < 15:
    print(a_num, end=", ")
    a_num, b_num = b_num, a_num + b_num
# -

# ## 3.8.4
#
# 1. Done;
# 2. Done;
# 3. Done.

"""Python basics."""

# ### MAIN PYTHON MANIPULATIONS

# ## Core number operations

# +
import sys

2 + 2
# -

3 - 5

8 / 5  # division always returns a floating point number

17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

# 5**2  # 5 squared

# ## Strings basics
#
# **\\** can be used to escape quotes

# ```python
# "python strings"  # single quotes
# ```

# ```python
# "doesn't"  # use \' to escape the single quote...
# ```

# ```python
# "doesn't"  # double quotes
# ```

# The print() function produces a more readable output, by omitting \
# the enclosing quotes and by printing escaped and special characters

# print('"Isn\'t," they said.')

# If you don't want characters prefaced by “\” to be interpreted as \
# special characters, you can use raw strings by adding an r before the \
# first quote

print("C:\\some\name")  # here \n means newline!

print(r"C:\some\name")  # note the r before the quote

# Concatenation and Repetition Strings can \
# be concatenated (glued together) with the + operator, \
# and repeated with *. To remember this, it is simple. + \
# operator adds, and * operator multiplies(see example)

print("a" + "b")
print("t" * 5)
print("no" * 3 + "dip")

# Two or more string literals (i.e. the ones enclosed between quotes) \
# next to each other are automatically concatenated.

# ```python
# "nil" "abh"
# ```

# Indexing Strings can be indexed
# (subscripted), with the first character having \
# index 0. There is no separate character type;
# a character is simply a string of size one.

word = "Python"
word[0]  # character in position 0

# Indices may also be negative numbers, to start counting from the
# right:

word[-4]

# Slicing In addition to indexing, slicing is also
# supported. While indexing is used to obtain \
# individual characters, slicing allows you to
# obtain substring:

word[0:2]  # characters from position 0 (included) to 2 (excluded)

# Python strings cannot be changed — they are immutable. Therefore, \
# assigning to an indexed position in the string results in an error So, if \
# you try to assign a new value in the string, it will give you an error.

# +
# word[2] = "l"
# -

# The built-in function len() returns the length of a string:
len(word)

# ### OTHER PYTHON-RELATED AFFAIRS

# Syntax of Code in Python Statement Instructions written in the \
# source code for execution are called statements.
# There are different types of statements in Python, \
# like Assignment statement, Conditional \
# statement, Looping statements, etc. These all help the user \
# to get the required output.
# For example, n = 20 is an assignment statement.
#
# Terminating a Statement In Python, the end of the line means \
# the end of the statement.
#
# Semicolon Can Optionally Terminate a Statement. Sometimes it can \
# be used to put multiple statements on a single line.\
# e.g. \
# Multiple Statements in one line, Declared using semicolons (;):

lag = 2
ropes = 3
pole = 4

# Variables and Assignment One of the most powerful features of a programming \
# language is the ability to manipulate variables. A variable is a \
# name that refers to a value. Please note that the variable only refers to the \
# value, to which it is assigned. It doesn't become equal to that value. The \
# moment it is assigned to another value, the old assignment becomes null and
# void automatically.
#
# Variable names can be of any length and can contain both alphabets \
# and numbers. They can be of uppercase or lowercase, but the same \
# name in different cases are different variables, as you must remember, \
# Python is case sensitive language
#
# Here’s a simple way to check which of the given variable names are invalid in Python:
#
# Summary of rules:
#
# * Must start with a letter or underscore (_).
# * Can contain letters, numbers, and underscores.
# * Cannot start with a number.
# * Cannot use Python keywords (reserved words).
# * Cannot contain spaces or special characters (*, @, %, etc.).
#

# ```python
# # Fibonacci series: # the sum of two elements defines the next
# a = 0
# b = 1
# while a < 10:
#     print(a)
#     a, b = b, a + b
# ```

# **Arguments** are anything that we pass in the function. \
# Like, string or variable are the arguments. \
# In Python, arguments are values passed to a function. \
# When the number of arguments is unknown, we use *args, \
# which allows passing multiple values as a tuple.
#
# **Keyword Arguments** in Python are the argument where you provide a name
# to the variable as you pass it into the function, like this: (key=value format), \
# making the function call more readable and flexible.
#
# Example with print():

print([3, 5], sep=" ", end="\n", file=sys.stdout, flush=False)

# **String formatting**

# ```Python
# a = 5
# b = 6
# ab = 5 * 6
# print(f"when {a} is multiplied by {b}, the result is {ab}".format(a, b, ab))
# ```

# **Troubleshooting** is essential when code doesn't work as expected. \
# Python provides informative error messages to help identify issues.
#
# **Major Types of Errors Which Occur Most Frequently:**
# - Syntax Errors – occur when when the correct Python Syntax \
# is not used (e.g., missing colons or parentheses).
# - Runtime Errors – take a place during program execution, frequently \
# in wake of invalid operations (e.g., an attempt to divide the number by zero or using \
# a variable before it was defined).
# - Semantic (Logic) Errors – occur in cases when the meaning of the program (its semantics) \
# is wrong, producing unexpected results.

# ## 3.8 Answers to the exercises
#
# ### 3.8.1
#
# 1.
# - Intelligent Code Assistance – Features like code completion, syntax highlighting, and debugging streamline development.
# - Variable Explorer – Provides an intuitive way to track and inspect data within the workspace.
# - IPython Console – Enables interactive execution and real-time code testing.
# - Integrated Debugger – Helps in efficiently identifying and fixing errors within the code.
# - Pre-installed Scientific Libraries – Comes with essential tools like NumPy, Pandas, and Matplotlib, reducing setup time.
# 2.
# - Addition (+) → a + b → Adds two numbers.
# - Subtraction (-) → a - b → Subtracts the second number from the first.
# - Multiplication (*) → a * b → Multiplies two numbers.
# - Division (/) → a / b → Performs division and always returns a float.
# - Floor Division (//) → a // b → Divides and returns the largest integer less than or equal to the result (rounds down).
# 3.
# - Multiplication (*) → a * b → Multiplies two numbers (e.g., 3 * 4 = 12).
# - Exponentiation ()** → a ** b → Raises the first number to the power of the second (e.g., 3 ** 4 = 81).
# 4. In Python, a statement is a single line of code that executes a specific action, defining the logic,        operations, or control flow within a program.
# 5. A variable in Python is a named reference that stores a value. The = operator is used to assign a value to a variable.
# 6. No, a variable cannot be named "import" in Python because "import" is a reserved keyword used for importing modules.
# 7. No, the statement is incorrect. Python is case-sensitive, meaning "math", "Math", and "MATH" are treated as distinct identifiers.
# 8. Use a comma to separate values, for instance:
#
#     ```python
#     flowers = ["chamomile", "rose", "tulip"]
#     x, y, z = flowers
#     ```
# 9. A syntax error occurs when the Python interpreter fails to understand the code due to structural issues, such as missing colons, parentheses, or incorrect indentation. In contrast, a semantic error happens when the code executes without crashing but produces incorrect or unintended results due to logical mistakes.
# 10.
# - The default separator (sep) in Python is a space (' '), which separates multiple arguments in the print() function.
# - The default end character (end) is a newline ('\n'), meaning the output moves to the next line after printing.
#
# ### 3.8.2
#
# 1. False;
# 2. True;
# 3. False;
# 4. False;
# 5. False;
# 6. False;
# 7. False;
# 8. True;
# 9. False;
# 10. True.

# ### 3.8.3

# +
# 1

first_name = "Ruslan"
last_name = "Kazmiryk"
print(first_name, last_name)
# -

# # 2
#
# length = 23
# height = 8
# area = length * height
# area

# +
# 3

square_32 = 32**2
cube_27 = 27**3

# +
# 4

# Assign values to variables
a_num = 3
b_num = 4

# Calculate both sides of the equation

# Left-hand side: (a + b)^2
lhs = (a_num + b_num) ** 2

# Right-hand side: a^2 + b^2 + 2ab
rhs = a_num**2 + b_num**2 + 2 * a_num * b_num

# Print results
print("LHS:", lhs)
print("RHS:", rhs)

# Verify if both sides are equal
print("Equation holds:", lhs == rhs)

# +
# 5

len("Ruslan")

# +
# 6

print("**********")
print("*        *")
print("*        *")
print("*        *")
print("**********")

# +
# 7

print("PPPPPP")
print("P     P")
print("P     P")
print("PPPPPP")
print("P")
print("P")
print("P")

# +
# 8

name = "Ruslan"
age = 44

print(f"My name is {name} and my age is {age}")

# +
# 9

words = ["cat", "window", "defenestrate"]
for word in words:
    print(word, len(word))

# +
# 10

a_num, b_num = 0, 1
while a_num < 15:
    print(a_num, end=", ")
    a_num, b_num = b_num, a_num + b_num
# -

# ## 3.8.4
#
# 1. Done;
# 2. Done;
# 3. Done.
