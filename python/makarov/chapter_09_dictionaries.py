"""Dictionaries in Python."""

# #### Creating a `dict()`

# +
# An empty dictionary can be created using {} or the dict() function.
# Import the Counter class.
from collections import Counter

# import the pprint() function from the pprint module
# it outputs some data structures better than the usual print()
from pprint import pprint

import numpy as np

dict_1: dict[str, str] = {}
dict_2: dict[str, str] = dict()  # pylint: disable=R1735
print(dict_1, dict_2)
# -

# the dictionary can be filled
# with keys and values right away
company: dict[str, str | int] = {
    "name": "Toyota",
    "founded": 1937,
    "founder": "Kiichiro Toyoda",
}
company

# A dictionary can be created from nested lists.
tickers: dict[str, str] = dict([["TYO", "Toyota"], ["TSLA", "Tesla"], ["F", "Ford"]])
tickers

# +
# if you put the keys in a tuple
keys: tuple[str, ...] = ("k1", "k2", "k3")
# and set the value for all keys
value_global = 0

# then, using the .fromkeys() method, you can create a dictionary
# with these keys and a specified value for each of them
empty_values = dict.fromkeys(keys, value_global)
empty_values
# -

# #### Dictionary keys and values

# Types of dictionary elements

# +
# Let's give an example of what the
# dictionary values might be.

val_types: dict[str, int | str | bool | None | list[int] | object | float] = {
    "k1": 123,
    "k2": "string",
    "k3": np.nan,  # none type
    "k4": True,  # boolean type
    "k5": None,
    "k6": [1, 2, 3],
    "k7": np.array([1, 2, 3]),
    "k8": {1: "v1", 2: "v2", 3: "v3"},
}

val_types
# -

# ```.keys(), .values() и .items()``` methods

# Example of a dictionary representing a person
person: dict[str, str | int | list[str]] = {
    "first name": "Ivan",
    "last name": "Ivanov",
    "born": 1980,
    "dept": "IT",
}

# lets see the keys of the dictionary
print(person.keys())

# values of the dictionary
print(person.values())

# items of the dictionary
print(person.items())

# Using a for loop

# keys and values can be output in a for loop
for key, value_p in person.items():
    print(key, value_p)

# Key access and method `.get()`

# the value can be viewed by key
person["last name"]

# +
# if there is no such key,
# Python will return an error
# person['education'] --> Error
# -

# To prevent this from happening, you can use the .get() method.
# By default, if the key is missing, it returns the value None.
print(person.get("education"))

# if the key does exist,
# .get() will return the corresponding value
print(person.get("born"))

# Checking whether a key and value are in the dictionary

# let's check if there is such a key in the dictionary
print("born" in person)

# and now let's check if there is such a value in the dictionary
print(1980 in person.values())

# You can also check for the presence
# of both the key and the value at the  same time.
print(("born", 1980) in person.items())

# ### Basic operation with dictionary types in Python

# #### Adding and changing elements

# You can add an element by assigning a new value to the new key.
# Please note that in this case, the new value is a list.
person["languages"] = ["Python", "C++"]
person

# You can change an element by assigning a new value to the existing key.
# The value is still a list, but it consists of a single element.
person["languages"] = ["Python"]
person

# +
# Now let's create a new dictionary with new elements
new_elements: dict[str, str | int] = {"job": "programmer", "experience": 7}

# and add it to the existing dictionary using the .update() method
person.update(new_elements)
person
# -

# The .setdefault() method checks whether the key exists in the dictionary.
# If it does, the value will not change.
person.setdefault("last name", "Petrov")
person

# if not, a new key and corresponding value will be added
person.setdefault("f_languages", ["russian", "english"])
person

# #### Deleting elements

# The .pop() method removes an element by key and outputs the value being      # removed.
print(person.pop("dept"))

# and we will see the updated dictionary
person

# The keyword del also removes an element by key.
# The value being removed is not displayed.
del person["born"]

# The .popitem() method removes the last added element and outputs it.
person.popitem()

# The .clear() method removes
# all elements from the dictionary.
person.clear()
person

# The keyword del also allows
# you to delete the entire dictionary.
del person

# Let's make sure that this dictionary no longer exists.
person

# #### Sorting dictionaries

# let's take a simple dictionary to demonstrate sorting
dict_to_sort: dict[str, int] = {"k2": 30, "k1": 20, "k3": 10}

# sort the keys
sorted(dict_to_sort)

# and values
sorted(dict_to_sort.values())

# Let's look at the key:value pairs.
dict_to_sort.items()

# to sort them by key (index [0])
# we will use the .items() method and a lambda function
sorted(dict_to_sort.items(), key=lambda item: item[0])

# Sorting by value is performed in the same way, however,
# we pass the index [1] to the lambda function.
sorted(dict_to_sort.items(), key=lambda item: item[1])

# #### Copying dictionaries

