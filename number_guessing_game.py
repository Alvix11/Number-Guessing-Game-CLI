def number_guessing_game():

    print("Please select the difficulty level:\n" \
          " 1. Easy (10 chances)\n" \
          " 2. Medium (5 chances)\n" \
          " 3. Hard (3 chances)\n"
          )
    
    option = input("Enter your choice: ")
    option_converted = convert_and_validate_number(option)


def convert_and_validate_number(num):
    try:
        num_coverted = int(num)
        return num_coverted
    except ValueError:
        return None 
    

print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n"
      "You have 5 chances to guess the correct number.\n"
      )

number_guessing_game()