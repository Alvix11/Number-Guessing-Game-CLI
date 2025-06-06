import random
import time
import sys
from utils import show_difficult_menu, get_difficulty, validate_number, convert_number, show_welcome_message

def number_guessing_game():

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
    num_random = random.randint(1, 100) 
    chances = chances_user
    condition = 0

    while condition < chances:
        start = time.perf_counter()
        number = input("Enter your guess: ")
        number_validate = validate_number(number)

        if number_validate:
            condition += 1
            if condition == chances:
                print(f"\nWhat a shame! No more attempts.\nThe number was {num_random}.")
                ask_play_again()
                break
            else:
                if number_validate == num_random:
                    end = time.perf_counter()
                    elapsed_time = end - start
                    print(f"Congratulations! You guessed the correct number in {condition} attempts and in a time of {elapsed_time:.2f} seconds.")
                    ask_play_again()
                    break
                else:
                    if num_random > number_validate:
                        print(f"Incorrect! The number is greater than {number_validate}.\n")
                    else:
                        print(f"Incorrect! The number is less than {number_validate}.\n")

def ask_play_again():
    while True:
        ask  = input("\nWould you like to play another round? Press '1' for Yes or '2' for No: ")
        ask_convert = convert_number(ask)
        if ask_convert == 1:
            number_guessing_game()
        elif ask_convert == 2:
            print("\nThanks for playing!")
            sys.exit()
        else:
            print("Error")

def main():

    show_welcome_message()
    number_guessing_game()

if __name__ == '__main__':
    main()