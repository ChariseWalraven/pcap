# Scenario

# Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the strftime method with the appropriate format to display the following result:

# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44
from datetime import date, datetime

def print_datetime():
    nov_date = datetime.fromisoformat('2020-11-04T14:53:00')
    print(nov_date.strftime("%Y/%m/%d% %H:%M:%S"))
    print(nov_date.strftime("%Y/%B/%d% %H:%M:%S %p"))
    print(nov_date.strftime("%a, %Y %h %d"))
    print(nov_date.strftime("%A, %Y %B %d"))
    print(nov_date.strftime("Weekday: %w"))
    print(nov_date.strftime("Day of the year: %j"))
    print(nov_date.strftime("Week number of the year: %U"))

print_datetime()
