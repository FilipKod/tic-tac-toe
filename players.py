import random

import board

class bcolors:
    BLUE = '\033[94m'
    ENDC = '\033[0m'

players = {}

chars = ["X", "O"]
random.shuffle(chars)

# Setup player names and their emblem
for player in range(1, 3):
    name = input(f"Player {player}, what is your name? ")
    players[player] = { "name": name }
    players[player]["char"] = chars[player - 1]
    name_string = bcolors.BLUE + name + bcolors.ENDC
    emblem_string = bcolors.BLUE + chars[player - 1] + bcolors.ENDC
    print(f"Hi {name_string}, you will be play with emblem {emblem_string}")


first_pl = random.randint(list(players.keys())[0], len(players))
first_pl_name = bcolors.BLUE + players[first_pl]["name"] + bcolors.ENDC

print("Start player with name", first_pl_name)

# count = 2
# while count > 0:
#     for pl_n in range(pl, len(players) + 1):
#         print(pl_n)
#     pl = list(players.keys())[0]
#     count -= 1