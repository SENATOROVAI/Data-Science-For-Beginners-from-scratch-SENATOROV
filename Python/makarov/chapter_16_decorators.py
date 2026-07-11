"""Decorators."""

import functools
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

Params = ParamSpec("Params")
T = TypeVar("T")

# Объекты первого класса


# объявим функцию
def say_hello(name: str) -> None:
    """Поприветствовать пользователя по имени."""
    print(f"Привет, {name}!")


# присвоим эту функцию переменной (без скобок)
say_hello_function = say_hello
# вызовем функцию из новой переменной
say_hello_function("Алексей")


# +
# Передача функции в качестве аргумента другой функции


def simple_calculator(
    operation: Callable[[float, float], float], num1: float, num2: float
) -> float:
    """Применить операцию к двум числам."""
    return operation(num1, num2)


def add(num1: float, num2: float) -> float:
    """Сложить два числа."""
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    """Вычесть одно число из другого."""
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    """Перемножить два числа."""
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    """Разделить одно число на другое."""
    return num1 / num2


simple_calculator(divide, 1, 3)


# +
# Вызов внутренней функции


def outer() -> None:
    """Вызвать внутреннюю функцию."""
    print("Вызов внешней функции.")

    # обратите внимание, мы объявляем, а затем
    def inner() -> None:
        print("Вызов внутренней функции.")

    # вызываем внутреннюю функцию
    inner()


# -

outer()


# +
def create_multiplier(factor: float) -> Callable[[float], float]:
    """Создать функцию, умножающую число на factor."""

    def multiplier(number: float) -> float:
        return number * factor

    return multiplier


double = create_multiplier(factor=2)
triple = create_multiplier(factor=3)
# -

print(double(2), triple(2))


# Простой декоратор


# +
def simple_decorator(func: Callable[[], None]) -> Callable[[], None]:
    """Обернуть func сообщениями до и после вызова."""

    def wrapper() -> None:
        print("Текст до вызова функции func().")
        func()
        print("Текст после вызова функции func().")

    return wrapper


def greet() -> None:
    """Поздороваться без параметров."""
    print("Привет!")


# -

greet = simple_decorator(greet)

greet()


# Конструкция @decorator


# +
@simple_decorator
def say_hi() -> None:
    """Ещё раз поздороваться."""
    print("Снова, привет!")


say_hi()


# +
@simple_decorator  # type: ignore[arg-type]
def say_hello_with_name_broken(name: str) -> None:
    """Поприветствовать по имени декоратором без поддержки аргументов."""
    print(f"Привет, {name}!")


# say_hello_with_name_broken('Алексей')


# -


def decorator_with_name_argument(func: Callable[[str], None]) -> Callable[[str], None]:
    """Обернуть func, принимающую один аргумент name."""

    def wrapper(name: str) -> None:
        print("Текст до вызова функции func().")
        func(name)
        print("Текст после вызова функции func().")

    return wrapper


@decorator_with_name_argument
def say_hello_with_name(username: str) -> None:
    """Поприветствовать по имени."""
    print(f"Привет, {username}!")


say_hello_with_name("Алексей")


def decorator_with_arguments(func: Callable[Params, None]) -> Callable[Params, None]:
    """Обернуть func с произвольными аргументами."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
        print("Текст до вызова функции func().")
        func(*args, **kwargs)
        print("Текст после вызова функции func().")

    return wrapper


@decorator_with_arguments
def say_hello_with_argument(name: str) -> None:
    """Поприветствовать по имени."""
    print(f"Привет, {name}!")


say_hello_with_argument("Алексей")


# Возвращение значения декорируемой функции


def another_decorator(func: Callable[Params, object]) -> Callable[Params, None]:
    """Обернуть func, не возвращая её результат."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
        print("Текст внутренней функции.")
        func(*args, **kwargs)

    return wrapper


@another_decorator
def return_name(username: str) -> str:
    """Вернуть переданное имя."""
    return username


returned_value: None = return_name("Алексей")


def repeat_twice(func: Callable[Params, None]) -> Callable[Params, None]:
    """Вызвать func дважды подряд."""

    @functools.wraps(func)
    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice
def square(number: float) -> None:
    """Squares a number."""
    print(number * number)


