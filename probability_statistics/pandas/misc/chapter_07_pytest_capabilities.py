"""Pytest capabilities."""

# # Возможности pytest

# - установите `pytest`
# - установите `pytest-sugar`, который предоставляет более приятный результат

# !pip -q install pytest pytest-sugar.

# +
# перейти в директорию tdd
from pathlib import Path

import pytest
from pytest import approx

if Path.cwd().name != "tdd":
    # %mkdir tdd
    # %cd tdd

# %pwd
# -

# очистка файлов
# %rm *.py

# # Как pytest обнаруживает тесты
#
# `pytest` использует следующие соглашения для автоматического обнаружения тестов:
#
# - файлы с тестами должны называться `test_*.py` или `*_test.py`
# - имя тестовой функции должно начинаться с `test_`

# # Наш первый тест
#
# чтобы увидеть, работает ли наш код, мы можем использовать ключевое слово `assert`. `pytest` добавляет хуки, чтобы сделать их более полезными

# +
# %%file test_math.py

import math
def test_add() -> None:
    """Проверяет сложение."""
    assert 1 + 1 == 2


def test_mul() -> None:
    """Проверяет умножение."""
    assert 6 * 7 == 42


def test_sin() -> None:
    """Проверяет значение sin(0)."""
    assert math.sin(0) == 0


# -

# !python -m pytest test_math.py

# мы только что написали 3 теста, которые показывают, что базовая математика все еще работает
#
# Ура!

# # Задание 1
#
# напишите тест для следующей функции.
#
# если есть ошибка в функции, исправьте ее

# +
# %%file make_triangle.py

# версия 1

from typing import Iterator

def make_triangle(a_var: int) -> Iterator[str]:
    """
    рисует треугольник, используя буквы '@'
    например:
        >>> print('\n'.join(make_triangle(3))
        @
        @@
        @@@
    """

    for i in range(a_var):
        yield '@' * i

    """
    рисует треугольник, используя буквы '@'
    например:
        >>> print('\n'.join(make_triangle(3))
        @
        @@
        @@@
    """

    for i in range(a_var):
        yield '@' * i


# -

# ## Решение 1

# +
# %%file test_make_triangle.py

from make_triangle import make_triangle

def test_make_triangle() -> None:
    """Проверяет генерацию треугольника из '@' при n=1."""
    expected = "@"
    actual = '\n'.join(make_triangle(1))
    assert actual == expected


# -

# !python -m pytest test_make_triangle.py

# и так ожидаемое начинается с `'@'`, а фактическое с `''`...
#
# это ошибка! давайте исправим код и перезапустим его

# +
# %%file make_triangle.py

# версия 2

def make_triangle(b_var: int) -> Iterator[str]:
    """
    рисует треугольник, используя буквы '@'
    например:
        >>> print('\n'.join(make_triangle(3))
        @
        @@
        @@@
    """

    for i in range(1, b_var + 1):
        yield '@' * i


# -

# !python -m pytest test_make_triangle.py

# # контекстно-зависимые сравнения
#
# `pytest` имеет богатую поддержку для предоставления контекстно-зависимой информации при сравнении.
#
# Специальные сравнения проводятся для ряда случаев:
#
# - сравнение длинных строк: показывается разница контекста
# - сравнение длинных последовательностей: первые неудачные индексы
# - сравнение словарей: разные записи
#
# Вот как это выглядит для множества:

# +
# %%file test_compare_fruits.py

def test_set_comparison() -> None:
    """
    Проверяет, что два множества фруктов идентичны
    независимо от порядка элементов.
    """
    set1: set[str] = {
        "Apples",
        "Bananas",
        "Watermelon",
        "Pear",
        "Guave",
        "Carambola",
        "Plum",
    }

    set2: set[str] = {
        "Plum",
        "Apples",
        "Grapes",
        "Watermelon",
        "Pear",
        "Guave",
        "Carambola",
        "Melon",
    }

    assert set1 == set2


# -

# !python -m pytest test_compare_fruits.py

# # Задание 2
#
# протестируйте следующую функцию `count_words()` и исправьте все ошибки.
#
# ожидаемый результат функции указан в `expected_output`

