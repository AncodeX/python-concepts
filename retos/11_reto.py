from datetime import datetime
from math import floor

date_now = datetime.now()
new_year = datetime(2024, 1, 1)
birthday = datetime(2003, 12, 18)


day = date_now.day
month = date_now.month
year = date_now.year
hour = date_now.hour
minute = date_now.minute

print(f"dia: {day}, mes: {month}, año: {year}, hora: {hour}, minuto: {minute}")

date_format = date_now.strftime("%m/%d/%Y, %H:%M:%S")
print(date_format)

date = "5 december, 2019"
date_object = datetime.strptime(date, "%d %B, %Y")
print(date_object)


age = date_now - birthday
age = age.days/356
age = floor(age)

print(new_year - date_now)
print(age)