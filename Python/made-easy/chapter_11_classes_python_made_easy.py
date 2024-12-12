"""Глава 11."""

# # Основные понятия
#
# Классы предоставляют способ объединения данных и функциональности. Создание нового класса - это создание нового типа объектов, с помощью которого в дальнейшем вы можете создавать новые объекты (экземпляры класса). У каждого экземпляра класса могут быть атрибуты, хранящие информацию о его состоянии. Экземпляр класса также может иметь методы (определенные в его классе), которые позволяют менять состояние экземпляра.
#
# **Введение в объектно-ориентироанное программирование**
#
# До этого мы использовали процедурно-ориентрованное программироание

# https://drive.google.com/file/d/1B2mTwYndWdAMszmgt7eVKfeorgVpN-b_/view?usp=sharing

# Объектно-ориентированное программирование (ООП) - это парадигма програм­мирования, в которой программу структурируют таким образом, чтобы данные и функциональность объединялись в отдельные объекты.

# https://drive.google.com/file/d/1B2mTwYndWdAMszmgt7eVKfeorgVpN-b_/view?usp=sharing

# **Введение в понятие класса**
#
# Классы используются для создания новых пользовательских структур данных, со­держащих информацию о чем-либо. В упомянутом выше случае мы можем создать класс Employee для работы с информацией обо всех сотрудниках компании, а также для выполнения над ними некоторых действий или функций.
# Важно отметить, что класс - это лишь структура данных или шаблон, показываю­щий, как что-то должно быть определено, но самих данных в классе не содержится. Класс Employee может указывать на то, что для сотрудника нужно знать его имя, квалификацию и возраст, но сам класс не хранит имя, квалификацию или возраст конкретного сотрудника.
#
# Внутри класса есть два типа объектов:
#
# ♦ объекты экземпляров;
#
# ♦ объекты методов.
#
# Аналогия:
#
# Объекты экземпляров можно понимать как имеющиеся атрибуты.
#
# Объекты методов можно понимать как имеющееся поведение.
#
# Класс - это шаблон объектов. И класс сам по себе тоже является объектом в Python.
#
# Самый простой способ создать класс в Python:


class EmployeeExample:
    """_summary_."""


# Теперь мы можем создавать экземпляры класса Employee
#
# **Метод __init__**
#
# Метод _init_ запускается в момент, когда создается объект экземпляра класса. Этот метод нужен для инициализации создаваемого объекта (например, для пере­дачи вашему объекту начальных значений).


class Employee:
    """_summary_.

    Returns:
        _type_: _description_
    """

    # общий атрибут для всех экземпляров
    company = "Python Enterprises"

    # атрибуты экземпляра
    def __init__(self, empname: str, age: int, dept: str) -> None:
        """_summary_.

        Args:
            empname (str): _description_
            age (int): _description_
            dept (str): _description_
        """
        self.empname = empname
        self.age = age
        self.department = dept

    def __str__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return f"I'm, {self.empname}, I'm {self.age}, job: {self.department}"

    # создание метода
    def yob(self, current_year: int) -> int:
        """_summary_.

        Args:
            current_year (int): _description_

        Returns:
            int: _description_
        """
        return current_year - self.age


# **Создание экземпляров класса**

john = Employee("John", 23, "Marketing")
kanye = Employee("Kanye", 34, "Production")

print((john.empname, kanye.empname, "- are the", Employee.company, "emp...s"))

# Мы использовали метод __init__, есть и другой, __str__, который возвращает строковое представление объекта

print(john)
print(kanye)

# # Объекты методов
#
# Методы - это функции, определенные внутри тела класса. Они используются для определения поведения объекта.

print(f"john was born in {john.yob(2024)}.")


# # Наследование
#
# Наследование - это мощный принцип объектно-ориентированного программиро­вания.
#
# Его значение следует из названия - объект может что-то наследовать от родителя. В данном случае дочерний класс наследует атрибуты и методы от своего родитель­ского класса.
#
# Новый класс называется производным (или дочерним) классом, а тот, от которого он наследуется, называется базовым (или родительским) классом.
#
# Наследование позволяет нам определить класс, который перенимает функциональность от родительского класса. Мы также можем добавить производному классу дополнительный функционал.
#
# У наследования есть много преимуществ.
#
# ♦ Наглядно отображает отношения в реальном мире.
#
# ♦ Обеспечивает возможность повторного использования кода. Нам не приходится писать один и тот же код снова и снова. Кроме того, это позволяет нам добав­лять в класс дополнительную функциональность, не изменяя его.
#
# ♦ Наследование носит транзитивный характер, а это означает, что если класс B на­следуется от класса А, то все подклассы B автоматически также наследуются от класса А.

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Множественное наследование

# Когда дочерний класс наследуется от нескольких родительских классов, это называется множественным наследованием

# ![image.png](attachment:image.png)

# # Полиморфизм

