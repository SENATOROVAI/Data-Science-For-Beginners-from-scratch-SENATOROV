"""Checking statistics for pandas using the pandera module."""

# # Проверка статистических данных для pandas с помощью модуля pandera

# [*pandera*](https://pandera.readthedocs.io/en/stable/) - инструмент проверки данных, который предоставляет интуитивно понятный, гибкий и выразительный API для проверки структур данных *pandas* во время выполнения.
#
# ![](https://raw.githubusercontent.com/pandera-dev/pandera/master/docs/source/_static/pandera-banner.png)

# !pip install pandera

# +
# conda install -c conda-forge pandera
# -

# Начем с показательного примера:

import numpy as np
import pandas as pd
import pandera as pa
from pandera import Check, Column, Hypothesis
from scipy import stats

# создадим фрейм данных:
df = pd.DataFrame(
    {
        "column1": [1, 4, 0, 10, 9],
        "column2": [-1.3, -1.4, -2.9, -10.1, -20.4],
        "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
    }
)
df

# определим схему для проверки фрейма данных:
schema = pa.DataFrameSchema(
    {
        "column1": pa.Column(
            int, checks=pa.Check.le(10)
        ),  # Проверим, что значения меньше или равны 10
        "column2": pa.Column(
            float, checks=pa.Check.lt(-1.2)
        ),  # Проверим, что значения ряда строго меньше -1.2
        "column3": pa.Column(
            str,
            checks=[
                pa.Check.str_startswith("value_"),
                # определим пользовательские проверки как функции,
                # которые принимают серию в качестве входных данных
                pa.Check(lambda s: s.str.split("_", expand=True).shape[1] == 2),
            ],
        ),
    }
)

schema(df)
# ошибок не произошло, значит проверка прошла успешно!

# Основные понятия *pandera* - [`schemas`](https://pandera.readthedocs.io/en/stable/API_reference.html#schemas) (*схемы*), [`schema components`](https://pandera.readthedocs.io/en/stable/API_reference.html#schema-components) (*компоненты схемы*) и [`checks`](https://pandera.readthedocs.io/en/latest/checks.html#checks) (*чекеры*).
#
# - *Схемы* - это вызываемые объекты, которые инициализируются правилами проверки. При вызове с совместимыми данными в качестве входного аргумента объект схемы возвращает сами данные, если проверка проходит успешно или вызывает ошибку `SchemaError`.
#
# - *Компоненты схемы* ведут себя так же, как *схемы*, но в основном используются для определения правил проверки для определенных частей объекта *pandas*, например столбцов во фрейме данных.
#
# - Наконец, *чекеры* позволяют пользователям формулировать правила проверки в зависимости от типа данных, которые *схема* или *компонент схемы* могут проверить.
#
# В частности, центральными объектами *pandera* являются [`DataFrameSchema`](https://pandera.readthedocs.io/en/stable/generated/pandera.schemas.DataFrameSchema.html#pandera-schemas-dataframeschema), [`Column`](https://pandera.readthedocs.io/en/stable/generated/pandera.schema_components.Column.html#pandera.schema_components.Column) и [`Check`](https://pandera.readthedocs.io/en/stable/generated/pandera.checks.Check.html#pandera-checks-check). Вместе эти объекты позволяют пользователям заранее выражать схемы в виде контрактов логически сгруппированных наборов правил проверки, которые работают с фреймами данных *pandas*.

# Например, рассмотрим простой набор данных, содержащий данные о людях, где каждая строка - это человек, а каждый столбец - атрибут об этом человеке:

dataframe = pd.DataFrame(
    {
        "person_id": [1, 2, 3, 4],
        "height_in_feet": [6.5, 7, 6.1, 5.1],
        "date_of_birth": pd.to_datetime(
            [
                "2005",
                "2000",
                "1995",
                "2000",
            ]
        ),
        "education": [
            "highschool",
            "undergrad",
            "grad",
            "undergrad",
        ],
    }
)

dataframe

# Изучив имена столбцов и значения данных, можем заметить, что возможно привнести некоторые знания о мире в предметную область, чтобы выразить наши предположения о том, что считать достоверными данными:

# +
typed_schema = pa.DataFrameSchema(
    {
        "person_id": Column(pa.Int),
        # поддерживаются типы данных numpy и pandas
        "height_in_feet": Column("float"),
        "date_of_birth": Column("datetime64[ns]"),
        "education": Column(pd.StringDtype(), nullable=True),
    },
    # принудительное преобразование к типам данных при проверке фрейма
    coerce=True,
)

