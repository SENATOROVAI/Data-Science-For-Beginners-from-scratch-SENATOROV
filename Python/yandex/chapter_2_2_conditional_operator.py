"""Conditional operator."""

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

first_competitor_avg_speed: int = int(input())
second_competitor_avg_speed: int = int(input())

if first_competitor_avg_speed > second_competitor_avg_speed:
    print("Петя")
else:
    print("Вася")

# +
# 3

petya_speed: float = float(input())
vasya_speed: float = float(input())
tolya_speed: float = float(input())

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    print("Петя")
elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    print("Вася")
else:
    print("Толя")

# +
# 4

bike_path_length: int = 43872

first_comp_name: str = "Петя"
first_comp_speed = float(input())

second_comp_name: str = "Вася"
second_comp_speed = float(input())

third_comp_name: str = "Толя"
third_comp_speed = float(input())

if first_comp_speed < second_comp_speed:
    first_comp_speed, second_comp_speed = second_comp_speed, first_comp_speed
    first_comp_name, second_comp_name = second_comp_name, first_comp_name

if second_comp_speed < third_comp_speed:
    second_comp_speed, third_comp_speed = third_comp_speed, second_comp_speed
    second_comp_name, third_comp_name = third_comp_name, second_comp_name

if first_comp_speed < second_comp_speed:
    first_comp_speed, second_comp_speed = second_comp_speed, first_comp_speed
    first_comp_name, second_comp_name = second_comp_name, first_comp_name

print(f"1. {first_comp_name}")
print(f"2. {second_comp_name}")
print(f"3. {third_comp_name}")

# +
# 5

petya_num_apples: int = 7
vasya_num_apples: int = 6
tolya_num_apples: int = 0

N_gain: int = int(input())
M_gain: int = int(input())

vasya_num_apples += 3
petya_num_apples -= 3

petya_num_apples += 2
tolya_num_apples -= 2

vasya_num_apples += 5
tolya_num_apples -= 5

vasya_num_apples -= 2

petya_num_apples += N_gain
vasya_num_apples += M_gain

if petya_num_apples > vasya_num_apples:
    print("Петя")
else:
    print("Вася")

# +
# 6

year: int = int(input())

div_by_4: bool = year % 4 == 0
not_div_by_100: bool = year % 100 != 0
div_by_400: bool = year % 400 == 0

if div_by_4 and (not_div_by_100 or div_by_400):
    print("YES")
else:
    print("NO")

# +
# 7

sample_object: str = input()

if sample_object == sample_object[::-1]:
    print("YES")
else:
    print("NO")

# +
# 8

expression: str = input()
element: str = "зайка"

if element in expression:
    print("YES")
else:
    print("NO")

# +
# 9

player_1: str = input()
player_2: str = input()
player_3: str = input()

first_player: str = min(player_1, player_2, player_3)

print(first_player)

# +
# 10

password: int = int(input())

password_str: str = str(password)

sum_first = int(password_str[1]) + int(password_str[2])
sum_second = int(password_str[0]) + int(password_str[1])

max_sum: int = max(sum_first, sum_second)
min_sum: int = min(sum_first, sum_second)

encrypted_password: int = int(f"{max_sum}{min_sum}")

print(encrypted_password)

# +
# 11

number_1: int = int(input())

