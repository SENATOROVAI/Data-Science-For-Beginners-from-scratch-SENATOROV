"""Monte Carlo Practice."""

# +
import pandas as pd
import numpy as np

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable
# -

dice = pd.Series([1,2,3,4,5,6])

dice.sample(1).values[0]

rolls = [dice.sample(1).values[0] for _ in range(100000)]

rolls[:10]

pd.Series(rolls).value_counts(normalize=True)

1/6

dice.value_counts(normalize=True)

# Определить вероятность того, что в группе, состоящей из 23 человек, у двух людей будет совпадение дней рождения (число и месяц).
#

# Парадокс дней рождения⁠⁠
# В теории вероятностей и комбинаторике с днями рождения связана известная задача, называемая «парадокс дней рождения». Данный «парадокс» гласит, что в любой случайно собранной группе из 23 человек с вероятностью более 50 % у двух или более человек дни рождения совпадают (на первый взгляд, это противоречит житейской интуиции). С ростом численности группы людей вероятность наличия совпадения в днях рождения быстро приближается к единице: так, в случайно собранной группе из 57 человек двое из них имеют день рождения в один день с вероятностью 99 %.
#
# ### ошибка Байесовского восприятия /  Искажение наших Байесов
# https://habr.com/ru/articles/72301/
#
# https://pikabu.ru/story/paradoks_dney_rozhdeniya_175264
#
# https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%B4%D0%BE%D0%BA%D1%81_%D0%B4%D0%BD%D0%B5%D0%B9_%D1%80%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F
# ![image.png](attachment:image.png)

bd = pd.Series(range(365))

bd

t = bd.sample(23,replace=True)

t.duplicated()

t.duplicated().max()

rooms = [bd.sample(23,replace=True).duplicated().max() for _ in range(10000)]

rooms[:10]

np.mean(rooms)

rooms = [bd.sample(57,replace=True).duplicated().max() for _ in range(10000)]

np.mean(rooms)



rooms = [bd.sample(364,replace=True).duplicated().max() for _ in range(100000)]

np.mean(rooms)

# Экзамен проходит по следующей схеме: если некоторый билет уже был вытянут, то после ответа экзаменатор откладывает его в сторону. Студент выучил 20 билетов из 30. Когда ему выгоднее идти, первым или вторым, чтобы вероятность вынуть выученный билет была больше?
#
# https://ege-study.ru/teoriya-veroyatnostej/
# ![image.png](attachment:image.png)
#

tickets = list(range(1,31))

tickets

student = list(range(1,21))

student

from random import shuffle

tickets

shuffle(tickets)

tickets

3 in student

# +
n = 100000
student = list(range(1,21))
tickets = list(range(1,31))
result = []

for _ in range(n):
  shuffle(tickets)
  result.append(tickets[0] in student)
# -

np.mean(result)

# +
n = 100000
student = list(range(1,21))
tickets = list(range(1,31))
result = []

for _ in range(n):
  shuffle(tickets)
  result.append(tickets[1] in student)
# -

np.mean(result) # искажение Байесовского восприятия

# +
n = 100000
student = list(range(1,21))
tickets = list(range(1,31))
result = []

for _ in range(n):
  shuffle(tickets)
  result.append(tickets[2] in student)
# -

np.mean(result)

2 / 3

# Ночью произошло ДТП с участием такси. В городе работают две компании такси — «Синие» и «Зелёные». «Зелёным» принадлежит 85% такси, «Синим» 15%. Свидетель аварии утверждает, что такси принадлежало «Синим». Следственный эксперимент показал, что ночью свидетель верно определяет цвет такси в 80%. Какова вероятность того, что такси действительно принадлежало «Синим»?
#
#
#

# Интуитивные догадки большинства людей обычно далеки от истины. Удивительно, но, несмотря на показания свидетеля, вероятность того, что такси зелёное — 59%. Причина в том, что зелёных такси в городе много (85%) и этот факт «перевешивает» другую вероятность 80% уверенности свидетеля.
#
#
# К примеру, возьмём 100 типичных ДТП:
#
#
# 1) Из этих 100 ДТП будут участвовать 15 синих такси, и свидетель верно определит цвет для 80% из них (то есть для 15 * 0,8 = 12 такси свидетель скажет, что такси было синим)
#
#
# 2) В других 85 ДТП будет участвовать зеленое такси, и свидетель неверно определит цвет для 20% из них (то есть для 85 * 0,2 = 17 такси свидетель скажет, что такси было синим, когда оно на самом деле было зеленым)
#
#
# В итоге из 100 ДТП свидетель в 29 случаях скажет, что такси было синим. Но синим оно действительно будет только в 12 случаях из этих 29. Вероятность того, что такси действительно синее, 12 / 29 = 0,41 = 41%
#
#
# Из тех, кому предлагали решить эту задачу, значения между 20% и 70% назвали меньше половины. Большинство ответов было в районе 80%. Люди переоценивали значимость конкретного и ясного показания свидетеля и недооценивали тот факт, что синих такси в городе намного меньше зелёных.

