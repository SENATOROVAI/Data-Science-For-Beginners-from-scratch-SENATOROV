"""Первый блок модуля."""

# +
# 1

print("Привет, мир!")

# +
# 2

user_name: str = "Анна"
print(f"Привет, {user_name}")

# +
# 3

message: str = "Привет"
print(f"{message}\n" * 3, end="")

# +
# 4

amount_paid: int = 100
price_per_item: float = 2.5
quantity: int = 38
total_cost: float = price_per_item * quantity
change: float = amount_paid - total_cost
print(int(change))

# +
# 5

cost_per_kg: int = 50
mass_kg: int = 3
money_given: int = 200

change_back: int = money_given - (cost_per_kg * mass_kg)
print(int(change_back))

# +
# 6

product_a: str = "Яблоки"
price_kg_a: int = 60
weight_a: int = 2
cash_a: int = 200

total_a: int = price_kg_a * weight_a
refund_a: int = max(cash_a - total_a, 0)

print(
    "Чек\n"
    f"{product_a} - {weight_a}кг - {price_kg_a}руб/кг\n"
    f"Итого к оплате: {total_a}руб\n"
    f"Внесено: {cash_a}руб\n"
    f"Сдача: {refund_a}руб\n"
)

# +
# 7

repetitions: int = 3
print("Купи слона!\n" * repetitions, end="")

# +
# 8

repeats: int = 2
phrase: str = "шоколад"

print(f'Я ни за что не буду выбирать "{phrase}"!\n' * repeats, end="")

# +
# 9

people_count: int = 4
minimum_expense: int = 100

ate_amount: int = (people_count * minimum_expense) // 2
print(ate_amount)

# +
# 10

name: str = "Иван"
locker_id: int = 234

group_id: int = locker_id // 100
bed_id: int = (locker_id // 10) % 10
list_pos: int = locker_id % 10

print(
    f"""Группа №{group_id}.
{list_pos}. {name}.
Шкафчик: {locker_id}.
Кроватка: {bed_id}.
"""
)

# +
# 11

value: int = 1234

digit4: int = value % 10
value //= 10
digit3: int = value % 10
value //= 10
digit2: int = value % 10
value //= 10
digit1: int = value

result: int = digit2 * 1000 + digit1 * 100 + digit4 * 10 + digit3
print(result)

# +
# 12

num_x: int = 123
num_y: int = 456

total: int = 0
place: int = 1

while num_x > 0 or num_y > 0:
    digit_x: int = num_x % 10
    digit_y: int = num_y % 10

    digit_val: int = (digit_x + digit_y) % 10

    total += digit_val * place

    num_x //= 10
    num_y //= 10
    place *= 10

print(total)

# +
# 13

kids_count: int = 2
candy_amount: int = 5

candies_each: int = candy_amount // kids_count
remaining: int = candy_amount % kids_count

print(candies_each)
print(remaining)

# +
# 14

red_count: int = 3
green_count: int = 2
blue_count: int = 4

attempts: int = red_count + blue_count + 1
print(attempts)

# +
# 15

hour: int = 10
minutes: int = 45
delay: int = 30

total_mins: int = minutes + delay
added_hours: int = total_mins // 60
result_minutes: int = total_mins % 60

result_hour: int = (hour + added_hours) % 24

print(f"{result_hour:02d}:{result_minutes:02d}")

# +
# 16

initial_km: int = 10
final_km: int = 50
velocity: int = 30

duration: float = (final_km - initial_km) / velocity
print(f"{duration:.2f}")

# +
# 17

total_prev: int = 150
last_code: int = int("1000", 2)

new_sum: int = total_prev + last_code
print(new_sum)

# +
# 18

binary_price: int = int("1010", 2)
paid_amount: int = 15

change_b: int = paid_amount - binary_price
print(change_b)

# +
# 19

item_label: str = "халва"
unit_price: int = 15
mass_kg_b: int = 10
money_in: int = 230

sum_cost: int = unit_price * mass_kg_b
rest_money: int = money_in - sum_cost

print(f"{'Чек':=^35}")
print(f"Товар:{item_label.rjust(29)}")
print(f"Цена:{f'{mass_kg_b}кг * {unit_price}руб/кг':>30}")
print(f"Итого:{f'{sum_cost}руб':>29}")
print(f"Внесено:{f'{money_in}руб':>27}")
print(f"Сдача:{f'{rest_money}руб':>29}")
print("=" * 35)

# +
# 20

load_weight: int = 40
avg_price: int = 22
price_x: int = 25
price_y: int = 18

overall_cost: int = avg_price * load_weight
kg_x: int = (overall_cost - price_y * load_weight) // (price_x - price_y)
kg_y: int = load_weight - kg_x

print(kg_x, kg_y)
