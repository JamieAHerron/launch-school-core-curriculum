'''
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:

P:
input: list (of integers)
output: list (of sorted integers)

- take a list of integers as an argument (between 0 and 19)
- return sorted list
- sort based on the english spelling of each number

Questions:
- do we mutate the list in place or make a new list?
(Assume a new list, unless told otherwise)

A:
- take list as argument
- make list comprehension
- sort list comprehension based on spelling of numbers 
***Helper function***
- create helper function for sorting key in sort
- create dictionary with integer numbers matching spelled number values
- return spelled number
***
- return sorted list
'''

#Code:

#Helper function to use as key in sort
def number_to_alphabet(num):
    #dictionary can be moved outside to a constant, then the function can simply be return NUMBER_SPELLINGS[num]. Also, a list can also work for this solution
    number_spellings = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }

    return number_spellings[num]

def alphabetic_number_sort(lst):

    return sorted(lst, key=number_to_alphabet)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True