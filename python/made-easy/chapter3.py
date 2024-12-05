"""Chapter."""

# Python Basics

# 3.2. Let's start with "Hello World!"

print("Hello World ! ")

# 3.3.1. Numbers

# Синтаксис выражений прост: арифме­
# тические операторы +, -, * и / работают так же, как в любой компьютерной про­
# грамме, которую вы могли использовать, например, в цифровом калькуляторе или
# электронной таблице Excel; круглые скобки (), как обычно, могут использоваться
# для группировки

# #### 2 + 2

# #### 50 - 5 * 6

# ####(50 - 5 * 6) / 4  # круглые скобки используется для группировки

# #### 8 / 5  # результат деления всегда с плавающей точкой

# ### Целые числа (например, 2, 4, 20) имеют тип int
# ### тип float - (напри­мер, 5.0, 1 .6)

# #### Оператор деления / всегда возвращает float
# #### 17 / 3  # обычное деление с плавающей точкой

# #### 17 // 3  # целочисленное деление

# #### 17 % 3  # остаток от деления  2 -->
#
# #### Для примера:
# #### 17 // 3 = 5# (Целочисленное число)
# #### 3 * 5 = 15
# #### 17 - 15 = 2 # (остаток от деление)

# Для вычисления степени можно использовать оператор **

# ### 5**2  # 5 в квадрате

# ### 2**7  # 5 в степени 7

# Знак равенства = используется для присвоения значения переменной. После при­
# своения результат не отображается:

# +
width = 20
height = 5 * 9

height
# обратите внимание, что этот код ничего не возвращает
# -

# Lines

# #### " Python string "

# #### 'doesn"t'  # используйте \ для экранирования кавычки
#
# #### 'doesn"t'

# #### "doesn't"  # ... или используйте двойные кавычки

# said = "'Isn't, 11 they said.'"
# said

# "'Isn't, 11 they said.'"

# Eсли вы не хотите, чтобы управляющие символы (такие как \n, \t) интерпретирова­
# лись как специальные, вы можете использовать необработанные строки, добавив
# букву r перед первой кавычкой:

# +
print("C:\\some\narne")  # эдесь \n - переход на новую строку!

# C:\some
# arne

# +
print("C:\\some\tarne")

# C:\some	arne

# +
print(r"C:\some\name")  # r перед открывающей кавычкой

# C:\some\name
# -

# Concatenation and repetition

# Строки можно объединять (склеивать) с помощью оператора + и повторять с по­
# мощью оператора *. Запомнить это просто. Оператор + складывает, а оператор *
# умножает

# #### "а" + "Ь"  # 'аЬ'

# #### "t" * 5

# #### "no" * 3 + "dip"
#
# #### ' nononodip '

# ### "nil" "abh"  # 'nilabh'

# +
text = " Put several strings within parentheses"
text_one = "to have them joined together."

text_full = text + text_one

text_full
# -

# 3.2. Indexing
#
# Строки можно индексировать (обращаться к элементам строки по индексу), при
# этом первый символ имеет индекс О. Отдельного типа для данных символов не
# существует, т. к. символ - это просто строка длиной в один символ

# Например, для слова ' Python ' индексы будут такими:
# р у t h о n
# о 1 2 3 4 5
# -6 -5 -4 -3 -2 -1

word = "Python"
word[0]  # символ в позиции О

word[5]  # символ в позиции 5

# #### Для отрицательных индексов отсчет ведется справа:

word[-4]

# Обратите внимание: поскольку -0 равняется 0, то отрицательные индексы начина­
# ются с -1.

# #### 3.3.2.3 Sections
#
# Помимо индексирования строк также поддерживаются срезы. Если индексирование
# используется для извлечения отдельных символов, то срез возвращает подстроку.

# +
word[0:2]  # с позиции О (включительно) до 2 (не включая его)

# 'Pyth'

# +
word[2:5]  # с позиции 2 (включительно) до 5 (не включая его)

# 'tho'
# -

# Обратите внимание, что начальный индекс всегда включается, а конечный всегда
# исключается. Это гарантирует, что s[ : i]_ + s [i: J всегда равно s.

