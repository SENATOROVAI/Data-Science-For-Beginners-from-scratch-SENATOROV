"""Datetime module in Python."""

# ## Date and time in Python

# ### Datetime module

# Import module and datetime class

# +
# It is often more convenient to import
# only the datetime class from the datetime module
from datetime import datetime, timedelta

# to change the time zone you need to import the pytz module
import pytz

# to get access to the now() function, we first refer to the module,
# then to the class
print(datetime.now())
# -

# and call him directly
print(datetime.now())

# The datetime object and function `now()`

# put the datetime object created with the now() function into the variable
current_date = datetime.now()
print(current_date)

# Using the appropriate attributes, we will display each component of the
#  object separately.
print(
    current_date.year,
    current_date.month,
    current_date.day,
    current_date.hour,
    current_date.minute,
    current_date.second,
    current_date.microsecond,
)

# you can also look at the day of the week
# .weekday() method starts the week index at zero,
# .isoweekday() starts the week index at one
print(current_date.weekday(), current_date.isoweekday())

# let's look at the time zone using the tzinfo attribute
print(current_date.tzinfo)

# lets print  the current time in Moscow
dt_moscow = datetime.now(pytz.timezone("Europe/Moscow"))
print(dt_moscow)

# let's look at the time zone attribute again
print(dt_moscow.tzinfo)

# Timestamp

# get the timestamp of the current time using the .timestamp() method
timestamp = datetime.now().timestamp()

# output the number of seconds elapsed from 01.01.1970 to the code execution
print(timestamp)

# return timestamp to the previous format using the .fromtimestamp() method
print(datetime.fromtimestamp(timestamp))

# Creating a datetime object manually

# pass datetime object February 20, 1991 to the hb variable
hb = datetime(1991, 2, 20)
print(hb)

# extract the year using the year attribute
print(hb.year)

# create a timestamp from the hb variable using the .timestamp() method
print(datetime.timestamp(hb))

# ### Converting strings to a datetime object and vice versa

# String ➞ datetime via `.strptime()`

str_to_dt = "2007-12-02 12:30:45"
type(str_to_dt)

# +
# convert it to datetime using the .strptime() method
res_dt = datetime.strptime(str_to_dt, "%Y-%m-%d %H:%M:%S")

print(res_dt)
print(type(res_dt))
# -

# Datetime ➞ string via `.strftime()`

dt_to_str = datetime(2002, 11, 19)
type(dt_to_str)

# +
# convert the object to a string in the format "day of week,
# month number, year"
res_str = datetime.strftime(dt_to_str, "%A, %B %d, %Y")

print(res_str)
print(type(res_str))
# -

# .strftime() can be applied directly to a datetime object
dt_to_str.strftime("%A, %B %d, %Y")

# also you can format the current date
datetime.now().strftime("%Y-%m-%d")

# and yet so
datetime.now().strftime("%c")

# Formatting the date and time via `.strptime()` and `.strftime()`

