"""Strings, tuples, lists."""

# #### str.islower()
#
# The islower() method in strings checks whether there are no uppercase letters in the string.
#
#
# #### str.capitalize()
#
# The capitalize() method returns a copy of the string with the first letter capitalized and the rest converted to lowercase.
#
#
# #### str.count(sub)
#
# The count(sub) method in strings returns the number of non-overlapping occurrences of the substring sub in the given string.
#
# #### str.endswith(suffix)
#
# Returns True if the string ends with the substring suffix, otherwise returns False. The suffix can also be a tuple of multiple suffixes.
#
# #### str.find(sub)
#
# Returns the index of the first occurrence of the substring sub. If not found, returns -1.
#
# #### str.index(sub)
#
# Returns the index of the first occurrence of the substring sub. Raises a ValueError if the substring is not found.
#
# #### str.isalnum()
#
# Returns True if all characters in the string are letters or digits and the string is not empty, otherwise returns False.
#
# #### str.isalpha()
#
# Returns True if all characters in the string are letters and the string is not empty, otherwise returns False.
#
# #### str.isdigit()
#
# Returns True if all characters in the string are digits and the string is not empty, otherwise returns False.
#
# #### str.islower()
#
# Returns True if all letters in the string are lowercase and there is at least one letter, otherwise returns False.
#
# #### str.isupper()
#
# Returns True if all letters in the string are uppercase and there is at least one letter, otherwise returns False.
#
# #### str.join(str_col)
#
# Returns a string created by concatenating the elements of the collection str_col with the calling string as a separator.
#
# #### str.ljust(width, fillchar)
#
# Returns a string of length width, left-aligned, and filled with fillchar on the right. The default fillchar is a space.
#
# #### str.lower()
#
# Returns a copy of the string with all letters converted to lowercase.
#
# #### str.lstrip(chars)
#
# Returns a string with the characters in chars removed from the beginning. If chars is not specified, whitespace is removed.
#
# #### str.rstrip(chars)
#
# Returns a string with the characters in chars removed from the end. If chars is not specified, whitespace is removed.
#
# #### str.split(sep)
#
# Returns a list of substrings split by the delimiter sep. If sep is not specified, splits by any whitespace.
#
# #### str.startswith(prefix)
#
# Returns True if the string starts with the substring prefix, otherwise returns False. The prefix can also be a tuple of multiple prefixes.
#
# #### str.strip(chars)
#
# Returns a string with the characters in chars removed from both the beginning and the end. If chars is not specified, whitespace is removed.
#
# #### str.title()
#
# Returns a string where the first letter of each word is uppercase, and all other letters are lowercase.
#
# #### str.upper()
#
# Returns a copy of the string with all letters converted to uppercase.
#
# #### str.zfill(width)
#
# Returns a string padded with zeros (0) on the left until it reaches the specified width.
#
#
# - x in s – Returns True if x is in list s, otherwise False.
# - x not in s – Returns False if x is in list s, otherwise True.
# - s + t – Returns a new list by concatenating lists s and t.
# - s * n – Returns a new list with s repeated n times.
# - len(s) – Returns the number of elements in list s.
# - min(s) – Returns the smallest element in list s.
# - max(s) – Returns the largest element in list s.
# - s.index(x) – Returns the index of the first occurrence of x, raises ValueError if x is not found.
# - s.count(x) – Returns the number of occurrences of x in list s.
# - s.append(x) – Adds x to the end of list s.
# - s.clear() – Removes all elements from list s.
# - s.copy() – Returns a shallow copy of list s.
# - s.extend(t) or s += t – Extends list s by appending elements from list t.
# - s.insert(i, x) – Inserts x at index i in list s.
# - s.pop(i) – Removes and returns the element at index i, or the last element if i is not specified.
# - s.remove(x) – Removes the first occurrence of x in list s.
# - s.reverse() – Reverses the order of elements in list s.
# - s.sort() – Sorts list s in ascending order (modifies the list). Use reverse=True for descending order.
# - sorted(s) – Returns a new sorted list without modifying s. Use reverse=True for descending order.

# +
# 1

count: int = int(input())
is_all_correct: bool = True
allowed_letters = ("а", "б", "в")

for _ in range(count):
    word = input()
    if not word.startswith(allowed_letters):
        is_all_correct = False

print("YES" if is_all_correct else "NO")

# +
# 2

value: str = input()
for i, char in enumerate(value):
    print(char)

# +
# 3

expected_title_length: int = int(input())
title_count: int = int(input())

for i in range(title_count):
    title: str = input()
    if len(title) > expected_title_length:
        result_title = title[: expected_title_length - 3] + "..."
    else:
        result_title = title
    print(result_title)

# +
# 4

while input_value := input():
    if not input_value:
        break
    result: str = input_value
    if input_value.endswith("@@@"):
        continue
    if input_value.startswith("##"):
        result = input_value[2:]
    print(result)

