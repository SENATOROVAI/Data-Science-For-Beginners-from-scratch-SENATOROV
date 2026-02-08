"""Декораторы."""

# ### Декораторы

# #### Объект функции переменной

# Присвоение функций переменной

# +
import functools
import time
from typing import Callable, ParamSpec, TypeVar


def say_hello(name: str) -> None:
    """Вывод имени.

    Args:
        name (str): имя
    """
    print(f"Привет, {name}!")


# -

say_hello_function = say_hello
say_hello_function("Алексей")


# Передача функции в качестве аргумента другой функции


# +
def simple_calculator(
    operation: Callable[[int | float, int | float], int | float],
    value_1: int | float,
    value_2: int | float,
) -> int | float:
    """Калькулятор.

    Args:
        operation (Callable[[int | float, int | float], int | float]): событие
        value_1 (int | float): первое число
        value_2 (int | float): второе число

    Result:
        int|float: результат события, участниками которого были переданные числа
    """
    return operation(value_1, value_2)


def add(value_1: int | float, value_2: int | float) -> int | float:
    """Сумма.

    Args:
        value_1 (int | float): Первое слагаемое
        value_2 (int | float): Второе слагаемое

    Result:
        int|float: Сумма
    """
    return value_1 + value_2


def subtract(value_1: int | float, value_2: int | float) -> int | float:
    """Разница.

    Args:
        value_1 (int | float): Исходное число
        value_2 (int | float): Вычитаемое число

    Result:
        int|float: Разница.
    """
    return value_1 - value_2


def multiply(value_1: int | float, value_2: int | float) -> int | float:
    """Произведение.

    Args:
        value_1 (int | float): Первый множитель
        value_2 (int | float): Второй множитель

    Result:
        int|float: Произведение
    """
    return value_1 * value_2


def divide(value_1: int | float, value_2: int | float) -> int | float:
    """Деление.

    Args:
        value_1 (int | float): Делимое
        value_2 (int | float): Делитель

    Result:
        int|float: Результат деления
    """
    return value_1 / value_2


# -

simple_calculator(divide, 1, 3)


# #### Внутренние функции

# Вызов внутренней функции


def outer() -> None:
    """Внешняя функция."""
    print("Вызов внешней функции.")

    def inner() -> None:
        """Внутренняя функция."""
        print("Вызов внутренней функции.")

    inner()


outer()


# Возвращение функции из функции и замыкание


def create_multiplier(factor: int | float) -> Callable[[int | float], int | float]:
    """Создание функции умножения чисел на константу.

    Args:
        factor (int | float): Константа для умножения

    Result:
        Callable[[int|float], int|float]: Функции умножения чисел на константу
    """

    def multiplier(number: int | float) -> int | float:
        """Умножение числа на константу, переданную во внешней функции.

        Args:
            number (int | float): Умножаемое число

        Result:
            (int | float): Результат умножения
        """
        return number * factor

    return multiplier


double = create_multiplier(factor=2)
triple = create_multiplier(factor=3)

print(double)

print(double(2), triple(2))


def create_multiplier2(factor: int | float) -> Callable[[int | float], int | float]:
    """Создание лямбда-функции умножения чисел на константу.

    Args:
        factor (int | float): Константа для умножения

    Result:
        Callable[[int|float], int|float]: Лямбда-функция умножения чисел на константу
    """
    return lambda number: factor * number


triple = create_multiplier2(factor=3)
print(triple(2))


# #### Знакомство с декораторами

# Простой декоратор


# +
def simple_decorator(func: Callable[[], None]) -> Callable[[], None]:
    """Простой декоратор.

    Args:
        func (Callable[[], None]): Декорируемая функция

    Result:
        Callable[[], None]: Обернутая функция
    """

    def wrapper() -> None:
        """Функционал обёртки."""
        print("Текст до вызова функции func().")
        func()
        print("Текст после вызова функции func().")

    return wrapper


def say_hello2() -> None:
    """Вывод строки."""
    print("Привет!")


# -

say_hello2()


# Конструкция @decorator


@simple_decorator
def say_hi() -> None:
    """Вывод строки."""
    print("Снова, привет!")


