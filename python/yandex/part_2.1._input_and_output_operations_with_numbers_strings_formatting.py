"""2.1 Input and output. Operations with numbers strings Formatting."""

# Привет, Яндекс!
print("Привет, Яндекс!")

# Привет, всем!
user_name = input("Как Вас зовут?")
print(f"Привет, {user_name}")

# Излишняя автоматизация
banknote = int(input())
print(banknote - int(2.5 * 38))

# Сдача
banknote = int(input())
print(banknote - int(2.5 * 38))

# Магазин
goods_price = int(input())
goods_weight = int(input())
user_money = int(input())
print(user_money - goods_weight * goods_price)

# +
# Чек
goods_name = input()
price_kg = int(input())
goods_weight = int(input())
user_money = int(input())
total_cost = price_kg * goods_weight
change = user_money - total_cost

print("Чек")
print(f"{goods_name} - {goods_weight}кг - {price_kg}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {user_money}руб")
print(f"Сдача: {change}руб")
# -

# Делу — время, потехе — час
count = int(input())
text = ("Купи слона!" + r"\count") * count
print(text)

# Наказание
count = int(input())
text_line = f'Я больше никогда не буду писать "{input()}"!'
text_final = (text_line + r"\count") * count
print(text_final)

# Деловая колбаса
children_count = int(input())
minutes_count = int(input())
print(children_count // 2 * minutes_count)

# +
# Детский сад — штаны на лямках
child_name = input()
locker_number = int(input())
group_number = locker_number // 100
bed_number = locker_number // 10 % 10
child_number = locker_number % 10

print(f"Группа №{group_number}.")
print(f"{child_number}. {child_name}.")
print(f"Шкафчик: {locker_number}.")
print(f"Кроватка: {bed_number}.")
# -

# Автоматизация игры
number = input()
print(f"{number[1]}{number[0]}{number[3]}{number[2]}")

# +
# Интересное сложение
number1 = int(input())
number2 = int(input())

left_numeral = str(number1 // 100 + number2 // 100)[-1]
medium_numeral = str(number1 // 10 % 10 + number2 // 10 % 10)[-1]
right_numeral = str(number1 % 10 + number2 % 10)[-1]

result_str = f"{left_numeral}{medium_numeral}{right_numeral}"
print(int(result_str))
# -

# Дед Мороз и конфеты
children_count = int(input())
candies_count = int(input())
print(candies_count // children_count)
print(candies_count % children_count)

# Шарики и ручки
red_count = int(input())
green_count = int(input())
blue_count = int(input())
print(red_count + blue_count + 1)

# +
# В ожидании доставки
order_hours = int(input())
order_minutes = int(input())
delivery_minutes_all = int(input())

all_time_minites = order_hours * 60 + order_minutes + delivery_minutes_all
delivery_minutes_all_today = all_time_minites % 1440
delivery_hours = delivery_minutes_all_today // 60
delivery_minutes = delivery_minutes_all_today % 60

print(f"{delivery_hours:02}:{delivery_minutes:02}")

# +
# Доставка
mark_a = int(input())
mark_b = int(input())
car_speed = int(input())

delivery_time = (mark_b - mark_a) / car_speed
print(f"{delivery_time:.2f}")
# -

# Ошибка кассового аппарата
current_total = int(input())
last_purchase_binary = input()
last_purchase_decimal = int(last_purchase_binary, 2)
total_revenue = current_total + last_purchase_decimal
print(total_revenue)

# Сдача 10
price_binary = input().strip()
payment_decimal = int(input())
price_decimal = int(price_binary, 2)
change = payment_decimal - price_decimal
print(change)

# +
# Украшение чека
product_name = input().strip()
price_per_kg = int(input())
weight = int(input())
money_given = int(input())

total_cost = price_per_kg * weight
change = money_given - total_cost
print_price = f"{weight}кг * {price_per_kg}руб/кг"

header = "================Чек================"
product_line = f"Товар:{product_name:>29}"
price_line = f"Цена:{print_price:>30}"
total_line = f"Итого:{total_cost:>26}руб"
paid_line = f"Внесено:{money_given:>24}руб"
change_line = f"Сдача:{change:>26}руб"
footer = "==================================="

print(header)
print(product_line)
print(price_line)
print(total_line)
print(paid_line)
print(change_line)
print(footer)

# +
# Мухи отдельно, котлеты отдельно
weight = int(input())
price_avg = int(input())
price1 = int(input())
price2 = int(input())

part1_weight = weight * (price_avg - price2) // (price1 - price2)
part2_weight = weight - part1_weight

print(part1_weight, part2_weight)
