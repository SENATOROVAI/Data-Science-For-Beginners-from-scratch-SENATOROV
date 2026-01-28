# +
"""Describe object-oriented lesson examples."""
from __future__ import annotations

from typing import ClassVar

import requests
from requests import Response

# -

google_response: Response = requests.get("https://www.google.ru")

print(type(google_response))

print(dir(google_response))


# +
# Lesson 1.
# -


class PersonLesson1:
    """Represent lesson 1 person with a default name."""

    name: ClassVar[str] = "Ivan"


print(PersonLesson1.name)

print(PersonLesson1.__name__)

print(dir(PersonLesson1))

print(PersonLesson1.__class__)

lesson1_person: PersonLesson1 = PersonLesson1()

print(lesson1_person.__class__)

print(lesson1_person.__class__.__name__)

print(type(lesson1_person))

cloned_person: PersonLesson1 = type(lesson1_person)()

print(id(lesson1_person))

print(id(cloned_person))


# +
# Lesson 2.
# -


class PersonLesson2:
    """Represent lesson 2 person with mutable attributes."""

    name: ClassVar[str] = "Ivan"
    age: ClassVar[int]
    dob: ClassVar[str]


print(dir(PersonLesson2))

print(PersonLesson2.__dict__)

print(PersonLesson2.name)

PersonLesson2.age = 123

print(PersonLesson2.__dict__)

print(getattr(PersonLesson2, "name"))

setattr(PersonLesson2, "dob", "123")

print(PersonLesson2.__dict__)

delattr(PersonLesson2, "dob")


# +
class PersonLesson2Method:
    """Represent lesson 2 person with a plain function-style method."""

    name: ClassVar[str] = "Ivan"

    def hello(self: PersonLesson2Method) -> None:
        """Say hello without binding to an instance."""
        print("hello!")


PersonLesson2Method.hello(PersonLesson2Method())
# -

print(PersonLesson2Method.__dict__)


# +
# Lesson 3.


# +
class PersonLesson3:
    """Represent lesson 3 person for attribute experiments."""

    name: str = "Ivan"
    age: int


print(PersonLesson3.__dict__)
# -

first_person: PersonLesson3 = PersonLesson3()

second_person: PersonLesson3 = PersonLesson3()

print(id(first_person))

print(id(second_person))

print(first_person.name == second_person.name)

print(id(first_person.name) == id(second_person.name))

print(first_person.__dict__)

print(second_person.__dict__)

print(PersonLesson3.__dict__)

first_person.name = "Oleg"
second_person.name = "Dima"

print(first_person.__dict__)

print(second_person.__dict__)

second_person.age = 25

print(second_person.__dict__)

# +
# first_person.age -> no attr
# -

fresh_person_one: PersonLesson3 = PersonLesson3()
fresh_person_two: PersonLesson3 = PersonLesson3()

print((fresh_person_one.name, fresh_person_two.name))

# +
PersonLesson3.name = "Dayal"

print((fresh_person_one.name, fresh_person_two.name))


# +
# Lesson 4.
# -


class PersonLesson4:
    """Represent lesson 4 person with a simple greeter."""

    def hello(self: PersonLesson4) -> None:
        """Say hello from the class namespace."""
        print("Hello!")


print(PersonLesson4.hello)

greeting_person: PersonLesson4 = PersonLesson4()
print(greeting_person.hello)

print(hex(id(greeting_person)))

PersonLesson4.hello(greeting_person)

# +
# greeting_person.hello()
# -

print(type(greeting_person.hello))

print(type(PersonLesson4.hello))

print((id(PersonLesson4.hello), id(greeting_person.hello)))

print(dir(PersonLesson4.hello))

print(dir(greeting_person.hello))

print(greeting_person.hello.__self__)  # type: ignore[attr-defined]

print(hex(id(greeting_person)))

print(greeting_person.hello.__func__)  # type: ignore[attr-defined]


# +
class PersonLesson4BoundInspector:
    """Inspect bound method internals via a person."""

    def hello(self: PersonLesson4BoundInspector) -> None:
        """Display the instance reference."""
        print(self)


inspected_person: PersonLesson4BoundInspector = PersonLesson4BoundInspector()
inspected_person.hello()
# -

print(hex(id(inspected_person)))


class PersonLesson4Self:
    """Display instance reference through self."""

    def hello(self: PersonLesson4Self) -> None:
        """Display the instance reference through self."""
        print(self)


# +
# Lesson 5.
# -


class PersonLesson5Placeholder:
    """Serve as a placeholder person for lesson 5."""

    name: str


person_with_dynamic_attr: PersonLesson5Placeholder = PersonLesson5Placeholder()
person_with_dynamic_attr.name = "Ivan"
print(person_with_dynamic_attr.name)


# +
class PersonLesson5Named:
    """Store and display a name."""

    def __init__(self, name: str) -> None:
        """Initialize a person with a provided name."""
        self.name: str = name

    def display(self) -> None:
        """Print the stored name."""
        print(self.name)


named_person: PersonLesson5Named = PersonLesson5Named("Dayal")
# -

print(named_person.__dict__)

print(named_person.name)


# +
# Lesson 6.


# +
class PersonLesson6:
    """Provide instance and static greetings."""

    def hello(self: PersonLesson6) -> None:
        """Greet from an instance method."""
        print("Hello!")

    @staticmethod
    def goodbye() -> None:
        """Say goodbye without binding to an instance."""
        print("Goodbye")


person_for_goodbye: PersonLesson6 = PersonLesson6()
person_for_goodbye.goodbye()  # call works after making goodbye static
# -

greeter_one: PersonLesson6 = PersonLesson6()
greeter_two: PersonLesson6 = PersonLesson6()

greeter_one.hello()
greeter_one.goodbye()

print((id(greeter_one.hello), id(greeter_two.hello)))

print((id(greeter_one.goodbye), id(greeter_two.goodbye)))

print((greeter_one.__dict__, greeter_two.__dict__))

print(type(greeter_one.goodbye))

PersonLesson6.goodbye()
