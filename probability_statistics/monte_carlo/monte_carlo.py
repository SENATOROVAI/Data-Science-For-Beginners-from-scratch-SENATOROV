# ![image.png](attachment:image.png)

#

"""Module on monte carlo."""
# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# +
import numpy as np
import pandas as pd

# from numpy.typing import NDArray
# import seaborn as sns # надстройка над матплотлиб
# from typing import Any
# -

# кидаем кубик
print(np.random.randint(1, 7))

# грани кубика
x_cube = np.arange(1, 7)

# void
# [4, 5, 1, 6, 2, 3]
print(np.random.shuffle(x_cube))

print(x_cube)

# выборка без повторений, replace=False
# мы берём грань и не возвращаем её
print(np.random.choice([1, 2, 3, 4, 5, 6], size=6, replace=False))

# +
# чтобы воспроизвести результаты эксперимента, нужно задать сиид
print(np.random.seed(321))

#  выборка с повторением
# [5, 3, 5, 2, 1, 2, 1, 3, 1, 5] # 321
print(np.random.choice([1, 2, 3, 4, 5, 6], size=10, replace=True))
# -

# ![image.png](attachment:image.png)

# +
n_ = 10**6  # > 10000 , > 100000
# счётчик благоприятствующих
m_ = 0
# Начальная установка датчика случайных чисел
print(np.random.seed(310))

# создаем модель

for i in range(0, n_):
    # 10 подбрасываний монетки
    a_ = np.random.choice([0, 1], p=[0.5, 0.5], size=10)
    b_ = np.random.choice([0, 1], p=[0.5, 0.5], size=10)

    if sum(a_) == sum(b_):
        m_ += 1

# относительная частота событий
proba = m_ / n_
# 0.176369
proba
# -

summa_a: int = sum([1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
summa_b: int = sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
print(summa_a == summa_b)

print(n_)

# монетка
#  sample - выборка
print(type(pd.Series([0, 1]).sample(1)))
# pandas.core.series.Series

# numpy.int64
print(type(pd.Series([0, 1]).sample(1).values[0]))

print(pd.Series([0, 1]).sample(1).values[0] + 1)

# выборка с повторением
print(pd.Series([0, 1]).sample(10, replace=True))

# ДСВ, PMF
# монетка
print(np.random.binomial(1, 0.5))

# ДСВ, PMF
# монетка 3 раза
print(np.random.binomial(1, 0.5, size=3))

# +
# побрасываем 3 раза монетку

result_1: list[int] = []
#  O(n)
for _ in range(3):
    result_1.append(np.random.binomial(1, 0.5))
# -

print(result_1)

# побрасываем 3 раза монетку
print([np.random.binomial(1, 0.5) for _ in range(3)])


# создаем функцию подбрасывания монетки
def coin_toss() -> float:
    """Подбрасывает монету и возвращает результат."""
    return pd.Series([0, 1]).sample(1).item()


# создаем функцию подбрасывания монетки
def coin_toss2() -> int:
    """Подбрасывает монету и возвращает результат."""
    return np.random.binomial(1, 0.5)


print(coin_toss())
print(coin_toss2())

result: list[float] = []
for _ in range(3):
    result.append(coin_toss())
print(result)

list_comreh_0: list[float] = [coin_toss() for _ in range(3)]
print(list_comreh_0)

list_comreh_1: list[int] = [coin_toss2() for _ in range(3)]
print(list_comreh_1)

# монетка 10 выборок
# выборка с повторением
print(pd.Series([0, 1]).sample(10, replace=True))

# кубик 10 выборок
lst = pd.Series([1, 2, 3, 4, 5, 6])
print(lst.sample(10, replace=True))

# выдадим общий индекс, и уберем 1 колонку - индексы
print(lst.sample(10, replace=True).reset_index())

# +
# уберем 1 колонку - индексы
sampled_series = lst.sample(10, replace=True).reset_index(drop=True)

# Print the sampled Series
print(sampled_series)
# -

# кубик 1000 подбрасываний, посчитаем количество каждой грани
# для дискретной переменной, чтобы посмотреть распределение
# нужно value_counts
# дсв
print(pd.Series(np.random.randint(1, 7, size=10000)).value_counts())

print(1 / 6)
