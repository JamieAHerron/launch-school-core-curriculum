'''
P:
input: list
output: (new) list

- take a list as argument
- rotate list by moving first element to end of list
- do not modify original list
- return new list
- if list contains one item, return that one item in list
- if input empty list, return empty list
- if input is not a list, return None

D:
- lists

A:
# error checking
- check for empty list as argument, return empty list 
- check for list with one element, return copy
- check if argument given is list, if not, return none
# solution
- take list as argument 
- make deep copy
- pop first element from list, store in variable 
- append to end of list
- return list
***could use slicing but that may cause problems with nested iterables and slicing creating only shallow copy, so deep copy is preferred***
'''
import copy

def rotate_list(lst):
    #error checking
    if not isinstance(lst, list):
        return None
    if lst == []:
        return [] 
    
    lst_copy = lst[:]
    rotated_copy = lst_copy[1:] + lst_copy[:1]

    return rotated_copy


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])