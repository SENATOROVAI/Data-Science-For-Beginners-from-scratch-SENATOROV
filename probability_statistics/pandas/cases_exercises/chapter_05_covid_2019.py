"""COVID 2019."""

# ### Где найти базы данных о коронавирусе COVID-19?
#
# Учёными и исследователями собираются многочисленные базы данных о коронавирусе, его генетической структуре, ходе распространения и научных исследованиях о нём. Значительные объёмы этих данных общедоступны.
#
# Подробности по [ссылке](https://covid19faq.ru/l/ru/article/f3sw02fiup-data)
#
# ### Почему так сложно сделать хорошую математическую модель COVID-19?
#
# В это сложное время пандемии нам всем нужны ответы. Тысячи ученых, исследовательских центров и активистов по всему миру собирают данные и проводят исследования по теме «коронавирус» (COVID-19). Кажется, что уже должны существовать точные ответы. Эти ответы основаны на данных, но проблема в том, что данные повсюду и часто один источник противоречит другому.
#
# Подробности по [ссылке](https://covid19faq.ru/l/ru/article/dwmsq2i0ef-good-mathematical-model-covid-19)
#
# **Почему так сложно построить хороший прогноз по COVID-19? Как понять, сколько продлится карантин?** [Подробнее](https://vc.ru/flood/117032-pochemu-tak-slozhno-postroit-horoshiy-prognoz-po-covid-19-kak-ponyat-skolko-prodlitsya-karantin)
#
# ### Где ведутся и публикуются исследования COVID-19?
#
# Исследования о COVID-19 ведутся в сотнях научных и исследовательских учреждений по всему миру. Здесь собраны ссылки на общедоступные исследования, базы научных публикаций и сообществ учёных.
#
# Подробности по [ссылке](https://covid19faq.ru/l/ru/article/5pqxj6az02-research)
#
# ### Граф знаний COVID-19
#
# Мы создаем граф знаний по COVID-19, который объединяет различные общедоступные наборы данных. Он включает в себя соответствующие публикации, статистику случаев, гены и функции, молекулярные данные и многое другое.
#
# Подробности по [ссылке](https://covidgraph.org)
#

# +
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()

# +
# pylint: disable=line-too-long

# Источник данных: https://github.com/datasets/covid-19

url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
df = pd.read_csv(
    url,
    parse_dates=["Date"],
    index_col="Date",
    usecols=["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"],
)
df.sample(10)
# -

df.info()

df["Country/Region"].unique()

df.plot(alpha=0.5);

# ### Россия

rus = df[df["Country/Region"] == "Russia"]
rus.head()

rus.describe()


# Округление:

# +
def fmt(x_var: float) -> str:
    """Преобразует входное значение в строку с форматированием."""
    return f"{x_var:.2f}"


rus.describe().apply(lambda col: col.apply(fmt))
# -

rus.plot();

rus.loc[pd.Timestamp("2020-09-25") : pd.Timestamp("2020-11-16")].plot()

rus.Confirmed.corr(rus.Recovered)

# Коэффициент корреляции стремится к 1.

# Вычисляем %-ное изменение с помощью метода [pct_change](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pct_change.html) для параметра Confirmed:

data = rus.Confirmed.pct_change()
data

print(data[data.notna()])

data[data.notna()].plot(label="all")
data[data.notna()].rolling(10).mean().plot(label="rolling 10")
plt.legend();

data[data.notna()].plot(label="all")
data[data.notna()].rolling(10).mean().plot(label="rolling 10")
data[data.notna()].expanding().mean().plot(label="expanding")
plt.legend();

rus.index

print(rus.loc[pd.Timestamp("2020-10") : pd.Timestamp("2020-11")][:10])

# ### Передискретизация и преобразование частот

rus.loc[pd.Timestamp("2020-10") : pd.Timestamp("2020-11")].plot()

rus.Confirmed.plot();

# среднее в месяц:
rus.Confirmed.resample("M").mean().plot(label="mean")
rus.Confirmed.plot(label="all")
plt.legend();

# среднее в месяц:
rus.Confirmed.resample("M", kind="period").mean()  # type: ignore[call-arg]

# среднее в месяц:
rus.Confirmed.resample("M", kind="period").mean().plot();  # type: ignore[call-arg]

rus.Confirmed.resample("M", kind="period").mean().pct_change().plot();  # type: ignore[call-arg]

# ### Италия

it = df[df["Country/Region"] == "Italy"]
it.head()

it.plot();

it[it.Deaths <= 1].tail()
