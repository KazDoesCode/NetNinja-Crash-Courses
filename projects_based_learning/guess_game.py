#This is a guessing game where the user has to guess a number between 1 and 100.
import random

def guess_game(a:int,b:int):
    tries = 0
    if a > b:
        a,b = b,a
        
    num_to_guess = random.randint(a,b)
    print(num_to_guess)
    while True:
        users_guess = int(input(f"Guess a number from {a} to {b} :  "))
        tries += 1

        if tries == 10:
            print('Max attempts reached, exiting... ')
            break        
        elif users_guess > num_to_guess:
            print("the number is actually lower than this")
        elif users_guess < num_to_guess:
            print("the number is actually higher than this")
        elif users_guess == num_to_guess:
            print("BINGO !!! IT TOOK YOU ",tries,' times to get it')
            break

def get_input(prompt:str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("False format, I need you to enter an integer instead ")

print('enter the range you want to have ')
guess_game(get_input('Lowest: '),get_input('Highest: '))        

