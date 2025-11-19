"""Yandex metrics."""

# # Яндекс-метрики

# Проведем анализ частоты запросов по версии [Яндекс.Метрики](https://yandex.ru/support/metrica/general/glossary.html).

# Для работы понадобится модуль [pymorphy2](https://pymorphy2.readthedocs.io/en/stable/).

# +
# pip install pymorphy2

# +
from itertools import chain

import matplotlib.pyplot as plt
import pandas as pd
import pymorphy2
import seaborn as sns

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stat/yandex-stat-q.csv"
# -

morph = pymorphy2.MorphAnalyzer()

# ### Задача: определите статистику встречаемости отдельных слов в поисковых фразах. Это позволит понять тематику данного сайта и настроить показ рекламы.
#
# За помощью обратитетесь к [инструкции](https://dfedorov.spb.ru/pandas/10.%20%D0%9A%D0%B0%D0%BA%20%D0%BC%D0%B0%D0%BD%D0%B8%D0%BF%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%BC%D0%B8%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8_.html) и возможностям модуля [pymorphy2](https://pymorphy2.readthedocs.io/en/stable/).

df = pd.read_csv(url)
df.head()

# ### Задача: определите статистику встречаемости отдельных слов в поисковых фразах. Это позволит понять тематику данного сайта и настроить показ рекламы.
#
# За помощью обратитетесь к [инструкции](https://dfedorov.spb.ru/pandas/10.%20%D0%9A%D0%B0%D0%BA%20%D0%BC%D0%B0%D0%BD%D0%B8%D0%BF%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%BC%D0%B8%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8_.html) и возможностям модуля [pymorphy2](https://pymorphy2.readthedocs.io/en/stable/).

df["Поисковая фраза"].str.lower()

list(enumerate(df["Поисковая фраза"].str.lower().iloc[:20]))

lst_phrases = df.loc[:, "Поисковая фраза"].str.lower().head(20).tolist()

# splited_phrases = list(map(lambda x: x.split(), lst_phrases))
# splited_phrases[:20]
splited_phrases = [x.split() for x in lst_phrases]

flat_list = list(chain.from_iterable(splited_phrases))
flat_list[:20]

morph.parse('итого')

# +
# morph.parse('итого')[0]

# +
# morph.parse('итого')[0].normal_form
# -

flat_list = [
    morph.parse(item)[0].normal_form for sublist in splited_phrases for item in sublist
]
flat_list[:20]

series_phrases = pd.Series(flat_list)
series_phrases

# +
sns.set()

plt.title("Слова, которые встречаются больше 2000 раз")

series_phrases.value_counts()[series_phrases.value_counts() > 2000].plot.bar()

plt.ylabel("Кол-во встречаемости слова")
plt.xlabel("Слова")
plt.show();