expected_output = {
    "and": 2,
    "chief": 2,
    "didnt": 1,
    "efficiency": 1,
    "expected": 1,
    "expects": 1,
    "fear": 2,
    "i": 1,
    "inquisition": 2,
    "is": 1,
    "no": 1,
    "one": 1,
    "our": 1,
    "ruthless": 1,
    "spanish": 2,
    "surprise": 3,
    "the": 2,
    "two": 1,
    "weapon": 1,
    "weapons": 1,
    "well": 1,
}

# +
# %%file spanish_inquisition.py

# версия 1: с багами

import collections

quote = """
Well, I didn't expected the Spanish Inquisition ...
No one expects the Spanish Inquisition!
Our chief weapon is surprise, fear and surprise;
two chief weapons, fear, surprise, and ruthless efficiency!
"""

def remove_punctuation(quote: str) -> str:
    """Убирает знаки пунктуации и приводит строку к нижнему регистру."""
    quote.translate(str.maketrans('', '', "',.!?;")).lower()
    return quote

def count_words(quote: str) -> Dict[str, int]:
    """
    Возвращает словарь {слово: количество} для переданного текста.
    Пунктуация предварительно удаляется, разделение по пробельным символам.
    """
    quote = remove_punctuation(quote)
    return dict(collections.Counter(quote.split(' ')))


# -

# ## Решение 2

# +
# %%file test_spanish_inquisition.py

from spanish_inquisition import *

expected_output = {
 'and': 2,
 'chief': 2,
 'didnt': 1,
 'efficiency': 1,
 'expected': 1,
 'expects': 1,
 'fear': 2,
 'i': 1,
 'inquisition': 2,
 'is': 1,
 'no': 1,
 'one': 1,
 'our': 1,
 'ruthless': 1,
 'spanish': 2,
 'surprise': 3,
 'the': 2,
 'two': 1,
 'weapon': 1,
 'weapons': 1,
 'well': 1}

def test_spanish_inquisition() -> None:
    """Проверяет корректный подсчёт слов в тексте про испанскую инквизицию."""
    actual = count_words(quote)
    assert actual == expected_output


# +
# %%file spanish_inquisition.py

# версия 2: исправленная

import collections

quote = """
Well, I didn't expected the Spanish Inquisition ...
No one expects the Spanish Inquisition!
Our chief weapon is surprise, fear and surprise;
two chief weapons, fear, surprise, and ruthless efficiency!
"""

def remove_punctuation(quote: str) -> str:
    """Удаляет пунктуацию и приводит строку к нижнему регистру."""
    # quote.translate(str.maketrans('', '', "',.!?;")).lower() # BUG: пропущен return
    return quote.translate(str.maketrans('', '', "',.!?;")).lower()

def count_words(quote: str) -> Dict[str, int]:
    """Возвращает частоты слов, разделённых пробелами/пробельными символами."""
    quote = remove_punctuation(quote)
    # return dict(collections.Counter(quote.split(' '))) # BUG
    return dict(collections.Counter(quote.split()))


# -

# !python -m pytest -vv test_spanish_inquisition.py

# # Использование фикстур для упрощения тестов

# ## Мотивирующий пример
#
# Давайте посмотрим на пример класса `Person`, где каждый человек имеет имя и помнит своих друзей.

# +
# %%file person.py

# версия 1

from __future__ import annotations
from typing import Set


class Person:
    """Человек с именем, любимым цветом, годом рождения и списком друзей."""

    def __init__(self, name: str, favorite_color: str, year_born: int) -> None:
        """Создаёт объект Person."""
        self.name: str = name
        self.favorite_color: str = favorite_color
        self.year_born: int = year_born
        self.friends: Set[Person] = set()

    def add_friend(self, other_person: Person) -> None:
        """Добавляет двустороннюю дружбу между двумя людьми."""
        if not isinstance(other_person, Person):
            raise TypeError(f"{other_person!r} is not a Person")
        self.friends.add(other_person)
        other_person.friends.add(self)

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        friends_list = [f.name for f in self.friends]
        return (
            f"Person(name={self.name!r}, "
            f"favorite_color={self.favorite_color!r}, "
            f"year_born={self.year_born!r}, "
            f"friends={friends_list})"
        )


# -

# Давайте напишем тест для функции `add_friend()`.
#
# обратите внимание, как `setup` для теста берет на себя так много функций, а также требует изобретать много повторяющихся данных
#
# есть ли способ уменьшить этот шаблонный код

# +
# %%file test_person.py

from person import Person

