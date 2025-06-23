"""Data analysis."""

# pylint: disable=line-too-long
# codespell:disable

# +
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, f_oneway, levene, ttest_ind


def chapter_2() -> None:
    """Return chapter_2 tasks."""
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
    """Return chapter_3 tasks."""
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
    """Return chapter_4 tasks."""
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
    df["Sleep"].replace(["normal", "not normal"], [1, 0], inplace=True)
    df["Media"].replace(["normal", "not normal"], [1, 0], inplace=True)
    contingency_table = pd.crosstab(df["Sleep"], df["Media"])
    chi2, p_value = chi2_contingency(contingency_table)
    print(chi2)

    df["Sleep"] = np.where(df["Time spent on sleep"] > 7, "normal", "not normal")
    df["Sleep"].replace(["normal", "not normal"], [1, 0], inplace=True)
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


chapter_4()
