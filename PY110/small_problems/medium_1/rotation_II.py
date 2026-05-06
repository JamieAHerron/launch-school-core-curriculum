'''
P:
input: integer, integer
output: integer

- take an integer as an argument and a second integer
- second integer rotates X number of final digits

D:
- integers

A:
- convert integer to string
- slice part of string to be manipulated (and part to remain the same)
- send part to be rotated to rotation helper function
- return original part and return value from helper function (converted to integer)
'''

def rotation(string_num):
    return string_num[1:] + string_num[0]

def rotate_rightmost_digits(digits, num):
    string_digits = str(digits)
    rotated_part = string_digits[-num:]
    original_part = string_digits[:-num]
    result = original_part + rotation(rotated_part)
    return int(result)



print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True