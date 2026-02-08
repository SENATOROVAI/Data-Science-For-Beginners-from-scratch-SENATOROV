"""ООП.Классы и объекты."""

# ## Классы и объекты в Питоне

# ### Создание класса

# #### Создание класса и метод `.__init__()`

# +
import numpy as np


class CatClass:
    """Класс кота."""

    def __init__(self) -> None:
        """Объявление экземпляра кота."""


# -

# #### Создание объекта

Matroskin = CatClass()
type(Matroskin)


# #### Атрибуты класса


class CatClass1:
    """Класс кота."""

    def __init__(self, color: str) -> None:
        """Объявление экземпляра кота.

        Args:
            color (str): Цвет кота
        """
        self.color = color
        self.type_ = "cat"


Matroskin1 = CatClass1("gray")
Matroskin1.color, Matroskin1.type_


# #### Методы класса


class CatClass2:
    """Класс кота."""

    def __init__(self, color: str) -> None:
        """Объявление экземпляра кота.

        Args:
            color (str): Цвет кота
        """
        self.color = color
        self.type_ = "cat"

    def meow(self) -> None:
        """Кот мяукает."""
        for _ in range(3):
            print("Мяу")

    def info(self) -> None:
        """Информация о коте."""
        print(self.color, self.type_)


Matroskin2 = CatClass2("gray")
Matroskin2.meow()

Matroskin2.info()

# ### Принципы ООП

# #### Инкапсуляция

Matroskin2.type_ = "dog"
Matroskin2.type_


class CatClass3:
    """Класс кота."""

    def __init__(self, color: str) -> None:
        """Объявление экземпляра кота.

        Args:
            color (str): Цвет кота
        """
        self.color = color
        # символ подчёркивания ПЕРЕД названием атрибута указывает,
        # что это частный атрибут и изменять его не стоит
        self._type_ = "cat"


Matroskin3 = CatClass3("gray")


# Этот код выдаст предупреждение, но не ошибку:
# ```python
# Matroskin3._type_ = "dog"
# ```


class CatClass4:
    """Класс кота."""

    def __init__(self, color: str) -> None:
        """Объявление экземпляра кота.

        Args:
            color (str): Цвет кота
        """
        self.color = color
        self.__type_ = "cat"
        print(self.__type_)


Matroskin4 = CatClass4("gray")


# Попытка обратится через dot-нотацию вызовет ошибку:
# ```python
# Matroskin4.__type_
# ```

# Но всё еще можно получить доступ по:
# ```python
# Matroskin4._CatClass__type_ = "dog"
# ```

# ### Наследование классов

# #### Создание родительского класса и класса-потомка


class Animal:
    """Класс животного."""

    def __init__(self, weight: int | float, length: int | float) -> None:
        """Объявление экземпляра животного.

        Args:
            weight (int|float): Вес птицы
            length (int|float): Рост птицы
        """
        self.weight = weight
        self.length = length

    def eat(self) -> None:
        """Животное ест."""
        print("Eating")

    def sleep(self) -> None:
        """Животное спит."""
        print("Sleeping")


class Bird(Animal):
    """Класс птицы.

    Args:
        Animal: Родительский класс животного
    """

    def move(self) -> None:
        """Основной способ перемещения птиц."""
        print("Flying")


pigeon = Bird(0.3, 30)
pigeon.weight, pigeon.length

pigeon.eat()

pigeon.move()


# #### Функция `super()`


class Bird1(Animal):
    """Класс птицы.

    Args:
        Animal: Родительский класс животного
    """

    def __init__(
        self, weight: int | float, length: int | float, flying_speed: float
    ) -> None:
        """Объявление экземпляра класса птицы.

        Args:
            weight (int|float): Вес птицы
            length (int|float): Рост птицы
            flying_speed (float): Скорость полёта птицы
        """
        super().__init__(weight, length)
        self.flying_speed = flying_speed

    def move(self) -> None:
        """Основной способ перемещения птиц."""
        print("Flying")


pigeon1 = Bird1(0.3, 30, 100)
pigeon1.weight, pigeon1.length, pigeon1.flying_speed

pigeon1.sleep()

pigeon1.move()


# #### Переопределение класса


