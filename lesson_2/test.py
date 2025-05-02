input_value = ['42']
try:
    numeric_value = int(input_value)
except TypeError:
    print("Invalid input type for conversion")