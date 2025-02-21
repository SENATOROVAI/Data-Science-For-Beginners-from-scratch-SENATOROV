"""Input and Output of Data: Operations and Formatting."""

# +
# 1

print("Привет, Яндекс!")

# +
# 2

user_name = input("Как Вас зовут?")
print(f"Привет, {user_name}")

# +
# 3

input_value = input()
print(f"{input_value}\n" * 3, end="")

# +
# 4

banknote_value = int(input())
total_expenses = 2.5 * 38
change = banknote_value - total_expenses
print(int(change))

# +
# 5

product_price_1 = int(input())
product_weight = int(input())
total_amount = int(input())

change = total_amount - (product_price_1 * product_weight)
print(int(change))

# +
# 6

product_name = input()
product_price_2 = int(input())
product_weight = int(input())
total_amount = int(input())

total_expenses = product_price_2 * product_weight
change = max(total_amount - total_expenses, 0)

print(
    "Чек\n"
    f"{product_name} - {product_weight}кг - {product_price_2}руб/кг\n"
    f"Итого: {total_expenses}руб\n"
    f"Внесено: {total_amount}руб\n"
    f"Сдача: {change}руб\n"
)

# +
# 7

counts = int(input())
print("Купи слона!\n" * counts, end="")

# +
# 8

counts = int(input())
punishment = input()
print(f'Я больше никогда не буду писать "{punishment}"!\n' * counts, end="")

# +
# 9

total_count = int(input())
total_minutes = int(input())

eaten_per_person = int((total_count * total_minutes) / 2)
print(eaten_per_person)

# +
# 10

first_name = input()
locker = int(input())

group = locker // 100
bed = locker // 10 % 10
child = locker % 10

print(
    f"""Группа №{group}.  
{child}. {first_name}.  
Шкафчик: {locker}.  
Кроватка: {bed}.
"""
)

# +
# 11

n_val = int(input())

d_val = n_val % 10
n_val //= 10
c_val = n_val % 10
n_val //= 10
b_val = n_val % 10
n_val //= 10
k_val = n_val

new_number = b_val * 1000 + k_val * 100 + d_val * 10 + c_val

print(new_number)

# +
# 12

a_val = int(input())
b_val = int(input())

result = 0
place = 1

while a_val > 0 or b_val > 0:
    digit_a = a_val % 10
    digit_b = b_val % 10

    sum_digit = (digit_a + digit_b) % 10

    result += sum_digit * place

    a_val //= 10
    b_val //= 10
    place *= 10

print(result)

# +
# 13

children_count = int(input())
candies_count = int(input())

received_per_children = candies_count // children_count
remainder = candies_count % children_count


print(received_per_children)
print(remainder)

# +
# 14

red_balls_count = int(input())
green_balls_count = int(input())
blue_balls_count = int(input())


max_attempts = red_balls_count + blue_balls_count + 1

print(max_attempts)

# +
# 15

order_hour = int(input())
order_minutes = int(input())
delivered_in_minutes = int(input())

deliver_minutes = order_minutes + delivered_in_minutes
deliver_hours = deliver_minutes // 60
deliver_minutes = deliver_minutes % 60

delivered_hour = (order_hour + deliver_hours) % 24
delivered_minutes = deliver_minutes

print(f"{delivered_hour:02d}:{delivered_minutes:02d}")

# +
# 16

warehouse_mileage = int(input())
shop_mileage = int(input())
average_speed = int(input())

delivery_time = (shop_mileage - warehouse_mileage) / average_speed

print(delivery_time)

# +
# 17

total_sum: int = int(input())
last_purchase: int = int(input(), 2)

profit: int = total_sum + last_purchase

print(profit)

# +
# 18

product_price_3: int = int(input(), 2)
banknote: int = int(input())

change = banknote - product_price_3

print(change)

# +
# 19

product = input()
price_per_kg = int(input())
weight = int(input())
money_given = int(input())

total_price = price_per_kg * weight
change = money_given - total_price

print(f"{'Чек':=^35}")
print(f"Товар:{product.rjust(29)}")
print(f"Цена:{str(weight) + 'кг * ' + str(price_per_kg) + 'руб/кг':>30}")
print(f"Итого:{str(total_price) + 'руб':>29}")
print(f"Внесено:{str(money_given) + 'руб':>27}")
print(f"Сдача:{str(change) + 'руб':>29}")
print("=" * 35)

# +
# 20

N_val: int = int(input())
M_val: int = int(input())
K1_val: int = int(input())
K2_val: int = int(input())

Total_Cost: int = M_val * N_val
x_val: int = (Total_Cost - (K2_val * N_val)) // (K1_val - K2_val)
y_val: int = N_val - x_val

print(x_val, y_val)
