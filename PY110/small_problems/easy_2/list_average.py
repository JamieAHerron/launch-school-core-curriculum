'''
Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.

P:
input: list (of integers)
output: integer

- take a list of integers as argument
- return average of all integers in list
- average is rounded down to the nearest integer
- list will never be empty
- numbers always positive integers 

D:
- lists

A:
- sum the contents of the list
- divide the total by the number of items in the list
- convert the result to an integer 
- return result 
'''

#code: 

def average(lst):

    #LS cleaner version
    return sum(lst) // len(lst)

    # average_float = sum(lst) / len(lst)
    # average_integer = int(average_float)

    # return average_integer

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True