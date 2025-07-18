# python

# Exercise: Text Analysis Tool

def analyze_text(text):
    """
    Analyze the given text and return various information about it.
    
    Args:
    text (str): The input text to analyze
    
    Returns:
    dict: A dictionary containing various analyzed information
    """
    analyzed_info = {}
    lower = text.casefold()
    stripped = lower.strip()
    word_list = stripped.split()

    analyzed_info['lower'] = lower
    analyzed_info['stripped'] = stripped
    analyzed_info['word_list'] = word_list
    analyzed_info['count'] = lower.count('python')
    analyzed_info['replace'] = lower.replace('difficult', 'challenging')
    analyzed_info['word_lengths'] = [len(word) for word in word_list]
    analyzed_info['more_than_5'] = sum(1 for word in word_list if len(word) > 5)
    analyzed_info['word_dict'] = {word:len(word) for word in word_list}
    analyzed_info['programming_find'] = lower.find('programming')

    return analyzed_info

    # Implement the following operations:
    
    # 1. Convert the text to a standardized case
    # 2. Remove any leading or trailing spaces
    # 3. Create a list of words from the text
    # 4. Count how many times the word "python" appears (case-insensitive)
    # 5. Replace all occurrences of "difficult" with "challenging"
    # 6. Create a list of the lengths of each word
    # 7. Count how many words are longer than 5 characters
    # 8. Create a dictionary where keys are words and values are their lengths
    # 9. Find the position of the first occurrence of "programming"
    # 10. Create a string with all vowels removed
    
    # Return the results in a dictionary

# Test the function
sample_text = """
    Python is a versatile programming language. 
    It's great for beginners and experts alike. 
    Python can be used for web development, data analysis, and more!
    Some find programming difficult, but practice makes perfect.
"""

result = analyze_text(sample_text)

# Print results
for key, value in result.items():
    print(f"{key}: {value}")

# Additional tasks:
# 1. Print the first 10 characters of the original text
print(sample_text[0:11])
# 2. Use a conditional expression to print whether the text is "long" (more than 100 characters) or "short"
print('long' if len(sample_text) > 100 else 'short')
# 3. Check if the 'word_count' in the result is an integer
# 4. Create a summary string using string formatting 

