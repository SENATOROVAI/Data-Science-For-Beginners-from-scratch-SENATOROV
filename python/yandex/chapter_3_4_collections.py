"""Collections."""

# ### Key Functions in `itertools`
#
# ####  Infinite Iterators
#
#  - `count(start, step)` – Produces an infinite sequence starting \
# from start and increasing by step
#
#         ```python
#         from itertools import count
#
#         for value in count(0, 0.1):
#             if value <= 1:
#                 print(round(value, 1))
#             else:
#                 break
#         ```
#
#  - `cycle(iterable)` – Repeats elements of an iterable indefinitely.
#
#         ```python
#         from itertools import cycle
#
#         max_len = 10
#         s = ""
#         for letter in cycle("ABC"):
#             if len(s) < max_len:
#                 s += letter
#             else:
#                 break
#         print(s)
#         ```
#
#  - `repeat(object, times)` – Repeats object times times.
#
#         ```python
#         from itertools import repeat
#
#         result = list(repeat("ABC", 5))
#         print(result)
#         ```
#
# #### Iterators Operating Until the Shortest Input
#
#  - `accumulate(iterable)` – Produces cumulative sums.
#
#         ```python
#         from itertools import accumulate
#
#         for value in accumulate([1, 2, 3, 4, 5]):
#             print(value)
#         ```
#
#  - `chain(i1, i2, ..., in)` – Combines multiple iterables into one.
#
#         ```python
#         from itertools import chain
#
#         values = list(chain("АБВ", "ГДЕЁ", "ЖЗИЙК"))
#         print(values)
#         ```
#
#  - `chain.from_iterable(iterable)` – Similar to chain, \
# but takes a single iterable of iterables.
#
#         ```python
#         from itertools import chain
#
#         values = list(chain.from_iterable(["АБВ", "ГДЕЁ", "ЖЗИЙК"]))
#         print(values)
#         ```
# #### Combinatorial Functions
#
#  - `product(iterables, repeat)` – Cartesian product of input iterables.
#
#         ```python
#         from itertools import product
#
#         values = list(product([1, 2, 3], "АБВГ", repeat=2))
#         print(values)
#         ```
#
#  - `permutations(iterable, r)` – Generates permutations of length r.
#
#         ```python
#         from itertools import permutations
#
#         values = list(permutations("АБВ"))
#         print(values)
#         ```
#  - `combinations(iterable, r)` – Generates unique subsets of length r.
#
#         ```python
#         from itertools import combinations
#
#         values = list(combinations("АБВ", 2))
#         print(values)
#         ```
#
#  - `combinations_with_replacement(iterable, r)` – Similar to combinations, but allows repeated elements.
#
#         ```python
#         from itertools import combinations_with_replacement
#
#         values = list(combinations_with_replacement("АБВ", 2))
#         print(values)
#         ```
#
#
# #### Other Useful Functions
#  - `enumerate(iterable, start=0)` – Adds an index to elements of an iterable.
#
#         ```python
#         for index, value in enumerate("ABC", 1):
#             print(index, value)
#         ```
#
#  - `zip(*iterables, strict=False)` – Combines elements with the same index from multiple iterables into tuples.
#
#         ```python
#         print(list(zip("ABC", [1, 2, 3])))
#         ```
#

# +
# 1

# fmt: off
from itertools import (accumulate, chain, combinations, count, cycle, islice,
                       permutations, product)

# fmt: on

products_list = input().split(" ")

for indx_val, prd in enumerate(products_list, 1):
    print(f"{indx_val}. {prd}")

# +
# 2

group_1 = input().split(",")
group_2 = input().split(",")

for person_1, person_2 in zip(group_1, group_2):
    print(f"{person_1.strip()} - {person_2.strip()}")

# +
# 3


[start, end, step] = [float(val) for val in input().split(" ")]

for el in count(start, step):
    if el >= end:
        break
    print(round(el, 2))

# +
# 4


for acc in accumulate(map(lambda val: f"{val} ", input().split())):
    print(acc)

# +
# 5


full_prd_list = chain.from_iterable(input().split(", ") for _ in range(3))

for prd_index, prd in enumerate(sorted(full_prd_list), start=1):
    print(f"{prd_index}. {prd}")

# +
# 6


nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
suits_val = ["пик", "треф", "бубен", "червей"]
suits_val.remove(input())
for card in product(nominal, suits_val):
    print(card[0], card[1])

# +
# 7


pupils: list[str] = [input() for _ in range(int(input()))]

for pair in list(combinations(pupils, 2)):
    print(f"{pair[0]} - {pair[1]}")

# +
# 8


porridge_count = int(input())
porridge_list = [input() for _ in range(porridge_count)]

days_count = int(input())

if porridge_count > days_count:
    for porridge in islice(porridge_list, days_count):
        print(porridge)
else:
    for porridge in islice(cycle(porridge_list), days_count):
        print(porridge)

# +
# 9


end = int(input())
table_items: list[int] = list(range(1, end + 1))

for t_it in table_items:
    product_iter = product(table_items, [t_it])
    print(" ".join(map(lambda x: str(x[0] * x[1]), product_iter)))

# +
# 10

orange_slices = int(input())

for sl_i in range(1, orange_slices - 1):
    if sl_i == 1:
        print("A Б В")
    for sl_j in range(1, orange_slices - sl_i):
        print(f"{sl_i} {sl_j} {orange_slices - sl_i - sl_j}")

# +
# 11


height_lines = int(input())
width_lines = int(input())

