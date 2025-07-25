#Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

def remove_non_letters(word):
    alpha_word = ''
    for char in word:
        if char.isalpha():
            alpha_word += char
    return alpha_word

def word_sizes(string):
    result = {}
    word_list = string.split()

    for word in word_list:
        alpha_word = remove_non_letters(word)
        if len(alpha_word) == 0:
            continue
        
        result[len(alpha_word)] = result.get(len(alpha_word), 0) + 1
    
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

print(word_sizes('---') == {})
