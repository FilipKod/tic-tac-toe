def check_win(actual_board, size_board, emblem):
    # Horizontal winner
    for row in range(size_board):
        if actual_board[row] == [emblem] * size_board:
            return True

    # Vertical winner
    for collumn in range(size_board):
        temp_array = []
        for row in range(size_board):
            temp_array.append(actual_board[row][collumn])
        if temp_array == [emblem] * size_board:
            return True

    # Diagonal winner
    temp_array = []
    for row in range(size_board):
        temp_array.append(actual_board[row][row])

    if temp_array == [emblem] * size_board:
        return True

    # Diagonale winner (opposite side)
    temp_array = []
    for row in range(size_board):
        temp_array.append(actual_board[row][size_board - row - 1])

    if temp_array == [emblem] * size_board:
        return True

    return False