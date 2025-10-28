"""Yandex handbook "Python Basics" answers."""

# +
from typing import Dict, List, Tuple, TypeVar, Union

# 1


def print_hello_1(name_1: str) -> None:
    """Выводит приветственное сообщение."""
    print(f"Hello, {name_1}!")


print_hello_1("Ruslan")


# +
# 2
def gcd_2(nat_number1_2: int, nat_number2_2: int) -> int:
    """Вычисляет наибольший общий делитель двух чисел."""
    while nat_number2_2:
        nat_number1_2, nat_number2_2 = (
            nat_number2_2, nat_number1_2 % nat_number2_2)
    return nat_number1_2


result_1_2: int = gcd_2(12, 45)
print(result_1_2)

# +
# 3


def number_length_3(number_3: int) -> int:
    """Возвращает количество цифр в целом числе."""
    if number_3 != 0:
        length_3: int = 0
    else:
        length_3 = 1
    while number_3 != 0:
        number_3 = int(number_3 / 10)
        length_3 += 1
    return length_3


result_2_3: int = number_length_3(12345)
print(result_2_3)

# +
# 4


def month_4(num_4: int, lang_4: str) -> str:
    """Возвращает название месяца по номеру и языку."""
    months_4: dict[str, list[str]] = {
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
    return months_4[lang_4][num_4 - 1]


result_3_4: str = month_4(1, "en")
print(result_3_4)

# +
# 5


def split_numbers_5(string_1_5: str) -> tuple[int, ...]:
    """Преобразует строку с числами в кортеж целых чисел."""
    result_5: List[int] = []
    for number_5 in string_1_5.split():
        result_5.append(int(number_5))
    return tuple(result_5)


result_4_5: tuple[int, ...] = split_numbers_5("1 2 3 4 5")
print(result_4_5)

# +
# 6
records_6: List[str] = []


def modern_print_6(string_2_6: str) -> None:
    """Выводит строку только если она не повторяется."""
    if string_2_6 not in records_6:
        records_6.append(string_2_6)
        print(string_2_6)


modern_print_6("Hello!")
modern_print_6("Hello!")
modern_print_6("How do you do?")
modern_print_6("Hello!")

# +
# 7


def can_eat_7(knight_7: tuple[int, int], cell_7: tuple[int, int]) -> bool:
    """Проверяет, может ли конь съесть фигуру на заданной клетке."""
    x_cell_7: int = knight_7[0] - cell_7[0]
    if x_cell_7 < 0:
        x_cell_7 = -x_cell_7
    y_cell_7: int = knight_7[1] - cell_7[1]
    if y_cell_7 < 0:
        y_cell_7 = -y_cell_7
    distances_7: List[int] = [x_cell_7, y_cell_7]
    distances_7.sort()
    return distances_7 == [1, 2]


result_5_7: bool = can_eat_7((5, 5), (6, 6))
print(result_5_7)


# +
# 8
def is_palindrome_8(
    test_8: Union[int, str, List[int], Tuple[int, ...], float]
) -> bool:
    """Проверяет, является ли объект палиндромом."""
    if isinstance(test_8, (int, float)):
        if test_8 < 0:
            test_8 = -test_8
        test_8 = str(test_8)
    return test_8 == test_8[::-1]


result_8_8: bool = is_palindrome_8(123)
print(result_8_8)

# +
# 9


def is_prime_9(number_9: int) -> bool:
    """Проверяет, является ли число простым."""
    if number_9 < 2:
        return False
    divider_9: int
    for divider_9 in range(2, int(number_9**0.5) + 1):
        if number_9 % divider_9 == 0:
            return False
    return True


result_7_9: bool = is_prime_9(1001459)
print(result_7_9)

# +
# 10


def merge_10(
    tuple_1_10: tuple[int, ...], tuple_2_10: tuple[int, ...]
) -> tuple[int, ...]:
    """Объединяет два отсортированных кортежа в один отсортированный."""
    turn_1_10: List[int] = list(tuple_1_10)
    turn_2_10: List[int] = list(tuple_2_10)
    result_10: List[int] = []
    while turn_1_10 and turn_2_10:
        if turn_1_10[0] > turn_2_10[0]:
            result_10.append(turn_2_10.pop(0))
        else:
            result_10.append(turn_1_10.pop(0))
    result_10.extend(turn_1_10)
    result_10.extend(turn_2_10)
    return tuple(result_10)


result_8_10: tuple[int, ...] = merge_10((1, 2), (3, 4, 5))
print(result_8_10)

# +
# 11


def split_numbers_11(input_line_11: str) -> Tuple[int, ...]:
    """Преобразует строку чисел в кортеж целых чисел."""
    numbers_list_11: List[int] = []
    for num_str_11 in input_line_11.split():
        numbers_list_11.append(int(num_str_11))
    return tuple(numbers_list_11)


test_line_11: str = "1 2 3 4 5"
result_11: Tuple[int, ...] = split_numbers_11(test_line_11)
print(result_11)

# +
# 12


def find_mountains_12(height_list_12: List[int]) -> Tuple[int, ...]:
    """Находит позиции горных вершин в одномерном массиве."""
    mountains_12: List[int] = []
    n_12: int = len(height_list_12)
    for i_12 in range(1, n_12 - 1):
        if height_list_12[i_12] > height_list_12[i_12 - 1]:
            if height_list_12[i_12] > height_list_12[i_12 + 1]:
                mountains_12.append(i_12 + 1)
    return tuple(mountains_12)


test_heights_12: List[int] = [1, 3, 2, 4, 1, 5, 3, 2]
result_12: Tuple[int, ...] = find_mountains_12(test_heights_12)
print(result_12)


# +
# 13
def find_mountains_13(
    matrix_data_13: List[List[int]]
) -> Tuple[Tuple[int, int], ...]:
    """Находит позиции горных вершин в двумерном массиве."""
    rows_13: int = len(matrix_data_13)
    if rows_13 == 0:
        return tuple()
    cols_13: int = len(matrix_data_13[0])
    mountains_13: List[Tuple[int, int]] = []
    directions_13: List[Tuple[int, int]] = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for i_13 in range(1, rows_13 - 1):
        for j_13 in range(1, cols_13 - 1):
            current_13: int = matrix_data_13[i_13][j_13]
            is_mountain_13: bool = True
            for di_13, dj_13 in directions_13:
                if current_13 <= matrix_data_13[i_13 + di_13][j_13 + dj_13]:
                    is_mountain_13 = False
                    break
            if is_mountain_13:
                mountains_13.append((i_13 + 1, j_13 + 1))
    return tuple(mountains_13)


test_data_13: List[List[int]] = [[1, 2, 1, 3], [4, 5, 2, 6], [1, 2, 3, 1]]
result_13: Tuple[Tuple[int, int], ...] = find_mountains_13(test_data_13)
print(result_13)

# +
# 14
lst_14: List[str] = []


def modern_print_14(output_string_14: str) -> None:
    """Выводит строку только если она не повторялась ранее."""
    if output_string_14 not in lst_14:
        print(output_string_14)
        lst_14.append(output_string_14)


modern_print_14("Hello")
modern_print_14("World")
modern_print_14("Hello")


# +
# 15
def can_eat_15(
    knight_pos_15: Tuple[int, int], target_pos_15: Tuple[int, int]
) -> bool:
    """Проверяет, может ли конь съесть фигуру за один ход."""
    dx_15: int = abs(knight_pos_15[0] - target_pos_15[0])
    dy_15: int = abs(knight_pos_15[1] - target_pos_15[1])
    return dx_15 + dy_15 == 3 and dx_15 != 0 and dy_15 != 0


result_15: bool = can_eat_15((2, 1), (4, 2))
print(result_15)

# +
# 16


def get_dict_16(input_text_16: str) -> Dict[str, Union[int, float, str]]:
    """Преобразует строку в словарь с автоматическим определением типов."""

    def convert_value_16(val_16: str) -> Union[int, float, str]:
        try:
            return int(val_16)
        except ValueError:
            try:
                return float(val_16)
            except ValueError:
                return val_16

    pairs_16: List[str] = input_text_16.split(";")
    result_dict_16: Dict[str, Union[int, float, str]] = {}
    for pair_16 in pairs_16:
        key_16, value_16 = pair_16.split("=")
        result_dict_16[key_16] = convert_value_16(value_16)
    return result_dict_16


test_text_16: str = "a=1;b=2.5;c=hello"
result_16: Dict[str, Union[int, float, str]] = get_dict_16(test_text_16)
print(result_16)

# +
# 17


def is_palindrome_17(
    check_value_17: Union[int, str, List[int], Tuple[int, ...], float],
) -> bool:
    """Проверяет, является ли объект палиндромом."""
    if isinstance(check_value_17, (int, float)):
        str_value_17: str = str(abs(check_value_17))
        return str_value_17 == str_value_17[::-1]
    if isinstance(check_value_17, str):
        return check_value_17 == check_value_17[::-1]
    list_value_17: List[int] = list(check_value_17)
    return list_value_17 == list_value_17[::-1]


result_17_1: bool = is_palindrome_17(12321)
result_17_2: bool = is_palindrome_17("abba")
result_17_3: bool = is_palindrome_17([1, 2, 1])
print(result_17_1)
print(result_17_2)
print(result_17_3)

# +
# 18


def is_prime_18(check_number_18: int) -> bool:
    """Проверяет, является ли число простым."""
    if check_number_18 < 2:
        return False
    divisor_18: int
    for divisor_18 in range(2, int(check_number_18**0.5) + 1):
        if check_number_18 % divisor_18 == 0:
            return False
    return True


result_18: bool = is_prime_18(17)
print(result_18)


# +
# 19
def merge_19(
    tuple1_19: Tuple[int, ...], tuple2_19: Tuple[int, ...]
) -> Tuple[int, ...]:
    """Объединяет два кортежа и сортирует результат пузырьковой сортировкой."""
    combined_19: List[int] = list(tuple1_19) + list(tuple2_19)
    n_19: int = len(combined_19)
    i_19: int
    j_19: int
    for i_19 in range(n_19):
        for j_19 in range(0, n_19 - i_19 - 1):
            if combined_19[j_19] > combined_19[j_19 + 1]:
                temp_19: int = combined_19[j_19]
                combined_19[j_19] = combined_19[j_19 + 1]
                combined_19[j_19 + 1] = temp_19
    return tuple(combined_19)


result_19: Tuple[int, ...] = merge_19((1, 3, 5), (2, 4, 6))
print(result_19)

# +
# 20
T = TypeVar("T")


def swap_20(list1_20: List[T], list2_20: List[T]) -> None:
    """Обменивает содержимое двух списков."""
    temp_20: List[T] = list1_20[:]
    list1_20[:] = list2_20[:]
    list2_20[:] = temp_20[:]


list_a_20: List[int] = [1, 2, 3]
list_b_20: List[int] = [4, 5, 6]
swap_20(list_a_20, list_b_20)
print(list_a_20)
print(list_b_20)