# +
word[:2] + word[2:]

# 'Py          thon
# -

# Строки Python нельзя изменить - они неизменяемы. Следовательно, присвоить
# новое значение символу по определенному индексу нельзя. Если вы попытаетесь
# это сделать, получите ошибку:

# +
# word[2] = "l"  # TypeError: 'str' object does not support item assignment
# -

# встроенная функция len () возвращает длину строки
len(word)

# 3.4. Python Code Syntax
# 3.4.1. Expressions

# Строки, написанные в исходном коде для выполнения, называются выражениями
# (рис. 3 .6), которые могут состоять из операторов разных типов, таких как оператор
# присваивания, условный оператор, оператор цикла и т. д. Все они нужны для того,
# чтобы пользователь мог получить нужный результат. Например, n = 20 - это вы­
# ражение с оператором присваивания.

# Выражения могут быть однострочными или многострочными. Многострочные вы­
# ражения можно переносить на другие строки с помощью круглых скобок ()
# фигурных скобок { } , квадратных скобок [], обратной косой черты (\). Если програм­мисту нужно выполнить длинные вычисления, а выражение не помещается в одну строку, эти символы помогут выйти из ситуации

# +
# перенос выражения на новую строку с использованием \
expressions_firs = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

expressions_firs

# +
# перенос выражения на новую строку с использованием ()
expressions_second = 1 * 2 * 3 + 7 + 8 + 9

expressions_second

# +
# перенос выражения на новую строку с использованием []
footballer = ["МESSI", "NEYМAR", "SUAREZ"]

footballer

# +
# перенос выражения на новую строку с использованием {}
third_expression = {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9}

third_expression
# -

# Выражения - это строительные блоки любой программы

# 3.4.1.1. End of expressions - Окончание выражений

# как написать выражение в нескольких строках.

# +
flag = 2
ropes = 3
pole = 4

flag, ropes, pole  # (2, 3, 4)
# -

# x_one = 2 + 3
#
# переминая,  присваивание, операнд, + оператор

# 3.4.2. Variables and value assignment
#
# #### Переменные и присваивание значений
#

# Одна из самых мощных функциональностей любого языка программирования -
# это возможность работать с переменными. Переменная - это некоторое имя, свя­занное со значением.
#
# Обратите внимание, что переменная лишь ссылается на зна­чение, которое ей присвоено, но не то дественна ему.
# Когда переменной присваи­вается другое значение, старое присвоение сразу становится недействительным.

# +
# переменной а присваиваем значение 45
a_variabl = 45

a_variabl

# +
a_variabl = 3 + 2

a_variabl
# -

# Variable names and keywords

# Для переменных следует выбирать имена со смыслом, которые что-то говорят
# о хранимых данных.
#
# Например, при работе с данными о продажах магазина в вы­
# ходные подойдет имя переменной Sales _ weekend.
#
# Это не строгое правило, но его
# соблюдение очень важно для обеспечения читабельности кода.
#
# И поскольку пере­
# менная может использоваться в коде несколько раз, такое именование поможет вам
# как программисту ориентироваться в своем же коде.
#
# Имена переменных могут быть любой длины и содержать как буквы, так и числа.
# Писать имена можно в верхнем или нижнем регистре, но одно и то же имя с раз­
# ными регистрами - это будут разные переменные, т. к. Python чувствителен к ре­
# гистру.
#
# Существует еще несколько правил именования переменных.
#
# ♦ Имя должно начинаться с буквы (не с цифры).
#
# ♦ В имени может присутствовать символ подчеркивания (_). Он используется для
# соединения слов в длинном имени переменной, т. к. пробелы использовать
# нельзя.

# ♦ Нельзя использовать в качестве имен переменных ключевые слова Python:
# and
# def
# ехес
# if
# not
# return
# assert
# del
# finally
# import
# or
# try
# break
# elif
# for
# in
# pass
# while
# class
# else
# from
# is
# print
# yield
# continue
# except
# global
# lamЬda
# raise

