# Scenario
# We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some
# specific expectations.

# Read them carefully as the class you're about write will be used to launch rockets carrying international
# missions to Mars. It's a great responsibility. We're counting on you!

# Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from
# range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range
# [0..59]).

# Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

# The class itself should provide the following facilities:
# - objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into
# strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
# - the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing
# the time stored inside objects by +1/-1 second respectively.

# Use the following hints:

# - all object's properties should be private;
# - consider writing a separate function (not method!) to format the time string.
from time import sleep


class Timer:
    # use lists to loop through seconds, minutes and hours
    __seconds__ = [i for i in range(60)]
    __minutes__ = [i for i in range(60)]
    __hours__ = [i for i in range(24)]

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f"{hh}:{mm}:{ss}"

    def __next_hour__(self):
        idx = Timer.__hours__.index(self.hours)
        # if we're at the last second in the hours list
        if idx == (len(Timer.__hours__) - 1):
            # start at the beginning again
            self.hours = Timer.__hours__[0]
        else:
            self.hours = Timer.__hours__[idx + 1]

    def __next_minute__(self):
        idx = Timer.__minutes__.index(self.minutes)
        # if we're at the last second in the minutes list
        if idx == (len(Timer.__minutes__) - 1):
            # start at the beginning again
            self.minutes = Timer.__minutes__[0]
            self.__next_hour__()
        else:
            self.minutes = Timer.__minutes__[idx + 1]

    def next_second(self):
        idx = Timer.__seconds__.index(self.seconds)
        # if we're at the last second in the seconds list
        if idx == (len(Timer.__seconds__) - 1):
            # start at the beginning again
            self.seconds = Timer.__seconds__[0]
            self.__next_minute__()
        else:
            self.seconds = Timer.__seconds__[idx + 1]

    def __prev_hour__(self):
        idx = Timer.__hours__.index(self.hours)
        # if we're at the last second in the hours list
        if idx == (len(Timer.__hours__) - 1):
            # start at the beginning again
            self.hours = Timer.__hours__[-1]
        else:
            self.hours = Timer.__hours__[idx - 1]

    def __prev_minute__(self):
        idx = Timer.__minutes__.index(self.minutes)
        # if we're at the last second in the minutes list
        if idx == 0:
            self.minutes = Timer.__minutes__[-1]
            self.__prev_hour__()
        else:
            self.minutes = Timer.__minutes__[idx - 1]

    def prev_second(self):
        idx = Timer.__seconds__.index(self.seconds)
        # if we're at the last second in the seconds list
        if idx == 0:
            # start at the beginning again
            self.seconds = Timer.__seconds__[-1]
            self.__prev_minute__()
        else:
            self.seconds = Timer.__seconds__[idx - 1]


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)

# expected output:
# 23:59:59
# 00:00:00
# 00:00:01
# 00:00:00
# 23:59:59
timer2 = Timer()
for i in range(10):
    timer.next_second()
    print(timer)
    sleep(1)
