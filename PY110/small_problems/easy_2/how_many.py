'''
Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
'''

def print_occurrences(occurrences):
    for item, count in occurrences.items():
        print(f'{item} => {count}')

def count_occurrences(vehicles):

    result = {}

    for item in vehicles:
        result[item] = result.get(item, 0) + 1
    
    print_occurrences(result)




vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

'''
your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
'''