"""Functions.

Scopes. Passing parameters to functions.
"""

# ```python
# # глобальная и локальная переменные не меняются
# def list_modify():
#     sample = [
#         4,
#         5,
#         6,
#     ]  # создалась своя локальная переменная, к-рая не влияет на глобальную
#
#
# sample = [1, 2, 3]
# list_modify()  # присвоение не происходит, тк хоть и переменные под 1 названием но все равно разные объекты
# print(sample)
#
# # Вывод программы:
# # [1, 2, 3]
# ```

# ```python
# # глобальная и локальная переменные меняются
# def list_modify_1(list_arg):
#     # создаём новый локальный список, не имеющий связи с внешним
#     list_arg = [1, 2, 3, 4]
#
#
# def list_modify_2(list_arg):
#     # меняем исходный внешний список, переданный как аргумент
#     list_arg += [4]
#
#
# sample_1 = [1, 2, 3]
# sample_2 = [1, 2, 3]
# list_modify_1(sample_1)
# list_modify_2(sample_2)
# print(sample_1)
# print(sample_2)
#
# # Вывод программы:
# # [1, 2, 3]
# # [1, 2, 3, 4]
# ```

# ```python
# # обращение к глобальной переменной чтобы изменить ее в функции
# # прикол в том что мы не указываем аргументы в функции - поэтому такая болезнь
# # не можем оставить без global, тк причина связана с изменяемостью объектов
# # списки, словари, множества - изменяемые (id будет тем же при изменении (искл. присваивание))
# # числа, кортежи, строки - неизменяемые (при изменении либо будет новый id, либо невозможно произвести что-либо (например, в строках нельзя поменять букву через присваивание; из кортежа нельзя удалить элемент))
# def inc():
#     global x  # меняет глобальную переменную
#     x += 1
#     print(f"Количество вызовов функции равно {x}.")
#
#
# x = 0
# inc()
# inc()
# inc()
#
# # Вывод программы:
#
# # Количество вызовов функции равно 1.
# # Количество вызовов функции равно 2.
# # Количество вызовов функции равно 3.
# ```

# ```python
# # использовать global нужно с осторожностью
# # Обычно лучше передавать значения в функцию и возвращать результат
# def f(count):
#     count += 1
#     print(f"Количество вызовов функции равно {count}.")
#     return count
#
#
# count_f = 0
# count_f = f(count_f)
# count_f = f(count_f)
# count_f = f(count_f)
#
# # Вывод программы:
# # Количество вызовов функции равно 1.
# # Количество вызовов функции равно 2.
# # Количество вызовов функции равно 3.
# ```

# ```python
# # Правило Python о global
# # Ключевое слово global нужно только когда функция изменяет (перезаписывает) глобальную переменную. Если функция только читает глобальную переменную — global не требуется.
#
# # click() — увеличивает значение счётчика на 1;
# # get_count() — возвращает текущее значение счётчика.
#
#
# def click():
#     global count
#     count += 1
#
#
# def get_count():
#     return count
#
#
# count = 0
# ```

# в переменную нельзя сохранить print
# ### **Чем отличаются `return` и `print` в функции?** 🐍
#
# #### **1. `print()` — просто печатает текст в консоль**
# - Это **вывод на экран**, но функция **не возвращает** это значение.
# - Удобно для отладки или показа информации пользователю.
# - **Пример:**
#   ```python
#   def greet(name):
#       print(f"Привет, {name}!")  # Печатает в консоль
#
#
#   greet("Анна")  # Выведет: "Привет, Анна!"
#   ```
#   **Что происходит?**
#   - Функция `greet()` печатает текст, но **не возвращает** его.
#   - Если попробовать сохранить результат в переменную, получим `None`:
#     ```python
#     result = greet("Анна")  # result = None (потому что нет return)
#     ```
#
# ---
#
# #### **2. `return` — возвращает значение из функции**
# - Функция **не печатает** результат, а **отдаёт** его для дальнейшего использования.
# - Можно сохранить в переменную, передать в другую функцию или вывести через `print()`.
# - **Пример:**
#   ```python
#   def add(a, b):
#       return a + b  # Возвращает сумму
#
#
#   result = add(3, 5)  # result = 8
#   print(result)  # Выведет: 8
#   ```
#   **Что происходит?**
#   - Функция `add()` **не печатает** результат, а **возвращает** его.
#   - Мы можем сохранить его в `result` и использовать дальше.
#
# ---
#
# ### **Когда использовать `print`, а когда `return`?**
#
# | **`print()`** | **`return`** |
# |--------------|-------------|
# | Когда нужно **показать** результат пользователю. | Когда нужно **передать** результат для дальнейших вычислений. |
# | Пример: вывод меню, сообщений об ошибках. | Пример: математические операции, обработка данных. |
# | **Не сохраняет** результат в переменную. | **Сохраняет** результат в переменную. |
# | ```python<br>def show(x):<br>    print(x)<br><br>show(5)  # Выведет 5<br>a = show(5)  # a = None<br>``` | ```python<br>def get(x):<br>    return x<br><br>get(5)  # Ничего не выведет<br>a = get(5)  # a = 5<br>``` |
#
# ---
#
# ### **Примеры для понимания**
#
# #### **С `print()` (только вывод)**
# ```python
# def say_hello(name):
#     print(f"Привет, {name}!")
#
#
# say_hello("Макс")  # Выведет: "Привет, Макс!"
# ```
# - **Нельзя** сохранить результат:
#   ```python
#   message = say_hello("Макс")  # message = None (бесполезно)
#   ```
#
# #### **С `return` (возврат значения)**
# ```python
# def create_hello(name):
#     return f"Привет, {name}!"
#
#
# message = create_hello("Макс")  # message = "Привет, Макс!"
# print(message)  # Теперь можно напечатать
# ```
# - **Можно** использовать результат дальше:
#   ```python
#   upper_message = message.upper()  # "ПРИВЕТ, МАКС!"
#   ```
#
# ---
#
# ### **Главное правило**
# - **`print`** — если нужно **просто показать** информацию.
# - **`return`** — если нужно **работать с результатом** функции дальше.

