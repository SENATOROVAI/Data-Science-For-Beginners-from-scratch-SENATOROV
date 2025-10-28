"""Yandex handbook "Python Basics" answers."""

# +
# 1
size_tbl_1: int = 7

for row_i_1 in range(size_tbl_1):
    for col_j_1 in range(size_tbl_1):
        print((row_i_1 + 1) * (col_j_1 + 1), end=" ")
    print()

# +
# 2
size_tbl_2: int = 3

for mult_a_2 in range(1, size_tbl_2 + 1):
    for mult_b_2 in range(1, size_tbl_2 + 1):
        print(f"{mult_b_2} * {mult_a_2} = {mult_a_2 * mult_b_2}")

# +
# 3
total_nums_3: int = 12

limit_3: int = 1
curr_cnt_3: int = 0

for idx_3 in range(total_nums_3):
    curr_cnt_3 += 1
    print(idx_3 + 1, end=" ")
    if curr_cnt_3 == limit_3:
        print()
        limit_3 += 1
        curr_cnt_3 = 0

# +
# 4
count_vals_4: int = 3
numbers_4: list[int] = [99, 88, 1]

total_sum_4: int = 0

for val_4 in numbers_4:
    temp_4: int = val_4
    while temp_4 > 0:
        total_sum_4 += temp_4 % 10
        temp_4 //= 10

print(total_sum_4)

# +
# 5
scenes_5: int = 3
texts_5: list[list[str]] = [
    ["зайка", "ёлка", "ВСЁ"],
    ["лиса", "зайка", "ВСЁ"],
    ["медведь", "ВСЁ"],
]

bunny_hits_5: int = 0

for scene_5 in texts_5:
    charged_5: bool = False
    for line_5 in scene_5:
        if line_5 == "ВСЁ":
            break
        if line_5 == "зайка" and not charged_5:
            bunny_hits_5 += 1
            charged_5 = True

print(bunny_hits_5)

# +
# 6
nums_gcd_6: int = 3
values_gcd_6: list[int] = [12, 18, 24]

result_gcd_6: int = values_gcd_6[0]

for idx_6 in range(1, nums_gcd_6):
    temp_6: int = values_gcd_6[idx_6]
    a_6, b_6 = result_gcd_6, temp_6
    while b_6 != 0:
        a_6, b_6 = b_6, a_6 % b_6
    result_gcd_6 = a_6

print(result_gcd_6)

# +
# 7
launches_7: int = 2
base_delay_7: int = 3

for launch_idx_7 in range(launches_7):
    for sec_7 in range(base_delay_7 + launch_idx_7, 0, -1):
        print(f"До старта {sec_7} секунд(ы)")
    print(f"Старт {launch_idx_7 + 1}!!!")

# +
# 8
entries_8: int = 2
names_8: list[str] = ["Анна", "Денис"]
scores_8: list[int] = [19, 23]

best_name_8: str = ""
max_sum_8: int = 0

for idx_8 in range(entries_8):
    name_8: str = names_8[idx_8]
    num_8: int = scores_8[idx_8]

    digit_sum_8: int = 0
    temp_8: int = num_8
    while temp_8 > 0:
        digit_sum_8 += temp_8 % 10
        temp_8 //= 10

    if digit_sum_8 >= max_sum_8:
        max_sum_8 = digit_sum_8
        best_name_8 = name_8

print(best_name_8)

# +
# 9
count_nums_9: int = 2
input_vals_9: list[int] = [42, 65]

final_num_9: int = 0

for val_9 in input_vals_9:
    max_dig_9: int = int(max(str(val_9)))
    final_num_9 = final_num_9 * 10 + max_dig_9

print(final_num_9)

# +
# 10
pieces_10: int = 3

print("А Б В")
for a_10 in range(1, pieces_10 - 1):
    for b_10 in range(1, pieces_10 - a_10):
        c_10: int = pieces_10 - a_10 - b_10
        print(a_10, b_10, c_10)

# +
# 11
total_vals_11: int = 5
candidates_11: list[int] = [2, 3, 4, 5, 6]

prime_total_11: int = 0

for num_11 in candidates_11:
    if num_11 > 1:
        is_prime_11: bool = True
        div_11: int = 2
        while div_11 <= int(num_11**0.5) and is_prime_11:
            if num_11 % div_11 == 0:
                is_prime_11 = False
            else:
                div_11 += 1
        if is_prime_11:
            prime_total_11 += 1

print(prime_total_11)

