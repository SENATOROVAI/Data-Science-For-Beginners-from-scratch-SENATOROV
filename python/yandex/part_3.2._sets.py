"""3.2 Sets."""

# Символическая выжимка
print("".join(set(input())))

# +
# Символическая разница
text1 = set(input())
text2 = set(input())

print("".join(text1 & text2))

# +
# Зайка — 8
count_area = int(input())
areas = set()

for _ in range(count_area):
    iter_areas = set(input().split())
    areas |= iter_areas

print(*areas, sep="\n")

# +
# Кашееды
count_mannaya = int(input())
count_ovsyanka = int(input())
like_mannaya = set()
like_ovsyanka = set()

for _ in range(count_mannaya):
    like_mannaya.add(input())

for _ in range(count_ovsyanka):
    like_ovsyanka.add(input())

double_like = like_mannaya & like_ovsyanka
print(len(double_like) if double_like else "Таких нет")

# +
# Кашееды — 2
count_mannaya = int(input())
count_ovsyanka = int(input())
count_all = count_mannaya + count_ovsyanka

double_like = set()
count_double = 0
for _ in range(count_all):
    text = input()
    if text not in double_like:
        double_like.add(text)
    else:
        count_double += 2
count_one = count_all - count_double
print(count_one if count_one else "Таких нет")

# +
# Кашееды — 3
count_mannaya = int(input())
count_ovsyanka = int(input())
count_all = count_mannaya + count_ovsyanka

like_one = set()
for _ in range(count_all):
    text = input()
    if text not in like_one:
        like_one.add(text)
    else:
        like_one.discard(text)
if like_one:
    print(*sorted(like_one), sep="\n")
else:
    print("Таких нет")

