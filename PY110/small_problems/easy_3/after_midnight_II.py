'''
P:
input: string (24hr time)
output: integer 

- take time of day string (24hr) as argument
- return number of minutes before/ after midnight
- should return integer value within the range of 0 and 1439

D:
- strings/ integers

A:
***AFTER MIDNIGHT***
- extract hours and minutes from time string
- multiply number for hours by 60
- add the above to number of minutes
- return result
'''

MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 24 * MINUTES_PER_HOUR

def after_midnight(time):
    hours, minutes = [int(unit) for unit in time.split(':')]

    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY
    # the % MINUTES_PER_DAY allows us to deal with 24:00 by doing 
    #1440 % 1440 which gives us 0
    
def before_midnight(time):
    minutes_after = after_midnight(time)
    delta_minutes = MINUTES_PER_DAY - minutes_after

    if delta_minutes == MINUTES_PER_DAY:
    #helps to deal with edges cases 00:00 and 24:00
        return 0
    return delta_minutes

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
