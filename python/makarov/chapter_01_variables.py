"""Variables and basic operations with them."""

# +
# defining a variable
my_variable = "Hello, World!"

# printing the variable
print(my_variable)
# -

# In Python, you can assign different values to several variables at once
x_axis, y_axis, z_axis = 1, 2, 3
print(x_axis, y_axis, z_axis)

#  as well as assign the same value to multiple variables
x_axis = y_axis = z_axis = 0
print(x_axis, y_axis, z_axis)

# +
#  each item in the list can be "unpacked" into variables

products_list = ["fruit", "vegetables", "dairy"]
category_1, category_2, category_3 = products_list

print(category_1, category_2, category_3)
# -

# ## Automatic data type detection (dynamic typing)

customer_name = "John Doe"  # string variable
loan_amount = 25000.75  # float variable
years = 5  # integer variable

# ## How to find out the type of a variable in Python?

# recognize the type of variables from the previous example
print(type(customer_name))
print(type(loan_amount))
print(type(years))

# ## Data type assignment and conversion

string_var = "25"
int_var = int(42)
float_var = float(3.14)

print(type(string_var), type(int_var), type(float_var))

# Changing the data type of a variable
changing_variable_type = int(string_var)  # converting string to integer
print(type(changing_variable_type), changing_variable_type)  # now it's an integer

# ## Variable naming
#
#
# ### Allowed variable names

# ```variable = "Just a variable"
# _variable = "Just a variable"
# variable_ = "Just a variable"
# my_variable = "Just a variable"
# My_variable_123 = "Just a variable"```

# ```
# # The name of a variable consists of several words!
# camelCaseVariable = "camelCaseVariable"  # all words except the first begin with a capital letter and are capitalized and spelled consecutively
# snake_case_variable = "snake_case_variable"  # all words are in lowercase and separated by underscores
# PascalCaseVariable = "PascalCaseVariable"  # all words begin with a capital letter and are spelled consecutively
#
# ```

# ### Invalid variable names

# ```
# # You can't do that.
# 2variable = 'Invalid variable name' # starts with a digit
# my-variable = 'Invalid variable name' # contains a hyphen
# my variable = 'Invalid variable name' # contains a space
# my.variable = 'Invalid variable name' # contains a dot
#
# ```

# ##  Question. How can I convert a list of numbers so that each element of the list becomes a separate string?

# +
# lets take a simple list

list_ = [1, 2, 3]

# +
# you cannot use only the str() function to convert a list to a string
# because it will convert the entire list to a single string

str(list_)
# -

# option 1: declare a new list and put string values into it in the for loop
string_list = []
for item in list_:
    string_list.append(str(item))
string_list

# # option 2: use list comprehension
string_list = [str(item) for item in list_]
string_list

# option 3: map() and list() functions
string_list = list(map(str, list_))
string_list
