"""Classes and objects in Python."""

import numpy as np

# ### Creating a class


class CatClass:
    """Cat Class."""

    # and we will define the method .__init__()
    def __init__(self) -> None:
        """Initialize  class instance."""
        print("Cat initializing")


# #### Creating an object of CatClass

# +
# Let's create a Matroskin object of the CatClass class.
Matroskin = CatClass()

# Let's check the data type of the created variable.
type(Matroskin)
# -

# #### Class attributes

# +
# Let's create an updated version of the CatClass class.


class CatClass1:
    """Cat Class."""

    # The __init__() method now also accepts the color parameter.
    def __init__(self, color: str) -> None:
        """Initialize cat class with color and type."""
        # that parameter will be stored in the self.color attribute variable
        self.color = color

        # The value of the type_ attribute is specified within the class.
        self.type_ = "cat"


# +
# Let's recreate the CatClass object, passing it the fur color parameter.
Matroskin1 = CatClass1("gray")

# and we will print the class attributes
Matroskin1.color, Matroskin1.type_
# -

# #### Class methods

# +
# Let's rewrite the CatClass class.


class CatClass2:
    """Cat Class."""

    # We will leave the __init__() method and attributes unchanged.
    def __init__(self, color: str) -> None:
        """Initialize  Cat with color and type."""
        self.color = color
        self.type_ = "cat"

    # lets add the .meow() method for meowing
    def meow(self) -> None:
        """Perform meowing.."""
        for _ in range(3):
            print("Meow!")

    # and the .info() method for displaying information about an object
    def info(self) -> None:
        """Display information about the Cat instance.."""
        print(self.color, self.type_)


# -

# let's create an object of the rewritten class
Matroskin2 = CatClass2("gray")

# and we will call the .info() method
Matroskin2.meow()

# и метод .info()
Matroskin2.info()

# ### Principles of OOP

# #### Encapsulation
#
#  This is the ability of a class to store data and methods within itself. In other words, a class object can be represented as a capsule containing the necessary data and methods.
#
#  The concepts of public and private attributes are closely related to the concept of encapsulation. Public attributes are those attributes that can be accessed outside the class "capsule."
#
#  By default, all attributes in Python are public.

# +
# change the type attribute of the Matroskin object to dog
Matroskin1.type_ = "dog"

# let's remove this attribute
Matroskin1.type_


# -

# We would like objects of the CatClass class not to change the value of the type_ attribute. In other words, we need to make this attribute private. There are two ways to do this:
#
# Method 1. Place a single underscore before the attribute to indicate to those who will be using our code that this is a private attribute.
#
# Unfortunately, this only partially solves the problem, because the attribute can still be changed.


class CatClass3:
    """Cat Class."""

    def __init__(self, color: str) -> None:
        """Initialize Cat with color and type."""
        self.color = color
        # An underscore symbol BEFORE the attribute name indicates,
        # that this is a private attribute and should not be changed outside
        # the class.
        self._type_ = "cat"


# +
# Let's create a new object of the CatClass class again.
Matroskin3 = CatClass3("gray")

# and change the value of the _type_ attribute
Matroskin3._type_ = "dog"  # pylint: disable=W0212
Matroskin3._type_  # pylint: disable=W0212


# -

# Method 2. Place a double underscore symbol before the attribute name. Now you will not be able to directly access this class.


class CatClass4:
    """Cat Class."""

    def __init__(self, color: str) -> None:
        """Initialize  Cat with color and type."""
        self.color = color
        # The double underscore symbol will prevent external access.
        self.__type_ = "cat"
        print(self.__type_)


# When attempting to call such an attribute, Python will return an error.
Matroskin4 = CatClass4("gray")
print(Matroskin4.__type_)  # pylint: disable=W0212

# +
# However, we can access this attribute using name mangling.
# Matroskin4._CatClass4__type_ = "dog"  C0103

# unfortunately, the value of the attribute will change
# print(Matroskin4._CatClass4__type_)
# -

# #### Class inheritance
#
# The principle of inheritance assumes that one class inherits the attributes and methods of another. In this case, we talk about a parent class or base class and a child class or derived class.

# Creating a parent class and a child class

# +
# Let's create a class called Animal.


class Animal:
    """Base class animal."""

    # Let's define the __init__() method with
    # two parameters: weight (kg) and height (cm).
    def __init__(self, weight: float, length: float) -> None:
        """Initialize Animal with weight and length."""
        # let's put the arguments of these parameters into the corresponding  # variables
        self.weight = weight
        self.length = length

    # declare methods .eat()
    def eat(self) -> None:
        """Involves eating food."""
        print("Eating")

    # and .sleep()
    def sleep(self) -> None:
        """Sleep method."""
        print("Sleeping")


# +
# Let's create a Bird class.
# We will write the parent class Animal in brackets.


