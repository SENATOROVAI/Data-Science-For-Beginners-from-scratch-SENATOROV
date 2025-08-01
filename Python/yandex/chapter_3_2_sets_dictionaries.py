"""Sets, dictionaries."""

# +
# 1

string_1: set[str] = set(input())

for char in string_1:
    print(char, end="")

# +
# 2

for char in set(input()) & set(input()):
    print(char, end="")

# +
# 3

items: set[str] = set()

for _ in range(int(input())):
    string_2: str = input()
    items |= set(string_2.split())

for item in items:
    print(item)

# +
# 4

first_list_size: int = int(input())
second_list_size: int = int(input())

first_set: set[str] = set()
second_set: set[str] = set()

for _ in range(first_list_size):
    first_set.add(input())

for _ in range(second_list_size):
    second_set.add(input())

common_elements: set[str] = first_set & second_set

if len(common_elements) != 0:
    print(len(common_elements))
else:
    print("Таких нет")

# +
# 5

total_first_list_size: int = int(input())
total_second_list_size: int = int(input())

unique_names: set[str] = set()
duplicate_names: set[str] = set()

for _ in range(total_first_list_size + total_second_list_size):
    surname: str = input()
    if surname in unique_names:
        duplicate_names.add(surname)
    else:
        unique_names.add(surname)

non_duplicate_surnames: set[str] = unique_names ^ duplicate_names

if len(non_duplicate_surnames) != 0:
    print(len(non_duplicate_surnames))
else:
    print("Таких нет")
