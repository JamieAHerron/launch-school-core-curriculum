cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city == None:
        continue
    else:
        print(len(city))

# #Launch school solution 
# for city in cities:
#     if city is None:
#         continue

#     print(len(city))