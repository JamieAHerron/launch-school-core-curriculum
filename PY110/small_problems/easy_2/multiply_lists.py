'''
Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

P:
input: (two) lists
output: (new) list

- take two lists of numbers as arguments
- return new list containing product of each respective pair
- arguments always contain same number of elements

D:
- lists

A:
- create new list result
- use zip to create list of tuple pairs from both lists
- iterate over tuple pairs
- multiply each pair
- append to new list
- return new list
'''

#Code:

def multiply_list(lst1, lst2):
    result = []
    #a list comprehension would be even more concise here
    for a, b in zip(lst1, lst2):
        result.append(a * b)
    
    return result

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True