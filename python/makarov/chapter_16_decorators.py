"""Макаров.

Декораторы.
"""

# # Декораторы

# ### Объекты первого класса

# Присвоение функции переменной

# +
import functools
import time
from typing import Callable, ParamSpec, TypeVar

# ParamSpec - это переменная типа для сигнатуры функции: она «запоминает»
# все аргументы (позиционные и именованные) функции,
# чтобы их можно было точно передать дальше с сохранением типобезопасности.
# Основное применение - функции высшего порядка (в отм числе декораторы)
Params = ParamSpec("Params")

# TypeVar - это переменная типа, которая позволяет писать обобщённые (generic)
# функции и классы, сохраняя связь между входными и выходными типами.
Return = TypeVar("Return")

# объявим функцию


def say_hello(name: str) -> None:
    """Выводит приветствие."""
    print(f"Привет, {name}!")


# -

# присвоим эту функцию переменной (без скобок)
say_hello_function = say_hello
# вызовем функцию из новой переменной
say_hello_function("Алексей")


# Передача функции в качестве аргумента другой функции

# +
def simple_calculator(
    operation: Callable[[int, int], int | float], a_arg: int, b_arg: int
) -> int | float:
    """Функция обертка.

    Вызывает переданную функцию с переданными аргументами.
    """
    return operation(a_arg, b_arg)


def add(a_arg: int, b_arg: int) -> int:
    """Возвращает сумму двух аргументов."""
    return a_arg + b_arg


def subtract(a_arg: int, b_arg: int) -> int:
    """Возвращает разность двух аргументов."""
    return a_arg - b_arg


def multiply(a_arg: int, b_arg: int) -> int:
    """Возвращает произведение двух аргументов."""
    return a_arg * b_arg


def divide(a_arg: int, b_arg: int) -> float:
    """Возвращает частное от деления первого аргумента на второй аргумент."""
    return a_arg / b_arg


# -

simple_calculator(divide, 1, 3)


# ### Внутренние функции

# Вызов внутренней функции

def outer() -> None:
    """Внешняя функция."""
    print("Вызов внешней функции.")

    # обратите внимание, мы объявляем, а затем
    def inner() -> None:
        """Внутренняя функция."""
        print("Вызов внутренней функции.")

    # вызываем внутреннюю функцию
    inner()


outer()


# +
# inner()
# -

# Возвращение функции из функции и замыкание

def create_multiplier(factor: int) -> Callable[[int], int]:
    """Создает функцию-умножитель."""

    def multiplier(number: int) -> int:
        return number * factor

    return multiplier


double = create_multiplier(factor=2)
triple = create_multiplier(factor=3)

print(double)

print(double(2), triple(2))


def create_multiplier_1(factor: int) -> Callable[[int], int]:
    """Создает функцию-умножитель."""
    return lambda number: factor * number


triple_1 = create_multiplier_1(factor=3)
triple_1(2)


# ### Знакомство с декораторами

# Простой декоратор

# +
def simple_decorator(
    func: Callable[Params, Return],
) -> Callable[Params, Return]:
    """Простой декоратор."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Функция-обертка."""
        print("Текст до вызова функции func().")
        result = func(*args, **kwargs)
        print("Текст после вызова функции func().")

        return result

    return wrapper


def say_hello_1() -> None:
    """Функция-приветствие."""
    print("Привет!")


# -

say_hello_var = simple_decorator(say_hello_1)

say_hello_var()


# Конструкция @decorator

@simple_decorator
def say_hi() -> None:
    """Функция повторного приветствия."""
    print("Снова, привет!")


say_hi()


# Функции с аргументами

@simple_decorator
def say_hello_with_name(name_arg: str) -> None:
    """Приветствие с именем."""
    print(f"Привет, {name_arg}!")


# +
# say_hello_with_name('Алексей')
# -

def decorator_with_name_argument(
    func: Callable[[str], None],
) -> Callable[[str], None]:
    """Декоратор, принимающий имя."""

    def wrapper(name: str) -> None:
        """Функция-обертка."""
        print("Текст до вызова функции func().")
        func(name)
        print("Текст после вызова функции func().")

    return wrapper


