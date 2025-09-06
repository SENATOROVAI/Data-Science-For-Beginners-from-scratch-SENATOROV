"""Data analysis."""

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# +
import math
import re
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup, Tag
from scipy.stats import chi2_contingency, f_oneway, levene, ttest_ind
from itertools import combinations
from math import comb


# Statistics


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

# +
# Linear algebra and Mathematical Analysis


def chapter_3_2_1() -> None:
    """Calculate N/(N+1) formula."""
    N = int(input().strip())
    result = N / (N + 1)
    print(f"{result:.6f}")


def chapter_3_2_2() -> None:
    """Check function continuity at point."""
    expr = sys.stdin.readline().strip()
    x0 = float(sys.stdin.readline().strip())
    delta = float(sys.stdin.readline().strip())

    env = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
    env.update(
        {
            "abs": abs,
            "max": max,
            "min": min,
            "round": round,
            "pow": pow,
            "int": int,
            "float": float,
            "math": math,
        }
    )

    def f(x):
        return eval(expr, {"__builtins__": {}}, {**env, "x": x})

    eps = 5 * delta
    f_x0 = f(x0)
    left = abs(f(x0 - delta) - f_x0)
    right = abs(f(x0 + delta) - f_x0)

    print("CONTINUOUS" if left < eps and right < eps else "DISCONTINUOUS")


def chapter_3_2_3() -> None:
    """Check if function satisfies Lipschitz condition."""
    expr = sys.stdin.readline().strip()
    a_str, b_str = sys.stdin.readline().split()
    L_str = sys.stdin.readline().strip()

    a = float(a_str)
    b = float(b_str)

    def safe_eval(s):
        return eval(s, {"__builtins__": {}}, {"e": math.e})

    L = safe_eval(L_str) if not L_str.replace(".", "", 1).isdigit() else float(L_str)

    code = compile(expr, "<expr>", "eval")

    def f(x):
        return eval(code, {"__builtins__": {}}, {"x": x, "e": math.e})

    epsilon = 1e-6

    N = 20000
    if b - a <= 0:
        print("LIPSCHITZ")
        sys.exit(0)
    N = max(2, N)

    h = (b - a) / N

    x_left = a
    f_left = f(x_left)

    ok = True

    for i in range(N):
        x_right = a + (i + 1) * h
        x_mid = (x_left + x_right) / 2.0

        f_mid = f(x_mid)
        f_right = f(x_right)

        if (
            abs(f_right - f_left) > L * h + epsilon
            or abs(f_mid - f_left) > L * (h * 0.5) + epsilon
            or abs(f_right - f_mid) > L * (h * 0.5) + epsilon
        ):
            ok = False
            break

        x_left = x_right
        f_left = f_right

    print("LIPSCHITZ" if ok else "NOT LIPSCHITZ")


def chapter_3_3_1() -> None:
    """Find critical points of cubic function."""
    EPS = 1e-9

    def in_interval(x, p, q):
        return (p - EPS) <= x <= (q + EPS)

    def fmt(x):
        if abs(x) < 0.5e-5:
            x = 0.0
        return f"{x:.5f}"

    data = sys.stdin.read().strip().split()
    if len(data) < 6:
        return
    a, b, c, d = map(float, data[:4])
    p, q = map(float, data[4:6])

    critical = []

    if abs(a) > EPS:
        disc = b * b - 3 * a * c
        if disc >= -EPS:
            if disc < 0:
                disc = 0.0
            sqrt_disc = math.sqrt(max(0.0, disc))
            if sqrt_disc < EPS:
                x = (-b) / (3 * a)
                if in_interval(x, p, q):
                    fpp = 6 * a * x + 2 * b
                    if abs(fpp) <= 1e-9:
                        kind = "Saddle point"
                    elif fpp < 0:
                        kind = "Local maximum"
                    else:
                        kind = "Local minimum"
                    fx = a * x * x * x + b * x * x + c * x + d
                    critical.append((x, kind, fx))
            else:
                x1 = (-b - sqrt_disc) / (3 * a)
                x2 = (-b + sqrt_disc) / (3 * a)
                for x in sorted([x1, x2]):
                    if in_interval(x, p, q):
                        fpp = 6 * a * x + 2 * b
                        if abs(fpp) <= 1e-9:
                            kind = "Saddle point"
                        elif fpp < 0:
                            kind = "Local maximum"
                        else:
                            kind = "Local minimum"
                        fx = a * x * x * x + b * x * x + c * x + d
                        critical.append((x, kind, fx))

    elif abs(b) > EPS:
        x = -c / (2 * b)
        if in_interval(x, p, q):
            fpp = 2 * b
            kind = "Local minimum" if fpp > 0 else "Local maximum"
            fx = a * x * x * x + b * x * x + c * x + d
            critical.append((x, kind, fx))
    else:
        pass

    critical.sort(key=lambda t: t[0])
    if not critical:
        print("No critical points found.")
    else:
        for x, kind, fx in critical:
            print(f"{kind} at x = {fmt(x)}")
            print(f"f(x) = {fmt(fx)}")


