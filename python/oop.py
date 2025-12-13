"""Programming Paradigms and Object-Oriented Programming in Python."""

# Here is a **clear, structured English conspect (summary + notes)** about OOP.
#
# ---
#
# # **Conspect: Introduction to Object-Oriented Programming (OOP)**
#
# ## **1. Programming Paradigms Overview**
#
# Programming paradigms are different ways of writing and organizing code. OOP is one of these approaches, but not the only one.
#
# ### **Main paradigms:**
#
# 1. **Procedural Programming**
#
#    * Code is written as a sequence of instructions, executed line by line.
#    * Easy to start with, but becomes difficult to maintain as the program grows.
#
# 2. **Functional Programming**
#
#    * Based on functions as the main building blocks.
#    * Focuses on transforming data through function calls.
#
# 3. **Object-Oriented Programming (OOP)**
#
#    * Organizes code around *objects* and *classes*.
#    * Objects act as containers that store data and behavior together.
#
# ---
#
# ## **2. The Scaling Problem in Non-OOP Paradigms**
#
# Functional and procedural programming share a major disadvantage:
#
# ### **❗ The problem of scalability and maintainability**
#
# * In large projects, code becomes tightly connected and interdependent.
# * Changing one part often requires modifying many lines across the program.
# * This makes development slow and error-prone.
#
# ---
#
# ## **3. Core Idea of OOP**
#
# OOP solves the maintainability problem by introducing two key concepts:
#
# ### **✔ Class**
#
# A blueprint or template that defines:
#
# * what data (attributes) an object holds
# * what actions (methods) it can perform
#
# ### **✔ Object**
#
# A concrete instance created from a class — a container that holds:
#
# * **data**
# * **methods that operate on that data**
#
# ---
#
# ## **4. Why OOP Helps with Large Projects**
#
# OOP makes complex programs easier to manage because:
#
# ### **Encapsulation**
#
# * Internal implementation of a component can be changed at any time
# * Other parts of the program are unaffected as long as the external interface stays the same
#
# ### **Reusability**
#
# * Classes and objects can be reused in other programs and tasks
# * Reduces duplication, speeds up development
#
# ### **Modularity**
#
# * The program is divided into independent components
# * Easier to debug, maintain, and extend
#
# ---
#
# ## **5. Summary**
#
# Object-Oriented Programming is a way of writing code that groups data and behavior into classes and objects. Unlike procedural and functional programming, OOP scales much better: changes in one place do not break the entire program. This makes the code cleaner, more modular, and reusable.
#
# ---

# +
# for example:
from __future__ import annotations

from typing import ClassVar

import requests
from requests import Response

# requesting with .get() method to get the response from google.com
google_response: Response = requests.get("https://google.com")
# -

# as we see below, google_response is an instance of Response class
type(google_response)

# we can also see all attributes and methods of the Response class
print(dir(google_response))


