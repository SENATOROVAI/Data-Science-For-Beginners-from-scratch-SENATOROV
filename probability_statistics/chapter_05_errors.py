"""Errors."""

# # Ошибки в данных

import pandas as pd

# ## Подготовка данных

# +
# создадим датафрейм из словаря
financials = pd.DataFrame(
    {
        "month": [
            "01/01/2019",
            "01/02/2019",
            "01/03/2019",
            "01/03/2019",
            "01/04/2019",
            "01/05/2019",
            "01/06/2019",
            "01/07/2019",
            "01/08/2019",
            "01/09/2019",
            "01/10/2019",
            "01/11/2019",
            "01/12/2019",
            "01/12/2019",
        ],
        "profit": [
            "1.20$",
            "1.30$",
            "1.25$",
            "1.25$",
            "1.27$",
            "1.13$",
            "1.23$",
            "1.20$",
            "1.31$",
            "1.24$",
            "1.18$",
            "1.17$",
            "1.23$",
            "1.23$",
        ],
        "MoM": [
            0.03,
            -0.02,
            0.01,
            0.02,
            -0.01,
            -0.015,
            0.017,
            0.035,
            0.02,
            0.01,
            0.00,
            -0.01,
            2.00,
            2.00,
        ],
        "high": [
            "Dubai",
            "Paris",
            "singapour",
            "singapour",
            "moscow",
            "Paris",
            "Madrid",
            "moscow",
            "london",
            "london",
            "Moscow",
            "Rome",
            "madrid",
            "madrid",
        ],
    }
)

financials
# -

# вначале получим общее представление о данных
financials.info()

# ## Дубликаты

# ### Поиск дубликатов

# keep = 'first' (параметр по умолчанию)
# помечает как дубликат (True) ВТОРОЕ повторяющееся значение
financials.duplicated(keep="first")

# keep = 'last' соответственно считает дубликатом ПЕРВОЕ повторяющееся значение
print(financials.duplicated(keep="last"))

# результат метода .duplicated() можно использовать как фильтр
print(financials[financials.duplicated(keep="last")])

# если смотреть по месяцам, у нас два дубликата, а не один
# с помощью параметра subset мы ищем дубликаты по конкретным столбцам
financials.duplicated(subset=["month"])

# и если смотреть по месяцм, дубликатов не один, а два
financials.duplicated(subset=["month"]).sum()

# создадим новый фильтр и выведем дубликаты по месяцам
print(financials[financials.duplicated(subset=["month"], keep="last")])

# аналогично мы можем посмотреть на неповторяющиеся значения
(~financials.duplicated(subset=["month"])).sum()

# этот логический массив можно также использовать как фильтр
print(financials[~financials.duplicated(subset=["month"], keep="last")])

# ### Удаление дубликатов

# метод .drop_duplicates() удаляет дубликаты и
# по сути принимает те же параметры, что и .duplicated()
financials.drop_duplicates(
    keep="last", subset=["month"], ignore_index=True, inplace=True
)
financials

# ## Неверные значения

# Доли процента и проценты

# рассчитаем среднемесячное изменение прибыли
financials.MoM.mean()

# заменим 2% на 0.02
financials.iloc[11, 2] = 0.02

# вновь рассчитаем средний показатель
financials.MoM.mean()

# ## Форматирование значений

# Тип str вместо float

# попробуем сложить данные о прибыли
financials.profit.sum()

# +
# вначале удалим знак доллара с помощью метода .strip()
financials["profit"] = financials["profit"].str.strip("$")

# затем воспользуемся знакомым нам методом .astype()
financials["profit"] = financials["profit"].astype("float")

# +
# отступление про ключевое слово assert
# напишем простейшую функцию деления одного числа на другое


def division(a_var: float, b_var: float) -> float:
    """Return division of 2 numbers."""
    # если делитель равен нулю, Питон выдаст ошибку (текст ошибки
    # указывать не обязательно)
    assert b_var != 0, "На ноль делить нельзя"
    return round(a_var / b_var, 2)


# +
# попробуем разделить 5 на 0
# division(5, 0)
# -

# проверим, получилось ли изменить тип данных
assert financials.profit.dtype == float

# теперь снова рассчитаем прибыль за год
financials.profit.sum()

# Названия городов с заглавной буквы

# пусть названия всех городов начинаются с заглавной буквы
# для этого подойдет метод .title()
financials["high"] = financials["high"].str.title()
financials

# ## Дата и время

# преобразуем столбец month в тип datetime, вручную указав
# исходный формат даты
financials["date1"] = pd.to_datetime(financials["month"], format="%d/%m/%Y")
financials

# теперь давайте попросим Питон самостоятельно определить формат даты
# для этого используем pd.to_datetime() без дополнительных параметров
financials["date2"] = pd.to_datetime(financials["month"])
financials

# исправить неточность с месяцем можно с помощью параметра dayfirst = True
financials["date3"] = pd.to_datetime(financials["month"], dayfirst=True)
financials

# убедимся, что столбцы с датами имеют тип данных datetime
financials.dtypes

# удалим ненужные столбцы
# кроме того, всегда удобно, если дата представляет собой индекс
financials.set_index(
    "date3", drop=True, inplace=True
)  # drop = True удаляет столбец date3
financials.drop(labels=["month", "date1", "date2"], axis=1, inplace=True)
financials.index.rename("month", inplace=True)
financials

# +
# создадим последовательность из 12 месяцев,
# передав начальный период (start), общее количество периодов (periods)
# и день начала каждого периода (MS, т.е. month start)
date_index = pd.date_range(start="1/1/2020", periods=12, freq="MS")

# сделаем эту последовательность индексом датафрейма
financials.index = date_index
financials
# -

# напоминаю, что для datetime конечная дата входит в срез
financials["2020-01":"2020-06"]  # type: ignore[misc]

# изменим формат индекса для создания визуализации
# будем выводить только месяцы (%B), так как все показатели у нас за 2020 год
financials.index = financials.index.strftime("%B")
financials

# построим графики для размера прибыли и изменения выручки за месяц
financials[["profit", "MoM"]].plot(
    subplots=True,  # обозначим, что хотим несколько подграфиков
    layout=(1, 2),  # зададим сетку
    kind="bar",  # укажем тип диаграммы
    rot=65,  # повернем деления шкалы оси x
    grid=True,  # добавим сетку
    figsize=(16, 6),  # укажем размер figure
    legend=False,  # уберем легенду
    title=["Profit 2020", "MoM Revenue Change 2020"],
);  # добавим заголовки
