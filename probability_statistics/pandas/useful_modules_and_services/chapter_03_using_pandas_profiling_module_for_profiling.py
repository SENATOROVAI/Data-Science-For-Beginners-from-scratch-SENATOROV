"""Using the Pandas Profiling module for profiling."""

# # Использование модуля Pandas Profiling для профилирования

# [`Pandas Profiling`](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/) - это библиотека для генерации интерактивных отчетов на основе пользовательских данных: можем увидеть распределение данных, типы, возможные проблемы.
#
# Библиотека очень проста в использовании: можем создать отчет и отправить его кому угодно!

# +
# Colab включает старую версию pandas-profiling, поэтому необходимо обновиться:

# +
# actual pandas-profiling compatible substitutor
# pip install ydata-profiling==4.7.0

# +
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=['a', 'b', 'c', 'd', 'e']
)
# -

profile = ProfileReport(df,
                        title='Pandas Profiling Report')

profile.to_widgets()

# +
# или отобразить во фрейме блокнота:
#profile.to_notebook_iframe()
# -

profile.to_file("report.html")

# > HTML-версия отчета доступна по [ссылке](https://dfedorov.spb.ru/pandas/reports/report.html)
#
# Авторы библиотеки приводят [результаты анализа данных про Титаник](https://pandas-profiling.github.io/pandas-profiling/examples/master/titanic/titanic_report.html).
#
# При работе с большими данными [можно включать минимальный режим](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/pages/big_data.html) конфигурирования (`minimal=True`).
#
# Разобраться во внутренностях можно через [чтение исходных текстов](https://github.com/pandas-profiling/pandas-profiling/blob/develop/src/pandas_profiling/visualisation/plot.py).
