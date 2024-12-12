"""Глава 9."""

# # Ввод данных
#
# Чтобы добиться гибкости выполнения, мы мо­ жем получать информацию от пользователя. В Python есть встроенная функция input(), которая делает именно это.
#
# Ввод может быть не только строкой, например int(input()) позволяет пользователю вводить данные типа int
#
# # Форматированный вывод данных
#
# В Python есть несколько способов вывести результат работы программы. Данные можно вывести на экран в удобочитаемой форме или записать в файл.
#
# Форматировать вывод можно несколькими способами
#
# **Форматированные строки**
#
# Форматированные строки (так называемые f-строки) позволяют включать значения выражений Python внутрь строки. Для этого перед самой строкой надо добавить префикс f или F, а выражение заключить в фигурные скобки {выражение}

# ![image.png](attachment:image.png)

# **Строковый метод format**

# ![image.png](attachment:image.png)

# Строковый метод rjust о выравнивает строку по правому краю в поле заданной ширины, заполняя строку пробелами слева. Похожим образом работают методы ljust() и center(). Эти методы ничего не выводят на экран, а просто возвращают новую строку.
# Существует еще один метод zfill() (fill with zero), который дополняет строку нулями. В этом методе можно использовать плюсы и минусы.
#
# **Функции str() и repr()**
# Функции str() и repr() используются для получения строкового представления
# объекта.
#
# При использовании функции repr() строка выво­дится в кавычках, а str() возвращает строку без кавычек.
#
# Другие различия между этими функциями:
# ♦ Функция str() используется для создания вывода для конечного пользователя, а repr() в основном используется для целей отладки и разработки. Функция repr() дает однозначность, а str() - удобочитаемость. Например, если мы подозрева­ем, что у числа с плавающей точкой есть небольшая ошибка округления, repr() покажет нам ее а str() - нет.
# ♦ Функция repr() возвращает «формальное» строковое представление объекта (представление, которое содержит всю информацию об объекте), а str() используется для вывода неформального строкового представления объекта
#
# **Старое форматирование строки**
# Для форматирования строки также используется оператор %.
#
# Левый аргумент интерпретируется как строка формата sprintf(), применяемая к правому аргументу, и оператор возвращает строку, полученную в результате операции форматирования.

# ![image.png](attachment:image.png)

# # Чтение и запись файлов
#
# Метод open() возвращает файловый объект и чаще всего используется с двумя аргументами:
# f = open(имя_файла, режим)
#
# Режим может состоять из:
# • 'г' — файл открывается только для чтения;
# • 'w' — файл открывается только для записи (если файл с таким же именем уже существует, он будет перезаписан);
# • 'а' — файл открывается для добавления; любые данные, записываемые в файл, добавляются в его конец;
# • 'г+' — файл открывается как для чтения, так и для записи.
#
# Аргумент режима не является обязательным. Если он не указан, по умолчанию используется режим 'г'.
# Обычно файлы открываются в текстовом режиме, что означает, что вы читаете из файла и записываете в файл строки в определенной кодировке.
# При работе с файловыми объектами рекомендуется использовать ключевое слово with. Преимущество его использования заключается в том, что файл правильно закрывается после завершения работы, даже если в какой-то момент возникнет исключение.

# ![image.png](attachment:image.png)

# Если вы не используете ключевое слово with, то в конце нужно вызвать метод f.close(), чтобы закрыть файл и высвободить все используемые им системные ресурсы.
#
# # Методы файловых объектов
#
# Чтобы прочитать содержимое файла, вызовите метод f.read (size), который считывает size символов (в текстовом режиме) или size байт (в бинарном режиме).
#
# Здесь size — необязательный числовой аргумент. Если размер опущен или указано отрицательное значение, будет прочитано и возвращено все содержимое файла, но если размер файла вдвое превышает объем памяти вашей машины — у вас будут проблемы.
#
# Если достигнут конец файла, f.read() вернет пустую строку ('').
#
# Для последовательного чтения строк из файла вы можете использовать цикл. Это эффективно с точки зрения памяти, быстро, и код будет простым
#
# Если вы хотите извлечь все строки из файла в список вы можете использовать функцию
# list(f) или метод f.readlines()

# # Практическая часть

# +
# Создаем файл и записываем в него текст
with open("small_story.txt", "w", encoding="utf-8") as file_story:
    # строковая переменная с произвольным текстом
    story: str = (
        "There was a curious student. "
        "He wanted to learn Python. "
        "His age was... Well, how does "
        "it matter. One can be a student "
        "at any age. Let's say, he was "
        "a good student and within a "
        "short time, learnt all about "
        "programming and python. He combined "
        "that with his business acumen, and "
        "became a good data scientist."
    )

    file_story.write(story)

# Теперь открываем файл для чтения
with open("small_story.txt", encoding="utf-8") as file_story:
    content = file_story.read()  # Читаем содержимое файла
    print(content)  # Выводим содержимое на экран
# -

# 1 . Напишите код, который принимает число от пользователя, а возвращает квадрат введенного числа.

