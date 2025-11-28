"""EDA practice."""

# # Практика EDA

# +
# codespell:disable
# pylint: disable=too-many-lines

# импортируем библиотеки
import io
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
from dotenv import load_dotenv
import sweetviz as sv
from matplotlib.axes._axes import _log as matplotlib_axes_logger
# -

# ## Подготовка данных

# ### Датасет "Титаник"

# +
load_dotenv()

train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
response = requests.get(train_csv_url)

# для импорта используем функцию read_csv()
titanic = pd.read_csv(io.BytesIO(response.content))

# посмотрим на первые три записи
# последние записи можно посмотреть с помощью метода .tail()
titanic.head(3)
# -

# иногда для получения более объективного представления о данных
# удобно использовать .sample()
# в данном случае мы получаем пять случайных наблюдений
titanic.sample(5)

# посмотрим на количество непустых значений, тип данных,
# статистику по типам данных и объем занимаемой памяти
titanic.info()

# найдем пропуски в датафрейме и просуммируем их по столбцам
titanic.isnull().sum()

# выполним простую обработку данных
# в частности, избавимся от столбца Cabin
titanic.drop(labels="Cabin", axis=1, inplace=True)
# заполним пропуски в столбце Age медианным значением
titanic["Age"] = titanic.Age.fillna(titanic.Age.median())
# два пропущенных значения в столбце Embarked заполним портом Southhampton
titanic["Embarked"] = titanic.Embarked.fillna("S")
# проверим результат (найдем общее количество пропусков сначала по столбцам,
# затем по строкам)
titanic.isnull().sum().sum()

# ### Датасет Tips

# для импорта воспользуемся функцией load_dataset() с параметром 'tips'
tips = sns.load_dataset("tips")
tips.head(3)

tips.info()

tips.isnull().sum()

# ## Описание

# ### Категориальные данные

# #### Методы `.unique()` и `.value_counts()`

# Методы ниже похожи на `np.unique(return_counts = True)`

# применим метод библиотеки Numpy
np.unique(titanic.Survived, return_counts=True)

# теперь воспользуемся методами библиотеки Pandas
# первый метод возращает только уникальные значения
titanic.Survived.unique()

# второй - уникальные значения и их частоту
titanic.Survived.value_counts()

# для получения относительной частоты, делить на общее количество строк не нужно,
# достаточно указать параметр normalize = True
titanic.Survived.value_counts(normalize=True)

# короткое решение: различие можно увидеть и с помощью mean()
# titanic.Survived.mean().round(2)
round(titanic.Survived.mean(), 2)

# #### `df.describe()`

# подробное описание результатов вывода этого метода для категориальных данных
# вы найдете на странице занятия
titanic[["Sex", "Embarked"]].describe()

# #### countplot и barplot

# функция countplot() сама посчитает количество наблюдений в каждой из категорий
sns.countplot(x="Survived", data=titanic);

# для функции barplot() количество наблюдений можно посчитать
# с помощью метода .value_counts()
sns.barplot(x=titanic.Survived, y=titanic.Survived.value_counts());

# относительное количество наблюдений удобно посчитать с параметром normalize = True
sns.barplot(x=titanic.Survived, y=titanic.Survived.value_counts(normalize=True));

# Matplotlib

# +
# первым параметром (по оси x) передадим уникальные значения,
# вторым параметром - количество наблюдений
plt.bar(
    titanic.Survived.unique(),
    titanic.Survived.value_counts(),
    # кроме того, явно пропишем значения оси x
    # (в противном случае будет указана просто числовая шкала)
    tick_label=["0", "1"],
)

plt.xlabel("Survived")
plt.ylabel("Count");

# +
# горизонтальная столбчатая диаграмма строится почти так же
plt.barh(
    titanic.Survived.unique(), titanic.Survived.value_counts(), tick_label=["0", "1"]
)

plt.xlabel("Count")
plt.ylabel("Survived");

# +
# найдем относительную частоту категорий с помощью параметра normalize = True
plt.bar(
    titanic.Survived.unique(),
    titanic.Survived.value_counts(normalize=True),
    tick_label=["0", "1"],
)

plt.xlabel("Survived")
plt.ylabel("Proportion");
# -

# перед применением метода .plot.bar() данные необходимо сгруппировать
# параметр rot = 0 ставит деления шкалы по оси x вертикально
titanic.groupby("Survived")["PassengerId"].count().plot.bar(rot=0)
plt.ylabel("count");

# можно также сначала выбрать один столбец
# и затем воспользоваться методом .value_counts()
titanic.Survived.value_counts().plot.bar(rot=0)
plt.xlabel("Survived")
plt.ylabel("count");

# ### Количественные данные

# #### `df.describe()`

# применим метод .describe() к количественным признакам
tips[["total_bill", "tip"]].describe().round(2)

# выведем второй и четвертый дециль, а также 99-й процентиль
tips[["total_bill", "tip"]].describe(percentiles=[0.2, 0.4, 0.99]).round(2)

# #### Гистограмма

# гистограмма распределения размера чека с помощью библиотеки Matplotlib
plt.hist(tips.total_bill, bins=10);

# такую же гистограмму можно построить с помощью Pandas
tips.total_bill.plot.hist(bins=10);

# в библиотеке Seaborn мы указываем источник данных,
# что будет на оси x и количество интервалов
# параметр kde = True добавляет кривую плотности распределения
sns.histplot(data=tips, x="total_bill", bins=10, kde=True);

