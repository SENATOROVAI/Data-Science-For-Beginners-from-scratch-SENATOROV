"""Built-in capabilities for working with collections."""

# +
# 1

from collections.abc import Iterable, Iterator, Mapping
from itertools import (
    accumulate,
    chain,
    combinations,
    count,
    cycle,
    islice,
    permutations,
    product,
)
from typing import cast

text: str = input()
words_1: list[str] = text.split()

for index, word in enumerate(words_1, start=1):
    print(f"{index}. {word}")

# +
# 2

left: list[str] = input().split(", ")
right: list[str] = input().split(", ")

for kids in zip(left, right):
    print(f"{kids[0]} - {kids[1]}")

# +
# 3

raw_input_1: str = input()
boundaries: list[float] = [float(x) for x in raw_input_1.split()]
start: float
stop: float
step: float
start, stop, step = boundaries

for num in count(start, step):
    if num >= stop:
        break
    print(f"{num:.2f}")

# +
# 4

raw_input_2: str = input()
words: list[str] = raw_input_2.split()

for partial_string in accumulate([word + " " for word in words]):
    print(partial_string)

# +
# 5

raw_inputs: list[str] = [input() for _ in range(3)]
split_items: list[list[str]] = [line.split(", ") for line in raw_inputs]

unique_sorted_items: list[str] = sorted(set(chain.from_iterable(split_items)))

for idx, item in enumerate(unique_sorted_items, start=1):
    print(f"{idx}. {item}")

# +
# 6

banned_suit: str = input()

suit_names: list[str] = ["пик", "треф", "бубен", "червей"]
card_ranks: list[str] = [str(rank) for rank in range(2, 11)] + [
    "валет",
    "дама",
    "король",
    "туз",
]

suit_names.remove(banned_suit)

card_combinations: list[str] = [
    f"{rank} {suit}" for rank, suit in product(card_ranks, suit_names)
]

print("\n".join(card_combinations))

# +
# 7

n_var: int = int(input())
names_1: list[str] = [input() for _ in range(n_var)]

pairs: list[tuple[str, str]] = list(combinations(names_1, 2))

output: list[str] = [f"{a} - {b}" for a, b in pairs]

print("\n".join(output))

# +
# 8

meal_count: int = int(input())
meal_list: list[str] = [input() for _ in range(meal_count)]

day_count: int = int(input())

repeated_meals: list[str] = list(islice(cycle(meal_list), day_count))

print("\n".join(repeated_meals))

# +
# 9

table_size: int = int(input())

multipliers: range = range(1, table_size + 1)

multiplication_values: list[int] = []
for row_factor, col_factor in product(multipliers, repeat=2):
    multiplication_values.append(row_factor * col_factor)

for row_index in range(table_size):
    row_start: int = row_index * table_size
    row_end: int = (row_index + 1) * table_size
    print(*islice(multiplication_values, row_start, row_end))

# +
# 10

target_sum: int = int(input())

value_range: range = range(1, target_sum - 1)

triplet_product = product(value_range, repeat=3)

triplet_combinations: list[tuple[int, int, int]] = list(
    cast(
        Iterable[tuple[int, int, int]],
        triplet_product,
    )
)

print("А Б В")
for triplet in triplet_combinations:
    if sum(triplet) == target_sum:
        print(*triplet)

# +
# 11

rows: int = int(input())
cols: int = int(input())

cell_width: int = len(str(rows * cols))

for row_idx, col_idx in product(range(1, rows + 1), range(1, cols + 1)):
    cell_number: int = (row_idx - 1) * cols + col_idx
    print(f"{cell_number:>{cell_width}}", end=" ")
    if col_idx == cols:
        print()

# +
# 12

all_items: list[str] = []

input_count: int = int(input())

for _ in range(input_count):
    entries: list[str] = input().split(", ")
    all_items.extend(entries)

sorted_items: list[str] = sorted(all_items)
indexed_items: list[tuple[int, str]] = list(enumerate(sorted_items, 1))

output_lines: list[str] = [f"{idx}. {val}" for idx, val in indexed_items]

print("\n".join(output_lines))

# +
# 13

participant_count: int = int(input())
participant_names: list[str] = [input() for _ in range(participant_count)]

participant_names.sort()

name_permutations: Iterator[tuple[str, ...]] = permutations(
    participant_names, participant_count
)

for name_tuple in name_permutations:
    print(", ".join(name_tuple))

# +
# 14

names_2: list[str] = []

num_names: int = int(input())

for _ in range(num_names):
    names_2.append(input())

names_2.sort()

perm_1: Iterator[tuple[str, str, str]] = permutations(names_2, 3)

for name_tuple in perm_1:
    print(", ".join(name_tuple))

# +
# 15

items_list: list[str] = []

item_count: int = int(input())

