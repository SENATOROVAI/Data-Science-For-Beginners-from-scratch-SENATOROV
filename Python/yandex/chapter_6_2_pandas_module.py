"""Pandas module."""

# +
# 1


import os
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd


def length_stats(line: str) -> pd.Series:  # type: ignore
    """Return a Series mapping each unique word in the string to its length."""
    clean_line = "".join(ch for ch in line if ch.isalpha() or ch.isspace())
    words = sorted(set(clean_line.lower().split()))
    return pd.Series({word: len(word) for word in words})


print(length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка."))

# +
# 2


def length_stats_double(line: str) -> tuple[pd.Series, pd.Series]:  # type: ignore
    """Return two Series: words with odd and even lengths."""
    clean_line = "".join(ch for ch in line if ch.isalpha() or ch.isspace())
    words = sorted(set(clean_line.lower().split()))
    series = pd.Series({word: len(word) for word in words})
    return series[series % 2 != 0], series[series % 2 == 0]


odd, even = length_stats_double("Мама мыла раму")
print(odd)
print(even)

# +
# 3


# fmt: off
def cheque(
    price_list: pd.Series,  # type: ignore
    **kwargs: int
) -> pd.DataFrame:
    """Return a DataFrame with products, prices, quantities, and total cost."""
    products = sorted(kwargs.keys())
    prices = [price_list.get(p, float("nan")) for p in products]

    data = pd.DataFrame(
        {
            "product": products,
            "price": prices,
            "number": [kwargs[p] for p in products],
        }
    )

    data["cost"] = data["price"] * data["number"]
    return data
# fmt: on


products_2 = ["bread", "milk", "soda", "cream"]
prices_2 = [37, 58, 99, 72]
price_list_2 = pd.Series(prices_2, products_2)
result_1 = cheque(price_list_2, soda=3, milk=2, cream=1)
print(result_1)

# +
# 4


def discount(result: pd.DataFrame, rate: float = 0.5) -> pd.DataFrame:
    """Return a copy of the DataFrame with a discount."""
    df = result.copy()
    df["cost"] = df["cost"].astype(float)
    mask_1 = df["number"] > 2
    df.loc[mask_1, "cost"] *= rate
    return df


products_3 = ["bread", "milk", "soda", "cream"]
prices_3 = [37, 58, 99, 72]
price_list_3 = pd.Series(prices_3, products_3)
result_ = cheque(price_list_3, soda=3, milk=2, cream=1)
with_discount = discount(result_)
print(result_)
print(with_discount)

# +
# 5


# fmt: off
def get_long(
    data_2: pd.Series,  # type: ignore   
    min_length: int = 5
) -> pd.Series:  # type: ignore  
    """Return a Series containing only certain values."""
    return data_2[data_2 >= min_length]
# fmt: on


data_smpl = pd.Series([3, 5, 6, 6], ["мир", "питон", "привет", "яндекс"])
filtered = get_long(data_smpl)
print(data_smpl)
print(filtered)

# +
# 6


def best(progress: pd.DataFrame, threshold: int = 4) -> pd.DataFrame:
    """Return students with all grades >= threshold."""
    data = progress.copy()
    numeric = data.select_dtypes(include="number")
    mask_3 = (numeric >= threshold).all(axis=1)
    return data[mask_3]


columns_1 = ["name", "maths", "physics", "computer science"]
data_sam = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal_1 = pd.DataFrame(data_sam, columns=columns_1)
filtered_2: pd.DataFrame = best(journal_1)
print(journal_1)
print(filtered_2)

# +
# 7


def need_to_work_better(progress: pd.DataFrame, threshold: int = 3) -> pd.DataFrame:
    """Return students with any grade below threshold."""
    data = progress.copy()
    numeric = data.select_dtypes(include="number")
    mask_2 = (numeric < threshold).any(axis=1)
    return data[mask_2]


columns_2 = ["name", "maths", "physics", "computer science"]
data_obj = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal_2 = pd.DataFrame(data_obj, columns=columns_2)
filtered_3 = need_to_work_better(journal_2)
print(journal_2)
print(filtered_3)

# +
# 8


def update(progress: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame with average grade, sorted by average and name."""
    data = progress.copy()
    numeric = data.select_dtypes(include="number")
    data["average"] = numeric.mean(axis=1)
    return data.sort_values(["average", "name"], ascending=[False, True])


columns_3 = ["name", "maths", "physics", "computer science"]
data_sbs = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal_3 = pd.DataFrame(data_sbs, columns=columns_3)
filtered_4: pd.DataFrame = update(journal_3)
print(journal_3)
print(filtered_4)

# +
# 9


top_x, top_y = map(int, input().split())
bottom_x, bottom_y = map(int, input().split())

try:
    base_dir = Path(__file__).parent
except NameError:
    base_dir = Path(os.getcwd())

csv_path = base_dir / "data.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")
game_data = pd.read_csv(csv_path)

mask_4 = (game_data["x"].between(top_x, bottom_x)) & (
    game_data["y"].between(bottom_y, top_y)
)

filtered_5: pd.DataFrame = game_data[mask_4]
print(filtered_5)

# +
# 10


def values(
    func: Callable[[float], float], start: float, end: float, step: float
) -> pd.Series:  # type: ignore
    """Return Series of function values for range [start, end] with step."""
    if step <= 0:
        raise ValueError("Step must be positive.")
    x_var = np.arange(start, end + step, step, dtype=float)
    y_var = np.array(np.vectorize(func)(x_var), dtype=float)
    return pd.Series(y_var, index=x_var, dtype=float)

def min_extremum(data: pd.Series) -> float:  # type: ignore
    """Return x of leftmost minimum."""
    return float(data.idxmin())


def max_extremum(data: pd.Series) -> float:  # type: ignore
    """Return x of rightmost maximum."""
    max_val = data.max()
    return float(data[data == max_val].index.max())


data_mt = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data_mt)
print(min_extremum(data_mt))
print(max_extremum(data_mt))
