"""Sets, dictionaries."""

# +
# 1

string_1: set[str] = set(input())

for char in string_1:
    print(char, end="")

# +
# 2

for char in set(input()) & set(input()):
    print(char, end="")

# +
# 3

items: set[str] = set()

for _ in range(int(input())):
    string_2: str = input()
    items |= set(string_2.split())

for item in items:
    print(item)

# +
# 4

first_list_size: int = int(input())
second_list_size: int = int(input())

first_set: set[str] = set()
second_set: set[str] = set()

for _ in range(first_list_size):
    first_set.add(input())

for _ in range(second_list_size):
    second_set.add(input())

common_elements: set[str] = first_set & second_set

if len(common_elements) != 0:
    print(len(common_elements))
else:
    print("Таких нет")

# +
# 5

total_first_list_size: int = int(input())
total_second_list_size: int = int(input())

unique_names: set[str] = set()
duplicate_names: set[str] = set()

for _ in range(total_first_list_size + total_second_list_size):
    surname: str = input()
    if surname in unique_names:
        duplicate_names.add(surname)
    else:
        unique_names.add(surname)

non_duplicate_surnames: set[str] = unique_names ^ duplicate_names

if len(non_duplicate_surnames) != 0:
    print(len(non_duplicate_surnames))
else:
    print("Таких нет")

# +
# 6

list1_size = int(input())
list2_size = int(input())

list1 = set()
list2 = set()

for _ in range(list1_size + list2_size):
    eater = input()
    if eater in list1:
        list2.add(eater)
    else:
        list1.add(eater)

if len(junction := list1 ^ list2) != 0:
    for eater in sorted(junction):
        print(eater)
else:
    print("Таких нет")

# +
# 7

MORZE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

for char in input():
    if char != " ":
        print(MORZE[char.upper()], end=" ")
    else:
        print()

# +
# 8

porridges_list: dict[str, list[str]] = {}

for _ in range(int(input())):
    string = input()
    eater, *porridges = string.split()
    for porridge in porridges:
        porridges_list[porridge] = porridges_list.get(porridge, []) + [eater]

porridge_: str = input()

if porridge_ in porridges_list:
    print("\n".join(sorted(porridges_list[porridge_])))
else:
    print("Таких нет")

# +
# 9

word_frequencies_1: dict[str, int] = {}

while (line := input()) != "":
    words: list[str] = line.split()
    for word in words:
        word_frequencies_1[word] = word_frequencies_1.get(word, 0) + 1

for word, freq in word_frequencies_1.items():
    print(word, freq)

# +
# 10

TRANSLITERATE_DICT: dict[str, str] = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ь": "",
    "Ъ": "",
}

result: str = ""

for original_char in input():
    uppercase_char = original_char.upper()
    if uppercase_char in TRANSLITERATE_DICT:
        mapped = TRANSLITERATE_DICT[uppercase_char]
        transliterated_char = (
            mapped.capitalize() if original_char.isupper() else mapped.lower()
        )
    else:
        transliterated_char = original_char
    result += transliterated_char

print(result)

# +
# 11

namesakes: dict[str, int] = {}

for _ in range(int(input())):
    name: str = input()
    namesakes[name] = namesakes.get(name, 0) + 1

count: int = 0
for name, value in namesakes.items():
    if value > 1:
        count += value

print(count)

# +
# 12

namesakes = {}
for _ in range(int(input())):
    name = input()
    namesakes[name] = namesakes.get(name, 0) + 1

namesakes = dict(sorted(namesakes.items()))

printed = False

for name in namesakes:
    if namesakes[name] > 1:
        print(name, "-", namesakes[name])
        printed = True

if not printed:
    print("Однофамильцев нет")

# +
# 13

porridges_2: set[str] = set()

for _ in range(int(input())):
    if (porridge := input()) not in porridges_2:
        porridges_2.add(porridge)

for _ in range(int(input())):
    for _ in range(int(input())):
        if (porridge := input()) in porridges_2:
            porridges_2.remove(porridge)

menu: list[str] = sorted(porridges_2)
print(type(menu))

if not menu:
    print("Готовить нечего")
else:
    for porridge in menu:
        print(porridge)

# +
# 14

products: list[str] = []
recipes: dict[str, list[str]] = {}
menu_2: list[str] = []

for _ in range(int(input())):
    products.append(input())

for _ in range(int(input())):
    name = input()
    ingredients = []
    for _ in range(int(input())):
        ingredients.append(input())
    recipes[name] = recipes.get(name, []) + ingredients

for name, ingredients in recipes.items():
    print(type(menu_2))
    if set(ingredients).issubset(products):
        menu_2.append(name)

if menu_2:
    print(type(menu_2))
    menu_2.sort()
    for name in menu_2:
        print(name)
else:
    print("Готовить нечего")

# +
# 15

binary_stats: list[dict[str, int]] = []
input_numbers: list[str] = input().split()

for number_str in input_numbers:
    binary_repr: str = f"{int(number_str):b}"
    stats: dict[str, int] = {
        "digits": len(binary_repr),
        "units": binary_repr.count("1"),
        "zeros": binary_repr.count("0"),
    }
    binary_stats.append(stats)

print(binary_stats)

# +
# 16

subject: str = "зайка"
objects: set[str] = set()

while (nature := input().split()) != []:
    seen = None
    for item in nature:
        if seen == subject:
            objects.add(item)
        if item == subject:
            if seen:
                objects.add(seen)
        seen = item

for item in objects:
    print(item)

# +
# 17

friends: dict[str, set[str]] = {}

while pair := input():
    friend1, friend2 = pair.split()
    friends[friend1] = friends.get(friend1, set()) | {friend2}
    friends[friend2] = friends.get(friend2, set()) | {friend1}

friends_of_friends: dict[str, list[str]] = {}

for name in sorted(friends):
    foaf_set: set[str] = set()
    for person in friends[name]:
        foaf_set |= friends[person]
    foaf_set.discard(name)
    foaf_set -= friends[name]
    friends_of_friends[name] = sorted(foaf_set)

for name in sorted(friends_of_friends):
    print(f'{name}: {", ".join(friends_of_friends[name])}')

# +
# 18

treasures: dict[tuple[int, int], int] = {}

for _ in range(count := int(input())):
    x_var, y_var = input().split()
    index = (int(x_var) // 10, int(y_var) // 10)
    treasures[index] = treasures.get(index, 0) + 1

print(max(treasures.values()))

# +
# 19

toys: list[str] = []
unique: dict[str, int] = {}

for _ in range(int(input())):
    name, str_ = input().split(": ")
    toys.extend(set(str_.split(", ")))

for toy in sorted(toys):
    unique[toy] = unique.get(toy, 0) + 1

for toy, count in unique.items():
    if count == 1:
        print(toy)

# +
# 20

items_2: set[str] = set(input().split("; "))

numbers: list[int] = []

for item in items_2:
    numbers.append(int(item))

numbers.sort()

for num1 in numbers:
    mutually = []
    for num2 in numbers:
        if num1 != num2:
            a_var, b_var = num1, num2
            while b_var != 0:
                a_var, b_var = b_var, a_var % b_var
            if a_var == 1:
                mutually.append(f"{num2}")
    if mutually:
        print(num1, "-", ", ".join(mutually))
