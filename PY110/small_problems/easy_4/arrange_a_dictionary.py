#Given a dictionary, return its keys sorted by the values associated with each key.

def sort_by_value(pair):
    return pair[1]

def order_by_value(a_dict):
    sorted_pairs =  sorted(a_dict.items(), key=sort_by_value)

    return [key for key, value in sorted_pairs]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True