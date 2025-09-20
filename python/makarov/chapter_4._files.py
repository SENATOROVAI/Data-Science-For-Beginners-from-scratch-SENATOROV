"""Работа с файлами в Google Colab."""

# ### Этап 1. Подгрузка файлов

# Способ 1. Вручную через вкладку 'Файлы'

# +
# см. материалы урока на сайте
# -

# Способ 2. Через модуль files библиотеки google.colab

# +
# импортируем модуль os
# fmt: off
import os

# импортируем библиотеку
import pandas as pd

# из библиотеки google.colab импортируем класс files
from google.colab import files

# fmt: on
# -

# создаем объект этого класса, применяем метод .upload()
uploaded = files.upload()

# +
# посмотрим на содержимое словаря uploaded
# uploaded
# -

# ### Этап 2. Чтение файлов

# #### Просмотр содержимого папки /content/

# ##### Модуль os и метод .walk()

# выводим пути к папкам (dirpath) и наименования файлов (filenames)
for dirpath, _, filenames in os.walk("/content/"):

    # во вложенном цикле проходимся по названиям файлов
    for filename in filenames:

        # и соединяем путь до папок и входящие в эти папки файлы
        # с помощью метода path.join()
        print(os.path.join(dirpath, filename))

# ##### Команда `!ls`

# посмотрим на содержимое папки content
# !ls

# заглянем внутрь sample_data
# !ls /content/sample_data/

# #### Чтение из переменной uploaded

# посмотрим на тип значений словаря uploaded
type(uploaded["test.csv"])

# Пример работы с объектом bytes

# +
# обратимся к ключу словаря uploaded и применим метод .decode()
uploaded_str = uploaded["test.csv"].decode()

# на выходе получаем обычную строку
print(type(uploaded_str))
# -

# выведем первые 35 значений
print(uploaded_str[:35])

# +
# если разбить строку методом .split()
uploaded_list = uploaded_str.split("\r\n")

# на выходе мы получим список
type(uploaded_list)
# -

# пройдемся по этому списку, не забыв создать индекс с enumerate()
for i, line in enumerate(uploaded_list):

    # начнем выводить записи
    print(line)

    # когда дойдем до четвертой строки
    if i == 3:

        # прервемся
        break

# #### Использование функции open() и конструкции with open()

# +
# передадим функции open() адрес файла
# параметр 'r' означает, что мы хотим прочитать (read) файл
# pylint: disable=consider-using-with
f1 = open("/content/train.csv", encoding="UTF-8")  # noqa: R1732

# метод .read() помещает весь файл в одну строку
# первые 142 символа (если параметр не указывать, выведется все содержимое)
print(f1.read(142))

# в конце файл необходимо закрыть
f1.close()

# +
# снова откроем файл
# pylint: disable=consider-using-with
f2 = open("/content/train.csv", encoding="UTF-8")  # noqa: R1732

# пройдемся по нашему объекту в цикле for и параллельно создадим индекс
for i, line in enumerate(f2):

    # выведем строки без служебных символов по краям
    print(line.strip())

    # дойдя до четвертой строки, прервемся
    if i == 3:
        break

# не забудем закрыть файл
f2.close()
# -

# скажем Питону: "открой файл  и назови его f3"
with open("/content/test.csv", encoding="UTF-8") as f3:

    # "пройдись по строкам без служебных символов"
    for i, line in enumerate(f3):
        print(line.strip())

        # и "прервись на четвертой строке"
        if i == 3:
            break

# #### Чтение через библиотеку Pandas

# применим функцию read_csv() и посмотрим на первые три записи файла train.csv
train = pd.read_csv("/content/train.csv")
train.head(3)

# сделаем то же самое с файлом test.csv
test = pd.read_csv("/content/test.csv")
test.head(3)

# ### Этап 4. Сохранение нового файла на сервере Google

# +
# файл с примером можно загрузить не с локального компьютера, а из Интернета
host = "https://www.dmitrymakarov.ru/"
url = host + "wp-content/uploads/2021/11/titanic_example.csv"

# просто поместим его url в функцию read_csv()
example = pd.read_csv(url)
example.head(3)

# +
# создадим новый файл result.csv с помощью to_csv(), удалив при этом индекс
example.to_csv("result.csv", index=False)

# файл будет сохранен и, если все пройдет успешно, выведем следующий текст:
print("Файл успешно сохранился в сессионное хранилище!")
# -

# ### Этап 5. Скачивание обратно на жесткий диск

# применим метод .download() объекта files
files.download("/content/result.csv")
