"""Data analysis."""

# pylint: disable=too-many-locals, too-many-branches, line-too-long

# +
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup, Tag
from scipy.stats import chi2_contingency, f_oneway, levene, ttest_ind


def chapter_2() -> None:
    """Analyze happiness scores and GDP data from 2019 dataset."""
    df = pd.read_csv("./2019.csv")

    print(df["Score"].max())
    print(df["Score"].min())
    print(df["Score"].mean())

    mean_by_country = df.groupby("Country or region")["Score"].mean().mean()
    print(mean_by_country)

    print(df["Score"].mode()[0])
    print(df["Score"].std())

    top10 = df.sort_values(by="Score", ascending=False).head(10)
    print(top10["Country or region"].to_list())

    print(df["GDP per capita"].sum())
    print(top10["GDP per capita"].sum())


def chapter_3() -> None:
    """Analyze book ratings and prices, perform statistical tests."""
    df = pd.read_csv("./books_prep.csv")

    print(df["Author"].describe()["top"])

    grp = df.groupby("Price (Above Average)")["User Rating"]
    print(grp.mean().round(2)["Yes"])
    print(grp.mean().round(2)["No"])

    exp = df[df["Price (Above Average)"] == "Yes"]["User Rating"]
    cheap = df[df["Price (Above Average)"] == "No"]["User Rating"]

    lev_result = levene(exp, cheap)
    print(round(lev_result[1], 2))

    ttest_result = ttest_ind(exp, cheap, equal_var=True)
    print(round(ttest_result[1], 2))

    r5 = df[df["User Rating (Round)"] == 5]["Reviews"]
    r4 = df[df["User Rating (Round)"] == 4]["Reviews"]
    r3 = df[df["User Rating (Round)"] == 3]["Reviews"]

    anova_result = f_oneway(r5, r4, r3)
    print(round(anova_result[1], 2))


def chapter_4() -> None:
    """Analyze COVID-19 survey responses about online classes and lifestyle."""
    df = pd.read_csv("./COVID-19 SSR.csv")
    print(df.dtypes.mode()[0])
    df["Rating of Online Class experience"] = df[
        "Rating of Online Class experience"
    ].str.title()
    print(df["Rating of Online Class experience"].head())
    df = pd.read_csv("./COVID-19 Survey Student Responses.csv")
    df["Sleep"] = np.where(
        (df["Time spent on sleep"] > 6.9) & (df["Time spent on sleep"] < 9),
        "normal",
        "not normal",
    )
    print(len(df[df["Sleep"] == "not normal"]))
    df["Time spent on TV"].replace(["No tv", "N", "n", " "], 0, inplace=True)
    df["Time spent on TV"] = pd.to_numeric(df["Time spent on TV"])
    print(df["Time spent on TV"].dtype)
    df["Media"] = np.where(
        (df["Time spent on social media"] < 2), "normal", "not normal"
    )
    contingency_table = pd.crosstab(df["Sleep"], df["Media"])
    chi2, p_value = chi2_contingency(contingency_table)
    print(chi2)

    df["Sleep"] = np.where(df["Time spent on sleep"] > 7, "normal", "not normal")
    contingency_table = pd.crosstab(df["Sleep"], df["Media"])
    chi2, p_value = chi2_contingency(contingency_table)
    print(p_value)

    df["Health issue during lockdown"].replace(["YES", "NO"], [1, 0], inplace=True)
    print(df["Health issue during lockdown"].value_counts())

    print(len(df[df["Stress busters"].str.contains("book")]))

    most_popular_platform = df["Preferred social media platform"].mode()[0]

    filtered_df = df[df["Preferred social media platform"] == most_popular_platform]

    average_time = round(filtered_df["Time spent on social media"].mean(), 2)

    print(average_time)

    most_spend_time_platform = (
        df.groupby(by="Preferred social media platform")["Time spent on social media"]
        .mean()
        .sort_values(ascending=False)
    )

    print(most_spend_time_platform.index[0], most_spend_time_platform.values[0])


# chapter_4()


def chapter_5_1() -> None:
    """Create histogram of Pokemon Attack stats."""
    data = pd.read_csv("PokemonData.csv")

    plt.figure()
    plt.hist(data["Attack"])

    plt.savefig("result.png")


def chapter_5_2() -> None:
    """Create overlapping histograms of Attack and SpAtk stats."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    plt.hist(data["Attack"])
    plt.hist(data["SpAtk"])

    plt.savefig("result.png")


def chapter_5_3() -> None:
    """Create labeled histograms with legend and axis labels."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    plt.hist(data["Attack"], alpha=0.5, label="Attack")
    plt.hist(data["SpAtk"], alpha=0.5, label="SpAtk")
    plt.legend()
    plt.xlabel("Attack")
    plt.ylabel("Power")

    plt.savefig("result.png")


def chapter_5_4() -> None:
    """Create histograms with Russian labels."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    plt.hist(data["Attack"], alpha=0.5, label="Обычная атака")
    plt.hist(data["SpAtk"], alpha=0.5, label="Специальная атака")
    plt.legend()

    plt.savefig("result.png")


def chapter_5_5() -> None:
    """Create histograms with complete Russian labeling."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    plt.hist(data["Attack"], alpha=0.5, label="Обычная атака")
    plt.hist(data["SpAtk"], alpha=0.5, label="Специальная атака")
    plt.legend()
    plt.xlabel("Мощность атаки")
    plt.ylabel("Количество покемонов")

    plt.savefig("result.png")


