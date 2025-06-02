import random
import time

def number_guessing_game():

    print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n"
      "You have 5 chances to guess the correct number.\n"
      )

    print("Please select the difficulty level:\n" \
          " 1. Easy (10 chances)\n" \
          " 2. Medium (5 chances)\n" \
          " 3. Hard (3 chances)\n"
          )
    
    while True:
        option = input("Enter your choice: ")
        option_validate = validate_number(option)

        if option_validate:

            if option_validate == 1:
                print("\nGreat! You have selected the Easy difficulty level.")
                print("Let's start the game!\n")
                logic_game(10)
                break
            elif option_validate == 2:
                print("\nGreat! You have selected the Medium difficulty level.")
                print("Let's start the game!\n")
                logic_game(5)
                break
            elif option_validate == 3:
                print("\nGreat! You have selected the Hard difficulty level.")
                print("Let's start the game!\n")
                logic_game(3)
                break
            else:
                print("Option not available.\n")    

def convert_number(num):
    try:
        num_coverted = int(num)
        return num_coverted
    except ValueError:
        print("Please enter numbers, not letters.\n")
        return None 

def validate_number(num):
    num_converted = convert_number(num)
    if num_converted:
        if not num_converted < 0:
            return num_converted
        else:
            print("Please enter positive numbers.\n")
            return None 

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
            break
        else:
            print("Error")

number_guessing_game()