"""Classes."""

import numpy as np

# ### Создание класса


# создадим класс CatClass
class CatClass:
    """Простейший класс кота без атрибутов."""

    # и пропишем метод .__init__()
    def __init__(self) -> None:
        """Создать объект без атрибутов."""


# +
# создадим объект matroskin класса CatClass
matroskin = CatClass()

# проверим тип данных созданной переменной
type(matroskin)


# -


# вновь создадим класс CatClass
class CatClassColor:
    """Кот с атрибутами цвета и типа."""

    # метод .__init__() на этот раз принимает еще и параметр color
    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        # этот параметр будет записан в переменную атрибута self.color
        self.color = color

        # значение атрибута type_ задается внутри класса
        self.type_ = "cat"


# +
# повторно создадим объект класса CatClassColor, передав ему параметр цвета шерсти
matroskin_color = CatClassColor("gray")

# и выведем атрибуты класса
matroskin_color.color, matroskin_color.type_


# -


# перепишем класс CatClass
class CatClassFull:
    """Кот с атрибутами и методами мяуканья и вывода информации."""

    # метод .__init__() и атрибуты оставим без изменений
    def __init__(self, color: str) -> None:
        """Сохранить цвет и тип кота."""
        self.color = color
        self.type_ = "cat"

    # однако добавим метод, который позволит коту мяукать
    def meow(self) -> None:
        """Мяукнуть три раза."""
        for _ in range(3):
            print("Мяу")

    # и метод .info() для вывода информации об объекте
    def info(self) -> None:
        """Вывести цвет и тип кота."""
        print(self.color, self.type_)


# +
# создадим объект
matroskin_full = CatClassFull("gray")

# применим метод .meow()
matroskin_full.meow()
# -

# и метод .info()
matroskin_full.info()

# ### Принципы ООП

# Инкапсуляция

# +
# изменим атрибут type_ объекта matroskin_full на dog
matroskin_full.type_ = "dog"

# выведем этот атрибут
matroskin_full.type_


# -


class CatClassProtected:
    """Кот с защищенным (по соглашению) атрибутом _type_."""

    def __init__(self, color: str) -> None:
        """Сохранить цвет и защищенный тип кота."""
        self.color = color
        # символ подчеркивания ПЕРЕД названием атрибута указывает,
        # что это частный атрибут и изменять его не стоит
        self._type_ = "cat"


# +
# вновь создадим объект класса CatClassProtected
matroskin_protected = CatClassProtected("gray")

# и изменим значение атрибута _type_
matroskin_protected._type_ = "dog"  # pylint: disable=protected-access
matroskin_protected._type_  # pylint: disable=protected-access


# -


class CatClassPrivate:
    """Кот с приватным (name mangling) атрибутом __type_."""

    def __init__(self, color: str) -> None:
        """Сохранить цвет и приватный тип кота."""
        self.color = color
        # символ двойного подчеркивания предотвратит доступ извне
        self.__type_ = "cat"  # pylint: disable=unused-private-member


# при попытке вызова такого атрибута Питон выдаст ошибку
matroskin_private = CatClassPrivate("gray")
matroskin_private.__type_  # pylint: disable=protected-access


# Наследование классов


# создадим класс Animal
class Animal:
    """Базовое животное с весом и длиной."""

    # пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
    def __init__(self, weight: float, length: float) -> None:
        """Сохранить вес и длину животного."""
        # поместим аргументы этих параметров в соответствующие переменные
        self.weight = weight
        self.length = length

    # объявим методы .eat()
    def eat(self) -> None:
        """Покормить животное."""
        print("Eating")

    # и .sleep()
    def sleep(self) -> None:
        """Уложить животное спать."""
        print("Sleeping")


# создадим класс Bird
# родительский класс Animal пропишем в скобках
class Bird(Animal):
    """Птица, унаследованная от Animal."""

    # внутри класса Bird объявим новый метод .move()
    def move(self) -> None:
        """Показать способ передвижения птицы."""
        # для птиц .move() будет означать "летать"
        print("Flying")


# +
# создадим объект pigeon и передадим ему значения веса и длины
pigeon = Bird(0.3, 30)

# посмотрим на унаследованные у класса Animal атрибуты
pigeon.weight, pigeon.length
# -

# и методы
pigeon.eat()

# теперь вызовем метод, свойственный только классу Bird
pigeon.move()


# снова создадим класс Bird
class BirdWithSpeed(Animal):
    """Птица со скоростью полета."""

    # в метод .__init__() добавим параметр скорости полета (км/ч)
    def __init__(self, weight: float, length: float, flying_speed: float) -> None:
        """Сохранить вес, длину и скорость полета."""
        # с помощью функции super() вызовем метод .__init__() родительского класса Animal
        super().__init__(weight, length)
        self.flying_speed = flying_speed

    # вновь пропишем метод .move()
    def move(self) -> None:
        """Показать способ передвижения птицы."""
        print("Flying")


