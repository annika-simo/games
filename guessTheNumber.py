import random
from re import X

# you guess the computer's number
def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a new number between 1 and {x}: '))
        if guess < randomNumber:
            print('Sorry guess again. Too low. \n')
        elif guess > randomNumber:
            print('Sorry, guess again. Too high. \n')
    
    print(f'Yay, congrats! you have guessed the number {randomNumber} correctly! \n')

# computer guesses your number
def computerGuess(x):
   low = 1
   high = x
   feedback = ''
   while feedback != 'c':
      if low != high:
         guess = random.randint(low,high)
      else:
         guess = high
      feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
      if feedback == 'h':
         high = guess - 1
      elif feedback == 'l':
         low = guess - 1

   print(f'Yay! The computer guessed your number, {guess}, correctly!')

again = 'y'

# remove the comment for the game you want to play!

while again == 'y':
   # guess(10)
   # computerGuess(1000)
    again = input('Would you like to play agian y/n? ')
