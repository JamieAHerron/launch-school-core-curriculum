#Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

def union(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)

    unified_set = set1.union(set2)

    return unified_set


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True