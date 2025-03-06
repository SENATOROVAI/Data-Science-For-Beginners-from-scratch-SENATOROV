"""List, memory model."""

# ### Example of size estimation
#
# ```python
# from sys import getsizeof
#
# # Создаём итератор из одного миллиона целых чисел
# numbers_iter = (i for i in range(10**6))
# # Выводим количество байт, занятых итератором
# print(f"Итератор занимает {getsizeof(numbers_iter)} байт.")
# # Создаём список
# numbers_list = list(range(10**6))
# # Выводим количество байт, занятых списком
# print(f"Список занимает {getsizeof(numbers_list)} байт.")
# ```
#
#
# ### Example of time estimation
#
# ```python
# from timeit import timeit
#
# print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number=10), 3))
# print(
#     round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number=10), 3)
# )
# ```
#
#
# In Python, data types can be mutable or immutable, affecting how values are stored in memory. Each variable has a unique identifier, which can be checked using the id() function. When a new value is assigned to a variable, its identifier changes, indicating that a new object is created in memory.
#
# ```python
# x = 5
# print(id(x))
# x = 10
# print(id(x))
# ```
#
#
# Immutable data types (int, float, str, tuple, frozenset) can only change their value by creating a new variable with a different identifier. Mutable data types (set, list, dict) can be modified without creating a new variable, keeping the same identifier. Methods like append() and the += operation for lists modify the existing object rather than creating a new one.

# +
# 1

print([value**2 for value in range(int(input()), int(input()) + 1)])

# +
# 2

table_max = int(input())

print(
    [
        [item * mult_val for item in [t_i for t_i in range(1, table_max + 1)]]
        for mult_val in range(1, table_max + 1)
    ]
)

# +
# 3

sentence = input()
print([len(word) for word in sentence.split(" ")])

# +
# 4

lst = list(range(1, 10))
print({number for number in lst if number % 2 != 0})

# +
# 5

inpt_lst = list(range(1, 10))
print({nmb for nmb in inpt_lst if (nmb**0.5).is_integer()})

# +
# 6

text = input()

print(
    {
        character: text.lower().count(character)
        for character in set(text.lower())
        if character.isalpha()
    }
)

# +
# 7

lst_inp = {15, 49, 36}

print({nmb: [i for i in range(1, nmb + 1) if not nmb % i] for nmb in lst_inp})


# +
# 8

full_string = "открытое акционерное общество"
print("".join([word[0].upper() for word in full_string.split(" ")]))

# +
# 9

numbers: list[int] = [3, 1, 2, 3, 2, 2, 1]
print(" - ".join(str(nmb) for nmb in sorted(set(numbers))))

# +
# 10

rle = [("a", 2), ("b", 3), ("c", 1)]
print("".join(["".join(trpl[0] for _ in range(trpl[1])) for trpl in rle]))