def chapter_3_3_2() -> None:
    """Find quadratic equation root using Newton's method."""
    MAX_ITERS = 1000
    DERIV_EPS = 1e-12

    def fmt6(x):
        if abs(x) < 0.5e-6:
            x = 0.0
        return f"{x:.6f}"

    data = sys.stdin.read().strip().split()
    if len(data) < 5:
        print("Solution not found")
        return

    a, b, c = map(float, data[:3])
    x = float(data[3])
    eps = float(data[4])

    def f(x):
        return a * x * x + b * x + c

    def fp(x):
        return 2 * a * x + b

    fx = f(x)
    if abs(fx) < eps:
        print(f"Root found: x = {fmt6(x)}")
        print("Number of iterations: 0")
        return

    iters = 0
    while iters < MAX_ITERS:
        fpx = fp(x)
        if abs(fpx) < DERIV_EPS:
            print("Solution not found")
            return
        x = x - fx / fpx
        iters += 1
        fx = f(x)
        if abs(fx) < eps:
            print(f"Root found: x = {fmt6(x)}")
            print(f"Number of iterations: {iters}")
            return

    print("Solution not found")
    
    
def chapter_4_2_1() -> None:
    """Calculate linear combination of vectors."""
    k = int(input().strip()) 
    lambdas = list(map(float, input().split()))

    vectors = [list(map(float, input().split())) for _ in range(k)]
    n = len(vectors[0])

    result = [0.0] * n

    for i in range(k):
        for j in range(n):
            result[j] += lambdas[i] * vectors[i][j]

    print(" ".join(f"{x:.2f}" for x in result))
    
def chapter_4_2_2() -> None:
    """Check if vectors are orthogonal."""
    k = int(input().strip())
    u = list(map(float, input().split()))
    v = list(map(float, input().split()))

    dot = sum(ui * vi for ui, vi in zip(u, v))

    if abs(dot) < 1e-9: 
        print("ORTHOGONAL")     
    else:
        print("NON-ORTHOGONAL")

def chapter_4_2_3() -> None:
    """Find linear combination coefficients."""
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v3 = list(map(int, input().split()))

    A = np.array([v1, v2]).T 
    b = np.array(v3)

    try:
        sol = np.linalg.solve(A, b) 
    except np.linalg.LinAlgError:
   
        M = np.column_stack([v1, v2, v3])
        if np.linalg.matrix_rank(M) == np.linalg.matrix_rank(A):
            if any(v1):
                if v1[0] != 0 and v3[0] % v1[0] == 0:
                    k = v3[0] // v1[0]
                    if np.all(np.array(v1) * k == b):
                        print(k, 0)
                        return
                if v1[1] != 0 and v3[1] % v1[1] == 0:
                    k = v3[1] // v1[1]
                    if np.all(np.array(v1) * k == b):
                        print(k, 0)
                        return
            if any(v2):
                if v2[0] != 0 and v3[0] % v2[0] == 0:
                    k = v3[0] // v2[0]
                    if np.all(np.array(v2) * k == b):
                        print(0, k)
                        return
                if v2[1] != 0 and v3[1] % v2[1] == 0:
                    k = v3[1] // v2[1]
                    if np.all(np.array(v2) * k == b):
                        print(0, k)
                        return
        print("NO_SOLUTION")
        return

    lam1, lam2 = sol
    if np.allclose([round(lam1), round(lam2)], sol) and \
       abs(round(lam1)) <= 10**10 and abs(round(lam2)) <= 10**10:
        print(int(round(lam1)), int(round(lam2)))
    else:
        print("NO_SOLUTION")


def chapter_4_2_4() -> None:
    """Calculate angle between vectors."""
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    v1 = data[1:1+n]
    v2 = data[1+n:1+2*n]

    dot = sum(a*b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a*a for a in v1))
    norm2 = math.sqrt(sum(b*b for b in v2))


    cosang = dot / (norm1 * norm2)
    cosang = max(-1.0, min(1.0, cosang))

    angle_deg = math.degrees(math.acos(cosang))
    print(int(angle_deg))

def chapter_4_2_5() -> None:
    """Check linear independence of vectors."""
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    m, n = next(it), next(it)

    A = np.fromiter(it, dtype=float, count=m*n).reshape(m, n)

    if m > n:
        print("LINEARLY_DEPENDENT")
    else:
        r = np.linalg.matrix_rank(A)
        print("LINEARLY_INDEPENDENT" if r == m else "LINEARLY_DEPENDENT")
        
