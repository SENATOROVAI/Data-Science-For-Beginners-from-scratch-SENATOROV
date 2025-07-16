"""Confidence level."""

# +
# Доверительный интервал (ДИ) — это диапазон значений, содержащий истинное
# значение того, что мы пытаемся измерить, например, средний рост учащихся или
# средний доход населения

# +
# Z -тест — это тип проверки гипотезы,
# который сравнивает среднее значение выборки со средним значением генеральной
# совокупности и вычисляет Z-счет и сообщает нам, насколько среднее значение
# выборки отличается от среднего значения генеральной совокупности,
# рассматривая, насколько данные обычно варьируются . Это особенно полезно,
# когда размер выборки большой >30. Этот Z-счет также известен как формула
# Z-статистики

# +
# Мы используем t-тест, чтобы проверить, есть ли существенная разница в
# средних результатах тестов между ними.

# +
# Уровень уверенности говорит нам, насколько мы уверены, что истинное значение
# находится в пределах вычисленного диапазона. Если нам придется повторять
# процесс выборки много раз, мы ожидаем, что определенный процент этих
# интервалов будет включать истинное значение.
# 1-alpha - уровень значисмости(confidence level)
# alpha dy default = 0.05
# -

# Почему доверительные интервалы важны в науке о данных?
#
#     Они помогают измерить неопределенность прогнозов и оценок.
#     С помощью этих данных ученые получают надежные результаты, а не просто дают одно число.
#     Они широко используются в A/B-тестировании, машинном обучении и анализе опросов.

# +
# Step 1: Identify the sample problem.

# Define the population parameter you want to estimate e.g., mean height of
# students. Choose the right statistic such as the sample mean.
# Step 2: Select a confidence level.

# In this step we select the confidence level some common choices are 90%, 95%
# or 99%. It represents how sure we are about our estimate.

# +
# Step 3: Find the margin of error.

# To find the Margin of Error, you use the formula:
#     Margin of Error = Critical Value × Standard Error

#     Critical Value: Found using Z-tables (for large samples) or T-tables
# (for small samples).
#     Standard Error (SE): Measures how much the sample mean varies.

#     SE = std / sqrt(n)

# Combine these to get your Margin of Error the amount you add/subtract from
# your estimate to create a range.

# Step 4: Specify the confidence interval.
# To find a Confidence Interval, we use this formula:

#      Confidence Interval = Point Estimate ± Margin of Error

#     The Point Estimate is usually your sample mean.
#     Adding and subtracting the margin of error gives the range where the
# true value is likely to be.
# -

# Some Key Takeaways from Confidence Interval are:
#
#     Confidence Intervals are essential in data science to find the uncertainty of estimates and make predictions more reliable.
#     t-distribution is used for small sample sizes (n < 30) while z-distribution is used for large sample sizes (n > 30).
#     Confidence intervals help to make data-driven decisions by providing a range instead of a single point estimate. This is especially important in A/B testing, market research and machine learning.

# +
import math

import numpy as np
from scipy import stats


# +
def calculate_t_test() -> None:
    """Calculate of t-test."""
    mean = 240
    std = 25
    n = 10
    df = n - 1
    alpha = 0.025
    t = stats.t.ppf(1 - alpha, df)

    moe = t * (std / math.sqrt(n))

    lower = mean - moe
    upper = mean + moe

    print(f"Confidence Interval: ({lower:.2f}, {upper:.2f})")


calculate_t_test()


# +
def calculate_z_test() -> None:
    """Calculate z-test."""
    mean = 4.63
    std_dev = 0.54
    n = 50
    z = 1.960

    se = std_dev / np.sqrt(n)
    moe = z * se

    lower = mean - moe
    upper = mean + moe

    print(f"Confidence Interval: ({lower:.3f}, {upper:.3f})")


calculate_z_test()


# -


def hypothesis_test() -> None:
    """Calculate hypothesis metrics."""
    alpha = 0.05
    b = np.array([120, 122, 118, 130, 125, 128, 115, 121, 123, 119])
    a = np.array([115, 120, 112, 128, 122, 125, 110, 117, 119, 114])
    t_stat, p_val = stats.ttest_rel(a, b)
    print(p_val)
    m = np.mean(b - a)
    s = np.std(b - a, ddof=1)
    t = m / (s / np.sqrt(len(b)))
    print(t)
    decision = "Reject" if p_val <= alpha else "Fail reject"
    concl = (
        "Significant difference."
        if decision == "Reject"
        else "No significant difference."
    )

    print("T:", t_stat)
    print("P:", p_val)
    print("T:", t)
    print(f"Decision: {decision} H0 at α={alpha}")
    print("Conclusion:", concl)
