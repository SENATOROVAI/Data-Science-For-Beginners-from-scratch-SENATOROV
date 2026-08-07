"""Atributes and funtions."""


class Person:
    name='Ivan'


dir(Person)

Person.__dict__

Person.__dict__['name']='afaefa'

Person.name

Person.age = 234324

Person.__dict__

getattr(Person, 'name')

setattr(Person, 'dob','123')

Person.__dict__

delattr(Person, 'dob')

Person.__dict__


# +
class Person:
    name = 'Ivan'
    
    def hello():
        print("Hello")

#Person.hello()
print(Person.__dict__)
# -


