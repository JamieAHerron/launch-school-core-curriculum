# Write a function that takes a string as input and counts the occurrences of each lowercase letter in the string. Return the counts in a dictionary where the letters are keys and their counts are values.

def letter_count(string):
    result = {}

    for letter in string:
        if letter.islower():
            result[letter] = result.get(letter, 0) + 1
    
    return result

print(letter_count('launchschool')) #=> { 'a': 1, 'c': 2, 'h': 2, 'l': 2, 'n':1, 'o': 2, 's':1, 'u': 1 }