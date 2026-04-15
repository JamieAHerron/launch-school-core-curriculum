'''
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

P:
Input: list (of integers)
output: list

- take a list of numbers as argument
- return list with same number of elements
- each element is the running total of original list
- empty list return empty list
- list with one number returns that number

Questions:
- should the original list be mutated? Assume no

D:
- list

A:
- if list given is an empty lsit, return empty list
- if list given has one element, return list as-is
- create new empty list
- iterate over original list (range?)
- if new list is empty, add element to list (first element)
- if element already in new list, add current element to new list 
- when adding new element, add that number to number at the end of new list
- return new list
'''

#Code:

def running_total(lst):
    result = []
    running_total = 0 

    for num in lst:
        running_total += num
        result.append(running_total)
    
    return result


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True