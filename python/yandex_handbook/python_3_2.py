"""Yandex handbook "Python Basics" answers."""

# +
# 1
text_1: str = "медведь"
chars_1: set[str] = set(text_1)

for ch_1 in chars_1:
    print(ch_1, end="")
print()

# +
# 2
word_a_2: str = "медведь"
word_b_2: str = "дельфин"

common_2: set[str] = set(word_a_2) & set(word_b_2)

for ch_2 in common_2:
    print(ch_2, end="")
print()

# +
# 3
entries_3: list[list[str]] = [
    ["зайка", "березка"],
    ["елочка", "зайка"],
    ["березка"],
]

unique_items_3: set[str] = set()

for entry_3 in entries_3:
    unique_items_3.update(entry_3)

for item_3 in sorted(unique_items_3):
    print(item_3)

# +
# 4
list_a_4: list[str] = ["зайка", "березка", "елочка"]
list_b_4: list[str] = ["березка", "елочка", "сосна"]

set_a_4: set[str] = set(list_a_4)
set_b_4: set[str] = set(list_b_4)

intersection_4: set[str] = set_a_4 & set_b_4

if intersection_4:
    print(len(intersection_4))
else:
    print("Таких нет")

# +
# 5
surnames_5: list[str] = ["Иванов", "Петров", "Сидоров", "Иванов", "Кузнецов"]

seen_once_5: set[str] = set()
seen_twice_5: set[str] = set()

for name_5 in surnames_5:
    if name_5 in seen_once_5:
        seen_twice_5.add(name_5)
    else:
        seen_once_5.add(name_5)

unique_surnames_5: set[str] = seen_once_5 - seen_twice_5

if unique_surnames_5:
    print(len(unique_surnames_5))
else:
    print("Таких нет")

# +
# 6
kids_6: list[str] = ["Иванов", "Петров", "Сидоров", "Иванов", "Кузнецов"]

group1_6: set[str] = set()
group2_6: set[str] = set()

for child_6 in kids_6:
    if child_6 in group1_6:
        group2_6.add(child_6)
    else:
        group1_6.add(child_6)

sym_diff_6: set[str] = group1_6 ^ group2_6

if sym_diff_6:
    for name_6 in sorted(sym_diff_6):
        print(name_6)
else:
    print("Таких нет")

