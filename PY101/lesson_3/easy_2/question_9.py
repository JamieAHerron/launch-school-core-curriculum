#We have most of the Munster family in our ages dictionary:
#Add entries for Marilyn and Spot to the dictionary:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.append(additional_ages)

print(ages)

#the above solution is incorrect, 'dict' doesn't have attribute 'append'
