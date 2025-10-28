"""Yandex handbook "Python Basics" answers."""

# +
from itertools import accumulate, combinations, count, permutations, product

# 1
line_1: str = "картина корзина картонка"
words_1: list[str] = list(line_1.split())

for idx_1, word_1 in enumerate(words_1, start=1):
    print(f"{idx_1}. {word_1}")

# +
# 2
left_2: list[str] = list("Аня, Вова".split(", "))
right_2: list[str] = list("Боря, Дима".split(", "))

for pair_2 in zip(left_2, right_2):
    print(f"{pair_2[0]} - {pair_2[1]}")

# +
# 3
raw_3: str = "3.2 7.0 0.8"
parts_3: list[str] = list(raw_3.split())
start_3: float = float(parts_3[0])
stop_3: float = float(parts_3[1])
step_3: float = float(parts_3[2])

for val_3 in count(start_3, step_3):
    if val_3 >= stop_3:
        break
    print(f"{val_3:.2f}")

# +
# 4
phrase_4: str = "мама мыла раму"
words_4: list[str] = list(phrase_4.split())

for partial_4 in accumulate(words_4):
    print(" ".join(partial_4))

# +
# 5
lines_5: list[str] = [
    "картина, корзина, картонка",
    "манка, молоко, сыр",
    "хлеб, мыло",
]

items_5: set[str] = set()
for line_5 in lines_5:
    for item_5 in line_5.split(", "):
        items_5.add(item_5)

for idx_5, item_5 in enumerate(sorted(items_5), start=1):
    print(f"{idx_5}. {item_5}")

# +
# 6
banned_suit_6: str = "треф"

ranks_6: list[str] = [str(i) for i in range(2, 11)] + [
    "валет", "дама", "король", "туз"]
suits_6: list[str] = ["пик", "треф", "бубен", "червей"]

suits_6.remove(banned_suit_6)

for card_6 in product(ranks_6, suits_6):
    print(card_6[0], card_6[1])

# +
# 7
players_7: list[str] = ["Аня", "Боря", "Вова"]

pairs_7: list[tuple[str, str]] = []
for pair_7 in combinations(players_7, 2):
    pairs_7.append(pair_7)

lines_7: list[str] = []
for a_7, b_7 in pairs_7:
    lines_7.append(f"{a_7} - {b_7}")

print("\n".join(lines_7))

# +
# 8
menu_8: list[str] = ["Манная", "Гречневая", "Пшённая"]
days_8: int = 4

