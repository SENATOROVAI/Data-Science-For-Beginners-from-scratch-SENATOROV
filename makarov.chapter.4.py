# ## Работа с файлами в Google Colab

# ### Этап 1. Подгрузка файлов

# Способ 1. Вручную через вкладку 'Файлы'
#
#
#

# Способ 2. Через модуль files библиотеки google.colab

# +
# импортируем модль os
import os

# импортируем библиотеку
import pandas as pd

#  из google.colab import files
from google.colab import files

# -

# создаем объект этого клласа, применяем метод .upload()
uploaded = files.upload()

# +
# посмотрим на содержимое словаря uploaded
# uploaded
# -

# ### Этап 2. Чтение файлов

# ### просмотр содержимого папки/content/

# #### модуль os и метод .walk()

# выводим пути к папкам (dirpath) и на именования файлов (filenames) и послеэтого
for dirpath, _, filenames in os.walk("/content"):
    print(f"В папке {dirpath} находятся файлы: {filenames}")

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
# если разбить строку методом .split() по символам \r (возврат к началу строки) и \n (новая строка)
uploaded_list = uploaded_str.split("\r\n")

# на выходе мы получим список
type(uploaded_list)
# -

# пройдемся по этому списку, не забыв создать индекс с помощью функции enumerate()
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
f1 = open("/content/train.csv")

# метод .read() помещает весь файл в одну строку
# выведем первые 142 символа (если параметр не указывать, выведется все содержимое)
print(f1.read(142))

# в конце файл необходимо закрыть
f1.close()

# +
# снова откроем файл
f2 = open("/content/train.csv")

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
with open("/content/test.csv") as f3:

    # "пройдись по строкам без служебных символов"
    for i, line in enumerate(f3):
        print(line.strip())

        # и "прервись на четвертой строке"
        if i == 3:
            break

# ### Чтение через библиотеку Pandas

# применим функцию  read_csv() и первый три записи файла train.csv
traun = pd.read_csv("/content/train.csv")
train.head(3)

# сделаем то же самое с файлом test.csv
test = pd.read_csv("/content/test.csv")
test.head(3)
