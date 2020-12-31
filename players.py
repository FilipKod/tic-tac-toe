import sys
import random

# class bcolors:
#     BLUE = '\033[94m'
#     ENDC = '\033[0m'

# players = {}

# chars = ["X", "O"]
# random.shuffle(chars)

# for player in range(1, 3):
#     name = input(f"Player {player}, what is your name? ")
#     players[player] = { "name": name }
#     name_string = bcolors.BLUE + name + bcolors.ENDC
#     emblem_string = bcolors.BLUE + chars[player - 1] + bcolors.ENDC
#     print(f"Hi {name_string}, you will be play with emblem {emblem_string}")


# for pl in players:
#     print(players[pl]['name'])

players = {
    1: "Adam",
    2: "Adam",
    3: "Adam",
    4: "Adam",
    5: "Adam",
    6: "Adam",
    7: "Adam",
    8: "Adam",
}

pl = random.randint(list(players.keys())[0], len(players))

count = 2
while count > 0:
    for pl_n in range(pl, len(players) + 1):
        print(pl_n)
    pl = list(players.keys())[0]
    count -= 1