def test_name() -> None:
    """Проверяет, что поле name задано корректно."""
    # setup
    terry = Person(
        'Terry Gilliam',
        'red',
        1940
        )

    # test
    assert terry.name == 'Terry Gilliam'


def test_add_friend() -> None:
    """Проверяет, что добавление друга работает в обе стороны."""
    # setup для тестирования
    terry = Person(
        'Terry Gilliam',
        'red',
        1940
        )
    eric = Person(
        'Eric Idle',
        'blue',
        1943
        )

    # актуальный test
    terry.add_friend(eric)
    assert eric in terry.friends
    assert terry in eric.friends


# -

# !python -m pytest -q test_person.py

# # Фикстуры спешат на помощь

# если у нас была бы волшебная фабрика, которая может вызвать имя, любимый цвет и год рождения?
#
# тогда мы могли бы написать наш `test_name()` более просто:

# ```python
# def test_name(person_name, favorite_color, birth_year):
#     person = Person(person_name, favorite_color, birth_year)
#
#     # test
#     assert person.name == person_name
# ```

# кроме того, если бы у нас была волшебная фабрика, которая может создавать `eric` и `terry`, мы могли бы написать нашу функцию `test_add_friend()` следующим образом:

# ```python
# def test_add_friend(eric, terry):
#     eric.add_friend(terry)
#     assert eric in terry.friends
#     assert terry in eric.friends
# ```

# фикстуры в `pytest` позволяют нам создавать такие волшебные фабрики, используя нотацию `@pytest.fixture`.
#
# вот пример:

# +
# %%file test_person_fixtures1.py

import pytest
from person import Person

@pytest.fixture
def person_name() -> str:
    """Возвращает имя человека для тестов."""
    return 'Terry Gilliam'

@pytest.fixture
def birth_year() -> int:
    """Возвращает год рождения человека для тестов."""
    return 1940

@pytest.fixture
def favorite_color() -> str:
    """Возвращает любимый цвет человека для тестов."""
    return 'red'

def test_person_name(person_name: str, favorite_color: str, birth_year: int) -> None:
    """Проверяет корректность имени при создании Person."""
    person = Person(person_name, favorite_color, birth_year)
    # test
    assert person.name == person_name


# -

# !python -m pytest test_person_fixtures1.py

# что тут происходит?
#
# `pytest` видит, что тестовая функция `test_person_name(person_name, favorite_color, birth_year)` требует три параметра, и ищет фикстуры с аннотацией `@pytest.fixture` с тем же именем.
#
# когда он их находит, он вызывает эти фикстуры от нашего имени и передает возвращаемое значение в качестве параметра. по сути, он вызывает

# ```
# test_person_name(person_name=person_name(), favorite_color=favorite_color(), birth_year=birth_year()
# ```

# обратите внимание, сколько кода это экономит

# # Задание 3
#
# - перепишите функцию `test_add_friend`, чтобы она принимала два параметра: `def test_add_friend(eric, terry)`
# - напишите фикстуры для `eric` и `terry`
# - запустите pytest

# ## Решение 3

# +
# %%file test_person_fixtures2.py

import pytest
from person import Person

@pytest.fixture
def eric() -> Person:
    """Фикстура: создаёт Person Эрика Idle."""
    return Person('Eric Idle', 'red', 1943)

@pytest.fixture
def terry() -> Person:
    """Фикстура: создаёт Person Терри Gilliam."""
    return Person('Terry Gilliam', 'blue', 1940)

def test_add_friend(eric: Person, terry: Person) -> None:
    """Проверяет двустороннее добавление друзей между Eric и Terry."""
    eric.add_friend(terry)
    assert eric in terry.friends
    assert terry in eric.friends


# -

# !python -m pytest -q test_person_fixtures2.py

# # параметризация фикстур
#
# функции фикстур могут быть параметризованы, и в этом случае они будут вызываться несколько раз, каждый раз выполняя набор зависимых тестов, т.е. тесты, которые зависят от этой фикстуры.
#
# Тестовые функции обычно не должны знать о своем повторном запуске. Параметризация фикстур помогает писать исчерпывающие функциональные тесты для компонентов, которые сами по себе могут быть сконфигурированы несколькими способами.

# +
# %%file test_primes.py

import pytest
import math

def is_prime(c_var: int) -> bool:
    """Проверяет, является ли число простым."""
    return all(x % factor != 0 for factor in range(2, int(c_var/2)))

