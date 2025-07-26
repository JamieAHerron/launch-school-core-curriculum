'''
In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.
'''

def string_to_integer(string):
    numbers = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    result = 0
    for char in string:
        result = (result * 10) + numbers[char]

    return result

def string_to_signed_integer(string):
    if string[0] == '+':
        string_number = string[1:]
        int_number = string_to_integer(string_number)
        return int_number
    elif string[0] == '-':
        string_number = string[1:]
        int_number = string_to_integer(string_number)
        negative_int_number = int_number - (int_number * 2)
        return negative_int_number
    else:
        int_number = string_to_integer(string)
        return int_number

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True