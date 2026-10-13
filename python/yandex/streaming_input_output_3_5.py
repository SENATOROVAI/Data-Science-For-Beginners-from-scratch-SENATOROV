"""Потоковый ввод/вывод. Работа с текстовыми файлами. JSON.

Вы научитесь считывать данные из файлов, а также записывать результаты работы программ
обратно в текстовые и JSON-файлы.
"""

# pylint: disable=too-many-lines
# pylint: disable=unused-import

# ## A+B+...
#
# - В этом блоке мы научимся работать с потоками ввода-вывода и с файлами, а ещё — познакомимся с форматом JSON. Все эти инструменты пригодятся, когда данных слишком много, чтобы вводить их вручную, или когда они приходят в программу из внешнего источника.
# - Начнём с простой, но полезной задачи.
# - Напишите программу, которая считывает все введённые строки и находит сумму всех чисел в потоке ввода.
# - Формат ввода
# - Вводятся строки чисел.
# - Формат вывода
# - Одно число — сумма всех чисел в потоке ввода.

# +
import json
import math
import os
import sys
from collections.abc import Iterator
from sys import stdin
from typing import Dict, List, TypedDict, Union

total_sum: int = 0
for line in sys.stdin:
    line_cleaned = line.strip()
    if line_cleaned:
        numbers: list[str] = line_cleaned.split()
        for num in numbers:
            total_sum += int(num)
print(total_sum)
# -

# ## Средний рост
#
# - Учитель физкультуры задался вопросом, на сколько в среднем его подопечные выросли за прошедший месяц. Поможем ему провести вычисления на Python!
# - Напишите программу, которая определяет, на сколько изменился средний рост учеников в классе.
# - Формат ввода
# - Вводится информация о детях в формате:
# - <Имя> <Рост месяц назад> <Рост сейчас>
# - Формат вывода
# - Одно число — ответ на вопрос задачи.
# - Ответ округлите до целых. Например, функцией round.

heights_before = []
heights_now = []
for line in stdin:
    line = line.strip()
    if line:
        parts = line.split()
        if len(parts) >= 3:
            try:
                height_before = float(parts[-2])
                height_now = float(parts[-1])
                heights_before.append(height_before)
                heights_now.append(height_now)
            except ValueError:
                continue
if heights_before and heights_now:
    avg_before = sum(heights_before) / len(heights_before)
    avg_now = sum(heights_now) / len(heights_now)
    difference = avg_now - avg_before
    print(round(difference))
else:
    print(0)

# ## Без комментариев 2.0
#
# - Как вы помните, когда вы комментируете свой код, перед его выполнением интерпретатор удаляет комментарии.
# - Напишите программу, которая выполняет эту функцию — удаляет комментарии из кода.
# - Формат ввода
# - Вводятся строки программы.
# - Формат вывода
# - Каждую строку нужно очистить от комментариев.
# - А если комментарий — вся строка, то выводить её не нужно.

for line in stdin:
    line_cl: str = line.rstrip("\n")
    if line_cl and not line_cl.startswith("#"):
        parts_: list[str] = line_cl.split("#", 1)
        code_part: str = parts_[0].rstrip()
        if code_part:
            print(code_part)

# ## Найдётся всё 2.0
#
# - Поиск информации — важная часть современной жизни. Создайте программу, которая реализует маленький компонент поисковой системы: она должна находить строки, содержащие заданный запрос.
# - Формат ввода
# - Вводятся заголовки страниц.
# - В последней строке записан поисковый запрос.
# - Формат вывода
# - Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
# - Порядок заголовков должен сохраниться.

# +
lines: list[str] = []
query: str = ""
for line in stdin:
    cleaned_line_2: str = line.strip()
    if cleaned_line_2:
        lines.append(cleaned_line_2)

if lines:
    query = lines.pop().lower()

for line in lines:
    if query in line.lower():
        print(line)
# -

