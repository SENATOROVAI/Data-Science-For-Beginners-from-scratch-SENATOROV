"""Classes and objects in Python."""

# ## Классы и объекты в Питоне

# ### Создание класса

# #### Создание класса и метод .__init__()

# +
import numpy as np


class CatClass:
    """Temporary training function."""

    def __init__(self) -> None:
        """Temporary training function."""
        self.color = "undefined"


# -

# #### Создание объекта
#

# +
matroskin_f: CatClass = CatClass()

print(type(matroskin_f))


# -

# #### Атрибуты класса
#


class CatClass1:
    """Temporary training function."""

    def __init__(self, color: str) -> None:
        """Temporary training function."""
        self.color = color
        self.type_ = "cat"


# +
matroskin_1: CatClass1 = CatClass1("grey")

print(matroskin_1.color, matroskin_1.type_)


# -

# #### Методы класса
#


class CatClass2:
    """Temporary training class."""

    def __init__(self, color: str) -> None:
        """Temporary training function."""
        self.color = color
        self.type_ = "cat"

    def meow(self) -> None:
        """Temporary training function."""
        for _ in range(3):
            print("meow")

    def info(self) -> None:
        """Temporary training function."""
        print(self.color, self.type_)


matroskin_2: CatClass2 = CatClass2("gray")

matroskin_2.meow()

matroskin_2.info()

# ### Принципы ООП
#

# #### Инкапсуляция

matroskin_2.type_ = "dog"
print(matroskin_2.type_)


# +
class CatClass3:
    """Temporary training class."""

    def __init__(self, color: str) -> None:
        """Temporary training function."""
        self.color = color
        self.type_ = "cat"


matroskin_3: CatClass3 = CatClass3("gray")
matroskin_3.type_ = "dog"
print(matroskin_3.type_)


# +
class CatClass4:
    """Temporary training class."""

    def __init__(self, color: str) -> None:
        """Temporary training function."""
        self.color = color
        self.__type_ = "cat"

    def set_type(self, new_type: str) -> None:
        """Temporary training function."""
        self.__type_ = new_type

    def get_type(self) -> str:
        """Temporary training function."""
        return self.__type_


matroskin_4: CatClass4 = CatClass4("grey")
# -

matroskin_4.set_type("dog")
print(matroskin_4.get_type())


# +
# matroskin_4.__type_ ERROR
# -

# ### Наследование классов
#
#
#

# #### Создание родительского класса и класса-потомка


class Animal:
    """Temporary training class."""

    def __init__(self, weight: float, length: int) -> None:
        """Temporary training function."""
        self.weight = weight
        self.length = length

    def eat(self) -> None:
        """Temporary training function."""
        print("Eating")

    def sleep(self) -> None:
        """Temporary training function."""
        print("Sleeping")


class Bird(Animal):
    """Temporary training class."""

    def move(self) -> None:
        """Temporary training function."""
        print("Flying")


pigeon: Bird = Bird(0.3, 30)
print(pigeon.weight, pigeon.length)

pigeon.eat()
pigeon.move()


# #### Функция super()


# +
class Bird2(Animal):
    """Temporary training function."""

    def __init__(self, weight: float, length: int, flying_speed: int) -> None:
        """Temporary training function."""
        super().__init__(weight, length)
        self.flying_speed = flying_speed

    def move(self) -> None:
        """Temporary training function."""
        print("Flying")


pigeon_2: Bird2 = Bird2(0.3, 30, 100)

print(pigeon_2.weight, pigeon_2.length, pigeon_2.flying_speed)
# -

pigeon_2.sleep()
pigeon_2.move()


# #### Переопределение класса
#


# +
class Flightless(Bird2):
    """Temporary training class."""

    def __init__(self, weight: float, length: int, running_speed: int) -> None:
        """Temporary training function."""
        super().__init__(weight, length, flying_speed=0)
        self.running_speed = running_speed

    def move(self) -> None:
        """Temporary training function."""
        print("Running")


ostrich: Flightless = Flightless(60.0, 200, 60)
print(ostrich.running_speed)
# -

ostrich.move()
ostrich.eat()


# #### Множественное наследование
#


# +
class Fish:
    """Temporary training class."""

    def swim(self) -> None:
        """Temporary training function."""
        print("Swimming")


class Bird3:
    """Temporary training class."""

    def fly(self) -> None:
        """Temporary training function."""
        print("Flying")


