"""Loops."""

# +
# 1

while (string := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# +
# 2

tally_1: int = 0
while (string := input()) != "Приехали!":
    if "зайка" in string:
        tally_1 += 1

print(tally_1)

# +
# 3

start: int = int(input())
end: int = int(input())

for i in range(start, end + 1):
    print(i, end=" ")

# +
# 4

launch: int = int(input())
completion: int = int(input())

step: int = 1
if completion < launch:
    step = -1
else:
    step = 1

for i in range(launch, completion + step, step):
    print(i, end=" ")

# +
# 5

total_sum: float = 0

while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    total_sum += price

print(total_sum)

# +
# 6

a_var: int = int(input())
b_var: int = int(input())

while a_var != 0 and b_var != 0:
    if a_var >= b_var:
        a_var -= b_var
    else:
        b_var -= a_var

print(a_var + b_var)

# +
# 7

c_var: int = int(input())
d_var: int = int(input())
e_var: int
f_var: int
e_var, f_var = c_var, d_var

while e_var != 0:
    e_var, f_var = f_var % e_var, e_var

print(c_var * d_var // (e_var + f_var))

# +
# 8

info: str = input()
repeat: int = int(input())

for i in range(repeat):
    print(info)

# +
# 9

num_1: int = int(input())
factorial: int = 1

for i in range(2, num_1 + 1):
    factorial *= i
print(factorial)

# +
# 10

x_coord: int = 0
y_coord: int = 0

while (direction := input()) != "СТОП":
    move = int(input())
    if direction == "ВОСТОК":
        x_coord += move
    elif direction == "ЗАПАД":
        x_coord -= move
    elif direction == "СЕВЕР":
        y_coord += move
    elif direction == "ЮГ":
        y_coord -= move

print(y_coord)
print(x_coord)

# +
# 11

num_2: int = int(input())

summa: int = 0

while num_2 > 0:
    summa += num_2 % 10
    num_2 //= 10

print(summa)

# +
# 12

num_3: int = int(input())

max_digit: int = max(int(digit) for digit in str(num_3))

print(max_digit)

# +
# 13

tally_2: int = int(input())

names: list[str] = [input() for i in range(tally_2)]

first_gamer: str = min(names)

print(first_gamer)

# +
# 14

num_4 = int(input())

simple = True

if num_4 <= 1:
    simple = False
else:
    for divisor_1 in range(2, int(num_4**0.5 + 1)):
        if num_4 % divisor_1 == 0:
            simple = False
            break

if simple is True:
    print("YES")
else:
    print("NO")

# +
# 15

locations: int = int(input())

bunnies: int = 0

for i in range(locations):
    nature = input()
    if "зайка" in nature:
        bunnies += 1

print(bunnies)

# +
# 16

num_5: int = int(input())

original_number_1: int = num_5
reversed_number: int = 0

while num_5 > 0:
    digit: int = num_5 % 10
    reversed_number = reversed_number * 10 + digit
    num_5 //= 10

if original_number_1 == reversed_number:
    print("YES")
else:
    print("NO")

# +
# 17

original_number_2: int = int(input())

filtered_number: int = 0
decimal_place: int = 1

while original_number_2 > 0:
    last_digit: int = original_number_2 % 10
    if last_digit % 2 != 0:
        filtered_number += last_digit * decimal_place
        decimal_place *= 10
    original_number_2 //= 10

print(filtered_number)

# +
# 18

sample_number: int = int(input())

if sample_number == 1:
    print(sample_number)

divisor_2: int = 2

while sample_number >= 2:
    prime: bool = True

    while divisor_2**2 <= sample_number and prime is True:
        if sample_number % divisor_2 == 0:
            prime = False
        else:
            divisor_2 = divisor_2 + 1
    if prime is True:
        print(sample_number)
        sample_number = 1
    else:
        print(f"{divisor_2}", end=" * ")
        sample_number = sample_number // divisor_2

# +
# 19

begin: int = 1
finish: int = 1001
attempts: int = 0

ask: int = (begin + finish) // 2
print(ask)

while (answer := input().strip()) != "Угадал!" and attempts < 10:
    if answer == "Меньше":
        finish = ask
    elif answer == "Больше":
        begin = ask

    ask = (begin + finish) // 2
    print(ask)
    attempts += 1

# +
# 20

query_count: int = int(input())

previous_hash: int = 0
first_error_index: int = 0
has_error: bool = False

for index in range(query_count):
    block_data: int = int(input())

    expected_hash: int = block_data % 256
    right_byte: int = (block_data // 256) % 256
    message: int = block_data // (256**2)

    calculated_hash: int = (37 * (message + right_byte + previous_hash)) % 256

    if calculated_hash != expected_hash or calculated_hash >= 100:
        if not has_error:
            first_error_index = index
            has_error = True

    previous_hash = expected_hash

print(-1 if not has_error else first_error_index)
