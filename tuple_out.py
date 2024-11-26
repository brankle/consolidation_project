
#importing sys, os and random
import sys
import os
import random
import input_checker

#player_name = sys.argv[1]

#print (f"Hello {player_name}! Welcome to my Tuple Out Dice Game!")

print ("Your goal is to roll a higher overall score than the computer player.\n")

print ("But be careful! If you roll the same number 3 times in a row you TUPLE OUT and the game is over!\n")

computer_reroll = input("Before we begin the game would you like to have the computer reroll its dice twice automatically (harder game mode)? \n")
computer_reroll = computer_reroll.lower()

if computer_reroll == 'yes' or 'y':
    hard_mode = True
    print("You've chosen the harder game mode! The computer will automatically reroll its non-matching dice twice.")
elif print("You've chosen the normal game mode. The computer will roll its dice once."):
    hard_mode = False
else:
    print("The computer didn't understand that response and will run the normal game mode by default.")
    hard_mode = False

#asking user how many rounds they would like to play and validating input
num_of_rounds = input("How many rounds would you like to play?\n")  
num_of_rounds = input_checker.check_input_type(num_of_rounds)

print(f"Great! You chose to play {num_of_rounds} rounds\n")
num_of_rounds_int = int(num_of_rounds)
round_num = 1
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
    elif len(set(dice)) == 2:
        print("Since you rolled the same number twice you can only reroll one of the die.\n")
        reroll_input = False
        while reroll_input == False:
            reroll_input = input("Would you like to reroll one of your die? \n")
            if reroll_input == 'yes' or 'y':
                #finding unique die to reroll
                for b in dice:
                    if dice.count(b) == 1:
                        unique_die = b
                #rerolling unique die
                print(f"You are rerolling {unique_die}. \n")
                for c in range(len(dice)):
                    if dice[c] == unique_die:
                        dice[c] = random.randint(1, 6)
                        
                if len(set(dice)) == 1:
                    print(f"After rerolling, your new dice are: {dice}")
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                else:
                    print(f"After rerolling, your new dice are: {dice}.")
                reroll_input = False
            elif reroll_input == "no" or 'n':
                reroll_input = True
            else:
                print("That response was not understood so you will not reroll.")
                reroll_input = True
                
    #if player rolls 3 unique die            
    elif len(set(dice)) == 3:
        print("Since you rolled three unique numbers you can reroll all of your die.\n")
        reroll_input = False
        while reroll_input == False:
            reroll_input = input("Would you like to reroll your die? \n")
            if reroll_input == 'yes' or 'y':
                for d in range(3):
                    dice_roll = random.randint(1,6)
                    dice.append(dice_roll)

                #printing rerolled result
                if len(set(dice)) == 0:
                    print(f"After rerolling, your new dice are: {dice}")
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                elif len(set(dice)) == 2:
                    print("Since you rolled the same number twice you can only reroll one of the die.\n")
                    reroll_input = False
                    while reroll_input == False:
                        reroll_input = input("Would you like to reroll one of your die? \n")
                if reroll_input == 'yes' or 'y':
                #finding unique die to reroll
                    for e in dice:
                        if dice.count(e) == 1:
                            unique_die = e
                #rerolling unique die
                print(f"You are rerolling {unique_die}. \n")
                for f in range(len(dice)):
                    if dice[f] == unique_die:
                        dice[f] = random.randint(1, 6)
                        
                if len(set(dice)) == 1:
                    print(f"After rerolling, your new dice are: {dice}")
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                else:
                    print(f"After rerolling, your new dice are: {dice}.")
                reroll_input = False
            elif reroll_input == "no" or 'n':
                reroll_input = True
            else:
                print("That response was not understood so you will not reroll.")
                reroll_input = True

    #computer player logic           
    print(f"Round {round_num}. The computer's turn:\n")
    comp_dice = []
    for g in range(3):
        dice_roll = random.randint(1,6)
        dice.append(dice_roll)
    print(f"The computer rolled a: {comp_dice}.") 

    #checking for matching die
    if len(set(comp_dice)) == 1:
        print("The computer Tupled out and earned 0 points this round!\n")
        computer_round_score = 0

        #computer hard mode logic
    elif hard_mode == True and len(set(comp_dice)) == 2 :
            #finding unique die to reroll
            for h in range(2):
                for comp_roll in comp_dice:
                    if dice.count(comp_roll) == 1:
                        comp_unique_die = comp_roll

                    #rerolling unique die
                    print(f"The computer is rerolling {unique_die}. \n")
                    for z in range(len(comp_dice)):
                        if comp_dice[z] == comp_unique_die:
                            comp_dice[z] = random.randint(1, 6)

                #tupling out during computer's reroll logic         
                if len(set(comp_dice)) == 1:
                    print(f"After rerolling, the computer's new dice are: {comp_dice}")
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                else:
                    print(f"After rerolling, the computer's new dice are: {dice}.")
'''               
        #if computer rolls 3 unique die            
    elif hard_mode == True and len(set(dice)) == 3:
        print("Since the computer rolled three unique numbers it can reroll all of its die.\n")
        for i in range(2):
            for d in range(3):
                comp_roll = random.randint(1,6)
                dice.append(dice_roll)

                #printing rerolled result
                if len(set(dice)) == 0:
                    print(f"After rerolling, the computer's new dice are: {dice}")
                    print("The computer Tupled out and earned 0 points this round!\n")
                    computer_round_score = 0
                elif len(set(dice)) == 2:
                    print("Since the computer rolled the same number twice it can only reroll one of its die.\n")
                    reroll_input = False
                    while reroll_input == False:
                        reroll_input = input("Would you like to reroll one of your die? \n")
                if reroll_input == 'yes' or 'y':
                #finding unique die to reroll
                    for e in dice:
                        if dice.count(e) == 1:
                            unique_die = e
                #rerolling unique die
                print(f"You are rerolling {unique_die}. \n")
                for f in range(len(dice)):
                    if dice[f] == unique_die:
                        dice[f] = random.randint(1, 6)
                        
                if len(set(dice)) == 1:
                    print(f"After rerolling, your new dice are: {dice}")
                    print("You Tupled out and earned 0 points this round!\n")
                    player_round_score = 0
                else:
                    print(f"After rerolling, your new dice are: {dice}.")
                reroll_input = False
            elif reroll_input == "no" or 'n':
                reroll_input = True
            else:
                print("That response was not understood so you will not reroll.")
                reroll_input = True




scoring: 
scores = {"player_name" : 0, "player 2" : 0}
scores["player 1"] = scores["player 1"] + new_score
'''