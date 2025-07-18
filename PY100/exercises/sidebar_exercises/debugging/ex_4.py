pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'] = pets['dog'].append('bowser') <<< This returned None 
pets['dog'].append('bowser')

print(pets)  