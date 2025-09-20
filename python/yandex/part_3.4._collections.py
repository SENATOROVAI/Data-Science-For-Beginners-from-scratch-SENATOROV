"""3.4 Collections."""

from itertools import (
    accumulate,
    chain,
    combinations,
    count,
    cycle,
    permutations,
    product,
)

# Автоматизация списка
products = input().split()
for index, prod in enumerate(products, start=1):
    print(f"{index}. {prod}")

# Сборы на прогулку
names1 = input().split(", ")
names2 = input().split(", ")
for name1, name2 in zip(names1, names2):
    print(f"{name1} - {name2}")

# Рациональная считалочка
start, end, step = map(float, input().split())
for number in count(start, step):
    if number > end:
        break
    print(number)

# +
# Словарная ёлка
text = map(lambda x: x + " ", input().split())

for phrase in accumulate(text):
    print(phrase)

# +
# Список покупок
products1 = input().split(", ")
products2 = input().split(", ")
products3 = input().split(", ")

all_products = sorted(chain(products1, products2, products3))
for index, prod in enumerate(all_products, start=1):
    print(f"{index}. {prod}")

# +
# Колода карт
remove_suit = input()
all_suit = ["пик", "треф", "бубен", "червей"]
all_suit.remove(remove_suit)
all_values = [
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

for value, suit in product(all_values, all_suit):
    print(value, suit)

# +
# Игровая сетка
count_users = int(input())
users = [input() for _ in range(count_users)]

for user1, user2 in combinations(users, 2):
    print(f"{user1} - {user2}")

# +
# Меню питания 2.0
count_food = int(input())
foods = [input() for _ in range(count_food)]
count_days = int(input())

for food in cycle(foods):
    if count_days == 0:
        break

    print(food)
    count_days -= 1
# -

# Таблица умножения 3.0
size = int(input())
numbers = (number for number in range(1, size + 1))
next_line = size
for first, second in product(numbers, repeat=2):
    if not next_line:
        print()
        next_line = size
    print(first * second, end=" ")
    next_line -= 1

# +
# Мы делили апельсин 2.0
part_orange = int(input())
parts = (part for part in range(1, part_orange + 1))

print("А Б В")
for anya, borya in product(parts, repeat=2):
    vova = part_orange - anya - borya
    if vova > 0:
        print(anya, borya, vova)

# +
# Числовой прямоугольник 3.0
rows = int(input())
cols = int(input())

max_number_lens = len(str(rows * cols))

linear = [number for number in range(1, rows * cols + 1)]
chunk_size = cols
iters = [iter(linear)] * chunk_size

for row in list(zip(*iters)):
    for num in row:
        print(f"{num:>{max_number_lens}}", end=" ")
    print()

# +
# Список покупок 2.0
count_people = int(input())
prods: list[list[str]] = [input().split(", ") for _ in range(count_people)]

all_products = sorted(chain.from_iterable(prods))
for index, prod in enumerate(all_products, start=1):
    print(f"{index}. {prod}")

# +
# Расстановка спортсменов
people = sorted([input() for _ in range(int(input()))])

for row in permutations(people):
    print(*row, sep=", ")

# +
# Спортивные гадания
people = sorted([input() for _ in range(int(input()))])

for row in permutations(people, 3):
    print(*row, sep=", ")

# +
# Список покупок 3.0
count_us = int(input())
lst_prods = chain.from_iterable([input().split(", ") for _ in range(count_us)])

for row in permutations(sorted(lst_prods), 3):
    print(*row)

# +
# Расклад таков...
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
# А есть ещё варианты?
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
# -

# Таблица истинности
example = input().strip()
print("a b c f")
for a1, b1, c1 in product([0, 1], [0, 1], [0, 1]):
    # pylint: disable=eval-used
    result = eval(example, {"a": a1, "b": b1, "c": c1})
    print(f"{a1} {b1} {c1} {int(result)}")

# +
# Таблица истинности 2
example = input().strip()
params = sorted({symbol for symbol in example if symbol.isupper()})

print(*params, "F")
lsts_values = [[0, 1] for _ in range(len(params))]
for values in product(*lsts_values):
    values_params = dict(zip(params, values))
    # pylint: disable=eval-used
    result = int(eval(example, values_params))
    print(*values, result)

# +
# Таблица истинности 3
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
