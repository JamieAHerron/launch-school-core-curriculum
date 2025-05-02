#Take everything that you've learned so far
#and build a mortgage calculator that determines
#the monthly payment assuming that interest is compounded monthly.

while True:
    def prompt(message):
        print(f'===> {message}')

    #loan amount
    prompt("Please enter the loan amount: ")
    loan_amount = int(input())

    #annual percentage return (APR)
    prompt("Please enter the Annual Percentage Rate (APR): ")
    apr = float(input())
    if apr == 0:
        apr = 0
    else:
        apr = apr / 1200

    #loan duration (months)
    prompt("Please enter the loan duration (in months): ")
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