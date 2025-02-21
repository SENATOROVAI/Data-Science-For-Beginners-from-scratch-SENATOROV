"""Conditional operators."""

# +
# 1
import math

username: str = input("Как Вас зовут?\n")
print(f"Здравствуйте, {username}!")
response: str = input("Как дела?\n")

if response == "хорошо":
    print("Я за вас рада!")
else:
    print("Всё наладится!")

# +
# 2

route_length: int = 43872

first_participant_average_speed: int = int(input())
second_participant_average_speed: int = int(input())

if first_participant_average_speed > second_participant_average_speed:
    print("Петя")
else:
    print("Вася")

# +
# 3

p_speed: float = float(input())
v_speed: float = float(input())
t_speed: float = float(input())


if p_speed > v_speed and p_speed > t_speed:
    print("Петя")
elif v_speed > p_speed and v_speed > t_speed:
    print("Вася")
else:
    print("Толя")

# +
# 4

track_length = 43872

first_name = "Петя"
first_speed = float(input())
second_name = "Вася"
second_speed = float(input())
third_name = "Толя"
third_speed = float(input())

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

print(f"1. {first_name}")
print(f"2. {second_name}")
print(f"3. {third_name}")

# +
# 5

petya_apples: int = 7
vasya_apples: int = 6
tolya_apples: int = 0

N_val = int(input())
M_val = int(input())

petya_apples -= 3
vasya_apples += 3

petya_apples += 2
tolya_apples -= 2

vasya_apples += 5
tolya_apples -= 5

vasya_apples -= 2

petya_apples += N_val
vasya_apples += M_val

if petya_apples > vasya_apples:
    print("Петя")
else:
    print("Вася")

# +
# 6

year: int = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("YES")
else:
    print("NO")

# +
# 7

number_1: int = int(input())

