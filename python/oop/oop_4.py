"""Classes functions."""


class Person:
    def hello():
        print('Hello')


Person.hello

p = Person()

p.hello

hex(id(p))

Person.hello()

p.hello()

type(p.hello)

type(Person.hello)

id(Person.hello)

id(p.hello)

dir(Person.hello)

dir(p.hello)

p.__dict__

'person-dima'.split('-')


'person'.split('-')

Person.hello()

Python.hello(p)

Person.hello(p)

p.hello.__self__

hex(id(p))

p.hello.__func__

p.hello.__func__(hello.__self__, *args)


class Person:
    def hello(instance):
        print(instance)


p = Person()

p.hello()

hex(id(p))


class Person:
    def hello(self):
        print(self)


