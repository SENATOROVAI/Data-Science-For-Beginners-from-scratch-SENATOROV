"""Модуль pandas."""

# +
from __future__ import annotations

from pathlib import Path
from typing import Callable, Iterator

import numpy as np
import pandas as pd


# 1
def length_stats_1(line: str) -> pd.Series:  # type: ignore
    """Возвращает Series, сопоставляющий каждое уникальное слово в строке с его длиной."""
    clean_line = "".join(ch for ch in line if ch.isalpha() or ch.isspace())
    words = sorted(set(clean_line.lower().split()))
    return pd.Series({word: len(word) for word in words})

# +
# 2


def length_stats_double_2(line: str) -> tuple[pd.Series, pd.Series]:  # type: ignore
    """Возвращает два Series: слова с нечетной и четной длиной."""
    clean_line = "".join(ch for ch in line if ch.isalpha() or ch.isspace())
    words = sorted(set(clean_line.lower().split()))
    series = pd.Series({word: len(word) for word in words})
    return series[series % 2 != 0], series[series % 2 == 0]

# +
# 3


def cheque_3(price_list: pd.Series, **kwargs: int) -> pd.DataFrame:  # type: ignore
    """Возвращает DataFrame с продуктами, ценами, количествами и общей стоимостью."""
    products = sorted(kwargs.keys())
    prices = [price_list.get(product, float("nan")) for product in products]
    numbers = [kwargs[product] for product in products]
    data_frame = pd.DataFrame({"product": products, "price": prices, "number": numbers})
    data_frame["cost"] = data_frame["price"] * data_frame["number"]
    return data_frame

# +
# 4


def discount_4(result_df: pd.DataFrame, rate: float = 0.5) -> pd.DataFrame:
    """Возвращает копию DataFrame со скидкой."""
    df_copy = result_df.copy()
    df_copy["cost"] = df_copy["cost"].astype(float)
    mask = df_copy["number"] > 2
    df_copy.loc[mask, "cost"] *= rate
    return df_copy

# +
# 5


def get_long_5(data_series: pd.Series, min_length: int = 5) -> pd.Series:  # type: ignore
    """Возвращает Series, содержащий только определенные значения."""
    return data_series[data_series >= min_length]

# +
# 6


def best_6(progress_df: pd.DataFrame, threshold: int = 4) -> pd.DataFrame:
    """Возвращает студентов со всеми оценками >= порога."""
    data_copy = progress_df.copy()
    numeric_columns = data_copy.select_dtypes(include="number")
    mask = (numeric_columns >= threshold).all(axis=1)
    return data_copy[mask]

# +
# 7


def need_to_work_better_7(
    progress_df: pd.DataFrame, threshold: int = 3
) -> pd.DataFrame:
    """Возвращает студентов с любой оценкой ниже порога."""
    data_copy = progress_df.copy()
    numeric_columns = data_copy.select_dtypes(include="number")
    mask = (numeric_columns < threshold).any(axis=1)
    return data_copy[mask]

# +
# 8


def update_8(progress_df: pd.DataFrame) -> pd.DataFrame:
    """Возвращает DataFrame со средней оценкой, отсортированный по средней и имени."""
    data_copy = progress_df.copy()
    numeric_columns = data_copy.select_dtypes(include="number")
    data_copy["average"] = numeric_columns.mean(axis=1)
    return data_copy.sort_values(["average", "name"], ascending=[False, True])

# +
# 9


def filter_game_data_9(
    top_x: int, top_y: int, bottom_x: int, bottom_y: int, csv_path: Path
) -> pd.DataFrame:
    """Фильтрует данные игры по координатам."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    game_data = pd.read_csv(csv_path)
    mask = (game_data["x"].between(top_x, bottom_x)) & (
        game_data["y"].between(bottom_y, top_y)
    )
    return game_data[mask]


# +
# 10
def values_10(
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
        yield x_val, func(x_val)


def min_extremum_10(data: Iterator[tuple[float, float]]) -> float:
    """Возвращает x самого левого минимума."""
    data_list = list(data)
    min_y = min(y_value for _, y_value in data_list)
    min_points = [x_value for x_value, y_value in data_list if y_value == min_y]
    return min(min_points)


def max_extremum_10(data: Iterator[tuple[float, float]]) -> float:
    """Возвращает x самого правого максимума."""
    data_list = list(data)
    max_y = max(y_value for _, y_value in data_list)
    max_points = [x_value for x_value, y_value in data_list if y_value == max_y]
    return max(max_points)