# функция displot() - еще один способ построить гистограмму в Seaborn
# для этого используется параметр по умолчанию kind = 'hist'
sns.displot(data=tips, x="total_bill", kind="hist", bins=10);

# Plotly, как уже было сказано, позволяет построить интерактивную гистограмму
# параметр text_auto = True выводит количество наблюдений в каждом интервале
px.histogram(tips, x="total_bill", nbins=10, text_auto=True)

# #### График плотности

# используем функцию displot(), которой передадим датафрейм tips,
# какой признак вывести по оси x, тип графика kind = 'kde',
# а также заполним график цветом через fill = True
sns.displot(tips, x="total_bill", kind="kde", fill=True);

# #### boxplot

# Seaborn

# функции boxplot() достаточно передать параметр x
# с данными необходимого столбца
sns.boxplot(x=tips.total_bill);

# если передать нужный нам столбец в параметр x,
# то мы получим горизонтальный boxplot
px.box(tips, x="total_bill")

# если в y, то вертикальный
px.box(tips, y="total_bill")

# Matplotlib и Pandas

# ##### plt.boxplot(tips.total_bill);

# ##### tips.total_bill.plot.box();

# #### Гистограмма и boxplot

# Matplotlib и Seaborn

# +
# создадим два подграфика ax_box и ax_hist
# кроме того, укажем, что нам нужны:
fig, (ax_box, ax_hist) = plt.subplots(
    2,  # две строки в сетке подграфиков,
    sharex=True,  # единая шкала по оси x и
    gridspec_kw={"height_ratios": (0.15, 0.85)},
)  # пропорция 15/85 по высоте

# затем создадим графики, указав через параметр ax в какой подграфик
# поместить каждый из них
sns.boxplot(x=tips["total_bill"], ax=ax_box)
sns.histplot(x=tips["total_bill"], ax=ax_hist, bins=10, kde=True)

# добавим подписи к каждому из графиков через метод .set()
ax_box.set(xlabel="")  # пустые кавычки удаляют подпись (!)
ax_hist.set(xlabel="total_bill")
ax_hist.set(ylabel="count")

# выведем результат
plt.show()
# -

# Plotly

# воспользуемся функцией histogram(),
px.histogram(
    tips,  # передав ей датафрейм,
    x="total_bill",  # конкретный столбец для построения данных,
    nbins=10,  # количество интервалов в гистограмме
    marginal="box",
)  # и тип дополнительного графика

# ## Нахождение отличий

# ### Два категориальных признака

# #### countplot и barplot

# Seaborn

# создадим grouped countplot, где по оси x будет класс, а по оси y - количество пассажиров
# в каждом классе данные разделены на погибших (0) и выживших (1)
sns.countplot(x="Pclass", hue="Survived", data=titanic);

# горизонтальный countplot получится,
# если передать данные о классе пассажира в переменную y
sns.countplot(y="Pclass", hue="Survived", data=titanic);

# относительное количество наблюдений удобно посчитать с параметром normalize = True
sns.barplot(x=titanic.Survived, y=titanic.Survived.value_counts(normalize=True));

# Matplotlib

# +
# первым параметром (по оси x) передадим уникальные значения,
# вторым параметром - количество наблюдений
plt.bar(
    titanic.Survived.unique(),
    titanic.Survived.value_counts(),
    # кроме того, явно пропишем значения оси x
    # (в противном случае будет указана просто числовая шкала)
    tick_label=["0", "1"],
)

plt.xlabel("Survived")
plt.ylabel("Count");

# +
# горизонтальная столбчатая диаграмма строится почти так же
plt.barh(
    titanic.Survived.unique(), titanic.Survived.value_counts(), tick_label=["0", "1"]
)

plt.xlabel("Count")
plt.ylabel("Survived");

# +
# найдем относительную частоту категорий с помощью параметра normalize = True
plt.bar(
    titanic.Survived.unique(),
    titanic.Survived.value_counts(normalize=True),
    tick_label=["0", "1"],
)

plt.xlabel("Survived")
plt.ylabel("Proportion");
# -

# Pandas

# перед применением метода .plot.bar() данные необходимо сгруппировать
# параметр rot = 0 ставит деления шкалы по оси x вертикально
titanic.groupby("Survived")["PassengerId"].count().plot.bar(rot=0)
plt.ylabel("count");

# можно также сначала выбрать один столбец
# и затем воспользоваться методом .value_counts()
titanic.Survived.value_counts().plot.bar(rot=0)
plt.xlabel("Survived")
plt.ylabel("count");

# ### Количественные данные

# #### `df.describe()`

# применим метод .describe() к количественным признакам
tips[["total_bill", "tip"]].describe().round(2)

# выведем второй и четвертый дециль, а также 99-й процентиль
tips[["total_bill", "tip"]].describe(percentiles=[0.2, 0.4, 0.99]).round(2)

# #### Гистограмма

# гистограмма распределения размера чека с помощью библиотеки Matplotlib
plt.hist(tips.total_bill, bins=10);

# такую же гистограмму можно построить с помощью Pandas
tips.total_bill.plot.hist(bins=10);

# в библиотеке Seaborn мы указываем источник данных,
# что будет на оси x и количество интервалов
# параметр kde = True добавляет кривую плотности распределения
sns.histplot(data=tips, x="total_bill", bins=10, kde=True);

