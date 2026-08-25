"""Data types in Python."""

# ## Типы данных в Питоне
#

# ### Работа с числами
#

# +
a_var: int = 25
b_var: float = 2.5
c_var: complex = 3 + 25j

print(a_var, b_var, c_var)
# -

# ##### Экспоненциальная запись, 2 умножить на 10 в степени 3
#

d_var: float = 2e3
print(d_var)
print(type(d_var))

# #### Арифметические операции

# Ниже закомментил потому что линтеры сильно ругаются на операции итак понятные
print(2 + 2, 4 - 2, 2 * 2, 4 / 2, 2**3)

print(7 // 2)
print(7 % 2)

# #### Операторы сравнения
#

# +
# print(2 == 4)
# print(2 != 4)
# -

# #### Логические операции

# +
# print(4 > 2 and 2 != 3)
# print(4 < 2 or 2 == 2)
# print(not (4 == 4))
# -

# #### Перевод чисел в другую систему счисления
#

# +
d_var_1: int = 25

bin_d: str = bin(d_var_1)
print(bin_d)

print(int(bin_d, 2))

# +
d_var_2: int = 25

oct_d: str = oct(d_var_2)
print(oct_d)

print(int(oct_d, 8))

# +
d_var_3: int = 25

hex_d: str = hex(d_var_3)
print(hex_d)

print(int(hex_d, 16))
# -

# ### Строковые данные

# +
string_1: str = "string"
string_2: str = "also string"

multi_string: str = """Мы все учились понемногу
Чему-нибудь и как-нибудь,
Так воспитаньем, слава богу,
У нас немудрено блеснуть."""
# -

# #### Длина строки

len(multi_string)

# #### Объединение строк
#

a_var_3: str = "programming"
b_var_3: str = "on"
c_var_3: str = "python"
a_var_3 + " " + b_var_3 + " " + c_var_3

# #### Индекс символа в строке и Срезы строк

# +
print(multi_string[0])
print(multi_string[-1])

print(multi_string[3:6])
print(multi_string[:2])
print(multi_string[3:])
# -

# #### Циклы в строках

for i in "Python":
    print(i)

# #### Методы .strip() и .split()

# +
print("********15 489 302**************".strip("*"))

print("       15 849 302            ".strip())
# -

print(multi_string.split())

len(multi_string.split())

# #### Замена символа в строке

# +
data_var_3: str = "20,25"

data_var_3_clean: str = data_var_3.replace(",", ".")

data_var_3_float: float = float(data_var_3_clean)
print(data_var_3_float)
print(type(data_var_3_float))
# -

# ### Логические значения

var_var_3: bool = False
type(var_var_3)

if var_var_3 is True:
    print("var is true")
else:
    print("var is false")
