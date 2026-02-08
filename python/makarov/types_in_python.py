"""Типы данных в python."""

# ### Работа с числами

integer_number = 25  # целое число
float_number = 2.5  # вещественное число
complex_number = 3 + 25j  # комплексное число

# стандартный вид
scientific_number = 2e3  # 2 * 10^3
print(scientific_number)
print(type(scientific_number))

# Арифметические операции

print(2 + 2, 4 - 2, 2 * 2, 4 / 2, 2**3)

# целая часть
print(7 // 2)
# остаток
print(7 % 2)

# Операторы сравнения

left_value = 2
right_value = 4
print(left_value == right_value)
print(left_value != right_value)

# Логические операции

left_number = 2
right_number = 3
print(4 > left_number and left_number != right_number)

# Перевод чисел в другую систему счисления

# +
decimal_number = 25

# двоичная система
binary_repr = bin(decimal_number)
print(binary_repr)

# обратно в десятичную
print(int(binary_repr, 2))

# +
decimal_number = 25

# восьмиричная
octal_repr = oct(decimal_number)
print(octal_repr)

# обратно в десятичную
print(int(octal_repr, 8))

# +
decimal_number = 25

# шестнадцатиричная
hex_repr = hex(decimal_number)
print(hex_repr)

# обратно в десятичную
print(int(hex_repr, 16))
# -

# ### Строковые данные

string1 = "строка"
string2 = "это тоже строка"

multi_string = """Мы все учились понемногу
Чему-нибудь и как-нибудь,
Так воспитаньем, слава богу,
У нас немудрено блеснуть."""

# Длина строки

# воспользуемся функцией len()
len(multi_string)

# Объединение строк

# +
word_1, word_2, word_3 = "Программирование", "на", "python"

word_1 + " " + word_2 + " " + word_3
# -

# Индекс символа в строке

print(multi_string[0])
print(multi_string[-1])

# Срезы строк

print(multi_string[3:6])
print(multi_string[:6])
print(multi_string[3:])

# Циклы в строках

for i in "Python":
    print(i)

# Методы .strip() и .split()

print("***15 343 212*****".strip("*"))
print("   15 343 212      ".strip("*"))

print(multi_string.split())

len(multi_string.split())

# Замена символа в строке

data = "20.25"
data = data.replace(",", ".")
data_float = float(data)
print(data_float)
print(type(data_float))

# Логические значения

is_true = False
type(is_true)

if is_true:
    print("Значение переменной истинно")
else:
    print("Значение переменной ложно")