@pytest.fixture(params=[2, 3, 5, 7, 11, 13, 17, 19, 101])
def prime_number(request) -> int:
    """Фикстура для простых чисел."""
    return int(request.param)

def test_prime(prime_number: int) -> None:
    """Проверяет, что числа из фикстуры действительно простые."""
    assert is_prime(prime_number) == True


# -

# !python -m pytest --verbose test_primes.py

# # Задание 4
#
# Напишите тест `is_prime()` для не простых чисел
#
#     дополнительно: можете ли вы найти и исправить ошибку в is_prime() с помощью теста?

# ## Решение 4

# +
# fmt: off

# %%file test_non_primes.py

fix_bug = True

if fix_bug:
    def is_prime_func(d_var: int) -> bool:
        """Проверяет, является ли число простым (исправленная версия)."""
        # notice the +1 - it is important when x=4
        return all(
            d_var % factor != 0 
            for factor in range(2, int(d_var / 2) + 1)
        )
else:
    from test_primes import is_prime as def is_prime_func


@pytest.fixture(
    params=[
        4, 6, 8, 9, 10, 12, 14, 15, 16, 28, 60, 100
    ]  # type: ignore[misc]
)
def non_prime_number(request: pytest.FixtureRequest) -> int:  # type: ignore[misc]
    """Фикстура для непростых чисел."""
    return request.param  # type: ignore[no-any-return]


def test_non_primes(np_number: int) -> None:
    """Проверяет, что числа из фикстуры действительно не простые."""
    assert not is_prime_func(np_number)

# fmt: on


# -

# !python -m pytest --verbose test_non_primes.py

all(factor for factor in range(2, int(4 / 2)))

# !python -m pytest --verbose test_primes.py

# # печать и логирование в тестах
#
# ## печать
#
# Вы можете использовать печать в тестах для предоставления дополнительной отладочной информации.
#
# `pytest` перенаправляет вывод и захватывает вывод каждого теста. тогда:
#
# - подавляет вывод всех успешных тестов (для краткости)
# - показывает вывод всех неудачных тестов (для отладки)
# - оба `stdout` и `stderr` захвачены

# +
# %%file test_prints.py
import sys

def test_print_success() -> None:
    """Пример успешного теста с print (stdout)."""
    print(
        """
        @@@@@@@@@@@@@@@
        this statement will NOT be printed
        @@@@@@@@@@@@@@@
        """
    )

    assert 6*7 == 42

def test_print_fail() -> None:
    """Пример неуспешного теста с print (stdout)."""
    print(
        """
        @@@@@@@@@@@@@@@
        this statement WILL be printed
        @@@@@@@@@@@@@@@
        """
    )
    assert True == False


def test_stderr_capture_success() -> None:
    """Пример успешного теста с print (stderr)."""
    print(
        """
        @@@@@@@@@@@@@@@
        this STDERR statement will NOT be printed
        @@@@@@@@@@@@@@@
        """,
        file=sys.stderr
    )

    assert True


def test_stderr_capture_fail() -> None:
    """Пример неуспешного теста с print (stderr)."""
    print(
        """
        @@@@@@@@@@@@@@@
        this STDERR statement WILL be printed
        @@@@@@@@@@@@@@@
        """,
        file=sys.stderr
    )

    assert False


# -

# !python -m pytest -q test_prints.py

# ## логирование
#
# pytest автоматически фиксирует сообщения журнала уровня `WARNING` или выше и отображает их в отдельном разделе для каждого неудавшегося теста так же, как захваченные `stdout` и `stderr`.
#
#      `WARNING` и выше будут отображаться для неудачных тестов.
#      `INFO` и ниже не будут отображаться
#
# пример:

# +
# %%file test_logging.py

import logging

logger = logging.getLogger(__name__)

def test_logging_warning_success() -> None:
    """Пример успешного теста с логированием WARNING."""
    logger.warning('\n\n @@@ this will NOT be printed \n\n')
    assert True

def test_logging_warning_success() -> None:
    """Пример успешного теста с логированием WARNING."""
    logger.warning('\n\n @@@ this WILL be printed @@@ \n\n')
    assert False

def test_logging_warning_success() -> None:
    """Пример успешного теста с логированием WARNING."""
    logger.info('\n\n @@@ this will NOT be printed @@@ \n\n')
    assert False


# -

# !python -m pytest test_logging.py

