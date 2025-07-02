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