def chapter_4_3_1() -> None:
    """Determine matrix type."""
    n = int(input())
    A = np.array([list(map(float, input().split())) for _ in range(n)])

    if np.allclose(A, np.diag(np.diag(A))):
        print("DIAGONAL")
        return

    if np.allclose(np.tril(A, -1), 0):
        print("UPPER_TRIANGULAR")
        return

    if np.allclose(np.triu(A, 1), 0):
        print("LOWER_TRIANGULAR")
        return

    print("OTHER")

def chapter_4_3_2() -> None:
    """Multiply two matrices."""
    def read_matrix(rows):
        return [list(map(int, input().split())) for _ in range(rows)]
    m, n = map(int, input().split())
    A = read_matrix(m)

    h, k = map(int, input().split())
    B = read_matrix(h)

    if n != h:
        print("NOT_DEFINED")
        return

    C = [[0] * k for _ in range(m)]
    for i in range(m):
        for j in range(k):
            s = 0
            for t in range(n):
                s += A[i][t] * B[t][j]
            C[i][j] = s

    for row in C:
        print(" ".join(map(str, row)))

def chapter_4_3_3() -> None:    
    """Find matrix nilpotency degree."""
    def read_matrix():
        data = sys.stdin.read().strip().split()
        n = int(data[0])
        vals = list(map(int, data[1:]))
        A = [vals[i*n:(i+1)*n] for i in range(n)]
        return n, A

    def is_zero(M):
        return all(x == 0 for row in M for x in row)

    def matmul(A, B):
        n = len(A)
        C = [[0]*n for _ in range(n)]
        for i in range(n):
            Ai = A[i]
            for k in range(n):
                aik = Ai[k]
                if aik == 0:
                    continue
                Bk = B[k]
                for j in range(n):
                    C[i][j] += aik * Bk[j]
        return C
    n, A = read_matrix()
    P = A
    for k in range(1, 101):
        if is_zero(P):
            print(k)
            return
        P = matmul(P, A)

def chapter_4_3_4() -> None:
    """Transpose matrix."""
    m, n = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(m)]

    B = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]

    for row in B:
        print(*row)

def chapter_4_3_5() -> None:
    """Standardize matrix columns."""
    m, n = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(m)]

    B = [[0] * n for _ in range(m)]

    for j in range(n): 
        col = [A[i][j] for i in range(m)]
        mean = sum(col) / m
        variance = sum((x - mean) ** 2 for x in col) / m
        std = math.sqrt(variance)

        for i in range(m):
            if std == 0:  
                B[i][j] = 0
            else:
                B[i][j] = int((A[i][j] - mean) / std)

    for row in B:
        print(*row)
        
def chapter_5_2_1() -> None:
    """Calculate binomial probability."""
    data = sys.stdin.readlines()
    n_val, k_val = map(int, data[0].split())
    p_val = float(data[1].strip())

    def binomial_probability(n, k, p):
        return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * \
            (p ** k) * ((1 - p) ** (n - k))

    result = 0.0
    for k in range(k_val, n_val + 1):
        result += binomial_probability(n_val, k, p_val)

    print(result)


def chapter_5_2_2() -> None:
    """Calculate probability for given range."""
    C, D = map(float, sys.stdin.read().split())

    if D <= 0:
        result = 0.0
    elif D >= 2 * C:
        result = 1.0
    elif D <= C:
        result = (D ** 2) / (2 * C * C)
    else:
        result = 1 - ((2 * C - D) ** 2) / (2 * C * C)

    print(result)
    
def chapter_5_2_3() -> None:
    """Calculate color probabilities."""
    R_val, G_val, B_val = map(int, input().split(" "))
    values = list(combinations(["R"] * R_val + ["G"] * G_val + ["B"] * B_val, 3))
    green_one_val_count = 0
    one_color_val_count = 0

    for val in values:
        if "G" in val:
            green_one_val_count += 1
        if len(set(val)) == 1:
            one_color_val_count += 1

    print(green_one_val_count / len(values), one_color_val_count / len(values))

