'''
Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

P:
input: list 
output: string

- take list of positive integers as input
- multiply all integers together
- divide the result by the number of entries in list
- return result as string to three decimal places

D:
-list
- strings

A:
- create result variable initialized to 0 
- iterate over list
- multiply item by current result amount
- divide result by length of original list
- return number as f-string with three decimal place formatting 
'''

#Code:
def multiplicative_average(lst):
    running_total = 1

    for num in lst:
        running_total *= num
    
    result = running_total / len(lst)

    return f'{result:.3f}'
    


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")