class Bird(Animal):
    """Class Bird, descendant of class Animal."""

    def __init__(self, weight: float, length: float) -> None:
        """Initialize Bird with weight, length."""
        # Using the super() function, call the .__init__() method of the
        # parent class Animal.
        Animal.__init__(self, weight, length)

    # Inside the Bird class, declare a new method .move()
    def move(self) -> None:
        """Perform a bird flight."""
        # for birds .move() will mean "to fly"
        print("Flying")


# -

# Let's create a pigeon object and assign it the values of weight and length.
pigeon = Bird(0.3, 30)

# Let's look at the attributes inherited from the Animal class.
print(pigeon.weight, pigeon.length)

# and methods inherited from the Animal class.
pigeon.eat()

# Now let's call a method that is specific to the Bird class.
pigeon.move()

# ### Function `super()`
#
# Note that in the previous example, the Bird class only received new methods; no new attributes appeared in it. The thing is, if we want to add an attribute to a child class while preserving the attributes of the parent class, we need to explicitly call the latter using the super() function.

# +
# Let's create the Bird class again.


class Bird1(Animal):
    """Class Bird, descendant of class Animal."""

    # Add the flight speed parameter (km/h) to the .__init__() method.
    def __init__(self, weight: float, length: float, flying_speed: float) -> None:
        """Initialize bird with weight, length, and flight speed."""
        # Using the super() function,
        # we call the .__init__() method of
        # the parent class Animal.
        Animal.__init__(self, weight, length)
        self.flying_speed = flying_speed

    # Let's redefine the .move() method.
    def move(self) -> None:
        """Perform  bird flight."""
        print("Flying")


# -

# Let's create another pigeon object of the Bird class,
# but this time with  three parameters.
pigeon1 = Bird1(0.3, 30, 100)

# Let's call both inherited and
# custom attributes of the Bird class.
print(pigeon1.weight, pigeon1.length, pigeon1.flying_speed)

# call the inherited method .sleep()
pigeon1.sleep()

# and its own .move() method
pigeon1.move()

# #### Class redefinition
#
# An interesting feature of a descendant class in Python is that it redefines (essentially rewrites) the parent class.Let's create a subclass for flightless birds called Flightless, in which:
#
# the only attribute will be their running speed; and we will replace the result of the .move() method (which is logical) from Flying to Running.

# +
# Let's create a subclass Flightless of the class Bird.


class Flightless(Bird):
    """Non-Flying Bird Class."""

    # The __init__() method of this subclass "overrides" the __init__()
    # method  of the parent class.
    def __init__(self, weight: float, length: float, running_speed: float) -> None:
        """Initialize  Non-Flying Bird at running speed."""
        # Thus, we are left with only one attribute.
        Bird.__init__(self, weight, length)

        self.running_speed = running_speed

    # In addition, the result of the .move() method will be 'Running'.
    def move(self) -> None:
        """Perform bird running."""
        print("Running")


# -

# Let's create an ostrich object of the Flightless class.
ostrich = Flightless(13, 33, 60)

# let's look at the value of the speed attribute
ostrich.running_speed

# and check the .move() method
ostrich.move()

# The Flightless subclass retains the methods of all parent classes.
ostrich.eat()

# Multiple inheritance
#
# Python allows a class to inherit methods from two or more classes. Suppose we want to create a SwimmingBird class and take the swimming and flying methods from two different parent classes, namely Fish and Bird.

# +
# Let's create a parent class Fish


class Fish:
    """Fish Class."""

    # and method .swim()
    def swim(self) -> None:
        """Perform swimming."""
        print("Swimming")


# +
# and another Bird parent class


class Bird2:
    """Class Bird."""

    # and method .fly()
    def fly(self) -> None:
        """Perform flying."""
        print("Flying")


# +
# Now let's create a descendant class of these two classes.


class SwimmingBird(Bird2, Fish):
    """Swimming Bird Class."""

    pass  # pylint: disable=unnecessary-pass


# -

# Let's create an object of the SwimmingBird class called duck.
duck = SwimmingBird()

# As we can see, ducks can fly,
duck.fly()

# and swim.
duck.swim()

# #### Polymorphism
#
# means that the same object can take different forms. In programming, polymorphism implies that operators, functions, and objects can interact with different types of data.
#
# For example, the + operator implies addition in the case of numbers and concatenation in the case of strings.

# for numbers, '+' is the addition operator
print(2 + 2)

# for strings - the concatenation operator
print("classes" + " and " + "objects")

# 1. Polymorphic functions
#
# These are functions that can work with different types of data. A classic example is the built-in len() function.

# The len() function can be applied to a string.
print(len("Hello, World!"))

# in addition, it is capable of working with a list
print(len(["hello", "world"]))

# dictionary
print(len({0: "Programming", 1: "in", 2: "Python"}))

