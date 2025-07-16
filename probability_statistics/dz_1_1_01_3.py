"""ДЗ 1. Блок 1. Введение в теорию вероятностей. 0.1 курс на Stepik. Метод
МонтеКарло.

ч.3 .
"""

# +
# pylint: disable=unused-import

from random import shuffle

# доп import чтоб линтеры проходили
# from typing import List, Optional, Tuple, Union
from typing import List, Tuple

import numpy as np
import pandas as pd

# +
# Парадокс ДР
# Определить вероятность того, что в группе, состоящей из 23 человек,
# у двух людей будет совпадение дней рождения (число и месяц).


bd = pd.Series(range(365))

# +
t_data = bd.sample(23, replace=True)

t_data.duplicated()
# -

rooms = [bd.sample(23, replace=True).duplicated().max() for _ in range(10000)]

np.mean(rooms)

# +
# Парадокс 2. Экзамент и билеты
# Экзамен проходит по следующей схеме: если некоторый билет уже был вытянут,
# то после ответа экзаменатор откладывает его в сторону.
# Студент выучил 20 билетов из 30. Когда ему выгоднее идти, первым или вторым,
# чтобы вероятность вынуть выученный билет была больше?
# -

tickets = list(range(1, 31))

student = list(range(1, 21))

shuffle(tickets)

# +
n_param = 100000
student = list(range(1, 21))
tickets = list(range(1, 31))
result = []

for _ in range(n_param):
    shuffle(tickets)
    result.append(tickets[0] in student)
# -

np.mean(result)

# +
n_param = 100000
student = list(range(1, 21))
tickets = list(range(1, 31))
result = []

for _ in range(n_param):
    shuffle(tickets)
    result.append(tickets[1] in student)
# -

np.mean(result)  # искажение Байесовского восприятия

# +
# Парадокс 3. Синие и зеленые такси


np.random.binomial(1, 0.15)
# 1 - синее
# 0 - зелёное

# +
# генератор


def witness(taxi: int) -> int:
    """witness."""
    if np.random.binomial(1, 0.8):
        return taxi
    return abs(taxi - 1)


# -

witness(0)
# input 0 - зелёное, return 1 - синее, ошибся

# +
# nbqa-mypy: disable-all

#  monte carlo
n_param = 100000
result_2: list[tuple[int, int]] = []
for _ in range(n_param):
    taxi_param = np.random.binomial(1, 0.15)
    witness_answer_1 = witness(taxi_param)
    result_2.append((taxi_param, witness_answer_1))
# -

t_data_2 = pd.DataFrame(result_2, columns=["taxi", "witness_answer"])
t_data_2

t_data_2.groupby("witness_answer")["taxi"].mean()
# 1    0.416681 41% случаев свидетель будет прав, что реально принадлежит синим
# самое интересное что свидетель верно определяет в 80% случаев,
# получается это опять искажение Баейсовского восприятия

# +
# Парадокс 4. Русская рулетка


chamber = [1, 1, 0, 0, 0, 0]

# +
# pylint: disable=redefined-outer-name


def one_turn(chamber_p: list[int]) -> list[int]:
    """One turn."""
    new_chamber = [0, 0, 0, 0, 0, 0]
    n_param = len(chamber_p)
    for i in range(n_param):
        if i < n_param - 1:
            new_chamber[i + 1] = chamber_p[i]
        else:
            new_chamber[0] = chamber_p[i]
    return new_chamber


# +
# pylint: disable=redefined-outer-name


def spin_chamber(chamber_p: list[int]) -> list[int]:
    """spin_chamber."""
    n_param = np.random.randint(1, 7)
    for _ in range(n_param):
        chamber_p = one_turn(chamber_p)
    return chamber_p


# -

spin_chamber([1, 1, 0, 0, 0, 0])

pd.Series([spin_chamber([1, 1, 0, 0, 0, 0]) for _ in range(100000)]).astype(
    str
).value_counts(normalize=True)

# +
n_param = 10000
result_3: list[tuple[int, int]] = []

for _ in range(n_param):
    # заряжаем револьвер
    chamber = [1, 1, 0, 0, 0, 0]
    # первый игрок крутит барабан
    chamber = spin_chamber(chamber)
    # первый игрок стреляет
    chamber = one_turn(chamber)
    p1 = chamber[0]
    # убрали пулю после выстрела
    chamber[0] = 0

    # второй игрок вращает барабан -- нужно ли это действие?
    chamber = spin_chamber(chamber)

    # второй игрок стреляет
    chamber = one_turn(chamber)
    p2 = chamber[0]

    result_3.append((p1, p2))
# -

t_data_2 = pd.DataFrame(result_3, columns=["p1", "p2"])
t_data_2

t_data_2.groupby("p1")["p2"].agg(["count", "mean"])
# 0 - выжил, первый игрок выжил, вероятность что 2 игрок умрет,
# если крутонешь барабан 0.33%
# 1 - умер
