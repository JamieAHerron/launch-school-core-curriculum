#Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

#Note: 1 square meter == 10.7639 square feet

print('Enter room length in meters: ')
length = int(input())
print('Enter room width in meters: ')
width = int(input())

def room_area(length, width):
    area_meters = length * width
    area_feet = area_meters * 10.7639

    print(area_meters)
    print(area_feet)

room_area(length, width)

#int() is not the appropriate function for this problem, try again 