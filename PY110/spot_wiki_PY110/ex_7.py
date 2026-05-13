'''
Write a function that takes a list of words and constructs a new word by concatenating the nth letter from each word, where n is the position of the word in the list. Ignore if the nth letter from the word does not exist.

- take word lst as argument
- initialize result variable to empty string
- iterate over word lst using enumerate
- if word length is greater than respective index number, concatenate letter via index number to result string
- return result string once iteration is complete 
'''
def nth_char(word_lst):
    result = ''

    for index, word in enumerate(word_lst):
        if len(word) > index:
            result += word[index]
    
    return result


print(nth_char(['yoda', 'best', 'has'])) # 'yes'
print(nth_char(['hello', 'hello', 'hello', 'hello', 'hello', 'no'])) # 'hello'