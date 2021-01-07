import board
import random

class bcolors:
    BLUE = '\033[94m'
    ENDC = '\033[0m'

# Setup player names and their emblem
def setup_players(players={}):
    chars = ["X", "O"]
    random.shuffle(chars)
    starting_player_id = chars.index("X") + 1

    for player in range(1, 3):
        name = input(f"Player {player}, what is your name? ")
        if name == "":
            name = "Player " + str(player)
        players[player] = { "name": name }
        players[player]["char"] = chars[player - 1]
        name_string = bcolors.BLUE + name + bcolors.ENDC
        emblem_string = bcolors.BLUE + chars[player - 1] + bcolors.ENDC
        print(f"Hi {name_string}, you will be play with emblem {emblem_string}")

    starting_player_print(starting_player_id, players)   
    return players, starting_player_id

def starting_player_print(player_id, players):
    starting_player_name = bcolors.BLUE + players[player_id]["name"] + bcolors.ENDC
    starting_player_char = bcolors.BLUE + players[player_id]["char"] + bcolors.ENDC
    print("\nPlayer", starting_player_name, "with emblem", starting_player_char, "begins as the first.", end="\n\n")
