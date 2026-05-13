'''
P:
input: string
output: list 

- take a string as an argument
- return a list of the top 3 words 
- top 3 most occuring words, in descending order
- A "word" consists of one or more letters (a-z), and can optionally include apostrophes.
- a string of apostrophes only is not a valid word
- should be case insensitive
- top 1 or top 2 words should be returned if list of words is less than 3
- empty list returned if no valid words

D:
- strings, lists

A:
- create empty dictionary, initialize to a variable word_counts
- initialize current_word variable and assign it to and empty string
- iterate over chars in lowercased string 
    - as long as string is letter or apostrophe, append to current_word 
    - once a space or different char is encountered, the current word has ended
    - check word is not just a string of apostrophes (len(current_word) * ' == current_word) AND not empty
    - add that word to word_counts dictionary (or increment count)
    - reset current_word to empty string

- **After the loop**, perform one final check for the last word:
  - If `current_word` is not empty AND is not just apostrophes:
    - Add `current_word` to `word_counts` (or increment its count).

###Getting the top 3
- convert word_count dictionary key value pairs into list of tuple pairs 
- sort list of tuple pairs by count in descending order
- create new empty list for results
- extract word from top 3 (use range to limit it to top 3?)
- return list of results
'''
def update_counts(word, counts):
    if word and word != "'" * len(word):
        counts[word] = counts.get(word, 0) + 1

def get_count(item):
    return item[1]

def top_3_words(string):
    word_counts = {}
    current_word = ''
    viable_chars = "abcdefghijklmnopqrstuvwxyz'"

    for char in string.lower():
        if char in viable_chars:
            current_word += char
        else:
            update_counts(current_word, word_counts)
            current_word = ''
    update_counts(current_word, word_counts)

    result = sorted([(key, value) for key, value in word_counts.items()], key=get_count, reverse=True)

    return [item[0] for item in result][:3]

print(top_3_words(" , e .. ")) # ["e"]
print(top_3_words(" ... ")) # []
print(top_3_words(" ' ")) # []
print(top_3_words(" ''' ")) # []
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")) # should return ["a", "of", "on"]