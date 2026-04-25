'''
Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

P:
input: integer
output: list

- take integer as argument
- return list
- list contains all integers between 1 and argument (inclusive)
- must be in ascending order
- argument will always be positive integer

D:
- list

A:
- create list comprehension and return
- use range to iterate from 1 to (argument + 1)
'''

#Code:

def sequence(num):
    return [num for num in range(1, (num + 1))]
    #or list(range(1, (num + 1)))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True