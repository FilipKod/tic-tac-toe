
def create_board(board_size=3):
    if board_size > 6:
        raise Exception("Board size can not be higher than 6.")
    elif board_size < 3:
        raise Exception("Board size can not be lower than 3.")

    board = []
    for row in range(0, board_size):
        temp_row = []
        for collumn in range (0, board_size):
            temp_row.append(" ")
        board.append(temp_row)
    return board


def show_board(board):
    ab_botom_string = " " * 3 + "-"

    horizontal_axis = ["A", "B", "C", "D", "E", "F"]
    # vertical_axis = [1, 2, 3]

    print("Actual state of board")
    print("🌫" * 25, end="\n\n")
    print(" " * 5, end="")

    for letter in range(0, len(board)):
        print(horizontal_axis[letter], " " * 2, end="")
    print()

    for row_b in range(0, len(board)):
        print(" ", ab_botom_string * len(board))
        print(row_b + 1," " , end="")
        for collumn_b in range(0, len(board[row_b])):
            player = board[row_b][collumn_b]
            print("|", player, end=" ")
        print("|", end="")
        print()

        if row_b == len(board) - 1:
            print(" ", ab_botom_string * len(board))

def update_board(emblem, vertical_axis, horizontal_axis, play_desk):
    letters = ["A", "B", "C", "D", "E", "F"]
    ver_point = vertical_axis - 1
    hor_point = letters.index(horizontal_axis)
    play_desk[ver_point][hor_point] = emblem
    return play_desk