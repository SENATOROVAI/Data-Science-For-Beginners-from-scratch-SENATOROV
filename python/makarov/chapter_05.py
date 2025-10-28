"""Дата и время в Питоне."""

# +
# импортируем весь модуль
# import datetime
# чтобы получить доступ к функции now(), сначала обратимся
# к модулю, потом к классу
# print(datetime.datetime.now())

# часто из модуля datetime удобнее импортировать только класс datetime

# +
# импортируем весь модуль
from datetime import datetime

import pytz
# -

# чтобы получить доступ к функции now(), сначала обратимся к модулю, потом к классу
print(datetime.now())

# поместим созданный с помощью функции now() объект datetime в переменную cur_dt
cur_dt: datetime = datetime.now()
print(cur_dt)

# с помощью соответствующих атрибутов выведем каждый из компонентов объекта
print(
    cur_dt.year,
    cur_dt.month,
    cur_dt.day,
    cur_dt.hour,
    cur_dt.minute,
    cur_dt.second,
    cur_dt.microsecond,
)

print(cur_dt.weekday(), cur_dt.isoweekday())

# посмотрим на часовой пояс с помощью атрибута tzinfo
print(cur_dt.tzinfo)

# выведем текущее время в Москве
dt_moscow = datetime.now(pytz.timezone("Europe/Moscow"))
print(dt_moscow)

print(dt_moscow.tzinfo)

# получим timestamp текущего времени с помощью метода .timestamp()
timestamp = datetime.now().timestamp()

print(timestamp)

# для этого воспользуемся методом .fromtimestamp()
print(datetime.fromtimestamp(timestamp))

# передадим объекту datetime 20 февраля 1991 года
hb: datetime = datetime(1991, 2, 20)
print(hb)

# извлечем год с помощью атрибута year
print(hb.year)

# создадим timestamp
print(datetime.timestamp(hb))

# дана строка с датой 2 декабря 2007 года и временем 12 часов 30 минут и 45 секунд
str_to_dt: str = "2007-12-02 12:30:45"
type(str_to_dt)

# +
res_dt: datetime = datetime.strptime(str_to_dt, "%Y-%m-%d %H:%M:%S")

print(res_dt)
print(type(res_dt))
# -

# вначале создадим объект datetime и передадим ему 19 ноября 2002 года
dt_to_str: datetime = datetime(2002, 11, 19)
type(dt_to_str)

# +
# преобразуем объект в строку в формате "день недели, месяц число, год"
# res_str: datetime = datetime.strftime(dt_to_str, '%A, %B %d, %Y')
#
# print(res_str)
# print(type(res_str))
# -

dt_to_str.strftime("%A, %B %d, %Y")

date1: datetime = datetime(1905, 6, 30)  # "К электродинамике движущихся тел"
date2: datetime = datetime(1916, 5, 11)  # Общая теория относительности

# date1 < date2

# date1 > date2

# +
# вначале запишем даты в виде строки и сравним их
# '2007-12-02' > '2002-11-19'

# +
# теперь в виде объекта datetime
# datetime(2007, 12, 2) > datetime(2002, 11, 19)
# -

diff = date2 - date1
print(diff)

type(diff)

# +
# datetime.timedelta
# -

print(diff.days)

# +
# а затем создадим объект timedelta продолжительностью 1 день
# timedelta(days=1)
# -

# допустим сейчас 1 января 2070 года
future: datetime = datetime(2070, 1, 1)

# +
# сначала просто умножим 365 дней на 170
# time_travel = timedelta(days=365) * 170
#
# а потом переместимся из будущего в прошлое
# past = future - time_travel
#
# к сожалению, мы немного "не долетим",
# потому что не учли високосные годы, в # # которых 366 дней
# past

# +
# time_travel: timedelta = timedelta(days=62092)
#
# past = future - time_travel
# past

# +
# cur_date: datetime = datetime(2021, 1, 1)
# эту дату мы будем выводить
# end_date: datetime = datetime(2021, 1, 10)
# это граница (условие в цикле # # while)
#
#  пока верно условие
# while cur_date <= end_date:
#
#     # выведем cur_date в формате "месяц число, год"
#     print(cur_date.strftime("%b %d, %Y"))
#
#     # прибавим к выводимой дате один день
#     cur_date += timedelta(days=1)

# +
# пусть дан список чисел в строковом формате, и мы хотим посчитать их сумму
# предположим, буква "а" попала в список случайно
numbers: list[str] = ["5", "10", "a", "15", "10"]

# объявим переменную суммы
total: int = 0

# пройдемся по числам
for number in numbers:

    # попробуем прибавить число к переменной total
    try:
        total += int(number)

    # если же этого сделать не удастся
    except ValueError:
        # перейдем к следующему числу
        pass

# выведем сумму
# total

# +
# temp_1 = pd.read_csv('temperature.csv')
# print(temp_1)

# +
# # создадим список с известными нам шаблонами
# formats: list[str] = ['%Y-%m-%d', '%Y-%m-%-d', '%Y-%m']
#
# # создадим счетчик для записей, которые не обработались
# counter_9 = 0
#
# # пройдемся в цикле по столбцу Date
# for d in temp.Date:
#
#   # затем пройдемся по известным нам форматам
#   for format in formats:
#
#     # попробуем, применив каждый из форматов,
#     # преобразовать строку с датой в объект datetime
#     try:
#       print(datetime.strptime(d, format))
#       counter_9 += 1
#
#     # если что-то пошло не так
#     except:
#       # перейдем к следующему формату (второй цикл for) или записи (первый цикл # for)
#       pass
#
# # посмотрим, сколько записей не обработалось
# print('Не обработалось записей:', len(temp) - counter_9)

# +
# temp_parsed = pd.read_csv('temperature.csv',
# index_col = 'Date', parse_dates = True)
# temp_parsed

# +
# индекс превратился в объект datetime
# type(temp_parsed.index)