# +
# 12
rows_12: int = 2
cols_12: int = 4

width_12: int = len(str(rows_12 * cols_12))
counter_12: int = 1

for _ in range(rows_12):
    for _ in range(cols_12):
        print(f"{counter_12:>{width_12}}", end=" ")
        counter_12 += 1
    print()

# +
# 13
height_13: int = 2
width_13: int = 5

cell_w_13: int = len(str(width_13 * height_13))

for r_13 in range(height_13):
    num_13: int = r_13 + 1
    for _ in range(width_13):
        print(f"{num_13:>{cell_w_13}}", end=" ")
        num_13 += height_13
    print()

# +
# 14
rows_14: int = 2
cols_14: int = 3

cell_w_14: int = len(str(rows_14 * cols_14))

for i_14 in range(rows_14):
    for j_14 in range(cols_14):
        val_14: int
        if i_14 % 2 == 0:
            val_14 = i_14 * cols_14 + j_14 + 1
        else:
            val_14 = (i_14 + 1) * cols_14 - j_14
        print(f"{val_14:>{cell_w_14}}", end=" ")
    print()

# +
# 15
height_15: int = 2
width_15: int = 3

cell_w_15: int = len(str(width_15 * height_15))

for r_15 in range(height_15):
    for c_15 in range(width_15):
        num_15: int
        if c_15 % 2 == 0:
            num_15 = c_15 * height_15 + r_15 + 1
        else:
            num_15 = (c_15 + 1) * height_15 - r_15
        print(f"{num_15:>{cell_w_15}}", end=" ")
    print()

# +
# 16
size_16: int = 3
cell_w_16: int = 3

row_len_16: int = size_16 * cell_w_16 + (size_16 - 1)

for i_16 in range(size_16):
    for j_16 in range(size_16):
        cell_val_16: int = (i_16 + 1) * (j_16 + 1)
        print(f"{cell_val_16:^{cell_w_16}}", end="")
        if j_16 != size_16 - 1:
            print("|", end="")
    print()
    if i_16 != size_16 - 1:
        print("-" * row_len_16)

# +
# 17
palin_count_17: int = 0
test_vals_17: list[int] = [121, 123, 454, 11, 9]

for num_17 in test_vals_17:
    orig_17: int = num_17
    rev_17: int = 0
    temp_17: int = num_17
    while temp_17 > 0:
        rev_17 = rev_17 * 10 + temp_17 % 10
        temp_17 //= 10
    if orig_17 == rev_17:
        palin_count_17 += 1

print(palin_count_17)

# +
# 18
limit_18: int = 6

curr_18: int = 0
row_w_18: int = 1
max_len_18: int = 0

while curr_18 <= limit_18:
    row_len_18: int = 0
    for pos_18 in range(row_w_18):
        curr_18 += 1
        if curr_18 <= limit_18:
            row_len_18 += len(str(curr_18))
        if pos_18 < row_w_18 - 1 and curr_18 < limit_18:
            row_len_18 += 1
    max_len_18 = max(max_len_18, row_len_18)
    row_w_18 += 1

curr_18 = 0
row_w_18 = 1

while curr_18 <= limit_18:
    row_str_18: str = ""
    for pos_18 in range(row_w_18):
        curr_18 += 1
        if curr_18 <= limit_18:
            row_str_18 += str(curr_18)
        if pos_18 < row_w_18 - 1 and curr_18 < limit_18:
            row_str_18 += " "
    print(f"{row_str_18:^{max_len_18}}")
    row_w_18 += 1

# +
# 19
size_19: int = 3

cell_w_19: int = len(str((size_19 + 1) // 2))

for i_19 in range(size_19):
    row_vals_19: list[str] = []
    for j_19 in range(size_19):
        val_19: int = min(
            i_19 + 1,
            j_19 + 1,
            size_19 - i_19,
            size_19 - j_19,
        )
        row_vals_19.append(f"{val_19:>{cell_w_19}}")
    print(" ".join(row_vals_19))

# +
# 20
num_20: int = 10

best_sum_20: int = 0
best_base_20: int = 0

for base_20 in range(10, 1, -1):
    digit_sum_20: int = 0
    temp_20: int = num_20
    while temp_20 > 0:
        digit_sum_20 += temp_20 % base_20
        temp_20 //= base_20
    if digit_sum_20 >= best_sum_20:
        best_sum_20 = digit_sum_20
        best_base_20 = base_20

print(best_base_20)
