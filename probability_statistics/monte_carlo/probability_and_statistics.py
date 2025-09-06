"""Probability and statistics."""

# +
import pandas as pd
import numpy as np
import seaborn as sns

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable
# -

np.random.randint(1,7)

np.arange(1,10)

# воспроизводимость результатов расчёта
np.random.seed(321)
# перемешали данные
x = [1,2,3,4]
np.random.shuffle(x)
x 

# выборка с повторением/без повторения
np.random.choice([1,2,3,4,5], size=10, replace=False)

# ![image.png](attachment:image.png)

# +
n = 10**6  # Объем испытаний
m = 0  # Счетчик числа благоприятствующих случаев

np.random.seed(312)  # Начальная установка датчика случайных чисел
# Данная команда используется для воспроизводимости результата моделирования

for i in range(0, n):  # Цикл; счетчик цикла i (от 0 до n-1) - номер опыта
    # В ячейках a и b - результат десяти подбрасываний (массивы, содержащие нули (выпала решка) и единицы (выпал герб))
    a = np.random.choice([0, 1], p=[0.5, 0.5], size=10)
    b = np.random.choice([0, 1], p=[0.5, 0.5], size=10)
    
    if sum(a) == sum(b):  # Если число гербов одинаковое
        m += 1  # Увеличить на 1 значение счетчика

# Для оценки вероятности берется относительная частота события
p = m / n
print(p)  # Вывод вероятности
# -

# случайным образом возьми 1 элемент 
pd.Series([0,1]).sample(1).values[0]

# два исхода биномиальное распр, дсв
np.random.binomial(1,0.5)

# подбросили 3 раза монетку
np.random.binomial(1,0.5,size=3)

# подбросили 3 раза монетку
result = []
for _ in range(3):
  result.append(np.random.binomial(1,0.5))

result

# подбросили 3 раза монетку
[np.random.binomial(1,0.5) for _ in range(3)]





# создаем функцию подбрасывания монетки
def coin_toss() -> int:
  """Simulate a coin toss and returns 0 or 1."""
  return pd.Series([0,1]).sample(1).values[0]


# создаем функцию подбрасывания монетки
def coin_toss2() -> int:
  """Simulate a coin toss using binomial distribution."""
  return np.random.binomial(1,0.5)


coin_toss()

result = []
for _ in range(3):
  result.append(coin_toss())

result

[coin_toss() for _ in range(3)]

[coin_toss2() for _ in range(3)]

# монетка 10 выборок
pd.Series([0,1]).sample(10,replace=True)

# кубик 10 выборок
pd.Series([1,2,3,4,5,6]).sample(10,replace=True)

# убираем индекс элемента, и выдаём общий индекс
# pd.Series([1,2,3,4,5,6]).sample(10,replace=True).reset_index()
pd.Series([1,2,3,4,5,6]).sample(10,replace=True).reset_index(drop=True)

# кубик 1000 подбрасываний, посчитаем количество каждой грани
# для дискретной переменной, чтобы посмотреть распределение
# нужно value_counts
# дсв
pd.Series(np.random.randint(1,7,size=10000)).value_counts()
# [0000000000000001,31123123123123123123123123123123123123123123123,5, 0000000000000005]

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

#  закон больших чисел, в данном случае мы увеличиваем выборку
# если мы повторяем один и тот же эксперимент много раз и записываем результат каждого раза, 
# то среднее значение результатов будет приближаться мат. ожиданию, то есть 
# к истинному(теоретическому) среднему
# монетка идеальный пример
# ДСВ распределение
pd.Series(np.random.randint(1,7,size=100000)).hist()

np.random.binomial(1,0.7)

# 7 from 10 orel
pd.Series([1,1,1,1,1,1,1,0,0,0]).sample(10,replace=True)

# 7 from 10 orel
[1]*7+[0]*3

[1]*3

[1] + [0]

pd.Series([1]*7+[0]*3).sample(10,replace=True)

# создаем ромашку
pd.Series(['любит','не любит']).sample(1)


def chamomile() -> pd.Series:
    """Return random choice between 'любит' and 'не любит' as pandas Series."""
    return pd.Series(['любит','не любит']).sample(1)