# ### присваивание переменной и id
# **при присваивании переменной нового значения сменится ли ее id?**
# В Python **`id` объекта** — это его уникальный идентификатор в памяти. При присваивании нового значения переменной её `id` **может измениться**, но это зависит от типа данных и самого значения.
#
# ### 1. **Неизменяемые (immutable) типы** (числа, строки, кортежи)
# При присваивании нового значения **создаётся новый объект**, и `id` меняется.
#
# #### Пример с целым числом (`int`):
# ```python
# x = 10
# print(id(x))  # Например, 140735849467792
#
# x = 20  # Присваиваем новое значение
# print(id(x))  # Новый id, например, 140735849468112
# ```
# **Вывод:** `id` изменился, потому что `10` и `20` — разные объекты.
#
# #### Пример со строкой (`str`):
# ```python
# s = "hello"
# print(id(s))  # Например, 2101674847408
#
# s = "world"  # Новое значение
# print(id(s))  # Другой id
# ```
# **Вывод:** `id` изменился, так как строки неизменяемы.
#
# ---
#
# ### 2. **Изменяемые (mutable) типы** (списки, словари, множества)
# Если изменять объект **без пересоздания** (например, через `append()`), `id` останется прежним. Но если присвоить **новый объект**, `id` изменится.
#
# #### Пример со списком (`list`):
# ```python
# lst = [1, 2, 3]
# print(id(lst))  # Например, 2101674847360
#
# lst.append(4)  # Изменяем объект, не создавая новый
# print(id(lst))  # Остаётся тем же!
#
# lst = [5, 6, 7]  # Полностью новый объект
# print(id(lst))  # Новый id
# ```
# **Вывод:**
# - `id` не меняется при изменении списка (`append`, `remove` и т. д.).
# - `id` меняется только при **полном переприсваивании**.
#
# ---
#
# ### 3. **Особые случаи (кэширование маленьких чисел и строк)**
# Python оптимизирует память, кэшируя маленькие целые числа (обычно от `-5` до `256`) и короткие строки.
#
# #### Пример с кэшированием чисел:
# ```python
# a = 100
# b = 100
# print(id(a) == id(b))  # True (один и тот же объект)
#
# a = 1000
# b = 1000
# print(id(a) == id(b))  # False (разные объекты)
# ```
#
# #### Пример с кэшированием строк:
# ```python
# s1 = "hello"
# s2 = "hello"
# print(id(s1) == id(s2))  # True (кэширование)
#
# s1 = "a very long string that won't be cached"
# s2 = "a very long string that won't be cached"
# print(id(s1) == id(s2))  # False (разные объекты)
# ```

# +
# 1


def print_hello(name: str) -> None:
    """Return Greeting statement."""
    print(f"Hello, {name}!")


# +
# 2


def gcd(number1: int, number2: int) -> int:
    """Calculate GCD."""
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


# +
# 3


def number_length(number_input: int) -> int:
    """Return input length."""
    return len(str(abs(number_input)))


# -

# #### 4
# ```python
# def take_small(money):
#     spisok = [i1 for i1 in money if i1 < 100]
#     return spisok
# ```

# #### 5
#
# ```python
# count = 0
#
#
# def click():
#     global count
#     count += 1
#
#
# def get_count():
#     return count
# ```

# #### 6
# ```python
# def move(player, num):
#     global number
#     if player == "Петя":
#         number += num
#     else:
#         number -= num
#     return number
#
#
# def game_over():
#     if number > 0:
#         return "Петя"
#     elif number < 0:
#         return "Ваня"
#     else:
#         return "Ничья"
#
#
# number = 0
# ```

# #### 7
# ```python
# from itertools import chain
#
#
# def max2D(matrix):
#     return max(list(chain.from_iterable(matrix)))
# ```

