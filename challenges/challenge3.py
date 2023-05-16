from datetime import datetime
import math

date_now = datetime.now()
new_year = datetime(year=2024, month=1, day=1)
happy_birthday = datetime(year=2003, month=12, day=18)

print(date_now)

date_format = date_now.strftime("%m/%d/%Y, %H:%M:%S")
print(date_format)

format = "5 December, 2019"

x = date_now.strptime(format, "%d %B, %Y")
print(x)

print(new_year - date_now)
print(date_now.timestamp())

date_days = date_now - happy_birthday
age = math.floor((date_days.days/365))
print(age)

