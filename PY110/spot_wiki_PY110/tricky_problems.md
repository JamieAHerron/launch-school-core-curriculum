# PY110
## Problem 3: Count Substring Instances

Write a function that takes two strings as input, `full_text` and `search_text`,
and returns the number of times `search_text` appears in `full_text`.

## Examples:

```python
solution('abcdeb','b') # should return 2 since 'b' shows up twice
solution('aaabbbcccc', 'bbb') # should return 1
solution('aaabbbbcccc', 'bbb') # should return 2
```

<details>
<summary>Solution:</summary>

```python
def solution(full_text, search_text):
    count = 0
    start = 0
    while True:
        pos = full_text.find(search_text, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count
```

</details>

## Problem 4: Detect the Pangram

A pangram is a sentence that contains every single letter of the alphabet at
least once. Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.

## Examples:

```python
pangram("The quick brown fox jumps over the lazy dog.") # should return True
pangram("This is not a pangram.") # should return False
```

<details>
<summary>Solution:</summary>

```python
def pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string_lower = string.lower()
    
    for letter in alphabet:
        if letter not in string_lower:
            return False
    
    return True
```

</details>

## Problem 5: Longest Chain of Vowels

Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists entirely of vowels (a, e, i, o, u).

## Examples:

```python
solve("roadwarriors") # should return 2
solve("suoidea") # should return 3
```

<details>
<summary>Solution:</summary>

```python
def solve(string):
    vowels = 'aeiou'
    max_length = 0
    current_length = 0
    
    for char in string:
        if char in vowels:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    
    return max_length
```

</details>

## Problem 7: The Nth Char

Write a function that takes a list of words and constructs a new word by
concatenating the nth letter from each word, where n is the position of the
word in the list. Ignore if the nth letter from the word does not exist.

## Examples:

```python
nth_char(['yoda', 'best', 'has']) # 'yes'
nth_char(['hello', 'hello', 'hello', 'hello', 'hello', 'no']) # 'hello'
```

<details>
<summary>Solution:</summary>

```python
def nth_char(words):
    result = ''
    for index, word in enumerate(words):
        if index < len(word):
            result += word[index]
    return result
```

</details>

## Problem 8: Smallest Substring Repeat

Write a function that takes a non-empty string `s` as input and finds the
minimum substring `t` and the maximum number `k`, such that the entire string
`s` is equal to `t` repeated `k` times.

## Examples:

```python
smallest_repeated_substring("ababab")        # ["ab", 3]
smallest_repeated_substring("aaaaaa")        # ["a", 6]
smallest_repeated_substring("abcabcabc")     # ["abc", 3]
smallest_repeated_substring("xyz")           # ["xyz", 1]
smallest_repeated_substring("zzzzzzzzzz")    # ["z", 10]
smallest_repeated_substring("ababababx")     # ["ababababx", 1]
smallest_repeated_substring("abcdabcd")      # ["abcd", 2]
smallest_repeated_substring("abaaba")        # ["aba", 2]
smallest_repeated_substring("a")             # ["a", 1]
```

<details>
<summary>Solution:</summary>

```python
def smallest_repeated_substring(s):
    for length in range(1, len(s) + 1):
        substring = s[:length]
        count = len(s) // length
        if substring * count == s:
            return [substring, count]
```

</details>