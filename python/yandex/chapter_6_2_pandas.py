"""Pandas."""

# Pandas provides two main data structures:
#
# Series – a one-dimensional array that can store any data type.
# DataFrame – a two-dimensional table where columns are Series objects.
#
# ```python
# s = pd.Series(data, index=index)
# ```
#
# The data for a Pandas object can be:
#
# A NumPy array, a dictionary, or a single value.
# The index argument defines axis labels, which can be numbers or, more commonly, strings.
# If data is a NumPy array, the index must have the same length as data. If no index is provided, it defaults to [0, ..., len(data) - 1].
#
#
# ```python
# s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
# print(s)
# print()
# s = pd.Series(np.linspace(0, 1, 5))
# print(s)
# ```
#
# A Series in Pandas is similar to a dictionary because it can use string labels instead of numeric indices.
#
# If data is a dictionary and index is not provided, the dictionary keys become the index.
# If an index is specified, it can differ in length from the dictionary.
# Missing values (when an index has no matching key in data) are represented as NaN, Pandas' standard notation for missing data.
#
# ```python
# d = {"a": 10, "b": 20, "c": 30, "g": 40}
# print(pd.Series(d))
# print()
# print(pd.Series(d, index=["a", "b", "c", "d"]))
# ```
#
# If data is a single number, an index must be provided.
#
# The number of elements in the Series will match the number of labels in index.
# Each value in the Series will be the same as data.
#
# ```python
# index = ["a", "b", "c"]
# print(pd.Series(5, index=index))
# ```
#
#
# A Series supports:
#
# Accessing elements by index.
# Slicing operations.
# Element-wise mathematical operations, similar to NumPy arrays.
#
# ```python
# s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
# print("Выбор одного элемента")
# print(s["a"])
# print("Выбор нескольких элементов")
# print(s[["a", "d"]])
# print("Срез")
# print(s[1:])
# print("Поэлементное сложение")
# print(s + s)
# ```
#
# A Series allows data filtering using conditions applied to the index.
#
# ```python
# s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
# print("Фильтрация")
# print(s[s > 2])
# ```
#
# A Series object has:
#
# The name attribute, which stores the dataset's name.
# The index.name attribute, which assigns a name to the index.
#
# ```python
# s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
# s.name = "Данные"
# s.index.name = "Индекс"
# print(s)
# ```
#
#
# A DataFrame handles two-dimensional tabular data.
#
# The easiest way to create a DataFrame is from a Python dictionary, like this:
#
# ```python
# students_marks_dict = {
#     "student": ["Студент_1", "Студент_2", "Студент_3"],
#     "math": [5, 3, 4],
#     "physics": [4, 5, 5],
# }
# students = pd.DataFrame(students_marks_dict)
# print(students)
# ```
#
# A DataFrame has two types of indices:
#
# index – for rows.
# columns – for column labels.
#
# ```python
# print(students.index)
# print(students.columns)
# ```
#
# By default, a DataFrame assigns numeric row indices.
#
# You can change row indices by assigning a list to the index attribute.
#
# ```python
# students.index = ["A", "B", "C"]
# print(students)
# ```
#
# To access table records using a string label, the loc attribute is used.
#
# It allows selecting rows by label.
# Supports slicing operations with string labels.
#
# ```python
# print(students.loc["B":])
# ```
#
# We can verify that DataFrame columns are Series objects by selecting a column and checking its type. Each column in a DataFrame is essentially a Series.
#
# ```python
# print(type(students["student"]))
# ```
#
# Tabular data is usually stored in files, commonly referred to as datasets.
# Pandas supports reading and writing datasets in various formats, including CSV, Excel, SQL, HTML, JSON, and more.
#
# Here are some examples of how to work with different file formats in Pandas:
#
# - CSV:
#     - Read: pd.read_csv(file)
#     - Write: df.to_csv(file)
# - Excel:
#     - Read: pd.read_excel(file)
#     - Write: df.to_excel(file)
# - JSON:
#     - Read: pd.read_json(file)
#     - Write: df.to_json(file)
#
# CSV example:
#
# ```python
# import numpy as np
# import pandas as pd
#
# students = pd.read_csv("StudentsPerformance.csv")
# ```
#
# To get the first n rows of a dataset, use the head(n) method.
#
# By default, head() returns the first 5 rows.
# You can specify n to get a different number of rows, e.g., df.head(10).
#
# ```python
# print(students.head())
# ```
#
# To get the last n rows of a dataset, use the tail(n) method.
#
# By default, tail() returns the last 5 rows.
# You can specify n to get a different number of rows, e.g., df.tail(10).
#
# ```python
# print(students.tail(3))
# ```
#
# To extract a portion of a dataset, you can use slicing:
#
# ```python
# print(students[10:13])
# ```
#
# Conditions can be used to filter data in a DataFrame.
#
# ```python
# print(students[students["test preparation course"] == "completed"]["math score"].head())
# ```
#
# To display the top 5 test results for three subjects from the previous selection, use the sort_values()
#
# ```python
# students[students["test preparation course"] == "completed"]
# print(
#     with_course[["math score", "reading score", "writing score"]]
#     .sort_values(["math score", "reading score", "writing score"], ascending=False)
#     .head()
# )
# ```
#
#
# To sort students by their total test scores, follow these steps:
#
#
# ```python
# with_course = students[students["test preparation course"] == "completed"]
# students["total score"] = (
#     students["math score"] + students["reading score"] + students["writing score"]
# )
# print(students.sort_values(["total score"], ascending=False).head())
# ```
#
# To add a column using the assign() method, follow this approach, it creates a new table:
#
# ```python
# scores = students.assign(
#     total_score=lambda x: x["math score"] + x["reading score"] + x["writing score"]
# )
#
# top_students = scores.sort_values(["total_score"], ascending=False).head()
#
# print(top_students)
# ```
#
# To group and count records based on gender and test preparation course completion, use the groupby() and count() methods:
#
# ```python
# print(students.groupby(["gender", "test preparation course"])["writing score"].count())
# ```
#
# To perform aggregation using multiple statistical functions, use the agg() method.
#
#
# ```python
# agg_functions = {"math score": ["mean", "median"]}
#
# aggregated_scores = students.groupby(["gender", "test preparation course"]).agg(
#     agg_functions
# )
#
# print(aggregated_scores)
# ```
#
# For data visualization, Pandas uses the `Matplotlib` library.
#
# ```python
# import matplotlib.pyplot as plt
# ```
#
# To create a histogram showing the distribution of students' math test scores, use Matplotlib and Pandas:
#
# ```python
# plt.hist(students["math score"], label="Тест по математике")
# plt.xlabel("Баллы за тест")
# plt.ylabel("Количество студентов")
# plt.legend()
# plt.show()
# ```

