'''
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

P:
input: list
output: (nested) list

- function takes a list as an argument
- split the list 
- first half goes into the first element of the returned list
- second half goes into the second element of the returned list
- if list is odd numbered, middle item goes in first element list
- if list contains only one item, return populated first element and empty second element
- if empty list, return two empty elements

D:
- lists

A:
- error check for empty list
- error check for list of one item only
- determine is list length is even or odd

'''

def halvsies(lst):
    length = len(lst)
    halfway_point = (length + 1) // 2

    first_half = lst[:halfway_point]
    second_half = lst[halfway_point:]

    return [first_half, second_half]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])