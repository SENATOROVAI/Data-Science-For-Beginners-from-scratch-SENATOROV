"""Conditions cycles."""

# +
x=42

if x<10:
    print("small")
elif x<100:
    print("Medium")
else:
    print("large")

# +
x=input("Введите число: ")

x=int(x)

if x<10:
    print("small")
elif x<100:
    print("Medium")
else:
    print("large")

# +
y=input("Введите число: ")

if len(y)!=0:
    
    y=int(y)
    
    if y<10:
        print("small")
    elif y<100:
        print("Medium")
    else:
        print("large")
        
else:
    print("Ввод пустой")

# +
z=42

if z>10 and z<100:
    print("Medium")
    
else:
    print("Small or large")

# +
z=2

if z<10 or z>100:
    print("Small or large")
    
else:
    print("Medium")

# +
sentence='To be, or not to be, that is the question'
word='question'

if word in sentence:
    print('Слово найдено')

# +
number_list=[1,2,3,4,5]
number=10

if number not in number_list:
    print('Число не найдено')
# -

D={'apple':3,'tomato':6,'carrot':2}

if 'apple' in D:
    print('Нашлись')

if 6 in D.values():
    print('Есть')

# +
number_list=[1,2,3,4,5]

for number in number_list:
    print(number)

# +
d = {'apple' : [3, 'kg'], 'tomato' : [6, 'pcs'], 'carrot' : [2, 'kg']}

for k, v in d.items():
    print(k, v)
# -

for v in d.values():
    print(v[0])

# +
import numpy as np

number_array=np.array([1,2,3,4,5])

for number in number_array:
    print(number)
# -

clients = {1: {'name': 'Анна', 'age': 24, 'sex': 'male', 'revenue': 12000},
           2: {'name': 'Илья', 'age': 18, 'sex': 'female', 'revenue': 8000}}

for id, info in clients.items():
    print(f'Client ID: {id}')
    for k, v in info.items():
        print(f'{k}: {v}')
    print()

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,6,2):
    print(i)

# +
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

sales = [47, 75, 79, 94, 123, 209, 233, 214, 197, 130, 87, 55]

for i in range(len(months)):
    print(months[i], sales[i])

# +
my_list = [0, 1, 2, 3, 4]

for i in reversed(my_list):
    print(i)
# -

for i in reversed(range(5)):
  print(i)

for i in range(4, -1, -1):
  print(i)

# +
r = range(5)

sorted_values = sorted(r,reverse=True)

for i in sorted_values:
    print(i)

# +
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

for i, day in enumerate(days,1):
    print(i, day)

# +
i=0

while i<3:
    print(f'Текущее значение счетчика: {i}')
    i=i+1
    print(f"Новое значение счетчика: {i}")
    print()
# -

for id, info in clients.items():
    print(id, info)
    break

# +
x=6

while x!=0:
    print(x)
    x-=1
    if x==3:
        break
# -

for i in range(1,11):
    if i%2!=0:
        continue
    else:
        print(i)

# +
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

Monday = days[0]
Monday

# -

print(f'{Monday} - день тяжелый')

print('{} - день тяжелый'.format(Monday))
