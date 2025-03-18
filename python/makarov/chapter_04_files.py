# ## Работа с файлами в Google Colab

"""Work with files."""

# ! pip install seaborn
# ! pip install pandas
# ! pip install numpy
# ! pip install scikit-learn

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
# для построения графиков воспользуемся новой для нас библиотекой seaborn
import seaborn as sns
# из библиотеки google.colab импортируем класс files
from google.colab import files
# импортируем логистическую регрессию из модуля linear_model библиотеки sklearn
from sklearn.linear_model import LogisticRegression
# импортируем метрику accuracy из sklearn
# построим матрицу ошибок
from sklearn.metrics import accuracy_score, confusion_matrix
# импортируем класс StandardScaler
from sklearn.preprocessing import StandardScaler

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

# ### Этап 3. Построение модели и прогноз

# #### **Шаг 1**. Обработка и анализ данных

# Исследовательский анализ данных (EDA)

# посмотрим на данные в целом
train.info()

# посмотрим насколько значим класс билета для выживания пассажира
# с помощью x и hue мы можем уместить две категориальные переменные
sns.countplot(x="Pclass", hue="Survived", data=train)

# кто выживал чаще, мужчины или женщины?
sns.countplot(x="Sex", hue="Survived", data=train)

# Пропущенные значения

# выявим пропущенные значения с помощью .isnull() и посчитаем их через sum()
train.isnull().sum()

# переменная Cabin (номер каюты), скорее всего, не является самой важной
# избавимся от нее с помощью метода .drop()
# (параметр axis = 1 отвечает за столбцы, inplace = True сохраняет изменения)
train.drop(columns="Cabin", axis=1, inplace=True)

# а вот Age (возраст) скорее важен, заменим пустые значения сред. ариф.
train["Age"] = train["Age"].fillna(train["Age"].mean())

# у нас остаются две пустые строки в Embarked, удалим их
train.dropna(inplace=True)

# посмотрим на результат
train.isnull().sum()

# Категориальные переменные

# one-hot encoding к переменной Sex (пол) с помощью функции pd.get_dummies()
pd.get_dummies(train["Sex"]).head(3)

# снова скачаем столбец Sex из датасета train в формате датафрейма
previous = pd.read_csv("/content/train.csv")[["Sex"]]
previous.head()

# закодируем переменную через 0 и 1
pd.get_dummies(previous["Sex"], dtype=int).head(3)

# удалим первый столбец, он избыточен
sex = pd.get_dummies(train["Sex"], drop_first=True)
sex.head(3)

# сделаем то же самое для переменных Pclass и Embarked
embarked = pd.get_dummies(train["Embarked"], drop_first=True)
pclass = pd.get_dummies(train["Pclass"], drop_first=True)

# присоединим закодированные через one-hot encoding переменные
# к исходному датафрейму через функцию .concat()
train = pd.concat([train, pclass, sex, embarked], axis=1)
train.head(3)

# Отбор признаков

# удалим те столбцы, которые нам теперь не нужны
fields_to_drop = ["PassengerId", "Pclass", "Name", "Sex", "Ticket", "Embarked"]
train.drop(fields_to_drop, axis=1, inplace=True)
train.head(3)

# Нормализация данных

# +
# создадим объект этого класса
scaler = StandardScaler()

# выберем те столбцы, которые мы хотим масштабировать
cols_to_scale = ["Age", "Fare"]

# рассчитаем среднее арифметическое и СКО для масштабирования данных
scaler.fit(train[cols_to_scale])

# применим их
train[cols_to_scale] = scaler.transform(train[cols_to_scale])

# посмотрим на результат
train.head(3)
# -

# названия столбцов теперь представляют собой числа, так быть не должно
train.columns

# преобразуем эти переменные в тип str через функцию map()
train.columns = train.columns.map(str)
train.columns

# #### **Шаг 2**. Разделение обучающей выборки на признаки \
# (X_train) и целевую переменную (y_train)

# +
# поместим в X_train все кроме столбца Survived
X_train = train.drop("Survived", axis=1)

# столбец 'Survived' станет нашей целевой переменной (y_train)
y_train = train["Survived"]
# -

