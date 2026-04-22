'''
P:
input: list
output: string

- count number of occurrences of each element in given list
- print each element alongside number of occurrences
- words are case sensitive

D:
- dictionary (?)

A:
- create empty dictionary
- iterate over given list
- use setdefault to populate dictionary with words as keys, counts as values
- iterate over dictionary to print results
'''

#Code:

def count_occurrences(lst):
    word_count_dict = {}

    for word in lst:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
    
    for key, value in word_count_dict.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2