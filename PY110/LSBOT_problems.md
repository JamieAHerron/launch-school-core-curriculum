```python
#Spot Wiki Problem 10 - Most Frequent Words 
def top_3_words(string):
    #Clean the string and get rid of any hyphens
    cleaned_string = ''

    for char in string.lower():
        if char.isalpha() or char == "'":
            cleaned_string += char
        else:
            cleaned_string += " "
    
    #Split cleaned string into word list then make sure all cleaned words are valid (nothing like ''' for example)
    all_words = cleaned_string.split()
    valid_words = []

    for word in all_words:
        if any(char.isalpha() for char in word):
            valid_words.append(word)
    
    #populate dictionary with words and their frequency
    counts = {}
    for word in valid_words:
        counts[word] = counts.get(word, 0) + 1
    
    #Grab top words using sorted and lambda function to sort by freqquency, then using reverse and slicing for top 3
    top3 = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:3]

    #Return list of top 3 words only
    return [item[0] for item in top3]

print(top_3_words(" , e .. ")) # ["e"]
print(top_3_words("hi how are you hi how hi"))
print(top_3_words(" ... ")) # []
print(top_3_words(" ' ")) # []
print(top_3_words(" ''' ")) # []
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, 
a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.""")) # should return ["a", "of", "on"]
```