# функция displot() - еще один способ построить гистограмму в Seaborn
# для этого используется параметр по умолчанию kind = 'hist'
sns.displot(data=tips, x="total_bill", kind="hist", bins=10);

# Plotly, как уже было сказано, позволяет построить интерактивную гистограмму
# параметр text_auto = True выводит количество наблюдений в каждом интервале
px.histogram(tips, x="total_bill", nbins=10, text_auto=True)

# #### График плотности

# используем функцию displot(), которой передадим датафрейм tips,
# какой признак вывести по оси x, тип графика kind = 'kde',
# а также заполним график цветом через fill = True
sns.displot(tips, x="total_bill", kind="kde", fill=True);

# #### boxplot

# Seaborn

# функции boxplot() достаточно передать параметр x
# с данными необходимого столбца
sns.boxplot(x=tips.total_bill);

# Plotly

# если передать нужный нам столбец в параметр x,
# то мы получим горизонтальный boxplot
px.box(tips, x="total_bill")

# если в y, то вертикальный
px.box(tips, y="total_bill")

# Matplotlib и Pandas

# ##### plt.boxplot(tips.total_bill);

# ##### tips.total_bill.plot.box();

# #### Гистограмма и boxplot

# Matplotlib и Seaborn

# +
# создадим два подграфика ax_box и ax_hist
# кроме того, укажем, что нам нужны:
fig, (ax_box, ax_hist) = plt.subplots(
    2,  # две строки в сетке подграфиков,
    sharex=True,  # единая шкала по оси x и
    gridspec_kw={"height_ratios": (0.15, 0.85)},
)  # пропорция 15/85 по высоте

# затем создадим графики, указав через параметр ax в какой подграфик
# поместить каждый из них
sns.boxplot(x=tips["total_bill"], ax=ax_box)
sns.histplot(x=tips["total_bill"], ax=ax_hist, bins=10, kde=True)

# добавим подписи к каждому из графиков через метод .set()
ax_box.set(xlabel="")  # пустые кавычки удаляют подпись (!)
ax_hist.set(xlabel="total_bill")
ax_hist.set(ylabel="count")

# выведем результат
plt.show()
# -

# Plotly

# воспользуемся функцией histogram(),
px.histogram(
    tips,  # передав ей датафрейм,
    x="total_bill",  # конкретный столбец для построения данных,
    nbins=10,  # количество интервалов в гистограмме
    marginal="box",
)  # и тип дополнительного графика

# ## Нахождение отличий

# ### Два категориальных признака

# #### countplot и barplot

# Seaborn

# создадим grouped countplot, где по оси x будет класс, а по оси y - количество пассажиров
# в каждом классе данные разделены на погибших (0) и выживших (1)
sns.countplot(x="Pclass", hue="Survived", data=titanic);

# горизонтальный countplot получится,
# если передать данные о классе пассажира в переменную y
sns.countplot(y="Pclass", hue="Survived", data=titanic);

# передадим функции catplot() параметр kind = 'count' для создания графика countplot
sns.catplot(x="Pclass", hue="Survived", data=titanic, kind="count");

# добавим еще один признак (пол) через параметр col
sns.catplot(x="Pclass", hue="Survived", col="Sex", kind="count", data=titanic);

# Plotly

px.histogram(
    titanic,  # возьмем данные
    x="Pclass",  # диаграмму будем строить по столбцу Pclass
    color="Survived",  # с разбивкой на выживших и погибших
    barmode="group",  # разделенные столбцы располагаются рядом друг с другом
    text_auto=True,  # выведем количество наблюдений в каждом столбце
    title="Survival by class",  # также добавим заголовок
)

# +
# создадим объект fig, в который поместим столбчатую диаграмму
fig = px.histogram(
    titanic,
    x="Pclass",
    color="Survived",
    barmode="stack",  # каждый столбец класса будет разделен по признаку Survived
    text_auto=True,
)

# применим метод .update_layout() к объекту fig
fig.update_layout(
    title_text="Survival by class",  # заголовок
    xaxis_title_text="Pclass",  # подпись к оси x
    yaxis_title_text="Count",  # подпись к оси y
    bargap=0.2,  # расстояние между столбцами
    # подписи классов пассажиров на оси x
    xaxis={
        "tickmode": "array",
        "tickvals": [1, 2, 3],
        "ticktext": ["Class 1", "Class 2", "Class 3"],
    },
)

fig.show()
# -

# используем новый параметр facet_col = 'Sex'
px.histogram(
    titanic,
    x="Pclass",
    color="Survived",
    facet_col="Sex",
    barmode="group",
    text_auto=True,
    title="Survival by class and gender",
)

# используем одновременно параметры facet_col и facet_row
px.histogram(
    titanic,
    x="Pclass",
    color="Survived",
    facet_col="Embarked",
    facet_row="Sex",
    barmode="group",
    text_auto=True,
    title="Survival by class, gender and port of embarkation",
)

# используем новый параметр facet_col = 'Sex'
px.histogram(
    titanic,
    x="Pclass",
    color="Survived",
    facet_col="Sex",
    barmode="group",
    text_auto=True,
    title="Survival by class and gender",
)

# используем одновременно параметры facet_col и facet_row
px.histogram(
    titanic,
    x="Pclass",
    color="Survived",
    facet_col="Embarked",
    facet_row="Sex",
    barmode="group",
    text_auto=True,
    title="Survival by class, gender and port of embarkation",
)

# #### Таблица сопряженности  

