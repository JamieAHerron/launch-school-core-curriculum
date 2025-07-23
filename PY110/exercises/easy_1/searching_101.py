'''
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

Example 1:

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2:

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

Input: Six numerical strings (if asking user for input)
Output: String (describing if the sixth number is in the first five)

Explicit requirements:
    - Ask user six times for various numbers
    - check whether the final number is the same as any of the first five
    - print a message that confirms whether the sixth number is/ is not the same as any of the first five

Implicit requirements:
    - Numerical string that is input will need to be converted to integer
    - Final input needs to be compared against the first five for equality
    - integers need to be coerced before final string result is output

Questions:
    - What if the input is not a numerical string?
    - Do we need to convert to an integer is strings input are always numerical?
    - How do we deal with empty strings (no input)?
'''
def get_valid_input(prompt):

    number = input(prompt)
    while not number.isdigit():
        number = input(prompt)
    return number


first_five_numbers = []
ordinals = ['1st', '2nd', '3rd', '4th', '5th']

for i in range(5):
    prompt = f'Enter the {ordinals[i]} number:'
    number_str = get_valid_input(prompt)
    first_five_numbers.append(int(number_str))

final_number_str = get_valid_input('Enter final value:')
final_number = int(final_number_str)
first_five_numbers_string_list = [str(num) for num in first_five_numbers]

if final_number in first_five_numbers:
    print(f'{final_number} is in {','.join(first_five_numbers_string_list)}')
else:
    print(f'{final_number} is not in {','.join(first_five_numbers_string_list)}')