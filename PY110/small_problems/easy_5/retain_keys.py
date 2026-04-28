'''
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

P:
input: dictionary, list
output: dictionary

- take dictionary and list of keys as arguments
- return new dictionary that contains only the keys from the list

D:
- dictionary

A:
- create empty dictionary result
- iterate over list
- check if key in dictionary
- if key in dictionary, add it to dictionary result 
- return dictionary 
'''

def keep_keys(items, lst):
    #LS more concise solution 
    #return {key: items[key] for key in lst if key in items}

    result = {}

    for key in lst:
        if key in items:
            result[key] = items[key]
    
    return result

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True