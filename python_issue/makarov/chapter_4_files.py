"""Files."""

# ### Подгрузка файлов
#

# #### Способ 2. Через модуль files библиотеки google.colab

# +
# from google.colab import files - only in google.colab
import os

import pandas as pd

files: int = 0
# uploaded: int = files.upload()
# -

# #### Модуль os и метод .walk()
#

for dirpath, _, filenames in os.walk("/content/"):
    for filename in filenames:
        print(os.path.join(dirpath, filename))

# #### Команда !ls
#

# !ls

# !ls /content/sample_data/

# ### Чтение из переменной uploaded
#

# +
# type(uploaded["test.csv"])
# -

# #### Пример работы с объектом bytes
#

# +
# uploaded_str: str = uploaded["test.csv"].decode()
# print(type(uploaded_str))

# +
# print(uploaded_str[:35])

# +
# uploaded_list: str = uploaded_str.split("\r\n")
# type(uploaded_list)

# +
# for i, line in enumerate(uploaded_list):
#    print(line)
#    if i == 3:
#        break
# -

# #### Использование функции open() и конструкции with open()
#

with open("/content/train.csv", encoding="utf-8") as f1:
    print(f1.read(142))


with open("/content/train.csv", encoding="utf-8") as f2:
    for i, line in enumerate(f2):
        print(line.strip())
        if i == 3:
            break


with open("/content/train.csv", encoding="utf-8") as f3:
    for i, line in enumerate(f3):
        print(line.strip())
        if i == 3:
            break

# #### Чтение через библиотеку Pandas
#

train: pd.DataFrame = pd.read_csv("/content/train.csv")
train.head(3)
test: pd.DataFrame = pd.read_csv("/content/test.csv")
test.head(3)
