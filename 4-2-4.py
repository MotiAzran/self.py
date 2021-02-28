import calendar

date = input("Enter a date: ")
day, month, year = map(int, date.split('/'))
print(calendar.day_name[calendar.weekday(year, month, day)])