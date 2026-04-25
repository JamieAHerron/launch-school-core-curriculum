'''
P:
input: (two) integers
output: list 

- take two integers as arguments
- first integer is a count
- second integer is the starting number of a sequence
- return a list
- list should contain same number of elements as count
- the value of each element should be multiple of starting number
- count argument will always be greater than or equal to 0
- if count is 0 return empty list
- starting number can be any integer

D:
- list

A:
- create result list
- create running_total variable initialize to 0 
- create sequence_count initialize to 0
- Create while loop
- while sequence count is < argument count
- assign starting number to running_total 
- append running_total to result list
- increment sequence_count by 1 
- return list


'''

#Code:

def sequence(count, starting_number):
    #LS version of a solution
    return [starting_number * n for n in range(1, (count + 1))]

    # result = []
    # running_total = 0

    # for _ in range(count):
    #     running_total += starting_number
    #     result.append(running_total)

    # return result

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True