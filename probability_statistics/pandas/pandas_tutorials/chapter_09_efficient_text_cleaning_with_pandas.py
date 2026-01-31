"""Efficient text cleaning with pandas."""

# # Эффективная очистка текста с помощью pandas

# ## Вступление
#
# Очистка данных занимает значительную часть процесса анализа данных. При использовании *pandas* существует несколько методов очистки текстовых полей для подготовки к дальнейшему анализу. По мере того, как наборы данных увеличиваются, важно использовать эффективные методы.
#
# В этой статье будут показаны примеры очистки текстовых полей в большом файле и даны советы по эффективной очистке неструктурированных текстовых полей с помощью *Python* и *pandas*.
#
# > Оригинал статьи Криса по [ссылке](https://pbpython.com/text-cleaning.html)

# ## Проблема
#
# Предположим, что у вас есть новый крафтовый виски, который вы хотели бы продать. Ваша территория включает Айову, и там есть [открытый набор данных](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy), который показывает продажи спиртных напитков в штате. Это кажется отличной возможностью, чтобы посмотреть, у кого самые большие счета в штате. Вооружившись этими данными, можно спланировать процесс продаж в магазины.
#
# В восторге от этой возможности, вы загружаете данные и понимаете, что они довольно большие. В этой статье я буду использовать данные, включающие продажи за `2019 год`. 
#
# Выборочный набор данных представляет собой CSV-файл размером `565 МБ` с `24` столбцами и `2,3 млн` строк, а весь датасет занимает `5 Гб` (`25 млн` строк). Это ни в коем случае не большие данные, но они достаточно большие для обработки в *Excel* и некоторых методов *pandas*.
#
# Давайте начнем с импорта модулей и чтения данных. 
#
# Я также воспользуюсь пакетом [`sidetable`](https://dfedorov.spb.ru/pandas/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D1%85%20%D1%81%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D1%85%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%20%D0%B2%20pandas%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20sidetable.html) для обобщения данных. Он не требуется для очистки, но может быть полезен для подобных сценариев исследования данных.

# %pip install sidetable

# ## Данные
#
# Загрузим данные:

# +
from typing import Iterable, Optional, Tuple, TypeVar

import numpy as np
import pandas as pd
# import sidetable
# -

# !curl -L -o 2019_Iowa_Liquor_Sales.csv "https://www.dropbox.com/s/9e88whmc03nkouz/2019_Iowa_Liquor_Sales.csv?dl=1"

df = pd.read_csv("2019_Iowa_Liquor_Sales.csv")

# Посмотрим на них:

df.head()

# Первое, что можно сделать, это посмотреть, сколько закупает каждый магазин, и отсортировать их по убыванию. У нас ограниченные ресурсы, поэтому мы должны сосредоточиться на тех местах, где мы получим максимальную отдачу от вложенных средств. Нам будет проще позвонить паре крупных корпоративных клиентов, чем множеству семейных магазинов.
#
# Модуль [`sidetable`](https://dfedorov.spb.ru/pandas/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D1%85%20%D1%81%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D1%85%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%20%D0%B2%20pandas%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20sidetable.html) позволяет обобщать данные в удобочитаемом формате и является альтернативой методу `groupby` с дополнительными преобразованиями.

df.stb.freq(["Store Name"], value="Sale (Dollars)", style=True, cum_cols=False)

# Похоже, во всех трех случаях  
#
# - `Hy-Vee #3 / BDI / Des Moines`
# - `Hy-Vee Wine and Spirits / Iowa City`
# - `Hy-Vee Food Store / Urbandale`
#
# речь идет об одном и том же магазине. Очевидно, что названия магазинов в большинстве случаев уникальны для каждого местоположения. 
#
# В идеале мы хотели бы сгруппировать вместе все продажи `Hy-Vee`, `Costco` и т.д.
#
# Нам нужно очистить данные!

# ### Попытка очистки №1
#
# Первый подход, который мы рассмотрим, - это использование `.loc` плюс логический фильтр с аксессором `str` для поиска соответствующей строки в столбце `Store Name`.

df.loc[df["Store Name"].str.contains("Hy-Vee", case=False), "Store_Group_1"] = "Hy-Vee"

# Этот код будет искать строку `Hy-Vee` без учета регистра и сохранять значение `Hy-Vee` в новом столбце с именем `Store_Group_1`. Данный код эффективно преобразует такие названия, как `Hy-Vee # 3 / BDI / Des Moines` или `Hy-Vee Food Store / Urbandale`, в обычное `Hy-Vee`.
#
# Вот, что `%timeit` говорит об эффективности:

