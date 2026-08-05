# +

"""Data structures."""

# +
some_list_1=[]
some_list_2=list()

print(some_list_1, some_list_2)
# -

number_three = [3,'число три',['число','три'],{'число':3}]
number_three

len(number_three)

# +
abc_list=['a','b','c','d','e']

print(abc_list[0],abc_list[-1])
# -

salary_list = [['Анна',90000],['Игорь',85000],['Алексей',95000]]
salary_list[1][0]

abc_list.index('c')

salary_list[0].index(90000)

days_list = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
days_list[1:5]

days_list[:5:2]

'Пн' in days_list

if 'Вт' in days_list:
    print('Такое слово есть')

# +
weekdays = ['Понедельник','Вторник']

weekdays.append('Четверг')
weekdays
# -

weekdays.insert(2, 'Среда')
weekdays

weekdays[3]='Пятница'
weekdays

weekdays.remove('Пятница')
weekdays

del(weekdays[2])
weekdays

weekdays.pop(1)

weekdays

# +
more_weekdays=['Вторник','Среда','Четверг','Пятница']

weekdays.extend(more_weekdays)
weekdays
# -

weekend=['Суббота','Воскресенье']
print(weekdays+weekend)

['Понедельник']*2

['Понедельник']*2 + ['Вторник']*2

week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

Mon = week[0]
Mon

Mon, Tue, Wed = week[:3]
Mon, Tue, Wed

Mon, *_=week
Mon

Mon, *days, Sun = week
Mon, Sun

nums = [25,10,30,20,5,15]
sorted(nums)

nums

sorted_nums = sorted(nums)
sorted_nums

nums.sort(reverse=True)
nums

nums.reverse()
nums

reversed(nums)

list(reversed(nums))

nums

str_list=['P','y','t','h','o','n']


joined_str=''.join(str_list)
joined_str

joined_str='_'.join(str_list)
joined_str

nums_=[3,2,1,4,5,12,3,3,7,9,11,15]

nums_.count(3)

print(min(nums_),max(nums_),sum(nums_))

names = ['Артем', 'Антон', 'Александр', 'Борис', 'Виктор', 'Геннадий']

# +
a_names = []

for name in names:
    
    if name.startswith('А'):
        
        a_names.append(name)
        
a_names
# -

a_names = [name for name in names if name.startswith('А')]
a_names

lower_names = [name.lower() for name in names]
lower_names

replace_name = [name if name !='Виктор' else 'Вадим' for name in names]
replace_name

lemmatized = ['paris','visited','lot','museum','first','went','louvre', 'largest','art','museum','world','always','interested','art','spent','many','hour','museum','enourmous','week','would','enought']

# +
from nltk.stem import PorterStemmer

porter = PorterStemmer()


stemmed_p=[porter.stem(s) for s in lemmatized]
print(stemmed_p)
# -

tuple_1, tuple_2 = (), tuple()
print(tuple_1,tuple_2)

# +
letters = ('a','b','c')

letters[0]
# -

letters[0]='d'

# +
letters = list(letters)

letters[0] = 'd'
letters
# -

let_a=('a',)
type(let_a)

let_a = ('a')
type(let_a)

# +
companies=['Microsoft','Apple','Tesla']

for company in enumerate(companies):
    print(company, type(company))
# -

shopping_dict={'огурцы': 2,'помидоры':3,'лук':1, 'картофель':2}

for item  in shopping_dict.items():
    print(item)

# +
a,b,c=('a','b','c')

print(a)
# -

for k, v in shopping_dict.items():
    print(k,v)

# +
names = ['Артем', 'Антон', 'Александр', 'Борис', 'Виктор', 'Геннадий']
income = [97000, 110000, 95000, 84000, 140000, 120000]

zip(names, income)
# -

list(zip(names, income))

# +
set_1=set()

set_2=set(['a','b','c','c'])
set_3={'a','b','c','c'}

print(set_1,set_2,set_3)
# -

not_a_set={}
type(not_a_set)

vowels = {'а', 'о', 'э', 'е', 'у', 'ё', 'ю'}
vowels

vowels.update(['и','ы'])
vowels

vowels.add('щ')
vowels

vowels.remove('щ')
vowels

{'a','b','c'}=={'c','b','a'}

len({'a','b','c'})

'a' in {'a','b','c'}

'a' not in {'a','b','c'}

# +
set_A={'a','b','c'}
set_B={'a','b','c','d','e','f'}

set_A.issubset(set_B)
# -

set_B.issuperset(set_A)

nlp = set(['Анна', 'Николай', 'Павел', 'Оксана'])
cv = set(['Николай', 'Евгений', 'Ольга', 'Оксана'])

print(nlp.union(cv))
print(nlp | cv)

print(nlp.intersection(cv))
print(nlp & cv)

print(nlp.difference(cv))
print(nlp - cv)

print(cv.difference(nlp))
print(cv - nlp)

print(nlp.symmetric_difference(cv))
print(nlp ^ cv)


