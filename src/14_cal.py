"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#input in terminal `14_cal.py [month] [year]`

#no input calendar will default to current date and time

#first argument for month, and second for year, must be separated by comma
monthYear = input('[month] [year]').split()

today = datetime.now()

month = monthYear[0] or monthYear
if len(monthYear) > 1:
  year = monthYear[1]
else:
   year = today.strftime("%Y")

print(month, year)
print(type(month))
#generate plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str= c.formatmonth(int(year), int(month))
print(str)





# month, year = input('[month] [year]').split(',')
# print(month)
# print(year)5
today = datetime.today()
print(type(today))
#print(str(today[6:9]))

#get year-month-time
today = datetime.now()
#turn datetime into a string and pull out year
print(today.strftime("%Y"))

#month, year = input().split(',')





# theyear = 2020
# themonth = 5
# c = calendar.formatmonth(theyear, themonth, withyear=True)
# print(c)
# year = 2020
# month = 4
# day = 9
# c = calendar.weekday(year, month, day)
# print(c)
