'''
Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

P:
input: string
output: list 

- take a string as an argument
- return list of substrings
- order by where in the string the substring begins
- All 0 index substrings first, then index 1 substrings etc.
- return substrings at a given index from shortest to longest

D:
- list

A:
- iterate over string argument
- nested loop to get all substrings
- nested for loops with ranges
- use slicing to get each substring [i:j]
- append slice to new result list
- return result list


'''

#Code:

#I have written in the LS solution for practice
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    results = []
    for idx in range(len(string)):
        string_at_index = string[idx:]
        for substring in leading_substrings(string_at_index):
            results.append(substring)
    
    return results

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True