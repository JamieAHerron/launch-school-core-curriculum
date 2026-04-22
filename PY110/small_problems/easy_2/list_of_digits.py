'''
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

P:
input: integer
output: list of digits

D:
- list

A:
***DID NOT COMPLETE ALGORITHM
- convert integer to string
'''

#Code

def digit_list(num):
    return [int(digit) for digit in str(num)]
    # LS suggestion for practice using arithmetic
    # original_num = num
    # result = []
    # while original_num > 0:
    #     result.append(original_num % 10)
    #     original_num //= 10
    
    # return result[::-1]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True