square(3)


# Примеры декораторов

# +
# Создание логов


def logging(func: Callable[Params, T]) -> Callable[Params, T]:
    """Логировать аргументы и результат вызова func."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> T:
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


# +
@logging
def power(base: float, exponent: float) -> float:
    """Возвести base в степень exponent."""
    return float(base**exponent)


power(5, 3)

# +
# Время исполнения функции


def timer(func: Callable[Params, T]) -> Callable[Params, T]:
    """Замерить время выполнения func."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> T:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


# +
@timer
def delayed_function(seconds: float) -> str:
    """Подождать seconds секунд и вернуть сообщение."""
    time.sleep(seconds)
    return "execution completed"


delayed_function(2)


# -

# Методы экземпляра


class CatClass:
    """Простой кот с цветом и типом."""

    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывести цвет и тип кота."""
        print(self.color, self.type_, sep=", ")


cat = CatClass(color="black")
cat.info()


# Методы класса


class CatClassWithSpecies:
    """Кот с переменной класса species и classmethod."""

    species = "кошка"  # переменная класса доступна всем экземплярам

    def __init__(self, color: str) -> None:
        """Сохранить цвет кота."""
        self.color = color

    def info(self) -> None:
        """Вывести цвет кота."""
        print(self.color)

    @classmethod
    def get_species(cls) -> None:
        """Вывести вид животного."""
        print(cls.species)
        # нет доступа к переменным color и type_


CatClassWithSpecies.species

CatClassWithSpecies.get_species()


# Статические методы


class CatClassFull:
    """Кот с переменной класса, classmethod и staticmethod."""

    species = "кошка"

    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывести цвет и тип кота."""
        print(self.color, self.type_)

    @classmethod
    def get_species(cls) -> None:
        """Вывести вид животного."""
        print(cls.species)
        # нет доступа к переменным color и type_

    @staticmethod
    def convert_to_pounds(weight_kg: float) -> None:
        """Перевести килограммы в фунты."""
        print(f"{weight_kg} kg is approximately {weight_kg * 2.205} pounds")
        # нет доступа к переменным species, color и type_


CatClassFull.convert_to_pounds(4)

cat_full = CatClassFull("gray")
cat_full.convert_to_pounds(5)


# Декорирование класса


class CatClassDecoratedMethods:
    """Кот, у которого декорированы отдельные методы."""

    @logging
    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        self.color = color
        self.type_ = "cat"

    @timer
    def info(self) -> None:
        """Подождать и вывести цвет и тип кота."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat_decorated = CatClassDecoratedMethods("black")

cat_decorated.info()


@timer
class CatClassTimed:
    """Кот, декорированный целиком через @timer."""

    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Подождать и вывести цвет и тип кота."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat_timed = CatClassTimed("gray")

cat_timed.info()


def add_attribute(attribute_name: str, attribute_value: str) -> Callable[[type], type]:
    """Создать декоратор класса, добавляющий атрибут attribute_name."""

    def wrapper(cls: type) -> type:
        setattr(cls, attribute_name, attribute_value)
        return cls

    return wrapper


@add_attribute("species", "кошка")
class CatClassWithAttribute:
    """Кот с атрибутом, добавленным декоратором класса."""

    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        self.color = color
        self.type_ = "cat"


CatClassWithAttribute.species  # type: ignore[attr-defined]


# +
# Несколько декораторов


@logging
@timer
def delayed_function_multi(seconds: float) -> str:
    """Подождать seconds секунд и вернуть сообщение."""
    time.sleep(seconds)
    return "execution completed"


# -

delayed_function_multi(3)


# +
# Декораторы с аргументами


def repeat(n_times: int) -> Callable[[Callable[Params, None]], Callable[Params, None]]:
    """Создать декоратор, вызывающий функцию n_times раз."""

    def inner_decorator(func: Callable[Params, None]) -> Callable[Params, None]:
        @functools.wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
            for _ in range(n_times):
                func(*args, **kwargs)

        return wrapper

    return inner_decorator


# -


@repeat(n_times=3)
def say_hello_repeated(name: str) -> None:
    """Поприветствовать по имени n_times раз."""
    print(f"Привет, {name}!")


say_hello_repeated("Алексей")
