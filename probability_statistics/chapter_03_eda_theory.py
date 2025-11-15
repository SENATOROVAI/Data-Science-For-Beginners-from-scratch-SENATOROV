"""EDA theory."""

# # Классификация данных и задачи EDA

# +
# импортируем библиотеки
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# новая для нас библиотека Plotly Express обычно сокращается как px
import plotly.express as px

# построим график теоретической вероятности
from scipy.stats import poisson

# fmt: off
# -

# ## Категориальные и количественные данные

# ### Категориальные данные

# #### Номинальные данные

# +
# поместим данные о количестве автомобилей различных марок в датафрейм
cars = pd.DataFrame(
    {"model": ["Renault", "Hyundai", "KIA", "Toyota"], "stock": [12, 36, 28, 32]}
)

cars
# -

# выведем данные с помощью столбчатой диаграммы
# обратите внимание, что служебную информацию о графике можно убрать
# как с помощью plt.show(),
# так и с помощью точки с запятой ";"
plt.bar(cars.model, cars.stock);

# #### Порядковые данные

# +
# соберем данные об уровне удовлетворенности десяти человек
satisfaction = pd.DataFrame(
    {
        "sat_level": [
            "Good",
            "Medium",
            "Good",
            "Medium",
            "Bad",
            "Medium",
            "Good",
            "Medium",
            "Medium",
            "Bad",
        ]
    }
)

satisfaction

# +
# переведем данные в тип categorical
satisfaction.sat_level = pd.Categorical(
    satisfaction.sat_level, categories=["Bad", "Medium", "Good"], ordered=True
)

# построим столбчатую диаграмму типа countplot
# с количеством оценок в каждой из категорий
sns.countplot(x="sat_level", data=satisfaction);
# -

# ### Количественные данные

# #### Дискретные данные

# Распределение Пуассона

# +
# смоделируем количество поступающих в колл-центр звонков,
# передав матожидание (lam) и желаемое количество экспериментов (size)
res = np.random.poisson(lam=3, size=1000)

# посмотрим на первые 10 значений
res[:10]
# -

# получим количество звонков в минуту (unique) и соответствующую им частоту (counts)
unique, counts = np.unique(res, return_counts=True)
unique, counts

# выведем абсолютные значения распределения количества звонков в минуту
plt.figure(figsize=(10, 6))
plt.bar([str(x) for x in unique], counts, width=0.95)
plt.title("Абсолютное распределение количества звонков в минуту", fontsize=16)
plt.xlabel("количество звонков в минуту", fontsize=16)
plt.ylabel("частота", fontsize=16);

plt.figure(figsize=(10, 6))
# теперь посмотрим на относительное распределение количества звонков в минуту
# для этого просто разделим количество звонков в каждом из столбцов на общее число звонков
plt.bar([str(x) for x in unique], counts / len(res), width=0.95)
plt.title("Относительное распределение количества звонков в минуту", fontsize=16)
plt.xlabel("количество звонков в минуту", fontsize=16)
plt.ylabel("относительная частота", fontsize=16);

# рассчитаем вероятность получить более шести звонков в минуту
np.round(len(res[res > 6]) / len(res), 3)

# рассчитаем вероятность получить от двух до шести звонков в минуту включительно
np.round(len(res[res <= 6]) / len(res) - len(res[res < 2]) / len(res), 3)

# +
# создадим последовательность целых чисел от 0 до 14
x_var = np.arange(15)
# передадим их в функцию poisson.pmf()
# mu в данном случае это матожидание (lambda из формулы)
f_var = poisson.pmf(x_var, mu=3)

# построим график теоретического распределения, изменив для наглядности его цвет
plt.figure(figsize=(10, 6))
plt.bar([str(x_var) for x_var in x_var], f_var, width=0.95, color="green")
plt.title("Теоретическое распределение количества звонков в минуту", fontsize=16)
plt.xlabel("количество звонков в минуту", fontsize=16)
plt.ylabel("относительная частота", fontsize=16);
# -

# рассчитаем вероятность получения нуля звонков или одного звонка в час
poisson.cdf(1, 3).round(3)

# найдем площадь столбцов до шести звонков в минуту включительно
# и вычтем результат из единицы
np.round(1 - poisson.cdf(6, 3), 3)

# для выполнения второго задания вычтем площадь столбцов ноль и один
# из площади столбцов до шестого включительно
np.round(poisson.cdf(6, 3) - poisson.cdf(1, 3), 3)

# #### Непрерывные данные

#

#

#

# +
# создадим датафрейм с данными по Франции, Бельгии и Испании
csect = pd.DataFrame(
    {
        "countries": ["France", "Belgium", "Spain"],
        "healthcare": [4492, 5428, 3616],
        "education": [9210, 10869, 6498],
    }
)

# посмотрим на результат
csect