# ## А роза упала на лапу Азора 6.0
#
# - Мы уже писали программы, которые определяли, палиндром ли перед нами. Теперь задача посложнее: найдите все слова-палиндромы среди введённых строк и выведите их без повторов, в алфавитном порядке.
# - Формат ввода
# - Вводятся слова.
# - Формат вывода
# - Список слов-палиндромов в алфавитном порядке без повторений.
# - Примечание
# - При проверке слов не обращайте внимание на регистр.

palindromes = set()
for line in stdin:
    line = line.strip()
    if line:
        words = line.split()
        for word in words:
            lower_word = word.lower()
            if lower_word == lower_word[::-1]:
                palindromes.add(word)
sorted_palindrom = sorted(palindromes)
for palindrome in sorted_palindrom:
    print(palindrome)

# ## Транслитерация 2.0
#
# - Переходим к работе с файлами. Для международных документов русский текст преобразуется с использованием латинского алфавита. Вам предстоит выполнить транслитерацию текста по стандарту ГОСТ.
# - Например: ГОСТ Р 52535.1-2006 задаёт правила транслитерации идентификационных карт.
# - В этой задаче вы впервые будете считывать текст из файла и записывать результат в другой файл.
# - А ещё — аккуратно работать с символами и строками, соблюдая правила преобразования регистра.
# - Ниже приведена таблица замен:
# - А — A
# - Б — B
# - В — V
# - Г — G
# - Д — D
# - Е — E
# - Ё — E
# - Ж — ZH
# - З — Z
# - И — I
# - Й — I
# - К — K
# - Л — L
# - М — M
# - Н — N
# - О — O
# - П — P
# - Р — R
# - С — S
# - Т — T
# - У — U
# - Ф — F
# - Х — KH
# - Ц — TC
# - Ч — CH
# - Ш — SH
# - Щ — SHCH
# - Ы — Y
# - Э — E
# - Ю — IU
# - Я — IA
# - Букву «ё» транслитерируйте как «e», «й» как «и», а «ъ» и «ь» (и их заглавные версии «Ъ» и «Ь») должны исчезнуть из текста. Строчные буквы заменяются на строчные, заглавные заменяются на заглавные.
# - Если заглавная буква превращается при транслитерации в несколько букв, то заглавной должна остаться только первая из них (например, «Ц» → «Tc»).
# - Все некириллические символы должны остаться на месте.
# - Формат ввода
# - В одной папке с вашей программой лежит файл cyrillic.txt. В нём, в числе прочих, содержится некоторое количество кириллических символов.
# - Формат вывода
# - В файл transliteration.txt записать результат транслитерации исходного файла.

# +
translit_dict: dict[str, str] = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "tc",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "y",
    "э": "e",
    "ю": "iu",
    "я": "ia",
}

with open("cyrillic.txt", encoding="utf-8") as file:
    text: str = file.read()

result: list[str] = []
char: str
for char in text:
    if char in translit_dict:
        replacement: str = translit_dict[char]
        if char.isupper() and len(replacement) > 1:
            replacement = replacement[0].upper() + replacement[1:].lower()
        result.append(replacement)
    elif char in ["Ъ", "Ь", "ъ", "ь"]:
        continue
    else:
        result.append(char)

with open("transliteration.txt", "w", encoding="utf-8") as output_file:
    output_file.write("".join(result))
# -

# ## Файловая статистика.
#
# - Иногда нужно быстро понять, что содержится в файле с числами: сколько их, какие, и каковы основные показатели.
# - Напишите программу, которая для заданного файла вычисляет следующие параметры:
# - количество всех чисел;
# - количество положительных чисел;
# - минимальное число;
# - максимальное число;
# - сумма всех чисел;
# - среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# - Формат ввода
# - Пользователь вводит имя файла.
# - Файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
# - Формат вывода
# - Выведите статистику в указанном порядке.