# Абсолютное количество наблюдений

# +
# создадим таблицу сопряженности
# в параметр index мы передадим данные по классу, в columns - по выживаемости
pclass_abs = pd.crosstab(index=titanic.Pclass, columns=titanic.Survived)

# создадим названия категорий класса и выживаемости
pclass_abs.index = pd.Index(["Class 1", "Class 2", "Class 3"])
pclass_abs.columns = ["Not survived", "Survived"]

# выведем результат
pclass_abs
# -

# построим grouped barplot в библиотеке Pandas
# rot = 0 делает подписи оси х вертикальными
pclass_abs.plot.bar(rot=0);

# параметр stacked = True делит каждый столбец класса на выживших и погибших
pclass_abs.plot.bar(rot=0, stacked=True);

# в Matplotlib вначале создадим barplot для одной (нижней) категории
plt.bar(pclass_abs.index, pclass_abs["Not survived"])
# затем еще один barplot для второй (верхней), указав нижнуюю в параметре bottom
plt.bar(pclass_abs.index, pclass_abs["Survived"], bottom=pclass_abs["Not survived"]);

# Таблица сопряженности вместе с суммой

# +
# для подсчета суммы по строкам и столбцам используется параметр margins = True
pclass_abs = pd.crosstab(index=titanic.Pclass, columns=titanic.Survived, margins=True)

# новой строке и новому столбцу с суммами необходимо дать название (например, Total)
pclass_abs.index = pd.Index(["Class 1", "Class 2", "Class 3", "Total"])
pclass_abs.columns = ["Not survived", "Survived", "Total"]
pclass_abs
# -

# Относительное количество наблюдений

# +
# так как нам важно понимать долю выживших и долю погибших, укажем normalize = # 'index'
# в этом случае каждое значение будет разделено на общее количество
# наблюдений # в строке (!)
pclass_rel = pd.crosstab(
    index=titanic.Pclass, columns=titanic.Survived, normalize="index"
)

pclass_rel.index = pd.Index(["Class 1", "Class 2", "Class 3"])
pclass_rel.columns = ["Not survived", "Survived"]
pclass_rel

# +
# если бы в индексе (в строках) была выживаемость, а в столбцах - классы,
# то логично было бы использовать параметр normalize = 'columns' для деления
# на сумму по столбцам
pclass_rel_t = pd.crosstab(
    index=titanic.Survived, columns=titanic.Pclass, normalize="columns"
)

pclass_rel_t.index = pd.Index(["Not survived", "Survived"])
pclass_rel_t.columns = ["Class 1", "Class 2", "Class 3"]
pclass_rel_t
# -

# теперь на stacked barplot мы видим доли выживших в каждом из классов
pclass_rel.plot.bar(rot=0, stacked=True).legend(loc="lower left");

# ### Количественный и категориальный признаки

# #### rcParams

# и посмотрим, какой размер графиков (ключ figure.figsize) установлен по умолчанию
matplotlib.rcParams["figure.figsize"]

# обновим этот параметр через прямое внесение изменений в значение словаря
matplotlib.rcParams["figure.figsize"] = (7, 5)
matplotlib.rcParams["figure.figsize"]

# +
# изменим размер обновив словарь в параметре rc функции sns.set()
sns.set(rc={"figure.figsize": (8, 5)})

# посмотрим на результат
matplotlib.rcParams["figure.figsize"]

# +
# весь словарь с параметрами доступен по атрибуту rcParams
# matplotlib.rcParams
# -

# #### Гистограммы

# выведем две гистограммы на одном графике в библиотеке Matplotlib
# отфильтруем данные по погибшим и выжившим и построим гистограммы по столбцу Age
plt.hist(x=titanic[titanic["Survived"] == 0]["Age"])
plt.hist(x=titanic[titanic["Survived"] == 1]["Age"]);

# сделаем то же самое в библиотеке Seaborn
# в x мы поместим количественный признак, в hue - категориальный
sns.histplot(x="Age", hue="Sex", data=titanic, bins=10);

# в Plotly количественный признак помещается в x, категориальный - в color
px.histogram(titanic, x="Age", color="Sex", nbins=8, text_auto=True)

# разное количество элементов в выборках

# сравним количество мужчин и женщин на борту
titanic.Sex.value_counts()

# создадим две гистограммы с параметров density = True
# параметр alpha отвечает за прозрачность каждой из гистограмм
plt.hist(x=titanic[titanic["Sex"] == "male"]["Age"], density=True, alpha=0.5)
plt.hist(x=titanic[titanic["Sex"] == "female"]["Age"], density=True, alpha=0.5);

# #### Графики плотности

# построим графики плотности распределений суммы чека в обеденное и вечернее время
sns.displot(tips, x="total_bill", hue="time", kind="kde");

# зададим границы диапазона от 0 до 70 долларов через clip = (0, 70)
# дополнительно заполним цветом пространство под кривой с помощью fill = True
sns.displot(tips, x="total_bill", hue="time", kind="kde", clip=(0, 70), fill=True);

# #### boxplots

# посмотрим, как различается сумма чека по дням недели
sns.boxplot(x="day", y="total_bill", data=tips);

# а также в зависимости от того, обед это или ужин
px.box(tips, x="time", y="total_bill", points="all")

# #### Гистограммы и boxplots

# +
# %%capture --no-display

px.histogram(
    tips,
    x="total_bill",  # количественный признак
    color="sex",  # категориальный признак
    marginal="box",
)  # дополнительный график: boxplot
# -

