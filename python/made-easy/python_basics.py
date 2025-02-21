"""Python basics."""

# ## Basic number operations

# +
import sys

2 + 2
# -

5 - 6

8 / 5  # division always returns a floating point number

17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5**2  # 5 squared

2**7  # 2 to the power of 7

width = 20  # = sign is used to assign a value to a variable

# ## Strings basics
#
# **\\** can be used to escape quotes

# ```python
# "python strings"  # single quotes
# ```

# ```python
# "doesn't"  # double quotes
# ```

# ```python
# "doesn't"  # use \' to escape the singlequote...
# ```

# The print() function produces a more readable output, by omitting \
# the enclosing quotes and by printing escaped and special characters

print('"Isn\'t," they said.')

# If you don't want characters prefaced by “\” to be interpreted as \
# special characters, you can use raw strings by adding an r before the \
# first quote

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
#

# +
# word[2] = "l"
# -

# The built-in function len() returns the length of a string:
len(word)

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
# Rules Recap:
#
# ✅ Must start with a letter or underscore (_).
#
# ✅ Can contain letters, numbers, and underscores.
#
# ❌ Cannot start with a number.
#
# ❌ Cannot use Python keywords (reserved words).
#
# ❌ Cannot contain spaces or special characters (*, @, %, etc.).
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
# **Keyword Arguments** in Python are arguments passed to a function with a name (key=value format), \
# making the function call more readable and flexible.
#
# Example with print():

print("Hello", "World", sep="-", end="!!!\n")

print([4, 64], sep=" ", end="\n", file=sys.stdout, flush=False)

# **String formatting**

# ```Python
# a = 5
# b = 6
# ab = 5 * 6
# print(f"when {a} is multiplied by {b}, the result is {ab}")
# ```

# **Troubleshooting** is essential when code doesn't work as expected. \
# Python provides detailed error messages to help identify issues.
#
# **Common Error Types:**
# - Syntax Errors – Occur when Python can't understand \
#   the code due to incorrect structure (e.g., missing colons or parentheses).
# - Runtime Errors – Happen while the program is running, often \
#   due to invalid operations (e.g., dividing by zero or using an undefined variable).
# - Semantic Errors – The code runs without crashing but produces incorrect results due to logic mistakes.

# ## 3.8 Exercise responses
#
# ### 3.8.1
#
# 1.
# - Code completion, syntax highlighting, and debugging
# - Variable Explorer to track data easily
# - IPython Console for interactive execution
# - Built-in Debugger for efficient error fixing
# - Pre-integrated scientific libraries (NumPy, Pandas, Matplotlib)
# 2.
# - Addition (+) → a + b
# - Subtraction (-) → a - b
# - Multiplication (*) → a * b
# - Division (/) → a / b (returns float)
# - Floor Division (//) → a // b (returns integer)
# 3.
# - * → Multiplication (3 * 4 = 12)
# - ** → Exponentiation (3 ** 4 = 81)
# 4. A statement in Python is a single line of code that performs an action. \
#    It defines logic, operations, and flow in a program.
# 5. A variable in Python is a name that stores a value. `=` is used to assigning a value to a variable.
# 6. No, we cannot name a variable "import" in Python because \
#    import is a reserved keyword used for importing modules.
# 7. No, the statement is incorrect. Python is case-sensitive, \
#    meaning "math", "Math", and "MATH" are treated as different identifiers.
# 8. Use comma, for example
#
#     ```python
#     fruits = ["apple", "banana", "cherry"]
#     x, y, z = fruits
#     ```
#
# 9.  A syntax error occurs when the Python interpreter cannot \
#     understand the code due to incorrect structure, such as missing colons, \
#     parentheses, or incorrect indentation. A semantic error, on the other hand, \
#     occurs when the code runs without crashing but produces an incorrect or unintended result due to a logical mistake.
# 10.
# - The default separator (sep) is a space (' '), which separates multiple arguments.
# - The default end (end) is a newline ('\n'), meaning the output moves to the next line after printing.
#
#
# ### 3.8.2
#
# 1. False
# 2. True
# 3. False
# 4. False
# 5. False
# 6. False
# 7. False
# 8. True
# 9. False
# 10. True
#
# ### 3.8.3

# +
# 1

first_name = "Maryia"
last_name = "Krauchanka"
print(first_name, last_name)

# +
# 2

length = 32
height = 8
area = length * height
area

# +
# 3

square_32 = 32**2
cube_27 = 27**3

# +
# 4

a_val = 5
b_val = 3

left_side = (a_val + b_val) ** 2
right_side = a_val**2 + b_val**2 + 2 * a_val * b_val

print(left_side == right_side)

# +
# 5

len("Maryia")

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

name = "Maryia"
age = 27

print(f"My name is {name} and my age is {age}")

# +
# 9

words = ["cat", "window", "defenestrate"]
for word in words:
    print(word, len(word))

# +
# 10


c_val, b_val = 0, 1
while c_val < 15:
    print(c_val, end=" , ")
    a_val, b_val = b_val, c_val + b_val
# -

# ## 3.8.4
#
# 1. Done
# 2. Done
# 3. Done
#
