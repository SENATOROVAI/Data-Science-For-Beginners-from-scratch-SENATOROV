"""Molchanov_OOP."""


class Person:
    """Простой класс с атрибутом класса name."""

    name = "Ivan"


Person.name

dir(Person)

Person.__dict__

Person.age = 23  # type: ignore[attr-defined]

Person.__dict__

# получить атрибут
getattr(Person, "name")

# задать атрибут
setattr(Person, "dob", "13/03/89")

Person.__dict__

# удалить атрибут
delattr(Person, "dob")


class PersonHello:
    """Класс с методом без self, вызываемым через сам класс."""

    name = "Ivan"

    @staticmethod
    def hello() -> None:
        """Поздороваться."""
        print("Hello")


PersonHello.hello()


class PersonCreate:
    """Класс, задающий атрибут через отдельный метод create()."""

    def create(self) -> None:
        """Задать имя Ivan."""
        self.name = "Ivan"  # pylint: disable=attribute-defined-outside-init

    def display(self) -> None:
        """Вывести имя."""
        print(self.name)


person_create = PersonCreate()

person_create.create()

person_create.display()


class PersonInit:
    """Класс, задающий имя через конструктор."""

    def __init__(self, name: str) -> None:
        """Сохранить имя."""
        self.name = name

    def display(self) -> None:
        """Вывести имя."""
        print(self.name)


person_init = PersonInit("Ivan")
person_init.name


class PersonStatic:
    """Класс с обычным методом и статическим методом."""

    def hello(self) -> None:
        """Поздороваться."""
        print("Hello")

    @staticmethod
    def goodbye() -> None:
        """Попрощаться."""
        print("Goodbye")


person_static = PersonStatic()

person_static.hello()

person_static.goodbye()

person_a = PersonStatic()
person_b = PersonStatic()

id(person_a.hello)

id(person_b.hello)

id(person_a.goodbye)

id(person_b.goodbye)

PersonStatic.goodbye()