# #### stripplot, violinplot

# по сути, stripplot - это точечная диаграмма (scatterplot),
# в которой одна из переменных категориальная
sns.stripplot(x="day", y="total_bill", data=tips);

# с помощью sns.catplot() мы можем вывести
# распределение количественной переменной (total_bill)
# в разрезе трех качественных: статуса курильщика, пола и времени приема пищи
sns.catplot(x="sex", y="total_bill", hue="smoker", col="time", data=tips, kind="strip");

# построим violinplot для визуализации распределения суммы чека по дням недели
sns.violinplot(x="day", y="total_bill", data=tips);

# ### Преобразование данных

# #### Логарифмическая шкала

# соберем данные о продажах
products = ["Phone", "TV", "Laptop", "Desktop", "Tablet"]
sales = [800, 4, 550, 500, 3]

# отразим продажи с помощью столбчатой диаграммы
sns.barplot(x=products, y=sales)
plt.title("Продажи в январе 2020 года");

# теперь выведем эти же данные, но по логарифмической шкале
sns.barplot(x=products, y=sales)
plt.title("Продажи в январе 2020 года (log)")
plt.yscale("log");

# #### Границы по оси y

# +
# код для получения этих значений вы найдете в блокноте
# с анализом текучести кадров
eval_left = [0.715473, 0.718113]

# построим столбчатую диаграмму,
# для оси x - выведем строковые категории,
# для y - доли покинувших компанию сотрудников
sns.barplot(x=["0", "1"], y=eval_left)
plt.title("Last evaluation vs. left");

# +
sns.barplot(x=["0", "1"], y=eval_left)
plt.title("Last evaluation vs. left")

# для ограничения значений по оси y можно использовать функцию plt.ylim()
plt.ylim(0.7, 0.73);
# -

# ## Выявление взаимосвязи

# ### Линейный график

# +
# создадим последовательность от -2пи до 2пи
# с интервалом 0,1
a_var = np.arange(-2 * np.pi, 2 * np.pi, 0.1)

# сделаем эту последовательность значениями по оси x,
# а по оси y выведем функцию косинуса
plt.plot(a_var, np.cos(a_var))
plt.title("cos(a_var)");
# -

# ### Точечная диаграмма

# построим точечную диаграмму в библиотеке Matplotlib
plt.scatter(tips.total_bill, tips.tip)
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.title("total_bill vs. tip");

# +
matplotlib_axes_logger.setLevel("ERROR")

# воспользуемся методом .plot.scatter()
tips.plot.scatter("total_bill", "tip")
plt.title("total_bill vs. tip");
# -

# категориальный признак добавляется через параметр hue
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("total_bill vs. tip by time");

# ### pairplot

# построим pairplot в библиотеке Pandas
# в качестве данных возьмем столбцы total_bill и tip датасета tips
pd.plotting.scatter_matrix(tips[["total_bill", "tip"]]);

# построим pairplot в библиотеке Seaborn
# параметр height функции pairplot() задает высоту каждого графика в дюймах
sns.pairplot(titanic[["Age", "Fare"]].sample(frac=0.2, random_state=42), height=4);

# метод .sample() с параметром frac = 0.2 позволяет взять случайные 20% наблюдений
# параметр random_state обеспечивает воспроизводимость результата
titanic[["Age", "Fare"]].sample(frac=0.2, random_state=42)

# при добавлении параметра hue (категориальной переменной) гистограмма
# по умолчанию превращается в график плотности
# обратите внимание, столбец Survived мы добавили
# и в параметр hue, и в датафрейм с данными
sns.pairplot(
    titanic[["Age", "Fare", "Survived"]].sample(frac=0.2, random_state=42),
    hue="Survived",
    height=4,
);

# +
# создадим объект класса PairGrid, в качестве данных передадим ему
# как количественные, так и категориальные переменные
b_var = sns.PairGrid(
    tips[["total_bill", "tip", "time", "smoker"]],
    # передадим в hue категориальный признак, который мы будем различать цветом
    hue="time",
    # зададим размер каждого графика
    height=5,
)

# метод .map_diag() с параметром sns.histplot выдаст гистограммы на диагонали
b_var.map_diag(sns.histplot)

# в левом нижнем углу мы выведем точечные диаграммы и зададим
# дополнительный категориальный признак smoker с помощью размера точек графика
b_var.map_lower(sns.scatterplot, size=tips["smoker"])

# в правом верхнем углу будет график плотности сразу двух количественных признаков
b_var.map_upper(sns.kdeplot)

# добавим легенду, adjust_subtitles = True делает текст легенды более аккуратным
b_var.add_legend(title="", adjust_subtitles=True);
# -

# ### jointplot

# построим график плотности совместного распределения
sns.jointplot(
    data=tips,  # передадим данные
    x="total_bill",  # пропишем количественные признаки,
    y="tip",
    hue="time",  # категориальный признак,
    kind="kde",  # тип графика
    height=8,
);  # и его размер

sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    # построим точечную диаграмму
    kind="scatter",
    # дополнительно укажем размер точек
    s=100,
    # и их прозрачность
    alpha=0.7,
    height=8,
);

# для построения линии регрессии на данных
# используем параметр kind = 'reg'
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", height=8);

# ### heatmap

# выведем корреляционную матрицу между total_bill и tip
tips[["total_bill", "tip"]].corr()

