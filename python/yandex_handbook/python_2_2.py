"""Yandex handbook "Python Basics" answers."""
import math

# +
# 1
user_greeting: str = "Анна"
print(f"Здравствуйте, {user_greeting}!")
mood_reply: str = "плохо"

if mood_reply == "хорошо":
    print("Я за вас рада!")
else:
    print("Всё наладится!")

# +
# 2
distance_total: int = 43872

speed_petya: int = 120
speed_vasya: int = 100

if speed_petya > speed_vasya:
    print("Петя")
else:
    print("Вася")

# +
# 3
speed_1: float = 8.5
speed_2: float = 9.0
speed_3: float = 10.2

if speed_1 > speed_2 and speed_1 > speed_3:
    print("Петя")
elif speed_2 > speed_1 and speed_2 > speed_3:
    print("Вася")
else:
    print("Толя")

# +
# 4
track_length: int = 43872

racer_a: str = "Петя"
speed_a: float = 8.5

racer_b: str = "Вася"
speed_b: float = 9.2

racer_c: str = "Толя"
speed_c: float = 8.9

if speed_a < speed_b:
    speed_a, speed_b = speed_b, speed_a
    racer_a, racer_b = racer_b, racer_a

if speed_b < speed_c:
    speed_b, speed_c = speed_c, speed_b
    racer_b, racer_c = racer_c, racer_b

if speed_a < speed_b:
    speed_a, speed_b = speed_b, speed_a
    racer_a, racer_b = racer_b, racer_a

print(f"1. {racer_a}")
print(f"2. {racer_b}")
print(f"3. {racer_c}")

# +
# 5
apples_p: int = 7
apples_v: int = 6
apples_t: int = 0

gain_n: int = 4
gain_m: int = 1

apples_v += 3
apples_p -= 3

apples_p += 2
apples_t -= 2

apples_v += 5
apples_t -= 5

apples_v -= 2

apples_p += gain_n
apples_v += gain_m

if apples_p > apples_v:
    print("Петя")
else:
    print("Вася")

# +
# 6
year_val: int = 1900

is_div4: bool = year_val % 4 == 0
is_not_div100: bool = year_val % 100 != 0
is_div400: bool = year_val % 400 == 0

if is_div4 and (is_not_div100 or is_div400):
    print("YES")
else:
    print("NO")

# +
# 7
text_sample: str = "топот"

if text_sample == text_sample[::-1]:
    print("YES")
else:
    print("NO")

# +
# 8
phrase: str = "зайка в лесу"

if "зайка" in phrase:
    print("YES")
else:
    print("NO")

# +
# 9
contestant_a: str = "Виталий"
contestant_b: str = "Анна"
contestant_c: str = "Борис"

earliest_name: str = min(contestant_a, contestant_b, contestant_c)
print(earliest_name)

# +
# 10
code_val: int = 561

code_text: str = str(code_val)

sum_a: int = int(code_text[1]) + int(code_text[2])
sum_b: int = int(code_text[0]) + int(code_text[1])

high_sum: int = max(sum_a, sum_b)
low_sum: int = min(sum_a, sum_b)

result_code: int = int(f"{high_sum}{low_sum}")
print(result_code)

# +
# 11
value_1: int = 123

