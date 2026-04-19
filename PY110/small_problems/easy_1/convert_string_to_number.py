'''
P: 
Input: string (of numbers)
output: integer

- take string number as argument
- convert string number to integer number
- cannot use standard conversion methods 
- No consideration for + or - signs, invalid characters, all characters are numeric

Questions:
- consider empty strings? Assume all string arguments are populated

D:
- dictionary

A:
- create a dictionary to map string numbers to integer numbers
- iterate over string number
- for each string digit, grab the corresponding integer value
- have avalue variable set to 0
- value is value multiplied by 10 plus digit
- return value

***Next steps: hex version***

Write a hexadecimal_to_integer function that converts a string representing a hexadecimal number to its integer value. Hexadecimal numbers use base 16 instead of 10, and the characters A, B, C, D, E and F (and the lowercase equivalents) correspond to decimal values of 10-15.
'''

def hexadecimal_to_integer(s):

    num_dict = {
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
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    value = 0
    for char in s:
        if char.isalpha():
            digit = num_dict[char.upper()]
            value = value * 16 + digit
        else:
            digit = num_dict[char]
            value = value * 16 + digit
    
    return value

print(hexadecimal_to_integer('4D9f') == 19871)  # True