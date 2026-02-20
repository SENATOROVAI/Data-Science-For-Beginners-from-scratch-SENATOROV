"""ООП.

Классы и объекты в python.
"""

# +
# # создадим класс CatClass
# class CatClass:

#   # и пропишем метод .__init__()
#   def __init__(self):
#     pass

# +
# # создадим объект Matroskin класса CatClass()
# Matroskin: class = CatClass()

# # проверим тип данных созданной переменной
# type(Matroskin)

# +
# # вновь создадим класс CatClass
# class CatClass:

#   # метод .__init__() на этот раз принимает еще и параметр color
#   def __init__(self, color):

#     # этот параметр будет записан в переменную атрибута с таким же названием
#     self.color = color

#     # значение атрибута type_ задается внутри класса
#     self.type_ = 'cat'

# +
# # повторно создадим объект класса CatClass, передав ему параметр цвета шерсти
# Matroskin = CatClass('gray')

# # и выведем атрибуты класса
# Matroskin.color, Matroskin.type_

# +
# # изменим атрибут type_ объекта Matroskin на dog
# Matroskin.type_ = 'dog'

# # выведем этот атрибут
# Matroskin.type_

# +
# class CatClass:

#   def __init__(self, color):
#     self.color = color
#     # символ подчеркивания ПЕРЕД названием атрибута указывает,
#     # что это частный атрибут и изменять его не стоит
#     self._type_ = 'cat'

# +
# # вновь создадим объект класса CatClass
# Matroskin = CatClass('gray')

# # и изменим значение атрибута _type_
# Matroskin._type_ = 'dog'
# Matroskin._type_

# +
# class CatClass:

#   def __init__(self, color):
#     self.color = color
#     # символ двойного подчеркивания предотвратит доступ извне
#     self.__type_ = 'cat'

# +
# Matroskin = CatClass('gray')

# # теперь при вызове этого атрибута Питон выдаст ошибку
# Matroskin.__type_

# +
# # поставим _CatClass перед __type_,
# # изменим значение атрибута и
# Matroskin._CatClass__type_ = 'dog'

# # выведем его
# Matroskin._CatClass__type_

# +
# # создадим класс Animal
# class Animal:

#   # пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
#   def __init__(self, weight, length):

#     # поместим аргументы этих параметров в соответствующие переменные
#     self.weight = weight
#     self.length = length

#   # объявим методы .eat()
#   def eat(self):
#     print('Eating')

#   # и .sleep()
#   def sleep(self):
#     print('Sleeping')

# +
# # создадим класс Bird
# # родительский класс Animal пропишем в скобках
# class Bird(Animal):

#   # внутри класса Bird объявим новый метод .move()
#   def move(self):

#     # для птиц .move() будет означать "летать"
#     print('Flying')

# +
# # создадим объект pigeon и передадим ему значения веса и длины
# pigeon = Bird(0.3, 30)

# +
# # посмотрим на унаследованные у класса Animal атрибуты
# pigeon.weight, pigeon.length

# +
# # снова создадим класс Bird
# class Bird(Animal):

#   # в метод .__init__() добавим параметр скорости полета (км/ч)
#   def __init__(self, weight, length, flying_speed):

#     # с помощью функции super() вызовем метод .__init__() родительского класса Animal
#     super().__init__(weight, length)
#     self.flying_speed = flying_speed

#   # вновь пропишем метод .move()
#   def move(self):
#     print('Flying')

# +
# # вновь создадим объект pigeon класса Bird, но уже с тремя параметрами
# pigeon = Bird(0.3, 30, 100)

# +
# # вызовем как унаследованные, так и собственные атрибуты класса Bird
# pigeon.weight, pigeon.length, pigeon.flying_speed

# +
# # вызовем унаследованный метод .sleep()
# pigeon.sleep()

# +
# # и собственный метод .move()
# pigeon.move()

# +
# # создадим подкласс Flightless класса Bird
# class Flightless(Bird):

#   # метод .__init__() этого подкласса "стирает" .__init__() родительского класса
#   def __init__(self, running_speed):

#     # таким образом, у нас остается только один атрибут
#     self.running_speed = running_speed

#   # кроме того, результатом метода .move() будет 'Running'
#   def move(self):
#     print('Running')

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
# # создадим родительский класс Fish
# class Fish:

