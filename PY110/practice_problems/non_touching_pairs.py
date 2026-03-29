# Write a function that takes a list of integers as input and counts the number of non-touching pairs in the list. A non-touching pair is defined as two equal integers separated by some other integer(s).

def non_touching_pairs(lst):
    count = 0

    for i in range(len(lst)):
        for j in range(i + 2, len(lst)):
            if lst[i] == lst[j]:
                count += 1
    
    return count // 2

print(non_touching_pairs([1, 2, 5, 6, 5, 2])) # 1
print(non_touching_pairs([1, 2, 2, 20, 6, 20, 2, 6, 2])) # 3