# +
# Азбука Морзе
morse_dict = {
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

input_text = input().strip().upper()
words = input_text.split()

for word in words:
    morse_word = " ".join(morse_dict[char] for char in word)
    print(morse_word)
# -

# Кашееды — 4
count_people = int(input())
hash_table: dict[str, list[str]] = {}
for _ in range(count_people):
    surname, *porridges = input().split()
    for porridge in porridges:
        hash_table[porridge] = hash_table.get(porridge, []) + [surname]
need_porridge = input()
if need_porridge in hash_table:
    print(*sorted(hash_table[need_porridge]), sep="\n")
else:
    print("Таких нет")

# +
# Зайка — 9
text = input()
hash_count: dict[str, int] = {}
while text != "":
    for word in text.split():
        hash_count[word] = hash_count.get(word, 0) + 1

    text = input()

for word, count_word in hash_count.items():
    print(word, count_word)

# +
# Транслитерация
translit_dict = {
    "А": "A",
    "а": "a",
    "Б": "B",
    "б": "b",
    "В": "V",
    "в": "v",
    "Г": "G",
    "г": "g",
    "Д": "D",
    "д": "d",
    "Е": "E",
    "е": "e",
    "Ё": "E",
    "ё": "e",
    "Ж": "ZH",
    "ж": "zh",
    "З": "Z",
    "з": "z",
    "И": "I",
    "и": "i",
    "Й": "I",
    "й": "i",
    "К": "K",
    "к": "k",
    "Л": "L",
    "л": "l",
    "М": "M",
    "м": "m",
    "Н": "N",
    "н": "n",
    "О": "O",
    "о": "o",
    "П": "P",
    "п": "p",
    "Р": "R",
    "р": "r",
    "С": "S",
    "с": "s",
    "Т": "T",
    "т": "t",
    "У": "U",
    "у": "u",
    "Ф": "F",
    "ф": "f",
    "Х": "KH",
    "х": "kh",
    "Ц": "TC",
    "ц": "tc",
    "Ч": "CH",
    "ч": "ch",
    "Ш": "SH",
    "ш": "sh",
    "Щ": "SHCH",
    "щ": "shch",
    "Ы": "Y",
    "ы": "y",
    "Э": "E",
    "э": "e",
    "Ю": "IU",
    "ю": "iu",
    "Я": "IA",
    "я": "ia",
    "Ъ": "",
    "ъ": "",
    "Ь": "",
    "ь": "",
}

text = input()

result = []
for char in text:
    if char in translit_dict:
        if char.isupper() and len(translit_dict[char]) > 1:
            first_character = translit_dict[char][0]
            second_character = translit_dict[char][1:]
            replacement = first_character + second_character.lower()
            result.append(replacement)
        else:
            result.append(translit_dict[char])
    else:
        result.append(char)

print("".join(result))

# +
# Однофамильцы
count_people = int(input())
hash_people: dict[str, int] = {}

for _ in range(count_people):
    surname = input()
    hash_people[surname] = hash_people.get(surname, 0) + 1

print(sum(count for count in hash_people.values() if count > 1))

# +
# Однофамильцы - 2
count_people = int(input())
peoples: dict[str, int] = {}
for _ in range(count_people):
    name = input()

    peoples[name] = peoples.get(name, 0) + 1

is_double_name = [value for value in peoples.values() if value > 1]
if is_double_name:
    for name, value in sorted(peoples.items(), key=lambda x: x[0]):
        if value > 1:
            print(f"{name} - {value}")
else:
    print("Однофамильцев нет")

# +
# Дайте чего-нибудь новенького!
count_food = int(input())
foods = {input() for _ in range(count_food)}

count_days = int(input())
for _ in range(count_days):
    count_food_day = int(input())
    food_day = {input() for _ in range(count_food_day)}
    foods -= food_day

need_foods = sorted(foods)
if need_foods:
    print(*need_foods, sep="\n")
else:
    print("Готовить нечего")

# +
# Это будет шедевр!
count_all_ingredients = int(input())
ingredients = {input() for _ in range(count_all_ingredients)}

count_dish = int(input())
good_dishes = []
for _ in range(count_dish):
    dish = input()
    count_ingredients = int(input())
    dish_ingredients = {input() for _ in range(count_ingredients)}
    if dish_ingredients <= ingredients:
        good_dishes.append(dish)

if good_dishes:
    print(*sorted(good_dishes), sep="\n")
else:
    print("Готовить нечего")

# +
# Двоичная статистика!
numbers = map(lambda x: list(bin(int(x))[2:]), input().split())

stats = []
for number in numbers:
    stat = {}
    count_digits = len(number)
    count_units = number.count("1")
    count_zeros = number.count("0")

    stat["digits"] = count_digits
    stat["units"] = count_units
    stat["zeros"] = count_zeros

    stats.append(stat)

print(stats)

# +
# Зайка — 10
text = input()
find_words = set()
while text != "":
    find_zaika = text.find("зайка")

    if find_zaika != -1:
        words = text.split()

        need_indexes = []
        for index, word in enumerate(words):
            if word == "зайка":
                need_indexes.append(index)

        for index in need_indexes:
            if index == 0:
                find_words.add(words[1])

            else:
                need_words = words[index - 1 : index + 2 : 2]
                for word in need_words:
                    find_words.add(word)

    text = input()

print(*find_words, sep="\n")

# +
# Друзья друзей
people: dict[str, set[str]] = {}

pair = input()
while pair != "":
    person1, person2 = pair.split()

    people.setdefault(person1, set()).add(person2)
    people.setdefault(person2, set()).add(person1)

    pair = input()

for person in sorted(people):
    friends = people[person]

    second_friends = set()
    for friend in friends:
        second_friends |= people[friend]

    second_friends.discard(person)
    second_friends -= friends

    print(f"{person}: ", end="")
    print(", ".join(sorted(second_friends)))

# +
# Карта сокровищ
count_points = int(input())
groups: dict[tuple[int, int], int] = {}

for _ in range(count_points):
    coord_x, coord_y = map(int, input().split())
    group_key = (coord_x // 10, coord_y // 10)
    groups[group_key] = groups.get(group_key, 0) + 1

print(max(groups.values()))

# +
# Частная собственность
count_children = int(input())

toys_count: dict[str, int] = {}
for _ in range(count_children):
    data = input().split(": ")
    child_toys = set(data[1].split(", "))

    for toy in child_toys:
        toys_count[toy] = toys_count.get(toy, 0) + 1

unique_toys = [toy for toy, count in toys_count.items() if count == 1]
for toy in sorted(unique_toys):
    print(toy)


# +
def compute_gcd(val_1: int, val_2: int) -> int:
    """Return greatest common divisor."""
    while val_2:
        val_1, val_2 = val_2, val_1 % val_2
    return val_1


input_data = input().strip()
numbers_list: list[int] = list(map(int, input_data.split("; ")))

unique_numbers = []
for num in numbers_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
unique_numbers.sort()

coprime_dict = {}

for num in unique_numbers:
    coprime_list = []
    for other_num in unique_numbers:
        if num != other_num and compute_gcd(num, other_num) == 1:
            coprime_list.append(other_num)
    if coprime_list:
        coprime_dict[num] = coprime_list

for num in sorted(coprime_dict.keys()):
    coprime_numbers = ", ".join(map(str, sorted(coprime_dict[num])))
    print(f"{num} - {coprime_numbers}")