# поместим корреляционную матрицу в функцию sns.heatmap()
sns.heatmap(
    tips[["total_bill", "tip"]].corr(),
    # дополнительно пропишем цветовую гамму
    cmap="coolwarm",
    # и зададим диапазон от -1 до 1
    vmin=-1,
    vmax=1,
);

# ## Sweetviz

# !pip install sweetviz

# +
train_csv_url = os.environ.get("TRAIN_CSV_URL", "")
test_csv_url = os.environ.get("TEST_CSV_URL", "")
response_train = requests.get(train_csv_url)
response_test = requests.get(test_csv_url)

# импортируем обучающую и тестовую выборки
train = pd.read_csv(io.BytesIO(response_train.content))
test = pd.read_csv(io.BytesIO(response_test.content))
# -

# передадим оба датасета в функцию sv.comparison()
comparison = sv.compare(train, test)

# посмотрим на тип созданного объекта
type(comparison)

# применим метод .show_notebook()
comparison.show_notebook()

# ## График в Matplotlib

# ### Стиль графика

# создадим последовательность для оси x
c_var = np.linspace(0, 10, 100)

# снова зададим размеры графиков и одновременно установим стиль Seaborn
sns.set(rc={"figure.figsize": (8, 5)})

# #### Цвет графика

# создадим несколько графиков функции косинуса со сдвигом
# и зададим цвет каждого графика одним из доступных в Matplotlib способов
plt.plot(c_var, np.cos(c_var - 0), color="blue")  # по названию
plt.plot(c_var, np.cos(c_var - 1), color="g")  # по короткому названию (rgbcmyk)
plt.plot(c_var, np.cos(c_var - 2), color="0.75")  # оттенки серого от 0 до 1
plt.plot(c_var, np.cos(c_var - 3), color="#FFDD44")  # HEX код (RRGGBB от 00 до FF)
plt.plot(
    c_var, np.cos(c_var - 4), color=(1.0, 0.2, 0.3)
)  # RGB кортеж, значения от 0 до 1
plt.plot(c_var, np.cos(c_var - 5), color="chartreuse");  # CSS название цветов

# #### Тип линии графика

# посмотрим на возможный тип линии графика
plt.plot(c_var, c_var + 0, linestyle="solid", linewidth=2)
plt.plot(c_var, c_var + 1, linestyle="dashed", linewidth=2)
plt.plot(c_var, c_var + 2, linestyle="dashdot", linewidth=2)
plt.plot(c_var, c_var + 3, linestyle="dotted", linewidth=2);

# создадим различные линии с помощью строки форматирования
plt.plot(c_var, c_var + 0, "-b", linewidth=2)  # сплошная синяя линия (по умолчанию)
plt.plot(
    c_var, c_var + 1, "--c", linewidth=2
)  # штриховая линия цвета морской волны (cyan)
plt.plot(c_var, c_var + 2, "-.k", linewidth=2)  # черная (key) штрихпунктирная линия
plt.plot(c_var, c_var + 3, ":r", linewidth=2);  # красная линия из точек

# #### Стиль точечной диаграммы

# зададим точку отсчета
np.random.seed(42)
# и последовательность из 10-ти случайных целых чисел от 0 до 10
d_var = np.random.randint(10, size=10)

# выведем первые 10 наблюдений в виде синих (b) кругов (o)
plt.scatter(c_var[:10], d_var, c="b", marker="o")
# выведем вторые 10 наблюдений в виде красных (r) треугольников (^)
plt.scatter(c_var[10:20], d_var, c="r", marker="^")
# выведем третьи 10 наблюдений в виде серых (0.50) квадратов (s)
# дополнительно укажем размер квадратов s = 100
plt.scatter(c_var[20:30], d_var, c="0.50", marker="s", s=100);

# #### Стиль графика в целом

# посмотрим на доступные стили
plt.style.available

# +
# применим стиль bmh
plt.style.use("bmh")

# и создадим точечную диаграмму с квадратными красными маркерами размера 100
plt.scatter(c_var[20:30], d_var, s=100, c="r", marker="s");

# +
# вернем блокнот к "заводским" настройкам (стиль default)
# такой стиль тоже есть, хотя он не указан в перечне plt.style.available
plt.style.use("default")

# дополнительно пропишем размер последующих графиков
matplotlib.rcParams["figure.figsize"] = (5, 4)
matplotlib.rcParams["figure.figsize"]
# -

# дополним белый прямоугольник сеткой и снова выведем график
plt.grid()
plt.scatter(c_var[20:30], d_var, s=100, c="r", marker="s");

# ### Пределы шкалы и деления осей графика

# #### Пределы шкалы

# Способ 1. Функции `plt.xlim()` и `plt.ylim()`

# +
# выведем график функции синуса
plt.plot(c_var, np.sin(c_var))

# пропишем пределы шкалы по обеим осям
plt.xlim(-2, 12)
plt.ylim(-1.5, 1.5);
# -

# Способ 2. Функция `plt.axis()`

# +
# выведем график функции синуса
plt.plot(c_var, np.sin(c_var))

# зададим пределы графика с помощью функции plt.axis()
# передадим параметры в следующей очередности: xmin, xmax, ymin, ymax
plt.axis([-2, 12, -1.5, 1.5]);
# -

# #### Деления

# +
# построим синусоиду и зададим график ее осей
plt.plot(c_var, np.sin(c_var))
plt.axis([-0.5, 11, -1.2, 1.2])

