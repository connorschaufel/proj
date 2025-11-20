# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Connor Schaufel
# Caleb Galvez
# Derek Rodriguez
# Brady Morrison
# Section: 538
# Assignment: ZANZIBAR - FINAL PROJECT
# Date: 1 DEC 2025

import random

# print("Welcome to the World of ZANZIBAR\n")
# print("""Enter '1' to start a game.
# Enter '2' for instructions on how to play.\n""")







def dice_roll(player_dict, player_name):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)

    print(f"\n{player_name}'s roll:")
    print(f"Dice #1:  {dice1}")
    print(f"Dice #2:  {dice2}")
    print(f"Dice #3:  {dice3}")

    roll_number = 1
    while roll_number < 3:
        reroll_input = input("\nWould you like to roll one or more of your dice again (Y/N)?  ")

        if reroll_input == "Y":
            roll_number += 1
            dice_rerolled = input("\nWhich dice would you like to re-roll (1, 2, 3)?  ")

            if "1" in dice_rerolled:
                dice1 = random.randint(1, 6)
            if "2" in dice_rerolled:
                dice2 = random.randint(1, 6)
            if "3" in dice_rerolled:
                dice3 = random.randint(1, 6)

            print(f"\nDice #1:   {dice1}")
            print(f"Dice #2:   {dice2}")
            print(f"Dice #3:   {dice3}")

        elif reroll_input == "N":
            break
        else:
            print("\nYou did not enter a valid response.")
            continue

    roll = str(dice1) + str(dice2) + str(dice3)
    player_dict[player_name]["roll"] = roll
    return roll









def roll_comparison(player_dict):
    special_roll = {
        "456": 268,
        "111": 267,
        "222": 266,
        "333": 265,
        "444": 264,
        "555": 263,
        "666": 262,
        "123": 261
    }

    score_roll = {
        "1": 100,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 60
    }

    for data in player_dict.values():
        roll = data["roll"]

        for key, value in special_roll.items():
            if sorted(roll) == sorted(key):
                data["score"] = value
                break

        if data["score"] == 0:
            temp_score = 0
            for char in roll:
                temp_score += score_roll[char]
                data["score"] = temp_score

    return player_dict













# Creates dictionary with initial player roster and nested dictionary
# with placeholders for player's rolls (str) and scores (int)

player_dict = {}

i = 1
while True:
    player_name = input(f"Please enter Player {i}'s name (type F when finished): ")

    if player_name == "F":
        break

    player_dict[player_name] = {
        "roll": "",
        "score": 0
    }

    i += 1









for player_name in player_dict:
    dice_roll(player_dict, player_name)

roll_comparison(player_dict)

final_display_list = []
for player_name, data in player_dict.items():
    final_display_list.append((player_name, data))

final_display_list.sort()

print("Final Scores:")
for player_name, data in final_display_list:
    print(f"{player_name}: {data["score"]}")
