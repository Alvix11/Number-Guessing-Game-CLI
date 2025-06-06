import random
import time
import sys
from utils import show_difficult_menu, get_difficulty, validate_number, convert_number

def number_guessing_game():
    '''Starts the number guessing game and manages the difficulty selection.'''

    show_difficult_menu()
    
    while True:
        
        option = get_difficulty()

        if option:

            if option == 1:
                print("\nGreat! You have selected the Easy difficulty level.")
                print("Let's start the game!\n")
                logic_game(10)
                break
            elif option == 2:
                print("\nGreat! You have selected the Medium difficulty level.")
                print("Let's start the game!\n")
                logic_game(5)
                break
            elif option == 3:
                print("\nGreat! You have selected the Hard difficulty level.")
                print("Let's start the game!\n")
                logic_game(3)
                break  

def logic_game(chances_user):
    '''Executes the main game logic:
       * Generates a random number between 1 and 100.
       * Allows the user to guess the number with a limited number of attempts.
       * Informs if the entered number is higher or lower than the secret number.
       * Measures the time taken for each successful attempt.
       * Calls the function to ask if the user wants to play again upon completion.'''
    
    num_random = random.randint(1, 100)
    chances = chances_user
    condition = 0

    while condition < chances:
        start = time.perf_counter()
        number = input("Enter your guess: ")
        number_validate = validate_number(number)

        if number_validate:
            condition += 1
            
            if number_validate == num_random:
                end = time.perf_counter()
                elapsed_time = end - start
                print(f"\nCongratulations! You guessed the correct number in {condition} attempts and in a time of {elapsed_time:.2f} seconds.")
                ask_play_again()
                break
            else:
                if num_random > number_validate:
                    print(f"Incorrect! The number is greater than {number_validate}.\n")
                else:
                    print(f"Incorrect! The number is less than {number_validate}.\n")

            if condition == chances:
                print(f"\nWhat a shame! No more attempts.\nThe number was {num_random}.")
                ask_play_again()
                break

def ask_play_again():
    '''Asks the user if they want to play again and acts accordingly based on their response.'''

    while True:

        print("\nWould you like to play another round?\n" \
          " 1. Yes\n" \
          " 2. No\n"
          )
        
        ask  = input("Enter your choice: ")
        ask_convert = convert_number(ask)
        if ask_convert == 1:
            number_guessing_game()
        elif ask_convert == 2:
            print("\nThanks for playing!")
            sys.exit()
        else:
            print("Error")