# %timeit df.loc[df['Store Name'].str.contains('Hy-Vee', case=False), 'Store_Group_1'] = 'Hy-Vee'

# Можем использовать параметр `regex=False` для ускорения вычислений:

# %timeit df.loc[df['Store Name'].str.contains('Hy-Vee', case=False, regex=False), 'Store_Group_1'] = 'Hy-Vee'

# Вот значения в новом столбце:

df["Store_Group_1"].value_counts(dropna=False)

# Мы очистили `Hy-Vee`, но теперь появилось множество других значений, с которыми нам нужно разобраться.
#
# Подход `.loc` включает много кода и может быть медленным. Поищем альтернативы, которые быстрее выполнять и легче поддерживать.

# ### Попытка очистки №2
#
# Другой очень эффективный и гибкий подход - использовать `np.select` для запуска нескольких совпадений и применения указанного значения при совпадении.
#
# Есть несколько хороших ресурсов, которые я использовал, чтобы узнать про `np.select`. Эта [статья](https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/) от *Dataquest* - хороший обзор, а также [презентация](https://docs.google.com/presentation/d/1X7CheRfv0n4_I21z4bivvsHt6IDxkuaiAuCclSzia1E/edit#slide=id.g635adc05c1_1_1840) Натана Чивера (*Nathan Cheever*). Рекомендую и то, и другое.
#
# Самое простое объяснение того, что делает `np.select`, состоит в том, что он оценивает список условий и применяет соответствующий список значений, если условие истинно.
#
# В нашем случае условиями будут разные строки для поиски (*string lookups*), а в качестве значений нормализованные строки, которые хотим использовать.
#
# После просмотра данных, вот список условий и значений в списке `store_patterns`. Каждый кортеж в этом списке представляет собой поиск по `str.contains()` и соответствующее текстовое значение, которое мы хотим использовать для группировки похожих счетов.

store_patterns = [
    (df["Store Name"].str.contains("Hy-Vee", case=False, regex=False), "Hy-Vee"),
    (
        df["Store Name"].str.contains("Central City", case=False, regex=False),
        "Central City",
    ),
    (
        df["Store Name"].str.contains("Smokin' Joe's", case=False, regex=False),
        "Smokin' Joe's",
    ),
    (df["Store Name"].str.contains("Walmart|Wal-Mart", case=False), "Wal-Mart"),
    (
        df["Store Name"].str.contains("Fareway Stores", case=False, regex=False),
        "Fareway Stores",
    ),
    (
        df["Store Name"].str.contains("Casey's", case=False, regex=False),
        "Casey's General Store",
    ),
    (
        df["Store Name"].str.contains("Sam's Club", case=False, regex=False),
        "Sam's Club",
    ),
    (df["Store Name"].str.contains("Kum & Go", regex=False, case=False), "Kum & Go"),
    (df["Store Name"].str.contains("CVS", regex=False, case=False), "CVS Pharmacy"),
    (df["Store Name"].str.contains("Walgreens", regex=False, case=False), "Walgreens"),
    (df["Store Name"].str.contains("Yesway", regex=False, case=False), "Yesway Store"),
    (df["Store Name"].str.contains("Target Store", regex=False, case=False), "Target"),
    (df["Store Name"].str.contains("Quik Trip", regex=False, case=False), "Quik Trip"),
    (df["Store Name"].str.contains("Circle K", regex=False, case=False), "Circle K"),
    (
        df["Store Name"].str.contains("Hometown Foods", regex=False, case=False),
        "Hometown Foods",
    ),
    (
        df["Store Name"].str.contains("Bucky's", case=False, regex=False),
        "Bucky's Express",
    ),
    (df["Store Name"].str.contains("Kwik", case=False, regex=False), "Kwik Shop"),
]

# Одна из серьезных проблем при работе с `np.select` заключается в том, что легко получить несоответствие условий и значений. Я решил объединить в кортеж, чтобы упростить отслеживание совпадений данных.
#
# Из-за такой структуры приходится разбивать список кортежей на два отдельных списка. 
#
# Используя `zip`, можем взять `store_patterns` и разбить его на `store_criteria` и `store_values`:

store_criteria, store_values = zip(*store_patterns)
df["Store_Group_1"] = np.select(store_criteria, store_values, "other")

# Этот код будет заполнять каждое совпадение текстовым значением. Если совпадений нет, то присвоим ему значение `other`.
#
# Вот как это выглядит сейчас:

df.stb.freq(["Store_Group_1"], value="Sale (Dollars)", style=True, cum_cols=False)

# Так лучше, но `32,28%` выручки по-прежнему приходится на `other` счета.
#
# Далее, если есть счет, который не соответствует шаблону, то используем `Store Name` вместо того, чтобы объединять все в `other`. 
#
# Вот как мы это сделаем:`

