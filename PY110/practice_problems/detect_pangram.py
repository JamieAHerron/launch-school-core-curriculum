# A pangram is a sentence that contains every single letter of the alphabet at least once. Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def pangram(string):
    string_lower = string.lower()
    letter_set = {letter for letter in string_lower if letter.isalpha()}
    return len(letter_set) >= 26

print(pangram("The quick brown fox jumps over the lazy dog.")) # should return True
print(pangram("This is not a pangram.")) # should return False