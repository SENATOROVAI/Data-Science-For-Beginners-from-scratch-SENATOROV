"""4.1 Functions."""

# +
# Функциональное приветствие


def print_hello(name: str) -> None:
    """Привет пользователю."""
    print(f"Hello, {name}!")


# +
# Функциональный НОД


def gcd(number1: int, number2: int) -> int:
    """Находит НОД."""
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return abs(number1)


# +
# Длина числа


def number_length(number1: int) -> int:
    """Находит длину числа."""
    return len(str(abs(number1)))


# +
# Копейка рубль бережёт


def take_small(money: list[float]) -> list[float]:
    """Фильтрует числа.

    Оставляет меньше 100.
    """
    return [coin for coin in money if coin < 100]


# +
# Виртуальный кликер
count = 0


def click() -> None:
    """Увеличение счетчика на 1."""
    # pylint: disable=global-statement
    global count
    count += 1


def get_count() -> int:
    """Возвращает значение счётчика."""
    return count


# +
# Странная игра
count = 0


def move(player: str, number: int) -> None:
    """Обновляет счёт."""
    # pylint: disable=global-statement
    global count
    if player == "Петя":
        count += number
    else:
        count -= number


def game_over() -> str:
    """Сообщает результат игры."""
    if count > 0:
        return "Петя"
    if count < 0:
        return "Ваня"
    return "Ничья"


# +
# Максимальный максимум
# pylint: disable=invalid-name
# flake8: noqa


def max2D(matrix: list[list[int]]) -> int:
    """Находит максимальное число в матрице."""
    return max(max(row) for row in matrix)


# +
# Числовое фрагментирование


def fragments(numbers: list[int]) -> list[list[int]]:
    """Возвращает список с возврастающими последовательностями."""
    final_lists = []

    if len(numbers) == 1:
        final_lists.append(numbers)
        return final_lists

    save_numbers = [numbers[0]]
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            save_numbers.append(numbers[index])
        else:
            final_lists.append(save_numbers)
            save_numbers = [numbers[index]]

    final_lists.append(save_numbers)
    return final_lists


# +
# Имя of the month


def month(number: int, language: str) -> str:
    """Возвращает название месяца на нужном языке."""
    months = {
        "en": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "ru": [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь",
        ],
    }

    # if 1 <= number <= 12 and language in months:
    return months[language][number - 1]


# +
# Числовая строка


def split_numbers(text: str) -> tuple[int, ...]:
    """Преобразует строку чисел в кортеж."""
    return tuple(map(int, text.split()))


# +
# Поиск гор


def find_mountains(heights: list[int]) -> tuple[int, ...]:
    """Находит позиции чисел больше соседних."""
    find_position = []
    for index in range(1, len(heights) - 1):
        if heights[index - 1] < heights[index] > heights[index + 1]:
            find_position.append(index + 1)

    return tuple(find_position)


# +
# Поиск гор 2


def find_mountainss(data: list[list[int]]) -> tuple[tuple[int, ...], ...]:
    """Находит позиции чисел больше соседних."""
    find_position = []
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[row]) - 1):
            cond1 = data[row][col] > data[row - 1][col - 1]
            cond2 = data[row][col] > data[row - 1][col]
            cond3 = data[row][col] > data[row - 1][col + 1]
            cond4 = data[row][col] > data[row][col - 1]
            cond5 = data[row][col] > data[row][col + 1]
            cond6 = data[row][col] > data[row + 1][col - 1]
            cond7 = data[row][col] > data[row + 1][col]
            cond8 = data[row][col] > data[row + 1][col + 1]

            if all([cond1, cond2, cond3, cond4, cond5, cond6, cond7, cond8]):
                find_position.append((row + 1, col + 1))
    return tuple(find_position)


# +
# Модернизация системы вывода
texts: list[str] = []


def modern_print(text: str) -> None:
    """Выводит уникальные строки."""
    if text not in texts:
        print(text)
        texts.append(text)


# +
# Шахматный «обед»


def can_eat(horse: tuple[int, int], other: tuple[int, int]) -> bool:
    """Проверка на валидность коня отведать."""
    cond1 = abs(horse[0] - other[0]) == 2 and abs(horse[1] - other[1]) == 1
    cond2 = abs(horse[0] - other[0]) == 1 and abs(horse[1] - other[1]) == 2

    return cond1 or cond2


# +
# Словарная строка


def get_dict(text: str) -> dict[str, str]:
    """Парсинг строки в словарь."""
    res_dict = {}
    for pair in text.split(";"):
        key, value = pair.split("=")
        res_dict[key] = value

    return res_dict


# +
# А роза упала на лапу Азора 7.0


def is_palindrome(xx: int | str | list[int] | tuple[int, ...] | float) -> bool:
    """Определение палиндрома."""
    if isinstance(xx, (int, str, list, tuple)):
        value_str = str(xx) if isinstance(xx, int) else xx
        return value_str == value_str[::-1]
    return False


# +
# Простая задача 5.0


def is_prime(number: int) -> bool:
    """Определяет простое ли число."""
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    if number < 2:
        return False

    return True


# +
# Слияние


def merge(nums1: tuple[int, ...], nums2: tuple[int, ...]) -> tuple[int, ...]:
    """Объединяет два отсортированных кортежа."""
    res_list = []

    index1 = 0
    index2 = 0

    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] <= nums2[index2]:
            res_list.append(nums1[index1])
            index1 += 1

        else:
            res_list.append(nums2[index2])
            index2 += 1

    if index1 < len(nums1):
        res_list.extend(nums1[index1:])

    if index2 < len(nums2):
        res_list.extend(nums2[index2:])

    return tuple(res_list)


# +
# Обмен содержимым


def swap(lst1: list[int], lst2: list[int]) -> None:
    """Свапает списки."""
    lst1[:], lst2[:] = lst2[:], lst1[:]


# +
def int_to_roman(num: int) -> str:
    """Переводит число в римский вид."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def roman(num1: int, num2: int) -> str:
    """Складывает 2 числа в римском виде."""
    sum_ab = num1 + num2
    roman_num1 = int_to_roman(num1)
    roman_num2 = int_to_roman(num2)
    roman_sum = int_to_roman(sum_ab)
    return f"{roman_num1} + {roman_num2} = {roman_sum}"