# # Задание 5
#
# Ниже мы приводим реализацию головоломки `FizzBuzz`:
#
# Напишите функцию, которая возвращает числа от 1 до 100. Но для чисел, кратных трем, вместо числа будет возвращено `Fizz`, а для чисел, кратных пяти, — `Buzz`. Для чисел, кратных как трем, так и пяти, возвращайте `FizzBuzz`.
#
# таким образом, это ДОЛЖНО быть правдой

# ```python
# fizzbuzz()  # should return the following (abridged) output
# [1, 2, "Fizz", 4, "Buzz", 6, 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", ...]
# ```

# НО реализация глючная. можете ли вы написать тесты для него и исправить это?

# +
# %%file fizzbuzz.py
from typing import List, Union


def is_multiple(n: int, divisor: int) -> bool:
    """Проверяет, делится ли n на divisor без остатка."""
    return n % divisor == 0

def fizzbuzz() -> List[Union[int, str]]:
    """
    expected output: list with elements numbers
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', ... ]
    """
    result = []
    for i in range(100):
        if is_multiple(i, 3):
            return "Fizz"
        if is_multiple(i, 5):
            return "Buzz"
        if is_multiple(i, 3) and is_multiple(i, 5):
            return "FizzBuzz"
        return i

    return result


# -

# ## Решение 5

# +
fix_bug = 1  

if not fix_bug:
    from fizzbuzz import fizzbuzz
else:

    def fizzbuzz_fixed() -> list[str | int]:
        """Исправленная версия FizzBuzz от 1 до 100."""

        def translate(e_var: int) -> str | int:
            """Возвращает 'Fizz', 'Buzz', 'FizzBuzz' или само число для i."""
            if e_var % 3 == 0 and e_var % 5 == 0:
                return "FizzBuzz"
            if e_var % 3 == 0:
                return "Fizz"
            if e_var % 5 == 0:
                return "Buzz"
            return e_var

        return [translate(e_var) for e_var in range(1, 101)]

    fizzbuzz = fizzbuzz_fixed


@pytest.fixture  # type: ignore[misc]
def fizzbuzz_result() -> list[str | int]:  # type: ignore[misc]
    """Фикстура: возвращает список FizzBuzz."""
    return fizzbuzz()  # type: ignore[no-any-return]


@pytest.fixture  # type: ignore[misc]
def fizzbuzz_dict(  # type: ignore[misc]
    fizzbuzz_result_list: list[str | int],
) -> dict[int, str | int]:
    """Фикстура: словарь {число: значение} для FizzBuzz."""
    return dict(enumerate(fizzbuzz_result_list, 1))


def test_fizzbuzz_len(fizzbuzz_result_list: list[str | int]) -> None:
    """Проверяет длину списка FizzBuzz."""
    assert len(fizzbuzz_result_list) == 100


def test_fizzbuzz_type(fizzbuzz_result_list: list[str | int]) -> None:
    """Проверяет, что FizzBuzz возвращает список."""
    assert isinstance(fizzbuzz_result_list, list)


def test_fizzbuzz_first_element(fizzbuzz_dict_smpl: dict[int, str | int]) -> None:
    """Проверяет первый элемент."""
    assert fizzbuzz_dict_smpl[1] == 1


def test_fizzbuzz_3(fizzbuzz_dict_smpl: dict[int, str | int]) -> None:
    """Проверяет кратность 3."""
    assert fizzbuzz_dict_smpl[3] == "Fizz"


def test_fizzbuzz_5(fizzbuzz_dict_smpl: dict[int, str | int]) -> None:
    """Проверяет кратность 5."""
    assert fizzbuzz_dict_smpl[5] == "Buzz"


def test_fizzbuzz_15(fizzbuzz_dict_smpl: dict[int, str | int]) -> None:
    """Проверяет кратность 3 и 5."""
    assert fizzbuzz_dict_smpl[15] == "FizzBuzz"


# -

# !python -m pytest test_fizzbuzz.py

# # float: когда вещи (почти) равны

# рассмотрите следующий код, какой вы ожидаете результат?

# ```
# x = 0.1 + 0.2
# y = 0.3
# print('x == y', x ==y) # what will it print?
# ```

f_var = 0.1 + 0.2
g_var = 0.3
print("f_var == g_var:", f_var == g_var)  # what will it print?

