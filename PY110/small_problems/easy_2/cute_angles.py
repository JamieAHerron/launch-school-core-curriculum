'''
Note: You can use the following constant to represent the degree symbol:

DEGREE = "\u00B0"

P:
Input: float
output: string

- function takes floating point as argument
- floating point represents angle between 0 and 360
- return string representing that angle in degrees, minutes, and seconds
- Use a degree symbol (°) to represent degrees
- Use a single quote (') to represent minutes
- Use a double quote (") to represent seconds
- 60 minutes in a degree, 60 seconds in a minutes

D:
- string

A:
- get degree part by converting to integer 
- deduct integer part from original float
- multiply result with 60 for minutes 
- deduct that answer from original float 
- multiply by 60 for seconds 

'''

#Code:
DEGREE = "\u00B0"

def leading_zero(n):
    string_num = str(n)
    if len(string_num) < 2:
        return f'0{string_num}'
    else:
        return string_num

def dms(num):
    degrees = int(num)

    total_minutes_float = (num - degrees) * 60
    minutes_int = int(total_minutes_float)

    seconds_int = int((total_minutes_float - minutes_int) * 60)

    return (f"{degrees}{DEGREE}"
            f"{leading_zero(minutes_int)}'"
            f'{leading_zero(seconds_int)}"')

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
