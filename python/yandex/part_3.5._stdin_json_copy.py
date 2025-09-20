"""3.5 Stdin and json."""

import json
import os
from sys import stdin

# A+B+...
numbers = map(int, stdin.read().split())
print(sum(numbers))

# +
# Средний рост
count_people = 0
old_rises = []
new_rises = []
for line in stdin:
    _, old_value, new_value = line.strip().split()
    old_rises.append(int(old_value))
    new_rises.append(int(new_value))
    count_people += 1

print(round(sum(new_rises) / count_people - sum(old_rises) / count_people))
# -

# Без комментариев 2.0
for text in stdin:
    index = text.find("#")

    if index != -1:
        if text.strip()[0] == "#":
            continue

        print(text[:index])

    else:
        print(text.rstrip())

# Найдётся всё 2.0
texts = stdin.readlines()
key_word = texts[-1].strip().lower()
need_texts = (text.strip() for text in texts[:-1] if key_word in text.lower())
print(*need_texts, sep="\n")

# А роза упала на лапу Азора 6.0
words = stdin.read().split()
palindromes = {word for word in words if word.lower() == word.lower()[::-1]}
print(*sorted(palindromes), sep="\n")

# +
# Транслитерация 2.0
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
    "Ж": "Zh",
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
    "Х": "Kh",
    "х": "kh",
    "Ц": "Tc",
    "ц": "tc",
    "Ч": "Ch",
    "ч": "ch",
    "Ш": "Sh",
    "ш": "sh",
    "Щ": "Shch",
    "щ": "shch",
    "Ы": "Y",
    "ы": "y",
    "Э": "E",
    "э": "e",
    "Ю": "Iu",
    "ю": "iu",
    "Я": "Ia",
    "я": "ia",
    "Ъ": "",
    "ъ": "",
    "Ь": "",
    "ь": "",
}

with open("cyrillic.txt", encoding="UTF-8") as file:
    text = file.read().strip()
results = []

for symbol in text:
    new_symbol = translit_dict.get(symbol, symbol)
    results.append(new_symbol)

with open("transliteration.txt", "w", encoding="UTF-8") as output_file:
    output_file.write("".join(results))

# +
# Файловая статистика
file_name = input()

lst_numbers = []
with open(file_name, encoding="UTF-8") as file:
    for line in file:
        lst_numbers.extend(list(map(int, line.strip().split())))

sum_number = sum(lst_numbers)
count_numbers = len(lst_numbers)
print(count_numbers)
print(sum(1 for number in lst_numbers if number > 0))
print(min(lst_numbers))
print(max(lst_numbers))
print(sum_number)
print(round(sum_number / count_numbers, 2))

# +
# Файловая разница
file_one = input()
file_two = input()
file_answer = input()

words1 = []
words2 = []

with open(file_one, encoding="UTF-8") as file:
    for line in file:
        words1.extend(line.strip().split())

with open(file_two, encoding="UTF-8") as file:
    for line in file:
        words2.extend(line.strip().split())

need_words = sorted(set(words1) ^ set(words2))

with open(file_answer, "a", encoding="UTF-8") as file:
    for word in need_words:
        file.write(word + "\n")

# +
# Файловая чистка
file_one = input()
file_two = input()

lines = []
with open(file_one, encoding="UTF-8") as file:
    for line in file:
        line = line.strip()

        line = line.replace("\t", "")
        line = line.replace("\n", "")

        while "  " in line:
            line = line.replace("  ", " ")

        if line:
            lines.append(line)

with open(file_two, "a", encoding="UTF-8") as file:
    for line in lines:
        file.write(line + "\n")

# +
# Хвост
file_name = input()
count_lines = int(input())

with open(file_name, encoding="UTF-8") as file:
    lines = file.readlines()

for line in lines[-count_lines:]:
    print(line.strip())

# +
# Файловая статистика 2.0
input_file = input()
output_file_name = input()

with open(input_file, encoding="UTF-8") as file:
    numbers_list: list[int] = list(map(int, file.read().strip().split()))

count_numbers = len(numbers_list)
positive_count_numbers = len([number for number in numbers_list if number > 0])
min_number = min(numbers_list)
max_number = max(numbers_list)
sum_number = sum(numbers_list)
average_number: float = round(sum_number / count_numbers, 2)

output_dict = {
    "count": count_numbers,
    "positive_count": positive_count_numbers,
    "min": min_number,
    "max": max_number,
    "sum": sum_number,
    "average": average_number,
}

with open(output_file_name, "w", encoding="UTF-8") as file:
    json.dump(output_dict, file)

