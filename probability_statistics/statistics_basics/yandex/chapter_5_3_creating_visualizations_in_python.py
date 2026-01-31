"""Creating visualizations in Python."""

# ## Создание визуализаций в Python

# +
# 1


import io
import os

import matplotlib.pyplot as plt
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

pokemon_data_csv_url = os.environ.get("POKEMON_DATA_CSV_URL", "")
response = requests.get(pokemon_data_csv_url)
pokemon_data = pd.read_csv(io.BytesIO(response.content))

plt.figure()
plt.hist(pokemon_data["Attack"])

plt.savefig("result.png")

# +
# 2


plt.figure()
plt.hist(pokemon_data["Attack"])
plt.hist(pokemon_data["SpAtk"])

plt.savefig("result.png")

# +
# 3


plt.figure()
plt.hist(pokemon_data["Attack"], alpha=0.5)
plt.hist(pokemon_data["SpAtk"], alpha=0.5)

plt.savefig("result.png")

# +
# 4


plt.figure()
plt.hist(pokemon_data["Attack"], label="Обычная атака")
plt.hist(pokemon_data["SpAtk"], label="Специальная атака")
plt.legend()

plt.savefig("result.png")

# +
# 5


plt.figure()
plt.hist(pokemon_data["Attack"], label="Обычная атака")
plt.hist(pokemon_data["SpAtk"], label="Специальная атака")
plt.legend()

plt.xlabel("Мощность атаки")
plt.ylabel("Количество покемонов")

plt.savefig("result.png")

# +
# 6


plt.figure()
plt.scatter(pokemon_data["Attack"], pokemon_data["Defense"])

plt.savefig("result.png")

# +
# 7


plt.figure()
plt.scatter(pokemon_data["Attack"], pokemon_data["Defense"], alpha=0.3)

plt.savefig("result.png")

# +
# 8


plt.figure()
pokemon_data["Type1"].value_counts().plot(kind="bar")

plt.savefig("result.png")

# +
# 9
# fmt: off

plt.figure()

(
    pokemon_data.groupby("Legendary")["Type1"]
    .value_counts()
    .unstack(0)
    .plot(kind="bar")
)

plt.savefig("result.png")
# fmt: on

# +
# 10
# fmt: off

plt.figure()

(
    pokemon_data.groupby("Legendary")["Type1"]
    .value_counts()
    .unstack(0)
    .plot(kind="bar")
)

plt.title("Легендарные покемоны по типам в сравнении с обычными")
plt.xlabel("Тип покемонов")
plt.ylabel("Количество")

plt.savefig("result.png")
# fmt: on
