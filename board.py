import sys

ab_botom_string = " " * 3 + "-"

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

board_len = len(board)

horizontal_axis = ["A", "B", "C"]
vertical_axis = [1, 2, 3]

def show_board():
    print("Actual state of board")
    print("🌫" * 25)
    print(" " * 5, end="")
    for horizontal_letter in horizontal_axis:
        print(horizontal_letter, " " * 2, end="")
    print()
    for row_b in range(0, board_len):
        print(" ", ab_botom_string * 3)
        print(row_b + 1," " , end="")
        for collumn_b in range(0, len(board[row_b])):
            player = board[row_b][collumn_b]
            print("|", player, end=" ")
        print("|", end="")
        print()

        if row_b == board_len - 1:
            print(" ", ab_botom_string * 3)


show_board()