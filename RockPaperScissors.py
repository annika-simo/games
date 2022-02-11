import random

# rock, paper, scissors

def play():
    user = 0
    cpu = 0
    while user == cpu:
        user = input('Rock (R), Paper (P), or Scissors (S)? ').lower()
        cpu = random.choice(['r','p','s']) # 1 = rock, 2 = paper, 3 = scissors
        if cpu == 'r':
            print('The computer chose ROCK \n')
        elif cpu == 'p':
            print('The computer chose PAPER \n')
        else:
            print('The computer chose SCISSORS \n')
        if cpu == user:
            print('There was a tie! Try again!')
        elif (cpu == 'r' and user == 'p') or (cpu == 'p' and user == 's') or (cpu == 's' and user == 'r'):
            print('YOU WON! :) \n')
        else:
            print('YOU LOST! :( \n')

again = 'y'

while again == 'y':
    play()
    again = input('Would you like to play agian y/n? ')

