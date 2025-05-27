def number_guessing_game():

    print("Please select the difficulty level:\n" \
          " 1. Easy (10 chances)\n" \
          " 2. Medium (5 chances)\n" \
          " 3. Hard (3 chances)\n"
          )
    
    option = input("Enter your choice: ")
    option_converted = convert_number(option)
    

def convert_number(num):
    try:
        num_coverted = int(num)
        return num_coverted
    except ValueError:
        print("Please enter numbers, not letters.")
        return None 

def validate_number(num):
    if not num < 0:
        return True
    else:
        print("Please enter positive numbers.")
        return False   

print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n"
      "You have 5 chances to guess the correct number.\n"
      )

number_guessing_game()