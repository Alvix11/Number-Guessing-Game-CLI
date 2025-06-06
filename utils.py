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

def show_difficult_menu():
    print("\nPlease select the difficulty level:\n" \
          " 1. Easy (10 chances)\n" \
          " 2. Medium (5 chances)\n" \
          " 3. Hard (3 chances)\n"
          )

def get_difficulty():
    while True:
        option = input("Enter your choice: ")
        option_validate = validate_number(option)
        if option_validate in [1, 2, 3]:
            return option_validate
        print("Option not available.\n")