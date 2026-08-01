"""Functions in Python."""

import matplotlib.pyplot as plt
import numpy as np

# +
np.random.seed(42)

height = list(np.round(np.random.normal(180, 10, 1000)))
# -

plt.hist(height, bins=10)
plt.show()

plt.hist(bins=10, x=height)
plt.show()

plt.hist(height)
plt.show()

print('Первая строка')
print()
print('Третья строка')

# +
some_string='machine learning'

some_string.title()

# +

some_list = ['machine', 'learning']
some_list.title()


# -

def double(x):
    res = x*2
    return res


double(2)


def only_return():
    return


only_return()


def only_pass():
    pass


only_pass()

print(only_return())


def double_print(x):
    res = x * 2
    print(res)


double_print(5)


def calc_sum(x,y):
    
    return x+y


calc_sum(1,y=2)


# +
def calc_sum_default(x = 1, y = 2):
    return x + y
 
calc_sum_default()


# +
def print_string():
    print('Some string')
 
print_string()


# -

def f(x: float=3.5)->int:
    return int(x)


f.__annotations__

f()


def f(x: float)->int:
    return float(x)


f(3)

calc_sum(1,2)*2

calc_sum(1,2)>2


# +
def first_letter():
    return 'Python'

first_letter()[0]


# +
def use_input():
    
    user_inp = int(input('Введите число:'))
    
    result = user_inp ** 2
    
    return result

use_input()


# +
def create_list(x):
    
    l=[]
    
    for i in range(x):
        l.append(i)
        
    return l

create_list(5)


# -

def tuple_f():
    string="python"
    x=42
    return string,x


a, b = tuple_f()
print(a,b)
print(type(a),type(b))

c=tuple_f()
print(c)
print(type(c))


# +
def if_divisible(x):
    if x % 2 == 0:
        return True
    else:
        return False

if_divisible(10)


# -

def mean_f(x):
    
    return np.mean(x)+1


# +
import numpy as np

x=[1,2,3]
mean_f(x)

# +
global_name="Петр"

def show_name():
    print(global_name)


# -

show_name()


def show_local_name():
    local_name="Алена"
    print(local_name)


show_local_name()

local_name


def make_global():
    global local_name
    local_name="Алена"
    print(local_name)


make_global()

# +
global_number=5

def print_number():
    local_number=10
    print('Local number: ',local_number)


# -

print_number()

print('Global number:', global_number)

lf = lambda a,b: a*b
lf(2,3)


# +
def normal_f(a, b):
    return a * b
 
normal_f(2, 3)

# +
nums = [15, 27, 9, 18, 3, 1, 4]

criterion = lambda n: True if (n > 10) else False
# -

list(filter(criterion, nums))

list(filter(lambda n: True if (n > 10) else False, nums))


# +
def criterion_2(n):
  if n > 10:
    return True
  else:
    return False
 
list(filter(criterion_2, nums))
# -

indices_distances = [(901, 0.0), (1002, 0.22982440568634488), (442, 0.25401128310081567)]

sorted(indices_distances, key = lambda x: x[1], reverse = False)

(lambda x: x * x)(10)


def mean(a, b):
    return (a + b) / 2
mean(1, 2)


def mean(list_):
    total=0
    for i in list_:
        total+=i
    
    return total/len(list_)


list_ = [1, 2, 3, 4]
mean(list_)

mean(1, 2)


def mean(*nums):
  total = 0
  for i in nums:
    total += i
  return total / len(nums)


mean(1, 2, 3, 4)

mean(*list_)


def test_type(*nums):
  print(nums, type(nums))


test_type(1, 2, 3, 4)

test_type(*list_)

# +
a = [1, 2, 3]
b = [*a, 4, 5, 6]
 
print(b)


# -

def f(**kwargs):
  return kwargs.items()


f(a = 1, b = 2)

import numpy as np
def simple_stats(*nums, **params):
    if 'mean' in params and params['mean'] == True:
        
        print(f'mean: \t{np.round(np.mean(nums), 3)}')
    if 'std' in params and params['std'] == True:
        print(f'std: \t{np.round(np.std(nums), 3)}')


simple_stats(5, 10, 15, 20, mean = True, std = True)

simple_stats(5, 10, 15, 20, mean = True, std = False)

# +

list_ = [5, 10, 15, 20]
settings = {'mean' : True, 'std' : True}
 
simple_stats(*list_, **settings)
# -

simple_stats(5, 10, 15, 20, mean = True, std = True, median = True)