# +
# 2nd_wife # нельзя

man_vs_wild = "oleg"

man_vs_wild

# "national geographic" # нельзя

data_science = "good"

data_science

sudhir22 = "434"

sudhir22

pythonl23 = "hello world"

pythonl23

# class # нельзя

# global # нельзя

tomorrow = "tomorrow "

tomorrow

Sundar_ban = "3rf"

Sundar_ban
# -

# Executing expressions -  Выполнение выражений

# Выражение - это совокупность значений, переменных и операторов. Когда вы
# вводите в командной строке выражение, интерпретатор вычисляет его и выводит
# результат.

# The first steps in programming - Первые шаги в программировании1

# В первой строке используется множественное присваивание: переменные а и b  одновременно получают значения о и 1. В последней строке кода это используется
#
# 2. Цикл while выполняется до тех пор, пока условие остается истинным (в первом
# варианте это было а < 10, которое мы позже изменили на а < 15).
#
# < (меньше), > (больше), == (равно),
# <= (меньше или равно), >= (больше или равно) и ! = (не равно)
#
# 3. Тело цикла записано с отступом. Отступы - это способ группировки выраже­ний в Python
#
# 4. Функция print () выводит значение переданного аргумента на экран эта функция по-другому обрабатывает несколько аргументов, числа с пла­вающей запятой и строки. Строки выводятся без кавычек, а между аргументами вставляется пробел, что позволяет красиво форматировать результаты
#
#

# +
# ряд Фибоначчи
# сумма двух элементов -- это следующий элемент ряда
# fibonacci_series

elem_fer = 0
elem_sec = 1

while elem_fer < 10:
    print(elem_fer)
    elem_fer, elem_sec = elem_sec, elem_fer + elem_sec
# -

# Давайте поэкспериментируем

# +
# тот же ряд фибоначчи

first_number, second_number = 0, 1
while first_number < 15:
    print(first_number, end=",")
    first_number, second_number = second_number, first_number + second_number

# этот код работает так же, как и первый вариант
# -

i_one = 256 * 256
print("The value of i_one is", i_one)

# 3.5.1 . Подробнее о функции print()

# #### Фактический синтаксис функции
# print () выглядит так:
#
# print(*object, sep=" ", end="\n", file=sys.stdout, flush=False)
#

# Аргументы (иногда обозначаемые словом args);
#
# Именованные аргументы (иногда обозначаемые словом kwargs).
#
# Аргументы - это все, что мы передаем в функцию.
#

# *args в Python используется для передачи переменного количества неименованных аргументов в функцию. Оно позволяет функции принимать любое количество аргументов, которые собираются в кортеж.
#
# Вот как это работает:
#
#     *args собирает все переданные аргументы в кортеж.
#     Имя args можно изменить, но важно сохранить звёздочку *, которая обозначает, что будет передано несколько аргументов.
#
#

# +
# mymodule.py


def summa(*args: int) -> int:
    """Возвращает сумму всех переданных аргументов.

    Аргументы:.


    Возвращает:.
    int - сумма всех аргументов.
    """
    return sum(args)


# *args: int - произвольное количество целых чисел.
# Можно передать любое количество аргументов
print(summa(1, 2, 3))  # Вывод: 6
print(summa(5, 10, 15, 20))  # Вывод: 50
# -

# *objects - любое количество любых объектов. Перед выводом все объекты со­бираются в строку;
#
# sep=' ' (необязательный) - задает разделитель объектов, если их несколько.
# Значение по умолчанию - символ пробела, указанный как ' ';
#
# end= ' \n' (необязательный) - определяет, что вывести в конце строки. Значение
# по умолчанию - символ переноса строки ' \n' ;
#
# file=sys. stdout - объект с методом write ( string) . Если этот
# параметр не указан, будет использоваться sys. stdout по умолчанию, что означает вывод результатов на экран;
#
# flush=False (необязательный) - логическое значение, указывающее, будет ли вывод очищен (тrue) или буферизован (False). По умолчанию имеет значение
# False
#

