"""Date and time."""

# +
import datetime
from datetime import datetime, timedelta

import pandas as pd
import pytz

# -

print(datetime.datetime.now())

print(datetime.now())

cur_dt = datetime.now()
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

print(cur_dt.weekday(), cur_dt.isoweekday())

print(cur_dt.tzinfo)

dt_moscow = datetime.now(pytz.timezone("Europe/Moscow"))
print(dt_moscow)

print(dt_moscow.tzinfo)

timestamp = datetime.now().timestamp()
print(timestamp)

print(datetime.fromtimestamp(timestamp))

hb = datetime(1991, 2, 20)
print(hb)

print(hb.year)

print(datetime.timestamp(hb))

str_to_dt = "2007-12-02 12:30:45"
type(str_to_dt)

# +
res_dt = datetime.strptime(str_to_dt, "%Y-%m-%d %H:%M:%S")

print(res_dt)
print(type(res_dt))
# -

dt_to_str = datetime(2002, 11, 19)
type(dt_to_str)

# +
res_str = datetime.strftime(dt_to_str, "%A, %B %d, %Y")

print(res_str)
print(type(res_str))
# -

date1 = datetime(1905, 6, 30)
date2 = datetime(1916, 5, 11)

date1 < date2

date1 > date2
"2007-12-02" > "2002-11-19"

datetime(2007, 12, 2) > datetime(2002, 11, 19)

diff = date2 - date1
print(diff)

type(diff)

print(diff.days)

timedelta(days=1)

future = datetime(2070, 1, 1)
future

# +
time_travel = timedelta(days=365) * 170

past = future - time_travel

past
# -

datetime(2070, 1, 1) - datetime(1900, 1, 1)

# +
time_travel = timedelta(days=62092)

past = future - time_travel
past
# -

365 * 170

datetime(2070, 1, 1) - datetime(1900, 1, 1)

# +
cur_date = datetime(2021, 1, 1)
end_date = datetime(2021, 1, 10)

while cur_date <= end_date:

    print(cur_date.strftime("%b %d, %Y"))

    cur_date += timedelta(days=1)

# +
numbers = ["5", "10", "a", "15", "10"]

total = 0

for number in numbers:

    try:
        total += int(number)
    except:
        pass

total

# +
total = 0

for number in numbers:
    try:
        total += int(number)
    except:
        print(f"Элемент '{number}' обработать не удалось")

total
# -

temp = pd.read_csv("temperature.csv")
temp

# +
formats = ["%Y-%m-%d", "%Y-%m-%-d", "%Y-%m"]

counter = 0

for d in temp.Date:

    for format in formats:

        try:
            print(datetime.strptime(d, format))
            counter += 1

        except:

            pass


print("Не обработалось записей:", len(temp) - counter)
# -

temp_parsed = pd.read_csv("temperature.csv", index_col="Date", parse_dates=True)
temp_parsed

type(temp_parsed.index)
