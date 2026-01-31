"""Graphical representation of experiments, tools for conducting them."""

# ## Графическое представление экспериментов, инструменты для их проведения

# +
# 1



import io
import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

patient_survival_csv_url = os.environ.get("PATIENT_SURVIVAL_CSV_URL", "")
response = requests.get(patient_survival_csv_url)
patient_survival = pd.read_csv(io.BytesIO(response.content))

print(patient_survival.sample(500).shape)

# +
# 2


cols = [
    "Patient_Age",
    "Patient_Body_Mass_Index",
    "Patient_Smoker",
    "Diagnosed_Condition",
    "Survived_1_year",
]


sampled = pd.concat(
    [
        group[cols].sample(30, random_state=42)
        for _, group in patient_survival.groupby("Treated_with_drugs")
    ],
    ignore_index=True,
)

print(sampled.shape)

# +
# 3


print(1)

# +
# 4


print(3)

# +
# 5


print(3)

# +
# 6


print(2)

# +
# 7


print(1)

# +
# 8


print(1)

# +
# 9


print(1)
