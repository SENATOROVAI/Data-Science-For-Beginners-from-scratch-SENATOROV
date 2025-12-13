"""Lists, tuples, and sets."""

# ### Lists

# Basics of working with lists

# +
# An empty list can be created using [] or the list() function.
# import the stemmer class and create an object

from nltk.stem import PorterStemmer

some_list_1: list[str] = []
some_list_2: list[str] = list()  # pylint: disable=R1734

print(some_list_1, some_list_2)
# -

# List elements can be numbers, strings, other lists,
# and dictionaries, among other things.
number_three = [3, "three", ["number", "three"], {"number": 3}]
number_three

# The length of the list is calculated using the len() function.
len(number_three)

# Index and list slice

# +
# the list has positive and negative indices
abc_list: list[str] = ["a", "b", "c", "d", "e"]

# let's use them to output the first and last elements
print(abc_list[0], abc_list[-1])

# +
# # when working with a nested list
salary_list: list[list[str | int]] = [
    ["Anna", 90000],
    ["Igor", 85000],
    ["Alex", 95000],
]

# First, we specify the index of the nested list,
# and then the index of the element in it.
salary_list[1][0]
# -

# The index can be found using the .index() method.
abc_list.index("c")

# The .index() method can also be applied to nested lists.
salary_list[0].index(90000)

# +
# Let's create a list with the days of the week.
days_list = ["Mn", "Tu", "Wd", "Th", "Fr", "St", "Sn"]

# and we will remove the second through fifth elements inclusive
days_list[1:5]
# -

# output every second element in the slice from the first to the fifth
days_list[:5:2]

# Let's check if "Mn" is in the list.
"Mn" in days_list

# if "Tu" is in the list
if "Tu" in days_list:

    # display a message
    print("There is such a word.")

# Adding, replacing, and deleting list items

# create a list
weekdays: list[str] = ["Monday", "Tuesday"]

# adding a new element with the .append() method
weekdays.append("Thursday")
weekdays

# add an element to a specific place in the list using the desired index of
# that element
weekdays.insert(2, "Wednesday")
weekdays

# change the fourth element in the list
weekdays[3] = "Friday"
weekdays

# remove the element by its value
weekdays.remove("Friday")
weekdays

# Remove an element by its index using the keyword del
del weekdays[2]
weekdays

# Let's do the same thing using the .pop() method.
# This method outputs the element being deleted.
weekdays.pop(1)

# Let's see what's left on our list.
weekdays

# Сложение списков

# +
# You can combine two lists using the .extend() method.
more_weekdays: list[str] = ["Tuesday", "Wednesday", "Thursday", "Friday"]

weekdays.extend(more_weekdays)
weekdays

# +
weekend = ["Saturday", "Sunday"]

# or simply by combining two lists
print(weekdays + weekend)
# -

# Sometimes it is useful to "multiply" list items.
["Monday"] * 2

# such "works" can also be stacked
["Monday"] * 2 + ["Tuesday"] * 2

# Unpacking lists

