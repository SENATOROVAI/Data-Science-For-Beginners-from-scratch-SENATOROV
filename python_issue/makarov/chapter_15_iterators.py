# +
"""Iterators and generators."""
from itertools import chain, count, cycle

# pylint: disable=invalid-name
# -

# ## Итерируемый объект и итератор
#

for value_1 in [1, 2, 3]:
    print(value_1)

temp_iterator = iter([1, 2, 3])
print(temp_iterator)

# +
iterable_object: list[int] = [1, 2, 3]

list_iterator = iter(iterable_object)
print(list_iterator)
print()

print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
# -

for element in iterable_object:
    print(element)

# +
iterable_numbers: list[int] = [1, 2, 3]

iterator_a = iter(iterable_numbers)
iterator_b = iter(iterable_numbers)

print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"B: {next(iterator_b)}")
# -

print(iterable_numbers)

iterator_a_list: list[int] = list(iterator_a)
iterator_b_list: list[int] = list(iterator_b)
print(iterator_a_list, iterator_b_list)

for number_value in [1, 1, 2, 3]:
    print(number_value)

# ## Отсутствие "обратного хода"
#

# +
iterator_c = iter(iterable_numbers)

for first_item in iterator_c:
    print(first_item)
    break

for remaining_item in iterator_c:
    print(remaining_item)
# -

# ## Функция zip()
#

zipped_pairs = zip(iterable_numbers, iterable_numbers)
print(zipped_pairs)

# +
iterator_tuple = zip(iterable_numbers, iterable_numbers)

print(next(iterator_tuple))
print(next(iterator_tuple))
print(next(iterator_tuple))
# -

for pair in zip(iterable_numbers, iterable_numbers):
    print(pair)


# ## Примеры итераторов
# ### Возведение в квадрат
#


class Square:
    """Iterator returning squared values from a sequence."""

    def __init__(self, seq: list[int] | tuple[int, ...]) -> None:
        """Initialize iterator with sequence."""
        self._seq = seq
        self._idx = 0

    def __iter__(self):  # type: ignore[no-untyped-def]
        """Return self as iterator."""
        return self

    def __next__(self) -> int:
        """Return next squared value or raise StopIteration."""
        if self._idx >= len(self._seq):
            raise StopIteration
        square_result: int = self._seq[self._idx] ** 2
        self._idx += 1
        return square_result


square_iterator: Square = Square([1, 2, 3, 4, 5])
print(square_iterator)

for square_value in square_iterator:
    print(square_value)


# ## Счетчик
#


class Counter:
    """Simple iterator that counts from start up to stop (exclusive)."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Initialize with bounds."""
        self._current = start - 1
        self._stop = stop

    def __iter__(self):  # type: ignore[no-untyped-def]
        """Return self as iterator."""
        return self

    def __next__(self) -> int:
        """Return next number or raise StopIteration."""
        self._current += 1
        if self._current >= self._stop:
            raise StopIteration
        return self._current


counter_instance: Counter = Counter()
print(counter_instance)

print(next(counter_instance))
print(next(counter_instance))

for count_value in counter_instance:
    print(count_value)


# ## Класс Iterator модуля collections.abc
#


class Counter2:
    """Iterator implementing the Iterator protocol explicitly."""

    def __init__(self, start: int = 3, stop: int = 9) -> None:
        """Initialize with bounds."""
        self._current = start - 1
        self._stop = stop

    def __iter__(self):  # type: ignore[no-untyped-def]
        """Return self as iterator."""
        return self

    def __next__(self) -> int:
        """Return next number or raise StopIteration."""
        self._current += 1
        if self._current >= self._stop:
            raise StopIteration
        return self._current


for count_value in Counter2():
    print(count_value)


# ## Бесконечный итератор
#


class FibIterator:
    """Iterator producing Fibonacci numbers."""

    def __init__(self) -> None:
        """Initialize starting values."""
        self._idx = 0
        self._current = 0
        self._next = 1

    def __iter__(self):  # type: ignore[no-untyped-def]
        """Return self as iterator."""
        return self

    def __next__(self) -> int:
        """Return next Fibonacci number."""
        if self._idx < 0:
            raise StopIteration
        self._idx += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


# +
fib_limit: int = 10

for fib_value in FibIterator():
    print(fib_value)
    fib_limit -= 1
    if fib_limit == 0:
        break


# -

# ## Генератор
#


# +
def sequence(count_limit: int) -> list[int]:
    """Return list of integers from 1 to n inclusive."""
    res: list[int] = [x for x in range(1, count_limit + 1)]
    return res


sequence(5)


# +
def sequence_gen(count_limit: int):  # type: ignore[no-untyped-def]
    """Yield integers from 1 to n inclusive."""
    yield from range(1, count_limit + 1)


sequence_gen(5)

# +
seq_5 = sequence_gen(5)

print(next(seq_5))
print(next(seq_5))
# -

for number in seq_5:
    print(number)

# ## Generator comprehension
#

gen_expr = (x for x in range(1, 5 + 1))
print(gen_expr)

gen_expr_list: list[int] = list(x for x in range(1, 5 + 1))
print(gen_expr_list)

sum_gen: int = sum(x for x in range(1, 5 + 1))
print(sum_gen)

contains_value: bool = 5 in (x for x in range(1, 5 + 1))
print(contains_value)

# ## Модуль itertools
#

# ## Функция count()
#

# +
natural_numbers = count(start=1, step=0.5)

for num in natural_numbers:
    print(num)
    if num == 2:
        break
# -

list_let: list[str] = ["a", "b", "c", "d"]
for enumerated_letter in zip(count(start=1), list_let):
    print(enumerated_letter)


# +
def quadratic(value: int | float) -> float:
    """Return quadratic expression result."""
    return value**2 + value - 2


f_x = map(quadratic, count())
print(next(f_x), next(f_x), next(f_x))
# -

for mapped_value in f_x:
    print(mapped_value)
    if mapped_value > 10:
        break

# ??????? ???????? ? ???????????? ?? ???????.
#

# ???? ?? ?????? ? ?????????????? cycle (?????? ????).
#

# +
cycle_numbers: list[int] = [1, 2, 3]
cycle_iterator_numbers = cycle(cycle_numbers)

cycle_nums_limit: int = 5
for number in cycle_iterator_numbers:
    print(number)
    cycle_nums_limit -= 1
    if cycle_nums_limit == 0:
        break

# +
string_value: str = "Python"
cycle_iterator_chars = cycle(string_value)

cycle_chars_limit: int = 10
for char in cycle_iterator_chars:
    print(char)
    cycle_chars_limit -= 1
    if cycle_chars_limit == 0:
        break
# -

chain_iterator = chain(["abc", "d", "e", "f"], "abc", [1, 2, 3])
print(chain_iterator)

# ????????? ???????? ????????? chain ???????.
#

flatten_letters: list[str] = list(chain.from_iterable(["abc", "def"]))
print(flatten_letters)

sum_numbers: int = sum(chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sum_numbers)
