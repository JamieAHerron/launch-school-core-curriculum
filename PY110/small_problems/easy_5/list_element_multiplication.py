'''
Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

P:
input: (2) lists
output: (new) list

- take two lists as arguments 
- return new list
- each element is the product of the corresponding elements from the two lists

D:
- lists

A:
- liost comprehension 
- iterate over both lists at the same time using a range
- multiply each corresponding item 
- return new list 
'''

#code:

def multiply_items(lst1, lst2):
    #Zip is the way to go! Consider it next time
    return [lst1[i] * lst2[i] for i in range(len(lst1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True