"""Макаров.

Итераторы и генераторы.
"""

# ## Итераторы и генераторы

# ### Итерируемый объект и итератор

# #### Основные определения

# +
from collections.abc import Iterator
from itertools import chain, count, cycle
from typing import Generator

for index in [1, 2, 3]:
    print(index)
# -

# встроенная функция iter() вызывает метод .__iter__(),
# создающий итератор
iterator1 = iter([1, 2, 3])

# +
iterable_object: list[int] = [1, 2, 3]

iterator = iter(iterable_object)
print(iterator)
print()

print(next(iterator))
print(next(iterator))
print(next(iterator))
# -

for iterator2 in iterable_object:
    print(iterator2)

# +
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

print(list(iterator_a), list(iterator_b))

for item_s in {1, 1, 2, 3}:  # pylint: disable=C0208,W0130
    print(item_s)

# #### Отсутствие "обратного хода"

# +
iterator_c = iter(iterable_object)

for item_c_1 in iterator_c:
    print(item_c_1)
    break

for item_c_2 in iterator_c:
    print(item_c_2)
# -

# #### Функция `zip()`

iterator_tuple = zip(iterable_object, iterable_object)
print(iterator_tuple)

print(next(iterator_tuple))
print(next(iterator_tuple))
print(next(iterator_tuple))

for item_z in zip(iterable_object, iterable_object):
    print(item_z)


# #### Примеры итераторов

# Возведение в квадрат

class Square:
    """Итератор, возводящий в квадрат числа из переданной последовательности."""

    def __init__(self, seq: list[int]) -> None:
        """Инициализация итератора."""
        self._seq = seq
        self._idx = 0

    def __iter__(self) -> "Square":
        """Возвращает сам объект как итератор."""
        return self

    def __next__(self) -> int:
        """Возвращает следующее значение итератора."""
        if self._idx < len(self._seq):
            square = self._seq[self._idx] ** 2
            self._idx += 1
            return square

        raise StopIteration


square_1 = Square([1, 2, 3, 4, 5])
print(square_1)

for num_square in square_1:
    print(num_square)


# Счетчик

class Counter:
    """Итератор, генерирующий последовательность целых чисел в заданном диапазоне."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Инициализирует итератор с заданными границами диапазона."""
        self._current = start - 1
        self._stop = stop

    def __iter__(self) -> "Counter":
        """Возвращает сам объект как итератор."""
        return self

    def __next__(self) -> int:
        """Возвращает следующее значение в последовательности."""
        self._current += 1
        if self._current < self._stop:
            return self._current

        raise StopIteration


counter = Counter()
print(counter)

print(next(counter))
print(next(counter))

for current_count in counter:
    print(current_count)


# Класс Iterator модуля collections.abc

class Counter2(Iterator[int]):
    """Итератор.

    Генерирует последовательность целых чисел в заданном диапазоне.
    """

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Инициализирует итератор с заданными границами диапазона."""
        self._current = start - 1
        self._stop = stop

    def __next__(self) -> int:
        """Возвращает следующее значение в последовательности."""
        self._current += 1
        if self._current < self._stop:
            return self._current

        raise StopIteration


for current_count in Counter2():
    print(current_count)


# Бесконечный итератор

class FibIterator:
    """Бесконечный Итератор.

    Генерирует последовательность целых чисел, начиная с 0.
    """

    def __init__(self) -> None:
        """Инициализирует итератор."""
        self._idx = 0
        self._current = 0
        self._next = 1

    def __iter__(self) -> "FibIterator":
        """Возвращает сам объект как итератор."""
        return self

    def __next__(self) -> int:
        """Возвращает следующее значение в последовательности."""
        self._idx += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


# +
limit = 10

for item_f in FibIterator():
    print(item_f)
    limit -= 1
    if limit == 0:
        break


# -

# ### Генератор

# #### Простой пример

def sequence(end: int) -> list[int]:
    """Возвращает список целых чисел от 1 до n включительно."""
    res = [num for num in range(1, end + 1)]
    return res


print(sequence(5))


def sequence_gen(num_arg: int) -> Generator[int, None, None]:
    """Генератор, возвращающий целые числа от 1 до n включительно."""
    yield from range(1, num_arg + 1)


print(sequence_gen(5))

# +
seq_5 = sequence_gen(5)

print(next(seq_5))
print(next(seq_5))
# -

for item_s in seq_5:
    print(item_s)

# +
# next(seq_5)
# -

# #### Generator comprehension

print(num for num in range(1, 5 + 1))

print(list(num for num in range(1, 5 + 1)))

print(sum(num for num in range(1, 5 + 1)))

print(5 in (num for num in range(1, 5 + 1)))

# ### Модуль itertools

# #### Функция `count()`

# +
natural_numbers = count(start=1, step=0.5)

for num in natural_numbers:
    print(num)
    if num == 2:
        break
# -

list_: list[str] = ["A", "B", "C", "D"]
for item_1 in zip(count(), list_):
    print(item_1)


# +
def quadratic_poly(num_arg: int) -> int:
    """Вычисляет значение квадратичной функции f(x) = x² + x - 2."""
    return num_arg**2 + num_arg - 2


f_x = map(quadratic_poly, count())
next(f_x)
# -

for value in f_x:
    print(value)
    if value > 10:
        break

# #### Функция `cycle()`

# +
list_1: list[int] = [1, 2, 3]
iterator_d = cycle(list_1)

limit = 5
for item_2 in iterator_d:
    print(item_2)
    limit -= 1
    if limit == 0:
        break

# +
string = "Python"
iterator_e = cycle(string)

limit = 10
for item_3 in iterator_e:
    print(item_3)
    limit -= 1
    if limit == 0:
        break
# -

# #### Функция `chain()`

iterator_f = chain(["abc", "d", "e", "f"], "abc", [1, 2, 3])
print(iterator_f)

print(list(iterator))

print(list(chain.from_iterable(["abc", "def"])))

result_1 = sum(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


