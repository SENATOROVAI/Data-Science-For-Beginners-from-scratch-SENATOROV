"""Yandex handbook "Python Basics" answers."""

# +
import json
from typing import Dict, List, Set, Union

# 1
summa_1: int = 0
test_data_1_1: List[str] = ["1 2 3", "4 5 6", "7 8 9"]
for line_1 in test_data_1_1:
    for item_1 in line_1.split():
        summa_1 += int(item_1)
print(summa_1)
# -

# 2
total_difference_2: int = 0
test_data_2_1: List[str] = ["A 10 15", "B 20 25", "C 30 35"]
for line_2 in test_data_2_1:
    identifier_2, previous_value_str_2, current_value_str_2 = line_2.split()
    previous_value_2: int = int(previous_value_str_2)
    current_value_2: int = int(current_value_str_2)
    total_difference_2 += current_value_2 - previous_value_2
average_difference_2: int = round(total_difference_2 / len(test_data_2_1))
print(average_difference_2)

# 3
test_data_3_1: List[str] = [
    "print('Hello')  # Комментарий",
    "# Только комментарий",
    "",
    "code_without_comment",
]
for raw_line_3 in test_data_3_1:
    if raw_line_3 == "\n":
        print(raw_line_3, end="")
    elif raw_line_3 and raw_line_3[0] != "#":
        comment_position_3: int = raw_line_3.find("# ")
        if comment_position_3 != -1:
            raw_line_3 = raw_line_3[:comment_position_3]
        if raw_line_3.endswith("\n"):
            raw_line_3 = raw_line_3[:-1]
        print(raw_line_3)
print("What is your name?")
name_3: str = "Иван"
print(f"Hello, {name_3}!")

# 4
clean_lines_4: List[str] = [
    "Яндекс выпустил задачник по программированию",
    "Как заказать Яндекс.Такси?!",
    "Новости технологий",
]
search_query_1_4: str = "яндекс"
for title_4 in clean_lines_4:
    if search_query_1_4.lower() in title_4.lower():
        print(title_4)

# 5
palindromic_words_5: List[str] = []
test_data_5_1: List[str] = ["Анна и Дед", "топот и шалаш", "Ара и Я"]
for line_5 in test_data_5_1:
    if line_5.endswith("\n"):
        line_5 = line_5[:-1]
    word_list_5: List[str] = line_5.split()
    for word_5 in word_list_5:
        upper_word_5: str = word_5.upper()
        if upper_word_5 == upper_word_5[::-1]:
            palindromic_words_5.append(word_5)
unique_sorted_words_5: List[str] = sorted(set(palindromic_words_5))
print("\n".join(unique_sorted_words_5))