# 2. Class polymorphism
#
# Class polymorphism assumes that different (unrelated) classes can have methods with the same names.
#
# Let's write two classes, Cat and Dog, and give them similar attributes and methods.

# +
# let's create a class of cats


class CatClass5:
    """Cat class."""

    # Let's define the attributes of the nickname, type, and coat color.
    def __init__(self, name: str, color: str) -> None:
        """Initialize Cat with a name, color, and type."""
        self.name = name
        self._type_ = "cat"
        self.color = color

    # Let's create a .info() method to output these attributes.
    def info(self) -> None:
        """Display information about the cat."""
        print(
            f"My name is {self.name}, I'm {self._type_}, the color of my fur {self.color}"
        )

    # and the .sound() method, showing that cats can meow
    def sound(self) -> None:
        """States that cats can meow."""
        print("I can meow")


# +
# let's create a class of dogs


class DogClass5:
    """Class Dog."""

    # with the same attributes
    def __init__(self, name: str, color: str) -> None:
        """Initialize Dog with name, color, and type."""
        self.name = name
        self._type_ = "dog"
        self.color = color

    # and methods
    def info(self) -> None:
        """Display information about the dog."""
        print(
            f"My name is {self.name}, I'm {self._type_}, the color of my fur {self.color}"
        )

    # although, please note, the actions within the methods differ
    def sound(self) -> None:
        """Reveals that dogs can bark."""
        print("I know how to bark")


# -

# Let's create objects of these classes

cat5 = CatClass5("Alpha", "black")
dog5 = DogClass5("Alpha", "gray")

# In the `for` loop, we will call the attributes and methods of each class.

for animal in (cat5, dog5):
    animal.info()
    animal.sound()
    print()

# ### Programming paradigms

patients: list[dict[str, str | int]] = [
    {"name": "Nikolai", "height": 178},
    {"name": "Ivan", "height": 182},
    {"name": "Alex", "height": 190},
]

# #### Procedural programming
#
# Procedural programming. Overall, this is the usual programming we have been practicing up to today's lesson. We define a task and sequentially arrive at the desired solution using a set of instructions.

# +
# Let's create variables for overall growth and number of patients.
total, count = 0, 0

# In the for loop, we will go through the patients (separate dictionaries)
for patient in patients:
    # get the growth value and add it to the current value of the total       # variable
    total += int(patient["height"])
    # At each iteration, we will increase the patient counter by one.
    count += 1

# divide the total growth by the number of patients,
# to obtain the average value
print(total / count)
# -

# #### Object-oriented programming
#
# In the world of OOP, all tasks are solved not by one large program, but by classes (and objects created on their basis). As a rule, a separate class is created for each task. And although at first the use of classes may seem rather complicated, in fact it greatly simplifies the solution of many tasks.

# +
# Let's create a class for working with data DataClass


class DataClass:
    """Class for working with data."""

    # When creating an object, we will pass data to it for analysis.
    def __init__(self, data: list[dict[str, str | int]]) -> None:
        """Class instance."""
        self.data = data
        self.metric: str | None = None
        self.__total: int | None = None
        self.__count: int | None = None

    # In addition, we will create a method for calculating the average value.
    def count_average(self, metric: str) -> float:
        """Расчет среднего значения по переданной метрике."""
        # The metric parameter determines which column to use to calculate the # average.
        self.metric = metric

        # declare two private attributes
        self.__total = 0
        self.__count = 0

        # In the for loop, we will go through the list of dictionaries.
        for item in self.data:

            # calculate the total amount specified in metric
            # the meaning of each dictionary
            self.__total += int(item[self.metric])

            # and the number of such entries
            self.__count += 1

        # divide the total amount of the indicator by the number of entries
        return self.__total / self.__count


# +
# Let's create an object of the DataClass class and pass it patient data.
data_object = DataClass(patients)

# call the .count_average() method with the 'height' metric
data_object.count_average("height")
# -

# #### Functional programming
#
# By and large, functional programming is a set of functions that sequentially solve a given task. The result of one function becomes the input parameter for another.

# function map()

# The lambda function will retrieve the value by the height key.
# The map() function will apply the lambda
# function to each dictionary nested in patients.
# The list() function will convert the result into a list.
heights: list[int] = list(map(lambda patient: int(patient["height"]), patients))
heights

# Let's use the sum() and len() functions to find the average value.
print(sum(heights) / len(heights))

# function einsum()

# +
# Let's take two two-dimensional arrays.
a_np_array = np.array([[0, 1, 2], [3, 4, 5]])

b_np_array = np.array([[5, 4], [3, 2], [1, 0]])
# -

# Multiply a and b by index j using the np.einsum() function.
einsum_result = np.einsum("ij, jk -> ik", a_np_array, b_np_array)
print(einsum_result)
