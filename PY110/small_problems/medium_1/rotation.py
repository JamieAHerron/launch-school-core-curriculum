'''
P:
input: list
output: (rotated) list

- take a list as an argument
- rotate the list by moving the first element to the end
- do not modify the original list
- return new list

D:
-lists

A:
- set up check for empty list, return empty list
- if not a list, return None
- slice original list into two parts (first element + remaining elements)
- return slices joined together in required order (first element last)
'''

def rotate_list(lst):

    if not isinstance(lst, list):
        return None
    if lst == []:
        return []
    
    first_element = lst[:1]
    remaining_elements = lst[1:]

    return remaining_elements + first_element


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