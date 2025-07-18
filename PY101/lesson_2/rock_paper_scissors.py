import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'===> {message}')

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        prompt('You win!')
    elif ((player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock')):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Please choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt('Please select a valid option: ')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    print(f'Your choice: {choice}, Computer choice: {computer_choice}')

    display_winner(choice, computer_choice)

    prompt('Do you wish to play again? (y/n)')
    answer = input().lower()

    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break
        prompt('Please input valid answer (y/n)')
        answer = input().lower()

    if answer[0] == 'n':
        break