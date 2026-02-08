"""Дата и время в питоне."""

# #### Модуль datetime

# Импорт модуля и класса datetime

# +
# импортируем весь модуль
import datetime as datetime_module

# timedelta вручную
# часто из модуля datetime удобнее импортировать только класс datetime
from datetime import datetime, timedelta

import pandas as pd

# для изменения часового пояса библиотека pytz
import pytz

# чтобы получить доступ к функции now(), сначала обратимся к модулю, потом к классу
print(datetime_module.datetime.now())
# -

# и обращаться непосредственно к нему
print(datetime.now())

# Объект datetime и функция `now()`

# поместим созданный с помощью функции now() объект datetime в переменную cur_dt
cur_dt = datetime.now()
print(cur_dt)

print(
    cur_dt.year,
    cur_dt.month,
    cur_dt.day,
    cur_dt.hour,
    cur_dt.minute,
    cur_dt.minute,
    cur_dt.second,
    cur_dt.microsecond,
)

# также можно посмотреть день недели
# .weekday() - c нуля, .isoweekday() - с единицы
print(cur_dt.weekday(), cur_dt.isoweekday())

# часовой пояс
print(cur_dt.tzinfo)

# выведем текущее время в Москве
dt_moscow = datetime.now(pytz.timezone("Europe/Moscow"))
print(dt_moscow)

# Timestamp

# timestamp - время в UNIX
timestamp = datetime.now().timestamp()

# кол-во секунд, прошедшее с 01.01.1970 до исполнения кода
print(timestamp)

# вернуть в прежний вид с помощью .fromtimestamp()
print(datetime.fromtimestamp(timestamp))

# Создание объекта datetime вручную

# передадим объекту datetime 20 февраля 1991 года
hb = datetime(1991, 2, 20)
print(hb)

# извлечём год с помощью атрибута year
print(hb.year)

# создадим timestamp
print(datetime.timestamp(hb))

# #### Преобразование строки в объект datetime и обратно

# Строка -> datetime через `.strptime()`

str_to_dt = "2007-12-02 12:30:45"
type(str_to_dt)

# +
res_dt = datetime.strptime(str_to_dt, "%Y-%m-%d %H:%M:%S")

print(res_dt)
print(type(res_dt))
# -

# Datetime -> строка через `.strftime()`

dt_to_str = datetime(2002, 11, 19)
type(dt_to_str)

# +
res_str = datetime.strftime(dt_to_str, "%A, %B %d, %Y")

print(res_str)
print(type(res_str))
# -

# .strfrime() можно применять непосредственно к объекту datetime
print(dt_to_str.strftime("%A, %B %d, %Y"))

# или так
print(datetime.now().strftime("%Y-%m-%d"))

# а еще так
print(datetime.now().strftime("%c"))

# Форматирование даты и времени через `.strptime()` и `.strftime()`
#
# |Код | Описание | Пример |
# | --- | --- | --- |
# | `%a` | Сокращенное название дня недели | Sun, Mon, … |
# | `%A` | Полное название дня недели | Sunday, Monday, … |
# | `%w` | День недели как число, Вс - 0, Пн - 1, ... Сб - 6 | 0, 1, …, 6 |
# | `%d` | День месяца в виде числа с нулями | 01, 02, …, 31 |
# | `%-d` | День месяца в виде числа без нулей | 1, 2, …, 31 |
# | `%b` | Сокращенное название месяца | Jan, Feb, …, Dec |
# | `%B` | Полное название месяца | January, February, … |
# | `%m` | Месяц в виде числа с нулями | 01, 02, …, 12 |
# | `%-m` | Месяц в виде числа без нулей | 1, 2, …, 12 |
# | `%y` | Год без века как число с нулями | 00, 01, …, 99 |
# | `%-y` | Год без века как число без нулей | 0, 1, …, 99 |
# | `%Y` | Год с веком | 1999, 2019, ... |
# | `%H` | Час (в 24-часовом формате) в виде числа с нулями | 00, 01, …, 23 |
# | `%-H` | Час (в 24-часовом формате) в виде числа без нулей | 0, 1, …, 23 |
# | `%I` | Час (12-часовой формат) в виде числа с нулями | 01, 02, …, 12 |
# | `%-I` | Час (12-часовой формат) в виде числа без нулей | 1, 2, …, 12 |
# | `%p` | AM или PM | AM, PM |
# | `%M` | Минуты в виде числа с нулями | 00, 01, …, 59 |
# | `%-M` | Минуты в виде числа без нулей | 0, 1, …, 59 |
# | `%S` | Секунды в виде числа с нулями | 00, 01, …, 59 |
# | `%-S` | Секунды в виде числа без нулей | 0, 1, …, 59 |
# | `%j` | День года в виде числа с нулями | 001, 002, …, 366 |
# | `%-j` | День года в виде числа без нулей | 1, 2, …, 366 |
# | `%c` | Полная дата и время | Sun Nov 21 10:38:12 2021 |
# | `%x` | Дата | 11/21/21 |
# | `%X` | Время | 10:43:51 |

