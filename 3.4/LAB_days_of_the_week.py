# Scenario
# Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact
# that objects of that class will be able to store and to manipulate the days of the week.

# The class constructor accepts one argument – a string. The string represents the name of the day of the week and the
# only acceptable values must come from the following set:

# Mon Tue Wed Thu Fri Sat Sun

# Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it
# yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the
# following facilities:

# - objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings
# of the same form as the constructor arguments;
# - the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an
# integer number and updating the day of week stored inside the object in the way reflecting the change of date by the
# indicated number of days, forward or backward.
# - all object's properties should be private;
from math import floor
class WeekDayError(Exception):
    pass


class Weeker:
    __days__ = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', ]

    def __init__(self, day):
        if day not in Weeker.__days__:
            raise WeekDayError()

        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        # today + 7 days = same day
        # n / 7 = num weeks in future (same day)
        # x = n - floor(n - 7) = days ahead of same day in that week
        # new day index = current day index + x
        days_ahead = n - 7 * floor(n / 7)
        day_idx = Weeker.__days__.index(self.day)
        new_day_index = day_idx + days_ahead
        new_day = Weeker.__days__[new_day_index]
        self.day = new_day

    def subtract_days(self, n):
        raise NotImplementedError('subtract_days method has not been implemented')


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")


# Expected output
# Mon
# Tue
# Sun
# Sorry, I can't serve your request.
