"""Introduction to MSTICP."""

# # Введение в MSTICPy
#
# ## Вступление
#
# [MSTICPy](https://msticpy.readthedocs.io/) или `Microsoft Threat Intelligence Python Security Tools` — это набор инструментов на языке Python, предназначенных для расследования инцидентов в области кибербезопасности, поиска индикаторов компрометации (IoC). Многие из инструментов возникли как Jupyter-блокноты, написанные для решения задач форензики. Некоторые инструменты полезны только в блокнотах (например, виджеты и визуализация), но многие другие можно использовать из командной строки или импортировать в свой Python-код.
#
# Пакет отвечает трем основным потребностям в расследовании инцидентов кибербезопасности:
#
# - получение и обогащение данных;
# - анализ данных;
# - визуализация данных.
#
# ### Дополнительно:
#
# Отличная обзорная [статья на Хабре](https://habr.com/ru/company/microsoft/blog/487584/) о том, чем Jupyter-блокноты могут помочь исследователям кибербезопасности.
#
# Также Microsoft ежегодно проводит онлайн конференцию [Infosec Jupyterthon](https://infosecjupyterthon.com/introduction.html) по использованию Jupyter-блокнотов в кибербезопасности.
#
# ## Варианты использования и среды
#
# Хотя `MSTICPy` изначально разрабатывался для использования с `Azure Sentinel` (это такая облачная SIEM от Microsoft), большая часть пакета не зависит от источников данных. Также включены компоненты запроса данных для `Splunk` (это платформа для сбора, хранения, обработки и анализа логов), `Microsoft 365 Defender Advanced`, `Microsoft Graph` и других.
#
# По опыту использования `MSTICPy` сильно привязан к облачным API, для которых необходимы лицензии и прочие ключи доступа, что несколько снижает заявленную открытость/доступность/полезность пакета. По сути `MSTICPy` является всего лишь интерфейсом поверх десятка различных API и различных пакетов Python.
#
# API-интерфейсы инструментов обычно используют формат `DataFrame` пакета pandas в качестве входных данных и, при необходимости, возвращают данные в виде `DataFrame`.

# ## Установка
#
# `MSTICPy` требует Python 3.8 или более поздней версии. У меня получилось установить только с Python 3.11. 
#
# Если вы используете Jupyter-блокноты локально, то потребуется установить Python 3.11. Рекомендую дистрибутив Ananconda, поскольку он поставляется со многими предустановленными пакетами, необходимыми для `MSTICPy`.

# `MSTICPy` имеет большое количество зависимостей и, чтобы избежать конфликтов с пакетами в существующей среде Python, вы можете создать виртуальную среду `conda` и установить пакет там.
#
# Для `сonda` используйте команду `conda create` из оболочки `conda`.
#
# ```
# (base) conda create --name infosec python==3.11
# ```
#
# Активируем созданное виртуальное окружение:
# ```
# (base) conda activate infosec
# ```
# Следующий шаг - установка `MSTICPy`. Вы можете выбрать несколько конфигураций пакетов, но у меня получилось установить только с полным набором (в MacOS):
# ```
# (infosec) pip install msticpy\[all]
# ```
# PS. или в ОС Windows: 
# ```
# (infosec) pip install msticpy[all]
# ```
# Вручную обновите `MSTICPy` до крайней версии, иначе примеры работать не будут:
# ```
# (infosec) pip install --upgrade msticpy==2.2.0
# ```
# Я предпочитаю использовать оболочку Jupyter Lab, поэтому далее устанавливаю ее:
# ```
# (infosec) conda install -c conda-forge jupyterlab
# ```
# Запукаем Jupyter Lab и радуемся, что все работает:
# ```
# (infosec) jupyter lab
# ```

# Вы можете импортировать `MSTICPy` как есть или переименовать его во что-то более простое для ввода, например `mp`:

# +
from io import BytesIO
from zipfile import ZipFile

import msticpy as mp
import pandas as pd
import requests
from msticpy.data import QueryProvider
from msticpy.nbtools.nbdisplay import display_alert
from msticpy.nbtools.nbwidgets import QueryTime, SelectAlert, SelectItem

# from msticpy.vis import mp_pandas_plot
from pandas.io import json
# -

# Доступна простая помощь:

help(mp)

# Используйте функцию `search`, чтобы найти необходимый модуль для импорта:

