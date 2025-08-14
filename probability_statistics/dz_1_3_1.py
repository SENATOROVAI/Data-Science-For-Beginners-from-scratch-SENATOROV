"""ДЗ 1. Блок 3. Основы статистики. Раздел 1. Матан+теорвер+статистика.

Книга «Математика для DataScience» Т.Нилд.
"""

# +
import numpy as np
import pandas as pd

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# +
# стр. 29 Суммы в SymPy

from sympy import *

i,n = symbols('i n')
# перебирает элементы i от 1 до n,
# затем умножает и суммирует
summation = Sum(2*i,(i,1,n))
# задает n равным 5,
# перебирает числа от 1 до 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit()) # 30

# +
# стр. 32 Упрощение выражений в SymPy

from sympy import *
x = symbols('x')
expr = x**2 / x**5
print(expr) # x**(-3)

# +
# стр. 34 Логарифмы

from math import log

# 2 в какой степени даст 8?
x = log(8, 2)
print(x) # выводит 3.0

# +
# достройка: точное число сможет вычислить SymPy? Смог

from sympy import log, S

# Вычисляем log₂(8)
result = log(8, 2)

# Упрощаем выражение (если нужно)
simplified_result = result.simplify()

print(result)          # Выведет: log(8)/log(2) (символическое представление)
print(simplified_result)  # Выведет: 3 (поскольку 2³ = 8)

# +
# стр. 36 вычисление сложного процента кредита за 2 года

from math import exp
loan_amount = 100
percents_per_year = .20
n_years = 2.0
n = 12
a = loan_amount * (1 + (percents_per_year/n))**(n * n_years)

print(a) # выводит 148.69146179463576

# +
# стр. 40 lim 1/x , x -> oo

from sympy import *
x = symbols('x')
f = 1 / x
result = limit(f, x, oo)
print(result) # 0

# +
# lim (1 + 1/n)**n = E

from sympy import *

n = symbols('n')
f = (1 + (1/n))**n
result = limit(f, n, oo)
print(result) # E
print(result.evalf()) # 2.71828182845905

# +
# стр. 44 Производная от x**2

from sympy import *

# Объявляем символ 'x' для SymPy
x = symbols('x')
# Теперь объявляем функцию через обычный синтаксис Python
f = x**2
# Вычисляем производную функции
dx_f = diff(f)
print(dx_f) # выводит 2*x
# -

# Вычисляем уклон при x = 2
print(dx_f.subs(x,2)) # выводит 4


# +
def f(x): 
    """Функция."""
    return x**2

def dx_f(x):
    """Производная этой функции."""
    return 2*x

slope_at_2 = dx_f(2.0) # уклон в точке x = 2
print(slope_at_2) # выводит 4.0

# +
# стр 46 Частные производные

from sympy import *
from sympy.plotting import plot3d
# Объявляем символы x и y в SymPy
x,y = symbols('x y')
# Теперь объявляем функцию через обычный синтаксис Python
f = 2*x**3 + 3*y**3
# Вычисляем частные производные по x и y
dx_f = diff(f, x)
dy_f = diff(f, y)
print(dx_f) # выводит 6*x**2
print(dy_f) # выводит 9*y**2
# Выводим график функции
plot3d(f)

# +
# стр 46 Производная как lim df/dx при dx -> 0

from sympy import *

# Объявляем x и шаг s
x, s = symbols('x s')
# Объявляем функцию
f = x**2
# Вычисляем уклон между двумя точками с шагом s
# Подставляем значения в формулу "подъема на дистанции"
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)
# Подставляем значение х = 2
slope_2 = slope_f.subs(x, 2)
# Вычисляем уклон при x = 2,
# когда шаг s бесконечно приближается к 0
result = limit(slope_2, s, 0)
print(result) # 4

# +
from sympy import *

# Объявляем x и шаг s
x, s = symbols('x s')
# Объявляем функцию
f = x**2
# Вычисляем уклон между двумя точками с шагом s
# Подставляем значения в формулу "подъема на дистанции"
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)
# Вычисляем производную,
# когда шаг s бесконечно приближается к 0
result = limit(slope_f, s, 0)
print(result) # 2*x

# +
# стр 48 chain rule

from sympy import *

x = symbols('x')
z = (x**2 + 1)**3 - 2
dz_dx = diff(z, x)
print(dz_dx) # 6*x*(x**2 + 1)**2

# +
from sympy import *