say_hi()


# Функция с аргументами

# Этот код вызовет ошибку:
# ```python
# @simple_decorator
# def say_hello_to_person2(person_name: str) -> None:
#     """Приветствие по имени.
#
#     Args:
#         person_name (str): Имя
#     """
#     print(f"Привет, {person_name}!")
#
#
# say_hello_to_person2("Алексей")
# ```


def decorator_with_name_argument(func: Callable[[str], None]) -> Callable[[str], None]:
    """Декоратор с передачей одного параметра.

    Args:
        func (Callable[[], None]): Декорируемая функция

    Result:
        Callable[[], None]: Обернутая функция
    """

    def wrapper(person_name: str) -> None:
        """Функционал обёртки с передачей одного параметра.

        Args:
            person_name (str): Имя
        """
        print("Текст до вызова функция func().")
        func(person_name)
        print("Текст после вызова функция func().")

    return wrapper


@decorator_with_name_argument
def say_hello_to_person3(person_name: str) -> None:
    """Приветствие с именем.

    Args:
        person_name (str): Имя
    """
    print(f"Привет, {person_name}!")


say_hello_to_person3("Алексей")

# +
Parameters = ParamSpec("Parameters")
Result = TypeVar("Result")


def decorator_with_arguments(
    func: Callable[Parameters, Result],
) -> Callable[Parameters, None]:
    """Декоратор с передачей параметров.

    Args:
        func (Callable[Parameters, Result]): Декорируемая функция

    Result:
        Callable[Parameters, None]: Обернутая функция
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> None:
        """Функционал обёртки с передачей параметров."""
        print("Текст до вызова функции func().")
        func(*args, **kwargs)
        print("Текст после вызова функции funс().")

    return wrapper


# -


@decorator_with_arguments
def say_hello_with_argument(name: str) -> None:
    """Приветствие с именем.

    Args:
        name (_type_): Имя
    """
    print(f"Привет, {name}!")


say_hello_with_argument("Алексей")


# Возвращение значения декорируемой функции


def another_decorator(
    func: Callable[Parameters, Result],
) -> Callable[Parameters, None]:
    """Декоратор с передачей параметров.

    Args:
        func (Callable[Parameters, Result]): Декорируемая функция

    Result:
        Callable[Parameters, None]: Обернутая функция
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> None:
        """Функционал обёртки с передачей параметров."""
        print("Текст внутренней функции.")
        func(*args, **kwargs)

    return wrapper


@another_decorator
def return_person(person_name: str) -> str:
    """Возврат переданной строки.

    Args:
        person_name (str): строка

    Result:
        str: исходная строка
    """
    return person_name


returned_value: None = return_person("Алексей")

print(returned_value)


def another_decorator2(
    func: Callable[Parameters, Result],
) -> Callable[Parameters, Result]:
    """Декоратор с передачей параметров и возвратом.

    Args:
        func (Callable[Parameters, Result]): Декорируемая функция

    Result:
        Callable[Parameters, Result]: Обернутая функция
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> Result:
        """Функционал обёртки.

        Result:
            Any: результат выполнения оборачиваемой функции
        """
        print("Текст внутренней функции.")
        return func(*args, **kwargs)

    return wrapper


@another_decorator2
def return_person2(person_name: str) -> str:
    """Возврат строки с именем.

    Args:
        person_name (str): Имя

    Result:
        str: Имя
    """
    return person_name


returned_value2 = return_person2("Алексей")

print(returned_value2)


# Декоратор @functools.wraps


def square(number_value: int | float) -> int | float:
    """Squares a number."""
    return number_value * number_value


square.__name__, square.__doc__


def repeat_twice(func: Callable[Parameters, Result]) -> Callable[Parameters, None]:
    """Двойной вызов функции.

    Args:
        func (Callable[Parameters, Result]): Исходная функция

    Result:
        Callable[Parameters, None]: Обёртка
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> None:
        """Функционал обёртки с двойным вызовом."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice
def square2(number_value: int | float) -> int | float:
    """Squares a number."""
    return number_value * number_value


square2(3)

square2.__name__, square2.__doc__


def repeat_twice2(func: Callable[Parameters, Result]) -> Callable[Parameters, None]:
    """Двойной вызов функции c сохранением документации.

    Args:
        func (Callable[Parameters, Result]): Исходная функция

    Result:
        Callable[Parameters, None]: Обёртка
    """

    @functools.wraps(func)
    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> None:
        """Функционал обёртки с двойным вызовом."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice2