hundreds_1: int = number_1 // 100
tens_1: int = (number_1 // 10) % 10
units_1: int = number_1 % 10

min_digit_1 = min(hundreds_1, tens_1, units_1)
max_digit_1 = max(hundreds_1, tens_1, units_1)

middle_digit_1: int = hundreds_1 + tens_1 + units_1 - min_digit_1 - max_digit_1

if min_digit_1 + max_digit_1 == 2 * middle_digit_1:
    print("YES")
else:
    print("NO")

# +
# 12

first_side: int = int(input())
second_side: int = int(input())
third_side: int = int(input())

summa: int = first_side + second_side + third_side

if max(first_side, second_side, third_side) * 2 < summa:
    print("YES")
else:
    print("NO")

# +
# 13

elf: int = int(input())
gnome: int = int(input())
human: int = int(input())

tens_elf: int
units_elf: int
tens_gnome: int
units_gnome: int
tens_human: int
units_human: int
tens_elf, units_elf = elf // 10, elf % 10
tens_gnome, units_gnome = gnome // 10, gnome % 10
tens_human, units_human = human // 10, human % 10

if tens_elf == tens_gnome and tens_gnome == tens_human:
    print(tens_elf)
elif units_elf == units_gnome and units_gnome == units_human:
    print(units_elf)
else:
    print("NO")

# +
# 14

number_2: int = int(input())

hundreds_2: int = number_2 // 100
tens_2: int = (number_2 // 10) % 10
units_2: int = number_2 % 10

variations: list[int] = [
    hundreds_2 * 10 + tens_2,
    hundreds_2 * 10 + units_2,
    tens_2 * 10 + hundreds_2,
    tens_2 * 10 + units_2,
    units_2 * 10 + hundreds_2,
    units_2 * 10 + tens_2,
]

valid_variations: list[int] = [val for val in variations if val >= 10]

min_val: int = min(valid_variations)
max_val: int = max(valid_variations)

print(min_val, max_val)

# +
# 15

number_3: int = int(input())
number_4: int = int(input())

digit_1: int = number_3 // 100 if number_3 >= 100 else -1
digit_2: int = (number_3 // 10) % 10
digit_3: int = number_3 % 10
digit_4: int = number_4 // 100 if number_4 >= 100 else -1
digit_5: int = (number_4 // 10) % 10
digit_6: int = number_4 % 10

digits: list[int] = [
    d for d in (digit_1, digit_2, digit_3, digit_4, digit_5, digit_6) if d >= 0
]

max_digit_2: int = max(digits)
min_digit_2: int = min(digits)
total: int = sum(digits)

middle_digit_2: int = (total - max_digit_2 - min_digit_2) % 10

print(f"{max_digit_2}{middle_digit_2}{min_digit_2}")

# +
# 16

petya: int = int(input())
vasya: int = int(input())
tolya: int = int(input())


first: int = max(petya, vasya, tolya)
third: int = min(petya, vasya, tolya)
second: int = petya + vasya + tolya - first - third

if first == petya:
    first_name = "Петя"
elif first == vasya:
    first_name = "Вася"
else:
    first_name = "Толя"

if second == petya:
    second_name = "Петя"
elif second == vasya:
    second_name = "Вася"
else:
    second_name = "Толя"

if third == petya:
    third_name = "Петя"
elif third == vasya:
    third_name = "Вася"
else:
    third_name = "Толя"


print(f"{first_name: ^24}")
print(f'{second_name: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_name: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')

# +
# 17


coef_a: float = float(input())
coef_b: float = float(input())
coef_c: float = float(input())

if coef_a == 0:
    if coef_b == 0:
        print("Infinite solutions" if coef_c == 0 else "No solution")
    else:
        root = -coef_c / coef_b
        print(f"{root:.2f}")
else:
    discriminant: float = coef_b**2 - 4 * coef_a * coef_c
    if discriminant < 0:
        print("No solution")
    elif discriminant == 0:
        single_root = -coef_b / (2 * coef_a)
        print(f"{single_root:.2f}")
    else:
        sqrt_d = math.sqrt(discriminant)
        root_1 = (-coef_b - sqrt_d) / (2 * coef_a)
        root_2 = (-coef_b + sqrt_d) / (2 * coef_a)
        print(f"{min(root_1, root_2):.2f} {max(root_1, root_2):.2f}")

# +
# 18

side1: int = int(input())
side2: int = int(input())
hypotenuse: int = int(input())

side1, side2, hypotenuse = sorted([side1, side2, hypotenuse])

sum_of_squares: int = side1**2 + side2**2
hypotenuse_squared: int = hypotenuse**2

if hypotenuse_squared == sum_of_squares:
    print("100%")
elif hypotenuse_squared > sum_of_squares:
    print("велика")
else:
    print("крайне мала")

# +
# 19

x_coord = float(input())
y_coord = float(input())

conditions: list[bool] = [
    x_coord**2 + y_coord**2 <= 100,
    y_coord <= 5,
    4 * y_coord >= (x_coord + 1) ** 2 - 36,
    x_coord**2 + y_coord**2 <= 25,
    3 * y_coord < 5 * x_coord + 3,
]

in_quicksand: bool = all(conditions[1:5])

if not conditions[0]:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif in_quicksand:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# +
# 20

line_1: str = input()
line_2: str = input()
line_3: str = input()

if line_1 > line_2:
    line_1, line_2 = line_2, line_1
if line_1 > line_3:
    line_1, line_3 = line_3, line_1
if line_2 > line_3:
    line_2, line_3 = line_3, line_2

if "зайка" in line_1:
    print(line_1, len(line_1))
elif "зайка" in line_2:
    print(line_2, len(line_2))
elif "зайка" in line_3:
    print(line_3, len(line_3))