# there is a list
week: list[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# By specifying the index of the element, it can be written to a variable.
monday = week[0]
monday

# +
# the slice can be placed in several variables
monday, tuesday, wednesday = week[:3]

# It is important that the number of cut elements is equal to the number of   # variables.
monday, tuesday, wednesday
# -

# you can select the first element and place the rest
# in a variable with an asterisk
monday, *rest = week
monday

# You can also do this, for example, with the first and last elements.
monday, *days, sunday = week
monday, sunday

# Let's see what elements remain in the variable with an asterisk.
days

# Sorting lists

# let's take a list of numbers
nums: list[int] = [25, 10, 30, 20, 5, 15]

# lets sort the list using the sorted() function
sorted(nums)

# the original list has not changed
nums

# let's save the sorted list to a new variable
sorted_nums = sorted(nums)
sorted_nums

# The .sort() method saves the result but does not display it immediately.
# reverse = True sets descending order
nums.sort(reverse=True)

# let's show the result
nums

# +
# The .reverse() method reverses the order, saves the result, but does not    # print it.
nums.reverse()

# it also needs to be displayed separately
nums
# -

# The reversed() function returns an iterator.
reversed(nums)

# You can display the result using the list() function.
list(reversed(nums))

# the result is not saved in
nums

# Преобразование списка в строку

# a list of string elements is given
str_list: list[str] = ["P", "y", "t", "h", "o", "n"]

# Using the .join() method, you can join all elements.
joined_str = "".join(str_list)
joined_str

# If nothing is specified in quotation marks,
# the elements will simply be joined,
# but any other element can be specified.
joined_str_ = "_".join(str_list)
joined_str_

# List arithmetic

# there is a list of numbers
nums_: list[int] = [3, 2, 1, 4, 5, 12, 3, 3, 7, 9, 11, 15]

# Using the .count() method,
# we can count the frequency of an element's
# occurrence in a list.
nums_.count(3)

# In addition, we can find the minimum and
# maximum values and the sum of the elements.
print(min(nums_), max(nums_), sum(nums_))

# List comprehension

# there is a list of names
# Let's leave names beginning with the letter "A"
names: list[str] = [
    "Artem",
    "Anton",
    "Alexandra",
    "Boris",
    "Viktor",
    "Kenneth",
]

# +
# First, let's solve this problem using a for loop.

# Let's create an empty list.
a_names: list[str] = []

# Let's go through the original list in a for loop.
for name in names:

    # Using the .startswith() method, we will
    # check whether the word begins with "A".
    if name.startswith("A"):

        # if yes, add to the new list
        a_names.append(name)

# print the result
a_names
# -

# The same task can be solved using list comprehension.
# Essentially, we are writing:
# "What to do while there is an element in the
# list, under what condition."
a_names = [name for name in names if name.startswith("A")]
a_names

# Let's convert all letters to lowercase; no condition is needed here.
lower_names = [name.lower() for name in names]
lower_names

# the if-else condition is slightly different
# leave the name if it is not Victor, if it is Victor, replace it with Vadim
replace_name = [name if name != "Viktor" else "Vadim" for name in names]
replace_name

# +
# In a class on natural language processing using list comprehension,
# we applied Porter's stemmer to a list of words.
lemmatized: list[str] = [
    "paris",
    "visited",
    "lot",
    "museum",
    "first",
    "went",
    "louvre",
    "largest",
    "art",
    "museum",
    "world",
    "always",
    "interested",
    "art",
    "spent",
    "many",
    "hour",
    "museum",
    "enormous",
    "week",
    "would",
    "enough",
]


porter = PorterStemmer()

# apply the stemmer to element s while there are elements s in the lemmatized # list
stemmed_p = [porter.stem(s) for s in lemmatized]
print(stemmed_p)
# -

# ### Tuples

# Basics of working with tuples

# An empty tuple can be created using empty parentheses ()
# or the tuple() function.
tuple_1: tuple[()] = ()
tuple_2: tuple[str, ...] = tuple()
print(tuple_1, tuple_2)

# The elements in the array are ordered, which means there is an index.
letters = ("a", "b", "c")
letters[0]

# +
# but you cannot change an element as we did in the list
# letters[0] = 'd' --> Error
# -

# To change an element, you first need to convert the tuple to a list.
letters_list = list(letters)
letters_list[0] = "d"
letters_list

# A single-element array can be created using a comma.
letter_a: tuple[str] = ("a",)
type(letter_a)

# if you don't specify the comma, you will get a string
let_a = "a"
type(let_a)

# `enumerate()` function

# +
companies: list[str] = ["Microsoft", "Apple", "Tesla"]

# if you store the result of the enumerate() function in a single variable,
for company in enumerate(companies):

    # then we will get tuples
    print(company, type(company))
# -

# Printing `dictionary` elements

shopping_dict: dict[str, int] = {
    "cucumbers": 2,
    "tomatoes": 3,
    "onion": 1,
    "potatoes": 2,
}

# The same applies to the dictionary and the .items() method.
for item in shopping_dict.items():
    print(item)

# Unpacking tuples

# Like a list, a tuple also can be unpacked into several variables.
a_var, b_var, c_var = ("a", "b_var", "c_var")
print(a_var)

# +
companies = ["Microsoft", "Apple", "Tesla"]

# We already know how to unpack into two variables
# using the enumerate() function.
for index, company_name in enumerate(companies):
    print(index, company_name)

# +
shopping_dict = {
    "cucumbers": 2,
    "tomatoes": 3,
    "onion": 1,
    "potatoes": 2,
}

# the same with dictionary keys and values

for key, value in shopping_dict.items():
    print(key, value)
# -

# `zip()` function

# +
# if there are two or more lists
names = ["Artyom", "Anton", "Alexander", "Boris", "Viktor", "Genadiy"]
income: list[int] = [97000, 110000, 95000, 84000, 140000, 120000]

# The zip() function will combine the first elements of the lists,
# the second elements of the lists, and so on.
zip(names, income)
# -

# to output the result, you need to pass the zip object to the list() function
# the output will be a list of tuples
list(zip(names, income))

# ### Sets

# Creating a `set()`

# +
# The empty set is defined using the set() function.
set_1: set[str] = set()

# A non-empty set is defined using the set() function and a list of elements.
set_2: set[str] = set("abcde")  # pylint: disable=W0130

# or by listing elements in curly brackets {}
set_3: set[str] = {"a", "b", "c", "c"}  # pylint: disable=W0130

# the set contains only unique elements, so duplicates are removed
print(set_1, set_2, set_3)
# -

# Adding and removing items

# Let's assume that we want to create a set of vowels in the English language.
vowels: set[str] = {"a", "e", "i", "o"}

# add one letter "ya" using the .add() method
vowels.add("ya")
vowels

# Let's add two letters "i" and "yoo" using the .update() method.
vowels.update(["i", "yoo"])
vowels

# if we accidentally add a consonant letter
# we can remove it using the .remove() method
vowels.add("ya")
vowels.remove("ya")
vowels

# Set theory in Python

# Two sets are equal if they contain the same elements,
# regardless of the order of the elements.
{"a", "b", "c"} == {"c", "b", "a"}

# Let's calculate the power of the set using the len() function.
print(len({"a", "b", "c"}))

# Let's check whether the element is contained in the set.
print("a" in {"a", "b", "c"})

# the reverse operation is also possible
print("a" not in {"a", "b", "c"})

# +
# Let's check whether A is a subset of B.
set_a: set[str] = {"a", "b", "c"}
set_b: set[str] = {"a", "b", "c", "d", "e", "f"}

set_a.issubset(set_b)
# -

# Let's check whether B is a superset of A.
set_b.issuperset(set_a)

# Participants in natural language processing
# (nlp) and computer vision (cv)   teams are listed.
nlp: set[str] = {"Anna", "Nikolai", "Pavel", "Oksana"}
cv: set[str] = {"Nikolai", "Yevgeniy", "Olga", "Oksana"}

# +
# find those who work either in nlp, or in cv, or in both teams

# you can use the .union() method
print(nlp.union(cv))

# or symbol |
print(nlp | cv)
# -

# find the intersection of sets, i.e., those who work in both NLP and CV
print(nlp.intersection(cv))
print(nlp & cv)

# Let's exclude those who work only in NLP,
# but not in CV or CV and NLP simultaneously.
print(nlp.difference(cv))
print(nlp - cv)

# Let's exclude those who work only in CV, but not in NLP, or in NLP and CV #
# simultaneously.
print(cv.difference(nlp))
print(cv - nlp)

# find those who work either in CV or NLP, but not in both fields at the same # time
print(nlp.symmetric_difference(cv))
print(nlp ^ cv)
