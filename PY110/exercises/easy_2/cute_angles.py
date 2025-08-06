'''
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Input: float (0-360)
Output: string (degrees, minutes, seconds)

Explicit requirements:
    - input a floating point number
    - return string that represents
        - the angle (in degrees)
        - minutes (using single quote)
        - seconds (using double quote)
    - 60 minutes in a degree 
    - 60 seconds in a minute

Implicit requirements:
    - extract degrees (left of float decimal point)
    - extract minutes (right of float decimal point * 60)
    - extract seconds (fractional part of minutes * 60)

Considerations:
    - How best to convert floats to strings?
    - What is the best data type? (building a string/ joining a list, etc.)
    - How to deal with input that is more/ less than 0/360?


Note: You can use the following constant to represent the degree symbol:
'''
DEGREE = "\u00B0"

def add_zero(number):
    if number < 10:
        return '0' + str(number)
    else:
        return number

def dms(num):
    degrees = int(num)
    minutes_float = (num - degrees) * 60
    minutes = int(minutes_float)
    seconds_float = (minutes_float - minutes) * 60
    seconds = int(seconds_float)



    return f"{degrees}{DEGREE}{add_zero(minutes)}'{add_zero(seconds)}\""


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")