'''
P:
input: 2 integers (row of digits, no. of nums to rotate)
output: integer

- take integer as argument (row of digits and how many digits to rotate)
- rotate said number of digits at the end of the digit row
- return new, rotated row of digits

D:
- integers, strings

A:
- convert row of digits integer to string
- slice end digits based on second integer argument
- assign slices (first part and rotated part) to variables
- use helper function for 'rotated part'
- return rotated digits
- return 'first part' joined with 'rotated part'
'''

def rotate_digits(digits):
    return digits[1:] + digits[0]

def rotate_rightmost_digits(digit_number, num):
    str_digit_row = str(digit_number)
    unrotated_section = str_digit_row[:-num]
    rotated_section = rotate_digits(str_digit_row[-num:])

    return int(unrotated_section + rotated_section)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True