def chapter_5_2_4() -> None:
    """Check coin fairness."""
    num_flips, fairness_threshold = input().split()
    num_flips = int(num_flips)
    fairness_threshold = float(fairness_threshold)

    flip_results = list(map(int, input().split()))
    num_heads = sum(flip_results)

    binomial_probabilities = [comb(num_flips, k) * (0.5 ** num_flips) for k in range(num_flips + 1)]

    best_margin = 0
    for margin in range(num_flips // 2 + 1):
        probability_within_margin = sum(binomial_probabilities[margin:num_flips - margin + 1])
        if probability_within_margin >= fairness_threshold:
            best_margin = margin

    min_heads = best_margin
    max_heads = num_flips - best_margin

    print(min_heads, max_heads)
    if min_heads <= num_heads <= max_heads:
        print("fair")
    else:
        print("biased")
        
        
def chapter_5_3_1() -> None:
    """Calculate conditional probability."""
    p, s1, f1, s2, f2 = map(float, input().split())
    test1, test2 = map(int, input().split())
    if test1 == 1:
        prob_test1_b = s1
        prob_test1_n = f1
    else:
        prob_test1_b = 1 - s1
        prob_test1_n = 1 - f1

    if test2 == 1:
        prob_test2_b = s2
        prob_test2_n = f2
    else:
        prob_test2_b = 1 - s2
        prob_test2_n = 1 - f2

    prob_test_given_sick = prob_test1_b * prob_test2_b

    prob_test_given_healthy = prob_test1_n * prob_test2_n

    prob_sick = p

    prob_healthy = 1 - p

    prob_test = prob_test_given_sick * prob_sick + prob_test_given_healthy * prob_healthy

    prob_b_given_test = (prob_test_given_sick * prob_sick) / prob_test

    print(f"{prob_b_given_test:.5f}")


def chapter_5_3_2() -> None:
    """Check event independence."""
    M = int(input())
    experiments = [tuple(map(int, input().split())) for _ in range(M)]

    count_A = count_B = count_C = 0
    count_AB = count_AC = count_BC = 0
    count_ABC = 0

    for xA, xB, xC in experiments:
        if xA == 1:
            count_A += 1
        if xB == 1:
            count_B += 1
        if xC == 1:
            count_C += 1
        if xA == 1 and xB == 1:
            count_AB += 1
        if xA == 1 and xC == 1:
            count_AC += 1
        if xB == 1 and xC == 1:
            count_BC += 1
        if xA == 1 and xB == 1 and xC == 1:
            count_ABC += 1

    P_A = count_A / M
    P_B = count_B / M
    P_C = count_C / M
    P_AB = count_AB / M
    P_AC = count_AC / M
    P_BC = count_BC / M
    P_ABC = count_ABC / M

    is_AB_independent = abs(P_AB - P_A * P_B) < 1e-6
    is_AC_independent = abs(P_AC - P_A * P_C) < 1e-6
    is_BC_independent = abs(P_BC - P_B * P_C) < 1e-6

    is_ABC_independent = abs(P_ABC - P_A * P_B * P_C) < 1e-6

    if is_AB_independent and is_AC_independent and is_BC_independent:
        if is_ABC_independent:
            print("ALL_INDEPENDENT")
        else:
            print("PAIRWISE_ONLY")
    else:
        print("NOT_INDEPENDENT")
        
        
def chapter_5_3_3() -> None:
    """Classify emails using Naive Bayes."""
    M, N, K = map(int, input().split())
    
    training_data = []
    for _ in range(M):
        training_data.append(list(map(int, input().split())))
    
    test_data = []
    for _ in range(N):
        test_data.append(list(map(int, input().split())))
    
    
    spam_count = sum(1 for email in training_data if email[0] == 1)
    non_spam_count = M - spam_count
    
    p_spam = spam_count / M
    p_non_spam = non_spam_count / M
    
    p_feature_given_spam = []
    for j in range(1, K + 1):
        count_feature_in_spam = sum(1 for email in training_data if email[0] == 1 and email[j] == 1)
        p_feature_given_spam.append(count_feature_in_spam / spam_count if spam_count > 0 else 0)
    
    p_feature_given_non_spam = []
    for j in range(1, K + 1):
        count_feature_in_non_spam = sum(1 for email in training_data if email[0] == 0 and email[j] == 1)
        p_feature_given_non_spam.append(count_feature_in_non_spam / non_spam_count if non_spam_count > 0 else 0)
    
    results = []
    
    for email in test_data:
        p_spam_given_features = p_spam
        for j in range(K):
            if email[j] == 1:
                p_spam_given_features *= p_feature_given_spam[j]
            else:
                p_spam_given_features *= (1 - p_feature_given_spam[j])
        
        p_non_spam_given_features = p_non_spam
        for j in range(K):
            if email[j] == 1:
                p_non_spam_given_features *= p_feature_given_non_spam[j]
            else:
                p_non_spam_given_features *= (1 - p_feature_given_non_spam[j])
        
        if p_spam_given_features == 0 and p_non_spam_given_features == 0:
            results.append(-1) 
        elif p_spam_given_features > p_non_spam_given_features:
            results.append(1)
        elif p_spam_given_features < p_non_spam_given_features:
            results.append(0)
        else:
            results.append(-1) 

    print(' '.join(map(str, results)))
