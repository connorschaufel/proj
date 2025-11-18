# player_dict = {
#     'Taylor': {'roll': '456', 'score': 0},
#     'Connor': {'roll': '111', 'score': 0},
#     'Trevor': {'roll': '116', 'score': 0}
# }

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
            if (roll[0] in key) and (roll[1] in key) and (roll[2] in key):
                data["score"] = value
                break

        if data["score"] == 0:
            temp_score = 0
            for char in roll:
                temp_score += score_roll[char]
                data["score"] = temp_score

    return player_dict


# print(roll_comparison(player_dict))
