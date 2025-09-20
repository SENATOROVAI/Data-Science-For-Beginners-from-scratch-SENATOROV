"""2.2 Conditional operator."""

# +
# Знакомимся с пользователем
print("Как Вас зовут?")
username = input()
print(f"Здравствуйте, {username}!")

print("Как дела?")
mood = input()

if mood == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")

# +
# Кто быстрее?
petya_speed = int(input())
vasya_speed = int(input())

if petya_speed > vasya_speed:
    print("Петя")
else:
    print("Вася")

# +
# Кто быстрее на этот раз?
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    print("Петя")

elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    print("Вася")

else:
    print("Толя")

# +
# Список победителей
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    if vasya_speed > tolya_speed:
        first, second, third = "Петя", "Вася", "Толя"
    else:
        first, second, third = "Петя", "Толя", "Вася"

elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    if petya_speed > tolya_speed:
        first, second, third = "Вася", "Петя", "Толя"
    else:
        first, second, third = "Вася", "Толя", "Петя"

else:
    if vasya_speed > petya_speed:
        first, second, third = "Толя", "Вася", "Петя"
    else:
        first, second, third = "Толя", "Петя", "Вася"

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")

# +
# Яблоки
apples_for_petya = int(input())
apples_for_vasya = int(input())

petya_apples = 7
vasya_apples = 7

petya_apples -= 3
vasya_apples -= 3

vasya_apples += 5 - 2

petya_apples += apples_for_petya
vasya_apples += apples_for_vasya

if petya_apples > vasya_apples:
    print("Петя")
else:
    print("Вася")

# +
# Сила прокрастинации
year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print("YES")
elif year % 400 == 0:
    print("YES")
else:
    print("NO")
# -

# А роза упала на лапу Азора
text = input()
if text == text[::-1]:
    print("YES")
else:
    print("NO")

# Зайка — 1
text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")

# Первому игроку приготовиться
name1 = input()
name2 = input()
name3 = input()
if name1 < name2 and name1 < name3:
    print(name1)
elif name2 < name1 and name2 < name3:
    print(name2)
else:
    print(name3)

# +
# Лучшая защита — шифрование
number = int(input())
left_numeral = number // 100
medium_numeral = number // 10 % 10
right_numeral = number % 10

code_part1 = medium_numeral + right_numeral
code_part2 = left_numeral + medium_numeral

if code_part1 >= code_part2:
    print(f"{code_part1}{code_part2}")
else:
    print(f"{code_part2}{code_part1}")

# +
#  Красота спасёт мир
number = int(input())
left_numeral = number // 100
medium_numeral = number // 10 % 10
right_numeral = number % 10

min_numberal = left_numeral
mid_numeral = medium_numeral
max_numeral = right_numeral

if left_numeral <= medium_numeral <= right_numeral:
    min_numberal = left_numeral
    mid_numeral = medium_numeral
    max_numeral = right_numeral
elif left_numeral <= right_numeral <= medium_numeral:
    min_numberal = left_numeral
    mid_numeral = right_numeral
    max_numeral = medium_numeral
elif medium_numeral <= left_numeral <= right_numeral:
    min_numberal = medium_numeral
    mid_numeral = left_numeral
    max_numeral = right_numeral
elif medium_numeral <= right_numeral <= left_numeral:
    min_numberal = medium_numeral
    mid_numeral = right_numeral
    max_numeral = left_numeral
elif right_numeral <= left_numeral <= medium_numeral:
    min_numberal = right_numeral
    mid_numeral = left_numeral
    max_numeral = medium_numeral
else:
    min_numberal = right_numeral
    mid_numeral = medium_numeral
    max_numeral = left_numeral

if min_numberal + max_numeral == mid_numeral * 2:
    print("YES")
else:
    print("NO")

# +
# Музыкальный инструмент
pipe1_length = int(input())
pipe2_length = int(input())
pipe3_length = int(input())

condition1 = pipe1_length + pipe2_length > pipe3_length
condition2 = pipe1_length + pipe3_length > pipe2_length
condition3 = pipe2_length + pipe3_length > pipe1_length
if condition1 and condition2 and condition3:
    print("YES")
else:
    print("NO")

# +
# Властелин Чисел: Братство общей цифры
elf_number = int(input())
gnome_number = int(input())
human_number = int(input())

elf_left_numeric = elf_number // 10
elf_right_numeric = elf_number % 10
gnome_left_numeric = gnome_number // 10
gnome_right_numeric = gnome_number % 10
human_left_numeric = human_number // 10
human_right_numeric = human_number % 10

if elf_left_numeric == gnome_left_numeric == human_left_numeric:
    print(elf_left_numeric)
else:
    print(elf_right_numeric)