for _ in range(item_count):
    items_list.extend(input().split(", "))

items_list.sort()

perm_2: Iterator[tuple[str, str, str]] = permutations(items_list, 3)

for item_tuple in perm_2:
    print(" ".join(item_tuple))

# +
# 16

selected_suit: str = input().strip()
excluded_rank: str = input().strip()

suit_map: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

all_ranks: list[str] = [
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "валет",
    "дама",
    "король",
    "туз",
]

all_ranks.remove(excluded_rank)

deck: Iterator[tuple[str, str]] = product(all_ranks, suit_map.values())

triplets: Iterator[tuple[tuple[str, str], ...]] = permutations(deck, 3)

filtered_triplets = [
    triple
    for triple in triplets
    if suit_map[selected_suit] in chain.from_iterable(triple)
]

for combo in sorted(filtered_triplets)[:10]:
    print(", ".join(f"{r} {s}" for r, s in combo))

# +
# 17

suit_map_2: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

all_ranks_2: list[str] = [
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "валет",
    "дама",
    "король",
    "туз",
]

suit: str = suit_map_2[input().strip()]
excluded: str = input().strip()
previous: str = input().strip()

cards: list[str] = []
for rank in all_ranks_2:
    if rank == excluded:
        continue
    for s_var in suit_map_2.values():
        cards.append(f"{rank} {s_var}")

cards_arr: list[str] = sorted(cards)

tri_com: list[tuple[str, str, str]] = []
for triple in combinations(cards_arr, 3):
    for card in triple:
        if suit in card:
            tri_com.append(triple)
            break

triple_sets: list[str] = []
for triple in tri_com:
    triple_sets.append(", ".join(triple))

try:
    idx_s: int = triple_sets.index(previous) + 1
    print(triple_sets[idx_s])
except ValueError:
    print("Предыдущий вариант не найден.")
except IndexError:
    print("Нет следующего варианта.")

# +
# 18

logical_expression: str = input()

print("a b c f")

for a_var, b_var, c_var in product([0, 1], repeat=3):
    result_1: int = int(
        eval(  # pylint: disable=eval-used
            logical_expression, {"a": a_var, "b": b_var, "c": c_var}
        )
    )

    print(a_var, b_var, c_var, result_1)

# +
# 19

expression: str = input()

var_s: list[str] = []
for item in sorted(set(expression.split())):
    if item.isupper():
        var_s.append(item)

length: int = len(var_s)

print(*[v for v in var_s], "F")

for values in product([False, True], repeat=length):
    glob: dict[str, bool] = {key: value for key, value in zip(var_s, values)}
    int_values = [int(v) for v in values]

    result_2 = int(eval(expression, glob))  # pylint: disable=eval-used

    print(*int_values, result_2)

# +
# 20

OPERATORS: dict[str, str] = {
    "not": "not",
    "and": "and",
    "or": "or",
    "^": "!=",
    "->": "<=",
    "~": "==",
}

PRIORITY: dict[str, int] = {
    "not": 0,
    "and": 1,
    "or": 2,
    "^": 3,
    "->": 4,
    "~": 5,
    "(": 6,
}


def parse_expression(expr: str, variables: list[str]) -> list[str]:
    """Convert a logical expression to Reverse Polish Notation (RPN)."""
    stack: list[str] = []
    result_9: list[str] = []

    expr = expr.replace("(", "( ").replace(")", " )")

    for token in expr.split():
        if token in variables:
            result_9.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                result_9.append(OPERATORS[stack.pop()])
            stack.pop()
        elif token in OPERATORS:
            while stack and PRIORITY[token] >= PRIORITY.get(stack[-1], 100):
                result_9.append(OPERATORS[stack.pop()])
            stack.append(token)

    while stack:
        result_9.append(OPERATORS[stack.pop()])

    return result_9


def evaluate(rpn_expr: list[str], v_dict: Mapping[str, int | bool]) -> int:
    """Evaluate the value of a logical expression given in RPN."""
    stack: list[int | bool] = []

    for token in rpn_expr:
        if token in v_dict:
            stack.append(v_dict[token])
        elif token == "not":
            operand = stack.pop()
            stack.append(not operand)
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(eval(f"{lhs} {token} {rhs}"))  # pylint: disable=eval-used

    return int(stack.pop())


log_expr: str = input().strip()
vars_in_expr: list[str] = sorted({ch for ch in log_expr if ch.isupper()})

rpn: list[str] = parse_expression(log_expr, vars_in_expr)

print(*vars_in_expr, "F")
for bool_values in product([0, 1], repeat=len(vars_in_expr)):
    value_pairs = zip(vars_in_expr, (bool(v) for v in bool_values))
    val_map: dict[str, bool] = dict(value_pairs)
    result_10: int = evaluate(rpn, val_map)
    print(*bool_values, result_10)