# если вы ожидали `True`, это означает, что вы еще не пробовали тестировать код с данными с плавающей запятой

print(f_var, "!=", g_var)

# проблема в том, что `float` приблизительно точен (достаточно для большинства расчетов), но может иметь небольшие ошибки округления.
# вот распространенный, но уродливый способ проверить эквивалентность чисел с плавающей точкой

print(abs((0.1 + 0.2) - 0.3) < 1e-6)

# вот более питонический и pytest-ический способ, используя `pytest.approx`

print(0.1 + 0.2 == approx(0.3))

# # Задание 6
#
# Напишите тесты:
# - `math.sin(0) == 0`,
# - `math.sin(math.pi / 2) == 1`
# - `math.sin(math.pi) == 0`
# - `math.sin(math.pi * 3/2) == -1`
# - `math.sin(math.pi * 2) == 0`

# ## Решение 6

# +
# %%file test_sin.py

from pytest import approx
import math

def test_sin() -> None:
    """Проверяет значения функции sin в ключевых точках."""
    assert math.sin(0) == 0
    assert math.sin(math.pi / 2) == approx(1)


# -

# !python -m pytest test_sin.py

# # добавление таймаутов в тесты
#
# Иногда код застревает в бесконечном цикле или ожидает ответа от сервера. Иногда тесты, которые выполняются слишком долго, сами по себе являются признаком неудачи.
#
# как мы можем добавить тайм-ауты к тестам, чтобы избежать зависания? пакет `pytest-timeout` решает эту проблему, предоставляя плагин для pytest.
#
# 1. установите пакет с помощью `pip install pytest-timeout`
# 2. вы можете установить тайм-ауты индивидуально для тестов, пометив их декоратором `@pytest.mark.timeout(timeout=60)`
# 3. вы можете установить тайм-аут для всех тестов глобально, используя параметр командной строки `timeout` для `pytest`, например так: `pytest --timeout=300`

# !pip install -q pytest-timeout

# +
# %%file test_timeouts.py

import pytest

@pytest.mark.timeout(5)
def test_infinite_sleep() -> None:
    """Тест, который зависает и должен быть остановлен по таймауту."""
    import time
    while True:
        time.sleep(1)
        print('sleeping ...')

def test_empty() -> None:
    """Пустой тест — всегда проходит."""
    pass


# -

# !python -m pytest --verbose test_timeouts.py

# обратите внимание, как тест `test_empty` все еще выполняется и проходит, даже если предыдущий тест был прерван

# # Задание 7
#
# 1. используйте модуль `requests` для вызова `.get()` URL http://httpstat.us/101 и вызовите `.raise_for_status()`
# 2. так как запрос будет зависать, используйте тайм-аут для теста, чтобы он не прошел через 5 секунд.
# 3. поскольку тест гарантированно провалится, пометьте его аннотацией `xfail` (ожидаемый провал) `@pytest.mark.xfail(reason='timeout')`

# ## Решение 7

# +
# %%file test_http101_timeout.py

import pytest
import requests

@pytest.mark.xfail(reason='timeout')
@pytest.mark.timeout(2)
def test_http101_timeout() -> None:
    """Проверяет, что запрос завершается по таймауту (ожидаемый xfail)."""
    response = requests.get('http://httpstat.us/101')
    response.raise_for_status()


# -

# !python -m pytest test_http101_timeout.py

# # Тестирование для исключений

# рассмотрим следующий фрагмент кода из `person.py`:

# ```python
# class Person:
#     def add_friend(self, other_person):
#         if not isinstance(other_person, Person):
#             raise TypeError(other_person, "is not a", Person)
#         self.friends.add(other_person)
#         other_person.friends.add(self)
# ```

# метод `add_friend()` вызовет исключение, если он используется с параметром, который не является `Person`
#
# как мы можем это проверить?
#
# если мы обернем код, который должен генерировать `exc`

# +
# %%file test_add_person_exception.py

import pytest
from person import Person
from test_person_fixtures2 import *  # terry, eric

def test_add_person_exception(terry: Person) -> None:
    """Проверяет, что при добавлении не-Person выбрасывается TypeError."""
    with pytest.raises(TypeError):
        terry.add_friend("a shrubbey!")

def test_add_person_exception_detailed(terry: Person) -> None:
    """Проверяет, что текст исключения содержит слово 'Person'."""
    with pytest.raises(TypeError) as excinfo:
        terry.add_friend("a shrubbey!")
    assert 'Person' in str(excinfo.value)

