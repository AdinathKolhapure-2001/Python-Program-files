# Guess the number game

""" In this game computer will decide the a random number between
a range. User have to guess the number, user will get the limited chances
which will be decided by the range. User will be prompted if the guessd number
is small or high or correct. If user we guess the number before it's
chances expires he will win otherwise he will lose."""


import math
import random


def guess_the_number():

    # Take range values from the user

    try:
        lower = int(input("Enter the lower range value: "))   # lower value of range
        upper = int(input("Enter the upper range value: "))   # upper value of range
    except ValueError:
        print("Entered value is not valid, try again")
        return

    print("-" * 100)
    
    
    # Generate a random number between lower value and upper value
    secret_number = random.randint(lower, upper)

    # Get the number of maximum number of attempts
    max_attempts = math.ceil(math.log(upper - lower + 1, 2))
    
    attempts = 0
    guessed_num_list = []
    
    print("Welcome to Guess the Number game!")
    print(f"I've picked a number between {lower} and {upper}. Can you guess what it is?")
    print(f"you have maximum {max_attempts} number of attempts")

    print("-" * 100)

    while attempts < max_attempts:
        
        # Take input from the user
        try:
            guess = int(input(f"Enter your guess (between {lower} and {upper}): "))
        except ValueError:
            print("Entered value is not valid, try again")
            print("-" * 100)
            continue

        # check if guess is in the range
        if guess not in range(lower, upper + 1):
            print("Guessed number is not in the defined range, try again")
            print("-" * 100)
            continue
            
        # append the guessed number into the guessed_num_list
        guessed_num_list.append(guess)
        

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("-" * 100)
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            print(f"And here is the list of your guessed numbers: {guessed_num_list}")
            break

        print("-" * 100)
        
        # Display the remaining number of attempts
        if max_attempts - attempts > 1:
            print(f"you have {max_attempts - attempts - 1} remaining attempts")
        
        attempts += 1

        
    else:
        print(f"Sorry, you've run out of attempts! The correct number was {secret_number}.")
        print("-" * 100)


    # If user wants to play again
    play_again = ""
    response_list = ("yes", "no", '1', '0', 'y', 'n')
    
    while play_again not in response_list:
        play_again = input("Do you want to play again(yes/no): ").strip().lower()

    print("-" * 100)
    
    if play_again == "yes":
        guess_the_number()
    else:
        print("THANK YOU!, Hope you enjoyed the game, come again!")
        return



# Start the game

if __name__ == "__main__":
    guess_the_number()