@decorator_with_name_argument
def say_hello_with_name_1(name: str) -> None:
    """Приветствие с именем."""
    print(f"Привет, {name}!")


say_hello_with_name_1("Алексей")


def decorator_with_arguments(
    func: Callable[Params, Return],
) -> Callable[Params, Return]:
    """Декоратор с аргументами."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Функция-обертка."""
        print("Текст до вызова функции func().")

        result = func(*args, **kwargs)

        print("Текст после вызова функции func().")

        return result

    return wrapper


@decorator_with_arguments
def say_hello_with_argument(name: str) -> None:
    """Функция-приветствие, принимающая имя."""
    print(f"Привет, {name}!")


say_hello_with_argument("Алексей")


# Возвращение значения декорируемой функции

def another_decorator(
    func: Callable[Params, Return],
) -> Callable[Params, Return]:
    """Другой декоратор с аргументами."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Функция-обертка."""
        print("Текст внутренней функции.")

        return func(*args, **kwargs)

    return wrapper


@another_decorator
def return_name_1(name: str) -> str:
    """Возвращает переданное имя."""
    return name


returned_value = return_name_1("Алексей")

print(returned_value)


def another_decorator_1(
    func: Callable[Params, Return],
) -> Callable[Params, Return]:
    """Другой декоратор."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Функция-обертка."""
        print("Текст внутренней функции.")
        return func(*args, **kwargs)  # внутренняя функция возвращает func()

    return wrapper


@another_decorator_1
def return_name(name_arg: str) -> str:
    """Возвращает переданное имя."""
    return name_arg


returned_value = return_name("Алексей")

print(returned_value)


# Декоратор @functools.wraps

def square(num: int) -> int:
    """Squares a number."""
    return num * num


print(square.__name__, square.__doc__)


def repeat_twice(
    func: Callable[Params, Return],
) -> Callable[Params, None]:
    """Декоратор, который дважды вызывает функция."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
        """Функция-обертка."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice
def square_1(num: int) -> int:
    """Squares a number."""
    result = num * num

    print(result)

    return result


square_1(3)

square.__name__, square.__doc__


def repeat_twice_1(
    func: Callable[Params, Return],
) -> Callable[Params, None]:
    """Декоратор, который дважды вызывает функция."""

    @functools.wraps(func)
    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
        """Функция-обертка."""
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice_1
def square_2(num: int) -> int:
    """Squares a number."""
    result = num * num

    print(result)

    return result


print(square_2.__name__, square_2.__doc__)

print(square_2.__wrapped__)  # type: ignore


def repeat_twice_2(
    func: Callable[Params, Return],
) -> Callable[Params, None]:
    """Декоратор, который дважды вызывает функция."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
        """Функция-обертка."""
        func(*args, **kwargs)
        func(*args, **kwargs)
        functools.update_wrapper(wrapper, func)

    return wrapper


@repeat_twice_2
def power(num: int, pow_arg: int) -> None:
    """Raise to a power."""
    print(num**pow_arg)


power(2, 3)

print(power.__doc__)


# ### Примеры декораторов

# Создание логов

def logging(
    func: Callable[Params, Return],
) -> Callable[Params, Return]:
    """Логирование вызовов функции."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Функция-обертка."""
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned: {result}")

        return result

    return wrapper


# +
@logging
def power_1(num: int, pow_arg: int) -> int:
    """Raise to a power."""
    return int(num**pow_arg)


power_1(5, 3)


# -

# Время исполнения функции

def timer(
    func: Callable[Params, Return],
) -> Callable[Params, Return]:
    """Декоратор для вычисления времени выполнения функции."""

    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Return:
        """Функция-обертка."""
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")

        return result

    return wrapper


# +
@timer
def delayed_function(delay: int) -> str:
    """Функция с задержкой выполнения."""
    time.sleep(delay)
    return "execution completed"


delayed_function(2)


# -

# ### Типы методов

# Методы экземпляра

class CatClass:
    """Класс кот."""

    def __init__(self, color: str) -> None:
        """Инициализация кота с цветом."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывод информации о коте."""
        print(self.color, self.type_, sep=", ")


cat = CatClass(color="black")
cat.info()


# +
# CatClass.info()

