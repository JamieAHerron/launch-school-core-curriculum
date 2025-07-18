# While loop version
names = ['Jamie', 'Aime', 'Stella', 'Martin']
upper_names = []
# counter = 0

# while counter <len(names):
#     upper_name = names[counter].upper()
#     upper_names.append(upper_name)
#     counter += 1

# print(upper_names)

#For loop version
for name in names:
    if name == 'Aime':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)