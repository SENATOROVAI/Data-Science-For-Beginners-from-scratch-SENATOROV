"""Yandex handbook "Python Basics" answers."""

# +
# 1
test_count_1: int = 2
words_1: list[str] = ["абрикос", "бобр"]

valid_all_1: bool = True

for word_1 in words_1:
    if word_1[0] not in "абв":
        valid_all_1 = False

print("YES" if valid_all_1 else "NO")

# +
# 2
max_len_3: int = 25
lines_3: list[str] = [
    "Экономика вошла в период рецессии",
    "Развитие новых технологий в области ИИ",
]

for line_3 in lines_3:
    if len(line_3) <= max_len_3:
        print(line_3)
    else:
        print(f"{line_3[:max_len_3 - 3]}...")

# +
# 3
allowed_length_3: int = 25
texts_to_truncate_3: list[str] = [
    "Экономика вошла в период рецессии",
    "Развитие новых технологий в области ИИ",
]

for phrase_3 in texts_to_truncate_3:
    if len(phrase_3) <= allowed_length_3:
        print(phrase_3)
    else:
        print(f"{phrase_3[:allowed_length_3 - 3]}...")

# +
# 4
entries_4: list[str] = [
    "##Hello, world",
    "Goodbye",
    "End@@@",
]

for item_4 in entries_4:
    if item_4.endswith("@@@"):
        continue
    if item_4.startswith("##"):
        item_4 = item_4[2:]
    print(item_4)

# +
# 5
word_5: str = "топот"

print("YES" if word_5 == word_5[::-1] else "NO")
# -

# 6
texts_6: list[str] = ["зайка в лесу", "зайка и волк", "зайка бежит"]
total_bunnies_6: int = sum(text.count("зайка") for text in texts_6)
print(total_bunnies_6)

# 7
raw_input_7: str = "1 3"
parts_7: list[str] = list(raw_input_7.split())
result_7: int = int(parts_7[0]) + int(parts_7[1])
print(result_7)

# +
# 8
places_8: list[str] = [
    "зайка у куста",
    "лиса в норе",
    "зайка на поле",
    "медведь",
]

for place_8 in places_8:
    if "зайка" in place_8:
        print(place_8.index("зайка") + 1)
    else:
        print("Заек нет =(")

# +
# 9
code_lines_9: list[str] = [
    "for i in range(10): # цикл",
    "print(i)",
    "",
]

for line_9 in code_lines_9:
    if not line_9:
        continue
    pos_9: int = line_9.find("#")
    if pos_9 == -1:
        print(line_9)
    elif pos_9 > 0:
        print(line_9[:pos_9])
    else:
        pass

# +
# 10
votes_10: list[str] = [
    "привет мир",
    "мир и дружба",
    "мир",
    "ФИНИШ",
]

chars_10: list[str] = []
counts_10: list[int] = []

for line_10 in votes_10:
    if line_10 == "ФИНИШ":
        break
    clean_10: str = line_10.lower().replace(" ", "")
    for ch_10 in clean_10:
        if ch_10 in chars_10:
            idx_10: int = chars_10.index(ch_10)
            counts_10[idx_10] += 1
        else:
            chars_10.append(ch_10)
            counts_10.append(1)

max_cnt_10: int = max(counts_10) if counts_10 else 0
candidates_10: list[str] = [
    ch for ch, cnt in zip(chars_10, counts_10) if cnt == max_cnt_10
]
candidates_10.sort()
print(candidates_10[0] if candidates_10 else "")

# +
# 11
titles_11: list[str] = [
    "Гугл внедрил новую фичу в поисковую систему",
    "Капитализация Гугла выросла на 10 млрд. долларов США",
    "Яндекс представил новый алгоритм",
]
search_term_11: str = "гугл"

for title_11 in titles_11:
    if search_term_11.lower() in title_11.lower():
        print(title_11)

# +
# 12
menu_12: list[str] = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
days_12: int = 4

