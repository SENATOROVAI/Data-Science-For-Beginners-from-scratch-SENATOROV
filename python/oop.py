"""ООП Молчанов."""

# ## ООП Молчанов.
# - Первые 6 лекций.

# +
import requests

response = requests.get("https://www.google.ru", timeout=5000)

print(type(response))

dir(response)


# +
class Person:
    """Класс личность."""

    name = "Ivan"


print(Person.name)  # Ivan
print(Person.__name__)  # Person
print(Person.__class__)  # Person

person = Person()

print(person.__class__)  # <class '__main__.Person'>
print(person.__class__.__name__)  # Person
print(type(person))  # <class '__main__.Person'>

print(person.__class__ == type(person) == Person)  # True

new_person = Person()

print(id(person))  # 135917969519696
print(id(new_person))  # 135917969518800
print(new_person.__class__ == person.__class__)  # True

# +
print(type(Person.__dict__))
print(Person.__dict__)
# Person.__dict__['name'] = 'some-new-name' ---> TypeError

print(Person.name)  # Ivan
print(getattr(Person, "name"))  # Ivan
setattr(Person, "dob", "123")
print(Person.dob)  # type: ignore
# 123

delattr(Person, "dob")
print(Person.__dict__)


# +
class Person1:
    """Кдасс личность."""

    name = "Ivan"

    def hello() -> None:  # type: ignore # pylint: disable=E0211
        """Выводит приветствие."""
        print("Hello")


Person1.hello()

print(Person1.__dict__)


# +
class Person2:
    """Класс личность."""

    name = "Ivan"


print(Person2.__dict__)

person2_1 = Person2()
person2_2 = Person2()

print(id(person2_1))
print(id(person2_2))

print(person2_1.name)
print(person2_2.name)

print(id(person2_1.name))
print(id(person2_2.name))

person2_1.name = "Oleg"
person2_2.name = "Dima"

person2_2.name = 123  # type: ignore # pylint: disable=W0201

print(person2_2.__dict__)

# print(person2_1.age) # AttributeError 'Person2' object has no attribute 'age'

Person2.name = "Some Name"

person2_3 = Person2()

print(person2_1.name)  # Oleg
print(person2_2.name)  # Dima
print(person2_3.name)  # Some Name


# +
class Person3:
    """Класс личности."""

    def hello() -> None:  # type: ignore # pylint: disable=E0211
        """Пирветствие."""
        print("Hello")


print(Person3.hello)  # <function Person3.hello at 0x7b9dde516ca0>

person3 = Person3()

print(person3.hello)  # type: ignore
# Вывод:
# <bound method Person3.hello of <__main__.Person3 object at 0x7b9dde60a9d0>>

print(hex(id(person3)))  # 0x7b9dde555c90

Person3.hello()  # Hello

# person3.hello()
# Вывод:
# TypeError: Person3.hello() takes 0 positional arguments but 1 was given

print(type(Person3.hello))  # 135917970309984
print(type(person3.hello))  # type: ignore
# 135917970326656
print(person3.__dict__)  # {}

# ВАЖНО!!!
# Под капотом вызов метода person3.hello() происходит следующим образом
# Person3.hello(person3)

print(person3.hello.__self__)  # type: ignore
# 0x7b9dde555c50
print(hex(id(person3)))  # 0x7b9dde555c50

print(person3.hello.__func__)  # type: ignore
# <function Person3.hello at 0x7b9dde6639c0>

# Учтем передачу экземпляра класса в метод класса при вызове


class Person4:
    """Класс личность."""

    def hello(self) -> None:
        """Приветствие."""
        print("Hello", self)


person4 = Person4()

person4.hello()  # Hello <__main__.Person4 object at 0x7b9dde4aafd0>


# +
class Person5:
    """Класс личность."""

    def create(self) -> None:
        """Создание личности."""
        self.name = "Ivan"  # pylint: disable=W0201

    def display(self) -> None:
        """Выводит имя и консоль."""
        print(self.name)


person5 = Person5()

# person5.display() # AttributeError: 'Person5' object has no attribute 'name'

person5.create()
person5.display()  # Ivan


class Person6:
    """Класс личность."""

    def __init__(self, name: str) -> None:
        """Инициализирует Личность."""
        self.name = name

    def display(self) -> None:
        """Выводит имя в консоль."""
        print(self.name)


person6 = Person6("Ivan")

print(person6.name)  # 'Ivan'
print(person6.__dict__)  # {'name': 'Ivan'}


# +
class Person7:
    """Класс личность."""

    def hello(self) -> None:
        """Приветствие."""
        print("Hello")

    # Не принимает self
    @staticmethod
    def goodbye() -> None:
        """Прощание."""
        print("GoodBye")


person7_1 = Person7()
person7_1.hello()  # Hello
person7_1.goodbye()  # Goodbye

person7_2 = Person7()

print(id(person7_1))  # 135917970333264
print(id(person7_2))  # 135917970333200
print(id(person7_1.goodbye))  # 135917970311424
print(id(person7_2.goodbye))  # 135917970311424

Person7.goodbye()  # Goodbye