x, y = symbols('x y')
# Производная первой функции
# Задаем имя с нижним подчеркиванием, чтобы не было конфликта переменных
_y = x**2 + 1
dy_dx = diff(_y)
# Производная второй функции
z = y**3 - 2
dz_dy = diff(z)
# Вычисляем производную с помощью цепного правила
# и без него, подставляем функцию y
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# Цепное правило работает:
# оба варианта дают одинаковый результат
print(dz_dx_chain) # 6*x*(x**2 + 1)**2
print(dz_dx_no_chain) # 6*x*(x**2 + 1)**2


# +
# стр. 52 Приближенный расчет интеграла через сумму S прямоугольников

def approximate_integral(a, b, n, f):
    """Приближенный расчет интеграла."""
    delta_x = (b - a) / n  # ширина каждого прямоугольника
    total_sum = 0
    
    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
            # midpoint — координата по x середины верхней стороны прямоугольника
        total_sum += f(midpoint)
        
    return total_sum * delta_x

def my_function(x):
    """Функция."""
    return x**2 + 1

area = approximate_integral(a=0, b=1, n=5, f=my_function)
print(area) # выводит 1.33
# -

area = approximate_integral(a=0, b=1, n=1000, f=my_function)
print(area) # выводит 1.333333250000001

area = approximate_integral(a=0, b=1, n=1_000_000, f=my_function)
print(area) # выводит 1.3333333333332733

# +
# стр. 53 Расчет интеграла через SymPy

from sympy import *

# Объявляем символ x для SymPy
x = symbols('x')
# Объявляем функцию через обычный синтаксис Python
f = x**2 + 1
# Вычисляем интеграл от функции по x в интервале от x = 0 до x = 1
area = integrate(f, (x, 0, 1))
print(area) # выводит 4/3

# +
# стр. 54 Расчет интеграла через пределы

from sympy import *

# Объявляем переменные для SymPy
x, i, n = symbols('x i n')
# Объявляем функцию и интервал
f = x**2 + 1
lower, upper = 0, 1
# Вычисляем ширину и высоту каждого прямоугольника с индексом i
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)
# Перебираем все n прямоугольников и суммируем их площади
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()
# Вычисляем площадь,
# устремив число прямоугольников n к бесконечности
area = limit(n_rectangles, n, oo)
print(area) # выводит 4/3

# +
# стр. 63 Расчет условной P по Ф Байеса

# вероятность того, что человек пьет кофе
p_coffee_drinker = .65
# вероятность того, что человек болен раком
p_cancer = .005
# вероятность того, что человек пьет кофе,
# при условии, что он болен раком
p_coffee_drinker_given_cancer = .85

# вероятность того, что человек болен раком,
# при условии, что он пьет кофе
p_cancer_given_coffee_drinker = \
    p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker
# выводит 0.006538461538461539
print(p_cancer_given_coffee_drinker)

# +
# стр. 68 биномиальные k

from scipy.stats import binom

n = 10 # количество испытаний
# p = 0.9 # P успеха в каждом испытании
p = 0.5 # P успеха в каждом испытании
for k in range(n + 1): # количество успехов
    probability = binom.pmf(k, n, p)
    print(f"{k} - {probability}")
# Вывод:
# 0 - 9.999999999999977e-11
# 1 - 8.999999999999976e-09
# 2 - 3.6449999999999933e-07
# 3 - 8.747999999999988e-06
# 4 - 0.00013778099999999974
# 5 - 0.0014880347999999982
# 6 - 0.011160260999999989
# 7 - 0.05739562799999997
# 8 - 0.1937102444999998
# 9 - 0.38742048899999976
# 10 - 0.34867844010000015

# +
# стр. 71 Бета-распределение. P что успех <= 90 %

from scipy.stats import beta

a = 8
b = 2

p = beta.cdf(.90, a, b)
# 0.7748409780000002
print(p)

# +
# стр. 73 P что базовая P успеха выше 90 %

from scipy.stats import beta

a = 8
b = 2
p = 1.0 - beta.cdf(.90, a, b)
# 0.2251590219999998
print(p)

# +
# стр. 74 Бета-распределение с бОльшим числом испытаний

from scipy.stats import beta

a = 30
b = 6
p = 1.0 - beta.cdf(.90, a, b)
# 0.13163577484183686
print(p)

# +
# стр. 75 S Бета-распределения в диапазоне значений

from scipy.stats import beta

a = 8
b = 2
p = beta.cdf(.90, a, b) - beta.cdf(.80, a, b)
# 0.3386333619999998
print(p)

# +
# стр 86 Среднее арифметическое

sample = [1, 3, 2, 5, 7, 0, 2, 3]
mean = sum(sample) / len(sample)
print(mean) # выводит 2.875

# +
# стр 87 Среднее взвешенное