# создадим последовательность от 0 до 10 с помощью функции np.arange()
# и передадим ее в функцию plt.xticks()
plt.xticks(np.arange(11))

# в функцию plt.yticks() передадим созданный вручную список
plt.yticks([-1, 0, 1]);
# -

# ### Подписи, легенда и размеры графика

# +
# зададим размеры отдельного графика (лучше указывать в начале кода)
plt.figure(figsize=(8, 5))

# добавим графики синуса и косинуса с подписями к кривым
plt.plot(c_var, np.sin(c_var), label="sin(c_var)")
plt.plot(c_var, np.cos(c_var), label="cos(c_var)")

# выведем легенду (подписи к кривым) с указанием места на графике и размера шрифта
plt.legend(loc="lower left", prop={"size": 14})

# добавим пределы шкал по обеим осям,
plt.axis([-0.5, 10.5, -1.2, 1.2])

# а также деления осей графика
plt.xticks(np.arange(11))
plt.yticks([-1, 0, 1])

# добавим заголовок и подписи к осям с указанием размера шрифта
plt.title("Функции y = sin(c_var) и y = cos(c_var)", fontsize=18)
plt.xlabel("c_var", fontsize=16)
plt.ylabel("d_var", fontsize=16)

# добавим сетку
plt.grid()

# выведем результат
plt.show()
# -

# ### `plt.figure()` и `plt.axes()`

sns.set_style("whitegrid")

# +
# создадим объект класса plt.figure()
fig = plt.figure()

# создадим объект класса plt.axes()
ax = plt.axes()

# +
# создадим объект класса plt.figure()
fig = plt.figure()

# создадим объект класса plt.axes()
ax = plt.axes()

# добавим синусоиду к объекту ax с помощью метода .plot()
ax.plot(c_var, np.sin(c_var));

# +
fig = plt.figure()
ax = plt.axes()
ax.plot(c_var, np.sin(c_var))

# используем методы класса plt.axes()
ax.set_title("y = sin(c_var)")
ax.set_xlabel("c_var")
ax.set_ylabel("y");
# -

# ### Построение подграфиков

# #### Создание вручную

# +
# создадим объект fig,
fig = plt.figure()

# стандартный подграфик
ax1 = plt.axes()

# и подграфик по следующим координатам и размерам
ax2 = plt.axes([0.5, 0.5, 0.3, 0.3])

# дополнительно покажем, как можно убрать деления на "вложенном" подграфике
ax2.set(xticks=[], yticks=[]);

# +
# создадим объект класса plt.figure()
fig = plt.figure()

# зададим координаты угла [0.1, 0.6] и размеры [0.8, 0.4] верхнего подграфика,
# дополнительно зададим пределы шкалы по оси y и уберем шкалу по оси x
ax1 = fig.add_axes([0.1, 0.6, 0.8, 0.4], ylim=(-1.2, 1.2), xticklabels=[])

# добавим координаты угла [[0.1, 0.1] и размеры [0.8, 0.4] нижнего подграфика
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

# выведем на них синусоиду и косинусоиду соответственно
ax1.plot(np.sin(c_var))
ax2.plot(np.cos(c_var));
# -

# #### Метод `.add_subplot()`

# +
# создаем объект figure, задаем размер объекта,
fig = plt.figure(figsize=(8, 4))
# указываем общий заголовок через метод .suptitle()
fig.suptitle(
    "Заголовок объекта fig"
)  # можно использовать plt.suptitle('Заголовок объекта fig')

# внутри него создаем объект ax1, прописываем сетку из одной строки и двух столбцов
# и положение (индекс) ax1 в сетке
ax1 = fig.add_subplot(1, 2, 1)
# используем метод .set_title() для создания заголовка объекта ax1
ax1.set_title("Объект ax1")

# создаем и наполняем объект ax2
# запятые для значений сетки не обязательны, а заголовок можно передать параметром
ax2 = fig.add_subplot(122, title="Объект ax2")

plt.show()

# +
# создадим объект figure и зададим его размер
fig = plt.figure(figsize=(9, 6))
# укажем горизонтальное и вертикальное расстояние между графиками
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# в цикле от 1 до 6 (так как у нас будет шесть подграфиков)
for i in range(1, 7):
    # поочередно создадим каждый подграфик
    # первые два параметра задают сетку, в переменной i содержится индекс подграфика
    ax = fig.add_subplot(2, 3, i)
    # метод .text() позволяет написать текст в заданном месте подграфика
    ax.text(
        0.5,
        0.5,  # разместим текст в центре
        str((2, 3, i)),  # выведем параметры сетки и индекс графика
        fontsize=16,  # зададим размер текста
        ha="center",
    )  # сделаем выравнивание по центру
# -

# #### Функция `plt.subplots()`

# +
# создаем объекты fig и ax
# в параметрах указываем число строк и столбцов, а также размер фигуры
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))

# с помощью индекса объекта ax заполним левый верхний график
ax[0, 0].plot(c_var, np.sin(c_var))

# через метод .set() задаем параметры графика
ax[0, 0].set(
    title="y = sin(c_var)",
    xlabel="c_var",
    ylabel="y",
    xlim=(-0.5, 10.5),
    ylim=(-1.2, 1.2),
    xticks=(np.arange(0, 11, 2)),
    yticks=[-1, 0, 1],
)

plt.tight_layout();

