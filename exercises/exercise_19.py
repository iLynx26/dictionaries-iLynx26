dict_of_games = {}

number = int(input())

# for i in range(number):
#     game = input().split(';')
#     if game[0] not in dict_of_games:
#         dict_of_games[game[0]] = [1, 0, 0, 0, game[1]]
#     else:
#         dict_of_games[game[0]][0] += 1
#         dict_of_games[game[0]][4] += game[1]
#     if game[2] not in dict_of_games:
#         dict_of_games[game[2]] = [1, 0, 0, 0, game[3]]
#     else:
#         dict_of_games[game[0]][0] += 1
#         dict_of_games[game[0]][4] += game[1]
#     if game[1] > game[3]:
#         dict_of_games[game[0]][1] += 1
#         dict_of_games[game[2]][3] += 1
#     elif game[1] < game[3]:
#         dict_of_games[game[2]][1] += 1
#         dict_of_games[game[0]][3] += 1
#     elif game[1] == game[3]:
#         dict_of_games[game[0]][2] += 1
#         dict_of_games[game[2]][2] += 1

# for key in dict_of_games.keys():
#     print(f"{key}: {' '.join(list(map(str, dict_of_games[key])))}")

    
for _ in range(number):
    team_1_name, team_1_goals, team_2_name, team_2_goals = input().split(';')

    team_performance = {
        "Total_Games" : 0,
        "Wins" : 0,
        "Draws" : 0,
        "Losses": 0,
        "Total_Points" : 0
    }

    if team_1_name not in dict_of_games:
        dict_of_games[team_1_name] = team_performance.copy()
    
    if team_2_name not in dict_of_games:
        dict_of_games[team_2_name] = team_performance.copy()
    
    if team_1_goals > team_2_goals:
        dict_of_games[team_1_name]["Wins"] += 1
        dict_of_games[team_2_name]["Losses"] += 1
        dict_of_games[team_1_name]["Total_Points"] += 3
    elif team_1_goals < team_2_goals:
        dict_of_games[team_2_name]["Wins"] += 1
        dict_of_games[team_1_name]["Losses"] += 1
        dict_of_games[team_2_name]["Total_Points"] += 3
    else:
        dict_of_games[team_1_name]["Draws"] += 1
        dict_of_games[team_2_name]["Draws"] += 1
        dict_of_games[team_1_name]["Total_Points"] += 1
        dict_of_games[team_2_name]["Total_Points"] += 1

    dict_of_games[team_1_name]["Total_Games"] += 1
    dict_of_games[team_2_name]["Total_Games"] += 1

for team_name, team_stat in dict_of_games.items():
    print(f"{team_name}: {team_stat['Total_Games']} {team_stat['Wins']} {team_stat['Draws']} {team_stat['Losses']} {team_stat['Total_Points']}")