filename: str = input().strip()
try:
    with open(filename, encoding="utf-8") as file:
        content: str = file.read()
        numbers_collection: list[float] = []
        for word in content.split():
            try:
                number: float = float(word)
                numbers_collection.append(number)
            except ValueError:
                continue
    if numbers_collection:
        total_count: int = len(numbers_collection)
        positive_count: int = sum(1 for n in numbers_collection if n > 0)
        min_num: float = min(numbers_collection)
        max_num: float = max(numbers_collection)
        sum_total: float = sum(numbers_collection)
        average: float = round(sum_total / total_count, 2)
        print(total_count)
        print(positive_count)
        print(int(min_num) if min_num.is_integer() else min_num)
        print(int(max_num) if max_num.is_integer() else max_num)
        print(int(sum_total) if sum_total.is_integer() else sum_total)
        print(average)
    else:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
except FileNotFoundError:
    print("Файл не найден")
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
except PermissionError:
    print("Нет прав доступа к файлу")
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
except OSError as e:
    print(f"Ошибка ввода-вывода: {e}")
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
except UnicodeDecodeError:
    print("Ошибка кодировки файла")
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)


# ## Файловая разница.
#
# - Иногда нужно понять, чем два текста отличаются. Например, какие слова встретились только в одном источнике.
# - Напишите программу, которая сравнивает два файла и записывает в третий файл все слова, которые есть только в одном из них.
# - Формат ввода
# - Пользователь вводит три имени файлов.
# - Каждый из входных файлов содержит произвольное количество слов, разделённых пробелами и символами перевода строки.
# - Формат вывода
# - В третий файл выведите в алфавитном порядке без повторений список слов, которые есть только в одном из файлов.


# +
def process_unique_words() -> None:
    """process_unique_words."""
    file1_name: str = input().strip()
    file2_name: str = input().strip()
    output_name: str = input().strip()

    words1: set[str] = set()
    try:
        with open(file1_name, encoding="utf-8") as f:
            for line_s in f:
                words1.update(line_s.split())
    except FileNotFoundError:
        print(f"Файл {file1_name} не найден")
        return

    words2: set[str] = set()
    try:
        with open(file2_name, encoding="utf-8") as f:
            for line_z in f:
                words2.update(line_z.split())
    except FileNotFoundError:
        print(f"Файл {file2_name} не найден")
        return

    unique_words: set[str] = words1 ^ words2

    sorted_words: list[str] = sorted(unique_words)

    try:
        with open(output_name, "w", encoding="utf-8") as f:
            for word_s in sorted_words:
                f.write(word_s + "\n")
    except OSError:
        print(f"Ошибка записи в файл {output_name}")


if __name__ == "__main__":
    process_unique_words()
# -

# ## Файловая чистка.
#
# - Python — отличный инструмент для создания утилит, которые обрабатывают текстовые файлы.
# - Напишите скрипт, который «почистит» заданный файл от мусора:
# - повторяющихся пробелов;
# - повторяющихся символов перевода строки;
# - табуляций;
# - излишних пробелов в начале и конце строк.
# - Формат ввода
# - Пользователь вводит два имени файлов.
# - Входной файл содержит неформатированный текст произвольной длины.
# - Формат вывода
# - Во второй файл выведите очищенный текст.

# +
with open(input(), encoding="UTF-8") as file_in:
    text_lines: list[str] = file_in.readlines()

formatted: list[str] = [
    " ".join(line.replace("\t", "").split())
    for line in text_lines
    if len(line.split()) > 0
]
with open(input(), "w", encoding="UTF-8") as file_out:
    print("\n".join(formatted), file=file_out)


# -

# ## Хвост.
#
# - В Linux есть удобная команда tail, которая показывает последние строки файла — особенно полезно, если файл большой.
# - Напишите аналог этой утилиты: программа должна выводить последние N строк из заданного файла.
# - Формат ввода
# - вводит имя файла (F), а затем количество строк (N), которые он хочет увидеть.
# - Формат вывода
# - Выведите N последних строк файла F.


# +
def tail(filename_tail: str, n_tail: int) -> None:
    """Выводит последние n_tail строк из файла.

    Args:
        filename_tail: Имя файла для чтения
        n_tail: Количество последних строк для вывода

    Returns:
        None
    """
    try:
        with open(filename_tail, encoding="utf-8") as file_tail:
            lines_tail = file_tail.readlines()
            for line_tail in lines_tail[-n_tail:]:
                print(line_tail, end="")
    except FileNotFoundError:
        print(f"Файл {filename_tail} не найден")
    except PermissionError:
        print(f"Нет прав доступа к файлу {filename_tail}")
    except UnicodeDecodeError:
        print(f"Ошибка кодировки файла {filename_tail}")
    except OSError as e:
        print(f"Системная ошибка при работе с файлом: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")