hundreds_a: int = value_1 // 100
tens_a: int = (value_1 // 10) % 10
units_a: int = value_1 % 10

min_dig_a: int = min(hundreds_a, tens_a, units_a)
max_dig_a: int = max(hundreds_a, tens_a, units_a)

mid_dig_a: int = hundreds_a + tens_a + units_a - min_dig_a - max_dig_a

if min_dig_a + max_dig_a == 2 * mid_dig_a:
    print("YES")
else:
    print("NO")

# +
# 12
side_a: int = 3
side_b: int = 4
side_c: int = 5

perimeter: int = side_a + side_b + side_c

if max(side_a, side_b, side_c) * 2 < perimeter:
    print("YES")
else:
    print("NO")

# +
# 13
score_elf: int = 12
score_gnome: int = 15
score_human: int = 18

tens_e: int = score_elf // 10
units_e: int = score_elf % 10
tens_g: int = score_gnome // 10
units_g: int = score_gnome % 10
tens_h: int = score_human // 10
units_h: int = score_human % 10

if tens_e == tens_g == tens_h:
    print(tens_e)
elif units_e == units_g == units_h:
    print(units_e)
else:
    print("NO")

# +
# 14
num_val: int = 103

hundreds_b: int = num_val // 100
tens_b: int = (num_val // 10) % 10
units_b: int = num_val % 10

candidates: list[int] = [
    hundreds_b * 10 + tens_b,
    hundreds_b * 10 + units_b,
    tens_b * 10 + hundreds_b,
    tens_b * 10 + units_b,
    units_b * 10 + hundreds_b,
    units_b * 10 + tens_b,
]

filtered_vals: list[int] = [x for x in candidates if x >= 10]

lowest: int = min(filtered_vals)
highest: int = max(filtered_vals)

print(lowest, highest)

# +
# 15
val_a: int = 34
val_b: int = 123

d1: int = val_a // 100 if val_a >= 100 else -1
d2: int = (val_a // 10) % 10
d3: int = val_a % 10
d4: int = val_b // 100 if val_b >= 100 else -1
d5: int = (val_b // 10) % 10
d6: int = val_b % 10

digit_list: list[int] = [d for d in (d1, d2, d3, d4, d5, d6) if d >= 0]

max_d: int = max(digit_list)
min_d: int = min(digit_list)
sum_d: int = sum(digit_list)

mid_d: int = (sum_d - max_d - min_d) % 10

print(f"{max_d}{mid_d}{min_d}")

# +
# 16
score_p: int = 85
score_v: int = 92
score_t: int = 98

top: int = max(score_p, score_v, score_t)
last: int = min(score_p, score_v, score_t)
mid: int = score_p + score_v + score_t - top - last

first_place: str
if top == score_p:
    first_place = "Петя"
elif top == score_v:
    first_place = "Вася"
else:
    first_place = "Толя"

second_place: str
if mid == score_p:
    second_place = "Петя"
elif mid == score_v:
    second_place = "Вася"
else:
    second_place = "Толя"

third_place: str
if last == score_p:
    third_place = "Петя"
elif last == score_v:
    third_place = "Вася"
else:
    third_place = "Толя"

print(f"{first_place: ^24}")
print(f'{second_place: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_place: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')

# +
# 17
a_val: float = 1.0
b_val: float = 2.0
c_val: float = 3.0

if a_val == 0:
    if b_val == 0:
        print("Infinite solutions" if c_val == 0 else "No solution")
    else:
        sol: float = -c_val / b_val
        print(f"{sol:.2f}")
else:
    disc: float = b_val**2 - 4 * a_val * c_val
    if disc < 0:
        print("No solution")
    elif disc == 0:
        root_val: float = -b_val / (2 * a_val)
        print(f"{root_val:.2f}")
    else:
        sqrt_disc: float = math.sqrt(disc)
        r1: float = (-b_val - sqrt_disc) / (2 * a_val)
        r2: float = (-b_val + sqrt_disc) / (2 * a_val)
        print(f"{min(r1, r2):.2f} {max(r1, r2):.2f}")

# +
# 18
leg_a: int = 5
leg_b: int = 6
hyp_side: int = 7

leg_a, leg_b, hyp_side = sorted([leg_a, leg_b, hyp_side])

squares_sum: int = leg_a**2 + leg_b**2
hyp_sq: int = hyp_side**2

if hyp_sq == squares_sum:
    print("100%")
elif hyp_sq > squares_sum:
    print("велика")
else:
    print("крайне мала")

# +
# 19
x_val: float = 2.0
y_val: float = 3.0

checks: list[bool] = [
    x_val**2 + y_val**2 <= 100,
    y_val <= 5,
    4 * y_val >= (x_val + 1) ** 2 - 36,
    x_val**2 + y_val**2 <= 25,
    3 * y_val < 5 * x_val + 3,
]

in_danger_zone: bool = all(checks[1:5])

if not checks[0]:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif in_danger_zone:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# +
# 20
text_a: str = "березка зайка"
text_b: str = "ель"
text_c: str = "сосна"

if text_a > text_b:
    text_a, text_b = text_b, text_a
if text_a > text_c:
    text_a, text_c = text_c, text_a
if text_b > text_c:
    text_b, text_c = text_c, text_b

if "зайка" in text_a:
    print(text_a, len(text_a))
elif "зайка" in text_b:
    print(text_b, len(text_b))
elif "зайка" in text_c:
    print(text_c, len(text_c))