# +
# зададим размер фигуры для обоих графиков
plt.figure(figsize=(12, 5))

# используем функцию plt.subplot() для создания первого графика (index = 1)
# передаваемые параметры: nrows, ncols, index
plt.subplot(1, 2, 1)
# построим столбчатую диаграмму для здравоохранения
plt.bar(csect.countries, csect.healthcare)
plt.title("Здравоохранение", fontsize=14)
plt.xlabel("Страны", fontsize=12)
plt.ylabel("Доллары США на душу населения", fontsize=12)

# создадим второй график (index = 2)
# параметры можно передать одним числом
plt.subplot(122)
# построим столбчатую диаграмму для образования
plt.bar(csect.countries, csect.education, color="orange")
plt.title("Образование", fontsize=14)
plt.xlabel("Страны", fontsize=12)
plt.ylabel("Евро на одного учащегося", fontsize=12)

# отрегулируем пространство между графиками
plt.subplots_adjust(wspace=0.4)

# зададим общий график
plt.suptitle("Расходы на здравоохранение и образование в 2019 году ", fontsize=16)

# выведем результат
plt.show()
# -

#

# +
# создадим временной ряд расходов на здравоохранение во Франции с 2010 по 2019 годы
tseries = pd.DataFrame(
    {
        "year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        "healthcare": [4598, 4939, 4651, 4902, 4999, 4208, 4268, 4425, 4690, 4492],
    }
)

# превратим год в объект datetime
tseries.year = pd.to_datetime(tseries.year, format="%Y")
# и сделаем этот столбец индексом
tseries.set_index("year", drop=True, inplace=True)

# посмотрим на результат
tseries

# +
# выведем эти данные с помощью линейного графика
plt.figure(figsize=(12, 5))
# дополнительно укажем цвет, толщину линии и вид маркера
plt.plot(tseries, color="green", linewidth=2, marker="o")

# добавим подписи к осям и заголовок
plt.xlabel("Годы", fontsize=14)
plt.ylabel("Доллары США", fontsize=14)
plt.title(
    "Расходы на здравоохранение на душу населения во Франции с 2010 по 2019 год",
    fontsize=14,
)

# выведем результат
plt.show()
# -

# ### Панельные данные

# Создание датафрейма с панельными данными с помощью иерархического индекса

# вначале создадим датафрейм с данными расходов на душу населения
# на здравоохранение трех стран с 2015 по 2019 годы
# первые пять цифр относятся к Франции, вторые пять - к Бельгии,
# третьи пять - к Испании
pdata = pd.DataFrame(
    {
        "healthcare": [
            4208,
            4268,
            4425,
            4690,
            4492,
            4290,
            4323,
            4618,
            4913,
            4960,
            2349,
            2377,
            2523,
            2736,
            2542,
        ]
    }
)

# +
# создадим кортежи для иерархического индекса
rows = [
    ("France", "2015"),
    ("France", "2016"),
    ("France", "2017"),
    ("France", "2018"),
    ("France", "2019"),
    ("Belgium", "2015"),
    ("Belgium", "2016"),
    ("Belgium", "2017"),
    ("Belgium", "2018"),
    ("Belgium", "2019"),
    ("Spain", "2015"),
    ("Spain", "2016"),
    ("Spain", "2017"),
    ("Spain", "2018"),
    ("Spain", "2019"),
]

# передадим кортежи в функцию pd.MultiIndex.from_tuples(),
# указав названия уровней индекса
custom_multindex = pd.MultiIndex.from_tuples(rows, names=["country", "year"])

# сделаем custom_multindex индексом датафрейма с панельными данными
pdata.index = custom_multindex

# посмотрим на результат
pdata
# -

# Визуализация панельных данных

# +
# сделаем данные по странам (index level = 0) отдельными столбцами
pdata_unstacked = pdata.healthcare.unstack(level=0)

# метод .unstack() выстроит столбцы в алфавитном порядке
pdata_unstacked

# +
# зададим размер графика
plt.figure(figsize=(10, 5))

# построим три кривые
pdata_unstacked.Belgium.plot(linewidth=2, marker="o", label="Бельгия")
pdata_unstacked.France.plot(linewidth=2, marker="o", label="Франция")
pdata_unstacked.Spain.plot(linewidth=2, marker="o", label="Испания")

# дополним подписями к осям, заголовком и легендой
plt.xlabel("Годы", fontsize=14)
plt.ylabel("Доллары США", fontsize=14)
plt.title(
    (
        "Расходы на здравоохранение на душу населения "
        "в Бельгии, Франции и Испании "
        "с 2015 по 2019 годы"
    ),
    fontsize=14,
)
plt.legend(loc="center left", prop={"size": 14})

plt.show()