for day_12 in range(days_12):
    print(menu_12[day_12 % len(menu_12)])

# +
# 13
values_13: list[int] = [2, 3, 4]
exp_13: int = 3

for val_13 in values_13:
    print(val_13**exp_13)

# +
# 14
data_14: str = "2 3 4"
power_14: int = 3

nums_14: list[int] = [int(x) for x in data_14.split()]

for num_14 in nums_14:
    print(num_14**power_14, end=" ")
print()

# +
# 15
numbers_15: list[int] = [12, 18, 24]

gcd_val_15: int = numbers_15[0]
for num_15 in numbers_15[1:]:
    a_15, b_15 = gcd_val_15, num_15
    while b_15:
        a_15, b_15 = b_15, a_15 % b_15
    gcd_val_15 = a_15

print(gcd_val_15)

# +
# 16
budget_16: int = 25
lines_16: list[str] = ["Последние новости текущего дня"]

for line_16 in lines_16:
    if budget_16 <= 0:
        break
    if len(line_16) <= budget_16:
        print(line_16)
        budget_16 -= len(line_16)
    else:
        if budget_16 > 3:
            print(line_16[: budget_16 - 3] + "...")
            budget_16 = 0
        elif budget_16 == 3:
            print("...")
            budget_16 = 0

# +
# 17
phrase_17: str = "А роза упала на лапу Азора"

clean_17: str = phrase_17.replace(" ", "").lower()
print("YES" if clean_17 == clean_17[::-1] else "NO")

# +
# 18
seq_18: str = "010000100001111111110111110000000000000011111111"

current_18: str = seq_18[0]
count_18: int = 1

for ch_18 in seq_18[1:]:
    if ch_18 == current_18:
        count_18 += 1
    else:
        print(current_18, count_18)
        current_18 = ch_18
        count_18 = 1

print(current_18, count_18)

# +
# 19
rpn_expr_19: str = "7 2 3 * -"
tokens_19: list[str] = list(rpn_expr_19.split())

stack_19: list[int] = []

for token_19 in tokens_19:
    if token_19 in "+-*/":
        b_19 = stack_19.pop()
        a_19 = stack_19.pop()
        if token_19 == "+":
            stack_19.append(a_19 + b_19)
        elif token_19 == "-":
            stack_19.append(a_19 - b_19)
        elif token_19 == "*":
            stack_19.append(a_19 * b_19)
        elif token_19 == "/":
            stack_19.append(int(a_19 / b_19))
    else:
        stack_19.append(int(token_19))

print(stack_19[0])

# +
# 20
expr_20: str = "7 1 10 100 # * ! ~ 100 / @ -"
tokens_20: list[str] = list(expr_20.split())

stack_20: list[int] = []

for token_20 in tokens_20:
    if token_20 == "~":
        op_20 = stack_20.pop()
        stack_20.append(-op_20)
    elif token_20 == "#":
        op_20 = stack_20.pop()
        stack_20.append(op_20)
        stack_20.append(op_20)
    elif token_20 == "!":
        op_20 = stack_20.pop()
        fact_20 = 1
        for i_20 in range(1, op_20 + 1):
            fact_20 *= i_20
        stack_20.append(fact_20)
    elif token_20 == "@":
        c_20 = stack_20.pop()
        b_20 = stack_20.pop()
        a_20 = stack_20.pop()
        stack_20.extend([b_20, c_20, a_20])
    elif token_20 in "+-*/":
        b_20 = stack_20.pop()
        a_20 = stack_20.pop()
        if token_20 == "+":
            stack_20.append(a_20 + b_20)
        elif token_20 == "-":
            stack_20.append(a_20 - b_20)
        elif token_20 == "*":
            stack_20.append(a_20 * b_20)
        elif token_20 == "/":
            stack_20.append(a_20 // b_20)
    else:
        stack_20.append(int(token_20))

print(stack_20[0])