@pytest.mark.xfail(reason='expected to fail')
def test_add_person_no_exception(terry: Person, eric: Person) -> None:
    """
    Ожидаемый провал: тест ожидает TypeError,
    но добавление корректного Person исключения не выбрасывает.
    """
    with pytest.raises(TypeError):  # ожидаем ошибку, но её не будет
        terry.add_friend(eric)


# -

# !python -m pytest test_add_person_exception.py

# # Задание 8

# используйте модуль `requests` и метод `.raise_for_status()`
#
# 1. проверьте, что `.raise_for_status` вызовет исключение при доступе к следующим URL-адресам:
# - http://httpstat.us/401
# - http://httpstat.us/404
# - http://httpstat.us/500
# - http://httpstat.us/501
#
# 2. проверьте, что `.raise_for_status` НЕ вызовет исключение при доступе к следующим URL-адресам:
# - http://httpstat.us/200
# - http://httpstat.us/201
# - http://httpstat.us/202
# - http://httpstat.us/203
# - http://httpstat.us/204
# - http://httpstat.us/303
# - http://httpstat.us/304

# Подсказки:
#
# 1. модуль `requests` вызывает исключения типа `request.HTTPError`
# 2. используйте параметризованные фикстуры, чтобы избежать написания большого количества тестов или стандартного кода
# 3. используйте тайм-ауты, чтобы избежать тестов, которые ждут вечно

# ## Решение 8

# +
# %%file test_requests.py

import pytest
import requests

import pytest
import requests

@pytest.fixture(params=[200, 201, 202, 203, 204, 303, 304])
def good_url(request) -> str:
    """Возвращает URL, который должен вернуть успешный HTTP-статус."""
    return f'http://httpstat.us/{request.param}'

@pytest.fixture(params=[401, 404, 500, 501])
def bad_url(request) -> str:
    """Возвращает URL, который должен вернуть ошибочный HTTP-статус."""
    return f'http://httpstat.us/{request.param}'

@pytest.mark.timeout(2)
def test_good_urls(good_url: str) -> None:
    """Проверяет, что успешные URL не вызывают исключений."""
    response = requests.get(good_url)
    response.raise_for_status()

@pytest.mark.timeout(2)
def test_bad_urls(bad_url: str) -> None:
    """Проверяет, что проблемные URL вызывают HTTPError."""
    response = requests.get(bad_url)
    with pytest.raises(requests.HTTPError):
        response.raise_for_status()


# -

# !python -m pytest --verbose test_requests.py

# # Запуск параллельных тестов
#
# Плагин `pytest-xdist` расширяет возможности `pytest` некоторыми уникальными режимами выполнения тестов:
#
# - *распараллеливание тестового прогона*: если у вас несколько процессоров или хостов, вы можете использовать их для комбинированного тестового прогона. Это позволяет ускорить разработку или использовать специальные ресурсы удаленных машин.
# - **--looponfail**: многократно запускать тесты в подпроцессе. После каждого запуска `pytest` ждет, пока файл в вашем проекте не изменится, а затем повторно запускает ранее не пройденные тесты. Это повторяется до тех пор, пока не будут пройдены все тесты, после чего снова выполняется полный прогон.
# - *Многоплатформенное покрытие*: вы можете указать разные интерпретаторы Python или разные платформы и запускать тесты параллельно на всех из них.
# - **--boxed** и **pytest-forked**: запуск каждого теста в своем собственном процессе, чтобы в случае катастрофического сбоя теста он не мешал другим тестам.
#
# Мы рассмотрим только распараллеливание тестового запуска.

# Установим pytest-xdist:

# !pip install -qq pytest-xdist

# теперь давайте напишем несколько длительных тестов

# +
# %%file test_parallel.py

import time

def test_t1() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t2() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t3() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t4() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t5() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t6() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t7() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t8() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t9() -> None:
    """Имитация долгой операции."""
    time.sleep(2)

def test_t10() -> None:
    """Имитация долгой операции."""
    time.sleep(2)
# -

# теперь мы можем запускать эти тесты параллельно, используя параметр командной строки `pytest -n NUM`.
#
# Давайте использовать 10 потоков, это позволит нам закончить за 2 секунды, а не за 20.

# !python -m pytest -n 10 test_parallel.py