# +
# 7
MORSE_CODE_7: dict[str, str] = {
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

message_7: str = "HELLO WORLD"

for char_7 in message_7:
    if char_7 == " ":
        print()
    else:
        print(MORSE_CODE_7[char_7], end=" ")
print()

# +
# 8
preferences_8: dict[str, list[str]] = {
    "овсянка": ["Анна", "Борис"],
    "манная": ["Вася"],
}

target_8: str = "рисовая"

if target_8 in preferences_8:
    for name_8 in sorted(preferences_8[target_8]):
        print(name_8)
else:
    print("Таких нет")

# +
# 9
lines_9: list[str] = ["зайка березка", "елочка зайка", "березка елочка"]

freq_9: dict[str, int] = {}

for line_9 in lines_9:
    for word_9 in line_9.split():
        freq_9[word_9] = freq_9.get(word_9, 0) + 1

for word_9, count_9 in freq_9.items():
    print(word_9, count_9)

# +
# 10
TRANS_10: dict[str, str] = {
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

text_10: str = "Привет, мир!"

result_10: str = ""
for ch_10 in text_10:
    upper_ch_10 = ch_10.upper()
    if upper_ch_10 in TRANS_10:
        mapped_10 = TRANS_10[upper_ch_10]
        if ch_10.isupper():
            out_ch_10 = mapped_10.capitalize()
        else:
            out_ch_10 = mapped_10.lower()
    else:
        out_ch_10 = ch_10
    result_10 += out_ch_10

print(result_10)

# +
# 11
names_11: list[str] = ["Анна", "Борис", "Вася"]

counts_11: dict[str, int] = {}
for name_11 in names_11:
    counts_11[name_11] = counts_11.get(name_11, 0) + 1

total_dup_11: int = sum(v for v in counts_11.values() if v > 1)
print(total_dup_11)

# +
# 12
names_12: list[str] = ["Анна", "Борис", "Вася"]

freq_12: dict[str, int] = {}
for name_12 in names_12:
    freq_12[name_12] = freq_12.get(name_12, 0) + 1

found_12: bool = False
for name_12 in sorted(freq_12):
    if freq_12[name_12] > 1:
        print(f"{name_12} - {freq_12[name_12]}")
        found_12 = True

if not found_12:
    print("Однофамильцев нет")

# +
# 13
initial_13: set[str] = {"Манная", "Овсянка", "Рисовая"}
used_13: set[str] = {"Рисовая"}

remaining_13: set[str] = initial_13 - used_13

menu_13: list[str] = sorted(remaining_13)
if menu_13:
    for dish_13 in menu_13:
        print(dish_13)
else:
    print("Готовить нечего")

# +
# 14
available_14: set[str] = {"мука", "сахар"}
recipes_14: dict[str, list[str]] = {
    "блинчики": ["мука", "молоко"],
    "печенье": ["мука", "сахар"],
}

possible_14: list[str] = []
for dish_14, ingredients_14 in recipes_14.items():
    if set(ingredients_14).issubset(available_14):
        possible_14.append(dish_14)

if possible_14:
    for dish_14 in sorted(possible_14):
        print(dish_14)
else:
    print("Готовить нечего")

# +
# 15
numbers_15: list[int] = [13, 2, 7]

stats_15: list[dict[str, int]] = []
for num_15 in numbers_15:
    bin_str_15: str = f"{num_15:b}"
    stats_15.append(
        {
            "digits": len(bin_str_15),
            "units": bin_str_15.count("1"),
            "zeros": bin_str_15.count("0"),
        }
    )

print(stats_15)

# +
# 16
scenes_16: list[list[str]] = [
    ["березка", "зайка", "елочка"],
    ["зайка", "сосна"],
]

neighbors_16: set[str] = set()

for scene_16 in scenes_16:
    for idx_16, item_16 in enumerate(scene_16):
        if item_16 == "зайка":
            if idx_16 > 0:
                neighbors_16.add(scene_16[idx_16 - 1])
            if idx_16 + 1 < len(scene_16):
                neighbors_16.add(scene_16[idx_16 + 1])

for obj_16 in sorted(neighbors_16):
    print(obj_16)

# +
# 17
scenes_data_17: list[list[str]] = [
    ["березка", "зайка", "елочка"],
    ["зайка", "сосна"],
]

adjacent_items_17: set[str] = set()

for scene_17 in scenes_data_17:
    for position_17, element_17 in enumerate(scene_17):
        if element_17 == "зайка":
            if position_17 > 0:
                adjacent_items_17.add(scene_17[position_17 - 1])
            if position_17 + 1 < len(scene_17):
                adjacent_items_17.add(scene_17[position_17 + 1])

for item_17 in sorted(adjacent_items_17):
    print(item_17)

# +
# 18
treasure_coords_18: list[tuple[int, int]] = [
    (12, 15),
    (18, 22),
    (13, 16),
    (55, 60),
]

grid_18: dict[tuple[int, int], int] = {}
for x_18, y_18 in treasure_coords_18:
    cell_18 = (x_18 // 10, y_18 // 10)
    grid_18[cell_18] = grid_18.get(cell_18, 0) + 1

print(max(grid_18.values()) if grid_18 else 0)

# +
# 19
gifts_19: list[tuple[str, list[str]]] = [
    ("Анна", ["кукла", "зайчик"]),
    ("Борис", ["кубики", "машинка"]),
    ("Вася", ["домик", "кубики"]),
]

all_toys_19: list[str] = []
for _, toys_19 in gifts_19:
    all_toys_19.extend(toys_19)

unique_19: dict[str, int] = {}
for toy_19 in all_toys_19:
    unique_19[toy_19] = unique_19.get(toy_19, 0) + 1

for toy_19 in sorted(unique_19):
    if unique_19[toy_19] == 1:
        print(toy_19)

# +
# 20
numbers_20: list[int] = [2, 7, 12, 49]

coprime_map_20: dict[int, list[int]] = {}

for a_20 in numbers_20:
    coprime_map_20[a_20] = []
    for b_20 in numbers_20:
        if a_20 != b_20:
            x_20, y_20 = a_20, b_20
            while y_20:
                x_20, y_20 = y_20, x_20 % y_20
            if x_20 == 1:
                coprime_map_20[a_20].append(b_20)

for num_20 in sorted(coprime_map_20):
    partners_20 = coprime_map_20[num_20]
    if partners_20:
        print(num_20, "-", ", ".join(map(str, sorted(partners_20))))
