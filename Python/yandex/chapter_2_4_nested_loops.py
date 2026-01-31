"""Nested loops."""

# +
# 1

table_size_1: int = int(input())

for row_number in range(table_size_1):
    for column_number in range(table_size_1):
        print((row_number + 1) * (column_number + 1), end=" ")
    print()

# +
# 2

initial_size: int = int(input())

for multiplicand in range(1, initial_size + 1):
    for multiplier in range(1, initial_size + 1):
        print(f"{multiplier} * {multiplicand} = {multiplicand * multiplier}")

# +
# 3

finish: int = int(input())

limit: int = 1
current: int = 0

for i in range(finish):
    current += 1
    print(i + 1, end=" ")
    if current == limit:
        print()
        limit += 1
        current = 0

# +
# 4

tally_1: int = int(input())

summa: int = 0

for _ in range(tally_1):
    number_1: int = int(input())
    while number_1 > 0:
        summa += number_1 % 10
        number_1 //= 10

print(summa)

# +
# 5

natures: int = int(input())

bunnies: int = 0

for _ in range(natures):
    debited: bool = False
    string: str
    while (string := input()) != "ВСЁ":
        if string == "зайка" and debited is False:
            bunnies = bunnies + 1
            debited = True

print(bunnies)

# +
# 6

tally_2: int = int(input())

gcd_value: int = int(input())

for _ in range(tally_2 - 1):
    number_2: int = int(input())
    while number_2 != 0:
        gcd_value, number_2 = number_2, gcd_value % number_2

print(gcd_value)

# +
# 7

tally_3: int = int(input())

base: int = 3

for number_3 in range(tally_3):
    for delay in range(base + number_3, 0, -1):
        print(f"До старта {delay} секунд(ы)")
    print(f"Старт {number_3 + 1}!!!")

# +
# 8

entries_count: int = int(input())

name_with_max_digit_sum: str = ""
max_digit_sum_1: int = 0

for _ in range(entries_count):
    current_name: str = input()
    current_number_1: int = int(input())

    digit_sum_1: int = 0
    while current_number_1 > 0:
        digit_sum_1 += current_number_1 % 10
        current_number_1 //= 10

    if digit_sum_1 >= max_digit_sum_1:
        max_digit_sum_1 = digit_sum_1
        name_with_max_digit_sum = current_name

print(name_with_max_digit_sum)

# +
# 9

count: int = int(input())

result: int = 0

for _ in range(count):
    number_4: int = int(input())
    max_digit: int = int(max(str(number_4)))
    result = result * 10 + max_digit
print(result)

# +
# 10

slices: int = int(input())

print("А Б В")
for a_var in range(1, slices - 1):
    for b_var in range(1, slices - a_var):
        c_var: int = slices - a_var - b_var
        print(a_var, b_var, c_var)

# +
# 11

total_numbers: int = int(input())

prime_count: int = 0

for _ in range(total_numbers):
    candidate: int = int(input())

    if candidate > 1:
        is_prime: bool = True
        divisor: int = 2

        while divisor <= int(candidate**0.5) and is_prime:
            if candidate % divisor == 0:
                is_prime = False
            else:
                divisor += 1

        if is_prime:
            prime_count += 1

print(prime_count)

# +
# 12

num_rows_1: int = int(input())
num_columns_1: int = int(input())

cell_width_1: int = len(str(num_rows_1 * num_columns_1))

current_number_2: int = 1
for _ in range(num_rows_1):
    for _ in range(num_columns_1):
        print(f"{current_number_2:>{cell_width_1}}", end=" ")
        current_number_2 += 1
    print()

# +
# 13

height_1: int = int(input())
width_1: int = int(input())

cell_width_2: int = len(str(width_1 * height_1))

number_5: int = 1
for row in range(height_1):
    number_5 = row + 1
    for _ in range(width_1):
        print(f"{number_5:>{cell_width_2}}", end=" ")
        number_5 += height_1
    print()

