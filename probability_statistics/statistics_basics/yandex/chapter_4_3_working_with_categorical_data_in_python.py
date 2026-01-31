"""Working with categorical data in Python."""

# ## Работа с категориальными данными в Python

# +
# 1


import io
import os

import pandas as pd
import requests
from dotenv import load_dotenv
from scipy.stats import chi2_contingency

load_dotenv()

covid_19_csv_url = os.environ.get("COVID_19_CSV_URL", "")
response = requests.get(covid_19_csv_url)
pandemic_impact = pd.read_csv(io.BytesIO(response.content))

print(pandemic_impact.dtypes.mode()[0])

# +
# 2


pandemic_impact["Rating of Online Class experience"] = pandemic_impact[
    "Rating of Online Class experience"
].str.title()

print(pandemic_impact["Rating of Online Class experience"].head())

# +
# 3


load_dotenv()

student_responses_csv_url = os.environ.get("STUDENT_RESPONSES_CSV_URL", "")
response = requests.get(student_responses_csv_url)
student_responses = pd.read_csv(io.BytesIO(response.content))


sleep_status = []

for hours in student_responses["Time spent on sleep"]:
    if 6.9 < hours < 9:
        sleep_status.append("normal")
    else:
        sleep_status.append("not normal")

student_responses["Sleep"] = sleep_status

not_normal_sleep = student_responses[student_responses["Sleep"] == "not normal"]

print(len(not_normal_sleep))

# +
# 4


student_responses["Time spent on TV"] = pd.to_numeric(
    student_responses["Time spent on TV"], errors="coerce"
).fillna(0)

print(student_responses["Time spent on TV"].dtype)

# +
# 5


media_status = []
for hours in student_responses["Time spent on social media"]:
    if hours < 2:
        media_status.append("normal")
    else:
        media_status.append("not normal")
student_responses["Media"] = media_status

cross_tab = pd.crosstab(student_responses["Sleep"], student_responses["Media"])

chi2, p_var, dof, expected = chi2_contingency(cross_tab)

print(chi2)

# +
# 6


student_responses["Sleep"] = [
    "normal" if x > 7 else "not normal"
    for x in student_responses["Time spent on sleep"]
]

student_responses["Media"] = [
    "normal" if x < 2 else "not normal"
    for x in student_responses["Time spent on social media"]
]

contingency_table = pd.crosstab(student_responses["Sleep"], student_responses["Media"])

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print(chi2)

# +
# 7


student_responses["Health issue during lockdown"] = student_responses[
    "Health issue during lockdown"
].map({"YES": 1, "NO": 0})

print(student_responses["Health issue during lockdown"].value_counts())

# +
# 8


stress_busters_col = student_responses["Stress busters"]

mask = stress_busters_col.str.contains("book")

filtered_df = student_responses[mask]

count = len(filtered_df)

print(count)

# +
# 9


most_popular_platform = student_responses["Prefered social media platform"].mode()[0]

filtered_df = student_responses[
    student_responses["Prefered social media platform"] == most_popular_platform
]

average_time = filtered_df["Time spent on social media"].mean()

average_time = round(average_time, 2)

print(average_time)

# +
# 10


grouped = student_responses.groupby(by="Prefered social media platform")[
    "Time spent on social media"
]

mean_time = grouped.mean()

sorted_mean_time = mean_time.sort_values(ascending=False)

most_spend_time_platform = sorted_mean_time

top_platform = most_spend_time_platform.index[0]
top_time = most_spend_time_platform.values[0]

print(top_platform, top_time)