# ---
#
# # **Conspect: Dualism of Data and Actions in OOP**
#
# ## **1. Dualism: Data vs. Actions**
#
# In computer science, every piece of information has two aspects:
#
# * **Data** — values or state that must be stored.
# * **Actions** — operations that can be performed on those values.
#
# OOP unifies these two aspects inside a single structure called an **object**.
#
# ---
#
# ## **2. Why Data Is Divided Into Types**
#
# Data types exist because:
#
# 1. **Different types require different amounts of memory.**
#    An integer, a float, and a string all occupy different memory sizes.
#
# 2. **Different types behave differently under the same operations.**
#    Example:
#
#    * `"2" + "2"` → `"22"` (string concatenation)
#    * `2 + 2` → `4` (integer addition)
#
# So a type defines:
#
# * how much memory to allocate
# * how operations should work with this data
#
# ---
#
# ## **3. What Is an Object?**
#
# An object is a memory allocation that contains **both**:
#
# 1. **Data (state)**
# 2. **Methods (behavior)** that operate on that data
#
# In Python, **everything is represented as an object**.
#
# You can think of an object as an abstract **container** holding:
#
# * the values (attributes)
# * the operations available for those values (methods)
#
# ---
#
# ## **4. Object State and Attributes**
#
# Objects stored in computer memory hold some **state**.
# State = values stored at specific memory addresses at a given moment.
#
# These stored values are called:
#
# * **fields**
# * **properties**
# * **attributes**
#
# Attributes describe the characteristics of the object.
#
# ---
#
# ## **5. Behavior of an Object**
#
# Besides data, every object also includes **functionality**—methods that define what the object can do or how it behaves.
#
# When designing in OOP we must:
#
# 1. Determine what the **data** will be.
# 2. Decide what **operations** need to be performed on that data.
# 3. Define **interaction rules** between objects.
#
# ### **Core idea of OOP**
#
# > Combine data + actions into a single unit (object).
#
# ---
#
# ## **6. Classes and Instances**
#
# Custom (user-defined) objects are created using **classes**.
#
# ### **Class**
#
# A class is a **description** or **blueprint** that tells Python:
#
# * what attributes the object will have
# * what methods will operate on those attributes
#
# ### **Instance (Object of a Class)**
#
# An object created from a class is called:
#
# * an **instance of the class**
# * a **class object**
#
# All objects of one class share the **same structure**:
#
# * same attributes
# * same methods
#
# …but they may hold **different states** (different values of those attributes).
#
# ---
#
# # **Short Summary**
#
# * Data types exist because memory usage and behavior differ between data kinds.
# * An **object** is a structure that stores both data (attributes) and actions (methods).
# * Python represents *everything* as an object.
# * OOP is about designing programs by combining data + behavior into objects.
# * Classes define what objects look like; objects are instances of classes and may have different states.
#
# ---


# key word "class" is used to define a class in Python
# here is a simple class definition
# pep say that class names should use CapWords convention
# where each word starts with a capital letter and there are no underscores
class FirstPerson:
    """A class representing a first-person perspective in programming."""

    name: ClassVar[str] = "Ivan"
    # Class variable shared by all instances


# We access the methods and properties of an object using a dot, known as dot notation.

print(FirstPerson.name)  # Accessing the class variable

# every class has a built-in attribute __name__
# that holds the name of the class as a string
print(FirstPerson.__name__)  # Output: FirstPerson

# with the dir() function, we can see all
# attributes and methods of the class
print(dir(FirstPerson))

# class of  user defined class is 'type'
# because class is a user-defined type
print(FirstPerson.__class__)
# Output: <class 'type'>

# To create an instance of a class, we must call the class.
# Calling the class returns a new object of that class.
first_person_instance = FirstPerson()
print(first_person_instance.__class__)
# Output: <class '__main__.FirstPerson'>

# same thing we can check with type()
print(type(first_person_instance))


# When I say class, I primarily mean object descriptions.

# ---
#
# # **Conspect: Properties of Class Functions and Namespaces in Python OOP**
#
# ## **1. A Class Creates Its Own Namespace**
#
# When a class is defined, Python creates a **namespace** for it — a special dictionary that stores:
#
# * variable names
# * function names
# * their corresponding values
#
# Example:
#
# ```python
# class Person:
#     name = "Ivan"
# ```
#
# Here, the class namespace contains:
#
# * key `"name"` with value `"Ivan"`
#
# You can inspect class attributes using:
#
# ```python
# dir(Person)
# ```
#
# ---
#
# ## **2. Where Object State Is Stored: `__dict__`**
#
# Both **classes** and **instances** store their attributes in a dictionary-like structure accessible via `__dict__`.
#
# * For classes: `Person.__dict__`
# * For instances: `p.__dict__`
#
# These dictionaries hold the state of the object at a given moment.
#
# ### But there is an important nuance:
#
# `Class.__dict__` returns a **mappingproxy** — a **read-only view** of the class namespace.
#
# Example:
#
# ```python
# Person.__dict__["name"] = "Vasa"
# ```
#
# This will raise an **error**, because `mappingproxy` cannot be modified directly.
#
# ---
#
# ## **3. Why `mappingproxy` Exists**
#
# `mappingproxy` protects the class namespace from direct accidental modification.
# It behaves like a dictionary **except**:
#
# * you **cannot assign** new values through it
# * you **cannot add** new keys
# * you **cannot delete** keys
#
# It is a read-only wrapper around the real dictionary inside the class.
#
# ---
#
# ## **4. How to Modify Attributes Correctly**
#
# Although the class namespace cannot be modified through `__dict__`, it **can** be changed using:
#
# ### ✔ Dot notation
#
# ```python
# Person.age = 30
# ```
#
# ### ✔ Built-in functions
#
# * `getattr(obj, "attr")`
# * `setattr(obj, "attr", value)`
# * `delattr(obj, "attr")`
#
# These functions allow controlled, dynamic access to attributes.
#
# ---
#
# ## **5. Python Allows Modifying Classes at Runtime**
#
# Because Python is a **dynamic language**, you can **add new attributes or methods to a class even after it has been defined**.
#
# Example:
#
# ```python
# Person.country = "Russia"
# ```
#
# Now all instances of `Person`, including previously created ones, have access to `country`.
#
# ---
#
# ## **Summary**
#
# * A class creates its own **namespace**, implemented as a dictionary of attributes.
# * This namespace is exposed as a read-only `mappingproxy` through `Class.__dict__`.
# * Instance attributes are stored in their own writable dictionary `Instance.__dict__`.
# * You cannot modify the class namespace *through* `__dict__`, but you can modify it:
#
#   * using dot notation
#   * using `getattr`, `setattr`, `delattr`
# * Python’s dynamic nature allows adding new attributes and methods to a class **after** definition.
#
# ---


