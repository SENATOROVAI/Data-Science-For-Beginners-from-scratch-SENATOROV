"""Bringing data to the target form."""

# ## Приведение данных к целевому виду

# +
# 1


import io
import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

disney_csv_url = os.environ.get("DISNEY_CSV_URL", "")
response = requests.get(disney_csv_url)
disney_production = pd.read_csv(io.BytesIO(response.content))
disney_production.info()

# +
# 2


disney_production["Date"] = pd.to_datetime(
    disney_production["Date"], 
    errors="coerce"
)
print(disney_production["Date"].dtype)

# +
# 3


filtered = disney_production.query("'2020-01-01' <= Date < '2021-01-01'")
print(filtered["title"].head(10))

# +
# 4


print(list(disney_production.drop(columns=["release_year"])))

# +
# 5


renamed_data = disney_production.copy()
renamed_data.columns = pd.Index(
    [col.capitalize() for col in renamed_data.columns]
)
print(list(renamed_data.columns))

# +
# 6


disney_production["listed_in1"] = (
    disney_production["listed_in"].str.replace("&", ",")
)
print(disney_production["listed_in1"].tail())

# +
# 7


omitted_values_count = disney_production.isnull().sum()
print(omitted_values_count) 

# +
# 8


data_cleaned = disney_production.dropna()
print(data_cleaned.isnull().sum())

# +
# 9


omitted_percentage = (
    disney_production.isnull().sum() / len(disney_production)
) * 100
omitted_percentage_rounded = omitted_percentage.round(2)
print(omitted_percentage_rounded)

# +
# 10


disney_production["country"] = (
    disney_production["country"].fillna("Country not specified")
)
print(disney_production["country"].head())