# +
# Властелин Чисел: Две Башни
number = int(input())
left_numeral = number // 100
medium_numeral = number // 10 % 10
right_numeral = number % 10

min_numberal = left_numeral
mid_numeral = medium_numeral
max_numeral = right_numeral

if left_numeral <= medium_numeral <= right_numeral:
    min_numberal = left_numeral
    mid_numeral = medium_numeral
    max_numeral = right_numeral
elif left_numeral <= right_numeral <= medium_numeral:
    min_numberal = left_numeral
    mid_numeral = right_numeral
    max_numeral = medium_numeral
elif medium_numeral <= left_numeral <= right_numeral:
    min_numberal = medium_numeral
    mid_numeral = left_numeral
    max_numeral = right_numeral
elif medium_numeral <= right_numeral <= left_numeral:
    min_numberal = medium_numeral
    mid_numeral = right_numeral
    max_numeral = left_numeral
elif right_numeral <= left_numeral <= medium_numeral:
    min_numberal = right_numeral
    mid_numeral = left_numeral
    max_numeral = medium_numeral
else:
    min_numberal = right_numeral
    mid_numeral = medium_numeral
    max_numeral = left_numeral

if min_numberal == 0:
    print(f"{mid_numeral}{min_numberal}", end=" ")
else:
    print(f"{min_numberal}{mid_numeral}", end=" ")

print(f"{max_numeral}{mid_numeral}")

# +
# Властелин Чисел: Возвращение Цезаря
number1 = input()
number2 = input()
numerics = [int(numerical) for numerical in f"{number1}{number2}"]

max_numerical = max(numerics)
min_numberal = min(numerics)

numerics.remove(max_numerical)
numerics.remove(min_numberal)

mid_numeral = sum(numerics) % 10

print(f"{max_numerical}{mid_numeral}{min_numberal}")

# +
# Легенды велогонок возвращаются: кто быстрее?
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    if vasya_speed > tolya_speed:
        first, second, third = "Петя", "Вася", "Толя"
    else:
        first, second, third = "Петя", "Толя", "Вася"

elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    if petya_speed > tolya_speed:
        first, second, third = "Вася", "Петя", "Толя"
    else:
        first, second, third = "Вася", "Толя", "Петя"

else:
    if vasya_speed > petya_speed:
        first, second, third = "Толя", "Вася", "Петя"
    else:
        first, second, third = "Толя", "Петя", "Вася"

print(f"{first:^24}")
print(f"{second:^8}")
print(f"{' ' * 16}{third:^8}")
print("   II      I      III   ")

# +
# Корень зла
coef_a = float(input())
coef_b = float(input())
coef_c = float(input())

if coef_a == coef_b == coef_c == 0:
    print("Infinite solutions")
elif coef_a == coef_b == 0:
    print("No solution")
elif coef_a == 0:
    answer1 = -coef_c / coef_b
    print(f"{answer1:.02f}")
else:
    discriminant = coef_b**2 - 4 * coef_a * coef_c
    if discriminant == 0:
        answer1 = (-coef_b + discriminant**0.5) / (2 * coef_a)
        print(f"{answer1:.02f}")
    elif discriminant < 0:
        print("No solution")
    else:
        answer1 = (-coef_b + discriminant**0.5) / (2 * coef_a)
        answer2 = (-coef_b - discriminant**0.5) / (2 * coef_a)
        if answer1 < answer2:
            print(f"{answer1:.02f} {answer2:.02f}")
        else:
            print(f"{answer2:.02f} {answer1:.02f}")

# +
# Территория зла
pipes_length = sorted(int(input()) for _ in range(3))

pipes_not_max_square_sum = sum(map(lambda x: x**2, pipes_length[:2]))
pipes_max_square = pipes_length[-1] ** 2

if pipes_not_max_square_sum == pipes_max_square:
    print("100%")
elif pipes_not_max_square_sum < pipes_max_square:
    print("велика")
else:
    print("крайне мала")

# +
# Автоматизация безопасности
coord_x = float(input())
coord_y = float(input())

cond_1 = ((coord_x + 1) ** 2) / 4 - 9 <= coord_y
cond_2 = coord_y <= 5
cond_3 = coord_x**2 + coord_y**2 <= 25
cond_4 = coord_y <= (5 * coord_x + 35) / 3

is_danger_zone = cond_1 and cond_2 and cond_3 and cond_4

if coord_x**2 + coord_y**2 >= 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif is_danger_zone:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# +
# Зайка — 2
texts = [input() for _ in range(3)]

texts_with_zaika = {text: len(text) for text in texts if "зайка" in text}
text_min = min(texts_with_zaika, key=lambda x: x[0])

print(text_min, texts_with_zaika[text_min])