def run_program() -> None:
    """Основная функция программы.

    Запрашивает у пользователя имя файла и количество строк,
    затем вызывает функцию tail для вывода последних строк.

    Returns:
        None
    """
    filename_run = input().strip()
    try:
        n_run = int(input().strip())
        if n_run < 0:
            print("Количество строк должно быть неотрицательным числом")
            return
        tail(filename_run, n_run)
    except ValueError:
        print("Введите корректное число строк")


if __name__ == "__main__":
    run_program()


# -

# ## Файловая статистика 2.0.
#
# - Иногда нужно не просто посчитать статистику по файлу, но и сохранить её в универсальном формате для других программ.
# - Напишите программу, которая вычисляет ключевые числовые параметры и сохраняет их в файл в формате JSON:
# - количество всех чисел;
# - количество положительных чисел;
# - минимальное число;
# - максимальное число;
# - сумма всех чисел;
# - среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# - Формат ввода
# - Пользователь вводит два имени файла.
# - Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
# - Формат вывода
# - Выведите статистику во второй файл в формате JSON.
# - Ключи значений задайте соответственно:
# - count — количество всех чисел;
# - positive_count — количество положительных чисел;
# - min — минимальное число;
# - max — максимальное число;
# - sum — сумма всех чисел;
# - average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.


