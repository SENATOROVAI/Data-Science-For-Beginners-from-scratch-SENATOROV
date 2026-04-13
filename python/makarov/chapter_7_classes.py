"""Классы."""

# Создание класса.

# Создание класса и метод .__init__()

# +
# создадим класс CatClass
# массивом Numpy и другими объектами
# import numpy as np


# class CatClass:

# и пропишем метод .__init__()
# def __init__(self):
# pass
# -

# Создание объекта

# +
# создадим объект Matroskin класса CatClass
# Matroskin = CatClass()

# проверим тип данных созданной переменной
# type(Matroskin)
# -

# Атрибуты класса

# +
# вновь создадим класс CatClass


# class CatClass:

# метод .__init__() на этот раз принимает еще и параметр color
# def __init__(self, color):

# этот параметр будет записан в переменную атрибута self.color
# self.color = color

# значение атрибута type_ задается внутри класса
# self.type_ = "cat"

# +
# повторно создадим объект класса CatClass, передав ему параметр цвета шерсти
# Matroskin = CatClass("gray")

# и выведем атрибуты класса
# Matroskin.color, Matroskin.type_
# -

# Методы класса

# +
# перепишем класс CatClass


# class CatClass:

# метод .__init__() и атрибуты оставим без изменений
# def __init__(self, color):
# self.color = color
# self.type_ = "cat"

# однако добавим метод, который позволит коту мяукать
# def meow(self):
# for i in range(3):
# print("Мяу")

# и метод .info() для вывода информации об объекте
# def info(self):
# print(self.color, self.type_)

# +
# создадим объект
# Matroskin = CatClass("gray")

# +
# применим метод .meow()
# Matroskin.meow()

# +
# и метод .info()
# Matroskin.info()
# -

# Принципы ООП

# Инкапсуляция

# +
# изменим атрибут type_ объекта Matroskin на dog
# Matroskin.type_ = "dog"

# выведем этот атрибут
# Matroskin.type_

# +
# class CatClass:

# def __init__(self, color):
# self.color = color
# символ подчеркивания ПЕРЕД названием атрибута указывает,
# что это частный атрибут и изменять его не стоит
# self._type_ = "cat"

# +
# вновь создадим объект класса CatClass
# Matroskin = CatClass("gray")

# и изменим значение атрибута _type_
# Matroskin._type_ = "dog"
# Matroskin._type_

# +
# class CatClass:

# def __init__(self, color):
# self.color = color
# символ двойного подчеркивания предотвратит доступ извне
# self.__type_ = "cat"

# +
# при попытке вызова такого атрибута Питон выдаст ошибку
# Matroskin = CatClass("gray")
# Matroskin.__type_

# +
# поставим _CatClass перед __type_
# Matroskin._CatClass__type_ = "dog"

# к сожалению, значение атрибута изменится
# Matroskin._CatClass__type_
# -

# Наследование классов

# Создание родительского класса и класса-потомка

# +
# создадим класс Animal


# class Animal:

# пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
# def __init__(self, weight, length):

# поместим аргументы этих параметров в соответствующие переменные
# self.weight = weight
# self.length = length

# объявим методы .eat()
# def eat(self):
# print("Eating")

# и .sleep()
# def sleep(self):
# print("Sleeping")

# +
# создадим класс Bird
# родительский класс Animal пропишем в скобках


# class Bird(Animal):

# внутри класса Bird объявим новый метод .move()
# def move(self):

# для птиц .move() будет означать "летать"
# print("Flying")

# +
# создадим объект pigeon и передадим ему значения веса и длины
# pigeon = Bird(0.3, 30)

# +
# посмотрим на унаследованные у класса Animal атрибуты
# pigeon.weight, pigeon.length

# +
# и методы
# pigeon.eat()

# +
# теперь вызовем метод, свойственный только классу Bird
# pigeon.move()
# -

# Функция super()

# +
# снова создадим класс Bird


# class Bird(Animal):

# в метод .__init__() добавим параметр скорости полета (км/ч)
# def __init__(self, weight, length, flying_speed):

# с помощью функции super() вызовем метод .__init__() родительского класса Animal
# super().__init__(weight, length)
# self.flying_speed = flying_speed

# вновь пропишем метод .move()
# def move(self):
# print("Flying")

# +
# вновь создадим объект pigeon класса Bird, но уже с тремя параметрами
# pigeon = Bird(0.3, 30, 100)

# +
# вызовем как унаследованные, так и собственные атрибуты класса Bird
# pigeon.weight, pigeon.length, pigeon.flying_speed

# +
# вызовем унаследованный метод .sleep()
# pigeon.sleep()

# +
# и собственный метод .move()
# pigeon.move()
# -

# Переопределение класса

# +
# создадим подкласс Flightless класса Bird


# class Flightless(Bird):

# метод .__init__() этого подкласса "стирает" .__init__() родительского класса
# def __init__(self, running_speed):

# таким образом, у нас остается только один атрибут
# self.running_speed = running_speed

