"""OOP."""

# +
# videolecture-1


class Person:
    """A class that represents a person with a specified name."""

    name = "Ivan"


print(Person.name)
print(Person.__name__)
print(dir(Person))
print(Person.__class__)

p_obj_1 = Person()
print(p_obj_1.__class__)
print(p_obj_1.__class__.__name__)
print(type(p_obj_1))
p_obj_2 = type(p_obj_1)()
print(id(p_obj_1))
print(id(p_obj_2))

# +
# videolecture-2


class Person2:
    """A class that represents a person and stores their name."""

    name = "Ivan"


print(dir(Person2))
print(Person2.__dict__)


# Person.__dict__['name'] = 'asdfsdf'  # Error
print(Person.name)

# Person2.age = 234324
# print(Person2.__dict__)


getattr(Person2, "name")
setattr(Person2, "dob", "123")
print(Person2.__dict__)
delattr(Person2, "dob")
print(Person2.__dict__)


class Person3:
    """A class that represents a person with a name and a method to greet."""

    name = "Ivan"

    def hello(self: "Person3") -> None:
        """Print a greeting message."""
        print("Hello")


print(Person3.__dict__)

# +
# videolecture-3


class Person4:
    """A class that represents a person and stores their name."""

    name: str = "Ivan"


print(Person4.__dict__)

p1 = Person4()
p2 = Person4()

print(id(p1) == id(p2))

print(p1.name)
print(p2.name)

print(id(p1.name))
print(id(p2.name))
print(id(Person4.name))

print(p1.__dict__)
print(p2.__dict__)
print(Person4.__dict__)

p1.name = "Oleg"

p2.name = "Dima"
# p2.age = 123

p1 = Person4()
p2 = Person4()
Person.name = "asdfsdf"

print(p1.name)
print(p2.name)

# +
# videolecture-4


class Person5:
    """A class that represents a person with a method to greet."""

    def hello(self: "Person5") -> None:
        """Print a greeting message."""
        print("Hello")


print(Person5.hello)


p3 = Person5()
print(hex(id(p3)))

p3.hello()

print(type(Person5.hello))
print(type(p3.hello))

print(id(Person5.hello))
print(id(p3.hello))

dir(Person5.hello)
dir(p3.hello)

p3.__dict__
Person5.__dict__


Person5.hello(p3)
# print(p3.hello.__self__)
print(hex(id(p3)))

# p3.hello.__func__

# +
# videolecture-5


class Person6:
    """A class that defines a person with create and display functions."""

    def create(self: "Person6") -> None:
        """Set the person's name."""
        self.name = "Ivan"  # pylint: disable=attribute-defined-outside-init

    def display(self: "Person6") -> None:
        """Print the person's name."""
        print(self.name)


p4 = Person6()
p4.display()  # Error


class Person7:
    """A class that represents a person and stores their name."""

    def __init__(self: "Person7") -> None:
        """Set the person's name."""
        self.name = "Ivan"

    def display(self: "Person7") -> None:
        """Print the person's name."""
        print(self.name)


p5 = Person7()
p5.display()

# +
# videolecture-6


class Person8:
    """A class that represents a person with a method to greet."""

    def hello(self: "Person8") -> None:
        """Print a hello greeting."""
        print("Hello")

    @staticmethod
    def goodbye() -> None:
        """Print a goodbye message."""
        print("Goodbye")


p6 = Person8()
p6.goodbye()

p7 = Person8()
p7.goodbye()

print(id(p7.hello))
print(id(p6.hello))

print(id(p7.goodbye))
print(id(p6.goodbye))
