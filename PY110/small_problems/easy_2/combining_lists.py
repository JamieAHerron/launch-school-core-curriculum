'''
Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

P:
Input: (2) lists
Output: set

- function takes two lists as arguments
- return set that is union of the values from both lists
- both arguments will always be lists 

Questions:
- What about empty lists? 

D:
- set

A:
- convert lists to sets
- perform union method
- return result

'''

#Code:

def union(lst1, lst2):

    return set(lst1) | set(lst2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True