"""Variables in programming."""

# ## Переменные в программировании

# +
# 1


import io
import os

import pandas as pd
import requests

from dotenv import load_dotenv


load_dotenv()

_2019_csv_url = os.environ.get("2019_CSV_URL", "")
response = requests.get(_2019_csv_url)
hapiness_report = pd.read_csv(io.BytesIO(response.content))

max_score = hapiness_report["Score"].max()
min_score = hapiness_report["Score"].min()

print(max_score)
print(min_score)

# +
# 2


mean_score = hapiness_report["Score"].mean()

print(round(mean_score, 3))

# +
# 3


median_score = hapiness_report["Score"].median()

print(round(median_score, 3))

# +
# 4


std_score_1 = hapiness_report["Score"].mode()[0]

print(std_score_1)

# +
# 5


std_score_2 = hapiness_report["Score"].std()  # type: float

print(round(std_score_2, 3))

# +
# 6
# fmt: off


top10 = (
    hapiness_report
    .sort_values(by="Score", ascending=False)
    ["Country or region"]
    .head(10)
    .tolist()
)

print(top10)
# fmt: on

# +
# 7


gdp_sum = hapiness_report["GDP per capita"].sum()

print(round(gdp_sum, 3))

# +
# 8


gdp_sum_top10 = hapiness_report["GDP per capita"].head(10).sum()

print(round(gdp_sum_top10, 3))