# +
# 5

input_string: str = input()

characters = list(input_string)
characters.reverse()
new_value = "".join(characters)

if input_string == new_value:
    print("YES")
else:
    print("NO")

# +
# 6

input_string_count = int(input())

count = 0

for _ in range(input_string_count):
    count += input().split().count("зайка")

print(count)

# +
# 7

input_sum_string: str = input()
values = input_sum_string.split(" ")
total_sum: int = 0

for value in values:
    total_sum += int(value)

print(total_sum)

# +
# 8

neighborhood_count: int = int(input())

for _ in range(neighborhood_count):
    neighborhood_desc: str = input()
    index = neighborhood_desc.find("зайка")
    if index < 0:
        print("Заек нет =(")
    else:
        print(index + 1)

# +
# 9

while True:
    line = input()
    if not line:
        break
    comment_index = line.find("#")
    if comment_index > -1:
        line = line[:comment_index]
    if line:
        print(line)

# +
# 10


frequencies: dict[str, int] = {}

while True:
    line = input().strip()
    if line == "ФИНИШ":
        break
    for char in line.lower():
        if char != " ":
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1

most_common_char = ""
max_freq = -1

for char, freq in frequencies.items():
    if freq > max_freq or (freq == max_freq and char < most_common_char):
        max_freq = freq
        most_common_char = char

print(most_common_char)

# +
# 11

title_count = int(input())

titles = [input().strip() for _ in range(title_count)]

query = input().strip().lower()

for title in titles:
    if query in title.lower():
        print(title)

# +
# 12

porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

days = int(input())

for day in range(days):
    print(porridges[day % 5])

# +
# 13

number_count = int(input())

numbers_list = [int(input()) for _ in range(number_count)]

exponent = int(input())

for number in numbers_list:
    print(number**exponent)

# +
# 14

numbers = input().split()
exponent = int(input())

print(" ".join(str(int(number) ** exponent) for number in numbers))

# +
# 15


def gcd(first_nmb: int, second_nmb: int) -> int:
    """Return greatest common divisor."""
    while second_nmb != 0:
        first_nmb, second_nmb = second_nmb, first_nmb % second_nmb
    return first_nmb


input_numbers: list[int] = list(map(int, input().split()))

output_result: int = input_numbers[0]
for num in input_numbers[1:]:
    output_result = gcd(output_result, num)

print(output_result)

# +
# 16

max_length = int(input())
lines = []

for _ in range(int(input())):
    lines.append(input())

for line in lines:
    if max_length > 3:
        if len(line) >= max_length - 3:
            line = line[: max_length - 3] + "..."
        else:
            if max_length == 4:
                line = line + "..."

        print(line)
        max_length -= len(line)

# +
# 17

input_string = input()

cleaned_string = input_string.replace(" ", "").lower()

if cleaned_string == cleaned_string[::-1]:
    print("YES")
else:
    print("NO")

# +
# 18

input_string = input()

current_char = input_string[0]
count = 1

for char in input_string[1:]:
    if char == current_char:
        count += 1
    else:
        print(current_char, count)
        current_char = char
        count = 1

print(current_char, count)

# +
# 19


expression = input().split()

operand_stack: list[int] = []

for token in expression:
    if token in "+-*/":
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        operation_result: int = 0
        if token == "+":
            operation_result = operand1 + operand2
        elif token == "-":
            operation_result = operand1 - operand2
        elif token == "*":
            operation_result = operand1 * operand2
        elif token == "/":
            operation_result = operand1 // operand2

        operand_stack.append(operation_result)
    else:
        operand_stack.append(int(token))

print(operand_stack[0])

# +
# 20


def factorial(nmb: int) -> int:
    """Return the factorial of a number."""
    rsl: int = 1
    for multiplier_val in range(2, nmb + 1):
        rsl *= multiplier_val
    return rsl


expression_value: str = input().strip()
tokens: list[str] = expression_value.split()

stack: list[int] = []

for token in tokens:
    if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
        stack.append(int(token))
    elif token in {"+", "-", "*", "/"}:
        b_val: int = stack.pop()
        a_val: int = stack.pop()
        if token == "+":
            stack.append(a_val + b_val)
        elif token == "-":
            stack.append(a_val - b_val)
        elif token == "*":
            stack.append(a_val * b_val)
        elif token == "/":
            stack.append(a_val // b_val)
    elif token == "~":
        stack.append(-stack.pop())
    elif token == "!":
        stack.append(factorial(stack.pop()))
    elif token == "#":
        stack_value: int = stack[-1]
        stack.append(stack_value)
    elif token == "@":
        first: int = stack.pop()
        second: int = stack.pop()
        third: int = stack.pop()
        stack.extend([second, first, third])

print(stack.pop())
