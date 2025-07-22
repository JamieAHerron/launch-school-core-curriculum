produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(produce_items):
    return {key: value for key, value in produce_items.items() if value == 'Fruit'}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' } 