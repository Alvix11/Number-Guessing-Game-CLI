import random

def number_guessing_game():

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
                game(10)
                break
            elif option_validate == 2:
                game(5)
                break
            elif option_validate == 3:
                game(3)
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

def game(chances_user):
    num_random = random.randint(1, 100) 
    chances = chances_user
    condition = 0

    while condition < chances:
        condition += 1
        print(condition)
        number = input("Enter your guess: ")
        number_validate = validate_number(number)

        if number_validate:
            if number_validate == num_random:
                print("Correct")
                break
            else:
                print("Incorrect")


print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n"
      "You have 5 chances to guess the correct number.\n"
      )

number_guessing_game()