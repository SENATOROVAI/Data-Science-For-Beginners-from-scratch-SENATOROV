"""Decorators."""

# +
from __future__ import annotations

import functools
import time
from collections.abc import Callable
from typing import ParamSpec, Protocol, TypeVar

Params = ParamSpec("Params")
Arguments = TypeVar("Arguments")
T = TypeVar("T")


# -

# ## Декораторы
# ### Объекты первого класса
# #### Присвоение функции переменной


def say_hello_basic(name: str) -> None:
    """Print greeting with provided name."""
    print(f"Hello, {name}!")


say_hello_function = say_hello_basic
say_hello_function("Alexey")


# ## Передача функции в качестве аргумента другой функции
#


# +
def simple_calculator(
    operation: Callable[[float, float], float],
    first_number: float,
    second_number: float,
) -> float:
    """Calculate result using provided binary operation."""
    return operation(first_number, second_number)


def add(first_number: float, second_number: float) -> float:
    """Return sum of numbers."""
    return first_number + second_number


def subtract(first_number: float, second_number: float) -> float:
    """Return difference of numbers."""
    return first_number - second_number


def multiply(first_number: float, second_number: float) -> float:
    """Return product of numbers."""
    return first_number * second_number


def divide(first_number: float, second_number: float) -> float:
    """Return division result of numbers."""
    return first_number / second_number


# -

print(simple_calculator(divide, 33, 3))


# ## Внутренние функции
# ### Вызов внутренней функции
#
#


# +
def outer() -> None:
    """Print messages from outer and inner functions."""
    print("out function call")

    def inner() -> None:
        """Print inner function call message."""
        print("inner function call")

    inner()


outer()


# -

# ## Возвращение функции из функции и замыкание
#


# +
class MultiplierCallable(Protocol):
    """Protocol defining callable multiplier function."""

    def __call__(self, number: int) -> int:
        """Callable signature defining multiplier behavior."""
        raise NotImplementedError


def create_multiplier(factor: int) -> MultiplierCallable:
    """Create multiplier closure for demonstration purposes."""

    def multiplier(number: int) -> int:
        """Multiply number by predefined factor."""
        return number * factor

    return multiplier


double_multiplier: MultiplierCallable = create_multiplier(factor=2)
triple_multiplier: MultiplierCallable = create_multiplier(factor=3)
# -

print(double_multiplier)

print((double_multiplier(number=2), triple_multiplier(number=2)))


def create_multiplier_2(factor: int) -> Callable[[int], int]:
    """Create multiplier using a nested function for demonstration purposes."""

    def multiplier(number: int) -> int:
        """Multiply number by predefined factor."""
        return factor * number

    return multiplier


triple_multiplier_v2 = create_multiplier_2(factor=3)
print(triple_multiplier_v2(2))


# ## Знакомство с декораторами
# ### Простой декоратор
#


