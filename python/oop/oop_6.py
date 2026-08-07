"""Static methods and decorator."""


class Person:
    def hello(self):
        print('Hello')
    
    @staticmethod
    def goodbye():
        print('Goodbye')    
p = Person()
p.goodbye()

a = Person()

b= Person()

a.hello()

a.goodbye()

id(a.hello)

id(b.hello)

id(a.goodbye)

id(b.goodbye)

a.__dict__

b.__dict__

type(a.goodbye)

Person.goodbye()


