"""OOP Молчанов."""


# +
# 1 урок

class Person:
    name = 'Hasan'
    
print(Person.name,'\n')
print(Person.__name__)

dir(Person)

# +
print(Person.__class__,'\n')

p = Person() # создаём экземпляр класса

print(p.__class__,'\n')
print(p.__class__.__name__)

type(p)

new_person = type(p)()  # создание экземпляра класса таким методом
new_person.name

# +
# 2 урок
Person.age = 18 # Обращение к полю класса и записывание значения

Person.__dict__ # выводит все поля класса

getattr(Person, 'name')                 #   получаем поле класса 
setattr(Person, 'DoB','10.19.2000')     #   устанавливаем, можно переопределять
delattr(Person, 'DoB')                  #   удаляем

Person.__dict__


# +
class Person:
    name = "Hasan"
    
    def hello():
        print("Hello world")
        
# Person.hello()

Person.__dict__

# +
# 3 урок
# Классы - это callable объекты, после объявления
# python автоматически присваивает ему некоторые свойства

print(Person.__dict__)

p1 = Person()
print(p1)

p2 = Person()
print(p1)

print(f"id p1 {id(p1)} and id p2 {id(p2)}")
# p1.name == p2.name 
# и id их будут равны так как ссылаются они на одно поле одного объекта


p1.name = "Ismail"
p2.name = "Abubakr"
p1.age = 123

print(f"dict p1 {p1.__dict__} and dict p2 {p2.__dict__}")

# В самом class Person поля не будут изменены

# p2.age ERROR

# +
# 4 урок

class Person:
    def hello():
        print("Hello!")
        
print(Person.hello)

p1 = Person()

# p.hello

print(type(p1.hello))
print(type(Person.hello))


print(dir(Person.hello))
print(dir(p1.hello))

class Person2:
    def hello(self):
        print(self)
        


# +
# 5 урок метод __init__

class Person22:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(self.name)     
    # end def
 
p2p = Person22('Hasan')   
p2p.__dict__


# +
# 6 урок метод декораторы

class Personn:
    def hello(self):
        print('Hello')
    
    @staticmethod 
    def goodbye():
        print('Goodbye')

aa = Personn()
bb = Personn()

# При вызове метода goodbye, айдишники объектов будут одинаковы, потому что
# они ссылаются на один объект класса 

# Статические методы не имеют доступа к свойствам и методам экземпляров
# классов, это просто функция, не принимающая аргументов

# Они нужны для того, чтобы ,к примеру, объединить несколько функций в
# один объект, можно эти функции выносить за классы, используются как
# вспомогательные методы 
