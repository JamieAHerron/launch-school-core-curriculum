# Write a function that takes a list of words and constructs a new word by concatenating the nth letter from each word, where n is the position of the word in the list. Ignore if the nth letter from the word does not exist.

def nth_char(lst):
    new_word = ''

    for index, word in enumerate(lst):
        if index < len(word):
            new_word += word[index]
    
    return new_word


print(nth_char(['yoda', 'best', 'has'])) # 'yes'
print(nth_char(['hello', 'hello', 'hello', 'hello', 'hello', 'no'])) # 'hello'