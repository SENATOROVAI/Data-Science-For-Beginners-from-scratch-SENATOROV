"""Пуассон."""

# +
from math import factorial as f

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -

# # Задача 1.
# Среднее число самолетов, взлетающих с полевого аэродрома за одни сутки, равно 10. Найти вероятность того, что за 6 часов взлетят:
#
# А) три самолета,
#
# Б) не менее двух самолетов.
#
# p = 10/24 = 0.4167
#
# k = 3
#
# l_ = 2.5002

# # а)
#

# +
p_: float = 10 / 24

k_: int = 3

l_: float = p_ * 6
# -

p_t: float = l_**k_ * np.exp(-l_) / f(k_)
p_t

# # б)

# p_t = 1 - p6(1)

p_t1: float = 1 - l_**1 * np.exp(-l_) - l_**0 * np.exp(-l_)
p_t1

# # Задача 2.
#  На автовокзале время прибытия автобусов различных рейсов объявляет дежурный. Появление информации о различных рейсах происходит случайно и независимо друг от друга. В среднем на автовокзал прибывает 5 рейсов каждые полчаса.
#
# А) Составьте ряд распределения числа сообщений о прибытии автобусов в течение получаса.
#
# Б) Найдите числовые характеристики этого распределения.
#
# В) Запишите функцию распределения вероятностей и постройте ее график.
#
# Г) Чему равна вероятность того, что в течение получаса прибудут не менее трех автобусов?
#
# Д) Чему равна вероятность того, что в течение четверти часа не прибудет ни один автобус?
#
#

# # А)
#
# Мат ожидание - 5

# +
lbd: int = 5


def ps(x1: int, lambda_: float) -> float:
    """Calculate Poisson probability.

    Args:
        x1: Number of events
        lambda_: Expected number of events

    Returns:
        Probability value
    """
    return float(lambda_**x1 * np.exp(-lambda_) / f(x1))


y_: list[float] = [ps(k_, 5) for k_ in range(13)]
x_: list[float] = [float(s_) for s_ in range(13)]
data: dict[str, list[float]] = {"k": x_, "P(k)": y_}

# +
summa_: float = sum(y_)

summa_
# -

d_: tuple[int, int] = len(x_), len(y_)
d_

df = pd.DataFrame(data)

df

# # Б) Не умею считать ни дисперсию, ни среднеквадратное отклонение

# # В)

# +
plt.figure(figsize=(8, 5))
plt.bar(x_, y_, color="green", alpha=0.9)

# Оформление графика
plt.title(f"Распределение Пуассона (λ = {lbd})", fontsize=14)
plt.xlabel("k (Количество событий)", fontsize=12)
plt.ylabel("P(k) (Вероятность)", fontsize=12)
plt.xticks(range(0, 13, 2))
plt.grid(axis="y", linestyle=":", alpha=0.6)

# Показать график
plt.show()
# -

# Г) Чему равна вероятность того, что в течение получаса прибудут не менее трех автобусов?

f_: float = 1 - sum(ps(x_2, 5) for x_2 in range(3))
f_

# Д) Чему равна вероятность того, что в течение четверти часа не прибудет ни один автобус?
#
# Поступим логически, и мат ожидание определим пропорционально уменьшению промежутка времени - уменьшим его на 2

# +
lbd1: float = 5 / 2

ps(0, lbd1)
# -

# # Задача 3.
# АТС получает в среднем за час 480 вызовов. Определить вероятность того, что за данную минуту она получит:
#
# a) ровно 3 вызова;
#
# b) от 2 до 5 вызовов.

# a)
lbd2: float = 480 / 60
ps(3, lbd2)

# +
# б)

w_: float = ps(3, lbd2) + ps(2, lbd2) + ps(4, lbd2) + ps(5, lbd2)
w_
# -

# # Локальная теорема лапласа

# # 1 задача

# ![image.png](attachment:image.png)

# # 2 задача

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # 3 задача

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # 4 задача

# ![image.png](attachment:image.png)

# # Интегральная теорема Лапласа

# # 1 Задача

# ![image.png](attachment:image.png)

# # 2 задача

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # 3 Задача

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)
