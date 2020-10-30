from datetime import datetime
import calendar

date_time_str = input("print pls a date:")

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')

year = date_time_obj.year
day = date_time_obj.day
month = date_time_obj.month

print(calendar.day_name[calendar.weekday(year, month, day)])
