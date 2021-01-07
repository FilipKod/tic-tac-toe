import board
import input_handler
import players

game_board = board.create_board(3)
players, start_pl_id = players.setup_players()

board.show_board(game_board)

empty_places = len(game_board)**2
game_counter = 1    # The number of games played
round_counter = 1   # The number of round
move_counter = 0    # The number of moves made by players (together)

while True:
    # All places are taken without winner (draw)
    if empty_places == move_counter:
        print("It's draw!")
        next_game = input("Do you want to play another game? (y/N): ")

        if next_game == "y":
            move_counter = 1
            continue
        elif next_game == "n":
            # Show same statistics and cancel program
            board.print_game_over()
            break
        else:
            board.print_game_over()
            break
    
    print("Welcome to the round", round_counter)
    print("⋯" * 30)
    
    for pl_id in range(start_pl_id, len(players) + 1):
        print(players[pl_id]["name"], "is on the turn.")
        x, y = input_handler.input_coordinates()
        emblem = players[pl_id]["char"]

        board.update_board(emblem, y, x, game_board)
        move_counter += 1

        board.show_board(game_board)

    start_pl_id = list(players.keys())[0]

        # board.update_board(emblem, )

    round_counter += 1