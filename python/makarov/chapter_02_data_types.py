"""Data types in Python."""

# ### Working with numbers

int_var = 25  # integer (int)
float_var = 2.5  # floating point number (float)
complex_number = 3 + 25j  # complex number (complex)

# exponential entry, 2 times 10 to the power of 3
exponential_number = 2e3
print(exponential_number)
print(type(exponential_number))

# Arithmetic operations

# addition, subtraction, multiplication, division, raising to a degree
example_digit = 2
example_digit_2 = 4
print(
    example_digit + example_digit_2,
    example_digit_2 - example_digit,
    example_digit * example_digit,
    example_digit_2 / example_digit,
    example_digit**3,
)

example_digit = 7
example_digit_2 = 2

# whole part of the division
print(example_digit_2 // example_digit)

# remainder of the division
print(example_digit_2 % example_digit)
# -

# Comparison operators

# greater than, less than, greater than or equal to, and less than or equal to
example_digit = 2
example_digit_2 = 4
print(
    example_digit_2 > example_digit,
    example_digit_2 < example_digit,
    example_digit_2 >= example_digit,
    example_digit_2 <= example_digit,
)

# +
# the usual equality operator
example_digit = 2
example_digit_2 = 4
print(example_digit == example_digit_2)

# not equal operator
print(example_digit != example_digit_2)
# -

# Logical operations

# +
# logical AND, both operations must be true
example_digit = 2
example_digit_2 = 4
print(example_digit_2 > example_digit and example_digit_2 != example_digit)

# logical OR, at least one of the operations must be true
print(example_digit_2 < example_digit or example_digit == example_digit_2)

# logical NOT, negation of the operation
print(example_digit != example_digit_2)
# -

# Converting numbers to another number system

# +
# create a decimal number
decimal_num = 25

# convert to binary
bin_dec = bin(decimal_num)
print(bin_dec)

# convert back to decimal
print(int(bin_dec, 2))

# +
# create a decimal number
decimal_num = 25

# convert to octal
oct_d = oct(decimal_num)
print(oct_d)

# convert back to decimal
print(int(oct_d, 8))

# +
# convert to hexadecimal
decimal_num = 25
hex_d = hex(decimal_num)
print(hex_d)

# convert back to decimal
print(int(hex_d, 16))
# -

# ### String data

string_1 = "this string"
string_2 = "this string too"

multi_string = """We've all learned a little bit
Somehow and some other way,
♪ So, thank goodness for our upbringing ♪
It's not hard for us to shine."""

# Line length

# use the len() function to find the length of a string
len(multi_string)

# String merge

# +
# lets merge strings
first_sen_part, second_sen_part, third_sen_part = "Programming", "on", "Python"

first_sen_part + " " + second_sen_part + " " + third_sen_part
# -

# Character index in the string

# +
# first element of the multi_string
print(multi_string[0])

# now output the last element
print(multi_string[-1])
# -

# slicing

# select elements four through six
print(multi_string[3:6])

# +
# output all elements up to the second one
print(multi_string[:2])

# as well as all elements starting from the fourth
print(multi_string[3:])
# -

# Cycles in strings

# Cycles in strings
for i in "Python":
    print(i)

# Methods  .strip() и .split()

# +
# removing unwanted characters from the beginning and end of a string
print("***15 849 302*****".strip("*"))

# if no argument is specified, spaces at the edges of the string are removed
print(" 15 849 302 ".strip())
# -

# split the string into a list of words
print(multi_string.split())

# count the number of words in the text (the length of the list)
len(multi_string.split())

# Replace a character in a string

# +
# let's assume the data is in this format
data = "20,25"

# now replace ',' with '.'
data = data.replace(",", ".")

# and convert to a number
data_converter = float(data)
print(data_converter)
print(type(data_converter))
# -

# ### Logical values

# create a variable and write the logical value True into it
# (capitalization required)
boll_var = False
type(boll_var)

# +
# we'll write a little program that will show you
# what value is contained in the variable var

if boll_var:
    print("The value of the variable is true")
else:
    print("The value of the variable is false")


# output return always a boolean value False because var is set to False
