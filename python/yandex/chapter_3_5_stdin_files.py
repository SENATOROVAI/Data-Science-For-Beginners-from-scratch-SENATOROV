"""Stream input/output.

Working with text files. JSON.
"""

# ### Read from stdin
#
# ```python
# from sys import stdin
#
# lines = []
# for line in stdin:
#     lines.append(line)
# print(lines)
# ```
#
# ### Read from stdin and rstrip new line
#
# ```python
# from sys import stdin
#
# lines = []
# for line in stdin:
#     lines.append(line.rstrip("\n"))
# print(lines)
# ```
#
#
# ### Alternative method tp read from stdin, it keeps new lines
#
# ```python
# from sys import stdin
#
# lines = stdin.readlines()
# print(lines)
# ```
#
# ### Read stdin in one string
#
# ```python
# from sys import stdin
#
# text = stdin.read()
# print([text])
# ```
#
#
# In Python, the built-in `open()` function is used for file operations. Key arguments include:
#
# - file: Path to the file (absolute or relative).
# mode: Access mode:
#     - "r": Read (default).
#     - "w": Write (creates a new file).
#     - "a": Append (creates file if it doesn’t exist).
#     - "+": Allows both reading and writing.
# - encoding: Specifies file encoding (e.g., "UTF-8").
# To read a UTF-8 encoded text file, ensure the file is saved with UTF-8 encoding.
#
# ```python
# file_in = open("input_1.txt", encoding="UTF-8")
# for line in file_in:
#     print(line)
# file_in.close()
# ```
#
#
# After working with a file in Python, it must be closed using the close()
# method to free system resources. If not closed, the file may remain inaccessible to other programs.
# To ensure proper closure, use the context manager (with statement),
# which automatically closes the file, even if an error occurs:
#
# ```python
# with open("input_1.txt", encoding="UTF-8") as file_in:
#     for line in file_in:
#         print(line.rstrip("\n"))
# ```
#
# To write to a file in Python, you must first open it in write ("w") or append ("a") mode.
# The `write()` method is used to write data from a string variable to the file. Example:
#
# ```python
# with open("output_1.txt", "w", encoding="UTF-8") as file_out:
#     n = file_out.write("Это первая строка\nА вот и вторая\nИ третья — последняя\n")
# print(n)
# ```
#
# To write lines, `writelines` method is used.
#
# ```python
# lines = ["Это первая строка\n", "А вот и вторая\n", "И третья — последняя\n"]
# with open("output_2.txt", "w", encoding="UTF-8") as file_out:
#     file_out.writelines(lines)
# ```
#
# To read JSON files in Python, use the json.load() method,
# which loads the entire JSON file and returns a corresponding
# Python data structure (e.g., dictionary or list).
#
# ```python
# import json
# from pprint import pprint
#
# with open("data.json", encoding="UTF-8") as file_in:
#     records = json.load(file_in)
# pprint(records)
# ```
#
#
# To write modified data back to a JSON file in Python, use the `json.dump()` method. Important arguments include:
#
# - ensure_ascii:
#     True (default) → Non-ASCII characters are stored as Unicode escape sequences (\uXXXX).
#     False → Stores characters as they are (useful for non-Latin scripts like Russian).
#
# - indent:
#     None (default) → Writes JSON in a single line.
#     Number (e.g., 4) → Formats JSON with that many spaces for readability.
#
# - sort_keys:
#     True → Sorts dictionary keys alphabetically.
#     False (default) → Keeps original order.
#
# ```python
# import json
#
# with open("data.json", encoding="UTF-8") as file_in:
#     records = json.load(file_in)
# records[1]["group_number"] = 2
# with open("data.json", "w", encoding="UTF-8") as file_out:
#     json.dump(records, file_out, ensure_ascii=False, indent=2)
# ```

# +
# 1

import json
import os
import sys
from sys import stdin

total: int = 0

