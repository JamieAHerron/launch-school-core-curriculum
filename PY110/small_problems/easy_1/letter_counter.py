'''
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes

P:
input: string
output: dictionary

- accept a string of zero or more space-seperated words
- return dictionary showing number of words of different sizes 
- non-alphabetical chars considered in word
- empty string returns empty dictionary 

D:
- dictionary 

A:
- seperate string by spaces
- iterate over list of words 
- count number of chars in word
- use word length as dictionary key
- number of words of given length as value 
- return dictionary (empty if empty string)

'''

#Code:

def word_sizes(word_string):
    word_list = word_string.split()
    result = {}

    for word in word_list:
        result[len(word)] = result.get(len(word), 0) + 1
    
    return result

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})