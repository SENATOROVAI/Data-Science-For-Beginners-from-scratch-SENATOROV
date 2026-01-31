"""Strings, tuples, lists."""

# +
# 1

number: int = int(input())

all_good: bool = True

for _ in range(number):
    word: str = input()
    if word[0] not in "абв":
        all_good = False

if all_good:
    print("YES")
else:
    print("NO")

# +
# 2

string_1: str = input()

for index, letter in enumerate(string_1):
    print(letter)

# +
# 3

length: int = int(input())
count_1: int = int(input())

for _ in range(count_1):
    string_a: str = input()
    if len(string_a) <= length:
        print(string_a)
    else:
        print(f"{string_a[:length - 3]}...")

# +
# 4

string_2: str

while string_2 := input():
    if string_2[-3:] != "@@@":
        if string_2[0:2] == "##":
            string_2 = string_2[2:]
        print(string_2)

# +
# 5

string_3: str = input()

if string_3 == string_3[::-1]:
    print("YES")
else:
    print("NO")

# +
# 6

count_2: int = int(input())

bunnies: int = 0
for _ in range(count_2):
    string_b: str = input()
    bunnies += string_b.count("зайка")

print(bunnies)

# +
# 7

string_4: str = input()

lst: list[str] = string_4.split()

print(int(lst[0]) + int(lst[1]))

# +
# 8

district_count: int = int(input())

for _ in range(district_count):
    string_c: str = input()
    if "зайка" in string_c:
        print(string_c.index("зайка") + 1)
    else:
        print("Заек нет =(")

# +
# 9

string_5: str

while string_5 := input():
    if not (comment_pos := string_5.find("#")) + 1:
        print(string_5)
    elif string_5[:comment_pos]:
        print(string_5[:comment_pos])

# +
# 10

unique_chars: list[str] = []
char_counts: list[int] = []

while (line := input()) != "ФИНИШ":
    line = line.lower().replace(" ", "")
    for char in line:
        if char in unique_chars:
            char_counts[unique_chars.index(char)] += 1
        else:
            unique_chars.append(char)
            char_counts.append(1)

max_count: int = 0
most_frequent_chars: list[str] = []

for i, char in enumerate(unique_chars):
    if char_counts[i] > max_count:
        max_count = char_counts[i]
        most_frequent_chars = [char]
    elif char_counts[i] == max_count:
        most_frequent_chars.append(char)

most_frequent_chars.sort()
if most_frequent_chars:
    print(most_frequent_chars[0])

# +
# 11

count_3: int = int(input())

titles: list[str] = []
for _ in range(count_3):
    titles.append(input())

query: str = input()

for title in titles:
    if query.lower() in title.lower():
        print(title)

# +
# 12

porridges: list[str] = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

days: int = int(input())
for day in range(days):
    print(porridges[day % len(porridges)])

# +
# 13

count_4: int = int(input())
numbers_1: list[int] = []

for _ in range(count_4):
    numbers_1.append(int(input()))

power_1: int = int(input())

for number in numbers_1:
    print(number**power_1)

# +
# 14


string_6: str = input()
power_2: int = int(input())

numbers_2: list[int] = [int(num) for num in string_6.split()]

for number in numbers_2:
    print(number**power_2, end=" ")

# +
# 15

user_input: str = input()
string_7: list[str] = user_input.split()

numbers_3: list[int] = []

for digits in string_7:
    numbers_3.append(int(digits))

current_gcd: int = numbers_3[0]

for number in numbers_3[1:]:
    while number != 0:
        current_gcd, number = number, current_gcd % number

print(current_gcd)

# +
# 16

max_total_length: int = int(input())

line_count: int = int(input())
input_lines: list[str] = [input() for _ in range(line_count)]

for line in input_lines:
    if max_total_length > 3:
        if len(line) >= max_total_length - 3:
            line = line[: max_total_length - 3] + "..."
        else:
            if max_total_length == 4:
                line = line + "..."

        print(line)
        max_total_length -= len(line)

# +
# 17

user_input_2: str = input()
string_8: str = user_input_2.replace(" ", "").lower()

if string_8 == string_8[::-1]:
    print("YES")
else:
    print("NO")

# +
# 18

incoming_string: str = input()

current_char: str = incoming_string[0]
tally: int = 1

for char in incoming_string[1:]:
    if current_char == char:
        tally += 1
    else:
        print(current_char, tally)
        current_char = char
        tally = 1

print(current_char, tally)

# +
# 19

input_string: str = input()
rpn_tokens: list[str] = input_string.split(" ")

evaluation_stack: list[int] = []

while rpn_tokens:
    current_token: str = rpn_tokens.pop(0)
    if current_token.isdigit():
        evaluation_stack.append(int(current_token))
    else:
        right = evaluation_stack.pop()
        left = evaluation_stack.pop()
        if current_token == "+":
            evaluation_stack.append(left + right)
        elif current_token == "-":
            evaluation_stack.append(left - right)
        elif current_token == "*":
            evaluation_stack.append(left * right)
        elif current_token == "/":
            evaluation_stack.append(int(left / right))

print(evaluation_stack[-1])

# +
# 20

expression: str = input()
tokens: list[str] = expression.split()

unary_ops: list[str] = ["~", "#", "!"]
binary_ops: list[str] = ["+", "-", "*", "/"]
ternary_ops: list[str] = ["@"]

stack: list[int] = []

while tokens:
    token: str = tokens.pop(0)

    if token in unary_ops:
        operand: int = stack.pop()
        if token == "~":
            stack.append(-operand)
        elif token == "!":
            result: int = 1
            for i in range(1, operand + 1):
                result *= i
            stack.append(result)
        elif token == "#":
            stack.append(operand)
            stack.append(operand)

    elif token in binary_ops:
        right_operand: int = stack.pop()
        left_operand: int = stack.pop()
        if token == "+":
            stack.append(left_operand + right_operand)
        elif token == "-":
            stack.append(left_operand - right_operand)
        elif token == "*":
            stack.append(left_operand * right_operand)
        elif token == "/":
            stack.append(left_operand // right_operand)

    elif token in ternary_ops:
        top_1: int = stack.pop()
        top_2: int = stack.pop()
        top_3: int = stack.pop()
        if token == "@":
            stack.append(top_2)
            stack.append(top_1)
            stack.append(top_3)

    else:
        stack.append(int(token))

print(int(stack[-1]))