class SwimmingBird(Bird3, Fish):
    """Temporary training class."""

    def demo(self) -> None:
        """Temporary training function."""
        self.fly()
        self.swim()


# -

duck: SwimmingBird = SwimmingBird()
duck.fly()
duck.swim()

# #### Полиморфизм
#
#

# # + для цифр это сложение, для строк слияние
print(2 + 2)
print("classes" + " and " + "objects")

# #### Полиморфизм функций
#
#

# +
# len можно применять ко многим последовательностям значений

print(len("programming in Python"))
print(len(["programming", "in", "Python"]))
print(len({0: "programming", 1: "in", 2: "Python"}))
# -

print(len(np.array([1, 2, 3])))

# #### Полиморфизм классов
#

# +
# Создадим объекты с одинаковыми атрибутами и методами


class CatClass5:
    """Temporary training class."""

    def __init__(self, name: str, color: str) -> None:
        """Temporary training function."""
        self.name = name
        self._type_ = "cat"
        self.color = color

    def info(self) -> None:
        """Temporary training function."""
        print(
            f"My name is {self.name}, i'm {self._type_}, color of my wool {self.color}"
        )

    def sound(self) -> None:
        """Temporary training function."""
        print("I can meow")


# -


class DogClass:
    """Temporary training class."""

    def __init__(self, name: str, color: str) -> None:
        """Temporary training function."""
        self.name = name
        self._type_ = "dog"
        self.color = color

    def info(self) -> None:
        """Temporary training function."""
        print(
            f"My name is {self.name}, i'm {self._type_}, color of my wool {self.color}"
        )

    def sound(self) -> None:
        """Temporary training function."""
        print("I can bark")


cat: CatClass5 = CatClass5("Barsik", "black")
dog: DogClass = DogClass("Barbos", "gray")

for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()

# ### Парадигмы программирования
#

patients: list[dict[str, int | str]] = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# #### Процедурное программирование
#

# +
total: int = 0
count_var: int = 0

for patient in patients:
    height_val: int = int(patient["height"])
    total += height_val
    count_var += 1

total / count_var


# -

# #### Объектно-ориентированное программирование
#


class DataClass:
    """Temporary training class."""

    def __init__(self, data: list[dict[str, int | str]]) -> None:
        """Temporary training function."""
        self.data = data

    def count_average(self, metric: str) -> float:
        """Temporary training function."""
        total_sum: int = 0
        count: int = 0

        for item in self.data:
            total_sum += int(item[metric])
            count += 1

        return total_sum / count


data_object = DataClass(patients)
print(data_object.count_average("height"))

# #### Функциональное программирование
#
#

# #### Функция map()

heights: list[int] = [int(p["height"]) for p in patients]
print(heights)

print(sum(heights) / len(heights))

# #### Функция einsum()

# +
a_arr = np.array([[0, 1, 2], [3, 4, 5]])

b_arr = np.array([[5, 4], [3, 2], [1, 0]])

print(np.einsum("ij, jk -> ik", a_arr, b_arr))
# -

# ### Классы и объекты в машинном обучении
#
#

# #### Готовые классы в библиотеке sklearn

X_ax = np.array(
    [
        1.48,
        1.49,
        1.49,
        1.50,
        1.51,
        1.52,
        1.52,
        1.53,
        1.53,
        1.54,
        1.55,
        1.56,
        1.57,
        1.57,
        1.58,
        1.58,
        1.59,
        1.60,
        1.61,
        1.62,
        1.63,
        1.64,
        1.65,
        1.65,
        1.66,
        1.67,
        1.67,
        1.68,
        1.68,
        1.69,
        1.70,
        1.70,
        1.71,
        1.71,
        1.71,
        1.74,
        1.75,
        1.76,
        1.77,
        1.77,
        1.78,
    ]
)
y_ax = np.array(
    [
        29.1,
        30.0,
        30.1,
        30.2,
        30.4,
        30.6,
        30.8,
        30.9,
        31.0,
        30.6,
        30.7,
        30.9,
        31.0,
        31.2,
        31.3,
        32.0,
        31.4,
        31.9,
        32.4,
        32.8,
        32.8,
        33.3,
        33.6,
        33.0,
        33.9,
        33.8,
        35.0,
        34.5,
        34.7,
        34.6,
        34.2,
        34.8,
        35.5,
        36.0,
        36.2,
        36.3,
        36.6,
        36.8,
        36.8,
        37.0,
        38.5,
    ]
)

X_2D = X_ax.reshape(-1, 1)
X_2D