# Объект sys.stdout
#
# sys.stdout — это стандартный поток вывода в Python, который по умолчанию выводит данные на экран (консоль). Он представляет собой объект, который имеет метод write(string). Когда вы используете print() в Python, это фактически вызывает метод write() на объекте sys.stdout, чтобы вывести строку.

# import sys
#
# Обычный вывод через print()
# print("This goes to the standard output")
#
# Прямое использование sys.stdout.write()
#
# sys.stdout.write("This also goes to the
#
# standard output\n")
#

# print("Этот текст выводится в консоль",
#
# file=sys.stdout)

# import sys
#
#
#
# #### Открываем файл и перенаправляем вывод в файл
# with open("output.txt", "w") as file:
#
#     print("Вывод в файл", file=file)
#
# #### После закрытия файла вывод снова будет в консоль
# #### print("Снова вывод в консоль", file=sys.stdout)
#

# import time
#
# print("This will be delayed", end='')
#
# No newline to flush the buffer
#
# time.sleep(5)  # Подождем 5 секунд перед
#
# завершением программы
#

# import sys
#
# Перенаправляем вывод в файл
# with open("output.txt", "w") as f:
#     sys.stdout = f
#     print("This will not appear on the screen")
#
# Восстанавливаем стандартный вывод
# sys.stdout = sys.__stdout__
#
# print("Now it will appear on the screen")
#

# Решение: Проверьте, был ли изменен sys stdout в коде, и если нужно вернуть вывод на
#
# экран, установите sys.stdout = sys.__stdout__.

# 3.5.2. Formatted output

# +
v_var = 5
b_one = 5
res = 5 * 6

# Используем f-строку
stroks = f"when {v_var} is multiplied by {b_one}, the result is {res}."
print(stroks)

# +
name = "oleg"
lastname = "olegNfedov"
place = "Mirny"

print(f"{name}, {lastname} lives in {place}")
# -

# 3.5.3.  The simplest geometry and print()

print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /_____|")

# 3.6 Error Search

# ♦ Синтаксическая ошибка - проблемы с языковыми конструкциями.
#
# ♦ Ошибка времени выполнения - проблемы с выполнением кода.
#
# ♦ Семантическая ошибка - неожиданный результат.

# # отсутствует закрывающая кавычка
# print ( "Hello World ! )
#
# File "<ipython-input-4 9-9d0e3bd45f27>" , line 3
#
# print ( "Hello World ! )
#
# SyntaxError : EOL while scanning string literal

# 3.6.2. Ошибки времени вы полнения
#
# Ошибки времени выполнения возникают во время работы программы. Поскольку
#
# Python является интерпретируемым языком, такие ошибки возникают лишь в тот
#
# момент, когда выполнение программы доходит до ошибочной строки.
#
# Частые причины таких ошибок следующие:
#
# ♦ неверно введенное имя переменной или функции;
#
# ♦ использование переменной до ее определения;
#
# ♦ имя должно было быть заключено в кавычки;
#
# ♦ деление на ноль.
#
# Ошибка времени выполнения возникает, когда Python понимает саму команду, но
#
# при ее выполнении сталкивается с проблемами. Поэтому эта ошибка и называется
#
# «времени выполнения», поскольку возникает только после запуска программы.
#
# In ( 5 1 ) : 5/0
#
# ZeroDivisionError Traceback (most recent call last)
#
# <ipython-input-51-0106664d39e8> in <module>
# ----> 1 5/0
# ZeroDivisionError : division Ьу zer

# 3.6.3. Семантические ош ибки
# Семантические или логические ошибки - это проблемы с самим построением
#
# вашей программы. Обычно такие проблемы не вызывают сообщений об ошибках,
#
# но поведение программы оказывается неверным. Ошибки такого типа сложнее всего
#
# отследить.
#
# Эти ошибки часто бывают вызваны случайным использованием неверных пере
#
# менных либо просто неправильными вычислениями.

# In [52) : # мы хотим вывести "Hello Nilabh"
#
# narne = "Nilabh"
#
# print ( "Hello narne " )
#
# Hello narne