# +
# 14

num_rows_2: int = int(input())
num_columns_2: int = int(input())

cell_width_3: int = len(str(num_rows_2 * num_columns_2))

if num_rows_2 > 0 and num_columns_2 > 0:
    for row_index in range(num_rows_2):
        for col_index in range(num_columns_2):
            value_1: int
            if (row_index % 2) == 0:
                value_1 = row_index * num_columns_2 + col_index + 1
            else:
                value_1 = (row_index + 1) * num_columns_2 - col_index
            print(f"{value_1:>{cell_width_3}}", end=" ")
        print()

# +
# 15

height_2: int = int(input())
width_2: int = int(input())

ceil_width_4: int = len(str(width_2 * height_2))

for row in range(height_2):
    for column in range(width_2):
        num: int
        if column % 2 == 0:
            num = column * height_2 + row + 1
        else:
            num = (column + 1) * height_2 - row
        print(f"{num:>{ceil_width_4}}", end=" ")
    print()

# +
# 16

table_size_2: int = int(input())
cell_width_5: int = int(input())

row_length: int = table_size_2 * cell_width_5 + (table_size_2 - 1)

for row_index in range(table_size_2):
    for col_index in range(table_size_2):
        cell_value: int = (row_index + 1) * (col_index + 1)
        print(f"{cell_value:^{cell_width_5}}", end="")

        if col_index != table_size_2 - 1:
            print("|", end="")
    print()

    if row_index != table_size_2 - 1:
        print("-" * row_length)

# +
# 17

palindrome_count: int = 0

for _ in range(int(input())):
    current_number_3: int = int(input())
    original_number: int = current_number_3
    reversed_number: int = 0

    while current_number_3 > 0:
        last_digit: int = current_number_3 % 10
        reversed_number = reversed_number * 10 + last_digit
        current_number_3 //= 10

    if original_number == reversed_number:
        palindrome_count += 1

print(palindrome_count)

# +
# 18

limit_value: int = int(input())

current_number_4: int = 0
row_width: int = 1
max_row_length: int = 0

while current_number_4 <= limit_value:
    current_row_length: int = 0

    for position_in_row in range(row_width):
        current_number_4 += 1

        if current_number_4 <= limit_value:
            current_row_length += len(str(current_number_4))

        if position_in_row < row_width - 1 and current_number_4 < limit_value:
            current_row_length += 1

    max_row_length = max(max_row_length, current_row_length)
    row_width += 1

current_number_4 = 0
row_width = 1

while current_number_4 <= limit_value:
    row_string = ""

    for position_in_row in range(row_width):
        current_number_4 += 1

        if current_number_4 <= limit_value:
            row_string += str(current_number_4)

        if position_in_row < row_width - 1 and current_number_4 < limit_value:
            row_string += " "

    print(f"{row_string:^{max_row_length}}")
    row_width += 1

# +
# 19

matrix_size: int = int(input())

cell_width_6: int = len(str((matrix_size + 1) // 2))

output_lines: list[str] = []

for row_index in range(matrix_size):
    current_row: list[str] = []
    for column_index in range(matrix_size):
        value_2: int = min(
            row_index + 1,
            column_index + 1,
            matrix_size - row_index,
            matrix_size - column_index,
        )
        current_row.append(f"{value_2:>{cell_width_6}}")
    output_lines.append(" ".join(current_row))

for line in output_lines:
    print(line)

# +
# 20

decimal_number: int = int(input())

max_digit_sum_2: int = 0
optimal_base: int = 0

for base in range(10, 1, -1):
    digit_sum_2: int = 0
    temp_number: int = decimal_number
    while temp_number > 0:
        digit_sum_2 += temp_number % base
        temp_number //= base
    if digit_sum_2 >= max_digit_sum_2:
        max_digit_sum_2 = digit_sum_2
        optimal_base = base

print(optimal_base)