for input_val in stdin:
    total += sum(map(int, input_val.split(" ")))
print(total)

# +
# 2


avrg_before: int = 0
avrg_after: int = 0
pupils_count: int = 0

for pupil_line in stdin:
    avrg_before += int(pupil_line.split(" ")[1])
    avrg_after += int(pupil_line.split(" ")[2])
    pupils_count += 1
height_diff = round(avrg_after / pupils_count - avrg_before / pupils_count)
print(height_diff)

# +
# 3


for program_line in stdin:
    comment_start_index = program_line.find("#")

    if comment_start_index != -1:
        cleaned_program_line = program_line[:comment_start_index]
        if cleaned_program_line.strip():
            print(cleaned_program_line)
    else:
        print(program_line, end="")

# +
# 4


title_lines = stdin.readlines()

titles = title_lines[:-1]
query = title_lines[-1].strip()

for title in titles:
    if title.lower().find(query.lower()) > -1:
        print(title, end="")

# +
# 5


palindromes = []

for ln in stdin:
    words = ln.split()
    for word in words:
        cleaned_word = word.strip().lower()
        if cleaned_word == cleaned_word[::-1]:
            palindromes.append(word.strip())

for word in sorted(set(palindromes)):
    print(word)

# +
# 6


translit_map = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
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
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "tc",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "y",
    "э": "e",
    "ю": "iu",
    "я": "ia",
    "ъ": "",
    "ь": "",
    "Ъ": "",
    "Ь": "",
}

input_file = "cyrillic.txt"
output_file = "transliteration.txt"


with open(input_file, encoding="utf-8") as infile:
    text = infile.read()

transliterated_text = "".join(translit_map.get(char, char) for char in text)

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(transliterated_text)

# +
# 7


file_name = stdin.read().strip()

stats_numbers: list[int] = []

with open(file_name, encoding="UTF-8") as file_with_numbers:
    for number_line in file_with_numbers:
        stats_numbers.extend(int(nmb) for nmb in number_line.split())

print(len(stats_numbers))
print(len([pos_nmb for pos_nmb in stats_numbers if pos_nmb > 0]))
print(min(stats_numbers))
print(max(stats_numbers))
print(sum(stats_numbers))
print(f"{sum(stats_numbers) / len(stats_numbers):.2f}")

# +
# 8


unique_words: set[str] = set()
file_names = stdin.read().splitlines()
file_names_in = file_names[:-1]
file_name_out = file_names[-1]


for file_name in file_names_in:
    with open(file_name, encoding="UTF-8") as file_in:
        file_words = []
        for words_line in file_in:
            file_words.extend(words_line.split())
        unique_words ^= set(file_words)

with open(file_name_out, "w", encoding="UTF-8") as file_out:
    for word in sorted(unique_words):
        print(word, file=file_out)

# +
# 9


util_file_names = stdin.read().splitlines()
util_file_name_in = util_file_names[0]
util_file_name_out = util_file_names[1]

cleaned_lines: list[list[str]] = []

with open(util_file_name_in, encoding="UTF-8") as file_in:
    for text_line in file_in:
        words = text_line.strip().replace("\t", "").split()
        if words:
            cleaned_lines.append(words)

with open(util_file_name_out, "w", encoding="UTF-8") as file_out:
    for words_list in cleaned_lines:
        file_out.write(" ".join(words_list) + "\n")

# +
# 10


tail_file_input = stdin.read().splitlines()
tail_file_name = tail_file_input[0]
tail_file_lines = tail_file_input[1]

tail_data = []

with open(tail_file_name, encoding="UTF-8") as file_in:
    for ln in file_in:
        tail_data.append(ln)
for tail_line in tail_data[-int(tail_file_lines) :]:
    print(tail_line, end="")

# +
# 11


user_input_files = stdin.read().splitlines()
user_input_number_file = user_input_files[0]
user_input_statistics_file = user_input_files[1]

nmb_ls_full: list[int] = []