mp.search("geo")

# ## Инициализация MSTICpy
#
# Функция инициализации `init_notebook` предназначена для подготовки блокнота. Она делает несколько полезных вещей:
#
# - Импортирует некоторые распространенные (не `MSTICPy`) пакеты, такие как `pandas`, `numpy`, `ipywidgets`.
#
# - Импортирует ряд компонентов `MSTICPy`, таких как `Entities`.
#
# - Проверяет наличие действительного файла конфигурации `msticpyconfig`. Для некоторых элементов `MSTICPy` требуются [параметры конфигурации](https://msticpy.readthedocs.io/en/latest/getting_started/msticpyconfig.html). Примером могут служить поставщики Threat Intelligence, т.е. потоков данных (фидов) с индикаторами компрометации.
#
# - Инициализирует магию блокнота `MSTICPy` и средства доступа к `pandas`.
#
# - Перехватывает обработку исключений блокнота для отображения дружественных исключений `MSTICPy` (другие исключения не затрагиваются).

help(mp.init_notebook)

mp.init_notebook()

# Вы можете заполнить `msticpyconfig` вручную или использовать редактор настроек `MSTICPy` для просмотра и редактирования сохраненных там настроек.

# +
# msticpy.MpConfigEdit()
# -

# ## Доступ к наборам данных Mordor

# Рассмотрим два способо загрузки данных из области кибербезопасности:
# - с помощью модуля `requests`;
# - с помощью `MSTICPy`.

# ### Использование requests для доступа к наборам данных Mordor
#
# Проект [Security Datasets](https://securitydatasets.com/introduction.html) — это инициатива с открытым исходным кодом, которая предоставляет предварительно записанные наборы данных, описывающие вредоносные действия с разных платформ, сообществу кибербезопасности для ускорения анализа данных и исследования угроз.
#
# Начнем с импорта необходимых библиотек Python для доступа к содержимому наборов данных:

# Мы сделаем HTTP-запрос к репозиторию [Security Datasets](https://github.com/OTRF/Security-Datasets) с помощью метода `GET` и сохраним содержимое ответа в переменной `zipFileRequest`.
#
# Важно отметить, что мы используем ссылку на необработанные данные, связанную с набором данных. Этот тип ссылок обычно начинается с https://raw.githubusercontent.com/ + ссылка на проект.

# +
# pylint: disable=line-too-long

url = "https://raw.githubusercontent.com/OTRF/Security-Datasets/master/datasets/atomic/windows/discovery/host/empire_shell_net_localgroup_administrators.zip"
zip_file_request = requests.get(url)
# -

type(zip_file_request)

# Тип данных содержимого HTTP-ответа
type(zip_file_request.content)

# Мы создадим объект [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO) для доступа к содержимому ответа и сохраним его в объекте [ZipFile](https://docs.python.org/3/library/zipfile.html#zipfile-objects). Все манипуляции с данными выполняются в памяти.

with ZipFile(BytesIO(zip_file_request.content)) as zip_file:
    print(type(zip_file))

# Любой объект `ZipFile` может содержать более одного файла. Мы можем получить доступ к списку имен файлов, используя метод [namelist](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.namelist). Поскольку наборы данных содержат один файл, то будем ссылаться на первый элемент списка при извлечении файла `JSON`.

zip_file.namelist()

# Мы извлечем файл `JSON` из сжатой папки, используя метод [extract](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract). После запуска приведенного ниже кода загрузим и сохраним файл в каталоге, указанном в параметре `path`.
#
# Важно отметить, что этот метод возвращает нормализованный путь к файлу `JSON`. Мы сохраняем путь к каталогу в переменной `datasetJSONPath` и используем его при попытке прочитать файл.

# +
dataset_json_path = zip_file.extract(zip_file.namelist()[0], path="../data")

print(dataset_json_path)
# -

# Теперь, когда файл загружен и известен путь к нему, мы можем прочитать файл `JSON` с помощью метода [read_json](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html?highlight=read_json#pandas.read_json).
#
# Важно отметить, что при записи набора данных каждая строка файла `JSON` представляет собой событие. Поэтому важно установить для параметра `lines` значение `True`.

dataset = json.read_json(path_or_buf=dataset_json_path, lines=True)

# Метод `read_json` возвращает объект `DataFrame`:

