"""Probability and statistics."""

import pandas as pd
import numpy as np
import seaborn as sns
import scipy
# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# !pip install pandas
# !pip install scipy

import matplotlib.pyplot as plt
plt.style.use('dark_background')

np.random.randint(1,7)

dice = pd.Series([1,2,3,4,5,6])

dice.mean()

np.random.randint(1,7,size=10)

dice.sample(10,replace=True)

dice.mean()

dice.sample(4,replace=True).mean()

result = []
for n in range(1,1000):
  result.append(dice.sample(n,replace=True).mean())

result[:10]

pd.Series(result).plot(grid=True)

result = [dice.sample(n,replace=True).mean() for n in range(1,1000)]

pd.Series([dice.sample(n,replace=True).mean() for n in range(1,1000)]).plot()

t = dice.sample(1000,replace=True).to_frame().reset_index(drop=True)
t['cum'] = t[0].cumsum()
t['sample_size'] = range(1,1001)
t['mean'] = t['cum'] / t['sample_size']
t.set_index('sample_size')['mean'].plot(grid=True)

pd.Series([dice.sample(n,replace=True).mean() for n in range(1,1000)]).plot()

np.random.normal(size=1000)

# Нормальное

t = pd.DataFrame(np.random.normal(size=1000))
t['cum'] = t[0].cumsum()
t['sample_size'] = range(1,1001)
t['mean'] = t['cum'] / t['sample_size']
t.set_index('sample_size')['mean'].plot(grid=True)

# Равномерное

n = 10000
t = pd.DataFrame(np.random.uniform(size=n))
t['cum'] = t[0].cumsum()
t['sample_size'] = range(1,n+1)
t['mean'] = t['cum'] / t['sample_size']
t.set_index('sample_size')['mean'].plot(grid=True)

# Логнормальное

sns.histplot(np.random.lognormal(size=1000))

from scipy.stats import lognorm

s = 0.954
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

mean

rv = lognorm(s)

s = 3
r = lognorm.rvs(s, size=1000)
sns.histplot(r)

pd.Series(r).hist()

sns.histplot(np.random.normal(size=10000))

mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

mean

n = 10000
t = pd.DataFrame(lognorm.rvs(s, size=n))
t['cum'] = t[0].cumsum()
t['sample_size'] = range(1,n+1)
t['mean'] = t['cum'] / t['sample_size']
t.set_index('sample_size')['mean'].plot(grid=True)

t[0].mean()

n = 10000
t = pd.DataFrame(np.random.uniform(size=n))
t['cum'] = t[0].cumsum()
t['sample_size'] = range(1,n+1)
t['mean'] = t['cum'] / t['sample_size']
t.set_index('sample_size')['mean'].plot(grid=True)

# Центральная предельная теорема
# если вы берёте большое количество случайных выборок из любой совокупности (распределения) с конечным средним и дисперсией, то распределение средних значений этих выборок будет примерно нормальным (то есть, как колокол), независимо от формы исходного распределения. Эта теорема используется, чтобы понять, как данные будут распределяться, когда размер выборки становится достаточно большим.

sns.histplot(dice,bins=6)

data = [dice.sample(1000,replace=True).mean() for _ in range(10000)]
sns.histplot(data)



# +
import pylab
import scipy.stats as stats

stats.probplot(data, dist="norm", plot=pylab)
pylab.show()
# -

data = [dice.sample(1000,replace=True).sum() for _ in range(10000)]
sns.histplot(data)



def d() -> int:
  """Return a single random dice roll value."""
  return dice.sample(1,replace=True).values[0]


d()

sns.histplot([d() + d() + d() + d() for _ in range(10000)])

data = [dice.sample(100,replace=True).mean() for _ in range(10000)]

sns.histplot(data)

data = [dice.sample(1000,replace=True).mean() for _ in range(10000)]

sns.histplot(data)

# Логнормальное

s = 1.5
r = lognorm.rvs(s, size=1000)
sns.histplot(r)

data = [lognorm.rvs(s, size=10000).mean() for _ in range(10000)]