df["Store_Group_1"] = np.select(store_criteria, store_values, None)
df["Store_Group_1"] = df["Store_Group_1"].combine_first(df["Store Name"])

# Здесь используется функция `comb_first`, чтобы заполнить все `None` значения `Store Name`. Это удобный прием, о котором следует помнить при очистке данных.
#
# Проверим наши данные:

df.stb.freq(["Store_Group_1"], value="Sale (Dollars)", style=True, cum_cols=False)

# Выглядит лучше, т.к. можем продолжать уточнять группировки по мере необходимости. Например, можно построить поиск по строке для `Costco`.
#
# Производительность не так уж и плоха для большого набора данных:
#
#     13.2 s ± 328 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# Гибкость данного подхода в том, что можно использовать `np.select` для числового анализа и текстовых примеров.
#
# Единственная проблема, связанная с этим подходом, заключается в большом количестве кода. 
#
# Есть ли другой подход, который мог бы иметь аналогичную производительность, но был бы немного чище?

# ### Попытка очистки №3
#
# Следующее решение основано на [этом](https://www.metasnake.com/blog/pydata-assign.html) примере кода от Мэтта Харрисона (*Matt Harrison*). Он разработал функцию `generalize`, которая выполняет сопоставление и очистку за нас! 
#
# Я внес некоторые изменения, чтобы привести ее в соответствие с этим примером, но хочу отдать должное Мэтту. Я бы никогда не подумал об этом решении, если бы оно не выполняло `99%` всей работы!

# +
T = TypeVar("T", bound=str)


def generalize(
    ser: pd.Series[T],
    match_name: Iterable[Tuple[str, str]],
    default: Optional[str] = None,
    regex: bool = False,
    case: bool = False,
) -> pd.Series[T]:
    """
    Поиск в серии текстовых совпадений.

    ser : pandas.Series — серия для поиска
    match_name : пары (шаблон, замена)
    default : значение по умолчанию
    regex, case : флаги поиска
    """
    seen = None
    for match, name in match_name:
        mask = ser.str.contains(match, case=case, regex=regex)
        if seen is None:
            seen = mask
        else:
            seen |= mask
        ser = ser.where(~mask, name)
    if default:
        ser = ser.where(seen, default)  # type: ignore[arg-type]
    else:
        ser = ser.where(seen, ser.values)  # type: ignore[arg-type]
    return ser


# -

# Эта функция может быть вызвана для серии *pandas* и ожидает список кортежей. 
#
# Первый элемент следующего кортежа - это значение для поиска, а второй - значение, которое нужно заполнить для совпадающего значения.
#
# Вот список эквивалентных шаблонов:

store_patterns_2 = [
    ("Hy-Vee", "Hy-Vee"),
    ("Smokin' Joe's", "Smokin' Joe's"),
    ("Central City", "Central City"),
    ("Costco Wholesale", "Costco Wholesale"),
    ("Walmart", "Walmart"),
    ("Wal-Mart", "Walmart"),
    ("Fareway Stores", "Fareway Stores"),
    ("Casey's", "Casey's General Store"),
    ("Sam's Club", "Sam's Club"),
    ("Kum & Go", "Kum & Go"),
    ("CVS", "CVS Pharmacy"),
    ("Walgreens", "Walgreens"),
    ("Yesway", "Yesway Store"),
    ("Target Store", "Target"),
    ("Quik Trip", "Quik Trip"),
    ("Circle K", "Circle K"),
    ("Hometown Foods", "Hometown Foods"),
    ("Bucky's", "Bucky's Express"),
    ("Kwik", "Kwik Shop"),
]

# Преимущество этого решения состоит в том, что поддерживать данный список намного проще, чем в предыдущем примере `store_patterns`.
#
# Другое изменение, которое я внес с помощью функции `generalize`, заключается в том, что исходное значение будет сохранено, если не указано значение по умолчанию. Теперь вместо использования `combine_first` функция `generalize` позаботится обо всем. 
#
# Наконец, я отключил сопоставление регулярных выражений по умолчанию для улучшения производительности.
#
# Теперь, когда все данные настроены, вызвать их очень просто:

df["Store_Group_2"] = generalize(df["Store Name"], store_patterns_2)