# кроме того, результатом метода .move() будет 'Running'
# def move(self):
# print("Running")

# +
# создадим объект ostrich класса Flightless
# ostrich = Flightless(60)

# +
# посмотрим на значение атрбута скорости
# ostrich.running_speed

# +
# и проверим метод .move()
# ostrich.move()

# +
# подкласс Flightless сохранил методы всех родительских классов
# ostrich.eat()
# -

# Множественное наследование

# +
# создадим родительский класс Fish


# class Fish:

# и метод .swim()
# def swim(self):
# print("Swimming")

# +
# и еще один родительский класс Bird


# class Bird:

# и метод .fly()
# def fly(self):
# print("Flying")

# +
# теперь создадим класс-потомок этих двух классов


# class SwimmingBird(Bird, Fish):
# pass

# +
# создадим объект duck класса SwimmingBird
# duck = SwimmingBird()

# +
# как мы видим утка умеет как летать,
# duck.fly()

# +
# так и плавать
# duck.swim()
# -

# Полиморфизм

# +
# для чисел '+' является оператором сложения
# 2 + 2

# +
# для строк - оператором объединения
# "классы" + " и " + "объекты"
# -

# 1 Полиморфизм функций

# +
# функцию len() можно применить к строке
# len("Программирование на Питоне")

# +
# кроме того, она способна работать со списком
# len(["Программирование", "на", "Питоне"])

# +
# словарем
# len({0: "Программирование", 1: "на", 2: "Питоне"})

# +
# len(np.array([1, 2, 3]))
# -

# 2 Полиморфизм классов

# Создадим атрибуты с одинаковыми объектами и методами

# +
# создадим класс котов


# class CatClass:

# определим атрибуты клички, типа и цвета шерсти
# def __init__(self, name, color):
# self.name = name
# self._type_ = "кот"
# self.color = color

# создадим метод .info() для вывода этих атрибутов
# def info(self):
# print(f"Меня зовут {self.name}, я {self._type_},
# цвет моей шерсти {self.color}")

# и метод .sound(), показывающий, что коты умеют мяукать
# def sound(self):
# print("Я умею мяукать")

# +
# создадим класс собак


# class DogClass:

# с такими же атрибутами
# def __init__(self, name, color):
# self.name = name
# self._type_ = "пес"
# self.color = color

# и методами
# def info(self):
# print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

# хотя, обратите внимание, действия внутри методов отличаются
# def sound(self):
# print("Я умею лаять")
# -

# Создадим объекты этих классов

# +
# cat = CatClass("Бегемот", "черный")
# dog = DogClass("Барбос", "серый")
# -

# В цикле for вызовем атрибуты и методы каждого из классов

# +
# for animal in (cat, dog):
# animal.info()
# animal.sound()
# print()
# -

# Парадигмы программирования

# +
# patients = [
# {"name": "Николай", "height": 178},
# {"name": "Иван", "height": 182},
# {"name": "Алексей", "height": 190},
# ]
# -

# Процедурное программирование

# +
# создадим переменные для общего роста и количества пациентов
# total, count = 0, 0

# в цикле for пройдемся по пациентам (отдельным словарям)
# for patient in patients:
# достанем значение роста и прибавим к текущему значению переменной total
# total += patient["height"]
# на каждой итерации будем увеличивать счетчик пациентов на один
# count += 1

# разделим общий рост на количество пациентов,
# чтобы получить среднее значение
# total / count
# -

# Объектно-ориентированное программирование

# +
# создадим класс для работы с данными DataClass


# class DataClass:

# при создании объекта будем передавать ему данные для анализа
# def __init__(self, data):
# self.data = data

# кроме того, создадим метод для расчета среднего значения
# def count_average(self, metric):

# параметр metric определит, по какому столбцу считать среднее
# self.metric = metric

# объявим два частных атрибута
# self.__total = 0
# self.__count = 0

# в цикле for пройдемся по списку словарей
# for item in self.data:

# рассчитем общую сумму по указанному в metric
# значению каждого словаря
# self.__total += item[self.metric]

# и количество таких записей
# self.__count += 1

# разделим общую сумму показателя на количество записей
# return self.__total / self.__count

# +
# создадим объект класса DataClass и передадим ему данные о пациентах
# data_object = DataClass(patients)

# вызовем метод .count_average() с метрикой 'height'
# data_object.count_average("height")
# -

# Функциональное программирование

# Функция map()

# +
# lambda-функция достанет значение по ключу height
# функция map() применит lambda-функцию к каждому вложенному в patients словарю
# функция list() преобразует результат в список
# heights = list(map(lambda x: x["height"], patients))
# heights

# +
# воспользуемся функциями sum() и len() для нахождения среднего значения
# sum(heights) / len(heights)
# -

# Функция einsum()

# +
# возьмем два двумерных массива
# a = np.array([[0, 1, 2], [3, 4, 5]])

# b = np.array([[5, 4], [3, 2], [1, 0]])

# +
# перемножим a и b по индексу j через функцию np.einsum()
# np.einsum("ij, jk -> ik", a, b)
