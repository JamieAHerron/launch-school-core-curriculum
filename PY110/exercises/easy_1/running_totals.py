#Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

'''
Input: List of numbers
Output: List of numbers

Explicit requirements:
    - take a list of numbers as input
    - return list with same number of elements
    - list of numbers returned should be running total

Data structure:
 - list (create a new list)
'''

def running_total(numbers):
    result = []

    for i in range(len(numbers)):
        if not result:
            result.append(numbers[i])
        else:
            result.append(numbers[i] + result[i - 1])
    
    return result



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True