# +
# fmt: off
from typing import Callable

import numpy as np
# 6
import pandas as pd

# fmt: on

# ! pip install pandas
# ! pip install numpy
# ! pip install matplotlib

# +
# 1


def length_stats(line: str) -> pd.Series:  # type: ignore
    """Calculate length statistics for unique words in a string."""
    line = "".join([char for char in line if char.isalpha() or char == " "])
    data = sorted(set(line.lower().split()))

    return pd.Series(data=list(map(len, data)), index=data)


# +
# 2


def length_stats_tuple(line: str) -> tuple[pd.Series, pd.Series]:  # type: ignore
    """Return tuple of Series with odd and even length words."""
    line = "".join([char for char in line if char.isalpha() or char == " "])
    data = sorted(set(line.lower().split()))
    series = pd.Series(data=list(map(len, data)), index=data)
    return series[series % 2 != 0], series[series % 2 == 0]


# +
# 3


def cheque(price_list: pd.Series, **kwargs: int) -> pd.DataFrame:  # type: ignore
    """Create a DataFrame with product details and calculate total cost."""
    my_products = sorted(kwargs)

    data = pd.DataFrame(
        {
            "product": my_products,
            "price": [price_list[p] for p in my_products],
            "number": [kwargs[p] for p in my_products],
        }
    )

    data["cost"] = data["price"] * data["number"]
    return data


# +
# 4


def discount(result: pd.DataFrame):  # type: ignore
    """Apply discount to products and return updated DataFrame."""
    copy = result.copy()
    copy.loc[result["number"] > 2, "cost"] = result["cost"] * 0.5
    return copy


# +
# 5


def get_long(data: pd.Series, min_length: int = 5):  # type: ignore
    """Return Series with values >= min_length."""
    return data[data >= min_length]


# +
# 6


def best(progress: pd.DataFrame):  # type: ignore
    """Return students with good grades in all subjects."""
    data = progress.copy()
    return data[
        (data["maths"] >= 4) & (data["physics"] >= 4) & (data["computer science"] >= 4)
    ]


# +
# 7


def need_to_work_better(progress: pd.DataFrame):  # type: ignore
    """Return students with good grades in all subjects."""
    data = progress.copy()
    return data[
        (data["maths"] < 3) | (data["physics"] < 3) | (data["computer  science"] < 3)
    ]


# +
# 8


def update(progress: pd.DataFrame):  # type: ignore
    """Return DataFrame with average grade sorted by average and name."""
    data = progress.copy()
    data["average"] = (data["physics"] + data["maths"] + data["computer science"]) / 3
    sorted_data = data.sort_values(["average", "name"], ascending=(False, True))
    return sorted_data


# +
# 9


# pylint: disable=all
# flake8: noqa
top_angle_x, top_angle_y = map(int, input().split())
bottom_angle_x, bottom_angle_y = map(int, input().split())
game_data = pd.read_csv("data.csv")
print(
    game_data[
        (top_angle_x <= game_data["x"])
        & (game_data["x"] <= bottom_angle_x)
        & (bottom_angle_y <= game_data["y"])
        & (game_data["y"] <= top_angle_y)
    ]
)
# pylint: enable=all
# flake8: enable

# +
# 10


def values(
    func: Callable[[float], float], start: float, end: float, step: float
) -> pd.Series:  # type: ignore
    """Create Series of function values with given range and step."""
    index = np.arange(start, end + step, step, dtype="float64")
    return pd.Series(list(map(func, index)), index=index, dtype="float64")


def min_extremum(data: pd.Series) -> float:  # type: ignore
    """Return x coordinate of leftmost minimum."""
    return float(min(data[data == min(data)].index))


def max_extremum(data: pd.Series) -> float:  # type: ignore
    """Return x coordinate of rightmost maximum."""
    return float(max(data[data == max(data)].index))
