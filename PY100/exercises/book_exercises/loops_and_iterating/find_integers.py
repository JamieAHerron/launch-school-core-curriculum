my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# def find_integers(collection):
#     new_list = []
#     [ new_list.append(index) for index in collection if type(index) is int]

#     print(new_list)


# integers = find_integers(my_tuple)
# print(integers)


# alternative (more pythonic) solution

def find_integers(collection):
    return [ index for index in collection if type(index) is int]

integers = find_integers(my_tuple)
print(integers)
