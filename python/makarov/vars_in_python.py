"""Переменные в Python."""

# ### Создание (объявление) переменных

number_value = 15
print(number_value)

text_value = "Я программирую на Питоне"
print(text_value)

language_1, language_2, language_3 = "Питон", "С++", "PHP"
print(language_1, language_2, language_3)

same_text_1 = same_text_2 = same_text_3 = "То же самое значение"
print(same_text_1, same_text_2, same_text_3)

my_list = ["помидоры", "огурцы", "картофель"]
vegetable_1, vegetable_2, vegetable_3 = my_list
print(vegetable_1, vegetable_2, vegetable_3)

# ### Автоматическое определение типа данных

example_int = 256
example_float = 0.25
example_str = "Просто текст"

# ### Как узнать тип переменной

print(type(example_int), type(example_float), type(example_str))

# ### Присвоение и преобразования типа данных

# Присвоение типа данных

string_number = str(25)
int_number = int(25)
float_number = float(25)

print(type(string_number), type(int_number), type(float_number))

# Изменение типа данных

print(type(int("25")))

print(type(float("2.5")))

print(int(36.6))
print(type(int(36.6)))

print(type(str(25)))
print(type(str(36.6)))

# ### Именование переменных

# Допустимые имена переменных

example_variable = "просто переменная"
_variable = "защищённая переменная"
__variable = "приватная переменная"
variable_ = "просто переменная"
my_variable = "просто переменная"
My_variable_123 = "просто переменная"

# Имя переменной состоит из нескольких слов

camel_case_variable = "Верблюжий регистр"
pascal_case_variable = "Нотация Паскаль"
snake_case_variable = "Змеиная нотация"

# ### Способы преобразовать список чисел, чтобы каждое из них стало строкой

list_ = [1, 2, 3]

# +
list_str = []

for number_item in list_:
    list_str.append(str(number_item))

list_str
# -

print([str(number_item) for number_item in list_])

list(map(str, list_))
