"""Data types."""

A1 = 25
B1 = 2.5
C1 = 3 + 25j

D1 = 2e3
print(D1)
print(type(D1))

print(2 + 2, 4 - 2, 2 * 2, 4 / 2, 2**3)

print(7 // 2)
print(7 % 2)

# +
FIRST_NUMBER = 2
SECOND_NUMBER = 4
THIRD_NUMBER = 3

print(FIRST_NUMBER == SECOND_NUMBER)
print(FIRST_NUMBER != SECOND_NUMBER)
print(SECOND_NUMBER > FIRST_NUMBER and FIRST_NUMBER != THIRD_NUMBER)
# -

print(4 > 2 and 2 != 3)
print(4 < 2 or 2 == 2)
print(not (4 == 4))

# +
D2 = 25

BIN_D = bin(D2)
print(BIN_D)

print(int(BIN_D, 2))
# -

STRING_1 = "строка"
STRING_2 = "строка"

MYLTI_STRING = """ArithmeticError,
пцолпоцп,
абецп."""

len(MYLTI_STRING)

A2, B2, C2 = "Программирование", "на", "Python"
A2 + " " + B2 + " " + C2

print(MYLTI_STRING[0])
print(MYLTI_STRING[-1])

print(MYLTI_STRING[3:10])

print(MYLTI_STRING[:2])
print(MYLTI_STRING[3:])

for i in "питон":
    print(i)

print("***15 849 302***".strip("*"))
print(" 15 849 302 ".strip())

print(MYLTI_STRING.split())

len(MYLTI_STRING.split())

# +
DATA = "20,25"

DATA = DATA.replace(",", ".")

DATA = float(DATA)
print(DATA)
print(type(DATA))
# -

VAR = True
type(VAR)

if VAR == True:
    print("Переменная VAR имеет значение True")
else:
    print("Переменная VAR имеет значение False")

list_1 = [1, 2, 3, 4, 5]
str(list_1)

# +
list_str = []
for X5 in list_1:
    list_str.append(str(X5))

print(list_str)
# -

[str(X6) for X6 in list_1]

list(map(str, list_1))
