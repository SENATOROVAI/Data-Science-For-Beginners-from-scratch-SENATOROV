"""Date and time in Python."""

# ## Дата и время в Питоне

# ### Модуль datetime

# #### Импорт модуля и класса datetime
#

# +
import datetime

import pandas as pd
import pytz

print(datetime.datetime.now())
# -

print(datetime.datetime.now())

# #### Объект datetime и функция now()
#

cur_dt: datetime.datetime = datetime.datetime.now()
print(cur_dt)

print(
    cur_dt.year,
    cur_dt.month,
    cur_dt.day,
    cur_dt.hour,
    cur_dt.minute,
    cur_dt.second,
    cur_dt.microsecond,
)

print(cur_dt.weekday, cur_dt.isoweekday)

print(cur_dt.tzinfo)

dt_moscow: datetime.datetime = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
print(dt_moscow)
print(dt_moscow.tzinfo)

# #### Timestamp
#

timestamp: float = datetime.datetime.now().timestamp()
print(timestamp)
print(datetime.datetime.fromtimestamp(timestamp))

# #### Создание объекта datetime вручную
#

hb: datetime.datetime = datetime.datetime(1991, 2, 20)
print(hb)
print(hb.year)
print(datetime.datetime.timestamp(hb))

# ### Преобразование строки в объект datetime и обратно

# ### Строка -> datetime через .strptime()
#

# +
str_to_dt: str = "2007-12-02 12:30:45"
type(str_to_dt)

res_dt: datetime.datetime = datetime.datetime.strptime(str_to_dt, "%Y-%m-%d %H:%M:%S")
print(res_dt)
print(type(res_dt))
# -

# ### Datetime -> строка через .strftime()
#

# +
dt_to_str: datetime.datetime = datetime.datetime(2002, 11, 19)
print(type(dt_to_str))

res_str: str = datetime.datetime.strftime(dt_to_str, "%A, %B %d, %Y")

print(res_str)
print(type(res_str))
# -

dt_to_str.strftime("%A, %B %d, %Y")

datetime.datetime.now().strftime("%Y-%m-%d")

datetime.datetime.now().strftime("%c")

# ### Сравнение и арифметика дат
#

# #### Сравнение дат

# +
date1: datetime.datetime = datetime.datetime(1905, 6, 30)
date2: datetime.datetime = datetime.datetime(1916, 5, 11)

# date1 < date2
# date1 > date2
# -

# #### Календарный и алфавитный порядок дат
#

# +
# "2007-12-02" > "2002-11-19"

# +
# datetime.datetime(2007, 12, 2) > datetime.datetime(2002, 11, 19)
# -

# #### Промежуток времени и класс timedelta
#

diff: datetime.timedelta = date2 - date1
print(diff)

type(diff)

print(diff.days)

datetime.timedelta(days=1)

# #### Арифметика дат
#

future: datetime.datetime = datetime.datetime(2070, 1, 1)
future

# +
time_travel_var: datetime.timedelta = datetime.timedelta(days=365) * 170

past_var: datetime.datetime = future - time_travel_var
past_var

# +
# datetime.datetime(2070, 1, 1) - datetime.datetime(1900, 1, 1)
time_travel: datetime.timedelta = datetime.timedelta(days=62092)

past: datetime.datetime = future - time_travel
past

# +
cur_date: datetime.datetime = datetime.datetime(2021, 1, 1)
end_date: datetime.datetime = datetime.datetime(2021, 1, 10)

while cur_date <= end_date:
    print(cur_date.strftime("%b %d, %Y"))
    cur_date += datetime.timedelta(days=1)
# -

# ### Дата и обработка ошибок

# #### Конструкция try/except и оператор pass
#

# +
numbers: list[str] = ["5", "10", "a", "15", "10"]

total: int = 0

for number in numbers:
    try:
        total += int(number)
    except ValueError:
        pass

total

# +
total_var: int = 0

for number in numbers:
    try:
        total_var += int(number)
    except ValueError:
        print(f"Элемент '{number}' обработать не удалось")

total_var
# -

# #### Обработка нескольких форматов дат
#

temp: pd.DataFrame = pd.read_csv("temperature.csv")
temp

# +
formats_var: list[str] = ["%Y-%m-%d", "%Y-%m-%-d", "%Y-%m"]

counter: int = 0

for d_var in temp.Date:
    for format_var in formats_var:
        try:
            print(datetime.datetime.strptime(d_var, format_var))
            counter += 1
        except ValueError:
            pass

print("Не отобразилось записей:", len(temp) - counter)
# -

temp_parsed: pd.DataFrame = pd.read_csv(
    "temperature.csv", index_col="Date", parse_dates=True
)
temp_parsed

type(temp_parsed.index)
