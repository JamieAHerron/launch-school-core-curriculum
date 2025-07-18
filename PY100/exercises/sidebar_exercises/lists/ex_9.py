destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(destination, lst):
    for item in lst:
        if item == destination:
            print('True') #the use of print() here causes False to print twice. Using a 
    print('False')            #statement would avoid this problem.

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False