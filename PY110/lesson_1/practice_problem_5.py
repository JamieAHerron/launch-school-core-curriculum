#Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

result = 0
for age in ages.values():
    result += age

print(result)

#LS Solution

total_age = sum(ages.values())
print(total_age)

#Practice problem 6

minimum_age = min(ages.values())
print(minimum_age)