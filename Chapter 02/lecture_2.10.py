'''Topic: Different way to import a libray'''

import calendar                         # here it only import the calendar library in this program

print(calendar.month(2025,1))
print(calendar.calendar(2026))

# 2nd way to import library
from calendar import *                  # here it import all the function from calendar library in this program

print(calendar(2023))
print(month(2000,12))

# 3rd way to import library
from calendar import month              # here it import only "month" function if we want to use "celender function it generate ERROR"

print(month(2001,3))

# To do that
from calendar import month, calendar    # Now it will work on "month and calendar" function of this library

print(month(2012,1))
print(calendar(1998))

# 4th way to import library as in a "variable"
import calendar as d                     # here the whole calendar library is import as variable "d", this help to reduce the time by typing full name

print(d.month(2012,3)) 

# this also perform as
from calendar import month as m

print(m(1947,8))