def square3(number_value: int | float) -> None:
    """Squares a number."""
    print(number_value * number_value)


square3.__name__, square3.__doc__


def repeat_twice3(func: Callable[Parameters, Result]) -> Callable[Parameters, None]:
    """Двойной вызов функции c сохранением документации.

    Args:
        func (Callable[Parameters, Result]): Исходная функция

    Result:
        Callable[Parameters, None]: Обёртка
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> None:
        """Функционал обёртки с двойным вызовом."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    functools.update_wrapper(wrapper, func)
    return wrapper


@repeat_twice3
def power_v2(base: int | float, exponent: int | float) -> None:
    """Возведение в степень.

    Args:
        base (int|float): Число
        exponent (int|float): Степень
    """
    print(base**exponent)


# #### Примеры декораторов

# Создание логов


def logging(
    func: Callable[Parameters, Result],
) -> Callable[Parameters, Result]:
    """Логирование функции.

    Args:
        func (Callable[Parameters, Result]): Обёртываемая функция

    Result:
        Callable[Parameters, Result]: Исходная функция в обёртке с логом.
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> Result:
        """Логи для функции.

        Result:
            Result: Результат работы обёртываемой функции
        """
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


# +
@logging
def power(base: int | float, exponent: int | float) -> float | int:
    """Возведение в степень.

    Args:
        base (int|float): Число
        exponent (int|float): Степень

    Result:
        float|int: Результат возведения
    """
    return base**exponent


power(5, 3)


# -

# Время исполнения функции


def timer(func: Callable[Parameters, Result]) -> Callable[Parameters, Result]:
    """Декоратор с таймером.

    Args:
        func (Callable[Parameters, Result]): Обёртываемая функция

    Result:
        Callable[Parameters, Result]: Обёрнутая функция со встроенным таймером
    """

    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> Result:
        """Функционал обёртки с таймером.

        Result:
            Result: Результат обёрнутой функции.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


# +
@timer
def delayed_function(delay_seconds: float | int) -> str:
    """Функция с задержкой.

    Args:
        delay_seconds (float|int): Длительность задержки

    Result:
        str: Строка - индикатор завершения работы функции
    """
    time.sleep(delay_seconds)
    return "execution completed"


delayed_function(2)


# -

# #### Типы методов

# Методы экземпляра


class CatClass:
    """Кот."""

    def __init__(self, color: str) -> None:
        """Создание экземпляра.

        Args:
            color (str): Цвет экземпляра класса кот.
        """
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывод информации о экземпляре класса кот."""
        print(self.color, self.type_, sep=", ")


cat = CatClass(color="black")
cat.info()


# Этот код вызовет ошибку:
# ```python
# CatClass.info()
# CatClass.color
# ```

# Методы класса


class CatClass2:
    """Кот."""

    species = "кошка"

    def __init__(self, color: str) -> None:
        """Создание экземпляра.

        Args:
            color (str): Цвет экземпляра класса кот.
        """
        self.color = color

    def info(self) -> None:
        """Вывод информации о экземпляре класса кот."""
        print(self.color)

    @classmethod
    def get_species(cls) -> None:
        """Доступ к методам класса с помощью спец. декоратора.

        Args:
            cls: Класс
        """
        print(cls.species)
        # нет доступа к переменным color и type_


CatClass2.species

CatClass2.get_species()


# Статические методы


class CatClass3:
    """Кот."""

    species = "кошка"

    def __init__(self, color: str) -> None:
        """Создание экземпляра.

        Args:
            color (str): Цвет экземпляра класса кот.
        """
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывод информации о экземпляре класса кот."""
        print(self.color, self.type_)

    @classmethod
    def get_species(cls) -> None:
        """Доступ к методам класса с помощью спец. декоратора.

        Args:
            cls: Класс
        """
        print(cls.species)
        # нет доступа к переменным color и type_

    @staticmethod
    def convert_to_pounds(kilograms: int | float) -> None:
        """Перевод килограмм в фунты.

        Args:
            kilograms (int|float): Килограммы
        """
        print(f"{kilograms} kg is approximately {kilograms * 2.205} pounds")
        # нет доступа к переменным species, color и type_


