"""Classes."""

# ## Классы и объекты в Питоне

# ### Создание класса

# #### Создание класса и метод `.__init__()`

# +
# выполняем все необходимые импорты
import numpy as np

# создадим класс CatClass1
class CatClass1:
    """A simple class representing a cat."""

    # и пропишем метод .__init__()
    def __init__(self) -> None:
        """Initialize a cat instance with no initial attributes."""
        pass  # pylint: disable=unnecessary-pass


# -

# #### Создание объекта

# +
# создадим объект Matroskin класса CatClass1
Matroskin = CatClass1()

# проверим тип данных созданной переменной
type(Matroskin)


# -

# #### Атрибуты класса

# вновь создадим класс CatClass2
class CatClass2:
    """A cat class with attributes for color and breed."""

    # метод .__init__() на этот раз принимает еще и параметр color
    def __init__(self, color: str) -> None:
        """Initialize cat with given color."""
        # этот параметр будет записан в переменную атрибута self.color
        self.color: str = color

        # значение атрибута type_ задается внутри класса
        self.type_: str = "cat"


# +
# повторно создадим объект класса CatClass, передав ему параметр цвета шерсти
Matroskin2 = CatClass2("gray")

# и выведем атрибуты класса
print(Matroskin2.color, Matroskin2.type_)


# -

# #### Методы класса

# перепишем класс CatClass3
class CatClass3:
    """A class that models a cat with color and type attributes."""

    # метод .__init__() и атрибуты оставим без изменений
    def __init__(self, color: str) -> None:
        """Initialize the cat with a specific color."""
        self.color = color
        self.type_ = "cat"

    # однако добавим метод, который позволит коту мяукать
    def meow(self) -> None:
        """Print 'Мяу' three times to simulate the cat meowing."""
        for _ in range(3):
            print("Мяу")

    # и метод .info() для вывода информации об объекте
    def info(self) -> None:
        """Display the cat's color and type."""
        print(self.color, self.type_)


# создадим объект
Matroskin3 = CatClass3("gray")

# применим метод .meow()
Matroskin3.meow()

# и метод .info()
Matroskin3.info()

# ### Принципы ООП

# #### Инкапсуляция

# +
# изменим атрибут type_ объекта Matroskin на dog
Matroskin3.type_ = "dog"

# выведем этот атрибут
Matroskin3.type_


# -

class CatClass4:
    """A cat class with color and a protected type attribute."""

    def __init__(self, color: str) -> None:
        """Create a cat instance with the given color."""
        self.color = color
        # символ подчеркивания ПЕРЕД названием атрибута указывает,
        # что это частный атрибут и изменять его не стоит
        self._type_: str = "cat"


# +
# вновь создадим объект класса CatClass
Matroskin4 = CatClass4("gray")

# и изменим значение атрибута _type_
# Matroskin4._type_ = "dog"
# Matroskin4._type_
# -

class CatClass5:
    """A cat with a color attribute and a private type."""

    def __init__(self, color: str) -> None:
        """Initialize the cat with the specified color."""
        self.color = color
        # символ двойного подчеркивания предотвратит доступ извне
        # self.__type_: str = "cat"


# при попытке вызова такого атрибута Питон выдаст ошибку
Matroskin5 = CatClass5("gray")
# Matroskin5.__type_

# +
# поставим _CatClass перед __type_
# Matroskin5._CatClass__type_ = "dog"

# к сожалению, значение атрибута изменится
# Matroskin5._CatClass__type_
# -

# #### Наследование классов

# Создание родительского класса и класса-потомка

# создадим класс Animal
class Animal:
    """Represents an animal with weight and length attributes."""

    # пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
    def __init__(self, weight: float, length: float) -> None:
        """Initialize the animal with its weight and length."""
        # поместим аргументы этих параметров в соответствующие переменные
        self.weight = weight
        self.length = length

    # объявим методы .eat()
    def eat(self) -> None:
        """Simulate the animal eating."""
        print("Eating")

    # и .sleep()
    def sleep(self) -> None:
        """Simulate the animal sleeping."""
        print("Sleeping")

