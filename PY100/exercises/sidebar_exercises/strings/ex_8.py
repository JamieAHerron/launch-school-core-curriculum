# my_string = 'launch school tech & talk'

# uppercase_string = my_string.title()

# print(uppercase_string)

#One of launch schools solutions

def print_title(string):
    words = string.split(' ')
    upper_string = []

    for word in words:
        upper_string.append(word.capitalize())
    
    print(' '.join(upper_string))

    

print_title('launch school tech & talk')