sns.histplot(data)

# +
# Построение Q-Q графика для проверки нормальности распределения
# Q-Q график сравнивает квантили нашего распределения с квантилями нормального распределения
# Если точки ложатся близко к прямой линии, это говорит о том, что распределение близко к нормальному
# Импортируем необходимые библиотеки:
# pylab - для визуализации
# scipy.stats - для статистических функций
import pylab
import scipy.stats as stats

# Создаем Q-Q график (quantile-quantile plot)
# stats.probplot() сравнивает квантили нашего распределения (data) 
# с теоретическими квантилями нормального распределения
# Параметры:
# - data: наши данные для анализа
# - dist="norm": сравниваем с нормальным распределением
# - plot=pylab: указываем использовать pylab для построения графика
stats.probplot(data, dist="norm", plot=pylab)

# Отображаем график
# Если точки ложатся близко к прямой линии - 
# это значит, что наше распределение близко к нормальному
# Отклонения от прямой указывают на отличия от нормального распределения
pylab.show()
# -

# Стандартное отклонение и квадратный корень и n

from tqdm.notebook import tqdm

# +



# -

result = []
for n in tqdm(range(1,100)):
  result.append(pd.Series([dice.sample(n,replace=True).mean() for _ in range(1000)]).std())

pd.Series(result).plot()

# Это обратно пропорционально квадратному корню из n

pd.Series(1/np.sqrt(range(100))).plot()

# +
import numpy as np
import matplotlib.pyplot as plt

# Параметры моделирования
n_simulations = 1000  # Количество повторений эксперимента
sample_sizes = [10, 50, 100, 500, 1000]  # Размеры выборок для тестирования
a = 0  # Нижняя граница равномерного распределения 
b = 1  # Верхняя граница равномерного распределения
true_mean = (a + b) / 2  # Теоретическое среднее значение = (a + b)/2
true_var = (b - a)**2 / 12  # Теоретическая дисперсия = (b-a)^2/12

# Для каждого размера выборки генерируем n_simulations выборок
# и строим гистограмму распределения их средних значений
for sample_size in sample_sizes:
    # Генерируем выборки и вычисляем их средние
    means = [np.random.uniform(a, b, sample_size).mean() 
             for _ in range(n_simulations)]
    
    # Вычисляем характеристики распределения выборочных средних:
    # empirical_mean - среднее значение всех выборочных средних
    # empirical_std - стандартное отклонение выборочных средних
    empirical_mean = np.mean(means)  # Усредняем все полученные средние значения
    empirical_std = np.std(means)    # Считаем разброс средних значений
    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.hist(means, bins=30, density=True, alpha=0.7,
             label=f'Эмпирическое распределение\nСреднее={empirical_mean:.3f}\nСКО={empirical_std:.3f}')
    plt.axvline(true_mean, color='r', linestyle='--', 
                label=f'Теоретическое среднее={true_mean}')
    
    plt.title(f'Распределение выборочного среднего\nРазмер выборки n={sample_size}')
    plt.xlabel('Значение')
    plt.ylabel('Плотность')
    plt.legend()
    plt.show()

# +
import matplotlib.pyplot as plt
import numpy as np
# Решение предела при x стремящемся к бесконечности
# lim (2x^2 - 3x - 5)/(x + 1) при x→+∞

# Для нахождения предела разделим числитель и знаменатель на старшую степень x (x^2)
# lim (2 - 3/x - 5/x^2)/(1/x + 1/x^2) = 2

# Создадим функцию для вычисления значений выражения
def f(x) -> float:
    """Calculate (2x^2 - 3x - 5)/(x + 1)."""
    return (2*x**2 - 3*x - 5)/(x + 1)

# Создадим массив значений x
x = np.linspace(1, 100, 1000)

# Вычислим значения функции
y = f(x)

# Построим график
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='f(x)')
plt.axhline(y=2, color='r', linestyle='--', label='y = 2')
plt.title('График функции f(x) = (2x^2 - 3x - 5)/(x + 1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

print(f"Предел функции при x→+∞ равен 2")