# +
# Разделяй и властвуй
input_files = stdin.read().splitlines()
input_file = input_files[0]
even_file = input_files[1]
odd_file = input_files[2]
eq_file = input_files[3]

with open(input_file, encoding="utf-8") as f_in, open(
    even_file, "w", encoding="utf-8"
) as f_even, open(odd_file, "w", encoding="utf-8") as f_odd, open(
    eq_file, "w", encoding="utf-8"
) as f_eq:

    for line in f_in:
        numbers_list_str = line.strip().split()
        even_numbers = []
        odd_numbers = []
        eq_numbers = []

        for number in numbers_list_str:
            evens = sum(1 for digit in number if int(digit) % 2 == 0)
            odds = len(number) - evens

            if evens > odds:
                even_numbers.append(number)
            elif odds > evens:
                odd_numbers.append(number)
            else:
                eq_numbers.append(number)

        f_even.write(" ".join(even_numbers) + "\n")
        f_odd.write(" ".join(odd_numbers) + "\n")
        f_eq.write(" ".join(eq_numbers) + "\n")

# +
# Обновление данных
input_file_name = input()
pairs_dicts = stdin.read().splitlines()

with open(input_file_name, encoding="UTF-8") as file:
    users_dict = json.load(file)

for pair_dict in pairs_dicts:
    key_dict, value_dict = pair_dict.split(" == ")
    users_dict[key_dict] = value_dict

with open(input_file_name, "w", encoding="UTF-8") as file:
    json.dump(users_dict, file, ensure_ascii=False, indent=2)

# +
# Слияние данных

users_file, users_updates_file = stdin.read().splitlines()

with open(users_file, encoding="UTF-8") as file:
    users_data = json.load(file)

with open(users_updates_file, encoding="UTF-8") as file:
    users_updates_data = json.load(file)

result: dict[str, dict[str, str]] = {}
for user in users_data + users_updates_data:
    name = user["name"]
    if name not in result:
        result[name] = {}

    for key, value in user.items():
        if key == "name":
            continue

        result[name][key] = max(value, result[name].get(key, value))

with open(users_file, "w", encoding="UTF-8") as file:
    json.dump(result, file, indent=4)

# +
# Поставь себя на моё место
user_answer = [line.strip() for line in stdin.read().splitlines()]

with open("scoring.json", encoding="UTF-8") as file:
    test_groups = json.load(file)

total_score = 0
index = 0

for group in test_groups:
    group_points = group["points"]
    tests = group["tests"]
    test_count = len(tests)
    points_per_test = group_points / test_count
    passed_tests = 0

    for test in tests:
        if index < len(user_answer) and user_answer[index] == test["pattern"]:
            passed_tests += 1
        index += 1

    total_score += int(passed_tests * points_per_test)

print(total_score)

# +
# Найдётся всё 3.0
search_text = " ".join(input().split()).lower()
files_for_analys = stdin.read().splitlines()

find_files_name = []
for file_name in files_for_analys:
    with open(file_name, encoding="UTF-8") as file:
        file_text = " ".join(file.read().split()).lower()

        if search_text in file_text:
            find_files_name.append(file_name)

if find_files_name:
    print(*find_files_name, sep="\n")
else:
    print("404. Not Found")
# -

# Прятки
with open("secret.txt", encoding="UTF-8") as file:
    print("".join([chr(ord(symbol) % 128) for symbol in file.read()]))

# +
# Сколько вешать в байтах?
size_file = os.path.getsize(input())
if size_file > 1024**3 - 1:
    size_file = int(size_file / 1024**3) + 1
    postfix = "ГБ"
elif size_file > 1024**2 - 1:
    size_file = int(size_file / 1024**2) + 1
    postfix = "МБ"
elif size_file > 1023:
    size_file = int(size_file / 1024) + 1
    postfix = "КБ"
else:
    postfix = "Б"

print(f"{size_file}{postfix}")

# +
# Это будет наш секрет
shift = int(stdin.read().strip())

with open("public.txt", encoding="UTF-8") as file:
    text_input = file.read()

text_output = ""
for char in text_input:
    if "a" <= char <= "z":
        text_output += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        text_output += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    else:
        text_output += char

with open("private.txt", "w", encoding="UTF-8") as file:
    file.write(text_output)

# +
# Файловая сумма
with open("numbers.num", "rb") as file:
    total_sum = 0

    chunk = file.read(2)
    while chunk:
        if len(chunk) < 2:
            continue
        total_sum += int.from_bytes(chunk, byteorder="big")
        chunk = file.read(2)

print(total_sum % 2**16)
