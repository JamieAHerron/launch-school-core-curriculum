'''
In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.
'''

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(integer):
    result = ''

    while integer > 0:
        integer, remainder = divmod(integer, 10)
        result = NUMBERS[remainder] + result
    
    return result or "0"

def signed_integer_to_string(num):
    if num < 0:
        return f"-{integer_to_string(-num)}"
    elif num > 0:
        return f"+{integer_to_string(num)}"
    else:
        return "0"


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True