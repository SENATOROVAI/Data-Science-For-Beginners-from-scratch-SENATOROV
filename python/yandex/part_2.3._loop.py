"""2.3 Loop."""

# Раз, два, три! Ёлочка, гори!
text = input()
while text != "Три!":
    print("Режим ожидания...")
    text = input()
print("Ёлочка, гори!")

# Зайка — 3
text = input()
count_word = 0
while text != "Приехали!":
    if "зайка" in text:
        count_word += 1
    text = input()
print(count_word)

# +
# Считалочка
start = int(input())
end = int(input())

for number in range(start, end + 1):
    print(number, end=" ")

# +
# Считалочка 2.0
start = int(input())
end = int(input())

step = 1 if start <= end else -1
for number in range(start, end + step, step):
    print(number, end=" ")
# -

# Внимание! Акция!
cost = float(input())
total_cost = 0.0
while cost != 0:
    if cost >= 500:
        cost *= 0.9
    total_cost += cost

    cost = float(input())
print(total_cost)

# +
# НОД
number1 = int(input())
number2 = int(input())

while number2 != 0:
    number1, number2 = number2, number1 % number2
print(abs(number1))

# +
# НОК


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


number1 = int(input())
number2 = int(input())
gcd = get_gcd(number1, number2)
print(number1 * number2 // gcd)

# +
# Излишняя автоматизация 2.0
text = input()
repeat_count = int(input())

for _ in range(repeat_count):
    print(text)
# -

# Факториал
number = int(input())
result = 1
for multiplier in range(1, number + 1):
    result *= multiplier
print(result)

# +
# Маршрут построен
coord_x = 0
coord_y = 0

digit = input()
while digit != "СТОП":
    count_step = int(input())

    if digit == "СЕВЕР":
        coord_y += count_step
    elif digit == "ЮГ":
        coord_y -= count_step
    elif digit == "ВОСТОК":
        coord_x += count_step
    else:
        coord_x -= count_step

    digit = input()

print(coord_y)
print(coord_x)
# -

# Цифровая сумма
number_str = input()
amount = 0
for numerical in number_str:
    amount += int(numerical)
    print(numerical)
print(amount)

# Сильная цифра
number_str = input()
max_number = max(number_str)
print(max_number)

# Первому игроку приготовиться 2.0
count_people = int(input())
first_player = min(input() for _ in range(count_people))
print(first_player)

# +
number = int(input())

for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        print("NO")
        break
else:
    if number < 2:
        print("NO")
    else:
        print("YES")
# -

# Зайка - 4
count_text = int(input())
count = 0
for _ in range(count_text):
    text = input()
    if "зайка" in text:
        count += 1
print(count)

# А роза упала на лапу Азора 2.0
number_str = input()
if number_str[::-1] == number_str:
    print("YES")
else:
    print("NO")

# +
# Чётная чистота
number_str = input()
answer = ""
for digit in number_str:
    if int(digit) % 2 != 0:
        answer += digit

print(answer)

# +
# Простая задача 2.0
number = int(input())
multipliers = []
divisor = 2

while divisor * divisor <= number:
    while number % divisor == 0:
        multipliers.append(str(divisor))
        number //= divisor
    divisor += 1

if number > 1:
    multipliers.append(str(number))

print(" * ".join(multipliers))

# +
# Игра в «Угадайку»
low, high = 1, 1000
attempts = 0

while attempts < 10:
    guess = (low + high) // 2
    print(guess)
    response = input().strip()

    if response == "Угадал!":
        break
    if response == "Больше":
        low = guess + 1
    elif response == "Меньше":
        high = guess - 1

    attempts += 1
# -

# Хайпанём немножечко!
count_hash = int(input())
prev_hash = 0
for i in range(count_hash):
    b_n = int(input())

    h_n = b_n % 256
    r_n = (b_n // 256) % 256
    m_n = b_n // (256**2)
    correct_hash = (37 * (m_n + r_n + prev_hash)) % 256

    if h_n >= 100 or h_n != correct_hash:
        print(i)
        break

    prev_hash = h_n
else:
    print(-1)