# Три промежуточных экзамена с весом 0,20 и выпускной экзамен с весом 0,40
sample = [90, 80, 63, 87]
weights = [0.2, 0.2, 0.2, 0.4]
weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights)
print(weighted_mean) # выводит 81.4
# -

# Три промежуточных экзамена с весом 1,0 и выпускной экзамен с весом 2,0
sample = [90, 80, 63, 87]
weights = [1.0, 1.0, 1.0, 2.0]
weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights)
print(weighted_mean) # выводит 81.4

# +
# стр 88 Медиана

# Количество домашних животных у каждого респондента
sample = [0, 1, 5, 7, 9, 10, 14]
def median(values):
    """Вычисляет медиану."""
    ordered = sorted(values)
    n = len(ordered)
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n/2)
   
    if n % 2 == 0:
        return (ordered[mid] + ordered[mid+1]) / 2.0
    else:
        return ordered[mid]
       
print(median(sample)) # выводит 7

# +
# стр 89 Мода

from collections import defaultdict
# Количество домашних животных у каждого респондента
sample = [1, 3, 2, 5, 7, 0, 2, 3]
def mode(values):
    """Вычисляет моду."""
    counts = defaultdict(int)
   
    for s in values:
        counts[s] += 1
       
    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes
   
print(mode(sample)) # [2, 3]

# +
# стр 91 Дисперсия

# Количество домашних животных у каждого респондента
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    """Вычисляет Дисперсию."""
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance

print(variance(data)) # выводит 21.387755102040817

# +
# стр 92 СКО

from math import sqrt

# Количество домашних животных у каждого респондента
data = [0, 1, 5, 7, 9, 10, 14]
def variance(values):
    """Вычисляет Дисперсию."""
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance
   
def std_dev(values):
    """Вычисляет СКО."""
    return sqrt(variance(values))
   
print(std_dev(data)) # выводит 4.624689730353899

# +
# стр 93 СКО выборки

from math import sqrt
# Количество домашних животных у каждого респондента
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values, is_sample: bool = False):
    """Вычисляет Дисперсию."""
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) /\
        (len(values) - (1 if is_sample else 0))
   
    return _variance
   
def std_dev(values, is_sample: bool = False):
    """Вычисляет СКО."""
    return sqrt(variance(values, is_sample))
   
print(f"Дисперсия = {variance(data, is_sample=True)}") # 24.952380952380953
print(f"Стандартное отклонение = {std_dev(data, is_sample=True)}") 
# 4.995235825502231

# +
# стр 98 Норм распределение на Python руками

import math

# нормальное распределение, возвращает правдоподобие
def normal_pdf(x: float, mean: float, std_dev: float) -> float:
    """Нормальное распределение."""
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * \
        math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * std_dev ** 2)))
       
value =  normal_pdf(1, 0, 1)
print(f'pdf {value:.2f}')

# +
# стр 101 Расчет CDF

from scipy.stats import norm

mean = 64.43 # среднее
std_dev = 2.99 # стандартное отклонение
x = norm.cdf(64.43, mean, std_dev)
print(x) # выводит 0.5

# +
from scipy.stats import norm

mean = 64.43
std_dev = 2.99
x = norm.cdf(66, mean, std_dev) - norm.cdf(62, mean, std_dev)
print(x) # выводит 0.4920450147062894

# +
from scipy.stats import norm

x = norm.ppf(.95, loc=64.43, scale=2.99)
    # первый аргумент 0.95 — вероятность
    # loc — среднее, scale — стандартное отклонение
print(x) # 69.3481123445849

# +
# стр 103 Пример 3.13. Генератор случайных чисел, которые соответствуют нормальному распределению

import random
from scipy.stats import norm

for i in range(0, 1000):
    random_p = random.uniform(0.0, 1.0)
    random_weight = norm.ppf(random_p, loc=64.43, scale=2.99)
    print(random_weight)


# +
# стр 104 Пример 3.14. Преобразование Z-оценки в значение x и обратно

def z_score(x, mean, std):
    """Z-оценка."""
    return (x - mean) / std
   
def z_to_x(z, mean, std):
    """Z-оценка обратная."""
    return (z * std) + mean
   
mean = 140_000
std_dev = 3_000
x = 150_000
# Преобразование из x в Z-оценку и обратно
z = z_score(x, mean, std_dev)
back_to_x = z_to_x(z, mean, std_dev)
print(f"Z-оценка: {z}") # Z-оценка: 3.333…
print(f"Преобразование обратно в x: {back_to_x}") # X: 150000.0

# +
# стр 106 Пример 3.15. Изучение центральной предельной теоремы на Python

# Выборочные средние равномерного распределения образуют нормальное распределение
import random
import plotly.express as px
import matplotlib.pyplot as plt

