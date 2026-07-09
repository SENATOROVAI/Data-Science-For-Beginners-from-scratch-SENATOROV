"""Iterators and Generators."""

from collections.abc import Iterator
from itertools import chain, count, cycle

# Итерируемый объект и итератор

for i in [1, 2, 3]:
    print(i)

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

# +
iterable_object = [1, 2, 3]

iterator_a = iter(iterable_object)
iterator_b = iter(iterable_object)

print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"B: {next(iterator_b)}")
# -

print(list(iterator_a), list(iterator_b))

# +
# Функция zip()

zip(iterable_object, iterable_object)

# +
iterator_tuple = zip(iterable_object, iterable_object)

print(next(iterator_tuple))
print(next(iterator_tuple))
print(next(iterator_tuple))
# -

for pair in zip(iterable_object, iterable_object):
    print(pair)


# Примеры итераторов


class Square:
    """Итератор, возводящий элементы последовательности в квадрат."""

    def __init__(self, seq: list[int]) -> None:
        """Сохранить исходную последовательность и индекс."""
        self._seq = seq
        self._idx = 0

    def __iter__(self) -> "Square":
        """Вернуть сам объект как итератор."""
        return self

    def __next__(self) -> int:
        """Вернуть квадрат следующего элемента последовательности."""
        if self._idx < len(self._seq):
            square = self._seq[self._idx] ** 2
            self._idx += 1
            return square
        raise StopIteration


square_iter = Square([1, 2, 3, 4, 5])
square_iter

for square_value in square_iter:
    print(square_value)


# +
# Счетчик


class Counter:
    """Итератор-счетчик от start до stop."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Сохранить начальное и конечное значения счетчика."""
        self._current = start - 1
        self._stop = stop

    def __iter__(self) -> "Counter":
        """Вернуть сам объект как итератор."""
        return self

    def __next__(self) -> int:
        """Вернуть следующее значение счетчика."""
        self._current += 1
        if self._current < self._stop:
            return self._current
        raise StopIteration


# -

counter = Counter()
counter

print(next(counter))
print(next(counter))

for count_value in counter:
    print(count_value)

# +
# Класс Iterator модуля collections.abc


class Counter2(Iterator[int]):
    """Счетчик, реализованный через абстрактный класс Iterator."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Сохранить начальное и конечное значения счетчика."""
        self._current = start - 1
        self._stop = stop

    def __next__(self) -> int:
        """Вернуть следующее значение счетчика."""
        self._current += 1
        if self._current < self._stop:
            return self._current
        raise StopIteration


# -

for count_value in Counter2():
    print(count_value)


# +
# Бесконечный итератор


class FibIterator:
    """Бесконечный итератор чисел Фибоначчи."""

    def __init__(self) -> None:
        """Задать начальные значения последовательности Фибоначчи."""
        self._idx = 0
        self._current = 0
        self._next = 1

    def __iter__(self) -> "FibIterator":
        """Вернуть сам объект как итератор."""
        return self

    def __next__(self) -> int:
        """Вернуть следующее число Фибоначчи."""
        self._idx += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


# +
limit = 10

for fib_num in FibIterator():
    print(fib_num)
    limit -= 1
    if limit == 0:
        break


# -

# Генератор


def sequence(count_arg: int) -> list[int]:
    """Вернуть список чисел от 1 до count_arg включительно."""
    res = [x for x in range(1, count_arg + 1)]
    return res


sequence(5)


def sequence_gen(count_arg: int) -> Iterator[int]:
    """Сгенерировать числа от 1 до count_arg включительно."""
    yield from range(1, count_arg + 1)


sequence_gen(5)

# +
seq_5 = sequence_gen(5)

print(next(seq_5))
print(next(seq_5))
# -

for i in seq_5:
    print(i)

# Generator comprehension

print(x for x in range(1, 6))

list(x for x in range(1, 6))

# Модуль itertools

# +
# Функция count()

natural_numbers = count(start=1, step=0.5)

for num in natural_numbers:
    print(num)
    if num == 2:
        break


# +
def square_minus_two(value: int) -> int:
    """Вычислить value в квадрате плюс value минус два."""
    return value**2 + value - 2


f_x = map(square_minus_two, count())
next(f_x)
# -

for result in f_x:
    print(result)
    if result > 10:
        break

# +
# Функция cycle()

list_ = [1, 2, 3]
cycle_iterator_nums = cycle(list_)

limit = 5
for i in cycle_iterator_nums:
    print(i)
    limit -= 1
    if limit == 0:
        break

# +
string = "Python"
cycle_iterator_str = cycle(string)

limit = 10
for char in cycle_iterator_str:
    print(char)
    limit -= 1
    if limit == 0:
        break

# +
# Функция chain()

chain_iterator = chain(["abc", "d", "e", "f"], "abc", [1, 2, 3])
chain_iterator
# -

list(chain_iterator)

list(chain.from_iterable(["abc", "def"]))

sum(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
