#mortgage calculator

def prompt(message):
    print(f'===> {message}')

#error checking function
def invalid_number(number_str):
    try:
        float(number_str)
        return False
    except ValueError:
        return True

prompt("Welcome to Mortgage Calculator!")
prompt("---------------------------------")

while True:
    prompt("Please enter the loan amount: ")
    loan_amount = input()

    #check for input errors
    while invalid_number(loan_amount) or float(loan_amount) <= 0:
        prompt("The amount must be a positive number. Please try again: ")
        loan_amount = input()

    loan_amount = float(loan_amount)

    prompt("Please enter the Annual Percentage Rate (APR): ")
    prompt("Example: 5 for 5%, 2.5 for 2.5%")
    apr = input()

    #check for input errors
    while invalid_number(apr) or float(apr) < 0:
        prompt("Please enter a valid percentage. Try again: ")
        apr = input()

    apr = float(apr)

    if apr == 0: #for zero interest loans
        apr = 0
    else:
        apr = apr / 1200

    prompt("Please enter the loan duration (in months): ")
    duration_months = input()

    #check for input error
    while invalid_number(duration_months) or int(duration_months) <= 0:
        prompt("The duration (in months) must be a positive number. " \
        "Try again: ")
        duration_months = input()

    duration_months = int(duration_months)

    #loan payment calculation
    if apr == 0:
        monthly_payment = loan_amount / duration_months
    else:
        monthly_payment = loan_amount * (apr / (1 - (1 + apr) ** (-duration_months)))

    print(f'Your monthly payment will be: ${monthly_payment:.2f}')

    prompt("Would you like to calculate another loan? (y/n): ")
    answer = input()
    if answer and answer[0].lower() != 'y':
        break