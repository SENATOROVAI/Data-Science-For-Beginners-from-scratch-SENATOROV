"""Stream input/output.

Working with text files. JSON.
"""

# +
# 1

import json
import sys
from sys import stdin

summa = 0
for line in stdin.readlines():
    for item in line.split():
        summa += int(item)

print(summa)

# +
# 2


total_difference = 0

input_lines_1 = [line.rstrip("\n") for line in stdin.readlines()]

for line in input_lines_1:
    identifier, previous_value_str, current_value_str = line.split()
    previous_value = int(previous_value_str)
    current_value = int(current_value_str)
    total_difference += current_value - previous_value

average_difference = round(total_difference / len(input_lines_1))

print(average_difference)

# +
# 3


input_lines_2 = stdin.readlines()

for raw_line in input_lines_2:
    if raw_line == "\n":
        print(raw_line, end="")
    elif raw_line and raw_line[0] != "#":
        comment_position = raw_line.find("# ")
        if comment_position != -1:
            raw_line = raw_line[:comment_position]
        if raw_line.endswith("\n"):
            raw_line = raw_line[:-1]
        print(raw_line)

# +
# 4


raw_lines = stdin.readlines()

clean_lines = [line[:-1] if line.endswith("\n") else line for line in raw_lines]

*title_list, search_query_1 = clean_lines

for title in title_list:
    if search_query_1.lower() in title.lower():
        print(title)

# +
# 5


palindromic_words = []

input_lines_3 = stdin.readlines()

for line in input_lines_3:
    if line.endswith("\n"):
        line = line[:-1]

    word_list = line.split()
    for word in word_list:
        upper_word = word.upper()
        if upper_word == upper_word[::-1]:
            palindromic_words.append(word)

unique_sorted_words = sorted(set(palindromic_words))
print("\n".join(unique_sorted_words))

# +
# 6

