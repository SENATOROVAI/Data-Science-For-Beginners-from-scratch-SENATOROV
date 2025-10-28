"""Yandex handbook "Python Basics" answers."""

# +
# 1
test_inputs: list[str] = ["Раз!", "Два!", "Три!"]
index: int = 0

while index < len(test_inputs):
    string: str = test_inputs[index]
    if string == "Три!":
        break
    print("Режим ожидания...")
    index += 1

print("Ёлочка, гори!")

# +
# 2
input_lines: list[str] = ["зайка в лесу", "ёлка", "зайка бежит", "Приехали!"]
bunny_counter: int = 0
loop_i_2: int = 0

while loop_i_2 < len(input_lines):
    current_line: str = input_lines[loop_i_2]
    if current_line == "Приехали!":
        break
    if "зайка" in current_line:
        bunny_counter += 1
    loop_i_2 += 1

print(bunny_counter)

# +
# 3
range_start: int = 1
range_end: int = 10

for num in range(range_start, range_end + 1):
    print(num, end=" ")

# +
# 4
start_val: int = 2
end_val: int = -4

direction: int = -1 if end_val < start_val else 1

for num in range(start_val, end_val + direction, direction):
    print(num, end=" ")

# +
# 5
prices_list: list[float] = [600.0, 400.0, 0.0]
total_amount: float = 0.0
idx: int = 0

while idx < len(prices_list):
    current_price: float = prices_list[idx]
    if current_price == 0.0:
        break
    if current_price >= 500:
        current_price *= 0.9
    total_amount += current_price
    idx += 1

print(total_amount)

# +
# 6
num_x: int = 12
num_y: int = 5

while num_x != 0 and num_y != 0:
    if num_x >= num_y:
        num_x -= num_y
    else:
        num_y -= num_x

print(num_x + num_y)

# +
# 7
val_m: int = 28
val_n: int = 44
temp_u: int
temp_v: int
temp_u, temp_v = val_m, val_n

while temp_u != 0:
    temp_u, temp_v = temp_v % temp_u, temp_u

print(val_m * val_n // (temp_u + temp_v))

# +
# 8
message_text: str = "3 + 6 = 8"
repeat_count: int = 4

for _ in range(repeat_count):
    print(message_text)

# +
# 9
input_val: int = 4
result_fact: int = 1

for num in range(2, input_val + 1):
    result_fact *= num

print(result_fact)

# +
# 10
route_plan: list[tuple[str, int]] = [
    ("СЕВЕР", 2),
    ("ВОСТОК", 3),
    ("ЮГ", 2),
    ("ЗАПАД", 3),
    ("СТОП", 0),
]

coord_x: int = 0
coord_y: int = 0
loop_i_11: int = 0

while loop_i_11 < len(route_plan):
    move_dir: str = route_plan[loop_i_11][0]
    if move_dir == "СТОП":
        break
    steps_count: int = route_plan[loop_i_11][1]
    if move_dir == "ВОСТОК":
        coord_x += steps_count
    elif move_dir == "ЗАПАД":
        coord_x -= steps_count
    elif move_dir == "СЕВЕР":
        coord_y += steps_count
    elif move_dir == "ЮГ":
        coord_y -= steps_count
    loop_i_11 += 1

print(coord_y)
print(coord_x)

# +
# 11
value_n: int = 689

digit_sum: int = 0

while value_n > 0:
    digit_sum += value_n % 10
    value_n //= 10

print(digit_sum)

# +
# 12
number_val: int = 546

largest_digit: int = max(int(d) for d in str(number_val))

print(largest_digit)

# +
# 13
player_count: int = 3
participant_list: list[str] = ["Вадик", "Анна", "Борис"]

earliest_player: str = min(participant_list)
print(earliest_player)

# +
# 14
test_number: int = 121

is_prime: bool = True

if test_number <= 1:
    is_prime = False
else:
    for divisor in range(2, int(test_number**0.5) + 1):
        if test_number % divisor == 0:
            is_prime = False
            break

if is_prime:
    print("YES")
else:
    print("NO")

# +
# 15
site_count: int = 4
sightings: int = 0

places: list[str] = ["лес", "зайка в поле", "река", "зайка у куста"]

for place in places:
    if "зайка" in place:
        sightings += 1

print(sightings)

# +
# 16
input_num: int = 121

original_val: int = input_num
reversed_val: int = 0

while input_num > 0:
    digit_val: int = input_num % 10
    reversed_val = reversed_val * 10 + digit_val
    input_num //= 10

if original_val == reversed_val:
    print("YES")
else:
    print("NO")

# +
# 17
source_num: int = 34569

result_num: int = 0
place_val: int = 1

while source_num > 0:
    digit_last: int = source_num % 10
    if digit_last % 2 != 0:
        result_num += digit_last * place_val
        place_val *= 10
    source_num //= 10

print(result_num)

# +
# 18
test_val: int = 120

if test_val == 1:
    print(test_val)

factor: int = 2

while test_val >= 2:
    is_prime_flag: bool = True

    while factor**2 <= test_val and is_prime_flag:
        if test_val % factor == 0:
            is_prime_flag = False
        else:
            factor += 1
    if is_prime_flag:
        print(test_val)
        test_val = 1
    else:
        print(f"{factor}", end=" * ")
        test_val //= factor

# +
# 19
low_val: int = 1
high_val: int = 1001
attempt_num: int = 0

answers_seq: list[str] = ["Меньше", "Больше", "Угадал!"]
ans_idx: int = 0

current_guess: int = (low_val + high_val) // 2
print(current_guess)

should_continue: bool = True
while should_continue:
    if ans_idx >= len(answers_seq):
        should_continue = False
    elif answers_seq[ans_idx] == "Угадал!":
        should_continue = False
    elif attempt_num >= 10:
        should_continue = False
    else:
        reply_text: str = answers_seq[ans_idx]
        if reply_text == "Меньше":
            high_val = current_guess
        elif reply_text == "Больше":
            low_val = current_guess

        current_guess = (low_val + high_val) // 2
        print(current_guess)
        attempt_num += 1
        ans_idx += 1

# +
# 20
block_count: int = 3

prev_hash_val: int = 0
error_pos: int = 0
found_error: bool = False

test_blocks: list[int] = [123456, 789012, 345678]

for pos in range(block_count):
    data_val: int = test_blocks[pos]

    hash_expected: int = data_val % 256
    byte_low: int = (data_val // 256) % 256
    payload: int = data_val // (256**2)

    hash_computed: int = (37 * (payload + byte_low + prev_hash_val)) % 256

    if hash_computed != hash_expected or hash_computed >= 100:
        if not found_error:
            error_pos = pos
            found_error = True

    prev_hash_val = hash_expected

print(-1 if not found_error else error_pos)