CatClass3.convert_to_pounds(4)

cat0 = CatClass3("gray")
cat0.convert_to_pounds(5)


# #### Декорирование класса

# Декорирование методов


class CatClass4:
    """Кот."""

    @logging
    def __init__(self, color: str) -> None:
        """Создание экземпляра.

        Args:
            color (str): Цвет экземпляра класса кот.
        """
        self.color = color
        self.type_ = "cat"

    @timer
    def info(self) -> None:
        """Вывод информации о экземпляре класса кот."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat1 = CatClass4("black")

cat1.info()


# Декорирование всего класса


@timer
class CatClass5:
    """Кот."""

    def __init__(self, color: str) -> None:
        """Создание экземпляра.

        Args:
            color (str): Цвет экземпляра класса кот.
        """
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывод информации о экземпляре класса кот."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat2 = CatClass5("gray")

cat2.info()

setattr(cat2, "weight", 5)

getattr(cat2, "weight")


def add_attribute(
    attribute_name: str, attribute_value: str | int | float
) -> Callable[[type], type]:
    """Создание класса и добавление в него св-ва класса.

    Args:
        attribute_name (str): Имя св-ва класса
        attribute_value (str | int | float): Значения св-ва класса

    Result:
        Callable[[type], type]: Обёртка класса
    """

    def wrapper(cls: type) -> type:
        """Обёртка класса.

        Result:
            type: Класс с добавленным св-вом
        """
        setattr(cls, attribute_name, attribute_value)
        return cls

    return wrapper


@add_attribute("species", "кошка")
class CatClass6:
    """Кот."""

    def __init__(self, color: str) -> None:
        """Создание экземпляра.

        Args:
            color (str): Цвет экземпляра класса кот.
        """
        self.color = color
        self.type_ = "cat"


getattr(CatClass6, "species")


# ### Несколько декораторов


@logging
@timer
def delayed_function2(delay_seconds: float | int) -> str:
    """Функция с задержкой.

    Args:
        delay_seconds (float | int): Длительность задержки

    Result:
        str: Строка индикатор выполнения функции
    """
    time.sleep(delay_seconds)
    return "execution completed"


delayed_function2(2)


def delayed_function3(delay_seconds: float | int) -> str:
    """Функция с задержкой.

    Args:
        delay_seconds (float | int): Длительность задержки

    Result:
        str: Строка индикатор выполнения функции
    """
    time.sleep(delay_seconds)
    return "execution completed"


delayed_function3 = logging(timer(delayed_function3))
delayed_function3(2)


# ### Декораторы с аргументами


def repeat(
    n_times: int,
) -> Callable[[Callable[Parameters, Result]], Callable[Parameters, None]]:
    """Декоратор повторения с задаваемым кол-вом.

    Args:
        n_times (int): Кол-во повторений внутренней функции

    Result:
        Callable[Callable[Parameters, Result], Callable[Parameters, None]]: Внешний декоратор повторения
    """

    def inner_decorator(
        func: Callable[Parameters, Result],
    ) -> Callable[Parameters, None]:
        """Внутренний декоратор повторения.

        Args:
            func (Callable[Parameters, Result]): Обёртываемая функция

        Result:
            Callable[Parameters, None]: Обёртка исходной функции
        """

        @functools.wraps(func)
        def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> None:
            """Обёртка исходной функции."""
            for _ in range(n_times):
                func(*args, **kwargs)

        return wrapper

    return inner_decorator


@repeat(n_times=3)
def say_hello3(name: str) -> None:
    """Приветствие с именем.

    Args:
        name (str): Имя
    """
    print(f"Привет, {name}")


say_hello3("Алексей")
