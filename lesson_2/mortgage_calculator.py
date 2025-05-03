#Take everything that you've learned so far
#and build a mortgage calculator that determines
#the monthly payment assuming that interest is compounded monthly.

#moved outside of while loop (LSBot feedback)
def prompt(message):
    print(f'===> {message}')

#error checking using try/except (LSBot feedback)
def invalid_number(number_str):
    try:
        float(number_str)
        return False
    except ValueError:
        return True

while True:
    #loan amount
    prompt("Please enter the loan amount: ")
    loan_amount = input()

    #check for input errors using invalid_number function (LSBot feedback)
    while invalid_number(loan_amount) or float(loan_amount) <= 0:
        prompt("The amount must be a positive number. Please try again: ")
        loan_amount = input()
    
    loan_amount = float(loan_amount)

    #annual percentage return (APR)
    prompt("Please enter the Annual Percentage Rate (APR): ")
    #Further clarification on desired input(LSBot feedback)
    prompt("Example: 5 for 5%, 2.5 for 2.5%")
    apr = float(input())

    #check for input errors using invalid_number function (LSBot feedback)
    while invalid_number(apr) or float(apr) < 0:
        prompt("Please enter a valid percentage. Try again: ")
        apr = float(input())

    #for zero interest loans
    if apr == 0:
        apr = 0
    else:
        apr = apr / 1200

    #loan duration (months)
    prompt("Please enter the loan duration (in months): ")
    duration_months = int(input())

    #check for input error using invalid_number function (LSBot feedback)
    while invalid_number(duration_months) or int(duration_months) <= 0:
        prompt("The duration (in months) must be a positive number. " \
        "Try again: ")
        duration_months = int(input())

    if apr == 0:
        monthly_payment = loan_amount / duration_months
    else:
        monthly_payment = loan_amount * (apr / (1 - (1 + apr) ** (-duration_months)))

    print(f'Your monthly payment will be: ${round(monthly_payment, 2)}')

    prompt("Would you like to calculate another loan? (y/n): ")
    answer = input()
    if answer and answer[0].lower() != 'y':
        break