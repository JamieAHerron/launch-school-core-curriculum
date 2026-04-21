'''
Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

P:
input: (two) lists
output: (new) list

- take two lists as arguments 
- return new list
- new list contains all elements from both list arguments
- each element alternates
- both argument lists are non-empty
- both argument lists have the same number of elements
'''

#Code:

#LS Solution suggestion
# def interleave(lst1, lst2):
#     result = []

#     for a, b in zip(lst1, lst2):
#         result.extend([a, b])

#     return result



def interleave(lst1, lst2):
    result = []

    for i in range(len(lst1)):
        result.append(lst1[i])
        result.append(lst2[i])
    
    return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
