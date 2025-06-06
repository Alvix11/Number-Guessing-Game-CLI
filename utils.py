def convert_number(num):
    '''Converts a string to an integer if possible; otherwise, displays a message to the user and returns None.'''
    try:
        num_coverted = int(num)
        return num_coverted
    except ValueError:
        print("Please enter numbers, not letters.\n")
        return None 

def validate_number(num):
    '''Verifies that the entered number is positive and not negative.'''
    num_converted = convert_number(num)
    if num_converted:
        if not num_converted < 0:
            return num_converted
        else:
            print("Please enter positive numbers.\n")
            return None 

def show_difficult_menu():
    '''Displays the difficulty menu.'''
    print("\nPlease select the difficulty level:\n" \
          " 1. Easy (10 chances)\n" \
          " 2. Medium (5 chances)\n" \
          " 3. Hard (3 chances)\n"
          )

def get_difficulty():
    '''Gets the user's option, verifies that the option exists, and returns it; otherwise, sends a message indicating the option is not available.'''
    while True:
        option = input("Enter your choice: ")
        option_validate = validate_number(option)
        if option_validate in [1, 2, 3]:
            return option_validate
        print("Option not available.\n")

def show_welcome_message():
    '''Displays the welcome message.'''
    print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n"
      "You have 5 chances to guess the correct number."
      )