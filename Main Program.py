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

def dice_roll(player_dict, player_name):
    perform_roll = input(f"\n{player_name}, enter R to perform your roll. ")
    if perform_roll.upper() == "R":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)

        print(f"\n{player_name}'s roll:")
        print(f"Dice #1:  {dice1}")
        print(f"Dice #2:  {dice2}")
        print(f"Dice #3:  {dice3}")

        roll_number = 1
        while roll_number < 3:
            dice_rerolled = input("\nWhich dice, if any, would you like to re-roll (1, 2, 3 or N for none)? ")
            if dice_rerolled.upper() == "N":
                break

            elif dice_rerolled != "N":
                if "1" in dice_rerolled:
                    dice1 = random.randint(1, 6)
                if "2" in dice_rerolled:
                    dice2 = random.randint(1, 6)
                if "3" in dice_rerolled:
                    dice3 = random.randint(1, 6)

                print(f"\nDice #1:   {dice1}")
                print(f"Dice #2:   {dice2}")
                print(f"Dice #3:   {dice3}")

                roll_number += 1

            else:
                print("\nYou did not enter a valid response.")
                continue

        roll = str(dice1) + str(dice2) + str(dice3)
        player_dict[player_name]["roll"] = roll
        return roll
    else:
        print("\nYou must enter 'R' to roll.")
        return dice_roll(player_dict, player_name)




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
        data["score"] = 0

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




def roll_to_chips(roll):
    sorted_roll = "".join(sorted(roll))

    if sorted_roll == "456":
        return 4

    elif sorted_roll in ("111", "222", "333", "444", "555", "666"):
        return 3

    elif sorted_roll == "123":
        return 2

    else:
        return 1




def update_chips(player_dict):
    first = True
    for name, data in player_dict.items():
        score = data["score"]
        if first:
            max_score = score
            min_score = score
            first = False
        else:
            if score > max_score:
                max_score = score
            if score < min_score:
                min_score = score

    winners = []
    losers = []
    for name, data in player_dict.items():
        if data["score"] == max_score:
            winners.append(name)
        if data["score"] == min_score:
            losers.append(name)

    if len(losers) > 1:
        print("\nTie for lowest score; no chips are exchanged")
        return player_dict

    winner_name = winners[0]
    loser_name = losers[0]

    winner_roll = player_dict[winner_name]["roll"]
    chips_gained = roll_to_chips(winner_roll)

    if len(winners) > 1:
        print("\nHighest rolls:")
        for name in winners:
            print(f"{name}: {player_dict[name]["roll"]}")
    else:
        print(f"\nHighest roll: {winner_name} ({winner_roll})")

    print(f"\nLowest roll: {loser_name}")
    if chips_gained == 1: # "Taylor receives 1 chip from EACH player."
        if len(player_dict) > 2:
            print(f"\n{loser_name} receives {chips_gained} chip from each player.")
        else:
            print(f"\n{loser_name} receives {chips_gained} chip from the other player.")
    else:
        if len(player_dict) > 2:
            print(f"\n{loser_name} receives {chips_gained} chips from each player.")
        else:
            print(f"\n{loser_name} receives {chips_gained} chips from the other player.")

    for name, data in player_dict.items():
        if name == loser_name:
            continue

        chips_paid = chips_gained
        if data["chips"] < chips_paid:
            chips_paid = data["chips"]

        data["chips"] -= chips_paid
        player_dict[loser_name]["chips"] += chips_paid

    return player_dict




# Creates dictionary with initial player roster and nested dictionary
# with placeholders for player's rolls (str), scores (int), and chips (int)
player_dict = {}

i = 1
while True:
    player_name = input(f"Please enter Player {i}'s name (type F when finished): ")

    if player_name.upper() == "F":
        if i < 3:
            print("At least two players are needed to play the game of Zanzibar.")
            continue
        break

    player_dict[player_name] = {
        "roll": "",
        "score": 0,
        "chips": 20
    }

    i += 1




# MAIN GAME LOOP
round_num = 1
game_over = False

while game_over == False:
    print()
    print("*" * 80)
    print(f"ROUND {round_num}")
    print("*" * 80)

    for player_name in player_dict:
        dice_roll(player_dict, player_name)

    player_dict = roll_comparison(player_dict)
    player_dict = update_chips(player_dict)

    print("\nCurrent chip counts: ")
    for name, data in player_dict.items():
        print(f"{name}: {data["chips"]} chips")

    zero_chips = False
    for name, data in player_dict.items():
        if data["chips"] <= 0:
            zero_chips = True
            break

    if zero_chips:
        first = True
        for name, data in player_dict.items():
            if first:
                max_chips = data["chips"]
                first = False

            else:
                if data["chips"] > max_chips:
                    max_chips = data["chips"]

        winners = []
        for name, data in player_dict.items():
            if data["chips"] == max_chips:
                winners.append(name)

        print("\nGAME OVER")
        print("\nFinal chip counts: ")
        for name, data in player_dict.items():
            print(f"{name}: {data["chips"]} chips")

        if len(winners) == 1:
            print(f"\nWinner: {winners[0]}")
        else:
            print("\nWinners (tie):")
            for name in winners:
                print(name)

        game_over = True

    else:
        another_round = input("\nWould you like to play another round (Y/N)?: ")
        if another_round.upper() == "Y":
            round_num += 1
        else:
            print("\nGAME ENDED BY PLAYERS")
            game_over = True