# +
def process_numbers(input_file: str, output_file_proc: str) -> None:
    """Обрабатывает числа из входного файла и записывает статистику в выходной
    файл.

    Args:
        input_file: Путь к входному файлу с числами
        output_file_proc: Путь к выходному файлу для записи статистики
    """
    try:
        numbers_proc: list[float] = []
        with open(input_file, encoding="utf-8") as f:
            for linee_proc in f:
                line_numbers: list[str] = linee_proc.split()
                for num_str in line_numbers:
                    try:
                        nume_proc: float = float(num_str)
                        numbers_proc.append(nume_proc)
                    except ValueError:
                        continue

        statistics: dict[str, Union[int, float, None]] = calculate_statistics(
            numbers_proc
        )

        with open(output_file_proc, "w", encoding="utf-8") as f:
            json.dump(statistics, f, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")


def calculate_statistics(
    numbers_calc: list[float],
) -> dict[str, Union[int, float, None]]:
    """Вычисляет статистику по списку чисел.

    Args:
        numbers_calc: Список чисел для анализа
    Returns:
        Словарь со статистикой: count, positive_count, min, max, sum, average
    """
    if not numbers_calc:
        return {
            "count": 0,
            "positive_count": 0,
            "min": None,
            "max": None,
            "sum": 0,
            "average": 0.0,
        }

    count: int = len(numbers_calc)
    positive_count_calc: int = sum(1 for num in numbers_calc if num > 0)
    min_num_calc: int = int(min(numbers_calc))
    max_num_calc: int = int(max(numbers_calc))
    total_sum_calc: int = int(sum(numbers_calc))
    average_calc: float = round(total_sum / count, 2) if count > 0 else 0.0

    return {
        "count": count,
        "positive_count": positive_count_calc,
        "min": min_num_calc,
        "max": max_num_calc,
        "sum": total_sum_calc,
        "average": average_calc,
    }


def process_numbers_from_user_input() -> None:
    """Основная функция для обработки чисел на основе пользовательского ввода.

    Запрашивает имена входного и выходного файлов и запускает обработку.
    """
    input_filename: str = input().strip()
    output_filename: str = input().strip()
    process_numbers(input_filename, output_filename)


if __name__ == "__main__":
    process_numbers_from_user_input()
# -

# ## Разделяй и властвуй.
#
# - Числа можно классифицировать по-разному. Например, по количеству чётных и нечётных цифр.
# - Напишите программу, которая делит числа из файла на три группы и записывает каждую в отдельный файл.
# - числа с преобладающим количеством чётных цифр;
# - числа с преобладающим количеством нечётных цифр;
# - числа с одинаковым количеством чётных и нечётных цифр.
# - Формат ввода
# - Пользователь вводит четыре имени файла.
# - Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
# - Формат вывода
# - В три другие файла выведите числа, которые подходят под требуемое условие.
# - Сохраните положение чисел в строках.

# +
input_file_: str = input()
evens_file: str = input()
odds_file: str = input()
equals_file: str = input()

with open(input_file_, encoding="UTF-8") as file:
    strings: list[str] = [string for string in file.read().split("\n") if string]

even_digits: str = "02468"
odd_digits: str = "13579"

string: str
for string in strings:
    evens: list[str] = []
    odds: list[str] = []
    equals: list[str] = []

    number_: str
    for number_ in string.split():
        total_evens: int = 0
        total_odds: int = 0
        char_: str
        for char_ in number_:
            if char_ in even_digits:
                total_evens += 1
            elif char_ in odd_digits:
                total_odds += 1

        if total_evens > total_odds:
            evens.append(number_)
        elif total_evens < total_odds:
            odds.append(number_)
        else:
            equals.append(number_)

    with open(evens_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(evens) + "\n")
    with open(odds_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(odds) + "\n")
    with open(equals_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(equals) + "\n")
# -

# ## Обновление данных.
#
# - Часто приходится обновлять данные.
# - Создайте программу, которая обновляет JSON файл.
# - Формат ввода
# - Пользователь вводит имя файла.
# - Затем вводятся строки вида ключ == значение.
# - Формат вывода
# - заданный пользователем файл следует записать обновленный JSON.

# +
filename_: str = input().strip()
data: dict[str, str]
try:
    with open(filename_, encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

while True:
    try:
        line_2: str = input().strip()
        if not line_2:
            break
        if " == " in line_2:
            key: str
            value: str
            key, value = line_2.split(" == ", 1)
            data[key.strip()] = value.strip()
        else:
            continue
    except EOFError:
        break
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")

with open(filename_, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
# -

# ## Слияние данных.
#
# - Местная компания решила обновить и одновременно перестроить свою систему хранения пользовательских данных.
# - Напишите программу, которая принимает два JSON-файла: с текущими данными и обновлениями, а затем объединяет их в новую структуру.
# - Формат ввода
# - Пользователь вводит два имени файла.
# - В первом хранится JSON массив пользователей.
# - Во втором — массив новых данных.
# - Информация о каждом пользователе представляется JSON объектом, в котором обязательно присутствует поле name, описывающее имя пользователя. Остальные поля являются дополнительными.
# - Формат вывода
# - В первый файл запишите информацию о пользователях в виде JSON объекта, ключами которого выступают имена пользователей, а значениями — объекты с информацией о них.
# - Если какая-либо дополнительная информация о пользователе изменяется, то требуется сохранить лексикографически большее значение.

# +
users_file: str = input().strip()
updates_file: str = input().strip()

users_data: list[dict[str, str]]
try:
    with open(users_file, encoding="utf-8") as file:
        users_data = json.load(file)
except FileNotFoundError:
    users_data = []

updates_data: list[dict[str, str]]
try:
    with open(updates_file, encoding="utf-8") as file:
        updates_data = json.load(file)
except FileNotFoundError:
    updates_data = []

users_dict: dict[str, dict[str, str]] = {}
user: dict[str, str]
for user in users_data:
    if "name" in user:
        name: str = user["name"]
        user_info: dict[str, str] = {k: v for k, v in user.items() if k != "name"}
        users_dict[name] = user_info

update: dict[str, str]
for update in updates_data:
    if "name" in update:
        name_2: str = update["name"]
        update_info: dict[str, str] = {k: v for k, v in update.items() if k != "name"}

        if name_2 in users_dict:
            key_: str
            value_: str
            for key_, value_ in update_info.items():
                if key_ in users_dict[name_2]:
                    users_dict[name_2][key_] = max(users_dict[name_2][key_], value_)
                else:
                    users_dict[name_2][key_] = value_
        else:
            users_dict[name_2] = update_info

with open(users_file, "w", encoding="utf-8") as file:
    json.dump(users_dict, file, ensure_ascii=False, indent=4)


# -

# ## Поставь себя на моё место.
#
# - Сегодня вы — Ядекс.Контест.
# - Напишите программу, которая рассчитывает итоговый балл за выполнение задания на основе файла с тестами и входного потока с ответами.
# - Вашему решению доступен файл scoring.json, в котором содержится информация о системе проверки.
# - Основой системы является список групп тестов.
# - Каждая группа представляет собой объект с полями:
# - points — количество очков, которое можно получить за прохождение данной группы;
# - tests — список объектов с описанием конкретного теста.
# - Объект описывающий тест содержит поля:
# - input — строка входных данных теста;
# - pattern — строка ожидаемых в качестве ответа.
# - В стандартный поток ввода вашего решения передаются ответы, полученные от тестируемой программы.
# - Формат ввода
# - В стандартный поток ввода передаются строки — ответы тестируемой программы на каждый тест.
# - В файле scoring.json содержится информация о тестах задачи.
# - Формат вывода
# - Одно число — количество полученных тестируемой программой баллов.
# - Если группа тестов не была пройдена полностью, то за данную группу ставится пропорциональный балл.
# - Гарантируется, что баллы за группу кратны количеству тестов в ней.


# +
class TestCase(TypedDict):
    """Представляет один тестовый случай с шаблоном для сравнения."""

    pattern: str


class Group(TypedDict):
    """Представляет группу тестовых случаев с associated баллами."""

    points: int
    tests: list[TestCase]


with open("scoring.json", encoding="utf-8") as file:
    groups: list[Group] = json.load(file)

answers: list[str] = []
while True:
    try:
        line_o: str = input().strip()
        if line_o:
            answers.append(line_o)
    except EOFError:
        break

answer_iter: Iterator[str] = iter(answers)
total_score: float = 0

for group in groups:
    points_per_group: int = group["points"]
    tests: list[TestCase] = group["tests"]
    tests_count: int = len(tests)

    correct_count: int = 0

    for test in tests:
        try:
            user_answer: str = next(answer_iter).strip()
            expected_answer: str = test["pattern"].strip()

            if user_answer == expected_answer:
                correct_count += 1
        except StopIteration:
            break

    group_score: float = (points_per_group / tests_count) * correct_count
    total_score += group_score

print(int(total_score))


# -

# ## Найдётся всё 3.0.
#
# - А теперь давайте вновь напишем компонент поисковой системы — на этот раз с учётом формата и содержимого файлов. Сначала вводится поисковый запрос. Затем — список файлов, в которых нужно искать. Нужно найти, в каких файлах встречается запрос, без учёта регистра и с учётом любых пробелов и переводов строки как обычных пробелов.
# - Формат ввода
# - Сначала вводится поисковый запрос.
# - Затем вводятся имена файлов, среди которых следует произвести поиск.
# - Формат вывода
# - Выведите все имена файлов, в которых есть поисковая строка без учета регистра и повторяющихся пробельных символов.
# - Если ни в одном файле информация не была найдена, выведите 404. Not Found.
# - Примечание
# - Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b", "a b" и "a\nb" как одинаковые.


# +
def normalize(text_norm: str) -> str:
    """Приводит текст к нижнему регистру, заменяет пробелы."""
    return " ".join(text_norm.lower().split())


def search_files_by_content() -> None:
    """Основная функция поиска файлов по содержимому."""
    search_query: str = input().strip()
    normalized_query: str = normalize(search_query)

    filenames: list[str] = []
    while True:
        try:
            filename_norm: str = input().strip()
            if filename_norm:
                filenames.append(filename_norm)
        except EOFError:
            break

    found_files: list[str] = []
    for filename_norm in filenames:
        try:
            with open(filename_norm, encoding="utf-8") as file_s:
                content_s: str = file_s.read()
                normalized_content: str = normalize(content_s)
                if normalized_query in normalized_content:
                    found_files.append(filename_norm)
        except FileNotFoundError:
            continue
        except ValueError as e:
            print(f"Ошибка значения: {e}")
        except TypeError as e:
            print(f"Ошибка типа данных: {e}")

    if found_files:
        for filename_norm in found_files:
            print(filename_norm)
    else:
        print("404. Not Found")


if __name__ == "__main__":
    search_files_by_content()


# -

# ## Прятки.
#
# - Нам дали зашифрованный файл, и сказали, что нужно «выдернуть» младший байт из каждого символа — так восстанавливается спрятанное сообщение.
# - Справка:
# - Стеганография — способ передачи или хранения информации с учётом сохранения в тайне самого факта такой передачи (хранения).
# - В отличие от криптографии, которая скрывает содержимое тайного сообщения, стеганография скрывает сам факт его существования. Как правило сообщение будет выглядеть как что-либо иное, например, как изображение, статья, список покупок, письмо или судоку. Стеганографию обычно используют совместно с методами криптографии, таким образом, дополняя её.
# - Нам был дан файл со скрытым текстом. И было сообщено, что для выделения полезной информации, нужно из каждого кода символа в тексте «выдернуть» младший байт. Это и будет код символа полезной информации. Однако есть одно «но». Если код символа меньше 128 — это и есть полезная информация.
# - Разработайте программу, которая из текстового файла выделяет полезную информацию.
# - Формат ввода
# - В файле secret.txt хранится текст.
# - Формат вывода
# - Выведите спрятанное сообщение.


# +
def extract_hidden_message(filename_ext: str) -> str:
    """Извлекает скрытое сообщение из файла.

    Для каждого символа:
    - Если код символа < 128, это полезный символ
    - Иначе извлекаем младший байт (младшие 8 бит).
    """
    try:
        with open(filename_ext, encoding="utf-8") as file_ext:
            content_ext: str = file_ext.read()
    except FileNotFoundError:
        print(f"Файл {filename_ext} не найден")
        return ""
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return ""
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
        return ""

    hidden_message: list[str] = []
    char_ext: str
    for char_ext in content_ext:
        code: int = ord(char_ext)
        if code < 128:
            hidden_message.append(char_ext)
        else:
            low_byte: int = code & 0xFF
            hidden_message.append(chr(low_byte))
    return "".join(hidden_message)


if __name__ == "__main__":
    filename_txt: str = "secret.txt"
    message: str = extract_hidden_message(filename_txt)
    print(message)


# -

# ## Сколько вешать в байтах?.
#
# - Перед этим — лёгкая утилита: нужно определить размер файла и отформатировать его по ГОСТу. Это пригодится для работы с логами, архивами или системными файлами.
# - В нашей странице согласно ГОСТ 8.417-2002 объём информации измеряется в следующих единицах:
# - бит (б)
# - Байт (Б) = 8 бит
# - Килобайт (КБ) = 1024 Б
# - Мегабайт (МБ) = 1024 КБ
# - Гигабайт (ГБ) = 1024 МБ
# - Напишите программу, которая вычисляет объём заданного файла.
# - Формат ввода
# - Вводится одно имя файла.
# - Формат вывода
# - Выведите объём файла в соответствующих единицах измерения.
# - При получении дробного значения, произведите округление вверх.


# +
def format_file_size(size_bytes: int) -> str:
    """Форматирует размер файла согласно ГОСТ 8.417-2002.

    Округляет дробные значения вверх.
    """
    if size_bytes == 0:
        return "0Б"
    units = ["Б", "КБ", "МБ", "ГБ"]
    size: float = float(size_bytes)
    unit: str
    for unit in units:
        if size < 1024:
            if unit == "Б":
                return f"{math.ceil(size)}{unit}"
        size /= 1024
    return f"{math.ceil(size)}ТБ"


def display_file_size() -> None:
    """Запрашивает имя файла и выводит его размер."""
    filename_dis: str = input().strip()
    try:
        file_size: int = os.path.getsize(filename_dis)
        formatted_size: str = format_file_size(file_size)
        print(formatted_size)
    except FileNotFoundError:
        print(f"Файл '{filename_dis}' не найден")
    except OSError as e:
        print(f"Ошибка доступа к файлу: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")


if __name__ == "__main__":
    display_file_size()


# -

# ## Это будет наш секрет.
#
# - Давайте реализуем шифр Цезаря, который сдвигает латинские буквы по кругу. Работать будем с текстом в файле — это приближает задачу к реальным случаям шифрования данных. Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых простых и наиболее широко известных методов шифрования. Он назван в честь римского полководца Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами. Давайте реализуем эту систему шифрования. Однако для простоты мы будем сдвигать только латинские символы по кругу.
# - Формат ввода
# - Вводится размер сдвига для шифрования.
# - В файле public.txt содержится текст на английском языке.
# - Формат вывода
# - В файл private.txt запишите зашифрованный текст.


# +
def caesar_cipher(text_: str, shift: int) -> str:
    """Шифрует текст шифром Цезаря.

    Сдвигает только латинские буквы.
    """
    result_ = []
    for char_2 in text_:
        if "a" <= char_2 <= "z":
            shifted = chr((ord(char_2) - ord("a") + shift) % 26 + ord("a"))
            result_.append(shifted)
        elif "A" <= char_2 <= "Z":
            shifted = chr((ord(char_2) - ord("A") + shift) % 26 + ord("A"))
            result_.append(shifted)
        else:
            result_.append(char_2)
    return "".join(result_)


def encrypt_file() -> None:
    """Читает текст из public.txt, шифрует его и записывает в private.txt."""
    try:
        shift = int(input().strip())
        with open("public.txt", encoding="utf-8") as file_2:
            original_text = file_2.read()
        encrypted_text = caesar_cipher(original_text, shift)
        with open("private.txt", "w", encoding="utf-8") as file_2:
            file_2.write(encrypted_text)
    except FileNotFoundError:
        print("Файл public.txt не найден")
    except ValueError:
        print("Введите целое число для сдвига")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")


if __name__ == "__main__":
    encrypt_file()


# -

# ## Файловая сумма.
#
# - Теперь вы умеете обрабатывать текстовые файлы, JSON, бинарные данные и строить консольные утилиты. Завершим на высокой ноте — вы вычислите сумму чисел в бинарном файле, представленных 2-байтными значениями.
# - Вы скорее всего знаете, что существуют не только текстовые файлы. Различные форматы данных предусматривают специальное кодирование. Например, BMP изображения хранят некоторую заголовочную информацию и цвета всех пикселей в виде чисел. Давайте поработаем с такими данными. Нам дают файл в некотором формате, назовем его NUM. Он содержит список 2-байтных чисел. Для простоты будем считать, что отрицательных чисел не существует. Напишите программу, которая вычисляет сумму всех записанных в файле чисел в 2-байтном диапазоне.
# - Формат ввода
# - В файле numbers.num содержатся числа в указанном формате.
# - Формат вывода
# - Одно число — сумма всех чисел в файле на 2-байтном диапазоне.
# - Примечание
# - Для простоты файлы в примерах записаны в HEX формате. В этом виде файл представляется как последовательность четырехзначных шестнадцатеричных чисел.
# - В первом примере записано 5 шестнадцатеричных чисел: 1, 2, 3, 4, 5. Их сумма равна 15.
# - Во втором — 255 и 257. Их сумма равна 512.
# - Файл из примеров в изначальном виде можно загрузить здесь:
# - Первый пример
# - Второй пример
# - Если вы хотите изучить принцип хранения целых чисел в ЭВМ, советуем почитать про прямой, обратный и дополнительный коды.


# +
def task_20() -> None:
    """Суммирует 2-байтовые числа из файла с обрезкой до 16 бит."""
    with open("numbers.num", "rb") as src:
        payload: bytes = src.read()
    usable_len: int = len(payload) - (len(payload) % 2)
    total_sum_t: int = sum(
        int.from_bytes(payload[i : i + 2], "big", signed=False)
        for i in range(0, usable_len, 2)
    )
    print(total_sum_t % (1 << 16))


task_20()