# Let's create a source dictionary
# with the number of students in the first
# and second years of university.
original: dict[str, int] = {"First course": 174, "Second Course": 131}

# Copying with method `copy()`

# +
# Let's create a copy of this dictionary using the .copy() method.
new_1 = original.copy()

# add information about the third course to the new dictionary
new_1["Third course"] = 117

# the source dictionary has not changed
print(original)
print(new_1)
# -

# Copying with `=` operator but its not recommended

# +
# transfer the source dictionary to a new variable
new_2 = original

# delete elements of the new dictionary
new_2.clear()

# data has also been deleted from the source dictionary
print(original)
print(new_2)
# -

# ###  `dir()` function

# +
# The dir() function returns
# all methods of the object passed to it.
some_dict = {"k": 1}

# Special methods come first.
# They begin and end with the symbol '__'.
# Let's display the first 11 elements.
print(dir(some_dict)[:11])
# -

# when we pass our dictionary to the print() function,
print(some_dict)

# In fact, we apply the .__str__() method to the object.
some_dict.__str__()  # pylint: disable=C2801

# In most cases, we will be interested in methods without '__'.
methods = dir(some_dict)[-11:]
print(methods)

# ### Dict comprehension

# Let's create another simple dictionary
source_dict: dict[str, int] = {"k1": 2, "k2": 4, "k3": 6}

# Using dict comprehension, multiply each value by two
new_source_dict = {
    key: value * 2 for (key, value) in source_dict.items()
}  # pylint: disable=C0301

# make all key characters uppercase
new_source_dict = {key.upper(): value for (key, value) in source_dict.items()}

# +
# add a condition that the value must be
# greater than two AND less than six
new_dict_1 = {
    key: value
    for (key, value) in source_dict.items()
    if value > 2
    if value < 6  # pylint: disable=C0301
}

print(new_dict_1)

# +
new_dict: dict[str, int] = {}

# when solving the same problem in a for loop
for key, value in source_dict.items():

    # we would use logical AND
    if 2 < value < 6:

        # if the conditions are true, write the key and
        # value to a new dictionary
        new_dict[key] = value

new_dict
# -

# The if-else condition is placed at the very beginning
# of the dict comprehension scheme.
# We will replace the value with the word even if it is even,
# and odd if it is  odd.
even_odd_dict: dict[str, str] = {
    key: ("even" if value % 2 == 0 else "odd")
    for (key, value) in source_dict.items()  # pylint: disable=C0301
}

# dict comprehension can be used
# instead of the .fromkeys() method.
keys = ("k1", "k2", "k3")
# Pass the keys from the keys tuple to
# the dictionary and set the value of each to 0.
zeros_dict = {key: 0 for key in keys}

# ### Additional examples

# #### lambda-functions, and `map()`,  `zip()` functions

# Example with `list()`

# Lets take a list of  words
words: list[str] = ["apple", "banana", "fig", "blackberry"]

# Create a lambda function that calculates
# the length of the word passed to it.
# Using the map() function, apply the lambda function
# to each element of the words list
# and place the word lengths in a new list
# called length using the list() function.
length = list(map(len, words))
length

# Using the zip() function, we will concatenate
# both lists element by element
# and convert them into a dictionary.
from_zip_dict = dict(zip(words, length))
print(from_zip_dict)

# The same can be done using the zip() function
# and list comprehension.
zip_length_dict = dict(zip(words, [len(word) for word in words]))
print(zip_length_dict)

# Example with `dictionary()`

# let's take a dictionary with people's height in feet
height_feet: dict[str, float] = {
    "Alex": 6.1,
    "Jerry": 5.4,
    "Ben": 5.8,
}

# To convert feet to meters, let's create a lambda
# function lambda m: m * 0.3048
# Apply this function to the dictionary
# values using the map() function
# Convert to a list
metres = list(map(lambda m: m * 0.3048, height_feet.values()))
metres

# Using the zip() function, we will connect the keys
# of the source dictionary with the elements of the list metres.
dict(zip(height_feet.keys(), np.round(metres, 2)))

# The same can be done using dict comprehensions.
# All in one line.
# We simply convert the dictionary values to meters.
students_heights_dict = {
    key: np.round(value * 0.3048, 2) for (key, value) in height_feet.items()
}
print(students_heights_dict)

# #### Nested dictionaries

# let's take a dictionary with employee IDs as keys
employees: dict[str, dict[str, str | int | float]] = {
    "id1": {
        "first name": "Alexander",
        "last name": "Ivanov",
        "age": 30,
        "job": "Programmer",
    },
    "id2": {
        "first name": "Olga",
        "last name": "Petrova",
        "age": 35,
        "job": "ML-engineer",
    },
}

# and values - nested dictionaries with information about them
for value_e in employees.values():
    print(value_e)

# ##### Basics operations

# To retrieve the value of an element in a nested dictionary,
# we will use a double key.
print(employees["id1"]["age"])