X_train.head(3)

# #### **Шаг 3**. Обучение модели логистической регрессии

# Обучим модель

# +
# создадим объект этого класса и запишем его в переменную model
model = LogisticRegression()

# обучим нашу модель
model.fit(X_train, y_train)
# -

# Сделаем прогноз на обучающей выборке

# сделаем предсказание класса на обучающей выборке
y_pred_train = model.predict(X_train)

# Оценка качества модели на обучающей выборке

# +
# передадим ей фактические и прогнозные значения
conf_matrix = confusion_matrix(y_train, y_pred_train)

# преобразуем в датафрейм
conf_matrix_df = pd.DataFrame(conf_matrix)
conf_matrix_df
# -

# для удобства можем добавить подписи
conf_matrix_labels = pd.DataFrame(
    conf_matrix,
    columns=["Прогноз погиб", "Прогноз выжил"],
    index=["Факт погиб", "Факт выжил"],
)
conf_matrix_labels

# рассчитаем метрику accuracy вручную
round((479 + 237) / (479 + 237 + 70 + 103), 3)

# +
# так же передадим ей фактические и прогнозные значения
model_accuracy = accuracy_score(y_train, y_pred_train)

# округлим до трех знаков после запятой
round(model_accuracy, 3)
# -

# #### **Шаг 4**. Построение прогноза на тестовой выборке

# посмотрим на тестовые данные
test.info()

test.head(3)

# теперь нам нужно создать тестовую выборку с теми же признаками
# и для начала дадим датасету привычное название
X_test = test

# заполним пропуски в переменных Age и Fare средним арифметическим
X_test["Age"] = X_test["Age"].fillna(test["Age"].mean())
X_test["Fare"] = X_test["Fare"].fillna(test["Fare"].mean())

# выполним one-hot encoding категориальных переменных
sex = pd.get_dummies(X_test["Sex"], drop_first=True)
embarked = pd.get_dummies(X_test["Embarked"], drop_first=True)
pclass = pd.get_dummies(X_test["Pclass"], drop_first=True)

# +
# присоединим новые столбцы к исходному датафрейму
X_test = pd.concat([test, pclass, sex, embarked], axis=1)

# и удалим данные, которые теперь не нужны
X_test.drop(
    ["PassengerId", "Pclass", "Name", "Sex", "Cabin", "Ticket", "Embarked"],
    axis=1,
    inplace=True,
)

# посмотрим на результат
X_test.head(3)
# -

# применим среднее арифметическое и СКО обучающей выборки
X_test[cols_to_scale] = scaler.transform(X_test[cols_to_scale])
X_test.head(3)

# превратим названия столбцов в строки
X_test.columns = X_test.columns.map(str)

# сделаем прогноз на тестовой выборке
y_pred_test = model.predict(X_test)

# посмотрим на первые 10 прогнозных значений
y_pred_test[:10]

# ### Этап 4. Сохранение нового файла на сервере Google

# Пример оформления результата

# +
# файл с примером можно загрузить не с локального компьютера, а из Интернета
host = "https://www.dmitrymakarov.ru/"
url = host + "wp-content/uploads/2021/11/titanic_example.csv"

# просто поместим его url в функцию read_csv()
example = pd.read_csv(url)
example.head(3)
# -

# Создание файла с прогнозом

# +
# возьмем индекс пассажиров из столбца PassengerId тестовой выборки
ids = test["PassengerId"]

# создадим датафрейм из словаря, в котором
# первая пара ключа и значения - это id пассажира, вторая - прогноз "на тесте"
result = pd.DataFrame({"PassengerId": ids, "Survived": y_pred_test})

# посмотрим, что получилось
result.head()

# +
# создадим новый файл result.csv с помощью to_csv(), удалив при этом индекс
result.to_csv("result.csv", index=False)

# файл будет сохранен и, если все пройдет успешно, выведем следующий текст:
print("Файл успешно сохранился в сессионное хранилище!")
# -

# ### Этап 5. Скачивание обратно на жесткий диск

# применим метод .download() объекта files
files.download("/content/result.csv")