cyrillic_to_latin = {
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

input_file_name = "cyrillic.txt"
output_file_name = "transliteration.txt"

with open(output_file_name, "w", encoding="UTF-8") as output_file:
    with open(input_file_name, encoding="UTF-8") as input_file:
        for line in input_file:
            for char in line:
                upper_char = char.upper()
                if upper_char in cyrillic_to_latin:
                    latin_equivalent = cyrillic_to_latin[upper_char]
                    transliterated_char = (
                        latin_equivalent.capitalize()
                        if char.isupper()
                        else latin_equivalent.lower()
                    )
                else:
                    transliterated_char = char
                print(transliterated_char, end="", file=output_file)

with open(output_file_name, encoding="UTF-8") as result_file:
    print(result_file.read())

# +
# 7

file_name_1 = input()

with open(file_name_1, encoding="UTF-8") as input_file:
    file_content = input_file.read()
    integer_list = [int(token) for token in file_content.split()]

total_count = len(integer_list)
positive_count = sum(1 for number in integer_list if number > 0)
minimum_value = min(integer_list)
maximum_value = max(integer_list)
total_sum = sum(integer_list)
average_value = total_sum / total_count

print(total_count)
print(positive_count)
print(minimum_value)
print(maximum_value)
print(total_sum)
print(f"{average_value:.2f}")

# +
# 8

input_file_name_1 = input()
input_file_name_2 = input()
output_file_name = input()

with open(input_file_name_1, encoding="UTF-8") as input_file_1:
    words_from_file_1 = set(input_file_1.read().split())

with open(input_file_name_2, encoding="UTF-8") as input_file_2:
    words_from_file_2 = set(input_file_2.read().split())

unique_words = words_from_file_1 ^ words_from_file_2

with open(output_file_name, "w", encoding="UTF-8") as output_file:
    for word in sorted(unique_words):
        output_file.write(word + "\n")

with open(output_file_name, encoding="UTF-8") as output_file:
    print(output_file.read())

# +
# 9

input_file_name_3 = input()
output_file_name_2 = input()

cleaned_lines = []
with open(input_file_name_3, encoding="UTF-8") as input_file:
    for raw_line in input_file:
        tokens = raw_line.strip().replace("\t", "").split()
        if any(tokens):
            cleaned_lines.append(tokens)

with open(output_file_name_2, "w", encoding="utf-8") as output_file:
    for token_list in cleaned_lines:
        print(" ".join(token_list), file=output_file)

with open(output_file_name_2, encoding="UTF-8") as output_file:
    print(output_file.read())

# +
# 10

file_name_1 = input()
lines_to_print = int(input())

lines = []
with open(file_name_1, encoding="UTF-8") as file:
    lines = file.readlines()

for line in lines[-lines_to_print:]:
    print(line.strip())

# +
# 11


input_file_name_4 = input().strip()
output_file_name_4 = input().strip()

number_list = []

with open(input_file_name_4, encoding="utf-8") as input_file:
    content_1 = input_file.read()
    tokens_2 = content_1.split()

    for token in tokens_2:
        number_list.append(int(token))

number_count = len(number_list)
positive_count_2 = len([num for num in number_list if num > 0])
minimum_value_2 = min(number_list)
maximum_value_2 = max(number_list)
total_sum_2 = sum(number_list)
average_value_2 = round(total_sum / number_count, 2)

statistics = {
    "count": number_count,
    "positive_count": positive_count_2,
    "min": minimum_value_2,
    "max": maximum_value_2,
    "sum": total_sum_2,
    "average": average_value_2,
}

with open(output_file_name_4, "w", encoding="utf-8") as output_file:
    json.dump(statistics, output_file, ensure_ascii=False, indent=4)

with open(output_file_name_4, encoding="utf-8") as output_file:
    print(output_file.read())

# +
# 12

input_file_path_5 = input().strip()
evens_file_path = input().strip()
odds_file_path = input().strip()
equals_file_path = input().strip()

lines_2 = []

with open(input_file_path_5, encoding="utf-8") as input_file:
    for raw_line in input_file.read().split("\n"):
        if raw_line.strip():
            lines_2.append(raw_line)

even_digits = set("02468")
odd_digits = set("13579")

for line in lines_2:
    even_numbers = []
    odd_numbers = []
    equal_numbers = []

    for number_str in line.split():
        even_count = 0
        odd_count = 0

        for char in number_str:
            if char in even_digits:
                even_count += 1
            elif char in odd_digits:
                odd_count += 1

        if even_count > odd_count:
            even_numbers.append(number_str)
        elif odd_count > even_count:
            odd_numbers.append(number_str)
        else:
            equal_numbers.append(number_str)

    with open(evens_file_path, "a", encoding="utf-8") as evens_file:
        evens_file.write(" ".join(even_numbers) + "\n")

    with open(odds_file_path, "a", encoding="utf-8") as odds_file:
        odds_file.write(" ".join(odd_numbers) + "\n")

    with open(equals_file_path, "a", encoding="utf-8") as equals_file:
        equals_file.write(" ".join(equal_numbers) + "\n")

    print("\n# Содержимое файла evens_file.txt:")
    with open(evens_file_path, encoding="utf-8") as evens_file:
        print(evens_file.read().strip())

    print("\n# Содержимое файла odds_file.txt:")
    with open(odds_file_path, encoding="utf-8") as odds_file:
        print(odds_file.read().strip())

    print("\n# Содержимое файла equals_file.txt:")
    with open(equals_file_path, encoding="utf-8") as equals_file:
        print(equals_file.read().strip())

# +
# 13


json_file_name_1 = input().strip()

with open(json_file_name_1, encoding="utf-8") as json_file:
    data = json.load(json_file)

input_lines_4 = []
for line in stdin:
    stripped_line = line.strip()
    if stripped_line:
        input_lines_4.append(stripped_line)

for line in input_lines_4:
    if "==" in line:
        key, value = line.split("==", maxsplit=1)
        data[key.strip()] = value.strip()

with open(json_file_name_1, "w", encoding="utf-8") as file:
    json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)

with open(json_file_name_1, encoding="utf-8") as output_file:
    print(output_file.read())

# +
# 14

source_file_name = input().strip()
update_file_name = input().strip()

with open(source_file_name, encoding="utf-8") as source_file:
    source_data = json.load(source_file)

with open(update_file_name, encoding="utf-8") as update_file:
    update_data = json.load(update_file)

name_key = "name"
merged_data = {}

for record in source_data:
    name = str(record[name_key])
    merged_data[name] = {k: v for k, v in record.items() if k != name_key}