# +
# CatClass.color
# -

# Методы класса

class CatClass1:
    """Класс кот."""

    species = "кошка"  # переменная класса доступна всем экземплярам

    def __init__(self, color: str) -> None:
        """Инициализация кота с цветом."""
        self.color = color

    def info(self) -> None:
        """Вывод информации о коте."""
        print(self.color)

    @classmethod
    def get_species(cls) -> None:
        """Вывод значения аттрибута класса species."""
        print(cls.species)
        # нет доступа к переменным color и type_


print(CatClass1.species)

CatClass1.get_species()


# Статические методы

class CatClass2:
    """Класс кот."""

    species = "кошка"

    def __init__(self, color: str) -> None:
        """Инициализация кота с цветом."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывод информации о коте."""
        print(self.color, self.type_)

    @classmethod
    def get_species(cls) -> None:
        """Вывод значения аттрибута класса species."""
        print(cls.species)
        # нет доступа к переменным color и type_

    @staticmethod
    def convert_to_pounds(kg: int) -> None:
        """Конвертирует килограммы в фунты."""
        print(f"{kg} kg is approximately {kg * 2.205} pounds")
        # нет доступа к переменным species, color и type_


CatClass2.convert_to_pounds(4)

cat2 = CatClass2("gray")
cat2.convert_to_pounds(5)


# ### Декорирование класса

# Декорирование методов

class CatClass3:
    """Класс кот."""

    @logging
    def __init__(self, color: str) -> None:
        """Инициализация кота с цветом."""
        self.color = color
        self.type_ = "cat"

    @timer
    def info(self) -> None:
        """Вывод информации о коте."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat3 = CatClass3("black")

cat3.info()


# Декорирование всего класса

@timer
class CatClass4:
    """Класс кот."""

    def __init__(self, color: str) -> None:
        """Инициализация кота с цветом."""
        self.color = color
        self.type_ = "cat"

    def info(self) -> None:
        """Вывод информации о коте."""
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat4 = CatClass4("gray")

cat4.info()

setattr(cat4, "weight", 5)

print(
    cat4.weight,  # type: ignore # pylint: disable=E1101
    getattr(cat4, "weight"),
)

# +
# TypeVar - это переменная типа, которая позволяет писать обобщённые (generic)
# функции и классы, сохраняя связь между входными и выходными типами.
Class = TypeVar("Class", bound=type)


def add_attribute(
    attribute_name: str, attribute_value: str
) -> Callable[[Class], Class]:
    """Декоратор класса, добавляющий указанный атрибут к классу."""

    def wrapper(cls: Class) -> Class:
        """Функция-обертка."""
        setattr(cls, attribute_name, attribute_value)
        return cls

    return wrapper


# -

@add_attribute("species", "кошка")
class CatClass5:
    """Класс кот."""

    def __init__(self, color: str) -> None:
        """Инициализация кота с цветом."""
        self.color = color
        self.type_ = "cat"


print(CatClass5.species)  # type: ignore # pylint: disable=E1101


# ### Несколько декораторов

@logging
@timer
def delayed_function_1(delay: int) -> str:
    """Функция с задержкой выполнения."""
    time.sleep(delay)
    return "execution completed"


delayed_function_1(2)

# +
# не забудем заново объявить функцию без декораторов


def delayed_function_3(delay: int) -> str:
    """Функция с задержкой выполнения."""
    time.sleep(delay)
    return "execution completed"


# -

delayed_function_4 = logging(timer(delayed_function))
delayed_function_4(2)


# ### Декораторы с аргументами

def repeat(
    n_times: int,
) -> Callable[[Callable[Params, Return]], Callable[Params, None]]:
    """Декоратор, вызывающий функцию указанное количество раз."""

    def inner_decorator(
        func: Callable[Params, Return],
    ) -> Callable[Params, None]:
        """Внутренний декоратор."""

        @functools.wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> None:
            """Функция-обертка."""
            for _ in range(n_times):
                func(*args, **kwargs)

        return wrapper

    return inner_decorator


@repeat(n_times=3)
def say_hello_3(name: str) -> None:
    """Функция-обертка."""
    print(f"Привет, {name}!")


say_hello_3("Алексей")
