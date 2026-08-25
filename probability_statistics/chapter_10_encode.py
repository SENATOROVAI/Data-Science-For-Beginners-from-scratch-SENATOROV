"""Encoding categorical data."""

# # Кодирование категориальных переменных

import category_encoders as ce
import jenkspy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import binned_statistic
from sklearn.preprocessing import (
    KBinsDiscretizer,
    LabelEncoder,
    OneHotEncoder,
    OrdinalEncoder,
)

# +
scoring = {
    "Name": ["Иван", "Николай", "Алексей", "Александра", "Евгений", "Елена"],
    "Age": [35, 43, 21, 34, 24, 27],
    "City": [
        "Москва",
        "Нижний Новгород",
        "Санкт-Петербург",
        "Владивосток",
        "Москва",
        "Екатеринбург",
    ],
    "Experience": [7, 13, 2, 8, 4, 12],
    "Salary": [95, 135, 73, 100, 78, 110],
    "Credit_score": ["Good", "Good", "Bad", "Medium", "Medium", "Good"],
    "Outcome": ["Вернул", "Вернул", "Не вернул", "Вернул", "Не вернул", "Вернул"],
}

df = pd.DataFrame(scoring)
df
# -

# ## Еще раз про категориальные данные

# ### `.info()`, `.unique()`, `.value_counts()`

df.info()

df.dtypes

df.City.unique()

# метод .value_counts() сортирует категории по количеству объектов
# в убывающем порядке
df.City.value_counts()

np.unique(df.City, return_counts=True)

# посмотрим на общее количество уникальных категорий
df.City.value_counts().count()

score_counts = df.Credit_score.value_counts()
sns.barplot(x=score_counts.index, y=score_counts.values)
plt.title("Распределение данных по категориям")
plt.ylabel("Количество наблюдений в категории")
plt.xlabel("Категории");

# ### Тип данных 'category'

df = df.astype({"City": "category", "Outcome": "category"})

df.Credit_score = pd.Categorical(
    df.Credit_score, categories=["Bad", "Medium", "Good"], ordered=True
)

df.Credit_score.cat.categories

df.Credit_score.dtype

df.Credit_score.cat.codes

# +
df.Outcome = df.Outcome.cat.rename_categories(
    new_categories={"Вернул": "Yes", "Не вернул": "No"}
)

df
# -

df.info()

# ### Кардинальность данных

# +
region = np.where(((df.City == "Екатеринбург") | (df.City == "Владивосток")), 0, 1)
df.insert(loc=3, column="Region", value=region)

df
# -

# ## Базовые методы кодирования

# ### Кодирование через `cat.codes`

df_cat = df.copy()
df_cat.Credit_score.cat.codes

df_cat.Credit_score = df_cat.Credit_score.astype("category").cat.codes
df_cat

# ### Mapping

# +
df_map = df.copy()

# ключами будут старые значения признака
# значениями словаря - новые значения признака
map_dict = {"Bad": 0, "Medium": 1, "Good": 2}

df_map["Credit_score"] = df_map["Credit_score"].map(map_dict)
df_map

# +
# fmt: off
# сделаем еще одну копию датафрейма
df_map = df.copy()

df_map["Credit_score"] = df_map["Credit_score"].map(
    {"Bad": 0, "Medium": 1, "Good": 2}
)
df_map
# fmt: on
# -

# ### Label Encoder

# +
labelencoder = LabelEncoder()

df_le = df.copy()

# на вход принимает только одномерные массивы
df_le.loc[:, "Outcome"] = labelencoder.fit_transform(df_le.loc[:, "Outcome"])
df_le
# -

# применим LabelEncoder к номинальной переменной City
df_le.loc[:, "City"] = labelencoder.fit_transform(df_le.loc[:, "City"])
df_le

# применим LabelEncoder к номинальной переменной Credit_score
df_le.loc[:, "Credit_score"] = labelencoder.fit_transform(df_le.loc[:, "Credit_score"])
df_le

# порядок нарушен
labelencoder.classes_

# ### Ordinal Encoder

# +
ordinalencoder = OrdinalEncoder(categories=[["Bad", "Medium", "Good"]])

df_oe = df.copy()

# используем метод .to_frame() для преобразования Series в датафрейм
df_oe.loc[:, "Credit_score"] = ordinalencoder.fit_transform(
    df_oe.loc[:, "Credit_score"].to_frame()  # type: ignore[operator]
)
df_oe
# -

ordinalencoder.categories_

# ### One Hot Encoding

# #### класс OneHotEncoder

# +
df_onehot = df.copy()


# создадим объект класса OneHotEncoder
# параметр sparse = True выдал бы результат в сжатом формате
onehotencoder = OneHotEncoder(sparse_output=False)

encoded_df = pd.DataFrame(onehotencoder.fit_transform(df_onehot[["City"]]))
encoded_df
# -

onehotencoder.get_feature_names_out()

encoded_df.columns = onehotencoder.get_feature_names_out()
encoded_df

df_onehot = df_onehot.join(encoded_df)
df_onehot.drop("City", axis=1, inplace=True)

# +
df_onehot = df.copy()