expanded_8: list[str] = menu_8 * (days_8 // len(menu_8) + 1)

for i_8 in range(days_8):
    print(expanded_8[i_8])

# +
# 9
size_9: int = 3

for row_9 in range(1, size_9 + 1):
    line_9: list[str] = []
    for col_9 in range(1, size_9 + 1):
        line_9.append(str(row_9 * col_9))
    print(" ".join(line_9))

# +
# 10
total_10: int = 3

print("А Б В")
for a_10 in range(1, total_10 - 1):
    for b_10 in range(1, total_10 - a_10):
        c_10: int = total_10 - a_10 - b_10
        print(a_10, b_10, c_10)

# +
# 11
rows_11: int = 2
cols_11: int = 3

width_11: int = len(str(rows_11 * cols_11))

for i_11 in range(rows_11):
    line_11: list[str] = []
    for j_11 in range(cols_11):
        val_11: int = i_11 * cols_11 + j_11 + 1
        line_11.append(f"{val_11:>{width_11}}")
    print(" ".join(line_11))

# +
# 12
lists_12: list[str] = [
    "картина, корзина",
    "картонка, манка",
    "молоко, мыло, сыр, хлеб",
]

all_items_12: list[str] = []
for line_12 in lists_12:
    all_items_12.extend(line_12.split(", "))

for idx_12, item_12 in enumerate(sorted(all_items_12), start=1):
    print(f"{idx_12}. {item_12}")

# +
# 13
names_13: list[str] = ["Аня", "Боря", "Вова"]

for perm_13 in sorted(permutations(names_13)):
    print(", ".join(perm_13))

# +
# 14
names_14: list[str] = ["Аня", "Боря", "Вова"]

for perm_14 in sorted(permutations(names_14, 3)):
    print(", ".join(perm_14))

# +
# 15
items_15: list[str] = ["кофе", "печенье", "сушки", "чай"]

for perm_15 in sorted(permutations(items_15, 3)):
    print(" ".join(perm_15))

# +
# 16
target_suit_16: str = "пики"  # ← ввод как в оригинале
excluded_rank_16: str = "10"

suit_map_16: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

ranks_16: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
suits_16: list[str] = ["бубен", "пик", "треф", "червей"]

ranks_16.remove(excluded_rank_16)

deck_16: list[tuple[str, str]] = list(product(ranks_16, suits_16))

hands_16: list[str] = []
target_full_suit_16: str = suit_map_16[target_suit_16]  # ← "пик"

for hand_16 in permutations(deck_16, 3):
    if any(card[1] == target_full_suit_16 for card in hand_16):
        sorted_hand_16 = sorted(hand_16)
        hand_str_16 = ", ".join(f"{r} {s}" for r, s in sorted_hand_16)
        hands_16.append(hand_str_16)

for hand_str_16 in sorted(set(hands_16))[:10]:
    print(hand_str_16)

# +
# 17
target_suit_17: str = "пики"
excluded_rank_17: str = "10"
prev_hand_17: str = "2 бубен, 2 пик, 2 треф"

suit_map_17: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

ranks_17: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
suits_17: list[str] = ["бубен", "пик", "треф", "червей"]

ranks_17.remove(excluded_rank_17)

deck_17: list[tuple[str, str]] = list(product(ranks_17, suits_17))

all_hands_17: list[str] = []
target_full_suit_17: str = suit_map_17[target_suit_17]  # ← "пик"

for hand_17 in permutations(deck_17, 3):
    if any(card[1] == target_full_suit_17 for card in hand_17):
        sorted_hand_17 = sorted(hand_17)
        hand_str_17 = ", ".join(f"{r} {s}" for r, s in sorted_hand_17)
        all_hands_17.append(hand_str_17)

unique_hands_17: list[str] = sorted(set(all_hands_17))

try:
    idx_17 = unique_hands_17.index(prev_hand_17)
    print(unique_hands_17[idx_17 + 1])
except (ValueError, IndexError):
    pass
# -

# 18
print("a b c f")
for var_a in [0, 1]:
    for var_b in [0, 1]:
        for var_c in [0, 1]:
            result_18 = (not var_a) or (var_b and var_c)
            print(var_a, var_b, var_c, int(result_18))

# +
# 19
variables_19: list[str] = ["A", "B", "C"]
print("A B C F")

for bits_19 in product([0, 1], repeat=3):
    env_19: dict[str, int] = dict(zip(variables_19, bits_19))
    value_19 = (env_19["A"] and env_19["B"]) or env_19["C"]
    print(bits_19[0], bits_19[1], bits_19[2], int(value_19))


# -

# 20
def to_postfix_20(expr: str, vars_list: list[str]) -> list[str]:
    """Преобразует логическое выражение в постфиксную запись."""
    op_map_20 = {
        "not": "not",
        "and": "and",
        "or": "or",
        "^": "!=",
        "->": "<=",
        "~": "==",
    }
    prec_20 = {
        "not": 0,
        "and": 1,
        "or": 2,
        "^": 3,
        "->": 4,
        "~": 5,
        "(": 6,
    }
    tokens_20 = expr.split()
    stack_20: list[str] = []
    output_20: list[str] = []
    for token_20 in tokens_20:
        if token_20 in vars_list:
            output_20.append(token_20)
        elif token_20 == "(":
            stack_20.append(token_20)
        elif token_20 == ")":
            while stack_20 and stack_20[-1] != "(":
                output_20.append(op_map_20[stack_20.pop()])
            if stack_20:
                stack_20.pop()
        elif token_20 in op_map_20:
            while True:
                if not stack_20:
                    break
                if stack_20[-1] == "(":
                    break
                if prec_20[token_20] < prec_20.get(stack_20[-1], -1):
                    break
                output_20.append(op_map_20[stack_20.pop()])
            stack_20.append(token_20)
    while stack_20:
        output_20.append(op_map_20[stack_20.pop()])
    return output_20
