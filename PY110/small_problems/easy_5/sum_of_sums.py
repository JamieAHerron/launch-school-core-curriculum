'''
P:
input: list
output: integer

- take list of numbers as argument
- return sum of the sums of each leading subsequence in list
- list will always contain at least one number

D:
- list

A:
#one method
- sum list
- pop off last number in list
- sum remaining numbers
- continue process until list is empty
- I believe this method will mutate the original list
#another method 
- list comprehension
- sum slices of list
- use a range to get full range of slices
- sum list comprehension of summed slices
'''
#LS third method:

# def sum_of_sums(lst):
#     total = 0
#     running_sum = 0
#     for num in lst:
#         running_sum += num
#         total += running_sum
#     return total

#method one code:

# def sum_of_sums(lst):
#     result = 0

#     while len(lst) > 0:
#         result += sum(lst)
#         lst.pop()
    
#     return result

#method two code:
def sum_of_sums(lst):
    return sum([sum(lst[:i]) for i in range(1, len(lst) + 1)])

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True