# +
# передадим подграфики в соответствующие переменные
# в первых внутренних скобках - первая строка, во вторых - вторая
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(6, 6))

# поместим функцию np.sin(x) во второй столбец первой строки
ax2.plot(c_var, np.sin(c_var))
ax2.set(
    title="y = sin(c_var)",
    xlabel="c_var",
    ylabel="y",
    xlim=(-0.5, 10.5),
    ylim=(-1.2, 1.2),
    xticks=(np.arange(0, 11, 2)),
    yticks=[-1, 0, 1],
)

plt.tight_layout();

# +
# возьмем данные о продажах в четырех магазинах
sales_2: pd.DataFrame = pd.DataFrame(
    {
        "year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009],
        "store 1": [35, 43, 76, 31, 46, 33, 26, 22, 23, 35],
        "store 2": [31, 40, 66, 25, 46, 34, 23, 22, 27, 35],
        "store 3": [33, 41, 66, 35, 34, 37, 27, 28, 22, 38],
        "store 4": [35, 45, 61, 27, 42, 38, 25, 29, 24, 31],
    }
)

# сделаем столбец year индексом
sales_2.set_index("year", inplace=True)

# посмотрим на данные
sales_2

# +
# определимся с количеством строк и столбцов
nrows, ncols = 2, 2
# создадим счетчик для столбцов
col = 0

# создадим объекты fig и ax (в ax уже будет четыре подграфика)
# дополнительно, помимо размера, зададим общую шкалу по обеим осям
fig, ax = plt.subplots(
    nrows=nrows, ncols=ncols, figsize=(6, 6), sharex=True, sharey=True
)

# в цикле пройдемся по строкам
for e_var in range(nrows):
    # затем во вложенном цикле - по столбцам
    for f_var in range(ncols):
        # для каждой комбинации i и j (координат подграфика) выведем
        # столбчатую диаграмму Seaborn
        # по оси x - годы, по оси y - соответстующий столбец (магазин)
        # в параметр ax мы передадим текущий подграфик с координатами
        sns.barplot(x=sales_2.index, y=sales_2.iloc[:, col], ax=ax[e_var, f_var])

        # дополнительно в методе .set() зададим заголовок подграфика,
        # уберем подпись к оси x и зададим единые для всех подграфиков пределы по оси y
        ax[e_var, f_var].set(title=sales_2.columns[col], xlabel="", ylim=(0, 80))
        # укажем, количество делений шкалы (по сути, список от 1 до 10)
        ax[e_var, f_var].set_xticks(list(range(1, len(sales_2.index) + 1)))
        # в качестве делений шкалы по оси x зададим годы и повернем их на 45 градусов
        ax[e_var, f_var].set_xticklabels(sales_2.index, rotation=45)

        # общая шкала по осям предполагает общие деления, но не общую подпись,
        # чтобы подпись оси y была только слева от первого столбца, выведем ее при j == 0
        # (индекс j как раз отвечает за столбцы)
        if f_var == 0:
            ax[e_var, f_var].set_ylabel("продажи, млн. рублей")
        # в противном случае выведем пустую подпись
        else:
            ax[e_var, f_var].set_ylabel("")

        # обновим счетчик столбцов
        col += 1

# выведем результат
plt.show()
# -

# #### Метод `.plot()` библиотеки Pandas

# применим метод .plot() ко всем столбцам датафрейма
sales_2.plot(
    subplots=True,  # укажем, что хотим создать подграфики
    layout=(2, 2),  # пропишем размерность сетки
    kind="bar",  # укажем тип графика
    figsize=(6, 6),  # зададим размер фигуры
    sharey=True,  # сделаем общую шкалу по оси y
    ylim=(0, 80),  # зададим пределы по оси y
    grid=False,  # уберем сетку
    legend=False,  # уберем легенду
    rot=45,
);  # повернем подписи к делениям по оси x на 45 градусов

# +
# зададим размер строк и столбцов
nrows, ncols = 2, 2

ax = sales_2.plot(
    subplots=True,  # укажем, что хотим создать подграфики
    layout=(nrows, ncols),  # пропишем размерность сетки
    kind="bar",  # укажем тип графика
    figsize=(6, 6),  # зададим размер фигуры
    sharey=True,  # сделаем общую шкалу по оси y
    ylim=(0, 80),  # зададим пределы по оси y
    grid=False,  # уберем сетку
    legend=False,  # уберем легенду
    rot=45,
)
# повернем подписи к делениям по оси x на 45 градусов

# пройдемся по индексам столбцов и строк
for g_var in range(nrows):
    for h_var in range(ncols):

        # удалим подписи к оси x
        ax[g_var, h_var].set_xlabel("")

        # сделаем подписи по оси y только к первому столбцу
        if h_var == 0:
            ax[g_var, h_var].set_ylabel("продажи, млн. рублей")
        else:
            ax[g_var, h_var].set_ylabel("")
# -

# продемонстрируем, как выглядят индексы подграфиков
# при использовании вложенных циклов
for i_var in range(nrows):
    for j_var in range(ncols):
        print(i_var, j_var)

# ## Ответы на вопросы

# **Вопрос**. Как посмотреть, какая версия библиотеки используется в Google Colab?

# версию можно посмотрет так
matplotlib.__version__

# обратимся к более подробной информации
# !pip show matplotlib

# посмотрим, упоминается ли слово matplotlib в списке библиотек
# и если да, выведем название библиотеки с этим словом и ее версию
# !pip list | grep matplotlib
