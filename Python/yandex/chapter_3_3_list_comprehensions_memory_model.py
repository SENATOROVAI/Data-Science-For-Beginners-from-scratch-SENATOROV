"""List comprehensions.

Memory model for Python types.
"""

# +
# 1

a_var: int = int(input())
b_var: int = int(input())

print([number**2 for number in range(a_var, b_var + 1)])

# +
# 2

table_size: int = int(input())

multiplication_table: list[list[int]] = [
    [
        column_number * row_number
        for column_number in [num for num in range(1, table_size + 1)]
    ]
    for row_number in range(1, table_size + 1)
]

print(multiplication_table)

# +
# 3

sentence: str = str(input())

print([len(word) for word in sentence.split(" ")])

# +
# 4

numbers_1: list[int] = list(range(1, 20))

print({number for number in numbers_1 if number % 2 == 1})

# +
# 5

numbers_2: list[int] = list(range(1, 20))

print({number for number in numbers_2 if int(number ** (0.5)) ** 2 == number})

# +
# 6

text: str = input()

print(
    {
        letter: text.lower().count(letter)
        for letter in set(text.lower())
        if letter.isalpha()
    }
)

# +
# 7

numbers_3: set[int] = {17, 25, 33, 47}

divisors_map: dict[int, list[int]] = {}

for number in numbers_3:
    divisors: list[int] = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            divisors.append(divider)
    divisors_map[number] = divisors

print(divisors_map)

# +
# 8

contract_type: str = "договор поставки сырья"

words: list[str] = contract_type.split(" ")
initials_list: list[str] = [word[0].upper() for word in words]
abbreviation: str = "".join(initials_list)

print(abbreviation)

# +
# 9

nums: list[int] = [3, 1, 2, 3, 2, 2, 1]

uniq_sorted: list[int] = sorted(set(nums))
str_nums: list[str] = [str(num) for num in uniq_sorted]
output: str = " - ".join(str_nums)

print(output)

# +
# 10

rle: list[tuple[str, int]] = [("a", 2), ("b", 3), ("c", 1)]

expanded_chunks: list[str] = [char * count for char, count in rle]
decoded_string: str = "".join(expanded_chunks)

print(decoded_string)
