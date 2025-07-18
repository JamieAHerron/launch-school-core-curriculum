my_list = ['Earth', 'Moon', 'Mars']
empty_list = []

def first_element(first):
    if first:
        print(first[0])
    else:
        print('empty list')

first_element(my_list)
first_element(empty_list)