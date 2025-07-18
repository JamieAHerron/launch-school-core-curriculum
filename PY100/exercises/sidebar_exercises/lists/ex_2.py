my_list = ['Earth', 'Moon', 'Mars']
empty_list = []

def last(lst):
    print(None if not lst else lst[len(lst) - 1]) #lst[-1] is more succinct

last(my_list)
last(empty_list)