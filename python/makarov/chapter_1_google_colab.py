"""Google colab."""

# +
# Модуль os и метод .walk()
# импортируем модуль os
# import os

# импортируем библиотеку
# import pandas as pd

# импортируем класс StandardScaler
# from sklearn.preprocessing import StandardScaler

# выводим пути к папкам (dirpath)
# и наименования файлов (filenames) и после этого
# for dirpath, _, filenames in os.walk("/content/"):

#  во вложенном цикле проходимся по названиям файлов
#     for filename in filenames:

# и соединяем путь до папок и входящие в эти папки файлы
# с помощью метода path.join()
#         print(os.path.join(dirpath, filename))

# Кроме того, если нас интересуют
# только видимые файлы и папки,
# мы можем воспользоваться командой !ls (ls означает to list, т.е. «перечислить»)

# +
# посмотрим на тип значений словаря uploaded
# type(uploaded["test.csv"])

# +
# Использование функции open() и конструкции with open()
# передадим функции open() адрес файла
# параметр 'r' означает, что мы хотим прочитать (read) файл
# f1 = open("/content/train.csv")

# метод .read() помещает весь файл в одну строку
# выведем первые 142 символа (если параметр не указывать, выведется все содержимое)
# print(f1.read(142))

# в конце файл необходимо закрыть
# f1.close()

# +
# снова откроем файл
# f2 = open("/content/train.csv")

# пройдемся по нашему объекту в цикле for
# и параллельно создадим индекс
# for i, line in enumerate(f2):

# выведем строки без служебных символов по краям
#     print(line.strip())

# дойдя до четвертой строки, прервемся
#     if i == 3:
#         break

# не забудем закрыть файл
# f2.close()

# +
# применим функцию read_csv()
# и посмотрим на первые три записи файла train.csv
# train = pd.read_csv("/content/train.csv")
# train.head(3)
