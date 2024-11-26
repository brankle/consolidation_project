def check_input_type(num_of_rounds):
    while num_of_rounds.isdigit() == False:
        print(f"The input you entered: '{num_of_rounds}' is not in the proper format. Please only enter numbers.\n")
        num_of_rounds = input("How many rounds would you like to play?\n")  
    
    print(f"Great! You chose to play {num_of_rounds} rounds")
    return (num_of_rounds)