def chapter_5_6() -> None:
    """Create scatter plot of Attack vs Defense."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    plt.scatter(data["Attack"], data["Defense"])
    plt.savefig("result.png")


def chapter_5_7() -> None:
    """Create transparent scatter plot of Attack vs Defense."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    plt.scatter(data["Attack"], data["Defense"], alpha=0.3)
    plt.savefig("result.png")


def chapter_5_8() -> None:
    """Create bar plot of Pokemon types distribution."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    data["Type1"].value_counts().plot(kind="bar")
    plt.savefig("result.png")


def chapter_5_9() -> None:
    """Create grouped bar plot comparing legendary vs normal Pokemon types."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    data.groupby("Legendary")["Type1"].value_counts().unstack(0).plot(kind="bar")
    plt.savefig("result.png")


def chapter_5_10() -> None:
    """Create fully labeled grouped bar plot comparing Pokemon types."""
    data = pd.read_csv("PokemonData.csv")
    plt.figure()
    data.groupby("Legendary")["Type1"].value_counts().unstack(0).plot(kind="bar")
    plt.xlabel("Тип покемонов")
    plt.title("Легендарные покемоны по типам в сравнении с обычными")
    plt.ylabel("Количество")
    plt.savefig("result.png")


chapter_5_1()
chapter_5_2()
chapter_5_3()
chapter_5_4()
chapter_5_5()
chapter_5_6()
chapter_5_7()
chapter_5_8()
chapter_5_9()
chapter_5_10()


def chapter_6() -> None:
    """Analyze World Values Survey data."""
    df = pd.read_csv("WVSW_6_2010_2014.csv")

    print(df.dtypes)
    print(4)
    print("V119", "V120", "V121", "V122", "V123")
    print("V108", "V109", "V117", "V118")
    print("V117")


# +
def chapter_7() -> None:
    """Parse and extract information from Kinopoisk HTML page."""
    with open("kinopoisk.html", encoding="utf-8") as file:
        html = file.read()
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and isinstance(soup.title.text, str):
        title_text = soup.title.text
        print(title_text)
        print(title_text.strip().split("—")[0].strip())

    all_links = soup.find_all("a")

    directors = []
    for link in all_links:
        if isinstance(link, Tag):
            href = link.get("href", "")
            if href and "/name/" in href:
                directors.append(link.text.strip())

    if directors:
        print(directors[0])

    description_tag = soup.find("meta", attrs={"name": "description"})

    if description_tag and isinstance(description_tag, Tag):
        description = description_tag.get("content")
        if isinstance(description, str):
            description = description.strip()
            print(description)

            capitalized_words = re.findall(r"[А-ЯЁ][а-яё]+", description)

            for word in capitalized_words:
                print(word)

    actors = soup.find_all(
        "li",
        class_="styles_root__vKDSE styles_rootInLight__EFZzH",
    )

    print(len(actors))

    for actor in actors:
        if isinstance(actor.text, str):
            print(actor.text)

    a_tags = soup.find_all("a")

    print(len(a_tags))

    for tag in a_tags:
        if isinstance(tag, Tag):
            href = tag.get("href")
            if isinstance(href, str):
                print(href)


chapter_7()


def chapter_8() -> None:
    """Process and clean Disney titles dataset."""
    data = pd.read_csv("disney_title.csv")
    data.info()
    data["Date"] = pd.to_datetime(data["Date"])
    print(data["Date"].dtype)

    filtered = data[(data["Date"] >= "2020-01-01") & (data["Date"] < "2021-01-01")]

    print(filtered["title"].head(10))

    removed_data = data.drop(labels="release_year", axis=1)
    print(list(removed_data))

    renamed_data = data.copy()
    renamed_data.columns = pd.Index([cl.capitalize() for cl in renamed_data.columns])
    print(list(renamed_data.columns))

    data["listed_in1"] = data["listed_in"].str.replace("&", ",")
    print(data["listed_in1"].tail())

    missing_values_count = data.isnull().sum()
    print(missing_values_count)

    data_cleaned = data.dropna()

    print(data_cleaned.isnull().sum())

    missing_percentage = (data.isnull().sum() / len(data)) * 100

    missing_percentage_rounded = missing_percentage.round(2)

    print(missing_percentage_rounded)

    data["country"] = data["country"].fillna("Country not specified")

    print(data["country"].head())


chapter_8()


# +
def chapter_9() -> None:
    """Process and analyze patient survival data."""
    data = pd.read_csv("Patient Survival.csv")
    print(data.sample(500).shape)
    cols = [
        "Patient_Age",
        "Patient_Body_Mass_Index",
        "Patient_Smoker",
        "Diagnosed_Condition",
        "Survived_1_year",
    ]
    sampled = data.groupby("Treated_with_drugs", group_keys=False).apply(
        lambda x: x[cols].sample(30, random_state=42)
    )
    print(sampled.shape)
    print(1)
    print(3)
    print(3)
    print(2)
    print(1)
    print(1)
    print(1)


chapter_9()
