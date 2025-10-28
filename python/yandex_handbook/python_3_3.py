"""Yandex handbook "Python Basics" answers."""

# +
# 1
start_a: int = 2
end_a: int = 5

result_a: list[int] = []
for num_a in range(start_a, end_a + 1):
    result_a.append(num_a**2)

print(result_a)

# +
# 2
start_b: int = 5
end_b: int = 2

step_b: int = 1 if start_b < end_b else -1
result_b: list[int] = []

for num_b in range(start_b, end_b + step_b, step_b):
    result_b.append(num_b**2)

print(result_b)

# +
# 3
start_c: int = 1
end_c: int = 10
divisor_c: int = 3

result_c: list[int] = []
for num_c in range(start_c, end_c + 1):
    if num_c % divisor_c == 0:
        result_c.append(num_c)

print(result_c)

# +
# 4
numbers_d: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_set_d: set[int] = set()
for num_d in numbers_d:
    if num_d % 2 == 1:
        odd_set_d.add(num_d)

print(odd_set_d)

# +
# 5
numbers_e: list[int] = [1, 2, 4, 5, 9, 10, 16]

max_val_e: int = max(numbers_e) if numbers_e else 0
squares_e: set[int] = set()

for i_e in range(1, int(max_val_e**0.5) + 1):
    squares_e.add(i_e * i_e)

full_squares_e: set[int] = set()
for num_e in numbers_e:
    if num_e in squares_e:
        full_squares_e.add(num_e)

print(full_squares_e)

# +
# 6
sentence_f: str = "Привет мир Python"

lengths_f: list[int] = []
for word_f in sentence_f.split():
    lengths_f.append(len(word_f))

print(lengths_f)

# +
# 7
text_g: str = "Привет123мир456"

digits_g: str = ""
for ch_g in text_g:
    if ch_g.isdigit():
        digits_g += ch_g

print(digits_g)

# +
# 8
phrase_h: str = "Центральный процессорный блок"

abbr_h: str = ""
for word_h in phrase_h.split():
    if word_h:
        abbr_h += word_h[0]

print(abbr_h.upper())

# +
# 9
numbers_i: list[int] = [3, 1, 4, 1, 5, 9, 2, 6]

unique_sorted_i: list[int] = sorted(set(numbers_i))
result_i: str = " - ".join(str(x) for x in unique_sorted_i)

print(result_i)

# +
# 10
words_j: str = "машина пианино аэробус океан"
vowels_j: str = "аяуюоёэеиыaeiouy"

selected_j: list[str] = []
for word_j in words_j.split():
    vowel_count_j: int = 0
    for ch_j in word_j:
        if ch_j.lower() in vowels_j:
            vowel_count_j += 1
    if vowel_count_j >= 3:
        selected_j.append(word_j)

print(selected_j)

# +
# 11
numbers_k: list[int] = [1, 2, 3, 2, 4, 5, 4]

unique_vals_k: set[int] = set()
for num_k in numbers_k:
    if numbers_k.count(num_k) == 1:
        unique_vals_k.add(num_k)

print(unique_vals_k)

# +
# 12
numbers_l: list[int] = [1, 2, 3, 4]

max_prod_l: int = numbers_l[0] * numbers_l[1]

for i_l, x_l in enumerate(numbers_l):
    for y_l in numbers_l[i_l + 1:]:
        prod_l = x_l * y_l
        if prod_l > max_prod_l:
            max_prod_l = prod_l

print(max_prod_l)

# +
# 13
data_m: dict[str, list[int]] = {
    "a": [1, 2],
    "b": [1, 1],
    "c": [2, 2],
}

candidates_m: list[str] = list(data_m.keys())
best_key_m: str = candidates_m[0]

for key_m in candidates_m[1:]:
    sum_current_m: int = sum(data_m[key_m])
    sum_best_m: int = sum(data_m[best_key_m])
    if (sum_current_m, key_m) < (sum_best_m, best_key_m):
        best_key_m = key_m

print(best_key_m)

# +
# 14
data_n: dict[str, list[int]] = {
    "x": [1, 2, 3],
    "y": [1, 1, 2],
    "z": [4, 5, 6],
}

bad_keys_n: set[str] = set()
for key_n, values_n in data_n.items():
    if len(values_n) != len(set(values_n)):
        bad_keys_n.add(key_n)

print(bad_keys_n)

# +
# 15
text_o: str = "Hello, World!"

letter_counts_o: dict[str, int] = {}
clean_text_o: str = text_o.lower()

for ch_o in clean_text_o:
    if ch_o.isalpha():
        letter_counts_o[ch_o] = letter_counts_o.get(ch_o, 0) + 1

print(letter_counts_o)

# +
# 16
rle_p: list[tuple[str, int]] = [("a", 3), ("b", 2), ("c", 1)]

decoded_p: str = ""
for char_p, count_p in rle_p:
    decoded_p += char_p * count_p

print(decoded_p)

# +
# 17
size_q: int = 3

table_q: list[list[int]] = []
for i_q in range(1, size_q + 1):
    row_q: list[int] = []
    for j_q in range(1, size_q + 1):
        row_q.append(i_q * j_q)
    table_q.append(row_q)

print(table_q)

# +
# 18
numbers_r: list[int] = [6, 8, 9]

divisors_r: dict[int, list[int]] = {}
for num_r in numbers_r:
    divisors_r[num_r] = []
    for d_r in range(1, num_r + 1):
        if num_r % d_r == 0:
            divisors_r[num_r].append(d_r)

print(divisors_r)

# +
# 19
numbers_s: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

primes_s: set[int] = set()
for num_s in numbers_s:
    if num_s > 1:
        is_prime_s: bool = True
        for div_s in range(2, int(num_s**0.5) + 1):
            if num_s % div_s == 0:
                is_prime_s = False
                break
        if is_prime_s:
            primes_s.add(num_s)

print(primes_s)

# +
# 20
text_t: str = "мир мирный миролюбивый"

words_t: list[str] = list(text_t.split())
pairs_t: set[tuple[str, str]] = set()

for i_t, w1_t in enumerate(words_t):
    for w2_t in words_t[i_t + 1:]:
        if len(set(w1_t) & set(w2_t)) >= 3:
            if w1_t <= w2_t:
                pair_t = (w1_t, w2_t)
            else:
                pair_t = (w2_t, w1_t)
            pairs_t.add(pair_t)

print(pairs_t)