# #### 8
# ```python
# def fragments(numbers):
#     union_spisok = []
#     start_index = 0
#     for index, num in enumerate(
#         numbers[1:], 1
#     ):  # важно дописать 2ой параметр "1", тк начинает с 0, а надо с 1
#         if num <= numbers[index - 1]:
#             end_index = index
#             nested_spisok = numbers[start_index:end_index]
#             print(nested_spisok)
#             union_spisok.append(nested_spisok)
#             start_index = index
#     # довкладываем последний вложенный список
#     nested_spisok = numbers[start_index:]
#     union_spisok.append(nested_spisok)
#     return union_spisok
# ```

# #### 9
#
#
# ```python
# def month(mn: int, lang: str) -> str | None:
#     """Return month in specified locale."""
#     months = {
#         "en": [
#             "January",
#             "February",
#             "March",
#             "April",
#             "May",
#             "June",
#             "July",
#             "August",
#             "September",
#             "October",
#             "November",
#             "December",
#         ],
#         "ru": [
#             "Январь",
#             "Февраль",
#             "Март",
#             "Апрель",
#             "Май",
#             "Июнь",
#             "Июль",
#             "Август",
#             "Сентябрь",
#             "Октябрь",
#             "Ноябрь",
#             "Декабрь",
#         ],
#     }
#     return months[lang][mn - 1] if 1 <= mn <= 12 and lang in months else None
# ```

# +
# 10


def split_numbers(numbers_string: str) -> tuple[int, ...]:
    """Return tuple of split numbers."""
    return tuple(int(nmb) for nmb in numbers_string.split())


# -

# #### 11
# ```python
# def find_mountains(heights):
#     mountains = tuple()
#     for index, h1 in enumerate(heights[1:-1], 1):
#         if heights[index - 1] < h1 and heights[index + 1] < h1:
#             mountains = mountains + (index + 1,)
#     return mountains
# ```

# #### 12
# ```python
# def find_mountains(data):
#     mountains = []
#     for index_r, row in enumerate(data[1:-1], 1):
#         for index_c, col in enumerate(row[1:-1], 1):  # тк края все равно не горы
#             if row[index_c - 1] < col and row[index_c + 1] < col:
#                 if (
#                     data[index_r - 1][index_c] < col
#                     and data[index_r + 1][index_c] < col
#                 ):
#                     if (
#                         data[index_r - 1][index_c - 1] < col
#                         and data[index_r - 1][index_c + 1] < col
#                     ):
#                         if (
#                             data[index_r + 1][index_c - 1] < col
#                             and data[index_r + 1][index_c + 1] < col
#                         ):
#                             mountains.append((index_r + 1, index_c + 1))
#     return tuple(mountains)
# ```

# +
# 13


outputs: list[str] = []


def modern_print(line: str) -> None:
    """Print only new lines."""
    if line not in outputs:
        outputs.append(line)
        print(line)


# +
# 14


def can_eat(knight: tuple[int, int], piece: tuple[int, int]) -> bool:
    """Determine if a knight can capture a given piece in a game of chess."""
    x1_c, y1_c = knight
    x2_c, y2_c = piece
    return (abs(x1_c - x2_c), abs(y1_c - y2_c)) in [(2, 1), (1, 2)]


# -

# #### 15
# ```python
# def get_dict(text):
#     text_dict = dict()
#     for t1 in text.split(";"):
#         text_dict[t1.split("=")[0]] = t1.split("=")[1]
#     return text_dict
# ```

# +
# 16

# fmt: off
def is_palindrome(
    value: int | str | list[int] | tuple[int, ...] | float
) -> bool:
    """Check if input value is a palindrome."""
    if isinstance(value, (int, str, list, tuple)):
        value_str = str(value) if isinstance(value, int) else value
        return value_str == value_str[::-1]
    return False
# fmt: on

# +
# 17


def is_prime(nmb: int) -> bool:
    """Check if input value is prime."""
    if nmb < 2:
        return False
    for i in range(2, int(nmb**0.5) + 1):
        if nmb % i == 0:
            return False
    return True


# +
# 18


def merge(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple[int, ...]:
    """Merge and return two tuples."""
    result = []
    i_val, j_val = 0, 0
    for _ in range(len(tuple1) + len(tuple2)):
        if i_val < len(tuple1) and (
            j_val >= len(tuple2) or tuple1[i_val] < tuple2[j_val]
        ):
            result.append(tuple1[i_val])
            i_val += 1
        else:
            result.append(tuple2[j_val])
            j_val += 1
    return tuple(result)


# -

# #### 19
# ```python
# def swap(a, b):
#     a[:], b[:] = b[:], a[:]
#     return a, b
# ```

# #### 20
# ```python
# def int_to_roman(num):
#     val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#     roman_num = ""
#     i = 0
#     while num > 0:
#         for _ in range(num // val[i]):
#             roman_num += syb[i]
#             num -= val[i]
#         i += 1
#     return roman_num
#
#
# def roman(a, b):
#     sum_ab = a + b
#     roman_a = int_to_roman(a)
#     roman_b = int_to_roman(b)
#     roman_sum = int_to_roman(sum_ab)
#     return f"{roman_a} + {roman_b} = {roman_sum}"
# ```