# +
# создадим класс Bird1
# родительский класс Animal пропишем в скобках


class Bird1(Animal):
    """A bird that can fly."""

    # внутри класса Bird объявим новый метод .move()
    def move(self) -> None:
        """Simulate the bird flying."""
        # для птиц .move() будет означать "летать"
        print("Flying")


# -

# создадим объект pigeon и передадим ему значения веса и длины
pigeon1 = Bird1(0.3, 30)

# посмотрим на унаследованные у класса Animal атрибуты
print(pigeon1.weight, pigeon1.length)

# и методы
pigeon1.eat()

# теперь вызовем метод, свойственный только классу Bird
pigeon1.move()


# Функция `super()`

# снова создадим класс Bird2
class Bird2(Animal):
    """A bird class that includes flying capability."""

    # в метод .__init__() добавим параметр скорости полета (км/ч)
    def __init__(self, weight: float, length: float, speed: float) -> None:
        """Initialize the bird with weight, length, and flying speed."""
        # с помощью super() вызовем метод .__init__() род. класса Animal
        super().__init__(weight, length)
        self.flying_speed = speed

    # вновь пропишем метод .move()
    def move(self) -> None:
        """Simulate the bird flying."""
        print("Flying")


# вновь создадим объект pigeon класса Bird, но уже с тремя параметрами
pigeon2 = Bird2(0.3, 30, 100)

# вызовем как унаследованные, так и собственные атрибуты класса Bird
print(pigeon2.weight, pigeon2.length, pigeon2.flying_speed)

# вызовем унаследованный метод .sleep()
pigeon2.sleep()

# и собственный метод .move()
pigeon2.move()


# Переопределение класса

# создадим подкласс Flightless класса Bird1
class Flightless(Bird1):
    """A bird subclass that cannot fly and only runs."""

    # метод .__init__() этого подкласса "стирает" .__init__() род. класса
    def __init__(  # pylint: disable=super-init-not-called
        self, running_speed: float
    ) -> None:
        """Initialize a flightless bird with its running speed."""
        # таким образом, у нас остается только один атрибут
        self.running_speed = running_speed

    # кроме того, результатом метода .move() будет 'Running'
    def move(self) -> None:
        """Simulate the flightless bird running."""
        print("Running")


# создадим объект ostrich класса Flightless
ostrich = Flightless(60)

# посмотрим на значение атрбута скорости
print(ostrich.running_speed)

# и проверим метод .move()
ostrich.move()

# подкласс Flightless сохранил методы всех родительских классов
ostrich.eat()


# Множественное наследование

# создадим родительский класс Fish
class Fish:
    """Base class representing a fish that can swim."""

    # и метод .swim()
    def swim(self) -> None:
        """Simulate the fish swimming."""
        print("Swimming")


# и еще один родительский класс Bird3
class Bird3:
    """A base class representing birds capable of flying."""

    # и метод .fly()
    def fly(self) -> None:
        """Simulate the bird flying."""
        print("Flying")


# теперь создадим класс-потомок этих двух классов
class SwimmingBird(Bird3, Fish):
    """A bird class that can swim like a fish and fly like a bird."""

    pass  # pylint: disable=unnecessary-pass


# создадим объект duck класса SwimmingBird
duck = SwimmingBird()

# как мы видим утка умеет как летать,
duck.fly()

# так и плавать
duck.swim()

# #### Полиморфизм

# для чисел '+' является оператором сложения
print(2 + 2)

# для строк - оператором объединения
print("классы" + " и " + "объекты")

# 1. Полиморфизм функций

# функцию len() можно применить к строке
len("Программирование на Питоне")

# кроме того, она способна работать со списком
len(["Программирование", "на", "Питоне"])

# словарем
len({0: "Программирование", 1: "на", 2: "Питоне"})

len(np.array([1, 2, 3]))


# 2. Полиморфизм классов

# Создадим объекты с одинаковыми атрибутами и методами

