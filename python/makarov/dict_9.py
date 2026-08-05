"""Dictionary."""

dict_1,dict_2 = {} ,{}
print(dict_1,dict_2)

company = {'name': 'Toyota', 'founded' : 1937, 'founder': 'Kiichiro Toyoda'}
company

tickers = dict([['TYO', 'Toyota'], ['TSLA', 'Tesla'], ['F', 'Ford']])
tickers

# +
keys = ('k1','k2','k3')

value = 0

empty_k=dict.fromkeys(keys,value)
empty_k

# +
import numpy as np

value_types = {'k1' : 123,
               'k2' : 'string',
               'k3' : np.nan ,
               'k4' : True,
               'k5' : None,
               'k6' : [1,2,3],
               'k7' : np.array([1,2,3]),
               'k8' : {1 : 'v1',2 : 'v2',3 : 'v3'}}

value_types
# -

person = {'first name' : 'Иван',
          'last name' : 'Иванов',
          'born' : 1980,
          'dept' : 'IT'}

person.keys()

person.values()

person.items()

for k, v in person.items():
    print(k,v)

person['last name']

person['education']

person.get('born')

print(person.get('education'))

'born' in person

1980 in person.values()

('born',1980) in person.items()

person['languages']=['Python','C++']
person

person['languages']=['Python']
person

person.setdefault('last name','Петров')
person

person.setdefault('f_languages',['русский','английский'])
person

person.pop('dept')

person

del(person['born'])

person.popitem()

person.clear()
person

# +
del person

person

# +

dict_to_sort = {'k2' : 30, 'k1' : 20, 'k3' : 10}
# -

sorted(dict_to_sort)

sorted(dict_to_sort.values())

dict_to_sort.items()

sorted(dict_to_sort.items(), key = lambda x: x[0])

sorted(dict_to_sort.items(), key = lambda x: x[1])

original = {'Первый курс' : 174, 'Второй курс' : 131}

# +
new_1 = original.copy()

new_1['Третий курс'] = 117

print(original)
print(new_1)

# +
new_2=original

new_2.clear()

print(original)
print(new_2)


# +
some_dict={'k1':1}

dir(some_dict)
# -

print(some_dict)

some_dict.__str__()

dir(some_dict)[-11:]

source_dict = {'k1' : 2, 'k2' : 4, 'k3' : 6}

{k : v * 2 for (k, v) in source_dict.items()}

{k.upper() : v for (k, v) in source_dict.items()}

{k : v for (k, v) in source_dict.items() if v > 2 if v < 6}

# +
new_dict={}

for k, v in source_dict.items():
    if v>2 and v<6:
        new_dict[k]=v
new_dict
# -

{k : ('even' if v % 2 == 0 else 'odd') for (k, v) in source_dict.items()}

# +
keys = ('k1', 'k2', 'k3')

{k : 0 for k in keys}
# -

words=['apple','banana','fig','blackberry']

lambda word : len(word)

lenght = list(map(lambda word : len(word), words))
lenght

dict(zip(words,lenght))

dict(zip(words, [len(word) for word in words]))

height_feet={'Alex':6.1, 'Jerry' : 5.4, 'Ben' : 5.8}

metres = list(map(lambda m: m * 0.3448, height_feet.values()))
metres

dict(zip(height_feet.keys(), np.round(metres,2)))

{k : np.round(v * 0.3048, 2) for (k, v) in height_feet.items()}

employees = {
    'id1': {
        'first name': 'Александр',
    'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
    'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
            }
}

for v in employees.values():
    print(v)

employees['id1']['age']

from pprint import pprint

# +
employees['id3'] = {'first name': 'Дарья', 'last name' : 'Некрасова', 'age': 27, 'job' : 'веб-дизайнер' }
 
pprint(employees)
# -

employees['id3']['age'] = 26
pprint(employees)

# +
for info in employees.values():
    
    for k,v in info.items():
        
        if k =='age':
            
            info[k] = float(v)
            
pprint(employees)
# -

pprint({id : info for id, info in employees.items()})

{k : (int(v) if k == 'age' else v) for k, v in info.items()}

pprint({id : {k : (int(v) if k == 'age' else v) for k, v in info.items()} for id, info in employees.items()})

corpus = 'When we were in Paris we visited a lot of museums. We first went to the Louvre, the largest art museum in the world. I have always been interested in art so I spent many hours there. The museum is enourmous, so a week there would not be enough.'


words = corpus.split()
print(words)

words = [word.strip('.').strip(',').lower() for word in words]
print(words)

# +
bow_1 = {}

for word in words:
    
    if word in bow_1:
        
        bow_1[word]=bow_1[word]+1
        
    else:
        
        bow_1[word]=1
        
sorted(bow_1.items(),key=lambda x : x[1], reverse=True)[:6]

# +
bow_2 = {}
 
for word in words:
  bow_2[word] = bow_2.get(word, 0) + 1
 
sorted(bow_2.items(), key = lambda x : x[1], reverse = True)[:6]

# -

bow_2.get(word, 0)

bow_2[word] = bow_2.get(word, 0) + 1

# +
from collections import Counter

bow_3 = Counter(words)

bow_3.most_common(6)


# +
string = 'Python'

id(string),type(string),string

# +
string = string + 'is cool'

id(string),type(string), string

# +
lst = [1,2,3]

id(lst),type(lst), lst

# +
lst.append(4)

id(lst), type(lst), lst
