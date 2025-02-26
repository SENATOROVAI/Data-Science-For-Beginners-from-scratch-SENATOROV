"""Nested loops."""

# +
# 1

table_size = int(input())

for row_number in range(1, table_size + 1):
    for column_number in range(1, table_size + 1):
        print(row_number * column_number, end=" ")
    print()

# +
# 2

multiplication_table_size = int(input())

for row_value in range(1, multiplication_table_size + 1):
    for column_value in range(1, multiplication_table_size + 1):
        print(f"{row_value} * {column_value} = {row_value * column_value}")

# +
# 3

max_value_1: int = int(input())

current_number_1: int = 1
current_row: int = 1

while current_number_1 <= max_value_1:
    for _ in range(current_row):
        if current_number_1 > max_value_1:
            break
        print(max_value_1, end=" ")
        current_number_1 += 1
    print()
    current_row += 1

# +
# 4

num_count_1: int = int(input())

total_sum: int = 0

for _ in range(num_count_1):
    number_str_1: str = input()
    for digit_char in number_str_1:
        total_sum += int(digit_char)

print(total_sum)

# +
# 5

num_lines = int(input().strip())

bunny_count: int = 0

for _ in range(num_lines):
    has_bunny: bool = False
    while True:
        word: str = input().strip()
        if word == "ВСЁ":
            break
        if word == "зайка":
            has_bunny = True
    if has_bunny:
        bunny_count += 1

print(bunny_count)

# +
# 6

num_count_2: int = int(input())

gcd_result: int = int(input())

for _ in range(num_count_2 - 1):
    next_num: int = int(input())
    while next_num != 0:
        gcd_result, next_num = next_num, gcd_result % next_num

print(gcd_result)

# +
# 7

num_participants_1: int = int(input())

countdown_start: int = 3

for participant_number_1 in range(num_participants_1):
    for seconds_left in range(countdown_start, 0, -1):
        print(f"До старта {seconds_left} секунд(ы)")
    print(f"Старт {participant_number_1 + 1}!!!")
    countdown_start += 1

# +
# 8

num_participants_2: int = int(input())

highest_digit_sum: int = -1
winner_name: str = ""

for _ in range(num_participants_2):
    participant_name: str = input()
    participant_number_2: str = input()

    digit_sum_total: int = sum(int(digit) for digit in participant_number_2)

    if digit_sum_total >= highest_digit_sum:
        highest_digit_sum = digit_sum_total
        winner_name = participant_name

print(winner_name)

# +
# 9

num_entries_1: int = int(input())

max_digits_result: str = ""

for _ in range(num_entries_1):
    number_str_2: str = input()
    max_digits_result += max(number_str_2)

print(max_digits_result)

# +
# 10

total_slices: int = int(input())

print("А Б В")

for slice_a in range(1, total_slices - 1):
    for slice_b in range(1, total_slices - slice_a):
        slice_c = total_slices - slice_a - slice_b
        if slice_c >= 1:
            print(slice_a, slice_b, slice_c)

# +
# 11


def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


num_entries_2: int = int(input())

prime_count: int = 0
for _ in range(num_entries_2):
    current_number_2: int = int(input())
    if is_prime(current_number_2):
        prime_count += 1

print(prime_count)

# +
# 12

num_rows_1: int = int(input())
num_columns_1: int = int(input())

max_number_1: int = num_rows_1 * num_columns_1
cell_width_1: int = len(str(max_number_1))

current_number_3: int = 1
for row_index in range(num_rows_1):
    row_values = []
    for column_index in range(num_columns_1):
        row_values.append(f"{current_number_3:>{cell_width_1}}")
        current_number_3 += 1
    print(" ".join(row_values))

# +
# 13

num_rows_2: int = int(input())
num_columns_2: int = int(input())

max_number_2: int = num_rows_2 * num_columns_2
cell_width_2: int = len(str(max_number_2))

for row_start in range(1, num_rows_2 + 1):
    row_values = []
    current_number_4 = row_start
    for _ in range(num_columns_2):
        row_values.append(f"{current_number_4:>{cell_width_2}}")
        current_number_4 += num_rows_2
    print(" ".join(row_values))

# +
# 14

num_rows_3: int = int(input())
num_columns_3: int = int(input())

max_number_3: int = num_rows_3 * num_columns_3
cell_width_3: int = len(str(max_number_3))

current_number_5: int = 1
for row_index in range(num_rows_3):
    row_values = []
    for _ in range(num_columns_3):
        row_values.append(f"{current_number_5:>{cell_width_3}}")
        current_number_5 += 1
    if row_index % 2 != 0:
        row_values.reverse()
    print(" ".join(row_values))

# +
# 15

num_rows_4 = int(input())
num_columns_4 = int(input())

max_number = num_rows_4 * num_columns_4
cell_width = len(str(max_number))

matrix = [[0] * num_columns_4 for _ in range(num_rows_4)]

current_number_6 = 1
for column_index in range(num_columns_4):
    if column_index % 2 == 0:
        for row_index in range(num_rows_4):
            matrix[row_index][column_index] = current_number_6
            current_number_6 += 1
    else:
        for row_index in range(num_rows_4 - 1, -1, -1):
            matrix[row_index][column_index] = current_number_6
            current_number_6 += 1

for row in matrix:
    print(" ".join(f"{value:>{cell_width}}" for value in row))

# +
# 16

table_size = int(input())
column_width = int(input())

for row_number in range(1, table_size + 1):
    row_values = [
        f"{row_number * col_number:^{column_width}}"
        for col_number in range(1, table_size + 1)
    ]
    print("|".join(row_values))

    if row_number < table_size:
        print("-" * (table_size * (column_width + 1) - 1))

# +
# 17

num_entries_3 = int(input())

palindrome_count = 0

for _ in range(num_entries_3):
    number_str = input().strip()
    if number_str == number_str[::-1]:
        palindrome_count += 1

print(palindrome_count)

# +
# 18

max_value_2: int = int(input())

current_number: int = 1
current_row_size: int = 1
rows: list[list[str]] = []
while current_number <= max_value_2:
    sub_row: list[str] = []
    for _ in range(current_row_size):
        if current_number > max_value_2:
            break
        sub_row.append(str(current_number))
        current_number += 1
    rows.append(sub_row)
    current_row_size += 1

max_width: int = len(" ".join(rows[-1]))

for rw in rows:
    line: str = " ".join(rw)
    print(line)

# +
# 19

grid_size = int(input())

max_value_3 = (grid_size // 2) + 1 if grid_size % 2 == 1 else grid_size // 2
cell_width = len(str(max_value_3))

for row_index in range(grid_size):
    row_values = []
    for col_index in range(grid_size):
        value = 1 + min(
            row_index,
            col_index,
            grid_size - 1 - row_index,
            grid_size - 1 - col_index,
        )
        row_values.append(f"{value:>{cell_width}}")
    print(" ".join(row_values))

# +
# 20


def sum_of_digits(number: int, base: int) -> int:
    """Return sum of digit."""
    digit_sum = 0
    while number > 0:
        digit_sum += number % base
        number //= base
    return digit_sum


def optimal_base(number: int) -> int:
    """Return optimal base."""
    max_digit_sum = -1
    best_base = 2
    for base in range(2, 11):
        current_digit_sum = sum_of_digits(number, base)
        if current_digit_sum > max_digit_sum:
            max_digit_sum = current_digit_sum
            best_base = base
    return best_base


input_val: int = int(input())
print(optimal_base(input_val))
