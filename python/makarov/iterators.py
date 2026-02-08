"""Итераторы."""

# ## Итераторы и генераторы

# ### Итерируемый объект и итератор

# #### Основные определения

# +
from collections.abc import Generator, Iterator
from itertools import chain, count, cycle

for i in [1, 2, 3]:
    print(i)
# -

# создание итератора
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

for i in iterable_object:
    print(i)

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

print(list(iterator_a), list(iterator_b))

# #### Отсутствие "обратного хода"

# +
iterator_c = iter(iterable_object)

for i in iterator_c:
    print(i)
    break

for i in iterator_c:
    print(i)
# -

# #### Функция `zip()`

zip(iterable_object, iterable_object)

# +
iterator_tuple = zip(iterable_object, iterable_object)

print(next(iterator_tuple))
print(next(iterator_tuple))
print(next(iterator_tuple))
# -

for tup1 in zip(iterable_object, iterable_object):
    print(tup1)


# #### Примеры итераторов

# Возведение в квадрат


class Square:
    """Квадрат."""

    def __init__(self, seq: list[int]) -> None:
        """Создание экземпляра.

        Args:
            seq (list[int]): Последовательность
        """
        self._seq = seq
        self._idx = 0

    def __iter__(self) -> Iterator[int]:
        """Итератор."""
        return self

    def __next__(self) -> int:
        """Переход к следующей итерации.

        Raises:
            StopIteration: Остановка итерации

        Returns:
            int|float: Элемент последовательности в квадрате.
        """
        if self._idx < len(self._seq):
            sq = self._seq[self._idx] ** 2
            self._idx += 1
            return sq
        raise StopIteration


square = Square([1, 2, 3, 4, 5])
square

for num in square:
    print(num)


# Счётчик


class Counter:
    """Счётчик."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Создание экземпляра.

        Args:
            start (int): Начальное значение счётчика (стандартно 3)
            stop (int): Конечное значение счётчика (стандартно 9)
        """
        self._current = start - 1
        self._stop = stop

    def __iter__(self) -> Iterator[int]:
        """Итератор."""
        return self

    def __next__(self) -> int:
        """Переход к следующему шагу."""
        self._current += 1
        if self._current < self._stop:
            return self._current
        raise StopIteration


counter = Counter()
counter

print(next(counter))
print(next(counter))

for i in counter:
    print(i)


# Класс Iterator модуля collections.abc


class Counter2(Iterator[int]):
    """Счётчик.

    Args:
        Iterator[int]: Родительский класс, позволяющий опустить __call__
    """

    def __init__(self, start: int = 3, stop: int = 9):
        """Создание экземпляра.

        Args:
            start (int): Начальное значение счётчика (стандартно 3)
            stop (int): Конечное значение счётчика (стандартно 9)
        """
        self._current = start - 1
        self._stop = stop

    def __next__(self) -> int:
        """Переход к следующему шагу."""
        self._current += 1
        if self._current < self._stop:
            return self._current
        raise StopIteration


for i in Counter2():
    print(i)


# Бесконечный итератор


class FibIterator:
    """Итератор по числам Фибоначчи."""

    def __init__(self) -> None:
        """Создание экземпляра."""
        self._idx = 0
        self._current = 0
        self._next = 1

    def __iter__(self) -> Iterator[int]:
        """Итератор."""
        return self

    def __next__(self) -> int:
        """Переход к следующему шагу."""
        self._idx += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


# +
limit = 10

for i in FibIterator():
    print(i)
    limit -= 1
    if limit == 0:
        break


# -

# ### Генератор

# #### Простой пример


def sequence(length: int) -> list[int]:
    """Генерация последовательности."""
    res = [x for x in range(1, length + 1)]
    return res


sequence(5)


def sequence_gen(length: int) -> Generator[int, None, None]:
    """Генерация итератора."""
    yield from range(1, length + 1)


sequence_gen(5)

# +
seq_5 = sequence_gen(5)

print(next(seq_5))
print(next(seq_5))
# -

for i in seq_5:
    print(i)

# #### Generator comprehension

print(x for x in range(1, 5 + 1))

list(x for x in range(1, 5 + 1))

sum(x for x in range(1, 5 + 1))

print(5 in (x for x in range(1, 5 + 1)))

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
for tup in zip(count(), list_):
    print(tup)


# +
def f(num1: int) -> float | int:
    """Математическое выражение.

    Args:
        num1 (int): Исходное число

    Returns:
        float | int: Результат
    """
    return num1**2 + num1 - 2


f_x = map(f, count())
next(f_x)
# -

for value in f_x:
    print(value)
    if value > 10:
        break

# #### Функция `cycle()`

# +
list1_ = [1, 2, 3]
iterator = cycle(list1_)

limit = 5
for i in iterator:
    print(i)
    limit -= 1
    if limit == 0:
        break

# +
string = "Python"
iterator1 = cycle(string)

limit = 10
for value1 in iterator1:
    print(value1)
    limit -= 1
    if limit == 0:
        break
# -

# #### Функция `chain()`

iterator = chain([3, 5], [1, 2, 3])
iterator

list(iterator)

list(chain.from_iterable(["abc", "def"]))

sum(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#
