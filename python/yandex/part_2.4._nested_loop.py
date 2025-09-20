"""2.4 Nested loop."""

# +
# Таблица умножения
size = int(input())

for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(row * col, end=" ")
    print()
# -

# Не таблица умножения
size = int(input())
for second in range(1, size + 1):
    for first in range(1, size + 1):
        print(f"{first} * {second} = {first * second}")

# Новогоднее настроение
count_numbers = int(input())
number = 1
row = 1
col = 1
while number <= count_numbers:
    print(number, end=" ")
    number += 1

    col += 1
    if col > row:
        print()
        col = 1
        row += 1

# Суммарная сумма
count_numbers = int(input())
amount = 0
for _ in range(count_numbers):
    amount += sum(map(int, list(input())))
print(amount)

# Зайка — 5
count_areas = int(input())
count_need_areas = 0
for _ in range(count_areas):
    need_word = False
    word = input()
    while word != "ВСЁ":
        if word == "зайка":
            need_word = True
        word = input()
    count_need_areas += need_word
print(count_need_areas)

# +
# НОД 2.0


def get_gcd(n1: int, n2: int) -> int:
    """Find gcd.

    Args:
        number1 (int): first number
        number2 (int): second_number

    Returns:
        int: gcd
    """
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return int(n1)


count_numbers = int(input())
number1 = int(input())
for _ in range(count_numbers - 1):
    number2 = int(input())
    number1 = get_gcd(number1, number2)
print(number1)

# +
# На старт! Внимание! Марш!
count_people = int(input())
count_time = 3

for number_start in range(1, count_people + 1):
    for sec in range(count_time, 0, -1):
        print(f"До старта {sec} секунд(ы)")
    print(f"Старт {number_start}!!!")
    count_time += 1
# -

# Максимальная сумма
name_win = ""
max_sum_numeric = 0
count_children = int(input())
for _ in range(count_children):
    name = input()
    sum_numerics = sum(map(int, list(input())))
    if sum_numerics >= max_sum_numeric:
        name_win = name
        max_sum_numeric = sum_numerics
print(name_win)

# Большое число
answer = ""
count_children = int(input())
for _ in range(count_children):
    max_numeric = max(map(int, list(input())))
    answer += str(max_numeric)
print(answer)

# Мы делили апельсин
count_parts = int(input())
print("А Б В")
for anya in range(1, count_parts - 1):
    for borya in range(1, count_parts - anya):
        vova = count_parts - anya - borya
        print(anya, borya, vova)

# +
# Простая задача 3.0
count_numbers = int(input())
count_need_numbers = 0
for _ in range(count_numbers):
    number = int(input())

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            break
    else:
        if number >= 2:
            count_need_numbers += 1

print(count_need_numbers)
# -

# Числовой прямоугольник
n_area = int(input())
m_area = int(input())
number = 1
width = len(str(n_area * m_area))
for row in range(n_area):
    for col in range(m_area):
        print(f"{number:>{width}}", end=" ")
        number += 1
    print()

# Числовой прямоугольник 2.0
n_area = int(input())
m_area = int(input())
number = 1
width = len(str(n_area * m_area))
for row in range(n_area):
    for col in range(m_area):
        print(f"{number:>{width}}", end=" ")
        number += n_area
    print()
    number -= n_area * (m_area) - 1

# Числовая змейка
n_area = int(input())
m_area = int(input())
number = 1
width = len(str(n_area * m_area))
for row in range(n_area):
    for col in range(m_area):
        number = (
            (row * m_area + col + 1) if row % 2 == 0 else (row * m_area + m_area - col)
        )
        print(f"{number:>{width}}", end=" ")
    print()

# Числовая змейка 2.0
# Числовая змейка
n_area = int(input())
m_area = int(input())
number = 1
width = len(str(n_area * m_area))
for row in range(n_area):
    for col in range(m_area):
        number = (
            (col * n_area + row + 1) if col % 2 == 0 else (col * n_area + n_area - row)
        )
        print(f"{number:>{width}}", end=" ")
    print()

# +
# Редизайн таблицы умножения
size = int(input())
width = int(input())

for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(f"{row * col:^{width}}", end="")
        if size * row != row * col:
            print("|", end="")
    print()
    if row != size:
        print("-" * (width * size + size - 1))
# -

# А роза упала на лапу Азора 3.0
count_numbers = int(input())
count = 0
for _ in range(count_numbers):
    number_str = input()
    if number_str == number_str[::-1]:
        count += 1
print(count)

# +
count_numbers = int(input())

rows = 0
total_used = 0

while total_used < count_numbers:
    rows += 1
    total_used += rows

lines = []
current_num = 1

for row in range(1, rows + 1):
    row_numbers = []
    numbers_in_row = min(row, count_numbers - current_num + 1)

    for _ in range(numbers_in_row):
        row_numbers.append(str(current_num))
        current_num += 1

    line = " ".join(row_numbers)
    lines.append(line)

    if current_num > count_numbers:
        break

max_width = len(lines[-1])

for line in lines:
    print(f"{line:^{max_width}}")
# -

size = int(input())
width = len(str(size // 2 + 1))
for row in range(size):
    for col in range(size):
        num1 = min(row - 0, abs(row - (size - 1))) + 1
        num2 = min(col - 0, abs(col - (size - 1))) + 1
        num = min(num1, num2)
        print(f"{num:>{width}}", end=" ")
    print()

# Математическая выгода
start_number = int(input())
max_result = 0
top_notation = 2
for notation in range(2, 11):
    number = start_number
    total = 0
    while number:
        total += number % notation
        number //= notation
    if total > max_result:
        max_result = total
        top_notation = notation
print(top_notation)
