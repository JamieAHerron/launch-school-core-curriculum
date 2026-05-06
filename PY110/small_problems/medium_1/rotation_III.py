'''
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

Num: 735291
R1: 352917
R2: 329175
R3: 321759
R4: 321597
R5: 321579
'''

def rotation(string_num):
    return string_num[1:] + string_num[0]

def rotate_rightmost_digits(digits, num):
    string_digits = str(digits)
    rotated_part = string_digits[-num:]
    original_part = string_digits[:-num]
    result = original_part + rotation(rotated_part)
    return int(result)

def max_rotation(num):
    num_digits = len(str(num))
    for count in range(num_digits, 1, -1):
        num = rotate_rightmost_digits(num, count)

    return num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True