# создадим класс котов
class CatClass6:
    """Class representing a cat with name, type, and fur color attributes."""

    # определим атрибуты клички, типа и цвета шерсти
    def __init__(self, name: str, color: str) -> None:
        """Initialize the cat with a name and fur color."""
        self.name = name
        self._type_ = "кот"
        self.color = color

    # создадим метод .info() для вывода этих атрибутов
    def info(self) -> None:
        """Display information about the cat."""
        print(f"Меня зовут {self.name}, я {self._type_}")
        print(f"цвет моей шерсти {self.color}")

    # и метод .sound(), показывающий, что коты умеют мяукать
    def sound(self) -> None:
        """Print the sound a cat makes."""
        print("Я умею мяукать")


# создадим класс собак
class DogClass:
    """Class representing a dog with name, type, and fur color attributes."""

    # с такими же атрибутами
    def __init__(self, name: str, color: str) -> None:
        """Initialize the dog with a name and fur color."""
        self.name = name
        self._type_ = "пес"
        self.color = color

    # и методами
    def info(self) -> None:
        """Display information about the dog."""
        print(f"Меня зовут {self.name}, я {self._type_}")
        print(f"цвет моей шерсти {self.color}")

    # хотя, обратите внимание, действия внутри методов отличаются
    def sound(self) -> None:
        """Print the sound a dog makes."""
        print("Я умею лаять")


# Создадим объекты этих классов

cat = CatClass6("Бегемот", "черный")
dog = DogClass("Барбос", "серый")

# В цикле `for` вызовем атрибуты и методы каждого из классов

for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()

# ### Парадигмы программирования

patients: list[dict[str, str | int]] = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# #### Процедурное программирование

# +
# создадим переменные для общего роста и количества пациентов
total, count = 0, 0

# в цикле for пройдемся по пациентам (отдельным словарям)
for patient in patients:
    # достанем значение роста и прибавим к текущему значению переменной total
    total += int(patient["height"])
    # на каждой итерации будем увеличивать счетчик пациентов на один
    count += 1

# разделим общий рост на количество пациентов,
# чтобы получить среднее значение
print(total / count)


# -

# #### Объектно-ориентированное программирование

# создадим класс для работы с данными DataClass
class DataClass:
    """Class for performing basic statistical calculations on data."""

    # при создании объекта будем передавать ему данные для анализа
    def __init__(self, data: list[dict[str, str | int]]) -> None:
        """Initialize the object with data for analysis."""
        self.data = data
        self.metric = ""
        self.__total = 0
        self.__count = 0

    # кроме того, создадим метод для расчета среднего значения
    def count_average(self, metric: str) -> float:
        """Calculate the average value for the specified metric."""
        # параметр metric определит, по какому столбцу считать среднее
        self.metric = metric

        # объявим два частных атрибута
        self.__total = 0
        self.__count = 0

        # в цикле for пройдемся по списку словарей
        for item in self.data:

            # рассчитем общую сумму по указанному в metric
            # значению каждого словаря
            self.__total += int(item[self.metric])

            # и количество таких записей
            self.__count += 1

        # разделим общую сумму показателя на количество записей
        return self.__total / self.__count


# +
# создадим объект класса DataClass и передадим ему данные о пациентах
data_object = DataClass(patients)

# вызовем метод .count_average() с метрикой 'height'
data_object.count_average("height")
# -

# #### Функциональное программирование

# Функция map()

# lambda-функция достанет значение по ключу height
# функция map() применит lambda-функцию к каждому вложенному в patients словарю
# функция list() преобразует результат в список
heights = list(map(lambda x: int(x["height"]), patients))
print(heights)

# воспользуемся функциями sum() и len() для нахождения среднего значения
print(sum(heights) / len(heights))

# Функция einsum()

# +
# возьмем два двумерных массива
a_var = np.array([[0, 1, 2], [3, 4, 5]])

b_var = np.array([[5, 4], [3, 2], [1, 0]])
# -

# перемножим a и b по индексу j через функцию np.einsum()
np.einsum("ij, jk -> ik", a_var, b_var)