class Flightless(Bird1):
    """Класс нелетающих птиц.

    Args:
        Bird1 : Родительский класс птиц
    """

    def __init__(
        self, weight: int | float, length: int | float, running_speed: float
    ) -> None:
        """Объявление экземпляра класса нелетающих птиц.

        Args:
            running_speed (float): Скорость бега птицы
            weight (int|float): Вес птицы
            length (int|float): Рост птицы
        """
        super().__init__(weight, length, 0)
        self.running_speed = running_speed

    def move(self) -> None:
        """Нелетающая птица бежит."""
        print("Running")


ostrich = Flightless(60, 20, 30)
ostrich.running_speed

ostrich.move()

ostrich.eat()


# #### Множественное наследование


# +
class Fish:
    """Класс рыбы."""

    def swim(self) -> None:
        """Рыба плывет."""
        print("Swimming")


class Bird2:
    """Класс птицы."""

    def fly(self) -> None:
        """Птица летит."""
        print("Flying")


class SwimmingBird(Bird2, Fish):
    """Класс плавающих птиц.

    Args:
        Bird: Родительский класс птиц
        Fish: Второй родительский класс птиц
    """


# -

duck = SwimmingBird()
duck.fly()

duck.swim()

# #### Полиформизм

print(2 + 2)

print("классы" + " и " + "объекты")

# 1. Полиформизм функций

len("Программирование на Питоне")

len(["Программирование", "на", "Питоне"])

len({0: "Программирование", 1: "на", 2: "Питоне"})

len(np.array([1, 2, 3]))


# 2. Полиморфизм классов

# Создадим объекты с одинаковыми атрибутами и методами


class CatClass5:
    """Класс кота."""

    def __init__(self, name: str, color: str) -> None:
        """Объявление экземпляра кота.

        Args:
            color (str): Цвет кота
        """
        self.name = name
        self._type_ = "кот"
        self.color = color

    def info(self) -> None:
        """Информация о коте."""
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    def sound(self) -> None:
        """Издаваемые звуки."""
        print("Я умею лаять")


class DogClass:
    """Класс собаки."""

    def __init__(self, name: str, color: str) -> None:
        """Объявление экземпляра собаки.

        Args:
            color (str): Цвет собаки
        """
        self.name = name
        self._type_ = "пёс"
        self.color = color

    def info(self) -> None:
        """Информация о собаке."""
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    def sound(self) -> None:
        """Издаваемые звуки."""
        print("Я умею лаять")


# Создадим объекты этих классов

cat = CatClass5("Бегемот", "чёрный")
dog = DogClass("Барбос", "серый")

# В цикле `for` вызовем атрибуты и методы каждого из классов

for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()

# ### Парадигмы программирования

patients = [
    {"name": "Николай", "height": "178"},
    {"name": "Иван", "height": "182"},
    {"name": "Алексей", "height": "190"},
]

# #### Процедурное программирование

# +
total, count = 0, 0
for patient in patients:
    total += int(patient["height"])
    count += 1

total / count


# -

# #### Объектно-ориентированное программирование


class DataClass:
    """Класс информации."""

    def __init__(self, data: list[dict[str, str]]) -> None:
        """Объявление экземпляра класса информации.

        Args:
            data (list[dict[str: str]]): Информация в массиве словарей
        """
        self.data = data
        self.metric: None | str = None
        self.__count: None | int = None
        self.__total: None | int = None

    def count_average(self, metric: str) -> float | int:
        """Подсчёт среднего по определённой метрике."""
        self.metric = metric
        self.__total = 0
        self.__count = 0
        for item in self.data:
            self.__total += int(item[self.metric])
            self.__count += 1

        return self.__total / self.__count


data_object = DataClass(patients)
data_object.count_average("height")

# #### Функциональное программирование

# Функция map()

heights = list(map(lambda x: int(x["height"]), patients))
heights

print(sum(heights) / len(heights))

# Функция einsum()

# +
matrix_a = np.array([[0, 1, 2], [3, 4, 5]])

matrix_b = np.array([[5, 4], [3, 2], [1, 0]])
# -

np.einsum("ij, jk -> ik", matrix_a, matrix_b)

#
