import random

def dice_roll(player_dict):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    print(f"Dice 1: {dice1}, Dice 2: {dice2}, Dice 3: {dice3}")
    roll_number = 1
    while roll_number < 3:
        reroll_input = input("\nWould you like to roll one of your dice again (Y/N)? ")
        if reroll_input == "Y":
            roll_number += 1
            dice_rerolled = input("\nWhich dice would you like to re-roll (1, 2, 3)? ")
            if "1" in dice_rerolled:
                dice1 = random.randint(1, 6)
            if "2" in dice_rerolled:
                dice2 = random.randint(1, 6)
            if "3" in dice_rerolled:
                dice3 = random.randint(1, 6)
        elif reroll_input == "N":
            break
        else:
            print("\nYou did not enter a valid response.")
            continue

        print(f"Dice 1: {dice1}, Dice 2: {dice2}, Dice 3: {dice3}")
    roll = str(dice1) + str(dice2) + str(dice3)
    player_dict[player_name]["roll"] = roll
    return roll




#print(dice_roll())