typed_schema(dataframe)
# возвращается фрейм данных
# -

# ## Проверка чекеров
#
# Приведенная выше `typed_schema` просто проверяет столбцы, которые, как ожидается, будут присутствовать в допустимом фрейме данных, и связанные с ними типы данных.
#
# Пользователи могут пойти дальше, сделав утверждения о значениях, которые заполняют эти столбцы:

# +
import pandas as pd
import pandera as pa
from pandera import Column, Check

checked_schema = pa.DataFrameSchema(
    {
        # ----- person_id -----
        "person_id": Column(
            pa.Int,                     # тип данных — целое число
            Check.greater_than(0),      # значения должны быть строго > 0
            unique=True,                # запрет на дублирование идентификаторов
        ),

        # ----- height_in_feet -----
        "height_in_feet": Column(
            pa.Float,                   # тип данных — число с плавающей точкой
            Check.in_range(0, 10),      # проверяем, что данные в диапазоне (0, 10)
        ),

        # ----- date_of_birth -----
        "date_of_birth": Column(
            pa.DateTime,                # тип данных — Timestamp
            Check.less_than_or_equal_to(
                pd.Timestamp.now()      # дата рождения не может быть в будущем
            ),
        ),

        # ----- education -----
        "education": Column(
            pd.StringDtype(),           # строковый тип с поддержкой NA
            Check.isin([                # допустимые значения
                "highschool",
                "undergrad",
                "grad",
            ]),
            nullable=True,              # допускаем пустые значения в этом столбце
        ),
    },

    coerce=True,                         # приведение типов данных автоматически
)

# Применяем схему для валидации DataFrame
checked_df = checked_schema(dataframe)

# Возвращается корректный и проверенный DataFrame
checked_df
# -

# Приведенное выше определение схемы устанавливает следующие свойства данных:
#
# - столбец `person_id` представляет собой положительное целое число, которое является распространенным способом кодирования уникальных идентификаторов в наборе данных. Установив для `allow_duplicates` значение `False`, схема указывает, что этот столбец является уникальным идентификатором в этом набор данных.
# - `height_in_feet` - положительное число с плавающей точкой, максимальное значение составляет `10 футов`, что является разумным предположением для максимального роста человека.
# - `date_of_birth` не может быть датой в будущем.
# - `education` может принимать допустимые значения в наборе `{"highschool", "undergrad", "grad"}`. Предположим, что эти данные были собраны в онлайн-форме, где ввод поля был необязательным, было бы целесообразно установить `nullable` как `True` (по умолчанию этот аргумент равен `False`).
#
# ## Отчеты об ошибках и отладка
#
# Если фрейм данных, переданный в вызываемый объект *схемы* (schema), не проходит проверки, *pandera* выдает информативное сообщение об ошибке:

# ```Python
# # данные, которые не проходят проверку:
# invalid_dataframe = pd.DataFrame({
#     "person_id": [6, 7, 8, 9],
#     "height_in_feet": [-10, 20, 20, 5.1],
#     "date_of_birth": pd.to_datetime([
#         "2005", "2000", "1995", "2000",
#     ]),
#     "education": [
#         "highschool", "undergrad", "grad", "undergrad",
#     ],
# })
#
# checked_schema(invalid_dataframe)
# ```

# Ошибка:
#
# ```Python
# SchemaError: <Schema Column(name=height_in_feet, type=float)> failed element-wise validator 0:
# <Check in_range: in_range(0, 10)>
# failure cases:
#    index  failure_case
# 0      0         -10.0
# 1      1          20.0
# ```
#
# Причины ошибки `SchemaError` отображаются в виде фрейма данных, где индекс `failure_case` - это конкретное значение данных, которое не соответствует правилу проверки `Check.in_range`, столбец индекса содержит список местоположений индекса в недействительном фрейме данных с ошибочными значениями, а столбец `count` суммирует количество случаев сбоя этого конкретного значения.
#
# Для более тонкой отладки аналитик может перехватить исключение с помощью шаблона `try ... except` для доступа к данным и случаям сбоя в качестве атрибутов в объекте `SchemaError`:

# ```Python
# from pandera.errors import SchemaError
#
# try:
#     checked_schema(invalid_dataframe)
# except SchemaError as e:
#     print("Failed check:", e.check)
#     print("\nInvalidated dataframe:\n", e.data)
#     print("\nFailure cases:\n", e.failure_cases)
# ```