sample_size = 31
sample_count = 1000
# Центральная предельная теорема в действии:
# 1000 выборок, в каждой из которых по 31 случайному значению
# в диапазоне от 0 до 1
x_values = [(sum([random.uniform(0.0, 1.0)
                  for i in range(sample_size)]) / sample_size)
for _ in range(sample_count)]
y_values = [1 for _ in range(sample_count)]

# px.histogram(x=x_values, y = y_values, nbins=20).show()
# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(x_values, bins=20, color='skyblue', edgecolor='black', density=True)

# +
# стр 110 Пример 3.16. Получение критических Z-оценок

from scipy.stats import norm

def critical_z_value(p):
    """2 критич z-значения, соответствующие заданному уровню P."""
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area = (1.0 - p) / 2.0
    upper_area = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)
   
print(critical_z_value(p=.95))
# (-1.959963984540054, 1.959963984540054)
# -

# ![image.png](attachment:image.png)

# +
# стр 111 Пример 3.17. Вычисление доверительного интервала на Python

from math import sqrt
from scipy.stats import norm

def critical_z_value(p):
    """2 критич z-значения, соответствующие заданному уровню P."""
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area = (1.0 - p) / 2.0
    upper_area = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)
   
def confidence_interval(p, sample_mean, sample_std, n):
    """Доверит интервал."""
    # Размер выборки должен быть больше 30
    lower, upper = critical_z_value(p)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))
   
    return sample_mean + lower_ci, sample_mean + upper_ci

print(confidence_interval(p=.95, sample_mean=64.408, sample_std=2.05, n=31))
# (63.68635915701992, 65.12964084298008)

# +
# стр 113 Пример 3.18. Вычисление вероятности восстановления в течение 15–21 дня

from scipy.stats import norm

# Среднее время восстановления после простуды — 18 дней,
# стандартное отклонение — 1,5 дня
mean = 18
std_dev = 1.5
# С вероятностью 95 % время восстановления занимает 15–21 день
x = norm.cdf(21, mean, std_dev) - norm.cdf(15, mean, std_dev)
print(x) # 0.9544997361036416
# -

# ![image.png](attachment:image.png)

# Теперь предположим, что группа из 40 пациентов получила новое экспериментальное лекарство, и им потребовалось в среднем 16 дней, чтобы восстановиться после простуды, 
#
# как показано на рис. 3.17.
#
# ![image-2.png](attachment:image-2.png)

# +
# Пример 3.20. Вычисление одностороннего p-значения

from scipy.stats import norm

# Среднее время восстановления после простуды — 18 дней,
# стандартное отклонение — 1,5 дня
mean = 18
std_dev = 1.5
# Вероятность для 16 и менее дней
p_value = norm.cdf(16, mean, std_dev)
print(p_value) # 0.09121121972586788
# -

# ![image.png](attachment:image.png)

# +
# стр 118 Пример 3.21. Вычисление интервала для статистической значимости 5 %

from scipy.stats import norm

# Среднее время восстановления после простуды — 18 дней,
# стандартное отклонение — 1,5 дня
mean = 18
std_dev = 1.5
# Какому значению x соответствуют первые 2,5 % площади под кривой?
x1 = norm.ppf(.025, mean, std_dev)
# Какому значению x соответствуют первые 97,5 % площади под кривой?
x2 = norm.ppf(.975, mean, std_dev)
print(x1) # 15.060054023189918
print(x2) # 20.93994597681008
# -

# Результат 2-стороннего теста
#
# ![image.png](attachment:image.png)

# 2-стороннее p-value добавляет 2 симметричную область
#
# ![image.png](attachment:image.png)

# +
# стр 119 Пример 3.22. Вычисление двустороннего p-значения

from scipy.stats import norm

# Среднее время восстановления после простуды — 18 дней,
# стандартное отклонение — 1,5 дня
mean = 18
std_dev = 1.5
# Вероятность восстановиться менее чем за 16 дней
p1 = norm.cdf(16, mean, std_dev)
# Вероятность восстановиться более чем за 20 дней
p2 = 1.0 - norm.cdf(20, mean, std_dev)
# p-значение для обоих хвостов
p_value = p1 + p2
print(p_value) # 0.18242243945173575

# +
# стр 122 Пример 3.23. Вычисление критической области с помощью распределения Стьюдента

from scipy.stats import t

# вычисляем интервал критических значений для уверенности 95 %
# (25 элементов в выборке)
n = 25
lower = t.ppf(.025, df=n-1)
upper = t.ppf(.975, df=n-1)
print(lower, upper)
# -2.063898561628021 2.0638985616280205
