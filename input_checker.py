def check_input_type(num_of_rounds):
    """"
    This function checks whether the number of rounds the user responds with an integer
    and prompts the user to keep responding until the computer recieves valid input.
    """
    while num_of_rounds.isdigit() == False:
        print(f"The input you entered: '{num_of_rounds}' is not in the proper format. Please only enter numbers.\n")
        num_of_rounds = input("How many rounds would you like to play?\n")  
    
    return (num_of_rounds)