# 6
cyrillic_to_latin_6: Dict[str, str] = {
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
test_input_6: str = "Привет, мир!"
transliterated_text_6: str = ""
for char_6 in test_input_6:
    upper_char_6: str = char_6.upper()
    if upper_char_6 in cyrillic_to_latin_6:
        latin_equivalent_6: str = cyrillic_to_latin_6[upper_char_6]
        if char_6.isupper():
            transliterated_char_6: str = latin_equivalent_6.capitalize()
        else:
            transliterated_char_6 = latin_equivalent_6.lower()
    else:
        transliterated_char_6 = char_6
    transliterated_text_6 += transliterated_char_6
print(transliterated_text_6)

# 7
file_content_7: str = "1 -2 3 -4 5 6 -7 8 9 10 -5 20 0 15"
integer_list_7: List[int] = []
for token_7 in file_content_7.split():
    integer_list_7.append(int(token_7))
total_count_7: int = len(integer_list_7)
positive_count_7: int = 0
for number_7 in integer_list_7:
    if number_7 > 0:
        positive_count_7 += 1
minimum_value_7: int = integer_list_7[0]
maximum_value_7: int = integer_list_7[0]
total_sum_7: int = 0
for number_7 in integer_list_7:
    minimum_value_7 = min(minimum_value_7, number_7)
    maximum_value_7 = max(maximum_value_7, number_7)
    total_sum_7 += number_7
average_value_7: float = total_sum_7 / total_count_7
print(total_count_7)
print(positive_count_7)
print(minimum_value_7)
print(maximum_value_7)
print(total_sum_7)
print(f"{average_value_7:.2f}")

# 8
words_from_file_1_8: Set[str] = {"чай", "кофе", "молоко", "печенье"}
words_from_file_2_8: Set[str] = {"кофе", "пряник", "жвачка", "чай"}
unique_words_8: Set[str] = words_from_file_1_8 ^ words_from_file_2_8
output_content_8: str = ""
for word_8 in sorted(unique_words_8):
    output_content_8 += word_8 + "\n"
print(output_content_8)

# 9
test_input_9: List[str] = [
    "  очень   плохо   форматированный   текст  ",
    "нуну",
    "  прямо  ",
    "  очень-очень  ",
]
cleaned_lines_9: List[List[str]] = []
for raw_line_9 in test_input_9:
    tokens_9: List[str] = raw_line_9.strip().replace("\t", "").split()
    if any(tokens_9):
        cleaned_lines_9.append(tokens_9)
output_content_9: str = ""
for token_list_9 in cleaned_lines_9:
    output_content_9 += " ".join(token_list_9) + "\n"
print(output_content_9)

# 10
lines_10: List[str] = [
    "1 строка", "2 строка", "3 строка", "4 строка", "5 строка"]
lines_to_print_10: int = 2
for line_10 in lines_10[-lines_to_print_10:]:
    print(line_10.strip())

# 11
number_list_11: List[int] = [1, -2, 3, -4, 5, 6, -7, 8, 9, 10, -5, 20, 0, 15]
number_count_11: int = len(number_list_11)
positive_count_2_11: int = 0
for num_11 in number_list_11:
    if num_11 > 0:
        positive_count_2_11 += 1
minimum_value_2_11: int = number_list_11[0]
maximum_value_2_11: int = number_list_11[0]
total_sum_2_11: int = 0
for num_11 in number_list_11:
    minimum_value_2_11 = min(minimum_value_2_11, num_11)
    maximum_value_2_11 = max(maximum_value_2_11, num_11)
    total_sum_2_11 += num_11
average_value_2_11: float = round(total_sum_2_11 / number_count_11, 2)
statistics_11: Dict[str, Union[int, float]] = {
    "count": number_count_11,
    "positive_count": positive_count_2_11,
    "min": minimum_value_2_11,
    "max": maximum_value_2_11,
    "sum": total_sum_2_11,
    "average": average_value_2_11,
}
json_output_11: str = json.dumps(statistics_11, ensure_ascii=False, indent=4)
print(json_output_11)

# 12
test_lines_12: List[str] = [
    "629700 650975472 42161437 591084323 577023 1504180",
    "8460612246 58531725 29409368 5725268 2198001838",
    "796451 69358 7195510 9756641 975628465",
    "979391 93479581 291170 44200289 28987042",
]
even_digits_12: Set[str] = set("02468")
odd_digits_12: Set[str] = set("13579")
even_numbers_12: List[str] = []
odd_numbers_12: List[str] = []
equal_numbers_12: List[str] = []
for line_12 in test_lines_12:
    for number_str_12 in line_12.split():
        even_count_12: int = 0
        odd_count_12: int = 0
        for char_12 in number_str_12:
            if char_12 in even_digits_12:
                even_count_12 += 1
            elif char_12 in odd_digits_12:
                odd_count_12 += 1
        if even_count_12 > odd_count_12:
            even_numbers_12.append(number_str_12)
        elif odd_count_12 > even_count_12:
            odd_numbers_12.append(number_str_12)
        else:
            equal_numbers_12.append(number_str_12)
print(" ".join(even_numbers_12))
print(" ".join(odd_numbers_12))
print(" ".join(equal_numbers_12))

# 13
data_13: Dict[str, str] = {"one": "один", "three": "три"}
test_updates_13: List[str] = ["two == два"]
for line_13 in test_updates_13:
    if "==" in line_13:
        key_13, value_13 = line_13.split("==", maxsplit=1)
        data_13[key_13.strip()] = value_13.strip()
json_output_13: str = json.dumps(
    data_13, sort_keys=False, indent=4, ensure_ascii=False)
print(json_output_13)

# 14
source_data_14: List[Dict[str, Union[str, int]]] = [
    {"name": "Ann", "address": "Flower st.", "phone": "+7 (098) 765-43-21"},
    {"name": "Bob", "address": "Winter st.", "phone": "+7 (123) 456-78-90"},
]
update_data_14: List[Dict[str, Union[str, int]]] = [
    {"name": "Ann", "phone": "+7 (111) 222-33-44"},
    {"name": "Bob", "address": "Summer st."},
]
name_key_14: str = "name"
merged_data_14: Dict[str, Dict[str, Union[str, int]]] = {}
for record_14 in source_data_14:
    name_14: str = str(record_14[name_key_14])
    merged_data_14[name_14] = {}
    for key_14, value_14 in record_14.items():
        if key_14 != name_key_14:
            merged_data_14[name_14][key_14] = value_14
for update_14 in update_data_14:
    name_14 = str(update_14[name_key_14])
    if name_14 not in merged_data_14:
        merged_data_14[name_14] = {}
    for key_14, new_value_14 in update_14.items():
        if key_14 == name_key_14:
            continue
        old_value_14 = merged_data_14[name_14].get(key_14)
        if isinstance(new_value_14, (int, float)) and isinstance(
            old_value_14, (int, float)
        ):
            if new_value_14 > old_value_14:
                merged_data_14[name_14][key_14] = new_value_14
        elif isinstance(new_value_14, str) and isinstance(old_value_14, str):
            if new_value_14 > old_value_14:
                merged_data_14[name_14][key_14] = new_value_14
        elif old_value_14 is None:
            merged_data_14[name_14][key_14] = new_value_14
json_output_14: str = json.dumps(merged_data_14, indent=4, ensure_ascii=False)
print(json_output_14)

# 15
test_blocks_15: List[Dict[str, object]] = [
    {
        "points": "50",
        "tests": [
            {"pattern": "42", "answer": ""},
            {"pattern": "hello", "answer": ""}
        ]
    }
]
total_score_15: int = 0
user_responses_15: List[str] = ["42", "hello"]
response_index_15: int = 0
for test_block_15 in test_blocks_15:
    questions_15 = test_block_15["tests"]
    points_value = test_block_15["points"]
    if isinstance(questions_15, list) and isinstance(points_value, str):
        points_raw_15: int = int(points_value)
        points_per_question_15: int = points_raw_15 // len(questions_15)
        for question_15 in questions_15:
            if isinstance(question_15, dict) and "pattern" in question_15:
                expected_answer_15: str = str(question_15["pattern"])
                user_response_15: str = user_responses_15[response_index_15]
                response_index_15 += 1
                if user_response_15 == expected_answer_15:
                    total_score_15 += points_per_question_15
print(total_score_15)

# 16
search_query_16: str = "test"
file_contents_16: List[str] = ["This is a test content", "No match here"]
match_found_16: bool = False
for content_16 in file_contents_16:
    raw_text_16: str = content_16.replace("\xa0", " ").lower()
    content_cleaned_16: str = " ".join(raw_text_16.split())
    if search_query_16.lower() in content_cleaned_16:
        print("test.txt")
        match_found_16 = True
        break
if not match_found_16:
    print("404. Not Found")

# 17
encoded_text_1_17: str = "Hello, world!"
decoded_text_17: str = ""
for character_17 in encoded_text_1_17:
    code_point_17: int = ord(character_17)
    if code_point_17 >= 128:
        normalized_code_17: int = code_point_17 % 256
    else:
        normalized_code_17 = code_point_17
    decoded_text_17 += chr(normalized_code_17)
print(decoded_text_17)

# 18
file_size_18: int = 193
size_units_18: List[str] = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
unit_index_18: int = 0
while file_size_18 > 1024 and unit_index_18 < len(size_units_18) - 1:
    quotient_18: int
    remainder_18: int
    quotient_18, remainder_18 = divmod(file_size_18, 1024)
    file_size_18 = quotient_18 + int(remainder_18 > 0)
    unit_index_18 += 1
print(f"{file_size_18}{size_units_18[unit_index_18]}")

# 19
alphabet_19: str = "abcdefghijklmnopqrstuvwxyz"
shift_value_19: int = 3 % len(alphabet_19)
shifted_alphabet_19: str = (
    alphabet_19[shift_value_19:] + alphabet_19[:shift_value_19]
)
cipher_map_19: Dict[str, str] = {}
for original_19, shifted_19 in zip(alphabet_19, shifted_alphabet_19):
    cipher_map_19[original_19] = shifted_19
original_text_19: str = "Hello, world!"
encoded_chars_19: List[str] = []
for char_19 in original_text_19:
    lower_char_19: str = char_19.lower()
    if lower_char_19 in cipher_map_19:
        new_char_19: str = cipher_map_19[lower_char_19]
        if char_19.isupper():
            encoded_chars_19.append(new_char_19.upper())
        else:
            encoded_chars_19.append(new_char_19)
    else:
        encoded_chars_19.append(char_19)
encoded_text_2_19: str = "".join(encoded_chars_19)
print(encoded_text_2_19)

# 20
test_bytes_20: bytes = b"\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00"
byte_chunk_size_20: int = 2
modulo_20: int = 0x10000
total_sum_20: int = 0
index_20: int = 0
while index_20 < len(test_bytes_20):
    chunk_20: bytes = test_bytes_20[index_20: index_20 + byte_chunk_size_20]
    total_sum_20 += int.from_bytes(chunk_20)
    index_20 += byte_chunk_size_20
result_20: int = total_sum_20 % modulo_20
print(result_20)
