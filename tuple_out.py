
#importing sys, os and random
import sys
import os
import random
import input_checker
import time

player_name = sys.argv[1]


print (f"Hello {player_name}! Welcome to my Tuple Out Dice Game!")

print ("Your goal is to roll a higher overall score than the computer player.\n")

print ("But be careful! If you roll the same number 3 times in a row you TUPLE OUT and the game is over!\n")

#asking user how many rounds they would like to play and using a function to validate input
num_of_rounds = input("How many rounds would you like to play?\n")  
num_of_rounds = input_checker.check_input_type(num_of_rounds)

print(f"Great! You chose to play {num_of_rounds} rounds.\n")

#flag to trigger to rerolls and the round to end. 
#turn_over = False 

#converting number of rounds to an integer
num_of_rounds_int = int(num_of_rounds)
round_num = 1

#score dictionary
scores = {f"{player_name}": 0, "computer": 0}

#tuple out function
def tupled_out(dice):
    """
    This function responds to a user tupling out. 
    """
    if len(set(dice)) == 1:
        print("You Tupled out and earned 0 points this round!\n")

for round_num in range(1, num_of_rounds_int + 1):
    print(f"Round {round_num}. Your turn:\n")
    time.sleep(1)
    start_time = time.time()

    #initializing player's score
    player_round_score = 0

    #player's initial rolls - intitializing dice roll list
    dice = []
    for a in range(3):
        player_dice_roll = random.randint(1,6)
        dice.append(player_dice_roll)
    input_checker.roll_delay
    print(f"You rolled a: {dice}")  

    #checking for matching die

    #2 matching dice
    if len(set(dice)) == 2: 
        print("Since you rolled the same number twice you can only reroll one of the die.\n")
        turn_over = False
        while not turn_over:
            reroll_input = input("Would you like to reroll one of your die? (yes/y or no/n) \n").lower()
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
                    input_checker.roll_delay
                    print(f"After rerolling, your new dice are: {dice}")
                    tupled_out(dice)
                    player_round_score = 0
                    turn_over = True
                else:
                    print(f"After rerolling, your new dice are: {dice}.")
            elif reroll_input == "no" or reroll_input == 'n':
                print("You chose not to reroll.")
                turn_over = True
            else:
                print("That response was not understood so you will not reroll.")
                turn_over = True          
                #if player rolls 3 unique die            
    elif len(set(dice)) == 3:
        print("Since you rolled three unique numbers you can reroll all of your die.\n")
    
        #dice reroll loop
        turn_over = False
        while not turn_over:
            reroll_input = input("Would you like to reroll your die? (yes/y or no/n) \n")
            reroll_input = reroll_input.lower()

            #rerolling all dice
            if reroll_input == 'yes' or reroll_input == 'y':
                dice = [random.randint(1, 6) for _ in range(3)]
                print(f"After rerolling, your new dice are: {dice}.")

                
                #two matching dice after reroll
                if len(set(dice)) == 2: 
                    print("Since you rolled the same number twice you can only reroll one of the die.\n") 
                    turn_over = False  
                    while not turn_over:
                        reroll_input = input("Would you like to reroll one of your die? (yes/y or no/n) \n")
                        reroll_input = reroll_input.lower()
                        if reroll_input == 'yes' or reroll_input == 'y':

                            #finding unique die to reroll
                            for e in dice:
                                if dice.count(e) == 1:
                                    unique_die = e

                                #rerolling unique die
                            print(f"You are rerolling {unique_die}. \n")
                            dice[dice.index(unique_die)] = random.randint(1, 6)
                            input_checker.roll_delay
                            print(f"After rerolling, your new dice are: {dice}.")

                            # Checking if the player tuples out after reroll
                            if tupled_out:
                                player_round_score = 0
                                turn_over = True
                        elif reroll_input == "no" or reroll_input == 'n':
                            print("You chose not to reroll.")
                            turn_over = True
                        else:
                            print("That response was not understood so you will not reroll.")
                            turn_over = True
                else:
                    tupled_out(dice)
            elif reroll_input == "no" or reroll_input == 'n':  # Handling "no" inside the main loop
                print("You chose not to reroll.")
                turn_over = True  
            else:
                print("That response was not understood so you will not reroll.")
                turn_over = True  
        else: 
            tupled_out(dice)        
    
    #determing how much time the player's rolls took
    elapsed_time = time.time() - start_time
    
    player_round_score = sum(dice) 
    
    #score multiplier rewarding quick decision-making
    print(f"Your rolls took: {elapsed_time} seconds\n")
    if elapsed_time < 5:
        player_round_score *= 1.5 
    #printing score for the round    
    print(f"Your score this round is: {player_round_score}\n")

    #updating player's score
    scores[player_name] += player_round_score  
    time.sleep(1)

    #computer player logic           
    print(f"Round {round_num}. The computer's turn:\n")
    time.sleep(2)
    computer_dice_rolls = tuple(random.randint(1, 6) for _ in range(3))
    print(f"The computer rolled a: {computer_dice_rolls}.\n") 

    #checking for tuple out
    if len(set(computer_dice_rolls)) == 1:
        print("The computer Tupled out and earned 0 points this round!\n")
        computer_round_score = 0
    else:
        computer_round_score = sum(computer_dice_rolls)
    scores["computer"] += computer_round_score

    #printing score for the round
    print(f"The computer's score this round is: {computer_round_score}\n")



    
    time.sleep(1)
    #printing current score
    print(f"Current Score: {player_name} - {scores[player_name]} | Computer - {scores['computer']}\n")

#determining who wins game logic 
print("Game Over!\n")
if scores[player_name] > scores["computer"]:
    print(f"You win with {scores[player_name]} points to the computer's {scores['computer']} points!")
elif scores[player_name] < scores["computer"]:
    print(f"The computer wins with {scores['computer']} points to your {scores[player_name]} points!")
else:
    print(f"It's a tie! Both you and the computer have {scores[player_name]} points.")