type(dataset)

# Наконец, мы должны начать исследовать наш набор данных, используя различные функции или методы, такие как `head`.

dataset.head(n=1)

# ### Использование MSTICPy для доступа к наборам данных Mordor

# Чтобы использовать [Mordor провайдер](https://msticpy.readthedocs.io/en/latest/data_acquisition/MordorData.html), сначала создайте провайдер запросов `Mordor`. Затем вызовите функцию `connect`: она загрузит метаданные из `Mordor` и `Mitre` для заполнения набора запросов.

qry_prov_sd = QueryProvider("Mordor")

# Ход загрузки отображается с помощью индикатора выполнения.

qry_prov_sd.connect()

# После загрузки метаданных поставщик заполняется функциями запроса, которые можно использовать для извлечения наборов данных.
#
# Вы можете увидеть список доступных запросов с помощью функции `list_queries`.

print(qry_prov_sd.list_queries()[:10])

# Вы можете использовать функцию провайдера `search_queries` для поиска запросов на соответствие требуемым атрибутам.

qry_prov_sd.search_queries("empire + localgroup")

# Чтобы получить набор данных, выполните требуемый запрос. Все запросы доступны как атрибуты провайдера `Mordor`.

emp_df = (
    qry_prov_sd.atomic.windows.discovery.host.empire_shell_net_localgroup_administrators()
)
emp_df.head()

# Убедитесь, что временные метки действительно являются временными метками, а не строками.

emp_df["EventTime"] = pd.to_datetime(emp_df["EventTime"])

emp_df.mp_plot.timeline(time_column="EventTime", group_by="EventID")

# ## Виджеты MSTICPy
#
# `MSTICPy` включает ряд виджетов, упрощающих взаимодействие с данными, особенно для пользователей, не имеющих опыта программирования.
#
# Виджеты предназначены для выполнения ряда общих задач, которые могут потребоваться пользователю для взаимодействия с блокнотом, таких как выбор элементов из возвращенных данных или установка временных рамок для запроса.
#
# Сами виджеты встроены в `ipywidgets` и доступны в модуле `msticpy.nbtools.nbwidgets`.
#
#     Примечание. Виджеты автоматически импортируются программой init_notebook.
#
# Приведенный ниже код создает виджет `Временной диапазон`, который можно использовать, чтобы позволить пользователю установить временной диапазон. Мы говорим ему использовать дни в качестве единицы измерения и устанавливаем максимальный диапазон для выбора.

time_select = QueryTime(units="day", max_before=20, before=5, max_after=1)
time_select.display()

# Затем мы можем вызвать свойства `start` / `end` и получить объекты даты и времени на основе выбора пользователя.

time_select.start

# Другие виджеты позволяют выбирать элементы из списка вместе с опцией текстового фильтра, чтобы помочь пользователям найти элементы:

# +
items = ["item 1", "item 2", "item 3"]

selection = SelectItem(item_list=items, description="Select item", auto_display=True)
# -

# Существуют также специальные виджеты, такие как `SelectAlert`, которые позволяют пользователю выбрать конкретное предупреждение из списка предупреждений. 

# +
# pylint: disable=line-too-long

alerts = pd.read_pickle(
    "https://github.com/microsoft/msticpy/raw/main/tests/testdata/localdata/alerts_list.pkl"
)

alert_select = SelectAlert(alerts=alerts, action=display_alert)
alert_select.display()
# -

# Другие виджеты `MSTICPy` включают:
#
# - Простой слайдер обратного просмотра на основе даты и времени `Lookback`
#
# - Текстовое поле для захвата пользовательского ввода `GetText`
#
# - Виджет для захвата и возврата переменной среды `GetEnvrionmentKey`
#
# - Виджет для выбора подмножества элементов из списка `SelectSubset`
#
# - Виджет, показывающий ход выполнения задачи `Progress`
#
# - Кнопки с несколькими вариантами с функцией ожидания, которая приостанавливает выполнение ячейки до тех пор, пока пользователь не выберет вариант `OptionButtons`
#
# - Более подробную информацию о виджетах `MSTICPy` можно найти [здесь](https://msticpy.readthedocs.io/en/latest/visualization/NotebookWidgets.html).

# Примеры официальных блокнотов по [ссылке](https://msticpy.readthedocs.io/en/latest/notebooksamples.html).