chamomile()

# збч, sample
pd.Series(np.random.binomial(1,0.5,size=100000)).hist()

pd.Series([1,2,3,4,5,6]).sample(100000,replace=True).hist()

# +
# НСВ расперделения
# -

# PDF
pd.Series(np.random.uniform(size=1000)).hist()

pd.Series(np.random.uniform(size=100))

# +
pd.Series(np.random.normal(size=10000)).hist()

# """
#     Code by Tae-Hwan Hung(@graykode)
#     https://en.wikipedia.org/wiki/Normal_distribution
# """
# import numpy as np
# from matplotlib import pyplot as plt

# def normal(x, n):
#     u = x.mean()
#     s = x.std()

#     # normalization
#     x = (x - u) / s

#     # divide [x.min(), x.max()] by n
#     x = np.linspace(x.min(), x.max(), n)

#     a = ((x - 0) ** 2) / (2 * (1 ** 2))
#     y = 1 / (s * np.sqrt(2 * np.pi)) * np.exp(-a)

#     return x, y, x.mean(), x.std()

# x = np.arange(-100, 100) # define range of x
# x, y, u, s = normal(x, 10000)

# plt.plot(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
# plt.legend()
# plt.savefig('graph/normal.png')
# plt.show()
# -

# моделирование звонков, в срднем 5 в час, всего 100 звонков
pd.Series(np.random.poisson(5,size=100)).hist()

# +
# цпт  
# в большом количестве независимых наблюдений среднее значение будет иметь нормальное распределение.

# Почему это важно?

# Центральная предельная теорема позволяет нам делать выводы о популяции, даже если мы не знаем всех ее данных. Например, 
# если мы хотим узнать средний рост людей в стране, мы можем взять случайную выборку и измерить рост людей в этой выборке. 
# Благодаря центральной предельной теореме мы знаем, 
# что средний рост в выборке будет приближаться к среднему росту в стране,
# и мы можем использовать это, чтобы сделать выводы о всей популяции.

pd.Series(np.random.chisquare(100,size=1000)).hist()
# -

# жирнохвостовое
pd.Series(np.random.lognormal(size=1000)).hist()

# жирный хвост
pd.Series(np.random.pareto(1,size=1000)).hist()

uniform = pd.Series(np.random.uniform(size=10000))

#pdf
pd.Series(uniform.sample(100000,replace=True)).hist()

import seaborn as sns

u = np.random.randint(1,7,size=100000)

#pmf
sns.histplot(u,stat='probability')

sns.ecdfplot(u)

2/6

#pmf
sns.histplot(pd.Series([1,2,3,4,4,5,6]).sample(10000,replace=True),stat='probability')

sns.ecdfplot(pd.Series([1,2,3,4,4,5,6]).sample(10000,replace=True))

0.12234312531252314531252314531253125312

sns.histplot(np.random.normal(size=10000),stat='probability')

# KDE - функция которая апроксимирует гистограмму
sns.kdeplot(np.random.normal(size=10000))

sns.ecdfplot(np.random.normal(size=10000))

sns.histplot(np.random.uniform(size=10000))

#cfd
sns.ecdfplot(np.random.uniform(size=1000))

#cdf
sns.ecdfplot(np.random.normal(size=10000))

measurements = np.random.normal(size=10000)

#pdf
sns.histplot(measurements)

measurements = np.random.uniform(size=10000)

#pdf
sns.histplot(measurements)

# +
## QQ - график
import numpy as np
import pylab
import scipy.stats as stats


stats.probplot(measurements, dist="uniform", plot=pylab)
pylab.show()
# -

np.random.binomial(1,0.5,size=2)

np.random.binomial(1,0.5,size=2).sum()

# 2 подбрасывания, 10 тысяч раз
n = 10000
result = []
for _ in range(n):
  result.append(np.random.binomial(1,0.5,size=2).sum())

pd.Series(result).value_counts(normalize=True)

0.5 * 0.5

#  два орла подряд
pd.Series(np.random.binomial(2,0.5,size=10000)).value_counts(normalize=True)

# 10  орлов подряд, pmf
sns.histplot(np.random.binomial(10,0.5,size=10000))