# |Code | Description | Example |
# | --- | --- | --- |
# | `%a` | Abbreviated name of the day of the week | Sun, Mon, … |
# | `%A` | Full name of the day of the week | Sunday, Monday, … |
# | `%w` | The day of the week as a number, Sun - 0, Mon - 1, ... Sat - 6 | 0, 1, …, 6 |
# | `%d` | Day of the month as a number with zeros | 01, 02, …, 31 |
# | `%-d` | Day of the month as a number without zeros | 1, 2, …, 31 |
# | `%b` | Abbreviated name of the month | Jan, Feb, …, Dec |
# | `%B` | Full name of the month | January, February, … |
# | `%m` | Month as a number with zeros | 01, 02, …, 12 |
# | `%-m` | Month as a number without zeros | 1, 2, …, 12 |
# | `%y` | A year without a century is like a number with zeros | 00, 01, …, 99 |
# | `%-y` | A year without a century is like a number without zeros | 0, 1, …, 99 |
# | `%Y` | A year and a century | 1999, 2019, ... |
# | `%H` | Hour (in 24-hour format) as a number with zeros | 00, 01, …, 23 |
# | `%-H` | Hour (in 24-hour format) as a number without zeros | 0, 1, …, 23 |
# | `%I` | Hour (12-hour format) as a number with zeros | 01, 02, …, 12 |
# | `%-I` | Hour (12-hour format) as a number without zeros | 1, 2, …, 12 |
# | `%p` | AM or PM | AM, PM |
# | `%M` | Minutes as a number with zeros | 00, 01, …, 59 |
# | `%-M` | Minutes as a number without zeros | 0, 1, …, 59 |
# | `%S` | seconds as a number with zeros | 00, 01, …, 59 |
# | `%-S` | Seconds as a number without zeros | 0, 1, …, 59 |
# | `%j` | Day of the year as a number with zeros | 001, 002, …, 366 |
# | `%-j` | Day of the year as a number without zeros | 1, 2, …, 366 |
# | `%c` | full date and time | Sun Nov 21 10:38:12 2021 |
# | `%x` | Date | 11/21/21 |
# | `%X` | Time | 10:43:51 |

# ### Comparison and arithmetic of dates

# Date comparison

# let's compare the two publication dates of Einstein's work
date1 = datetime(1905, 6, 30)  # "To the electrodynamics of moving bodies"
date2 = datetime(1916, 5, 11)  # General theory of relativity

# the later date is considered the  longer date
print(date1 < date2)

# the contrary will be proven false
print(date1 > date2)

# Calendar and alphabetical order of dates

# +
# if the dates are recorded as a string in the format YYYY.MM.DD,
# then we can compare them as if we were comparing datetime objects
date_1 = "2007-12-02"
date_2 = "2002-11-19"

# first write the dates as a string and compare them
print(date_1 > date_2)
# -

# now as a datetime object
print(datetime(2007, 12, 2) > datetime(2002, 11, 19))

# Time interval and timedelta class

# if we subtract the smaller date from the larger date,
# we get the time interval between the dates
diff = date2 - date1
print(diff)

# the result will be stored in a special timedelta object
type(diff)

# the days attribute allows you to view only days
print(diff.days)

# a timedelta object can also be created manually
timedelta(days=60)

# The arithmetic of dates

# +
# By combining datetime and timedelta objects, we can "time travel"

# let's assume it's January 1, 2070.
future = datetime(2070, 1, 1)
future

# +
# and we want to go back to January 1, 1900, which is 170 years ago.

# first we just multiply 365 days by 170.
time_travel = timedelta(days=365) * 170

# and then we go from the future to the past
past = future - time_travel

# Unfortunately, we're a little "off" because we left out leap years, which have 366 days.
past
# -

# we've traveled 62050 days, but actually there are
# 62 leap years in this period
365 * 170

# but we already know how to calculate
# the exact number of days (taking leap years into account).
print(datetime(2070, 1, 1) - datetime(1900, 1, 1))

# +
# sometimes it is convenient to use a while loop to create a list of dates
# for example, a list of New Year's Eve holidays in 2021

cur_date = datetime(2021, 1, 1)  # that's the date we'll be outputting
end_date = datetime(2021, 1, 10)  # is the boundary (condition in the while)


while cur_date <= end_date:
    print(cur_date.strftime("%b %d, %Y"))
    cur_date += timedelta(days=1)
# -

# ### Date and error handling

# Try/except construct and pass operator

# +
# Let a list of numbers in string format be given,
# and we want to calculate their sum, assume that the 'a' accidentally there
numbers = ["5", "10", "a", "15", "10"]
total = 0

# Let's go over the numbers
for number in numbers:

    # let's try to add a number to the total variable
    try:
        total += int(number)

    # if it can't be done, an exception will be raised
    except ValueError:
        pass

# output the sum
total

# +
# same code, but with a for loop and a warning message
total = 0

for number in numbers:
    try:
        total += int(number)
    except ValueError:
        print(f"Element '{number}' could not be processed")

total
