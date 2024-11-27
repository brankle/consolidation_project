
#importing sys, os and random
import sys
import os
import random
import input_checker

#player_name = sys.argv[1]

#print (f"Hello {player_name}! Welcome to my Tuple Out Dice Game!")

print ("Your goal is to roll a higher overall score than the computer player.\n")

print ("But be careful! If you roll the same number 3 times in a row you TUPLE OUT and the game is over!\n")

#asking user how many rounds they would like to play and using a function to validate input
num_of_rounds = input("How many rounds would you like to play?\n")  
num_of_rounds = input_checker.check_input_type(num_of_rounds)

print(f"Great! You chose to play {num_of_rounds} rounds.\n")

#flag to trigger to rerolls and the round to end. 
turn_over = False 

#converting number of rounds to an integer
num_of_rounds_int = int(num_of_rounds)
round_num = 1

#main game logic
for round_num in range(1, num_of_rounds_int + 1):
    print(f"Round {round_num}. Your turn:\n")
    #player's initial rolls - intitializing dice roll list
    dice = []
    for a in range(3):
        dice_roll = random.randint(1,6)
        dice.append(dice_roll)
    print(f"You rolled a: {dice}")  

    #checking for matching die
    if len(set(dice)) == 1:
        print("You Tupled out and earned 0 points this round!\n")
        player_round_score = 0

    elif len(set(dice)) == 2: #2 matching dice
        print("Since you rolled the same number twice you can only reroll one of the die.\n")
        turn_over = False
        while not turn_over:
            reroll_input = input("Would you like to reroll one of your die? \n")
            reroll_input = reroll_input.lower()
            if reroll_input == 'yes' or reroll_input == 'y':
                #finding unique die to reroll
                for b in dice:
                    if dice.count(b) == 1:
                        unique_die = b

                #rerolling unique die
                print(f"You are rerolling {unique_die}. \n")
                for c in range(len(dice)):
                    if dice[c] == unique_die:
                        dice[c] = random.randint(1, 6)

                #if player tuples out during reroll        
                if len(set(dice)) == 1:
                    print(f"After rerolling, your new dice are: {dice}")
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                    turn_over = True
                else:
                    print(f"After rerolling, your new dice are: {dice}.")
            elif reroll_input == "no" or reroll_input == 'n':
                turn_over = True
            else:
                print("That response was not understood so you will not reroll.")
                turn_over = True
                
    #if player rolls 3 unique die            
    elif len(set(dice)) == 3:
        print("Since you rolled three unique numbers you can reroll all of your die.\n")
        turn_over = False
        while not turn_over:
            reroll_input = input("Would you like to reroll your die? \n")
            reroll_input = reroll_input.lower()

            #rerolling all dice
            if reroll_input == 'yes' or reroll_input == 'y':
                for d in range(3):
                    dice[d] = random.randint(1,6)

                #printing rerolled result
                print(f"After rerolling, your new dice are: {dice}.")

                if len(set(dice)) == 1: #tupled out
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                    turn_over = True

                elif len(set(dice)) == 2: #two matching dice
                    print("Since you rolled the same number twice you can only reroll one of the die.\n") 
                    turn_over = False  
                    while not turn_over:
                        reroll_input = input("Would you like to reroll one of your die? \n")
                        reroll_input = reroll_input.lower()
                        if reroll_input == 'yes' or reroll_input == 'y':

                        #finding unique die to reroll
                            for e in dice:
                                if dice.count(e) == 1:
                                    unique_die = e

                            #rerolling unique die
                            print(f"You are rerolling {unique_die}. \n")
                            for f in range(len(dice)):
                                if dice[f] == unique_die:
                                    dice[f] = random.randint(1, 6)
                            print(f"After rerolling, your new dice are: {dice}.")
                            if len(set(dice)) == 1:  # Check if the player tuples out
                                print("You Tupled out and earned 0 points this round!\n")
                                player_round_score = 0
                                turn_over = True
                        elif reroll_input == "no" or reroll_input == 'n':
                            turn_over = True
                        else:
                            print("That response was not understood so you will not reroll.")
                            turn_over = True
            else: # Still three unique numbers
                print(f"After rerolling, your new dice are: {dice}.")
                continue  # Allowing another reroll of all dice
    elif reroll_input == 'no' or reroll_input == 'n':
            print("You chose not to reroll.")
            reroll_input = True 
    else:
        print("Invalid response. Please respond with 'yes/y' or 'no/n'.")
            
    #computer player logic           
    print(f"Round {round_num}. The computer's turn:\n")
    comp_dice = []
    for g in range(3):
        dice_roll = random.randint(1,6)
        dice.append(dice_roll)
    print(f"The computer rolled a: {comp_dice}.") 

    #checking for tuple out
    if len(set(comp_dice)) == 1:
        print("The computer Tupled out and earned 0 points this round!\n")
        computer_round_score = 0
