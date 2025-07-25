#Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

#You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

def swap(string):
    word_list = string.split()
    result = ''

    for word in word_list:
        if len(word) == 1:
            result += word + ' '
        elif len(word) == 2:
            result += word[1] + word[0] + ' '
        else:
            result += word[len(word) -1] + word[1:len(word) - 1] + word[0] + ' '
    return result.strip()


print(swap('Oh what a wonderful day it is') 
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True