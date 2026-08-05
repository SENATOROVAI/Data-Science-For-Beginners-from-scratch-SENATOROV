"""OOP classes and objects."""

# +
import numpy as np


class CatClass:

    def __init__(self):
        pass


# +
Matroskin = CatClass()

type(Matroskin)


# -


class CatClass:

    def __init__(self, color):
        self.color = color
        self.type_ = "cat"


# +
Matroskin = CatClass("gray")

Matroskin.color, Matroskin.type_


# -


class CatClass:

    def __init__(self, color):
        self.color = color
        self.type = "cat"

    def meow(self):
        for i in range(3):
            print("Мяу")

    def info(self):
        print(self.color, self.type)


Matroskin = CatClass("gray")

Matroskin.meow()

Matroskin.info()

# +
Matroskin.type_ = "dog"

Matroskin.type_


# -


class CatClass:

    def __init__(self, color):
        self.color = color
        self._type_ = "cat"


# +
Matroskin = CatClass("gray")

Matroskin._type_ = "dog"
Matroskin._type_


# -


class CatClass:

    def __init__(self, color):
        self.color = color
        self.__type_ = "cat"


# +
Matroskin = CatClass("gray")

Matroskin.__type_

# +
Matroskin._CatClass__type_ = "dog"

Matroskin._CatClass__type_


# -


class Animal:

    def __init__(self, weight, lenght):
        self.weight = weight
        self.lenght = lenght

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Bird(Animal):

    def move(self):

        print("Flying")


pigeon = Bird(0.3, 30)

pigeon.weight, pigeon.lenght

pigeon.eat()

pigeon.move()


class Bird(Animal):

    def __init__(self, weight, lenght, flying_speed):
        super().__init__(weight, lenght)
        self.flying_speed = flying_speed

    def move(self):
        print("Flying")


pigeon = Bird(0.3, 30, 100)

pigeon.weight, pigeon.lenght, pigeon.flying_speed

pigeon.sleep()

pigeon.move()


class Flightless(Bird):

    def __init__(self, running_speed):

        self.running_speed = running_speed

    def move(self):
        print("Running")


ostrich = Flightless(60)

ostrich.running_speed

ostrich.move()

ostrich.eat()


class Fish:

    def swim(self):
        print("Swimming")


class Bird:

    def fly(self):
        print("Flying")


class SwimmingBird(Bird, Fish):
    pass


duck = SwimmingBird()

duck.fly()

duck.swim()

2 + 2
"классы" + " и " + "объекты"

len("Программирование на Python — это просто!")

len(["Программирование", "на", "Питоне"])

len({0: "Программирование", 1: "на", 2: "Питоне"})

len(np.array([1, 2, 3]))


class CatClass:

    def __init__(self, name, color):
        self.name = name
        self._type_ = "кот"
        self.color = color

    def info(self):
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    def sound(self):
        print("Я умею мяукать")


class DogClass:

    def __init__(self, name, color):
        self.name = name
        self._type_ = "пес"
        self.color = color

    def info(self):
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    def sound(self):
        print("Я умею лаять")


cat = CatClass("Бегемот", "черный")
dog = DogClass("Барбос", "серый")

for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()

patients = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# +
total, count = 0, 0

for patient in patients:

    total += patient["height"]

    count += 1

total / count


# -


class DataClass:

    def __init__(self, data):
        self.data = data

    def count_average(self, metric):

        self.metric = metric

        self.__total = 0
        self.__count = 0

        for item in self.data:

            self.__total += item[self.metric]

            self.__count += 1

        return self.__total / self.__count


# +
data_object = DataClass(patients)

data_object.count_average("height")

# +
heights = list(map(lambda x: x["height"], patients))

heights
# -

sum(heights) / len(heights)

# +
a = np.array([[0, 1, 2], [3, 4, 5]])

b = np.array([[5, 4], [3, 2], [1, 0]])
# -

np.einsum("ij, jk -> ik", a, b)
