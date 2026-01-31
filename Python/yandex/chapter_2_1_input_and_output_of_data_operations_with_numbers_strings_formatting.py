"""Input and Output of Data: Operations and Formatting."""

# +
# 1

print("Привет, мир!")

# +
# 2

user_name: str = input("Как Вас зовут?")
print(f"Привет, {user_name}")

# +
# 3

input_value: str = input()
print(f"{input_value}\n" * 3, end="")

# +
# 4

inserted_amount: int = int(input())
item_price: float = 2.5
item_quantity: int = 38
total_outlay: float = item_price * item_quantity
remaining_change: float = inserted_amount - total_outlay
print(int(remaining_change))

# +
# 5

price_per_kg_1: int = int(input())
weight_in_kg: int = int(input())
amount_paid: int = int(input())

refund_amount: int = amount_paid - (price_per_kg_1 * weight_in_kg)
print(int(refund_amount))

# +
# 6

item_name: str = input()
price_per_kg_2: int = int(input())
weight_kg: int = int(input())
amount_given: int = int(input())

total_sum: int = price_per_kg_2 * weight_kg
change_due: int = max(amount_given - total_sum, 0)

print(
    "Чек\n"
    f"{item_name} - {weight_kg}кг - {price_per_kg_2}руб/кг\n"
    f"Итого к оплате: {total_sum}руб\n"
    f"Внесено: {amount_given}руб\n"
    f"Сдача: {change_due}руб\n"
)

# +
# 7

counts: int = int(input())
print("Купи слона!\n" * counts, end="")

# +
# 8

tally: int = int(input())
punishment: str = input()
print(f'Я ни за что не буду выбирать "{punishment}"!\n' * tally, end="")

# +
# 9

num_people: int = int(input())
min_spent: int = int(input())

person_ate: int = int((num_people * min_spent) / 2)
print(person_ate)

# +
# 10

first_name: str = input()
locker_number: int = int(input())

group_number: int = locker_number // 100
bed_number: int = (locker_number // 10) % 10
child_number_in_list: int = locker_number % 10

print(
    f"""Группа №{group_number}.  
{child_number_in_list}. {first_name}.  
Шкафчик: {locker_number}.  
Кроватка: {bed_number}.
"""
)

# +
# 11

original_number: int = int(input())

last_digit: int = original_number % 10
original_number //= 10
third_digit: int = original_number % 10
original_number //= 10
second_digit: int = original_number % 10
original_number //= 10
first_digit: int = original_number

rearranged_number: int = (
    second_digit * 1000 + first_digit * 100 + last_digit * 10 + third_digit
)

print(rearranged_number)

# +
# 12

number_a: int = int(input())
number_b: int = int(input())

final_sum: int = 0
digit_place: int = 1

while number_a > 0 or number_b > 0:
    last_digit_a: int = number_a % 10
    last_digit_b: int = number_b % 10

    digit_sum: int = (last_digit_a + last_digit_b) % 10

    final_sum += digit_sum * digit_place

    number_a //= 10
    number_b //= 10
    digit_place *= 10

print(final_sum)

# +
# 13

num_children: int = int(input())
total_candies: int = int(input())

candies_per_child: int = total_candies // num_children
leftover_candies: int = total_candies % num_children

print(candies_per_child)
print(leftover_candies)

# +
# 14

num_red_balls: int = int(input())
num_green_balls: int = int(input())
num_blue_balls: int = int(input())

max_tries: int = num_red_balls + num_blue_balls + 1

print(max_tries)

# +
# 15

order_hour: int = int(input())
order_minutes: int = int(input())
wait_minutes: int = int(input())

total_minutes: int = order_minutes + wait_minutes
extra_hour: int = total_minutes // 60
final_minutes: int = total_minutes % 60

final_hour: int = (order_hour + extra_hour) % 24

print(f"{final_hour:02d}:{final_minutes:02d}")

# +
# 16

start_km: int = int(input())
end_km: int = int(input())
speed: int = int(input())

travel_time: float = (end_km - start_km) / speed

print(f"{travel_time:.2f}")

# +
# 17

current_total: int = int(input())
last_item_binary: int = int(input(), 2)

new_total: int = current_total + last_item_binary

print(new_total)

# +
# 18

price_binary: int = int(input(), 2)
cash_given: int = int(input())

change: int = cash_given - price_binary

print(change)

# +
# 19

product_name: str = input()
price_per_kg: int = int(input())
item_weight: int = int(input())
money_given: int = int(input())

total_price: int = price_per_kg * item_weight
remaining_money: int = money_given - total_price

print(f"{'Чек':=^35}")
print(f"Товар:{product_name.rjust(29)}")
print(f"Цена:{f'{weight_kg}кг * {price_per_kg}руб/кг':>30}")
print(f"Итого:{f'{total_price}руб':>29}")
print(f"Внесено:{f'{money_given}руб':>27}")
print(f"Сдача:{f'{remaining_money}руб':>29}")
print("=" * 35)

# +
# 20

total_weight: int = int(input())
basic_price: int = int(input())
price_first_type: int = int(input())
price_second_type: int = int(input())

total_cost: int = basic_price * total_weight
first_type_weight: int = (total_cost - (price_second_type * total_weight)) // (
    price_first_type - price_second_type
)
second_type_weight: int = total_weight - first_type_weight

print(first_type_weight, second_type_weight)