# +
def simple_decorator(
    func: Callable[Params, Arguments],
) -> Callable[Params, Arguments]:
    """Decorate function by adding text before and after execution."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        """Wrap function call and print surrounding text."""
        print("Text before func().")
        result = func(*args, **kwargs)
        print("Text after func().")
        return result

    return wrapper


def say_hello_decorated() -> None:
    """Print simple greeting."""
    print("Hello!")


say_hello_decorated = simple_decorator(say_hello_decorated)
# -

say_hello_decorated()


# ## Конструкция @decorator
#


@simple_decorator
def say_hi() -> None:
    """Print repeated greeting."""
    print("Hello, again...")


say_hi()


# ## Функции с аргументами
#


# +
@simple_decorator
def say_hello_with_name_simple(name: str) -> None:
    """Print greeting with provided name."""
    print(f"Hello, {name}!")


say_hello_with_name_simple("Alex")


# -


def decorator_with_name_argument(func: Callable[[str], None]) -> Callable[[str], None]:
    """Decorate function expecting a single name argument."""

    def wrapper(name: str) -> None:
        """Wrap function call and print surrounding text."""
        print("Text before func().")
        func(name)
        print("Text after func().")

    return wrapper


@decorator_with_name_argument
def say_hello_with_name_logged(name: str) -> None:
    """Print greeting with provided name."""
    print(f"Hello, {name}!")


say_hello_with_name_logged("Alex")


# +
def decorator_with_arguments(
    func: Callable[Params, Arguments],
) -> Callable[Params, Arguments]:
    """Decorate function printing text before and after call."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        """Wrap function call and print surrounding text."""
        print("Text before func().")
        result = func(*args, **kwargs)
        print("Text after func().")
        return result

    return wrapper


@decorator_with_arguments
def say_hello_with_argument(name: str) -> None:
    """Print greeting with provided name."""
    print(f"Hello, {name}!")


# -

say_hello_with_argument("Alex")


# ## Возвращение значения декорируемой функции
#


def another_decorator(func: Callable[[str], str]) -> Callable[[str], None]:
    """Decorate function by printing text before call."""

    def wrapper(name: str) -> None:
        """Wrap function call and print inner text."""
        print("Inner function text")
        func(name)

    return wrapper


@another_decorator
def return_name_silent(name: str) -> str:
    """Return provided name."""
    return name


returned_value: str | None = return_name_silent("Alex")

print(returned_value)


def another_decorator_verbose(
    func: Callable[[str], Arguments],
) -> Callable[[str], Arguments]:
    """Decorate function by printing text and returning result."""

    def wrapper(name: str) -> Arguments:
        """Wrap function call, print text, and return result."""
        print("����� ���������� �������.")
        return func(name)

    return wrapper


@another_decorator_verbose
def return_name_verbose(name: str) -> str:
    """Return provided name."""
    return name


returned_value_verbose: str = return_name_verbose("Alex")

print(returned_value_verbose)


# ## Декоратор @functools.wraps
#


def square_basic(value: int) -> int:
    """Return square of the given number."""
    return value * value


print((square_basic.__name__, square_basic.__doc__))


def repeat_twice(
    func: Callable[Params, Arguments],
) -> Callable[Params, Arguments]:
    """Decorate function to run twice."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        result = func(*args, **kwargs)
        return result

    return wrapper


@repeat_twice
def square_repeated(value: int) -> int:
    """Return square of the given number."""
    return value * value


square_repeated(3)

print((square_repeated.__name__, square_repeated.__doc__))


def repeat_twice_with_wraps(
    func: Callable[Params, Arguments],
) -> Callable[Params, Arguments]:
    """Decorate function by repeating execution twice with wraps."""

    @functools.wraps(func)
    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        """Wrap function call, execute twice, and return result."""
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@repeat_twice_with_wraps
def square_wrapped(value: int) -> None:
    """Return square of the given number."""
    print(value * value)


print((square_wrapped.__name__, square_wrapped.__doc__))

print(getattr(square_wrapped, "__wrapped__"))


