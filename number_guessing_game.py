def number_guessing_game():

    print("Please select the difficulty level:\n" \
          " 1. Easy (10 chances)\n" \
          " 2. Medium (5 chances)\n" \
          " 3. Hard (3 chances)\n"
          )
    
    option = input("Enter your choice: ")
    option_validate = validate_number(option)

    if option_validate:

        if option_validate == 1:
            pass
        elif option_validate == 2:
            pass
        elif option_validate == 3:
            pass
        else:
            print("Option not available.")
    

def convert_number(num):
    try:
        num_coverted = int(num)
        return num_coverted
    except ValueError:
        print("Please enter numbers, not letters.")
        return None 

def validate_number(num):
    num_converted = convert_number(num)
    if num_converted:
        if not num_converted < 0:
            return num_converted
        else:
            print("Please enter positive numbers.")
            return None 

print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n"
      "You have 5 chances to guess the correct number.\n"
      )

number_guessing_game()