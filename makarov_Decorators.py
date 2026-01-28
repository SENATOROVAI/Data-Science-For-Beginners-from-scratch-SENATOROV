# объявим функцию
import functools
import time


def say_hello(name):
    print(f"Привет, {name}!")


# присвоим эту функцию переменной (без скобок)
say_hello_function = say_hello
# вызовем функцию из новой переменной
say_hello_function("Алексей")


def simple_calculator(operation, a, b):
    return operation(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


simple_calculator(divide, 1, 3)


def outer():
    print("Вызов внешней функции.")

    # обратите внимание, мы объявляем, а затем
    def inner():
        print("Вызов внутренней функции.")

    # вызываем внутреннюю функцию
    inner()


outer()

# inner()


def create_multiplier(factor):
    def multiplier(number):
        return number * factor

    return multiplier


double = create_multiplier(factor=2)
triple = create_multiplier(factor=3)

double

double(number=2), triple(number=2)


def create_multiplier(factor):
    return lambda number: factor * number


triple = create_multiplier(factor=3)
triple(number=2)


def simple_decorator(func):
    def wrapper():
        print("Текст до вызова функции func().")
        func()
        print("Текст после вызова функции func().")

    return wrapper


def say_hello():
    print("Привет!")


say_hello = simple_decorator(say_hello)

say_hello()


@simple_decorator
def say_hi():
    print("Снова, привет!")


say_hi()


# @simple_decorator
# def say_hello_with_name(name):
#     print(f"Привет, {name}!")


# # say_hello_with_name('Алексей')


def decorator_with_name_argument(func):
    def wrapper(name):
        print("Текст до вызова функции func().")
        func(name)
        print("Текст после вызова функции func().")

    return wrapper


@decorator_with_name_argument
def say_hello_with_name(name):
    print(f"Привет, {name}!")


say_hello_with_name("Алексей")


def decorator_with_arguments(func):
    def wrapper(*args, **kwargs):
        print("Текст до вызова функции func().")
        func(*args, **kwargs)
        print("Текст после вызова функции func().")

    return wrapper


@decorator_with_arguments
def say_hello_with_argument(name):
    print(f"Привет, {name}!")


say_hello_with_argument("Алексей")


def another_decorator(func):
    def wrapper(*args, **kwargs):
        print("Текст внутренней функции.")
        func(*args, **kwargs)

    return wrapper


@another_decorator
def return_name(name):
    return name


returned_value = return_name("Алексей")

print(returned_value)


def another_decorator(func):
    def wrapper(*args, **kwargs):
        print("Текст внутренней функции.")
        return func(*args, **kwargs)  # внутренняя функция возвращает func()

    return wrapper


@another_decorator
def return_name(name):
    return name


returned_value = return_name("Алексей")

print(returned_value)


def square(x):
    """Squares a number."""
    return x * x


square.__name__, square.__doc__


def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice
def square(x):
    """Squares a number."""
    return x * x


square(3)

square.__name__, square.__doc__


def repeat_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeat_twice
def square(x):
    """Squares a number."""
    print(x * x)


square.__name__, square.__doc__

square.__wrapped__


def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    functools.update_wrapper(wrapper, func)
    return wrapper


@repeat_twice
def power(x, n):
    """Raises to a power."""
    print(x**n)


power(2, 3)

power.__doc__


def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@logging
def power(x, n):
    return x**n


power(5, 3)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timer
def delayed_function(t):
    time.sleep(t)
    return "execution completed"


delayed_function(2)


class CatClass:

    def __init__(self, color):
        self.color = color
        self.type_ = "cat"

    def info(self):
        print(self.color, self.type_, sep=", ")


cat = CatClass(color="black")
cat.info()

# CatClass.info()

# CatClass.color


class CatClass:

    species = "кошка"  # переменная класса доступна всем экземлярам

    def __init__(self, color):
        self.color = color

    def info(self):
        print(self.color)

    @classmethod
    def get_species(cls):
        print(cls.species)
        # нет доступа к переменным color и type_


CatClass.species

CatClass.get_species()


class CatClass:

    species = "кошка"

    def __init__(self, color):
        self.color = color
        self.type_ = "cat"

    def info(self):
        print(self.color, self.type_)

    @classmethod
    def get_species(cls):
        print(cls.species)
        # нет доступа к переменным color и type_

    @staticmethod
    def convert_to_pounds(x):
        print(f"{x} kg is approximately {x * 2.205} pounds")
        # нет доступа к переменным species, color и type_


CatClass.convert_to_pounds(4)

cat = CatClass("gray")
cat.convert_to_pounds(5)


class CatClass:

    @logging
    def __init__(self, color):
        self.color = color
        self.type_ = "cat"

    @timer
    def info(self):
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat = CatClass("black")

cat.info()


@timer
class CatClass:

    def __init__(self, color):
        self.color = color
        self.type_ = "cat"

    def info(self):
        time.sleep(2)
        print(self.color, self.type_, sep=", ")


cat = CatClass("gray")

cat.info()

setattr(cat, "weight", 5)

cat.weight, getattr(cat, "weight")


def add_attribute(attribute_name, attribute_value):
    def wrapper(cls):
        setattr(cls, attribute_name, attribute_value)
        return cls

    return wrapper


@add_attribute("species", "кошка")
class CatClass:

    def __init__(self, color):
        self.color = color
        self.type_ = "cat"


CatClass.species


@logging
@timer
def delayed_function(t):
    time.sleep(t)
    return "execution completed"


delayed_function(2)


# не забудем заново объявить функцию без декораторов
def delayed_function(t):
    time.sleep(t)
    return "execution completed"


delayed_function = logging(timer(delayed_function))
delayed_function(2)


def repeat(n_times):
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n_times):
                func(*args, **kwargs)

        return wrapper

    return inner_decorator


@repeat(n_times=3)
def say_hello(name):
    print(f"Привет, {name}!")


say_hello("Алексей")
