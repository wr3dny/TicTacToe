def winning(current_board):
    if (current_board[1][2] and current_board[1][4] and current_board[1][6]) == 'X':  # row A
        return 'won'