# чтобы удалить первый признак, используем параметр drop = 'first'
onehot_first = OneHotEncoder(drop="first", sparse_output=False)

encoded_df = pd.DataFrame(onehot_first.fit_transform(df_onehot[["City"]]))
encoded_df.columns = onehot_first.get_feature_names_out()

df_onehot = df_onehot.join(encoded_df)
df_onehot.drop("Outcome", axis=1, inplace=True)
df_onehot
# -

# #### `pd.get_dummies()`

df_dum = df.copy()
pd.get_dummies(df_dum, columns=["City"])

pd.get_dummies(df_dum, columns=["City"], prefix="", prefix_sep="")

pd.get_dummies(df_dum, columns=["City"], prefix="", prefix_sep="", drop_first=True)

# #### Библиотека category_encoders

# установим библиотеку
# !pip install category_encoders

# +
df_catenc = df.copy()


# в параметр cols передадим столбцы, которые нужно преобразовать
ohe_encoder = ce.OneHotEncoder(cols=["City"])
# в метод .fit_transform() мы передадим весь датафрейм целиком
df_catenc = ohe_encoder.fit_transform(df_catenc)
df_catenc
# -

# #### Сравнение инструментов

train = pd.DataFrame({"recom": ["yes", "no", "maybe"]})
train

test = pd.DataFrame({"recom": ["yes", "no", "yes"]})
test

# ##### `pd.get_dummies()`

pd.get_dummies(train)

pd.get_dummies(test)

# ##### OHE sklearn

ohe = OneHotEncoder()
ohe_model = ohe.fit(train)
ohe_model.categories_

train_arr = ohe_model.transform(train).toarray()
pd.DataFrame(train_arr, columns=["maybe", "no", "yes"])

test_arr = ohe_model.transform(test).toarray()
pd.DataFrame(test_arr, columns=["maybe", "no", "yes"])

ohe = OneHotEncoder()
ohe_model = ohe.fit(test)
ohe_model.categories_

# ##### OHE category_encoders

ohe_encoder = ce.OneHotEncoder()
ohe_encoder.fit(train)

# категория maybe стоит на последнем месте
ohe_encoder.transform(test)

# убедимся в этом, добавив названия столбцов
test_df = ohe_encoder.transform(test)
test_df.columns = ohe_encoder.category_mapping[0]["mapping"].index[:3]
test_df

# ## Binning/bucketing

# +
import io
import os
from dotenv import load_dotenv
import requests


load_dotenv()

boston_csv_url = os.environ.get("BOSTON_CSV_URL", "")
response = requests.get(boston_csv_url)
boston = pd.read_csv(io.BytesIO(response.content))
boston.TAX.hist();
# -

# ### На равные интервалы

# +
min_value = boston.TAX.min()
max_value = boston.TAX.max()

bins = np.linspace(min_value, max_value, 4)
bins
# -

labels = ["low", "medium", "high"]

boston["TAX_binned"] = pd.cut(
    boston.TAX,
    bins=bins,
    labels=labels,
    # уточним, что первый интервал должен включать
    # нижнуюю границу (значение 187)
    include_lowest=True,
)

boston[["TAX", "TAX_binned"]].sample(5, random_state=42)

boston.TAX.value_counts(bins=3, sort=False)

# ### По квантилям

# для наглядности вначале найдем интересующие нас квантили
np.quantile(boston.TAX, q=[1 / 3, 2 / 3])

# +
boston["TAX_qbinned"], boundaries = pd.qcut(
    boston.TAX,
    q=3,
    # precision определяет округление
    precision=1,
    labels=labels,
    retbins=True,
)

boundaries
# -

boston[["TAX", "TAX_qbinned"]].sample(5, random_state=42)

boston.TAX_qbinned.value_counts()

# ### KBinsDiscretizer

# #### strategy = 'uniform'

# +
est = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="uniform", subsample=None)

est.fit(boston[["TAX"]])
est.bin_edges_
# -

np.unique(est.transform(boston[["TAX"]]), return_counts=True)

# #### strategy = 'quantile'

est = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")
est.fit(boston[["TAX"]])
est.bin_edges_

np.unique(est.transform(boston[["TAX"]]), return_counts=True)

# #### strategy = 'kmeans'

# +
est = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="kmeans", subsample=None)

est.fit(boston[["TAX"]])
est.bin_edges_
# -

np.unique(est.transform(boston[["TAX"]]), return_counts=True)

# ### С помощью статистических показателей

# +
medians, bin_edges, _ = binned_statistic(
    boston.TAX, np.arange(0, len(boston)), statistic="median", bins=3
)

medians, bin_edges

# +
boston["TAX_binned_median"] = pd.cut(
    boston.TAX, bins=bin_edges, labels=medians, include_lowest=True
)

boston["TAX_binned_median"].value_counts()
# -

# ### Алгоритм Дженкса

# !pip install jenkspy

breaks = jenkspy.jenks_breaks(boston.TAX, n_classes=3)
breaks

# +
boston["TAX_binned_jenks"] = pd.cut(
    boston.TAX, bins=breaks, labels=labels, include_lowest=True
)

boston["TAX_binned_jenks"].value_counts()