class SecondPerson:
    """Represent lesson 2 person with mutable attributes."""

    name: ClassVar[str] = "Peter"
    age: ClassVar[int]
    dob: ClassVar[str]


# checking the attributes of SecondPerson class
print(dir(SecondPerson))

# checking the namespace of SecondPerson class
print(SecondPerson.__dict__)

# modifying class attributes
SecondPerson.age = 30
SecondPerson.dob = "1993-01-01"
# checking the updated namespace of SecondPerson class
print(SecondPerson.__dict__)


# ---
#
# # **Conspect: Classes as Callable Objects and Isolated Namespaces**
#
# ## **1. Classes Are Callable Objects**
#
# In Python, a **class is a callable object**.
# When a class is called, Python creates and returns a **new instance** of that class.
#
# Example:
#
# ```python
# p = Person()
# ```
#
# Here:
#
# * `Person` is called like a function
# * `p` is an instance of the class `Person`
#
# ---
#
# ## **2. Classes and Instances Have Separate Namespaces**
#
# Each **class** and each **instance** has its own **independent namespace**.
#
# * Class namespace → stores **class attributes and methods**
# * Instance namespace → stores **instance-specific attributes (state)**
#
# These namespaces:
#
# * are **isolated from each other**
# * do **not overwrite** one another
# * interact only through defined attribute lookup rules
#
# ---
#
# ## **3. Why Namespace Isolation Is Important**
#
# Namespace isolation allows:
#
# * creation of many objects with the **same structure**
# * each object to maintain its **own unique state**
# * safe modification of one object without affecting others
#
# Example:
#
# ```python
# p1 = Person()
# p2 = Person()
#
# p1.name = "Ivan"
# p2.name = "Alex"
# ```
#
# Both objects:
#
# * share the same class definition
# * have different values for their attributes
#
# ---
#
# ## **4. Core Advantage of This Design**
#
# The separation of namespaces enables:
#
# * scalability
# * memory efficiency
# * predictable behavior
#
# This is why we can create **thousands or millions of objects** with:
#
# * identical properties and methods
# * different internal data values
#
# ---
#
# ## **Short Summary**
#
# * Classes in Python are callable.
# * Calling a class creates an instance.
# * Classes and instances have isolated namespaces.
# * This isolation allows many similar objects to exist with different states.
# * It is a fundamental mechanism behind object-oriented programming.
#
# ---

# поведение функции отличается от поведения свойств


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

print(type(greeting_person.hello))

print(type(PersonLesson4.hello))

print((id(PersonLesson4.hello), id(greeting_person.hello)))

print(dir(PersonLesson4.hello))

print(dir(greeting_person.hello))

print(greeting_person.hello.__self__)  # type: ignore[attr-defined]

print(hex(id(greeting_person)))

