'''
Sort Strings by Most Adjacent Consonants

Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

Input: List (of strings)
Output: List (of organized strings by adjacent consonants)

Explicit rules:
 - Sort list by highest number of adjacents consonants 
 - return sroted list
 - strings with same number of adjacent consonants must retain order in relation to each other
 - Adjacent consonants - next to each other OR space between two consonants in adjacent words (within that string object)

Implicit rules:
 - List can only contain strings

Quiestions:
 - What if string contains no adjacent consonants? 
 - What if the string contains no consonants?
 - How do we handle incorrect input?
 - How to check/sort if there is a space between two consonants in adjacent words?
 - If all strings are 'equal' do they keep their original order or are they organized alphabetically?

 Data Structures:
  - A list will be provided as input
  - A list will be returned
  - Building and empty list based on certain rules may be optimal

Algorithm:
 - Provide list of strings as argument
 - Iterate through list of strings
 - Perform some operation on string object to count adjacent consonants
 - Perform some operation to deal with strings with the same number of adjacent consonants
 - Based on results of said operation, re-organize list (or build a new one)
 - return organized list
'''

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa'] #???

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa'] #???