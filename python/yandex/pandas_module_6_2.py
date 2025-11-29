"""Модуль pandas.

В этом параграфе вы познакомитесь с библиотекой pandas — одним из ключевых инструментов
для анализа данных в Python. Вы узнаете, как создавать и использовать объекты Series и
DataFrame, считывать данные из файлов, фильтровать и сортировать таблицы, выполнять
агрегирование и строить простые визуализации. Библиотека pandas построена на базе numpy и
предоставляет удобный интерфейс для работы с табличными структурами, которые встречаются
почти во всех проектах, связанных с анализом, отчётами и машинным обучением.
"""

# ## Длины всех слов - 2.
#
# - Напишите функцию length_stats, которая получает текст, а возвращает объект Series со словами в качестве индексов и их длинами в качестве значений.
# - Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.

# +
from __future__ import annotations

from collections.abc import Iterator
from typing import Callable

# +
import numpy as np
import pandas as pd


def length_stats(text: str) -> pd.Series:  # type: ignore
    """Возвращает Series с длинами уникальных слов."""
    words: list[str] = []
    word: list[str] = []
    for char in text.lower():
        if char.isalpha():
            word.append(char)
        elif word:
            words.append("".join(word))
            word = []

    if word:
        words.append("".join(word))
    words = sorted(set(words))
    return pd.Series(map(len, words), index=words, dtype="int64")


# -

# ## Длины всех слов по чётности.
#
# - В этот раз продумайте функцию length_stats, которая получает текст, а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.
# - Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def length_stats_2(line: str) -> tuple[pd.Series, pd.Series]:  # type: ignore
    """Возвращает кортеж с Series четных и нечетных длин слов."""
    clean_line = "".join(ch for ch in line if ch.isalpha() or ch.isspace())
    words = sorted(set(clean_line.lower().split()))
    series = pd.Series({word: len(word) for word in words})
    return series[series % 2 != 0], series[series % 2 == 0]


# ## Чек - 2.
#
# - В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
# - Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия, а значениями — цены.
# - Напишите функцию, cheque, которая принимает прайс-лист и список покупок в виде неопределённого количества именованных параметров (ключ — название товара, значение — количество).
# - Функция должна вернуть объект DataFrame со столбцами:
# - наименование продукта (product);
# - цена за единицу (price);
# - количество (number);
# - итоговая цена (cost).
# - Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.


def cheque(price_list: pd.Series, **kwargs: int) -> pd.DataFrame:  # type: ignore
    """Создает чек покупок с сортировкой по товарам."""
    df: pd.DataFrame = pd.DataFrame(
        {
            "product": list(kwargs.keys()),
            "price": [price_list[p] for p in kwargs],
            "number": list(kwargs.values()),
            "cost": [price_list[p] * n for p, n in kwargs.items()],
        }
    )

    return df.sort_values("product").reset_index(drop=True)


# ## Акция.
#
# - Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:
# - При покупке больше двух товаров — скидка 50%
# - мелкий шрифт: скидка распространяется только на товары купленные в количестве более двух штук
# - Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.
# - Примечание
# - Не удаляйте функцию cheque, она потребуется для тестирования.
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def cheque_2(price_list: pd.DataFrame, rate: float = 0.5) -> pd.DataFrame:
    """Создает чек покупок с сортировкой по товарам."""
    df_copy = price_list.copy()
    df_copy["cost"] = df_copy["cost"].astype(float)
    mask = df_copy["number"] > 2
    df_copy.loc[mask, "cost"] *= rate
    return df_copy


# ## Длинные слова.
#
# - Фильтрация данных — одна из первостепенных задач их анализа.
# - Напишите функцию get_long, принимающую серию формата первой задачи и фильтрующую её по именованному параметру min_length (по умолчанию 5).
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def length_stats_3(text: pd.Series, min_length: int = 5) -> pd.Series:  # type: ignore
    """Возвращает Series с длинами уникальных слов."""
    return text[text >= min_length]


# ## Отчёт успеваемости.
#
# - Во всех без исключения учебных заведениях ведутся журналы успеваемости. Это отличный пример данных, подлежащих обработке.
# - Рассмотрим журнал летней олимпиадной школы, в которой основными предметами выступают математика, физика и информатика. Данные об успеваемости представлены DataFrame со столбцами:
# - name — имя;
# - maths — оценка по математике;
# - physics — оценка по физике;
# - computer science — оценка по информатике.
# - Напишите функцию best, которая фильтрует всех «ударников» в журнале.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def best(journal: pd.Series, min_length: int = 5) -> pd.Series:  # type: ignore
    """Возвращает Series, содержащий только определенные значения."""
    return journal[journal >= min_length]


