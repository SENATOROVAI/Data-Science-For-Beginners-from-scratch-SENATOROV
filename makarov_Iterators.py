# ## Итераторы и генераторы

# ### Итерируемый объект и итератор

# #### Основные определения

# +
from collections.abc import Iterator
from itertools import chain, count, cycle

for i in [1, 2, 3]:
    print(i)
# -

# встроенная функция iter() вызывает метод .__iter__(),
# создающий итератор
iter([1, 2, 3])

# +
iterable_object = [1, 2, 3]

iterator = iter(iterable_object)
print(iterator)
print()

print(next(iterator))
print(next(iterator))
print(next(iterator))
# -

for iterator in iterable_object:
    print(iterator)

# +
iterable_object = [1, 2, 3]

iterator_a = iter(iterable_object)
iterator_b = iter(iterable_object)

print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"B: {next(iterator_b)}")
# -

iterable_object

# +
# print(f'A: {next(iterator_a)}')
# -

list(iterator_a), list(iterator_b)

for s in {1, 1, 2, 3}:
    print(s)

# #### Отсутствие "обратного хода"

# +
iterator_c = iter(iterable_object)

for i in iterator_c:
    print(i)
    break

for j in iterator_c:
    print(j)
# -

# #### Функция `zip()`

zip(iterable_object, iterable_object)

# +
iterator_tuple = zip(iterable_object, iterable_object)

print(next(iterator_tuple))
print(next(iterator_tuple))
print(next(iterator_tuple))
# -

for i in zip(iterable_object, iterable_object):
    print(i)


# #### Примеры итераторов

# Возведение в квадрат


class Square:
    def __init__(self, seq):
        self._seq = seq
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._seq):
            square = self._seq[self._idx] ** 2
            self._idx += 1
            return square
        else:
            raise StopIteration


square = Square([1, 2, 3, 4, 5])
square

for s in square:
    print(s)


# Счетчик


class Counter:
    def __init__(self, start=3, stop=9):
        self._current = start - 1
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self._current += 1
        if self._current < self._stop:
            return self._current
        else:
            raise StopIteration


counter = Counter()
counter

print(next(counter))
print(next(counter))

for c in counter:
    print(c)


# Класс Iterator модуля collections.abc


class Counter2(Iterator):
    def __init__(self, start=3, stop=9):
        self._current = start - 1
        self._stop = stop

    def __next__(self):
        self._current += 1
        if self._current < self._stop:
            return self._current
        else:
            raise StopIteration


for c in Counter2():
    print(c)


# Бесконечный итератор


class FibIterator:
    def __init__(self):
        self._idx = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._idx += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


# +
limit = 10

for f in FibIterator():
    print(f)
    limit -= 1
    if limit == 0:
        break


# -

# ### Генератор

# #### Простой пример


def sequence(n):
    res = [x for x in range(1, n + 1)]
    return res


sequence(5)


def sequence_gen(n):
    yield from range(1, n + 1)


sequence_gen(5)

# +
seq_5 = sequence_gen(5)

print(next(seq_5))
print(next(seq_5))
# -

for i in seq_5:
    print(i)

# +
# next(seq_5)
# -

# #### Generator comprehension

(x for x in range(1, 5 + 1))

list(x for x in range(1, 5 + 1))

sum(x for x in range(1, 5 + 1))

5 in (x for x in range(1, 5 + 1))

# ### Модуль itertools

# #### Функция `count()`

# +
natural_numbers = count(start=1, step=0.5)

for num in natural_numbers:
    print(num)
    if num == 2:
        break
# -

list_ = ["A", "B", "C", "D"]
for i in zip(count(), list_):
    print(i)


# +
def f(x):
    return x**2 + x - 2


f_x = map(f, count())
next(f_x)
# -

for val in f_x:
    print(val)
    if val > 10:
        break

# #### Функция `cycle()`

# +
list_ = [1, 2, 3]
iterator = cycle(list_)

limit = 5
for i in iterator:
    print(i)
    limit -= 1
    if limit == 0:
        break

# +
string = "Python"
iterator = cycle(string)

limit = 10
for i in iterator:
    print(i)
    limit -= 1
    if limit == 0:
        break
# -

# #### Функция `chain()`

iterator = chain(["abc", "d", "e", "f"], "abc", [1, 2, 3])
iterator

list(iterator)

list(chain.from_iterable(["abc", "def"]))

sum(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
