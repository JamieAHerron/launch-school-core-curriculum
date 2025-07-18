#Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]

# counter = 0
# while counter < len(numbers):
#     numbers.remove(numbers[counter])
#the above solution is too verbose, there is an easier
#way using a while loop

numbers.clear()

print(numbers)