# Таким образом, пользователи могут легко получить доступ и проверить недопустимый фрейм данных и случаи сбоя, что особенно полезно в контексте длинных цепочек методов преобразования данных:
#
# ```Python
# raw_data = ... # получение сырых данных
# schema = ... # определение схемы
#
# try:
#     clean_data = (
#         raw_data
#         .rename(...)
#         .assign(...)
#         .groupby(...)
#         .apply(...)
#         .pipe(schema)
#     )
# except SchemaError as e:
#     # e.data будет содержать итоговый фрейм данных
#     # для вызова groupby().apply()
#     ...
# ```
#
# ## Расширенные возможности
#
# **Проверка гипотезы**
#
# Чтобы предоставить специалистам полнофункциональный инструмент проверки данных, *pandera* наследует подклассы от класса `Check` для определения `Hypothesis` с целью выражения [проверок статистических гипотез](https://pandera.readthedocs.io/en/stable/hypothesis.html#hypothesis-testing).
#
# Чтобы проиллюстрировать один из вариантов использования этой функции, рассмотрим игрушечное научное исследование, в котором контрольная группа получает плацебо, а лечебная группа получает лекарство, которое, как предполагается, улучшает физическую выносливость. Затем участники этого исследования бегают на беговой дорожке (настроенной с одинаковой скоростью) столько, сколько они могут, и продолжительность бега собирается для каждого человека.
#
# Еще до сбора данных мы можем определить *схему*, которая выражает наши ожидания относительно положительного результата:

# +
from pandera import Check, Column, Hypothesis


endurance_study_schema = pa.DataFrameSchema(
    {
        "subject_id": Column(pa.Int),
        "arm": Column(pa.String, Check.isin(["treatment", "control"])),
        "duration": Column(
            pa.Float,
            checks=[
                Check.greater_than(0),
                # Рассчитайте t-критерий для средних значений двух выборок
                # https://pandera.readthedocs.io/en/stable/generated/methods/
                # pandera.hypotheses.Hypothesis.two_sample_ttest.html
                Hypothesis.two_sample_ttest(
                    sample1="treatment",
                    relationship="greater_than",
                    sample2="control",
                    groupby="arm",
                    alpha=0.01,
                ),
            ],
        ),
    }
)
# -

# После того, как набор данных для этого исследования будет собран, мы можем пропустить его через *схему*, чтобы подтвердить гипотезу о том, что группа, принимающая препарат, увеличивает физическую выносливость, измеряемую продолжительностью бега.
#
# Другой распространенной проверкой гипотез может быть проверка нормального распределения выборки. Используя функцию [`scipy.stats.normaltest`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html), можно написать:

# +
import numpy as np


dataframe = pd.DataFrame(
    {
        "x1": np.random.normal(0, 1, size=100),
    }
)

dataframe.head()

# +
import pandera as pa
from scipy import stats

schema = pa.DataFrameSchema(
    {
        "x1": Column(
            checks=Hypothesis(
                test=stats.normaltest,
                # нулевая гипотеза: x1 нормально распределено
                relationship=lambda k2, p: p > 0.01,
            )
        ),
    }
)

schema(dataframe)
# -

# ## Правила условной проверки
#
# Если мы хотим проверить значения одного столбца, связанного с другим, мы можем указать имя другого столбца в аргументе `groupby`. Это изменяет ожидаемую сигнатуру функции `Check` для входного словаря, где ключи представляют собой уровни дискретных групп в условном столбце, а значения представляют собой объекты `Series` *pandas*, содержащие подмножества интересующего столбца.
#
# Возвращаясь к примеру исследования выносливости, мы могли бы просто утверждать, что средняя продолжительность бега в экспериментальной группе больше, чем в контрольной группе, без оценки статистической значимости:

# +
import pandera as pa


simple_endurance_study_schema = pa.DataFrameSchema(
    {
        "subject_id": Column(pa.Int),
        "arm": Column(pa.String, Check.isin(["treatment", "control"])),
        "duration": Column(
            pa.Float,
            checks=[
                Check.greater_than(0),
                Check(
                    lambda duration_by_arm: (
                        duration_by_arm["treatment"].mean()
                        > duration_by_arm["control"].mean()  # noqa: W503
                    ),
                    groupby="arm",
                ),
            ],
        ),
    }
)
# -

# ## Дополнительные материалы:
#
# - https://www.pyopensci.org/blog/pandera-python-pandas-dataframe-validation
# - https://youtu.be/PxTLD-ueNd4
# - https://ericmjl.github.io/blog/2020/8/30/pandera-data-validation-and-statistics/