with open(user_input_number_file, encoding="UTF-8") as file_in:
    for ln in file_in:
        nmb_ls_full.extend(int(nmb_inp) for nmb_inp in ln.split())

with open(user_input_statistics_file, "w", encoding="UTF-8") as file_out:
    positive_count = len(list(filter(lambda vl: vl > 0, nmb_ls_full)))
    json.dump(
        {
            "count": len(nmb_ls_full),
            "positive_count": positive_count,
            "min": min(nmb_ls_full),
            "max": max(nmb_ls_full),
            "sum": sum(nmb_ls_full),
            "average": f"{sum(nmb_ls_full) / len(nmb_ls_full):.2f}",
        },
        file_out,
        ensure_ascii=False,
        indent=4,
    )

# +
# 12


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
        numbers = line.strip().split()
        even_numbers = []
        odd_numbers = []
        eq_numbers = []

        for num in numbers:
            evens = sum(1 for digit in num if int(digit) % 2 == 0)
            odds = len(num) - evens

            if evens > odds:
                even_numbers.append(num)
            elif odds > evens:
                odd_numbers.append(num)
            else:
                eq_numbers.append(num)

        f_even.write(" ".join(even_numbers) + "\n")
        f_odd.write(" ".join(odd_numbers) + "\n")
        f_eq.write(" ".join(eq_numbers) + "\n")

# +
# 13


user_inout_json_changes = stdin.read().splitlines()
user_json_file_name = user_inout_json_changes[0]
user_json_file_changes = user_inout_json_changes[1:]

with open(user_json_file_name, encoding="UTF-8") as file_in:
    json_records = json.load(file_in)

    for change in user_json_file_changes:
        [key, val] = change.split(" == ")
        json_records[key] = val

    with open(user_json_file_name, "w", encoding="UTF-8") as file_out:
        json.dump(json_records, file_out, ensure_ascii=False, indent=2)

# +
# 14


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
# 15


usr_answr = [line.strip() for line in stdin.read().splitlines()]

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
        if index < len(usr_answr) and usr_answr[index] == test["pattern"]:
            passed_tests += 1
        index += 1

    total_score += int(passed_tests * points_per_test)

print(total_score)

# +
# 16


search_input_params = sys.stdin.read().splitlines()
search_query = " ".join(search_input_params[0].split()).lower()
search_files = search_input_params[1:]

found_files = []

for srch_fl in search_files:
    with open(srch_fl, encoding="UTF-8") as srch_file_in:
        file_content = " ".join(srch_file_in.read().split()).lower()
        if search_query in file_content:
            found_files.append(srch_fl)

if found_files:
    print("\n".join(found_files))
else:
    print("404. Not Found")

# +
# 17

with open("secret.txt", encoding="UTF-8") as f:
    print("".join([chr(ord(i) % 128) for i in f.read()]))

# +
# 18


size = os.path.getsize(input())
if size > 1024**3 - 1:
    size = int(size / 1024**3) + 1
    postfix = "ГБ"
elif size > 1024**2 - 1:
    size = int(size / 1024**2) + 1
    postfix = "МБ"
elif size > 1023:
    size = int(size / 1024) + 1
    postfix = "КБ"
else:
    postfix = "Б"
print(str(size) + postfix)

# +
# 19


shift = int(sys.stdin.read().strip())

with open("public.txt", encoding="UTF-8") as file:
    text = file.read()

encrypted_text = ""
for char in text:
    if "a" <= char <= "z":
        encrypted_text += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        encrypted_text += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    else:
        encrypted_text += char

with open("private.txt", "w", encoding="UTF-8") as file:
    file.write(encrypted_text)

# +
# 20

with open("numbers.num", "rb") as file:
    total_sum = 0
    while chunk := file.read(2):
        if len(chunk) < 2:
            continue
        total_sum += int.from_bytes(chunk, byteorder="big")

print(total_sum % 2**16)
