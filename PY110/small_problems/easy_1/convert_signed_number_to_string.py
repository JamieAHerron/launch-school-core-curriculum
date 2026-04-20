'''
Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.
P:
Input: integer
Output: string
'''

def integer_to_string(num):

    result = ''
    digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if num == 0:
        return '0'

    while num > 0:
        digit = num % 10
        result = digit_list[digit] + result
        num //= 10
    
    return result

def signed_integer_to_string(number):

    if number == 0:
        return integer_to_string(number)
    elif number < 0:
        return f'-{integer_to_string(-number)}'
    else:
        return f'+{integer_to_string(number)}'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True