# winning table

def winning_condition(symb, current_board):
    if (current_board[1][2] and current_board[1][4] and current_board[1][6]) == symb:  # row A
        answer = 'won'
    elif (current_board[2][2] and current_board[2][4] and current_board[2][6]) == symb:  # row B
        answer = 'won'
    elif (current_board[3][2] and current_board[3][4] and current_board[3][6]) == symb:  # row C
        answer = 'won'
    elif (current_board[1][2] and current_board[2][2] and current_board[3][2]) == symb:  # column 1
        answer = 'won'
    elif (current_board[1][4] and current_board[2][4] and current_board[3][4]) == symb:  # column 2
        answer = 'won'
    elif (current_board[1][6] and current_board[2][6] and current_board[3][6]) == symb:  # column 3
        answer = 'won'
    elif (current_board[1][2] and current_board[2][4] and current_board[3][6]) == symb:  # diagonal 1
        answer = 'won'
    elif (current_board[1][6] and current_board[2][4] and current_board[3][2]) == symb:  # diagonal 2
        answer = 'won'
    else:
        answer = 'no winner'

    return answer
