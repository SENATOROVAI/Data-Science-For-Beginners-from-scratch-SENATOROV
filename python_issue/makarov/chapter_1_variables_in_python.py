"""Variables in Python."""

# ## Переменные в Питоне

# ### Создание (объявление) переменных
#

x_var: int = 15
print(x_var)

y_var: str = "Я программирую на Питоне"
print(y_var)

# +
a_var: str = "Python"
b_var: str = "C++"
c_var: str = "PHP"

print(a_var, b_var, c_var)
# -

x_var_1 = y_var_1 = z_var_1 = "same value"
print(x_var_1, y_var_1, z_var_1)

my_list: list[str] = ["tomatoes", "cucumbers", "potatoes"]
a_var_1, b_var_1, c_var_1 = my_list
print(a_var_1, b_var_1, c_var_1)

# ### Автоматическое определение типа данных
#

# +
x_var_2: int = 256
y_var_2: float = 0.25
z_var_2: str = "just text"

# Как узнать тип переменной в Питоне
print(type(x_var_2), type(y_var_2), type(z_var_2))
# -

# ### Присвоение и преобразование типа данных

# #### Присвоение типа данных
#

# +
x_var_3: str = str(25)
y_var_3: int = int(25)
z_var_3: float = float(25)

print(type(x_var_3), type(y_var_3), type(z_var_3))
# -

# #### Изменение типа данных

# Изменение типа данных
print(type(int("25")))
print(type(float("2.5")))
print(int("36.6"))
print(type(int("36.6")))
print(type(str(25)))
print(str)

# ### Именование переменных

# #### Допустимые имена переменных

# variable: str = "just variable"
# _variable: str = "just variable"
variable_: str = "just variable"
my_variable: str = "just variable"
My_variable_123: str = "just variable"

# #### Имя переменной состоит из нескольких слов
#

# camelCaseVariable: str = "camel case variable"
# PascalCaseVariable: str = "pascal case variable"
snake_case_variable: str = "snake case variable"

# #### Недопустимые названия переменной

# +
# my-variable = 'WRONG'
# 123variable = 'WRONG'
# my variable = 'WRONG'
# -

# ### Как конвертировать список чисел в строки
#

# +
list_: list[int] = [1, 2, 3]
str(list_)  # -> Wrong answer

# 1
list_str: list[str] = []

for i in list_:
    list_str.append(str(i))

print(list_str)

# 2
print([str(x) for x in list_])

# 3
print(list(map(str, list_)))