#   # и метод .swim()
#   def swim(self):
#     print('Swimming')

# +
# # и еще один родительский класс Bird
# class Bird:

#   # и метод .fly()
#   def fly(self):
#     print('Flying')

# +
# # родительские классы мы перечисляем в скобках через зяпятую
# class SwimmingBird(Bird, Fish):
#   pass

# +
# duck = SwimmingBird()

# +
# # для чисел '+' является оператором сложения
# 2 + 2

# +
# # для строк - оператором объединения
# 'классы' + ' и ' + 'объекты'

# +
# len('Программирование на Питоне')
# 26
# len(['Программирование', 'на', 'Питоне'])
# 3
# len({0 : 'Программирование', 1 : 'на', 2 : 'Питоне'})
# 3
# import numpy as np
# len(np.array([1, 2, 3]))

# +
# # создадим класс котов
# class CatClass:

#   # определим атрибуты клички, типа и цвета шерсти
#   def __init__(self, name, color):
#     self.name = name
#     self._type_ = 'кот'
#     self.color = color

#   # создадим метод .info() для вывода этих атрибутов
#   def info(self):
#     print(f'Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}')

#   # и метод .sound(), показывающий, что коты умеют мяукать
#   def sound(self):
#     print('Я умею мяукать')

# +
# # создадим класс собак
# class DogClass:

#   # с такими же атрибутами
#   def __init__(self, name, color):
#     self.name = name
#     self._type_ = 'пес'
#     self.color = color

#   # и методами
#   def info(self):
#     print(f'Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}')

#   # хотя, обратите внимание, действия внутри методов отличаются
#   def sound(self):
#     print('Я умею лаять')

# +
# cat = CatClass('Бегемот', 'черный')
# dog = DogClass('Барбос', 'серый')

# +
# for animal in (cat, dog):
#   animal.info()
#   animal.sound()
#   print()

# +
# patients = [{'name': 'Николай', 'height': 178},
#             {'name': 'Иван', 'height': 182},
#             {'name': 'Алексей', 'height': 190}]

# +
# # создадим переменные для общего роста и количества пациентов
# total, count = 0, 0

# # в цикле for пройдемся по пациентам (отдельным словарям)
# for patient in patients:
#   # достанем значение роста и прибавим к текущему значению переменной total
#   total += patient['height']
#   # на каждой итерации будем увеличивать счетчик пациентов на один
#   count += 1

# # разделим общий рост на количество пациентов,
# # чтобы получить среднее значение
# total / count

# +
# # создадим класс для работы с данными DataClass
# class DataClass:

#   # при создании объекта будем передавать ему данные для анализа
#   def __init__(self, data):
#     self.data = data

#   # кроме того, создадим метод для расчета среднего значения
#   def count_average(self, metric):

#     # параметр metric определит, по какому столбцу считать среднее
#     self.metric = metric

#     # объявим два частных атрибута
#     self.__total = 0
#     self.__count = 0

#     # в цикле for пройдемся по списку словарей
#     for item in self.data:

#       # рассчитем общую сумму по указанному в metric
#       # значению каждого словаря
#       self.__total += item[self.metric]

#       # и количество таких записей
#       self.__count += 1

#     # разделим общую сумму показателя на количество записей
#     return self.__total / self.__count

# +
# # создадим объект класса DataClass и передадим ему данные о пациентах
# data_object = DataClass(patients)

# # вызовем метод .count_average() с метрикой 'height'
# data_object.count_average('height')

# +
# # lambda-функция достанет значение по ключу height
# # функция map() применит lambda-функцию к каждому вложенному в patients словарю
# # функция list() преобразует результат в список
# heights = list(map(lambda x: x['height'], patients))
# heights

# +
# # возьмем два двумерных массива
# a = np.array([[0, 1, 2],
#               [3, 4, 5]])

# b = np.array([[5, 4],
#               [3, 2],
#               [1, 0]])

# +
# # перемножим a и b по индексу j через функцию np.einsum()
# np.einsum('ij, jk -> ik', a, b)

# +
# sum(select(filter(babynames, sex == "M", name == "Taylor"), n))

# +
# # в таком виде последовательность становится еще более наглядной
# babynames %>% filter(sex == "M", name == "Taylor") %>%
#               select(n) %>%
#               sum
