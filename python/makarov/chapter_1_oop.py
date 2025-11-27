"""ООП."""

# +
# создадим класс для работы с данными DataClass
# from typing import Dict, List, Union

# # возьмем два двумерных массива
# import numpy as np


# class CatClass:
#     def __init__(self) -> None:
#         pass

# +
# Matrsokin = CatClass()
# type(Matrsokin)

# +
# Атрибуты класса
# Давайте дополним наш класс
# CatClass атрибутом типа (назовем его type_)
# и атрибутом цвета шерсти (color).


# class CatClass:
#     color: str
#     type_: str

#     def __init__(self, color: str) -> None:
#         self.color = color
#         self.type_ = "cat"

# +
# # Названия атрибутов могут быть любыми.
# При этом, обратите внимание,
# чтобы избежать конфликта с
# названием встроенноей функции type(),
# мы снабдили наш атрибут символом
# нижнего подчеркивания _.
# # повторно создадим объект класса CatClass,
# передав ему параметр цвета шерсти
# Matroskin = CatClass("gray")

# # и выведем атрибуты класса
# Matroskin.color, Matroskin.type_

# +
# Методы класса
# Дополним наш класс возможностью
# выполнять определенные действия (то есть # создадим методы класса).


# class CatClass:
#     color: str
#     type_: str

#     def __init__(self, color) -> None:
#         self.color = color
#         self.type_ = "cat"

#     def meow(self) -> None:
#         for meooww in range(3):
#             print("Мяу")

#     def info(self) -> None:
#         print(self.color, self.type_)

# +
# Matroskin = CatClass("gray")
# Matroskin.meow()

# +
# Matroskin.info()

# +
# # Принципы объектно-ориентированного программирования
# # Продолжим изучать тему классов
# и объектов и рассмотрим некоторые
# принципы объектно-ориентированного программирования

# # Инкапсуляция
# # Инкапсуляция (encapsulation) —
# это способность класса хранить данные
# и методы внутри себя. Другими словами,
# объект класса можно представить
# в виде капсулы, в которой содержатся
# необходимые данные и методы.

# # Публичные и частные атрибуты класса
# # С понятием инкапсуляции тесно
# связаны понятия публичных
# и частных атрибутов
# (public and private attributes).
# Публичные атрибуты — это те атрибуты,
# к которым можно получить доступ за пределами «капсулы» класса.

# # изменим атрибут type_ объекта Matroskin на dog
# Matroskin.type_ = "dog"

# # выведем этот атрибут
# Matroskin.type_

# +
# class CatClass:
#     color: str
#     _type_: str

#     def __init__(self, color: str) -> None:
#         self.color = color

#         self._type_ = "cat"

# +
# # вновь создадим объект класса CatClass
# Matroskin = CatClass("gray")

# # и изменим значение атрибута _type_
# Matroskin._type_ = "dog"
# Matroskin._type_

# +
# class CatClass:
#     __type_: str
#     color: str

#     def __init__(self, color):
#         self.color = color
#
#         self.__type_ = "cat"

# +
# Matroskin = CatClass("gray")

# Matroskin.__type_

# +
# # поставим _CatClass перед __type_,
# # изменим значение атрибута и
# Matroskin._CatClass__type_ = "dog"

# # выведем его
# Matroskin._CatClass__type_

# +
# # Наследование
# # Принцип наследования (inheritance) предполагает,
# что один класс наследует атрибуты и методы другого.
# В этом случае, говорят про
# Родителя или Суперкласс (parent class, base class)
# и Потомка или Подкласс (child class, derived class).
# # Создание родительского класса и класса-потомка


# class Animal:
#     weight: int
#     length: int

#     def __init__(self, weight: int, length: int) -> None:
#
#         self.weight = weight
#         self.length = length

#     # объявим методы .eat()

#     def eat(self) -> None:
#         print("Eating")

#     def sleep(self) -> None:
#         print("Sleeping")

# +
# class Bird(Animal):
#     def move(self) -> None:
#         print("Flying")


# # создадим объект pigeon
# и передадим ему значения веса и длины
# pigeon = Bird(0.3, 30)

# +
# # посмотрим на унаследованные
# у класса Animal атрибуты
# pigeon.weight, pigeon.length

# +
# # и методы
# pigeon.eat()

# +
# pigeon.move()

# +
# # Обратите внимание, в предыдущем
# примере класс Bird получил только
# новые методы, новых атрибутов в нем не появилось.
# Все дело в том,
# что если мы хотим добавить атрибут
# в классе-потомке, сохранив атрибуты
# родительского класса, нам нужно явным образом
# вызвать последние с помощью функции super().


# class Bird(Animal):
#     weight: int
#     length: int
#     flying_speed: int

#     def __init__(self, weight: int, length: int, flying_speed: int) -> None:
#         super().__init__(weight, length)
#         self.flying_speed = flying_speed

#     # вновь пропишем метод .move()

