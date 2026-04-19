'''
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes

P:
input: string
output: dictionary

- accept a string of zero or more space-seperated words
- return dictionary showing number of words of different sizes 
- non-alphabetical chars considered NOT in word
- empty string returns empty dictionary 

D:
- dictionary 

A:
- seperate string by spaces
- iterate over list of words
- iterate over characters in said word
- determine if character is alphabetical 
- count number of alphabetical chars in word
- store number in variable
- use number variable as dictionary key
- number of words of given length as value 
- return dictionary (empty if empty string)

'''

#Code:

def letter_count(word):
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    return count


def word_sizes(word_string):
    result = {}

    for word in word_string.split():
        size = letter_count(word)
        if size == 0:
            continue
        result[size] = result.get(size, 0) + 1
    return result

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})