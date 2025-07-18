import random
random_number = random.randint(0, 1)

if random_number == 1: #if random_number: <--  also works because 0 is falsy so 1 is Truthy
    print('Yes!')
else:
    print('No')