# Полиморфизм - способность функции с одним и тем же именем выполнять разные операции для разных данных. Полиморфизм позволяет создавать структуру которая может работать с объектами разных типов.
# В ООП полиморфизм позволяет использовать экземпляр одного класса так же как будто бы это экземпляр другого класса
# Python не поддерживает полиморфизм во время компиляции или перегрузки методов. Если у класса или в скрипте Python есть несколько методов с одинаковым именем, метод, определенный последним, переопределяет предыдущий.
#
# # Абстракция и инкапсуляция
#
# Абстракция и инкапсуляция — две основные концепции ООП, наряду с наследованием и полиморфизмом.
# Абстракция означает сокрытие сложности объекта и отображение только его основных характеристик. Другими словами, абстракция означает сокрытие реальной реализации, а «наружу» пользователю показывается только то, что ему нужно для использования.
#
# Инкапсуляция является одной из фундаментальных концепций ООП. Инкапсуляцией называют идею обертывания данных и работающих с ними методов в один модуль. Это накладывает ограничения на прямой доступ к переменным и методам и помогает предотвратить порчу данных. Чтобы избежать случайного изменения, к переменной объекта можно обращаться только в методах объекта. Такие переменные называются приватными.
#
# # Практическая часть


class Yourclass:
    """_summary_.

    Returns:
        _type_: _description_
    """

    marks = 10
    objname: str = "АБС"

    def __init__(self, marks: int, objname: str) -> None:
        """_summary_.

        Args:
            marks (int): _description_
            name (str): _description_
        """
        self.marks = marks
        self.objname = objname

    def display(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return f"Marks: {self.marks}, Name: {self.objname}"


# 1. Напишите команду для создания объекта класса Yourclass.

obj1 = Yourclass(8, "CDE")
print(obj1.objname)


# 2. Напишите класс с именем Rectangle, состоящий из длины и ширины, и метода, который будет вычислять площадь прямоугольника.


class Rectangle:
    """_summary_."""

    def __init__(self, width: int, height: int) -> None:
        """_summary_.

        Args:
            width (int): _description_
            height (int): _description_
        """
        self.width = width
        self.height = height

    def area(self) -> int:
        """_summary_.

        Returns:
            int: _description_
        """
        return self.width * self.height


ABCD = Rectangle(23, 45)
ABCD.area()


# 3. Напишите класс, который имеет два метода get_String() и print_String(). Метод get_string() принимает строку от пользователя, а print_String выводит строку в верхнем регистре.


class String:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        self.input = ""

    def get_string(self) -> None:
        """_summary_."""
        self.input = input("Enter your string")

    def print_string(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return self.input.upper()


speech = String()
speech.get_string()
speech.print_string()


# 4. Напишите класс, который меняет порядок слов в строке. Строка "hello world" превращается в "world hello".


# +
class HelloWorld:
    """_summary_."""

    def __init__(self, word: str) -> None:
        """_summary_.

        Args:
            word (str): _description_
        """
        self.word = word

    def reverse_words(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        words = self.word.split()
        return " ".join(words[::-1])


user_input = input("Введите строку: ")
hello_world = HelloWorld(user_input)
print(hello_world.reverse_words())


# -

# 5. Напишите класс для преобразования целого числа в римские цифры.
#
# **Примечание**
#
# римские цифры использовались для обозначения чисел менее 4000, так как отсутствие нуля сильно затрудняло написание больших чисел. Мы последуем такой же логике, ограничим функцию 3999 возможными значениями


class RomanConverter:
    """_summary_."""

    def __init__(self, num2: int) -> None:
        """_summary_.

        Args:
            num2 (_type_): _description_

        Returns:
            str: _description_
        """
        self.num = num2

    def to_roman(self) -> str:
        """_summary_.

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """
        roman_units: dict[int, str] = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        }
        roman_tens: dict[int, str] = {
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC",
        }
        roman_hundreds: dict[int, str] = {
            0: "",
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM",
        }

        roman_thousands: dict[int, str] = {0: "", 1: "M", 2: "MM", 3: "MMM"}

        # Проверяем, что число в диапазоне от 1 до 100
        if self.num < 1 or self.num > 3999:
            raise ValueError("Input must be between 1 and 3999")

        units: int = int(str(self.num)[-1]) if self.num >= 1 else 0
        tens: int = int(str(self.num)[-2]) if self.num >= 10 else 0
        hundreds: int = int(str(self.num)[-3]) if self.num >= 100 else 0
        thousands: int = int(str(self.num)[-4]) if self.num >= 1000 else 0

        rom: str = ""
        rom1: str = roman_thousands[thousands] + roman_hundreds[hundreds]
        rom2: str = roman_tens[tens] + roman_units[units]
        rom = rom1 + rom2
        return rom


u_input: int = int(input("Enter a number between 1 and 3999"))
lead = RomanConverter(u_input)
lead.to_roman()


# 6. Определите класс с именем Shape (фигура) и его дочерний класс Square (квадрат).
# Класс square имеет метод инициализации, который принимает в качестве аргу­мента сторону квадрата. Оба класса имеют метод вычисления площади, который может выводить площадь на экран. Площадь фигуры Shape по умолчанию рав­на О.


# +
class Shape:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        self.area: int = 0

    def calc_area(self) -> int:
        """_summary_.

        Returns:
            int: _description_
        """
        return self.area


class Square(Shape):
    """_summary_.

    Args:
        Shape (_type_): _description_
    """

    def __init__(self, side_length: int) -> None:
        """_summary_.

        Args:
            side_length (int): _description_
        """
        super().__init__()
        self.side_length = side_length
        self.area = self.calc_area()

    def calc_area_square(self) -> int:
        """_summary_.

        Returns:
            int: _description_
        """
        return self.side_length**2


square = Square(4)
square.calc_area_square()


# -

# 7. Определите класс Student с заданными характеристиками.
# Атрибуты экземпляра:
#
# • номер курса;
#
# • имя.
#
# Методы:
#
# getdata() - для ввода номера курса и имени
# printdata() - для вывода номера курса и имени
#


class Student:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        self.coursenum: int = 0
        self.studname: str = ""

    def getdata(self) -> None:
        """_summary_."""
        self.coursenum = int(input("Enter the course number: "))
        self.studname = input("Enter the name: ")

    def printdata(self) -> None:
        """_summary_."""
        print(f"Name: {self.studname}, Course: {self.coursenum}")


stud = Student()
stud.getdata()

stud.printdata()


# 8. Определите класс Marks, производный от класса Student.
# Переменная экземпляра:
#
# • Оценки по пяти предметам.
#
# Методы:
#
# • inputdata() — ВЫЗОВ getdata() и ввод 5 оценок;
#
# • outdata() — Вызов printdata() и отображение 5 оценок.
#
# Реализуйте классы на Python.


class Marks(Student):
    """_summary_.

    Args:
        Student (_type_): _description_
    """

    def __init__(self) -> None:
        """_summary_."""
        super().__init__()
        self.marks: list[int] = []

    def inputdata(self) -> None:
        """_summary_."""
        self.getdata()

        for _ in range(5):
            mark: int = int(input(f"Enter a mark for {self.studname}:"))
            self.marks.append(mark)

    def outdata(self) -> None:
        """_summary_."""
        self.printdata()
        print(f"Marks:, {self.marks}")


student = Marks()
student.inputdata()

student.outdata()

# 9. Гостиница xyz предлагает проживание, питание.
#
# а) Создайте класс rooms с номером комнаты, типом комнаты, ценой аренды и т. Д.
#
# б) Создайте класс Meal, содержащий код обеда, название, цену и т. д.
#
# в) Создайте класс Customer, содержащий номер клиента, его имя, адрес и т. д.
#
# г) Класс Customer должен наследоваться от Accommodation И Meal.

# +
# a)


class Rooms:
    """_summary_."""

    def __init__(
        self, room_number: int, room_type: str, rent_price: int, capacity: int
    ) -> None:
        """_summary_.

        Args:
            room_number (int): _description_
            room_type (str): _description_
            rent_price (int): _description_
            capacity (int): _description_
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rent_price = rent_price
        self.capacity = capacity

    def inforoom(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"information about the room {self.room_number}:, "
            f"room_type: {self.room_type}, rent price: {self.rent_price}, "
            f"room_capacity: {self.capacity}"
        )


# б)


class Meal:
    """_summary_."""

    def __init__(
        self, idmeal: int, mealname: str, price: int, classification: str
    ) -> None:
        """_summary_.

        Args:
            id (int): _description_
            mealname (str): _description_
            price (int): _description_
            classification (str): _description_
        """
        self.idmeal = idmeal
        self.mealname = mealname
        self.classification = classification
        self.price = price

    def infomeal(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"information about the meal: id - {self.idmeal}:, "
            f"name: {self.mealname}, price: {self.price}, "
            f"meal type: {self.classification}"
        )


# в), г)


class Customer(Rooms, Meal):
    """_summary_.

    Args:
        Rooms (_type_): _description_
        Meal (_type_): _description_
    """

    def __init__(
        self, fullname: str, phonenum: str, room_number: int, idmeal: int
    ) -> None:
        """_summary_."""
        Rooms.__init__(self, room_number, "", 0, 0)
        Meal.__init__(self, idmeal, "", 0, "")
        self.phonenum = phonenum
        self.fullname = fullname
        self.room_number = room_number

    def custinfo(self) -> str:
        """.

        Returns:
            str: _description_
        """
        return (
            f"name: {self.fullname},"
            f"phone number: {self.phonenum}, "
            f"information about the room: {self.room_number}, "
            f"the meal: id - {self.idmeal} "
        )


# -

room1 = Rooms(1, "standard", 30, 3)
room1.inforoom()

meal1 = Meal(1, "Prague", 5, "dessert")
meal1.infomeal()

client1 = Customer("Jake Paul", "+1 983 233 543", 23, 145)
client1.custinfo()
