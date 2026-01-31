"""What is being added to favorites on OZON."""

# # Что добавляют в избранное на OZON
#
# > [источник](https://opendata.ozon.ru/data/chto-dobavlyaut-v-izbrannoe/)
#
# Один из способов оценить, насколько товар востребован среди покупателей - посмотреть, как часто его добавляют в избранное. В этом датасете мы собрали товары, которые пользователи чаще всего добавляли в избранное, и которых уже более 15 дней нет в наличии. Такие товары мы разбили на две группы:
#
# - Товары, добавленные в избранное наибольшее количество раз по итогам последнего месяца, которых нет в наличии более 15 дней.
# - Товары, которые пользователи больше всего добавляли в избранное за всю историю и которых нет в наличии более 15 дней

import pandas as pd

# +
# pylint: disable=line-too-long

df = pd.read_excel(
    "https://github.com/dm-fedorov/pandas_basic/blob/master/%D0%BA%D0%B5%D0%B9%D1%81%D1%8B%20%D0%BF%D0%BE%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D1%83%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/ozon_case_02/data/raw/chto-dobavlyali-v-izbrannoe-v-noyabre-2020.xlsx?raw=True"
)
df.head()
