"""Methods."""


# +
class Person:
    name='Ivan'
    
print(Person.__dict__)
# -

p1 = Person()

p1

p2 = Person()

id(p1)

id(p2)

p1.name

p2.name

id(p1.name)

id(p2.name)

p1.__dict__

p2.__dict__

Person.__dict__

p1.name='Oleg'

p2.name='Dima'

p1.__dict__

p2.__dict__

p2.age=123

p2.__dict__

p1.name

p2.name

Person.__dict__

p1.age

p1 = Person()

p2 = Person()

Person.name='eifqwefiqw'

p1.name

p2.name


