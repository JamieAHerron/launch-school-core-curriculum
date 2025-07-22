#Given the following tuple, how would you count the number of occurrences of "banana" in the tuple?

fruits = ("apple", "banana", "cherry", "date", "banana")

def fruit_count(fruits, countable_fruit):
    
    return sum(1 for fruit in fruits if fruit == countable_fruit)

banana_count = fruit_count(fruits, 'banana')
print(banana_count)

#LS Solution

count = fruits.count('banana')
print(count)