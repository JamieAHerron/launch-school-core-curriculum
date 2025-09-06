'''
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

input: list
output: list (containing two lists)

Explicit requirements:
    - take a list as input
    - check if the number of items are even or odd
    - divide input list into two seperate lists
    - if odd number, place middle item in first list
    - return list with two nested lists (original items divided)

Implicit requirements:
    - if list is empty, return two empty lists
    - if only one item, return one populated list and one empty list

'''
def split_list(lst, index):
    lst1 = lst[:index]
    lst2 = lst[index:]
    result = [lst1, lst2]

    return result

def halvsies(lst):
    if len(lst) % 2 == 0:
        split_index = int(len(lst) / 2)
        result = split_list(lst, split_index)
    else:
        split_index = int((len(lst) + 1) / 2)
        result = split_list(lst, split_index)

    return result

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])