for update in update_data:
    name = str(update[name_key])
    if name not in merged_data:
        merged_data[name] = {}

    for key, new_value in update.items():
        if key == name_key:
            continue

        old_value = merged_data[name].get(key)

        is_new_num = isinstance(new_value, (int, float))
        is_old_num = isinstance(old_value, (int, float))

        if isinstance(new_value, (int, float)):
            if isinstance(old_value, (int, float)):
                if new_value > old_value:
                    merged_data[name][key] = new_value
        elif isinstance(new_value, str):
            if not isinstance(old_value, (int, float)) and (
                old_value is None or new_value > str(old_value)
            ):
                merged_data[name][key] = new_value

with open(source_file_name, "w", encoding="utf-8") as file:
    json.dump(merged_data, file, indent=4, ensure_ascii=False)

with open(source_file_name, encoding="utf-8") as source_file:
    print(source_file.read())

# +
# 15

json_file_name_2 = "scoring.json"

with open(json_file_name_2, encoding="utf-8") as json_file:
    test_blocks = json.load(json_file)

total_score = 0

for test_block in test_blocks:
    questions = test_block["tests"]
    points_raw = int(test_block["points"])
    points_per_question = points_raw // len(questions)

    for question in questions:
        expected_answer = question["pattern"]
        user_response = input("Введите ответ: ").strip()

        if user_response == expected_answer:
            total_score += points_per_question

print(total_score)

# +
# 16

search_query = input().strip()
file_name_3 = input().strip()
file_name_4 = input().strip()

file_set = [file_name_3, file_name_4]
match_found = False

for single_file in file_set:
    try:
        with open(single_file, encoding="utf-8") as file:
            raw_text = file.read().replace("\xa0", " ").lower()
            content_cleaned = " ".join(raw_text.split())

            if search_query.lower() in content_cleaned:
                print(file)
                match_found = True
    except FileNotFoundError:
        continue

if not match_found:
    print("404. Not Found")

# +
# 17

file_name_1 = "secret.txt"

try:
    with open(file_name_1, encoding="utf-8") as file:
        encoded_text_1 = file.read()
        decoded_text = ""

        for character in encoded_text_1:
            code_point = ord(character)
            if code_point >= 128:
                normalized_code = code_point % 256
            else:
                normalized_code = code_point
            decoded_text += chr(normalized_code)

        print(decoded_text)

except FileNotFoundError:
    print(f"Файл '{file_name_1}' не найден.")
except UnicodeDecodeError:
    print(f"Ошибка декодирования файла '{file_name_1}'.")

# +
# 18


file_name_2 = input()

try:
    with open(file_name_2, "rb") as file:
        file.seek(0, 2)
        file_size = file.tell()
except FileNotFoundError:
    print(f"Файл '{file_name_2}' не найден.")
    sys.exit(1)

size_units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
unit_index = 0

while file_size > 1024 and unit_index < len(size_units) - 1:
    quotient, remainder = divmod(file_size, 1024)
    file_size = quotient + int(remainder > 0)
    unit_index += 1

print(f"{file_size}{size_units[unit_index]}")

# +
# 19


input_file_path_6 = "public.txt"
output_file_path_5 = "private.txt"

alphabet = "abcdefghijklmnopqrstuvwxyz"

shift_value = int(input()) % len(alphabet)

shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]

cipher_map = {
    original: shifted for original, shifted in zip(alphabet, shifted_alphabet)
}

encoded_chars = []

with open(input_file_path_6, encoding="utf-8") as file:
    original_text = file.read()

    for char in original_text:
        lower_char = char.lower()
        if lower_char in cipher_map:
            new_char = cipher_map[lower_char]
            encoded_chars.append(new_char.upper() if char.isupper() else new_char)
        else:
            encoded_chars.append(char)

encoded_text_2 = "".join(encoded_chars)

with open(output_file_path_5, "w", encoding="utf-8") as file:
    file.write(encoded_text_2)

with open(output_file_path_5, encoding="utf-8") as file:
    final_output = file.read()
    print(final_output)

# +
# 20


input_file_path_7 = "numbers.num"
byte_chunk_size = 2
modulo = 0x10000

total_sum = 0

with open(input_file_path_7, "rb") as binary_file:
    while chunk := binary_file.read(byte_chunk_size):
        total_sum += int.from_bytes(chunk)

result = total_sum % modulo
print(result)
