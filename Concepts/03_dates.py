from datetime import datetime, date, timedelta

now = datetime.now()

print(now)

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

timestamp = now.timestamp()

print(f"{year}/{month}/{day}")
print(timestamp)

t = now.strftime("%H:%M:%S")
x = now.strftime("%j")

print(x)
print(f"time: {t}")

date_string = "5 december, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


my_date = date.today()

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

print(now.timestamp())