# #### Сравнение и арифметика дат

# Сравнение дат

date1 = datetime(1905, 6, 30)
date2 = datetime(1916, 5, 11)

# большей считается более поздняя дата
print(date1 < date2)

# Календарный и алфавитный порядок дат

# Если строки с датой, записаны в виде ГГГГ.ММ.ДД, то мы можем их сравнивать, как если бы мы сравнивали объекты datetime

print(datetime(2007, 12, 2) > datetime(2002, 11, 19))

# Промежуток времени и класс timedelta

# если из большей даты вычесть меньшую, то мы получим временной промежуток между датами
diff = date2 - date1
print(diff)

print(type(diff))

print(diff.days)

print(timedelta(days=1))

# Арифметика дат

# +
# объединив объекты datetime и timedelta, мы можем "путешествовать во времени"

print(datetime(2070, 1, 1) - timedelta(days=365) * 170)

# +
# также с помощью этого удобно перебирать даты

cur_date = datetime(2021, 1, 1)
end_date = datetime(2021, 1, 10)

while cur_date <= end_date:
    print(cur_date.strftime("%b %d, %Y"))
    cur_date += timedelta(days=1)
# -

# #### Дата и обработка ошибок

# Конструкция try/except и оператор pass

numbers = ["5", "10", "a", "15", "10"]
total = 0
for number in numbers:
    try:
        total += int(number)
    except ValueError:
        pass
total

# +
total = 0

for number in numbers:
    try:
        total += int(number)
    except ValueError:
        print(f"Элемент '{number}' обработать не удалось")
# -

# Обработка нескольких форматов дат

temp = pd.read_csv(".\\content\\temperature.csv")
print(temp)

# +
formats = ["%Y-%m-%d", "%Y-%m-%-d", "%Y-%m"]
counter = 0
for date_text in temp.Date:
    for date_format in formats:
        try:
            print(datetime.strptime(date_text, date_format))
            counter += 1
        except TypeError:
            pass
print("Не обработалось записей:", len(temp) - counter)

# Вывод
# 2002-01-01 00:00:00
# 2002-02-01 00:00:00
# 2002-03-01 00:00:00
# 2002-04-01 00:00:00
# 2002-05-01 00:00:00
# 2002-06-01 00:00:00
# 2002-07-01 00:00:00
# 2002-08-01 00:00:00
# 2002-09-01 00:00:00
# 2002-10-01 00:00:00
# 2002-12-01 00:00:00
# Не обработалось записей: 1
# -

int("a")

# +
# воспользуемся решением "из коробки" библиотеки Pandas
# передадим функции read_csv() параметр parse_dates
temp_parsed = pd.read_csv(
    r".\content\temperature.csv", index_col="Date", parse_dates=True
)

print(temp_parsed)
# -

# индекс превратился в объект datetime
print(type(temp_parsed.index))