for i in range(height_lines):
    line = product(range(1, width_lines + 1), [i * width_lines])
    base_val = (height_lines - 1 - i) * width_lines

    formatted_numbers = [
        str(sum(x)).rjust(len(str(base_val + sum(x))), " ") for x in line
    ]

    print(" ".join(formatted_numbers))

# +
# 12

products = []
for _ in range(int(input())):
    products.extend([prd_item for prd_item in input().split(", ")])
for prod_index, it in enumerate(sorted(products), start=1):
    print(f"{prod_index}. {it}")

# +
# 13


people_count = int(input())
people_names = sorted([input() for _ in range(people_count)])
for permutation in permutations(people_names):
    print(", ".join(permutation))

# +
# 14


gamers_count = int(input())
gamers_names = sorted([input() for _ in range(gamers_count)])
for permutation in permutations(gamers_names, r=3):
    print(", ".join(permutation))

# +
# 15


fml_membr = int(input())
product_list = [pr for _ in range(fml_membr) for pr in input().split(", ")]

product_names = sorted(set(product_list))

for permutation in permutations(product_names, r=3):
    print(" ".join(permutation))

# +
# 16

suits_values: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}
ranks_ls: list[str] = [
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

required_suit_nominative = input().strip()
excluded_rank = input().strip()

required_suit_genitive = suits_values[required_suit_nominative]


all_cards = [
    f"{rank} {value}"
    for _, value in suits_values.items()
    for rank in ranks_ls
    if rank != excluded_rank
]

valid_combinations = [
    combo
    for combo in combinations(sorted(all_cards), 3)
    if any(required_suit_genitive in card for card in combo)
]

valid_combinations.sort()

for combination in valid_combinations[:10]:
    print(", ".join(combination))

# +
# 17


sts_vl = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}

ranks: list[str] = [
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

suit = sts_vl[input().strip()]
no_rank = input().strip()
previous = input().strip()

# fmt: off
card_tuples = [
    (rank, value) 
    for _, value in sts_vl.items() 
    for rank in ranks 
    if rank != no_rank
]
# fmt: on

cards = [f"{rank} {suit}" for rank, suit in card_tuples]

cards.sort()

# fmt: off
triples = [
    triple 
    for triple in combinations(cards, 3) 
    if any(suit in card for card in triple)
]
# fmt: on

triple_strings = [", ".join(triple) for triple in triples]

if previous in triple_strings:
    index = triple_strings.index(previous) + 1
    if index < len(triples):
        print(triple_strings[index])
    else:
        print("Нет следующего варианта.")
else:
    print("Предыдущий вариант не найден.")

# +
# 18

expression_input = input()
print("a b c f")
for i in range(8):
    bin_values = list(bin(i)[2:].zfill(3))
    a_val, b_val, c_val = map(int, bin_values)
    print(
        " ".join(bin_values),
        int(
            eval(  # pylint: disable=eval-used
                expression_input, {"a": a_val, "b": b_val, "c": c_val}
            )
        ),
    )

# +
# 19

expr_input_val = input().strip()
vbls_in_expr = sorted({exprs for exprs in expr_input_val if exprs.isupper()})

print(f"{' '.join(vbls_in_expr)} F")
for i_val in range(2 ** len(vbls_in_expr)):
    values = list(map(int, bin(i_val)[2:].zfill(len(vbls_in_expr))))
    local_vars = dict(zip(vbls_in_expr, values))
    print(
        " ".join(map(str, values)),
        int(eval(expr_input_val, local_vars)),  # pylint: disable=eval-used
    )

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


def infix_to_postfix(expression: str, variables: list[str]) -> list[str]:
    """Convert infix expression to postfix notation."""
    opr_stack: list[str] = []
    postfix_result: list[str] = []
    tokens: list[str] = expression.split()

    for token in tokens:
        if token in variables:
            postfix_result.append(token)
        elif token == "(":
            opr_stack.append(token)
        elif token == ")":
            while opr_stack and opr_stack[-1] != "(":
                postfix_result.append(OPERATORS[opr_stack.pop()])
            opr_stack.pop()  # Remove "("
        elif token in OPERATORS:
            while opr_stack and PRIORITY[token] >= PRIORITY[opr_stack[-1]]:
                postfix_result.append(OPERATORS[opr_stack.pop()])
            opr_stack.append(token)

    while opr_stack:
        postfix_result.append(OPERATORS[opr_stack.pop()])

    return postfix_result


def evaluate_postfix(pstf_exp: list[str], variables: dict[str, int]) -> int:
    """Evaluate a postfix (Reverse Polish Notation) expression."""
    eval_stack: list[int] = []

    for token in pstf_exp:
        if token in variables:
            eval_stack.append(variables[token])
        else:
            if token == "not":
                eval_stack.append(int(not eval_stack.pop()))
            else:
                operand2: int = eval_stack.pop()
                operand1: int = eval_stack.pop()
                eval_stack.append(
                    int(
                        eval(  # pylint: disable=eval-used
                            f"{operand1} {token} {operand2}"
                        )
                    )
                )

    return eval_stack.pop()


log_stmt: str = input().strip()

chrs: list[str] = sorted({char for char in log_stmt if char.isupper()})

print(" ".join(chrs), "F")

log_stmt = log_stmt.replace("(", "( ").replace(")", " )")

postfix_exp: list[str] = infix_to_postfix(log_stmt, chrs)

truth_table: tuple[tuple[int, ...], ...] = ()
truth_table = tuple(product([0, 1], repeat=len(chrs)))

for row in truth_table:
    vrbls_values: dict[str, int] = {}
    vrbls_values = {var: value for var, value in zip(chrs, row)}
    row_values = " ".join(str(value) for value in row)
    result = evaluate_postfix(postfix_exp, vrbls_values)

    print(row_values, result)
