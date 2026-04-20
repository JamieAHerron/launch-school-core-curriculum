'''
Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number

P:
Input: integer
Output: string

- take non-negative integer as argument
- convert integer value to a string
- return string

D:
- list (of individual integers)
- dictionary
- string (to be returned)

A:
- create dictionary with integers as keys and string equivalents as values
- create empty string to build the result for return
- parse integer into individual digits using while loop
- place individual digits into list object 
- iterate over integer list
- for each integer, access respective key in dict and build string equivalent
- return string equivalent 
'''

#Code:

def integer_to_string(num):

    number = num
    result = ''
    digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if num == 0:
        return '0'

    while number > 0:
        digit = number % 10
        result = digit_list[digit] + result
        number //= 10
    
    return result


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True