# +
# add information about the new employee
employees["id3"] = {
    "first name": "Darya",
    "last name": "Nekrasova",
    "age": 27,
    "job": "web-designer",
}

# and display the updated dictionary using the pprint() function
pprint(employees)
# -

# You can also change the value of a nested dictionary using a double key.
employees["id3"]["age"] = 26
pprint(employees)

# #####  `for` loops

# +
# change the data type in the age information from int to float

# To do this, we will first go through the nested dictionaries,
# i.e., the values of info in the external dictionary employees.
for info in employees.values():

    # then by keys and values of the nested dictionary info
    for key_info, value_info in info.items():

        # if the key matches the word 'age'
        if key_info == "age":

            # convert the value to float type
            info[key_info] = float(value_info)

pprint(employees)
# -

# ##### Nested dictionaries and dict comprehension
#

# convert back from float to int, but now using dict comprehension
# first, let's just print the employees dictionary without any changes
pprint({id: info for id, info in employees.items()})

# and then replace the value of the outer dictionary info
# (i.e., the nested dictionary)
# with another dict comprehension with an if-else condition
pprint(
    {
        id: {
            key: (int(value_i) if key == "age" else value_i)
            for key, value_i in info.items()
        }
        for id, info in employees.items()
    }
)

# #### Word frequency in the text

# lets take a text corpus
corpus = (
    "When we were in Paris we visited a lot of museums. "
    "We first went to the Louvre, the largest art museum in the world."
    "I have always been interested in art so I spent many hours there."
    "The museum is enormous, so a week there would not be enough."
)

# ##### Preliminary text processing

# let's split into words
words = corpus.split()
print(words)

# Using list comprehension, we will remove periods and commas
# and convert all words to lowercase.
words = [word.strip(".").strip(",").lower() for word in words]
print(words)

# ##### Method 1. If-else condition

# +
# Let's create an empty dictionary for the bag of words bow.
bow_1: dict[str, int] = {}

# Let's go through the words in the text
for word in words:

    # if we encounter a word that is already in the dictionary
    if word in bow_1:

        # increase its value (frequency) by 1
        bow_1[word] = bow_1[word] + 1

    # otherwise, if the word appears for the first time
    else:

        # set its value to 1
        bow_1[word] = 1

# sort the dictionary by meaning in descending order (reverse = True)
# and display the six most frequent words
print(sorted(bow_1.items(), key=lambda item: item[1], reverse=True)[:6])
# -

# ##### Method 2. The .get() method

# +
bow_2: dict[str, int] = {}

# Let's go through the for loop again by words
for word in words:

    # if the word is not yet in the dictionary, .get() will return the value 0,
    # to which we will add one
    # if the word exists, the .get() method will return the existing value,
    # for example, 2 or 3,
    # and we will also increase the counter by 1
    bow_2[word] = bow_2.get(word, 0) + 1

# let's list the most popular words
print(sorted(bow_2.items(), key=lambda item: item[1], reverse=True)[:6])
# -

# ##### Method 3. The collections module

# +
# create an object of this class, passing it a list of words
bow_3 = Counter(words)

# Let's extract the six most common words using the .most_common method.
bow_3.most_common(6)
# -

# ### Additional materials

# #### Mutable and immutable data types

# Immutable data type

# +
# let's create a string object
string = "Python"

# let's look at identity, type, and value
# the id() function outputs the address of an object in the computer's memory
print(id(string), type(string), string)

# +
# let's try to change this object
string = string + " is cool"

# Let's look at the identity, type, and value
print(id(string), type(string), string)
# -

# Mutable data type

# +
# creating the list again
lst: list[int] = [1, 2, 3]

# Let's look at the identity, type, and value
print(id(lst), type(lst), lst)

# +
# add an item to the list
lst.append(4)

# display the identity, type, and value again
print(id(lst), type(lst), lst)
# -

# Copying objects

# +
# let's create the string again
string = "Python"

# # copy via assignment
string2 = string

# changing the copy
string2 = string2 + " is cool"

# let's see the result
print(string, string2)
# -

# The == operator compares values.
# The is operator compares identities.
print(string == string2, string is string2)

# +
# let's create a list again
lst = [1, 2, 3]

# Copy it to a new variable through assignment
lst2 = lst

# add a new item to the copied list
lst2.append(4)

# let's display the original list and a copy
print(lst, lst2)
# -

# let's make sure we're talking about the same thing
print(lst == lst2, lst is lst2)

# +
# Let's create the list again
lst = [1, 2, 3]

# # copy using the .copy() method
lst2 = lst.copy()

# add a new item to the copied list
lst2.append(4)

# let's display the original list and a copy
print(lst, lst2)

# +
# now let's make the values of the lists the same
lst.append(4)

# and make sure that these are still different objects
print(lst, lst2, lst == lst2, lst is lst2)