# +
# вновь создадим объект pigeon_with_speed класса BirdWithSpeed, но уже с тремя параметрами
pigeon_with_speed = BirdWithSpeed(0.3, 30, 100)

# вызовем как унаследованные, так и собственные атрибуты класса BirdWithSpeed
pigeon_with_speed.weight, pigeon_with_speed.length, pigeon_with_speed.flying_speed
# -

# вызовем унаследованный метод .sleep()
pigeon_with_speed.sleep()
# и собственный метод .move()
pigeon_with_speed.move()


# +
# Множественное наследование


# создадим родительский класс Fish
class Fish:
    """Рыба, умеющая плавать."""

    # и метод .swim()
    def swim(self) -> None:
        """Проплыть."""
        print("Swimming")


# и еще один родительский класс SimpleBird
class SimpleBird:
    """Птица, умеющая летать (без наследования от Animal)."""

    # и метод .fly()
    def fly(self) -> None:
        """Пролететь."""
        print("Flying")


# +
# теперь создадим класс-потомок этих двух классов
class SwimmingBird(SimpleBird, Fish):
    """Птица, которая умеет и летать, и плавать."""


# создадим объект duck класса SwimmingBird
duck = SwimmingBird()
# -

# как мы видим утка умеет как летать,
duck.fly()
# так и плавать
duck.swim()

# Полиморфизм

# +
# функцию len() можно применить к строке
print(len("Программирование на Питоне"))

# кроме того, она способна работать со списком
print(len(["Программирование", "на", "Питоне"]))

# словарем
print(len({0: "Программирование", 1: "на", 2: "Питоне"}))

# массивом Numpy и другими объектами
print(len(np.array([1, 2, 3])))


# +
# Полиморфизм классов


# создадим класс котов
class CatClassPoly:
    """Кот с кличкой, типом и цветом шерсти."""

    # определим атрибуты клички, типа и цвета шерсти
    def __init__(self, name: str, color: str) -> None:
        """Сохранить кличку, тип и цвет шерсти кота."""
        self.name = name
        self._type_ = "кот"
        self.color = color

    # создадим метод .info() для вывода этих атрибутов
    def info(self) -> None:
        """Вывести кличку, тип и цвет шерсти."""
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # и метод .sound(), показывающий, что коты умеют мяукать
    def sound(self) -> None:
        """Издать звук мяуканья."""
        print("Я умею мяукать")


# создадим класс собак
class DogClass:
    """Пес с кличкой, типом и цветом шерсти."""

    # с такими же атрибутами
    def __init__(self, name: str, color: str) -> None:
        """Сохранить кличку, тип и цвет шерсти пса."""
        self.name = name
        self._type_ = "пес"
        self.color = color

    # и методами
    def info(self) -> None:
        """Вывести кличку, тип и цвет шерсти."""
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # хотя, обратите внимание, действия внутри методов отличаются
    def sound(self) -> None:
        """Издать звук лая."""
        print("Я умею лаять")


# +
# Создадим объекты этих классов

cat = CatClassPoly("Бегемот", "черный")
dog = DogClass("Барбос", "серый")

# В цикле for вызовем атрибуты и методы каждого из классов
for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()
# -

# ### Парадигмы программирования

patients: list[dict[str, object]] = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# Процедурное программирование

# +
# создадим переменные для общего роста и количества пациентов
total, count = 0, 0

# в цикле for пройдемся по пациентам (отдельным словарям)
for patient in patients:
    # достанем значение роста и прибавим к текущему значению переменной total
    total += patient["height"]  # type: ignore[operator]
    # на каждой итерации будем увеличивать счетчик пациентов на один
    count += 1

# разделим общий рост на количество пациентов,
# чтобы получить среднее значение
print(total / count)


# -

# Объектно-ориентированное программирование


# создадим класс для работы с данными DataClass
class DataClass:
    """Класс для расчета среднего значения по списку словарей."""

    # при создании объекта будем передавать ему данные для анализа
    def __init__(self, data: list[dict[str, object]]) -> None:
        """Сохранить данные и объявить служебные атрибуты."""
        self.data = data
        self.metric = ""
        self.__total = 0.0
        self.__count = 0

    # кроме того, создадим метод для расчета среднего значения
    def count_average(self, metric: str) -> float:
        """Рассчитать среднее значение по указанному ключу metric."""
        # параметр metric определит, по какому столбцу считать среднее
        self.metric = metric

        # объявим два частных атрибута
        self.__total = 0.0
        self.__count = 0

        # в цикле for пройдемся по списку словарей
        for item in self.data:

            # рассчитем общую сумму по указанному в metric
            # значению каждого словаря
            self.__total += item[self.metric]  # type: ignore[operator]

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

# Функциональное программирование

# lambda-функция достанет значение по ключу height
# функция map() применит lambda-функцию к каждому вложенному в patients словарю
# функция list() преобразует результат в список
heights = list(map(lambda patient: patient["height"], patients))
heights

# воспользуемся функциями sum() и len() для нахождения среднего значения
print(sum(heights) / len(heights))  # type: ignore[arg-type]
