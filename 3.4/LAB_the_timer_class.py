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
import json

from time import sleep
from enum import Enum
from sorcery import dict_of


class TimeUnit(Enum):
    HOURS = 'hours'
    MINUTES = 'minutes'
    SECONDS = 'seconds'
    UNITS = ['seconds', 'minutes', 'hours', ]


class Deviation(Enum):
    FORWARDS = 1
    BACKWARDS = -1


class Timer:
    # use lists to loop through seconds, minutes and hours
    __sixty__ = [i for i in range(60)]
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

    def __deviate_time__(self, unit=TimeUnit.SECONDS, deviation=Deviation.FORWARDS):
        if type(unit) != TimeUnit:
            raise TypeError('"unit" must be a TimeUnit Enum')
        if type(deviation) != Deviation:
            raise TypeError('"deviation" must be a Deviation Enum')

        unit = unit.value
        time_units = TimeUnit.UNITS.value
        base = Timer.__sixty__ if unit != TimeUnit.HOURS.value else Timer.__hours__
        self_unit = getattr(self, unit)
        idx = base.index(self_unit)
        limit = len(base) - 1 if deviation == Deviation.FORWARDS else 0
        unit_idx = time_units.index(unit)
        next_unit = TimeUnit(
            time_units[unit_idx + 1]) if unit_idx < len(time_units) - 1 else None

        # if we're at the end of a cycle
        if idx == limit:
            if deviation == Deviation.FORWARDS:
                # start at the beginning of the cycle again
                setattr(self, unit, base[0])
            else:
                # go to end of cycle
                setattr(self, unit, base[-1])

            # increment the next unit if there is one
            if next_unit:
                self.__deviate_time__(next_unit, deviation=deviation)
        else:
            setattr(self, unit, base[idx + deviation.value])

    def next_second(self):
        self.__deviate_time__()

    def prev_second(self):
        self.__deviate_time__(deviation=Deviation.BACKWARDS)


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