h_val = number_1 // 1000
j_val = (number_1 // 100) % 10
t_val = (number_1 // 10) % 10
d_val = number_1 % 10

if h_val == d_val and j_val == t_val:
    print("YES")
else:
    print("NO")

# +
# 8

sentence: str = input()
query_1: str = "зайка"

if query_1 in sentence:
    print("YES")
else:
    print("NO")

# +
# 9

player1: str = input()
player2: str = input()
player3: str = input()

first_player = min(player1, player2, player3)

print(first_player)

# +
# 10

number_2: int = int(input())

hundreds = number_2 // 100
tens = (number_2 // 10) % 10
units = number_2 % 10

sum1 = tens + units
sum2 = hundreds + tens

if sum1 > sum2:
    encrypted_number = int(f"{sum1}{sum2}")
else:
    encrypted_number = int(f"{sum2}{sum1}")

print(encrypted_number)

# +
# 11

number_3: int = int(input())

hundreds = number_3 // 100
tens = (number_3 // 10) % 10
units = number_3 % 10

min_digit = min(hundreds, tens, units)
max_digit = max(hundreds, tens, units)
middle_digit_val = hundreds + tens + units - min_digit - max_digit

if min_digit + max_digit == 2 * middle_digit_val:
    print("YES")
else:
    print("NO")

# +
# 12

r_val: int = int(input())
l_val: int = int(input())
z_val: int = int(input())

if r_val + l_val > z_val and r_val + z_val > l_val and l_val + z_val > r_val:
    print("YES")
else:
    print("NO")

# +
# 13

elf_number: int = int(input())
gnome_number: int = int(input())
human_number: int = int(input())

elf_tens = elf_number // 10
elf_units = elf_number % 10
gnome_tens = gnome_number // 10
gnome_units = gnome_number % 10
human_tens = human_number // 10
human_units = human_number % 10

if elf_tens == gnome_tens == human_tens:
    print(elf_tens)
elif elf_units == gnome_units == human_units:
    print(elf_units)
else:
    print("NO")

# +
# 14

number_4: int = int(input())

hundreds = number_4 // 100
tens = (number_4 // 10) % 10
units = number_4 % 10

combinations = [
    hundreds * 10 + tens,
    hundreds * 10 + units,
    tens * 10 + hundreds,
    tens * 10 + units,
    units * 10 + hundreds,
    units * 10 + tens,
]
valid_combinations = [num for num in combinations if num >= 10]

print(min(valid_combinations), max(valid_combinations))

# +
# 15

num1 = int(input())
num2 = int(input())

num1_hundreds = (num1 // 100) if num1 >= 100 else None
num1_tens = (num1 // 10) % 10
num1_units = num1 % 10

num2_hundreds = (num2 // 100) if num2 >= 100 else None
num2_tens = (num2 // 10) % 10
num2_units = num2 % 10

digits: list[float | None] = [
    num1_hundreds,
    num1_tens,
    num1_units,
    num2_hundreds,
    num2_tens,
    num2_units,
]

filtered_digits = [d for d in digits if d is not None]


first_digit = max(filtered_digits)
last_digit = min(filtered_digits)

sum_rest_digits = sum(filtered_digits) - first_digit - last_digit

middle_digit = sum_rest_digits % 10

print(int(f"{first_digit}{middle_digit}{last_digit}"))

# +
# 16

pete_speed = float(input())
vase_speed = float(input())
tolya_speed = float(input())

distance = 43872

time_pete = distance / pete_speed
time_vase = distance / vase_speed
time_tolya = distance / tolya_speed


racers: list[dict[str, float | str]] = [
    {"name": "Петя", "time": time_pete},
    {"name": "Вася", "time": time_vase},
    {"name": "Толя", "time": time_tolya},
]


racers.sort(key=lambda obj: obj["time"])

# Формируем красивый пьедестал
print(f"{racers[0]['name']:^22}")  # Второе место (по центру)
print(f"{racers[1]['name']:^10}")  # Первое место (по центру шире)
print(f"{racers[2]['name']:>20}")  # Третье место (справа)
print("   II      I      III   ")

# +
# 17


m_val = float(input())
p_val = float(input())
w_val = float(input())

D_val = p_val**2 - 4 * m_val * w_val

if m_val == 0:
    if p_val == 0:
        if w_val == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x_val = -w_val / p_val
        print(f"{x_val:.2f}")
else:
    if D_val < 0:
        print("No solution")
    elif D_val == 0:
        x_val = -p_val / (2 * m_val)
        print(f"{x_val:.2f}")
    else:
        x1_val = (-p_val - math.sqrt(D_val)) / (2 * m_val)
        x2_val = (-p_val + math.sqrt(D_val)) / (2 * m_val)
        print(f"{min(x1_val, x2_val):.2f} {max(x1_val, x2_val):.2f}")

# +
# 18

s_val: int = int(input())
u_val: int = int(input())
f_val: int = int(input())

s_val, u_val, f_val = sorted([s_val, u_val, f_val])

if f_val**2 == s_val**2 + u_val**2:
    print("100%")
elif f_val**2 > s_val**2 + u_val**2:
    print("велика")
else:
    print("крайне мала")

# +
# 19

n_val: float = float(input())
q_val: float = float(input())

on_island = n_val**2 + q_val**2 <= 100

condition_1 = 4 * q_val >= (n_val + 1) ** 2 - 36
condition_2 = q_val <= 5
condition_3 = n_val**2 + q_val**2 <= 25
condition_4 = 3 * q_val < 5 * n_val + 3

in_quicksand = condition_1 and condition_2 and condition_3 and condition_4

if not on_island:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif in_quicksand:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# +
# 20

input_1: str = input()
input_2: str = input()
input_3: str = input()

strings = [input_1, input_2, input_3]
query_2: str = "зайка"

bunny_strings = [s for s in strings if query_2 in s]

best_string = min(bunny_strings)

print(best_string, len(best_string))
