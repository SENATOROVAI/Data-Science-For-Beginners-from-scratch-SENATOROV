"""init."""


class Person:
    pass


p = Person()

p.name = 'Ivan'

p.name


class Person:
    def __init__(self,name):
        self.name='Ivan'

    def display(self):
        print(self.name)


p = Person()

p.display()

p.__dict__

p.create()

p.__dict__

p =Person('ivan')

p.name

p.__dict__

p.age=123


