"""2.5 Strings, tuples, lists."""

# +
# Азбука
# Польский калькулятор

count = int(input())
is_all_correct = True
allowed_letters = ("а", "б", "в")

for _ in range(count):
    word = input()
    if not word.startswith(allowed_letters):
        is_all_correct = False

print("YES" if is_all_correct else "NO")
# -

# Кручу-верчу
text = input()
for symbol in text:
    print(symbol)

# +
# Анонс новости
title_len = int(input())
count_title = int(input())

for _ in range(count_title):
    title = input()
    if len(title) <= title_len:
        print(title)
    else:
        print(f"{title[:title_len - 3]}...")
# -

# Очистка данных
text = input().strip()
while text:
    if text.startswith("##"):
        text = text[2:]

    if text.endswith("@@@"):
        text = input().strip()
        continue

    print(text)

    text = input().strip()

# А роза упала на лапу Азора 4.0
text = input()
print("YES" if text == text[::-1] else "NO")

# Зайка — 6
count_areas = int(input())
count_res = 0
for _ in range(count_areas):
    count_res += input().split().count("зайка")
print(count_res)

# А и Б сидели на трубе
print(sum(map(int, input().split())))

# Зайка — 7
count_areas = int(input())
for _ in range(count_areas):
    text = input()
    index = text.find("зайка")
    if index == -1:
        print("Заек нет =(")
    else:
        print(index + 1)

# Без комментариев
text = input()
while text:
    index = text.find("#")

    if index == -1:
        print(text)

    else:
        need_text = text[:index]

        if need_text:
            print(need_text)
    text = input()

# +
# Частотный анализ на минималках
text = input()
dict_symbols: dict[str, int] = {}

while text != "ФИНИШ":
    text = text.lower().replace(" ", "")
    for symbol in text:
        dict_symbols[symbol] = dict_symbols.get(symbol, 0) + 1

    text = input()

need_k = ""
max_v = 0

for key, value in dict_symbols.items():
    if value > max_v:
        need_k = key
        max_v = value
print(need_k)

# +
# Найдётся всё
count_text = int(input())
texts = []
for _ in range(count_text):
    text = input()
    texts.append(text)

find_text = input()
for text in texts:
    if find_text.lower() in text.lower():
        print(text)

# +
# Меню питания
count_days = int(input())
porridge = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

for day in range(count_days):
    print(porridge[day % 5])

# +
# Массовое возведение в степень
count_numbers = int(input())
numbers = [int(input()) for _ in range(count_numbers)]
power = int(input())

print(*[number**power for number in numbers], sep="\n")
# -

# Массовое возведение в степень 2.0
numbers = list(map(int, input().split()))
power = int(input())
numbers_power = " ".join([str(number**power) for number in numbers])
print(numbers_power)

# +
# НОД 3.0


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


numbers = list(map(int, input().split()))
number1 = numbers[0]
for index in range(1, len(numbers)):
    number2 = numbers[index]
    number1 = get_gcd(number1, number2)
print(number1)

# +
# Анонс новости 2.0
max_length = int(input())
lines = []

for _ in range(int(input())):
    lines.append(input())

for line in lines:
    if max_length > 3:
        if len(line) >= max_length - 3:
            line = line[: max_length - 3] + "..."
        else:
            if max_length == 4:
                line = line + "..."

        print(line)
        max_length -= len(line)
# -

# А роза упала на лапу Азора 5.0
text = input().lower().replace(" ", "")
print("YES" if text == text[::-1] else "NO")

# +
# RLE
text = input()

value_str = text[0]
count_value = 0
rle_list = []

for symbol in text:  # Используем прямую итерацию вместо enumerate
    if symbol == value_str:
        count_value += 1
    else:
        rle_list.append([value_str, count_value])
        value_str = symbol
        count_value = 1

rle_list.append([value_str, count_value])

for rle in rle_list:
    print(*rle)

# +
# Польский калькулятор с унарными и тернарными операциями


def factorial(nmb: int) -> int:
    """Return the factorial of a number."""
    rsl: int = 1
    for multiplier_val in range(2, nmb + 1):
        rsl *= multiplier_val
    return rsl


expression_value: str = input().strip()
tokens: list[str] = expression_value.split()

stack: list[int] = []

for token in tokens:
    if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
        stack.append(int(token))
    elif token in {"+", "-", "*", "/"}:
        b_val: int = stack.pop()
        a_val: int = stack.pop()
        if token == "+":
            stack.append(a_val + b_val)
        elif token == "-":
            stack.append(a_val - b_val)
        elif token == "*":
            stack.append(a_val * b_val)
        elif token == "/":
            stack.append(a_val // b_val)
    elif token == "~":
        stack.append(-stack.pop())
    elif token == "!":
        stack.append(factorial(stack.pop()))
    elif token == "#":
        stack_value: int = stack[-1]
        stack.append(stack_value)
    elif token == "@":
        first: int = stack.pop()
        second: int = stack.pop()
        third: int = stack.pop()
        stack.extend([second, first, third])

print(stack.pop())
