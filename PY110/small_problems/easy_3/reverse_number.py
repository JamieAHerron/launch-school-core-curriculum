'''
Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

P: 
input: integer
output: integer (reversed)

- take integer as argument
- reverse said integer 
- return reversed version of integer argument 

D:
- integers/ strings

A:
- convert integer to strings
- reverse string using slicing
- convert reversed string back to integer 
- return reversed integer 
'''

#Code:

def reverse_number(num):
    string_num = str(num)
    reversed_string_num = string_num[::-1]
    reversed_num = int(reversed_string_num)

    return reversed_num

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True