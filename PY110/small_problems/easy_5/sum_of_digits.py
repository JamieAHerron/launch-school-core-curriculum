'''
Write a function that takes one argument, a positive integer, and returns the sum of its digits.

input: integer
output: integer

A:
- convert integer to string
- iterate overstring, converting each character back to a single digits
- sum the contents of the list

'''

#code:

def sum_digits(num):
    
    return sum(int(char) for char in str(num))

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True