# ## Отчёт неуспеваемости.
#
# - Продолжим обрабатывать DataFrame из прошлой задачи.
# - Напишите функцию need_to_work_better, которая выбирает тех, у кого есть хотя бы одна двойка.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def need_to_work_better(journal: pd.DataFrame, threshold: int = 4) -> pd.DataFrame:
    """Возвращает студентов с хотя бы одной двойкой."""
    data_copy = journal.copy()
    numeric_columns = data_copy.select_dtypes(include="number")
    mask = (numeric_columns >= threshold).all(axis=1)
    return data_copy[mask]


# ## Обновление журнала.
#
# - Продолжим обрабатывать DataFrame из прошлых задач.
# - Напишите функцию update, которая добавляет к данным столбец average, содержащий среднюю оценку ученика, а также сортирует данные по убыванию этого столбца, а при равенстве средних — по имени лексикографически.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def update(journal: pd.DataFrame, threshold: int = 3) -> pd.DataFrame:
    """Добавляет средний балл и сортирует журнал."""
    data_copy = journal.copy()
    numeric_columns = data_copy.select_dtypes(include="number")
    mask = (numeric_columns < threshold).any(axis=1)
    return data_copy[mask]


# ## Бесконечный морской бой.
#
# - Представьте себе поле морского боя, которое не имеет границ. Для простоты координаты выстрелов будем обозначать целыми координатами на плоскости.
# - Бесконечное поле порождает большое количество данных, которые требуется проанализировать. Один из игроков для упрощения этой задачи просит вас написать программу, которая обрезает данные до ограниченного прямоугольника.
# - Формат ввода
# - В первой строке записано два числа — координаты верхнего левого угла. Во второй строке — правого нижнего.
# - В файле data.csv находится датасет с координатами всех выстрелов противника.
# - Формат вывода
# - Часть датасета, ограниченная заданным прямоугольником.

# +
x1: int
y1: int
x1, y1 = map(int, input().split())

x2: int
y2: int
x2, y2 = map(int, input().split())

data: pd.DataFrame = pd.read_csv("data.csv")

left: int = min(x1, x2)
right: int = max(x1, x2)
top: int = max(y1, y2)
bottom: int = min(y1, y2)

filtered_data: pd.DataFrame = data.loc[
    data["x"].between(left, right) & data["y"].between(bottom, top)
]

print(filtered_data)
# -

# ## Экстремум функции.
#
# - Экстремум в математике — максимальное или минимальное значение функции на заданном множестве.
# - Чаще всего математики для поиска экстремума функции прибегают к её дифференцированию. Однако мы можем обойти этот трудоёмкий процесс и схитрить.
# - Напишите три функции:
# - values(func, start, end, step), строящую Series значений функции в точках диапазона и принимающую:
# - функцию одной переменной;
# - начало диапазона;
# - конец диапазона;
# - шаг вычисления;
# - min_extremum(data) возвращает точку, в которой был достигнут минимум на диапазоне;
# - max_extremum(data) возвращает точку, в который был достигнут максимум на диапазоне.
# - Примечание
# - Ваше решение должно содержать только функции.
# - В решении не должно быть вызовов требуемых функций.


def values(
    func: Callable[[float], float],
    start: float,
    end: float,
    step: float,
) -> Iterator[tuple[float, float]]:
    """Возвращает итератор пар (x, y) значений функции в точках диапазона."""
    if step <= 0:
        raise ValueError("Шаг должен быть положительным.")
    x_values = np.arange(start, end + step, step)
    for x_val in x_values:
        x_float = float(x_val)
        y_float = float(func(x_float))
        yield x_float, y_float


def min_extremum(data_: Iterator[tuple[float, float]]) -> float:
    """Возвращает x самого левого минимума."""
    data_list = list(data_)
    min_y = min(y_value for _, y_value in data_list)
    min_points = [x_value for x_value, y_value in data_list if y_value == min_y]
    return min(min_points)


def max_extremum(data_: Iterator[tuple[float, float]]) -> float:
    """Возвращает x самого правого максимума."""
    data_list = list(data_)
    max_y = max(y_value for _, y_value in data_list)
    max_points = [x_value for x_value, y_value in data_list if y_value == max_y]
    return max(max_points)