print(greeting_person.hello.__func__)  # type: ignore[attr-defined]


class PersonLesson4BoundInspector:
    """Inspect bound method internals via a person."""

    def hello(self: PersonLesson4BoundInspector) -> None:
        """Display the instance reference."""
        print(self)


inspected_person: PersonLesson4BoundInspector = PersonLesson4BoundInspector()
inspected_person.hello()

print(hex(id(inspected_person)))


class PersonLesson4Self:
    """Display instance reference through self."""

    def hello(self: PersonLesson4Self) -> None:
        """Display the instance reference through self."""
        print(self)


# Here is a **minimal, clean demo** that shows **exactly the core ideas**:
# class function → bound method → `self` → `__self__` / `__func__`.
#
# ```python
# class Person:
#     def hello(self) -> None:
#         print("Hello")
#
#
# p = Person()
#
# # 1. Class attribute vs instance attribute
# print(Person.hello)  # function (unbound)
# print(p.hello)  # bound method
#
# # 2. Calling methods
# Person.hello(p)  # manual call
# p.hello()  # automatic self passing
#
# # 3. Types
# print(type(Person.hello))  # function
# print(type(p.hello))  # method
#
# # 4. Bound method internals
# print(p.hello.__self__)  # instance the method is bound to
# print(p.hello.__func__)  # original function object
#
# # 5. Identity proof
# print(hex(id(p)))
# print(hex(id(p.hello.__self__)))
# ```
#
# ### What this demo proves
#
# * A method is **just a function in the class**
# * Access through an instance creates a **bound method**
# * `self` is passed automatically
# * Bound methods store:
#
#   * `__self__` → the instance
#   * `__func__` → the function
# * Class and instance namespaces remain separate

# ---
#
# ## **Dynamic Attributes vs Initialization with `__init__`**
#
# ### **1. Dynamic Attribute Assignment**
#
# ```python
# class PersonLesson5Placeholder:
#     name: str
# ```
#
# * The class only contains a **type annotation**, not a real attribute.
# * No memory is allocated for `name` at class creation.
# * The attribute appears **only when assigned to an instance**.
#
# ```python
# person_with_dynamic_attr = PersonLesson5Placeholder()
# person_with_dynamic_attr.name = "Ivan"
# ```
#
# ✔ Python allows adding attributes to objects **at runtime**.
# ✔ The attribute `name` now exists **only in the instance namespace**.
#
# ```python
# print(person_with_dynamic_attr.name)
# ```
#
# ---
#
# ### **2. Instance Namespace (`__dict__`)**
#
# Every instance stores its state in `__dict__`.
#
# If you printed:
#
# ```python
# print(person_with_dynamic_attr.__dict__)
# ```
#
# You would get:
#
# ```python
# {"name": "Ivan"}
# ```
#
# ---
#
# ## **3. Attribute Initialization via `__init__`**
#
# ```python
# class PersonLesson5Named:
#     def __init__(self, name: str) -> None:
#         self.name = name
# ```
#
# * `__init__` defines **how an object is initialized**
# * Guarantees that every instance **has the attribute**
# * Prevents partially initialized objects
#
# ```python
# named_person = PersonLesson5Named("Max")
# ```
#
# Now the attribute exists immediately after creation.
#
# ---
#
# ### **4. Inspecting Object State**
#
# ```python
# print(named_person.__dict__)
# ```
#
# Output:
#
# ```python
# {"name": "Max"}
# ```
#
# This confirms:
#
# * Attributes live in the instance namespace
# * `self.name` is just a key-value pair in `__dict__`
#
# ---
#
# ## **Key Differences (Very Important)**
#
# | Dynamic attribute | `__init__` initialization |
# | ----------------- | ------------------------- |
# | Added at runtime  | Added during creation     |
# | Optional          | Guaranteed                |
# | Error-prone       | Safe and explicit         |
# | Flexible          | Structured                |
#
# ---
#
# ## **Core Takeaway**
#
# * Python allows **dynamic attribute creation**, but this is rarely ideal.
# * `__init__` is the **correct and safe** way to define an object’s state.
# * All instance data is stored in `instance.__dict__`.
#
# ---