def repeat_twice_updated(
    func: Callable[Params, Arguments],
) -> Callable[Params, Arguments]:
    """Decorate function by repeating execution twice and preserving
    metadata."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        """Wrap function call, execute twice, and return result."""
        func(*args, **kwargs)
        return func(*args, **kwargs)

    functools.update_wrapper(wrapper, func)
    return wrapper


@repeat_twice_updated
def power_repeated(base_value: float, exponent: float) -> int | float:
    """Return base raised to exponent."""
    result: int | float = base_value**exponent
    return result


power_repeated(2, 3)

print(power_repeated.__doc__)


# ## Примеры декораторов
# ### Создание логов
#


def logging(func: Callable[Params, Arguments]) -> Callable[Params, Arguments]:
    """Decorate function with logging."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        """Wrap function call and log arguments and result."""
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


# +
@logging
def power_logged(base_value: int, exponent: int) -> int | float:
    """Return power of a number."""
    result: int | float = base_value**exponent
    return result


power_logged(5, 3)


# -

# ## Время исполнения функции
#


def timer(func: Callable[Params, Arguments]) -> Callable[Params, Arguments]:
    """Wrap function to measure execution time."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Arguments:
        """Wrap function call, measure duration, and return result."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


# +
@timer
def delayed_function_timed(delay_time: float) -> str:
    """Delay execution for specified time."""
    time.sleep(delay_time)
    return "execution completed"


delayed_function_timed(2)


# -

# ## Типы методов
# ### Методы экземпляра
#


class CatClassBasic:
    """Represent basic cat data."""

    def __init__(self, color: str) -> None:
        """Initialize instance attributes."""
        self.color: str = color
        self.type_: str = "cat"

    def info(self) -> None:
        """Print cat information."""
        print(self.color, self.type_, sep=", ")


cat_basic = CatClassBasic(color="black")
cat_basic.info()


# ## Методы класса
#


class CatClassWithSpecies:
    """Represent cat data with species information."""

    species: str = "Cat"

    def __init__(self, color: str) -> None:
        """Initialize instance attributes."""
        self.color: str = color

    def info(self) -> None:
        """Print cat color."""
        print(self.color)

    @classmethod
    def get_species(cls) -> None:
        """Print species name."""
        print(cls.species)


print(CatClassWithSpecies.species)

CatClassWithSpecies.get_species()


# ## Статические методы
#


class CatClassWithConverter:
    """Represent cat data with conversion utility."""

    species: str = "Cat"

    def __init__(self, color: str) -> None:
        """Initialize instance attributes."""
        self.color: str = color

    def info(self) -> None:
        """Print cat color."""
        print(self.color)

    @classmethod
    def get_species(cls) -> None:
        """Print species name."""
        print(cls.species)

    @staticmethod
    def convert_to_pounds(weight_kg: float) -> None:
        """Convert kilograms to pounds and print result."""
        print(f"{weight_kg} kg is approximately {weight_kg * 2.205} pounds")


CatClassWithConverter.convert_to_pounds(4)

cat_with_converter = CatClassWithConverter("gray")
cat_with_converter.convert_to_pounds(12)


# ## Декорирование класса
# ### Декорирование методов
#
#


class CatClassDecorated:
    """Represent cat data with decorated methods."""

    color: str
    type_: str

    @logging
    def __init__(self, color: str) -> None:
        """Initialize instance attributes."""
        self.color = color
        self.type_ = "cat"

    @timer
    def info(self) -> None:
        """Print cat information with delay."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat_decorated = CatClassDecorated("black")

cat_decorated.info()


# ## Декорирование всего класса
#


@timer
class CatClassTimed:
    """Represent cat data with timed methods."""

    weight: float | int | None = None
    color: str
    type_: str

    def __init__(self, color: str) -> None:
        """Initialize instance attributes."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Print cat information with delay."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat_timed = CatClassTimed("grey")

cat_timed.info()

setattr(cat_timed, "weight", 5)

print((cat_timed.weight, getattr(cat_timed, "weight")))


def add_attribute(
    attribute_name: str, attribute_value: str
) -> Callable[[type[T]], type[T]]:
    """Decorate class by adding specified attribute."""

    def wrapper(cls: type[T]) -> type[T]:
        """Attach attribute to class and return the class."""
        setattr(cls, attribute_name, attribute_value)
        return cls

    return wrapper


@add_attribute("species", "cat")
class CatClassAttributed:
    """Represent cat data with added attributes."""

    species: str = "cat"
    color: str
    type_: str

    def __init__(self, color: str) -> None:
        """Initialize instance attributes."""
        self.color = color
        self.type_ = "cat"


print(CatClassAttributed.species)


# ## Несколько декораторов
#


@logging
@timer
def delayed_function_logged_timed(delay_time: float) -> str:
    """Delay execution with logging and timing."""
    time.sleep(delay_time)
    return "execution completed"


delayed_function_logged_timed(2)


def delayed_function_plain(delay_time: float) -> str:
    """Delay execution for specified time."""
    time.sleep(delay_time)
    return "execution completed"


delayed_function_wrapped = logging(timer(delayed_function_plain))
delayed_function_wrapped(2)


# ## Декораторы с аргументами
#


def repeat(
    repeat_count: int,
) -> Callable[[Callable[Params, None]], Callable[Params, None]]:
    """Create decorator repeating function calls."""

    def inner_decorator(func: Callable[Params, None]) -> Callable[Params, None]:
        """Wrap function to repeat calls the specified number of times."""

        @functools.wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
            """Wrap function call and repeat execution."""
            for _ in range(repeat_count):
                func(*args, **kwargs)

        return wrapper

    return inner_decorator


@repeat(repeat_count=3)
def say_hello_repeated(name: str) -> None:
    """Print greeting with provided name."""
    print(f"Hello, {name}!")


say_hello_repeated("Alex")
