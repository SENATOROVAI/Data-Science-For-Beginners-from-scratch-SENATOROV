"""Списки, кортежи и множества в python."""

# +
# some_list_1 = []
# some_list_2 = list()

# print(some_list_1, some_list_2)

# +
# number_three = [3, 'число три', ['число', 'три'], {'число': 3}]
# number_three

# +
# len(number_three)

# +
# # создадим список из букв
# abc_list = ['a', 'b', 'c', 'd', 'e']

# # выведем первый и последний элементы
# print(abc_list[0], abc_list[-1])

# +
# salary_list = [['Анна', 90000], ['Игорь', 85000], ['Алексей', 95000]]
# salary_list[1][0]

# +
# days_list = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# days_list[1:5]

# +
# weekdays = ['Понедельник', 'Вторник']

# weekdays.append('Четверг')
# weekdays

# +
# # для этого методу .insert() мы передаем желаемый индекс нового элемента
# # и сам этот элемент
# weekdays.insert(2, 'Среда')
# weekdays

# +
# weekdays[3] = 'Пятница'
# weekdays

# +
# # добавим к списку, в котором есть только понедельник, остальные дни
# more_weekdays = ['Вторник', 'Среда', 'Четверг', 'Пятница']

# weekdays.extend(more_weekdays)
# weekdays

# +
# # отсортируем список по возрастанию
# nums = [25, 10, 30, 20, 5, 15]
# sorted(nums)

# +
# # с помощью параметра reverse = True сортируем список по убыванию
# nums.sort(reverse = True)
# nums

# +
# joined_str = ''.join(str_list)
# joined_str

# +
# # создадим пустой список a_names
# a_names = []

# # пройдемся по списку имен
# for name in names:

#   # если имя начинается с 'А'
#   if name.startswith('А'):

#     # добавим его в список a_names
#     a_names.append(name)

# # посмотрим на результат
# a_names

# +
# a_names = [name for name in names if name.startswith('А')]
# a_names

# +
# lower_names = [name.lower() for name in names]
# lower_names

# +
# # импортируем класс стеммера Портера
# from nltk.stem import PorterStemmer

# # и создаем объект этого класса
# porter = PorterStemmer()

# # применяем метод .stem() к каждому слову с помощью list comprehension
# stemmed_p = [porter.stem(s) for s in lemmatized]
# print(stemmed_p)

# +
# # создадим кортеж
# letters = ('a', 'b', 'c')

# # и выведем его первый элемент
# letters[0]

# +
# # преобразуем кортеж в список через функцию list()
# letters = list(letters)

# # теперь элементы можно изменять
# letters[0] = 'd'
# letters

# +
# # создадим список с названием трех компаний
# companies = ['Microsoft', 'Apple', 'Tesla']

# # и в цикле поместим результат работы функции enumerate()
# # в одну переменную company
# for company in enumerate(companies):
#   print(company, type(company))

# +
# # снова возьмем список компаний
# companies = ['Microsoft', 'Apple', 'Tesla']

# # однако с функцией enumerate() используем две переменные
# for i, company in enumerate(companies):
#   print(i, company)

# +
# shopping_dict = {'огурцы': 2, 'помидоры': 3, 'лук': 1, 'картофель': 2}

# # используем две переменные с методом .items()
# for k, v in shopping_dict.items():
#   print(k, v)

# +
# # создадим одно пустое
# set_1 = set()

# # и два непустых множества с повторяющимся элементом 'c'
# set_2 = set(['a', 'b', 'c', 'c'])
# set_3 = {'a', 'b', 'c', 'c'}

# print(set_1, set_2, set_3)

# +
# set_A = {'a', 'b', 'c'}
# set_B = {'a', 'b', 'c', 'd', 'e', 'f'}

# set_A.issubset(set_B)

# +
# nlp = set(['Анна', 'Николай', 'Павел', 'Оксана'])
# cv = set(['Николай', 'Евгений', 'Ольга', 'Оксана'])
