"""Analyzing IP and MAC addresses with cyberpandas."""

# # Анализ IP- и MAC-адресов с помощью модуля cyberpandas

# Обычно при анализе сетевого трафика используются наборы данных, содержащие IP-адреса.
#
# В стандртном Python для этого есть:
# - [Модуль ipaddress](https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/ipaddress.html)
# - [Learn IP Address Concepts With Python's ipaddress Module](https://realpython.com/python-ipaddress-module/)
# - [An introduction to the ipaddress module](https://docs.python.org/3/howto/ipaddress.html)
#
# Но мы помним про объемы памяти, которые выделяет стандартный Python в момент создания объектов.

# Основываясь на [`ExtensionArray`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.api.extensions.ExtensionArray.html) интерфейсе, [`cyberpandas`](https://cyberpandas.readthedocs.io/en/latest/) предоставляет два новых типа данных: для IP-адреса и для MAC-адреса, совместимые с типами данных pandas.

# !pip install cyberpandas

import pandas as pd
from cyberpandas import IPArray, to_ipaddress

# создаем объекти типа IPArray
arr = IPArray(["192.168.1.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"])  # IP  # MAC
arr

type(arr)

# Создадим `Series` на основе массива `IPArray`:

ser = pd.Series(arr)

ser

# Обратите внимание на `dtype`.
#
# Данные по-прежнему хранятся в формате `IPArray`. Это обеспечивает высокопроизводительный рабочий процесс, который будет [естественным для пользователей pandas](https://cyberpandas.readthedocs.io/en/latest/usage.html#pandas-integration).
#
# Рассмотрим пример анализа сетевого трафика:

# +
# pylint: disable=line-too-long

# данные получены из wireshark -> csv
df = pd.read_csv(
    "https://raw.githubusercontent.com/dm-fedorov/infosec/master/traffic-analysis/data/processed/scan_26112020.csv"
)
# -

df_copy = df.copy()
df_copy.head()

# Посмотрим на типы данных:

df_copy.dtypes

# Преобразуем столбцы `Source` и `Destination` в тип данных `IPArray`:

df_copy["Source"] = IPArray(df_copy["Source"])
df_copy["Destination"] = IPArray(df_copy["Destination"])
df_copy.dtypes

# Или еще один способ для преобразования в `IPArray`:

# +
df_copy = df.copy()

df_copy["Destination"] = to_ipaddress(df_copy["Destination"])
df_copy["Source"] = to_ipaddress(df_copy["Source"])
# -

df_copy.dtypes

df_copy.head()

# Различные атрибуты по [ссылке](https://cyberpandas.readthedocs.io/en/latest/api.html#ip-address-attributes):

df_copy.Source.values.is_ipv4  # type: ignore[union-attr]