# Как насчет производительности?
#
#     15.5 s ± 409 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# Немного медленнее, но думаю, что это более элегантное решение и я бы использовал его в будущем.
#
# Обратной стороной этого подхода является то, что он предназначен для очистки строк. Решение `np.select` более полезно, поскольку его можно применять и к числовым значениям.
#
# ### А как насчет типов данных?
#
# В последних версиях *pandas* есть специальный тип `string`. Я попытался преобразовать `Store Name` в строковый тип *pandas*, чтобы увидеть, есть ли улучшение производительности. Никаких изменений не заметил. Однако не исключено, что в будущем скорость будет повышена, так что имейте это в виду.
#
# Тип `category` показал многообещающие результаты. 
#
# > Обратитесь к моей [предыдущей статье](https://dfedorov.spb.ru/pandas/%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%82%D0%B8%D0%BF%D0%B0%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8%20%D0%B2%20pandas.html) за подробностями о типе данных категории.
#
# Можем преобразовать данные в тип `category` с помощью `astype`:

df["Store Name"] = df["Store Name"].astype("category")

# Теперь повторно запустите пример `np.select` точно так же, как мы делали ранее:

df["Store_Group_3"] = np.select(store_criteria, store_values, None)
df["Store_Group_3"] = df["Store_Group_1"].combine_first(df["Store Name"])

#     786 ms ± 108 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# Мы перешли с `13` до менее `1 секунды`, сделав одно простое изменение. Удивительно!
#
# Причина, по которой это произошло, довольно проста. Когда *pandas* преобразует столбец в категориальный тип, функция `str.contains()` будет вызываться для каждого уникального текстового значения. Поскольку этот набор данных содержит много повторяющихся данных, мы получаем огромный прирост производительности.
#
# Посмотрим, работает ли это для нашей функции `generalize`:
#
#     df['Store_Group_4'] = generalize(df['Store Name'], store_patterns_2)
#
# К сожалению, получаем ошибку:
#
#     ValueError: Cannot setitem on a Categorical with a new category, set the categories first
#
# Эта ошибка подчеркивает некоторые проблемы, с которыми я сталкивался в прошлом при работе с категориальными (*Categorical*) данными. При *merging* и *joining* категориальных данных вы можете столкнуться с подобными типами проблем.
#
# Я попытался найти хороший способ изменить работу `generalize()`, но не смог. 
#
# Тем не менее есть способ воспроизвести категориальный подход (*Category approach*), построив [таблицу поиска](https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0) (*lookup table*).

# ### Таблица поиска
#
# Как мы узнали из категориального подхода, данный набор содержит много повторяющихся данных. 
#
# Мы можем построить таблицу поиска и запустить ресурсоемкую функцию только один раз для каждой строки.
#
# Чтобы проиллюстрировать, как это работает со строками, давайте преобразуем значение обратно в строковый тип вместо категории:

df["Store Name"] = df["Store Name"].astype("string")

df.head()

# Сначала мы создаем `DataFrame` поиска, который содержит все уникальные значения, и запускаем функцию `generalize`:

lookup_df = pd.DataFrame()
lookup_df["Store Name"] = df["Store Name"].unique()
lookup_df["Store_Group_5"] = generalize(lookup_df["Store Name"], store_patterns_2)

lookup_df.head()

# Можем объединить (*merge*) его обратно в окончательный `DataFrame`:

df = pd.merge(df, lookup_df, how="left")

#     1.38 s ± 15.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# Он работает медленнее, чем подход `np.select` для категориальных данных, но влияние на производительность может быть уравновешено более простой читабельностью для ведения списка поиска.
#
# Кроме того, промежуточный `lookup_df` может стать отличным выходом для аналитика, который поможет очистить больше данных. Эту экономию можно измерить часами работы!

# ## Резюме
#
# [Этот](https://counting.substack.com/p/data-cleaning-is-analysis-not-grunt) информационный бюллетень Рэнди Ау (*Randy Au*) - хорошее обсуждение важности очистки данных и отношения любви / ненависти, которое многие специалисты по данным чувствуют при выполнении данной задачи. Я согласен с предположением Рэнди о том, что очистка данных - это анализ.
#
# По моему опыту, вы можете многое узнать о своих базовых данных, взяв на себя действия по очистке, описанные в этой статье.
#
# Я подозреваю, что в ходе повседневного анализа вы найдете множество случаев, когда вам нужно очистить текст, аналогично тому, что я показал выше.
#
# Вот краткое изложение рассмотренных решений:



# |Решение   |Время исполнения   |Примечания   |
# |---|---|---|
# |`np.select`   | `13 с` |Может работать для нетекстового анализа   |
# |`generalize`  | `15 с` |Только текст   |
# |Категориальные данные и `np.select`   |`786 мс`  |Категориальные данные могут быть сложными при *merging* и *joining*   |
# |Таблица поиска и `generalize`   | `1.3 с` |Таблица поиска может поддерживаться кем-то другим|
