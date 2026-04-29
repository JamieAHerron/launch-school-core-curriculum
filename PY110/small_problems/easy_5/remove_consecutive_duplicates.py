'''
P:
input: integer list
output: integer list 

- take list of integers as argument
- return integer list with only initial occurence of each integer

A:
- create result list - assign to first number in list
- create current_number variable assigned to first number in list
- iterate over list
- if number not equal to current number, append to list
- reassign current_number to number that was just appened to list
- repeat process
- return result list
'''

def unique_sequence(lst):
    if not lst:
        return []
    
    result = [lst[0]]
    current_number = lst[0]

    for num in lst[1:]:
        if num != current_number:
            result.append(num)
            current_number = num
    
    return result

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True