# +
pdata_unstacked.plot.bar(
    subplots=True,
    layout=(1, 3),
    rot=0,
    figsize=(13, 5),
    sharey=True,
    fontsize=11,
    width=0.8,
    xlabel="",
    ylabel="доллары США",
    legend=None,
    title=["Бельгия", "Франция", "Испания"],
)

# отрегулируем ширину между графиками
plt.subplots_adjust(wspace=0.1)

# добавим общий заголовок
plt.suptitle("Расходы на здравоохранение с 2015 по 2019 годы", fontsize=16);
# -

# ## Одномерный и многомерный анализ

# #### Многомерный временной ряд

# +
# создадим временной ряд расходов на здравоохранение во Франции на душу
# населения в долларах с 2010 по 2019 годы
# и приведем процент ВВП, потраченный на образование, за аналогичный период
tseries_mult = pd.DataFrame(
    {
        "year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        "healthcare": [4598, 4939, 4651, 4902, 4999, 4208, 4268, 4425, 4690, 4492],
        "education": [5.69, 5.52, 5.46, 5.50, 5.51, 5.46, 5.48, 5.45, 5.41, 6.62],
    }
)

# превратим год в объект datetime
tseries_mult.year = pd.to_datetime(tseries_mult.year, format="%Y")
# и сделаем этот столбец индексом
tseries_mult.set_index("year", drop=True, inplace=True)

# посмотрим на результат
tseries_mult
# -

# #### Многомерные панельные данные

# +
# вначале создадим датафрейм с данными расходов на здравоохранение и
# образование трех стран с 2015 по 2019 годы
pdata_mult = pd.DataFrame(
    {
        "healthcare, per capita": [
            4208,
            4268,
            4425,
            4690,
            4492,
            4290,
            4323,
            4618,
            4913,
            4960,
            2349,
            2377,
            2523,
            2736,
            2542,
        ],
        "education, % of GDP": [
            5.46,
            5.48,
            5.45,
            5.41,
            6.62,
            6.45,
            6.46,
            6.43,
            6.38,
            6.40,
            4.29,
            4.23,
            4.21,
            4.18,
            4.26,
        ],
    }
)

# создадим кортежи для иерархического индекса
rows = [
    ("France", "2015"),
    ("France", "2016"),
    ("France", "2017"),
    ("France", "2018"),
    ("France", "2019"),
    ("Belgium", "2015"),
    ("Belgium", "2016"),
    ("Belgium", "2017"),
    ("Belgium", "2018"),
    ("Belgium", "2019"),
    ("Spain", "2015"),
    ("Spain", "2016"),
    ("Spain", "2017"),
    ("Spain", "2018"),
    ("Spain", "2019"),
]

# передадим кортежи в функцию pd.MultiIndex.from_tuples(),
# указав названия уровней индекса
custom_multindex = pd.MultiIndex.from_tuples(rows, names=["country", "year"])

# сделаем custom_multindex индексом датафрейма с панельными данными
pdata_mult.index = custom_multindex

# посмотрим на результат
pdata_mult
# -

# ## Библиотеки

# ### Matplotlib

# #### Стиль MATLAB

# +
# зададим последовательность от -5 до 5 с шагом 0,1
y_var = np.arange(-5, 5, 0.1)

# построим график синусоиды
plt.plot(y_var, np.sin(y_var))

# зададим заголовок, подписи к осям и сетку
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid();
# -

# #### Подход ООП

# +
# создадим объект класса figure
fig = plt.figure()

# и посмотрим на его тип
print(type(fig))

# +
# применим метод .add_subplot() для создания подграфика (объекта ax)
# напомню, что первые два параметра задают количество строк и столбцов,
# третий параметр - это индекс (порядковый номер подграфика)
ax = fig.add_subplot(2, 1, 1)

# посмотрим на тип этого объекта
print(type(ax))
# -

fig.number

# +
# вначале создаем объект figure, указываем размер объекта
fig = plt.figure(figsize=(8, 6))
# и его заголовок с помощью метода .suptitle()
fig.suptitle("Figure object")
# можно и plt.suptitle('Figure object')

# внутри него создаем первый объекта класса axes
ax1 = fig.add_subplot(2, 2, 1)
# к этому объекту можно применять различные методы
ax1.set_title("Axes object 1")

# и второй (напомню, параметры можно передать без запятых)
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title("Axes object 2")

# выведем результат
plt.show()
# -

# ### Pandas

# "под капотом" для построения графиков
# библиотека Pandas использует объекты библиотеки matplotilb
# в этом несложно убедиться с помощью функции type()
type(tseries.plot())

# ### Seaborn

# +
# см. примеры выше
# -

# ### Plotly Express

# по оси x разместим страны, по оси y - признаки
# параметр barmode = 'group' указывает,
# что столбцы образования и здравоохранения нужно разместить рядом,
# а не внутри одного столбца (stacked)
px.bar(csect, x="countries", y=["healthcare", "education"], barmode="group")