np.random.binomial(1,0.15)
# 1 - синее
# 0 - зелёное

# генератор 
def witness(taxi) -> int:
  """Return witness testimony (0 or 1) given actual taxi color with 80%
  accuracy."""
  if np.random.binomial(1,0.8):
    return taxi
  return abs(taxi - 1)


witness(0)
# input 0 - зелёное, return 1 - синее, ошибся

#  monte carlo
n = 100000
result = []
for _ in range(n):
  taxi = np.random.binomial(1,0.15)
  witness_answer = witness(taxi)
  result.append((taxi,witness_answer))

result

t = pd.DataFrame(result, columns=['taxi','witness_answer'])
t

t.groupby('witness_answer')['taxi'].mean()
# 1    0.416681 41% случаев свидетель будет прав, что реально принадлежит синим 
# самое интересное что свидетель верно определяет в 80% случаев, получается это опять искажение Баейсовского восприятия

# Русская рулетка. Есть револьвер с 2 вставленными подряд патронами. Первый крутит барабан и стреляет и остается жив. Твоя очередь: тебе предлагает покрутить барабан перед выстрелом. Согласишься или сразу выстрелишь и почему?
# ![image.png](attachment:image.png)
# https://math.stackexchange.com/questions/849347/russian-roulette-should-a-player-pull-the-trigger-or-spin-the-cylinder

# ![image.png](attachment:image.png)

chamber = [1,1,0,0,0,0]

[1,0,0,0,0,1]


def one_turn(chamber) -> list:
  """Rotate chamber one position clockwise."""
  new_chamber = [0,0,0,0,0,0]
  n = len(chamber)
  for i in range(n):
    if i < n-1:
      new_chamber[i+1] = chamber[i]
    else:
      new_chamber[0] = chamber[i]
  return new_chamber


chamber = [1,1,0,0,0,0]

one_turn(chamber)

one_turn([0, 1, 1, 0, 0, 0])

one_turn([0, 0, 1, 1, 0, 0])

one_turn([0, 0, 0, 1, 1, 0])

one_turn([0, 0, 0, 0, 1, 1])

one_turn([1, 0, 0, 0, 0, 1])


def spin_chamber(chamber) -> list:
  """Randomly rotate chamber 1-6 positions clockwise."""
  n = np.random.randint(1,7)
  for _ in range(n):
    chamber = one_turn(chamber)
  return chamber


spin_chamber([1, 1, 0, 0, 0, 0])

pd.Series([spin_chamber([1, 1, 0, 0, 0, 0]) for _ in range(100000)]).astype(str).value_counts(normalize=True)

# +
# заряжаем револьвер
chamber = [1,1,0,0,0,0]
# первый игрок крутит барабан
chamber = spin_chamber(chamber)
# первый игрок стреляет
chamber = one_turn(chamber)
p1 = chamber[0]
chamber[0] = 0

# второй игрок вращает барабан -- нужно ли это действие?
chamber = spin_chamber(chamber)

# второй игрок стреляет
chamber = one_turn(chamber)
p2 = chamber[0]
# -

p1

p2

# +
n = 10000
result = []

for _ in range(n):
  # заряжаем револьвер
  chamber = [1,1,0,0,0,0]
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

  result.append((p1,p2))
# -

t = pd.DataFrame(result,columns=['p1','p2'])

t

t.groupby('p1')['p2'].agg(['count','mean'])
# 0 - выжил, первый игрок выжил, вероятность что 2 игрок умрет, если крутонешь барабан 0.33%
# 1 - умер

# +
n = 10000
result = []

for _ in range(n):
  # заряжаем револьвер
  chamber = [1,1,0,0,0,0]
  # первый игрок крутит барабан
  chamber = spin_chamber(chamber)
  # первый игрок стреляет
  chamber = one_turn(chamber)
  p1 = chamber[0]
  chamber[0] = 0

  # второй игрок не вращает барабан
  # chamber = spin_chamber(chamber)

  # второй игрок стреляет
  chamber = one_turn(chamber)
  p2 = chamber[0]

  result.append((p1,p2))
# -

t = pd.DataFrame(result,columns=['p1','p2'])

t.groupby('p1')['p2'].agg(['count','mean'])
# выгоднее не вращать барабан, чтобы выжил 2 игрок, вероятность смерти 25%
