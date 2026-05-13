'''
Write a function that takes a lowercase string as input and returns the length of the longest substring that consists entirely of vowels (a, e, i, o, u).

- take a string as an argument
- create sub_count and total_count variables, initialize to 0
- create vowels variable, initialize to string of vowels
- iterate over string
- if char in vowels, increment sub_total by one
- if char not in vowels, set sub_total to 0
- if sub_total is great than total, reassign total to sub_totals value
- return total 
'''

def solve(string):
    total_count = 0
    sub_count = 0
    vowels = 'aeiou'

    for char in string:
        if char in vowels:
            sub_count += 1
        else:
            sub_count = 0
        if sub_count > total_count:
            vowel_count = sub_count
    
    return total_count 

print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3)