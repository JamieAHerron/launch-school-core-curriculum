'''
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.

P:
input: dictionary
output: dictionary (inverted)

- take dictionary as argument, both keys and values are unique
- invert dictionary, keys become values and vice-versa 

D:
- dictionary

A:
- itrate over dictionary 
- swap keys and values
- return inverted dictionary 
- use dictionary comprehension? 
'''

#Code:

def invert_dict(food_items):

    return {value: key for key, value in food_items.items()}


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True