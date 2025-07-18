my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

string_lengths = { key: len(key) for key in my_set if len(key) % 2 != 0 }

print(string_lengths)