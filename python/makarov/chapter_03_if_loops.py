"""Examples of using conditions (if/elif/else) and loops in Python."""

# ## === CONDITIONS (IF / ELIF / ELSE) ===

# +
import numpy as np

# === CONDITIONS (IF / ELIF / ELSE) ===


# Example 1. Classification of a number by magnitude
number_example = 42

if number_example < 10:
    print("Small")
elif number_example < 100:
    print("Medium")
else:
    print("Large")

# +
# request a number from the user


user_input = input("Enter a number: ")

# convert to int
user_number = int(user_input)

# classify the number
if user_number < 10:
    print("Small")
elif user_number < 100:
    print("Medium")
else:
    print("Large")
# -

# ## Nested decisions

# +
# Example 3. Nested conditions
entered_text = input("Enter a number: ")

if len(entered_text) != 0:

    entered_number = int(entered_text)

    if entered_number < 10:
        print("Small")
    elif entered_number < 100:
        print("Medium")
    else:
        print("Large")

else:
    print("Empty input")
# -

# Example 4. Logical operators and / or
#

# +
check_number = 42


if 10 < check_number < 100:

    print("Medium")


else:
    print("Small or Large")

# +
another_number = 2

if another_number < 10 or another_number > 100:

    print("Small or Large")

else:
    print("Medium")
# -

# Example 5. Checking occurrences with in / not in

# +
sentence = "To be, or not to be, that is the question"
target_word = "question"

if target_word in sentence:
    print("Word found")

# +
numbers = [2, 3, 4, 6, 7]
target_number = 5

if target_number not in numbers:
    print("That number is not on the list")
# -

fruits = {"apple": 3, "tomato": 6, "carrot": 2}

if "apple" in fruits:
    print("were found apples")

if 6 in fruits.values():
    print("Got it")

# ### Cycles in Python

# #### For loop

# ##### Basic operations

# +
numbers = [1, 2, 3]

for number in numbers:
    print(number)
# -

# let's create a dictionary whose values will be lists of two elements
fruits_info = {"apple": [3, "kg"], "tomato": [6, "pcs"], "carrot": [2, "kg"]}

# and then create two container variables and apply the .items() method.
for fruit_name, fruit_data in fruits_info.items():
    print(fruit_name, fruit_data)

# Let's take only one variable and apply the .values() method
for fruit_data in fruits_info.values():
    # value is a list, output its first element with индексом [0]
    print(fruit_data[0])

# +
# create an array and put it into the number_array variable
number_array = np.array([1, 2, 3])

# Let's go through it with a for loop
for number in number_array:
    print(number)
# -

# suppose we have the following customer database
clients = {
    1: {"name": "Anna", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Ilya", "age": 18, "sex": "female", "revenue": 8000},
}

for client_id, client_info in clients.items():

    # output the client id
    print(f"Client ID:  {client_id}")

    # on the second loop we take information about this client (this is also a dictionary)
    for field, value in client_info.items():

        # and output each key (field name) and value (the information itself)
        print(f"{field}:  {value}")

    # we will add an empty line after we output the information about one client.
    print()

# ##### Function range()

# Let's create a sequence from 0 to 4.
for i in range(5):
    print(i)

for number in range(1, 6):
    print(number)

for number in range(0, 6, 2):
    print(number)

# Exercise 6 enumerate()

# +
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

sales = [47, 75, 79, 94, 123, 209, 233, 214, 197, 130, 87, 55]

length = len(months)

# setting the sequence via range(len()),
for index in range(length):
    print(months[index], sales[index])
# -

# Sequence in reverse order

# **Method 1**. Function reversed()

# +
# lets create a list
my_list = [0, 1, 2, 3, 4]

# pass it to the reversed() function and
# output each of the items in the list using the for loop
for element in reversed(my_list):
    print(element)
# -

for element in reversed(range(5)):
    print(element)

# **Method 2**. Specify $-1$ as a step parameter

# the first parameter is the final element of the list,
# and the second parameter is the initial element of the list
for element in range(4, 0, -1):
    print(element)

# to output 0, the second parameter should be -1
for element in range(4, -1, -1):
    print(element)

# **See Method 3**. Function sorted()

# +
# lets create a sequence from 0 to 4
range_values = range(5)

# sort it in descending order
sorted_desc = sorted(range_values, reverse=True)

# print elements of the sorted sequence
for element in sorted_desc:
    print(element)
# -

# ##### Function enumerate()

# +
# let's have a list with the days of the week
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# print index and the elements of the list (day)
for index, day in enumerate(days):
    print(index, day)
# -

# #### While loop

# +
# set the initial value of the counter
counter = 0

# while the count is less than three
while counter < 3:

    # in each cycle we will output its current value
    print(f"The current value of the counter:  {counter}")

    # inside the loop, do not forget to "increment" the counter
    counter = counter + 1

    # and print the new value
    print(f"New counter value:     {counter}")

    # add an empty string
    print()

# +
# the same code can be simplified using the += operator
counter_2 = 0

while counter_2 < 3:
    print(counter_2)
    #  the += operator immediately increments and assigns a new value
    counter_2 += 1
# -

# #### Break, continue

# Operator break

# +
clients_data = {
    1: {"name": "Anna", "age": 24, "sex": "male", "revenue": 12000},
    2: {"name": "Ilya", "age": 18, "sex": "female", "revenue": 8000},
}

# loop through the keys and values of the dictionary
for client_id, client_info in clients_data.items():

    # and print them
    print(client_id, client_info)

    # however already after the first execution of the loop, we will interrupt
    break

# +
counter_3 = 6

# execute the loop until x is zero
while counter_3 != 0:

    # output the current counter value
    print(counter_3)

    # and reduce (!) it by 1
    counter_3 -= 1

    # if the counter value becomes equal to 3, break the loop
    if counter_3 == 3:
        break
# -

# Operator continue

# +
# output all even numbers in the range from 1 to 10 inclusive.

for number in range(1, 11):
    if number % 2 != 0:
        continue
    print(number)
# -

# #### f strings

# +
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

Monday = days[0]
Monday
# -

print(f"{Monday} - hard day")

# ### Answers to the questions for the session

# **Question**. Can I use a while loop with the range() function?

# +
# You can use a while loop with the range() function, but this solution is not optimal


counter_4 = 1

while counter_4 in range(1, 11):  # while  counter is between 1 and 10
    print("Counter value ", counter_4)  # print its value and
    counter_4 += 1  # increment the counter by 1
# -

# better code
for number in range(1, 11):
    print(f"Counter value  {number}")

# **Question**. Is it possible to do without the continue operator in the example given in the lesson?

for number in range(1, 11):
    # if the number is even, output it
    if number % 2 == 0:
        print(number)
