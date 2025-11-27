"""Date and time."""

# +
# from datetime import datetime, timedelta

# import pytz

# +
# print(datetime.now())

# +
# cur_dt: datetime = datetime.now()
# print(cur_dt)

# +
# print(
#     cur_dt.year,
#     cur_dt.month,
#     cur_dt.day,
#     cur_dt.hour,
#     cur_dt.minute,
#     cur_dt.second,
#     cur_dt.microsecond,
# )

# +
# print(cur_dt.weekday(), cur_dt.isoweekday())
# print(cur_dt.tzinfo)

# +
# dt_moscow: datetime = datetime.now(pytz.timezone("Europe/Moscow"))
# print(dt_moscow)
# print(dt_moscow.tzinfo)

# +
# timestamp: float = datetime.now().timestamp()
# print(timestamp)
# print(datetime.fromtimestamp(timestamp))

# +
# hb: datetime = datetime(1991, 2, 20)
# print(hb)
# print(hb.year)
# print(datetime.timestamp(hb))

# +
# str_to_dt: str = "2007-12-02 12:30:45"
# res_dt: datetime = datetime.strptime(str_to_dt, "%Y-%m-%d %H:%M:%S")
# print(res_dt)
# print(type(res_dt))

# +
# dt_to_str: datetime = datetime(2002, 11, 19)
# print(dt_to_str.strftime("%A, %B %d, %Y"))

# +
# date1: datetime = datetime(1905, 6, 30)
# date2: datetime = datetime(1916, 5, 11)

# diff = date2 - date1
# print(diff)
# print(diff.days)

# +
# future: datetime = datetime(2070, 1, 1)
# time_travel: timedelta = timedelta(days=62092)
# past = future - time_travel
# past

# +
# cur_date: datetime = datetime(2021, 1, 1)
# end_date: datetime = datetime(2021, 1, 10)

# while cur_date <= end_date:
#     print(cur_date.strftime("%b %d, %Y"))
#     cur_date += timedelta(days=1)

# +
# numbers: list[str] = ["5", "10", "a", "15", "10"]
# total: int = 0

# for number in numbers:
#     try:
#         total += int(number)
#     except ValueError:
#         pass

# total