#     def move(self) -> None:
#         print("Flying")

# +
# # вновь создадим объект pigeon класса
# Bird, но уже с тремя параметрами
# pigeon = Bird(0.3, 30, 100)

# +
# # вызовем как унаследованные,
# так и собственные атрибуты класса Bird
# pigeon.weight, pigeon.length, pigeon.flying_speed

# +
# # вызовем унаследованный метод .sleep()
# pigeon.sleep()

# +
# # и собственный метод .move()
# pigeon.move()

# +
# class Flightless(Bird):
#     running_speed: int

#     def __init__(self, running_speed: int) -> None:
#         self.running_speed = running_speed

#     # кроме того, результатом метода .move() будет 'Running'

#     def move(self) -> None:
#         print("Running")

# +
# ostrich = Flightless(60)

# +
# # страусы бегают довольно быстро
# ostrich.running_speed

# +
# ostrich.move()

# +
# # применим метод .eat() класса Animal
# ostrich.eat()

# +
# # Множественное наследование
# # Питон позволяет классу наследовать
# методы двух и более классов


# class Fish:
#     def swim(self) -> None:
#         print("Swim")


# class Bird:
#     def fly(self) -> None:
#         print("Flying")

# +
# # родительские классы мы перечисляем
# в скобках через зяпятую


# class SwimmingBird(Bird, Fish):
#     pass

# +
# duck = SwimmingBird()
# duck.fly()

# +
# duck.swim()

# +
# # Полиморфизм
# # Полиморфизм (polymorphism) означает,
# что один и тот же объект может принимать разные формы.
# В программировании, полиморфизм предполагает,
# что операторы, функции и объекты
# могут взаимодействовать с различными типами данных.

# # для чисел '+' является оператором сложения
# 2 + 2


# # для строк - оператором объединения
# "классы" + " и " + "объекты"

# +
# # Полиморфизм функций
# # Полиморфные функции (polymorphic functions) —
# это функции, которые могут работать
# с разными типами данных.
# Классическим примером является встроенная функция len().


# class CatClass:
#     name: str
#     color: str
#     _type_: str

#     def __init__(self, name: str, color: str):
#         self.name = name
#         self._type_ = "кот"
#         self.color = color

#     # создадим метод .info() для вывода этих атрибутов

#     def info(self):
#         print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

#     def sound(self):
#         print("Я умею мяукать")

# +
# class DogClass:
#     name: str
#     color: str
#     _type_: str

#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self._type_ = "пес"
#         self.color = color

#     # и методами

#     def info(self) -> None:
#         print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

#     # хотя, обратите внимание, действия внутри методов отличаются
#     def sound(self) -> None:
#         print("Я умею лаять")

# +
# cat = CatClass("Бегемот", "черный")
# dog = DogClass("Барбос", "серый")

# +
# for animal in (cat, dog):
#     animal.info()
#     animal.sound()
#     print()

# +
# Парадигма программирования
# Парадигма программирования — это,
# по большому счету, способ организации
# и стиль написания кода.
# Создание различных парадигм необходимо для того,
# чтобы справиться со все возрастающей
# сложностью компьютерных программ.

# +
# # Например, у нас есть список словарей
# с данными пациентов, и нам нужно посчитать их средний рост.
# patients = [
#     {"name": "Николай", "height": 178},
#     {"name": "Иван", "height": 182},
#     {"name": "Алексей", "height": 190},
# ]

# # создадим переменные для общего роста и количества пациентов
# total, count = 0, 0

# # в цикле for пройдемся по пациентам (отдельным словарям)
# for patient in patients:
#     # достанем значение роста и прибавим
# к текущему значению переменной total
#     total += patient["height"]
#     # на каждой итерации будем увеличивать счетчик пациентов на один
#     count += 1

# # разделим общий рост на количество пациентов,
# # чтобы получить среднее значение
# total / count

# +
# class DataClass:
#     data: List[Dict[str, Union[int, float]]]
#     metric: str
#     __total: float
#     __count: int

#     def __init__(self, data: List[Dict[str, Union[int, float]]]) -> None:
#         self.data = data

#     def count_average(self, metric: str) -> float:
#         self.metric = metric

#         self.__total = 0.0
#         self.__count = 0

#         for item in self.data:
#             self.__total += item[self.metric]
#             self.__count += 1

#         return self.__total / self.__count

# +
# # создадим объект класса DataClass
# и передадим ему данные о пациентах
# data_object = DataClass(patients)

# # вызовем метод .count_average() с метрикой 'height'
# data_object.count_average("height")

# +
# # функция list() преобразует результат в список
# heights = list(map(lambda x: x["height"], patients))
# heights

# +
# sum(heights) / len(heights)

# +
# a = np.array([[0, 1, 2], [3, 4, 5]])

# b = np.array([[5, 4], [3, 2], [1, 0]])


# # перемножим a и b по индексу j через функцию np.einsum()
# np.einsum("ij, jk -> ik", a, b)