num: int = int(input("Enter a number: "))
num**2

# 2. Попросите у пользователя ввести его возраст в качестве входных данных. Вы­чтите его возраст из текущего года, чтобы узнать год рождения пользователя. Результат выведите в формате «Я родился в ... году».

age: int = int(input("Enter your age: "))
print("Я родился в", 2024 - age, "году")


# 3. Напишите функцию, которая принимает три аргумента: входной файл, выход­ной файл и функцию преобразования. Первый аргумент - это файл, открытый для чтения, второй аргумент - это файл, открытый для записи, а третий аргу­мент - это функция преобразования, которая принимает строку на вход, вы­полняет какое-то преобразование по вашему выбору и возвращает измененную строку. Основная функция должна читать строку из входного файла, выполнять над ней функцию преобразования, а затем записывать измененную строку в вы­ходной файл. Преобразование может быть, например, таким: каждое слово
# в строке должно начинаться с заглавной буквы.


def case_change(inputstr_: str, output: str, method: str = "up") -> str:
    """_summary_.

    Args:
        input (str): _description_
        output (str): _description_
        method (str, optional): _description_. Defaults to "up".

    Returns:
        str: _description_
    """
    with open(inputstr_, encoding="utf-8") as file1:
        string1: str = file1.read()
    with open(output, "w", encoding="utf-8") as file2:
        if method == "up":
            file2.write(string1.upper())
        else:
            file2.write(string1.lower())

    return "the text is annotated in " + output


case_change("small_story.txt", "big_story_txt")

with open("big_story_txt", encoding="utf-8") as total:
    print(total.read())


# 4. Напишите функцию для создания следующего файла, содержащего следующие данные
#
# The 344-sq. Jan. the periphery of Navi Мumbаi starts on the East with Kalundre village, on the West is the hill range that starts from Digha and runs up to Taloja; in the North is Digha village while Chanje village lies in the South, Dronagiri is on the South-East. The area comprised of 95 villages of Thane and Raigad Districts.
#
# а) прочтите содержимое файла
#
# б) Выведите содержимое
# файла с номерами строк.
#
# в) Выведите последнюю строку файла.
#
# г) Выведите первую строку, начиная с 1О-го символа.
#
# д) Попросите пользователя указать номер строки из файла, которую нужно про­читать.


# +
def mumbai_data() -> None:
    """_summary_."""
    with open("mumbai.txt", "w", encoding="utf-8") as file3:
        file3.write(
            """The 344-sq. Jan. the
periphery of Navi Mumbai
starts on the East with
Kalundre village, on the
West is the hill range
that starts from Digha
and runs up to Taloja;
in the North is Digha
village while Chanje
village lies in the South,
Dronagiri is on the South-East.
The area comprised of 95
villages of Thane and
Raigad Districts."""
        )


mumbai_data()
# -

# а) Читаем файл
with open("mumbai.txt", encoding="utf-8") as file5:
    print(file5.read())

# б) Выводим с номерами строк
with open("mumbai.txt", encoding="utf-8") as file6:
    line_num: int = 1
    for line in file6:
        print(line_num, line, end="")
        line_num += 1

# в) Выводим последнюю строку
with open("mumbai.txt", encoding="utf-8") as file7:
    lines: list[str] = file7.readlines()
    print(lines[-1])

# +
# г) Выводим первую строку с 10 символа, при
# этом можно не открывать файл еще раз так как
# строки у нас лежат в другой переменной.

lines[0][10::]

# +
# д) Пользователь указывает номер нужной строки

num_line: int = int(input("Введите номер строчки"))
lines[num_line]


# -

# 5. Напишите программу, которая принимает от пользователя имя файла и отобра­жает все строки из файла, которые содержат символ комментария Python '#'.


def htg_in_file(file_path: str) -> list[str]:
    """_summary_.

    Args:
        file_path (str): _description_

    Returns:
        list[str]: _description_
    """
    with open(file_path, encoding="utf-8") as file00:
        final_list: list[str] = []
        for string in file00.readlines():
            if "#" in string:
                final_list.append(string)
    return final_list


# # Проверка

with open("file#.txt", "w", encoding="utf-8") as file8:
    file8.write(
        """The 344-sq. Jan. the
periphery of Navi Mumbai
starts on the East # with
Kalundre village, on the
West is the hill # range
that starts from Digha
and runs up to Taloja;
in the North is Digha
village while # Chanje
village lies in the South,
Dronagiri is on the South-East.
The area comprised # of 95
villages of Thane and
Raigad Districts."""
    )

htg_in_file("file#.txt")


# 6. Читать файл с начала - это просто, но что если вам нужно прочитать файл в обратном направлении, например для чтения файлов с логами. Напишите про­грамму для чтения и отображения содержимого файла от конца до начала.


def reverse_file(path: str) -> str:
    """_summary_.

    Args:
        path (str): _description_

    Returns:
        str: _description_
    """
    with open(path, encoding="utf-8") as file0:
        reved = file0.read()[::-1]
    return reved


reverse_file("mumbai.txt")
