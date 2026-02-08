"""Работа с файлами."""

# ## Работа с файлами в Google Colab

# ### Этап 1. Подгрузка файлов

# Способ 1. Вручную через вкладку 'Файлы'

# Способ 2. Через модуль files библиотеки google.colab

# +
# импортируем модуль os
import os

# импортируем библиотеку
import pandas as pd
from google.colab import files

# -

uploaded = files.upload()

# ### Этап 2. Чтение файлов

# #### Просмотр содержимого папки /content/

# Модуль os и метод .walk()

# выводим пути к папкам (dirpath) и наименования файлов (filenames) и после этого
for dirpath, _, filenames in os.walk("/content/"):
    # во вложенном цикле проходимся по названиям файлов
    for filename in filenames:
        # и соединяем путь до папок и входящие в эти папки файлы
        # с помощью метода path.join()
        print(os.path.join(dirpath, filename))

# Команда `!ls`

# посмотрим на содержимое папки contest
# !ls

# заглянем внутрь sample_data
# !ls /content/sample_data/

# #### Чтение из переменной uploaded

type(uploaded["test.csv"])  # вывод: bytes

# Пример работы с объектом bytes

# +
# обратимся к ключу словаря uploaded и применим метод .decode()
uploaded_str = uploaded["test.csv"].decode()

# на выходе получим обычную строку
print(type(uploaded_str))  # вывод: str

# +
# если разбить строку методом .split() по символам \r (возврат к началу строки) и \n (новая строка)
uploaded_list = uploaded_str.split("\r\n")

# на выходе мы получим список
type(uploaded_list)  # вывод: list

# +
for i, line in enumerate(uploaded_list):
    print(line)
    if i == 3:
        break

# Вывод:
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 892,3,"Kelly, Mr. James",male,34.5,0,0,330911,7.8292,,Q
# 893,3,"Wilkes, Mrs. James (Ellen Needs)",female,47,1,0,363272,7,,S
# 894,2,"Myles, Mr. Thomas Francis",male,62,0,0,240276,9.6875,,Q
# -

# #### Использование функции open() и конструкции with open()

# передадим функции open() адрес файла
# параметр 'r' означает, что мы хотим прочитать (read) файл
with open("./content/train.csv", encoding="utf-8") as f1:

    # метом .read() помещает весь файл в одну строку
    # выведем первые 142 символа (если параметр не указывать выведется всё содержимое)
    print(f1.read(142))

    # в конце файл необходимо закрыть
    f1.close()

    # Вывод:
    # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    # 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S№

# снова откроем файл
with open("./content/train.csv", encoding="utf-8") as f2:

    # пройдемся по нашему объекту в цикле for и параллельно создадим индекс
    for i, line in enumerate(f2):

        # выведем строки без служебных символов по краям
        print(line.strip())

        # дойдя до четвертой строки, прервемся
        if i == 3:
            break

    # и не забудем закрыть файл
    f2.close()

    # Вывод:
    # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    # 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
    # 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
    # 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S

# +
# скажем Питону открой файл и назови его f3
with open("./content/test.csv", encoding="utf-8") as f3:

    # пройдись по строкам без служебных символов
    for i, line in enumerate(f3):
        print(line.strip())

        # и прервись на четвертой строке
        if i == 3:
            break

# Вывод:
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 892,3,"Kelly, Mr. James",male,34.5,0,0,330911,7.8292,,Q
# 893,3,"Wilkes, Mrs. James (Ellen Needs)",female,47,1,0,363272,7,,S
# 894,2,"Myles, Mr. Thomas Francis",male,62,0,0,240276,9.6875,,Q
# -

# #### Чтение через библиотеку Pandas

# применим функцию read_csv() и посмотрим на первые три записи файла train.csv
train = pd.read_csv("./content/train.csv")
train.head(3)  # Вывод: первые три записи датафрейма

# ### Этап 4. Сохранение нового файла на сервере

# Пример оформления результата

# +
# файл с примером можно загрузить не с локального компьютера, а из Интернета
url = "https://www.dmitrymakarov.ru/wp-content/uploads/2021/11/titanic_example.csv"

# просто поместим его url в функцию read_csv()
example = pd.read_csv(url)
example.head(3)
# -

# Сохранение результата

# +
# создадим новый файл result.csv с помощью функции to_csv(), удалив при этом индекс

example.head(15).to_csv("result.csv", index=False)

# файл будет успешно сохранён в 'Cессионном хранилище' и, если всё пройдёт успешно, выведем следующий текст:
print("Файл успешно сохранился в сессионное хранилище!")
# -

# ### Этап 5. Скачивание обратно на жесткий диск

# применим метод .download() объекта files
files.download("/content/result.csv")
