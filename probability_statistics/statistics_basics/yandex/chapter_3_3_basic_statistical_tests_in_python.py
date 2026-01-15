"""Basic statistical tests in Python."""

# ## Базовые статистические тесты в Python

# +
# 1


import io
import os

import pandas as pd
import requests
from dotenv import load_dotenv
from scipy.stats import f_oneway, levene, ttest_ind

load_dotenv()

popular_books_csv_url = os.environ.get("POPULAR_BOOKS_CSV_URL", "")
response = requests.get(popular_books_csv_url)
popular_books = pd.read_csv(io.BytesIO(response.content))

popular_author = popular_books["Author"].describe()["top"]
print(popular_author)

# +
# 2
# fmt: off

mean_rating_expensive = (
    popular_books[popular_books["Price (Above Average)"] == "Yes"]
    ["User Rating"]
    .mean()
)

print(round(mean_rating_expensive, 2))
# fmt: on

# +
# 3
# fmt: off

mean_rating_cheap = (
    popular_books[popular_books["Price (Above Average)"] == "No"]
    ["User Rating"]
    .mean()
)

print(round(mean_rating_cheap, 2))
# fmt: on

# +
# 4
# fmt: off


cheap = (
    popular_books[popular_books["Price (Above Average)"] == "No"]
    ["User Rating"]
)
expensive = (
    popular_books[popular_books["Price (Above Average)"] == "Yes"]
    ["User Rating"]
)

p_value = levene(cheap, expensive).pvalue

print(round(p_value, 2))
# fmt: on

# +
# 5
# fmt: off


cheap = (
    popular_books[popular_books["Price (Above Average)"] == "No"]
    ["User Rating"]
)
expensive = (
    popular_books[popular_books["Price (Above Average)"] == "Yes"]
    ["User Rating"]
)

p_value = ttest_ind(cheap, expensive).pvalue

print(round(p_value, 2))
# fmt: on

# +
# 6


groups = [
    popular_books[popular_books["User Rating (Round)"] == val]["Reviews"]
    for val in popular_books["User Rating (Round)"].unique()
]

p_value = f_oneway(*groups).pvalue

print(round(p_value, 2))
