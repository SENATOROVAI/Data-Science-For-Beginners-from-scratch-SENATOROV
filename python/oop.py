"""OOP."""


# +
class Person:
    """A class representing a person with a name."""

    name = "Ivan"


print(Person.name)
print(Person.__name__)
print(dir(Person))

p_obj = Person()
print(p_obj.__class__)
print(p_obj.__class__.__name__)
print(type(p_obj))
p_obj_2 = type(p_obj)()
print(id(p_obj))
print(id(p_obj_2))


# +
class Person2:
    """A class representing a person with a name attribute."""

    name = "Ivan"


print(dir(Person2))
print(Person2.__dict__)


# Person.__dict__['name'] = 'ffff'  # ERROR

# Person2.age = 4455
# print(Person2.__dict__)


getattr(Person2, "name")
setattr(Person2, "dob", "123")
print(Person2.__dict__)
delattr(Person2, "dob")


class Person3:
    """A class representing a person with a name and greeting method."""

    name = "Ivan"

    def hello(self: "Person3") -> None:
        """Print a greeting message."""
        print("Hello")


print(Person3.__dict__)


# +
class Person4:
    """A class representing a person with a name attribute."""

    name: str = "Ivan"  # Default name value


print(Person4.__dict__)

p1 = Person4()
p2 = Person4()

print(id(p1) == id(p2))

print(p1.name)
print(p2.name)

print(id(p1.name))
print(id(p2.name))

print(p1.__dict__)
print(p2.__dict__)

p1.name = "Oleg"

p2.name = "Dima"
# p2.age = 123

print(p1.__dict__)
print(p2.__dict__)

print(id(p1.name))
print(id(p2.name))


# +
class Person5:
    """A class representing a person with a greeting method."""

    def hello(self: "Person5") -> None:
        """Print a greeting message."""
        print("Hello")


print(Person5.hello)


p3 = Person5()
print(p3.hello)
print(hex(id(p3)))

p3.hello()

print(dir(Person5.hello))
print(dir(p3.hello))

Person5.hello(p3)
# print(p3.hello.__self__)


# +
class Person6:
    """A class representing a person with create and display methods."""

    def create(self: "Person6") -> None:
        """Initialize person's name attribute."""
        self.name = "Ivan"  # pylint: disable=attribute-defined-outside-init

    def display(self: "Person6") -> None:
        """Display the person's name."""
        print(self.name)


p4 = Person6()
p4.display()  # ERROR


class Person7:
    """A class representing a person with name attribute."""

    def __init__(self: "Person7") -> None:
        """Initialize person's name attribute."""
        self.name = "Ivan"

    def display(self: "Person7") -> None:
        """Display the person's name."""
        print(self.name)


p5 = Person7()
p5.display()


# +
class Person8:
    """A class representing a person with greeting methods."""

    def hello(self: "Person8") -> None:
        """Print a hello greeting."""
        print("Hello")

    @staticmethod
    def good_buy() -> None:
        """Print a goodbye message."""
        print("Goodbye")


p6 = Person8()
p6.good_buy()

p7 = Person8()
p7.good_buy()

print(id(p7.hello))
print(id(p6.hello))

print(id(p7.good_buy))
print(id(p6.good_buy))
