# winning table

def winning_condition(current_board):
    if current_board[1][2] == 'X' and current_board[1][4] == 'X' and current_board[1][6] == 'X':  # row A
        answer = 'won'
    elif current_board[1][2] == 'O' and current_board[1][4] == 'O' and current_board[1][6] == 'O':  # row A
        answer = 'won'
    elif current_board[2][2] == 'X' and current_board[2][4] == 'X' and current_board[2][6] == 'X':  # row B
        answer = 'won'
    elif current_board[2][2] == 'O' and current_board[2][4] == 'O' and current_board[2][6] == 'O':  # row B
        answer = 'won'
    elif current_board[3][2] == 'X' and current_board[3][4] == 'X' and current_board[3][6] == 'X':  # row C
        answer = 'won'
    elif current_board[3][2] == 'O' and current_board[3][4] == 'O' and current_board[3][6] == 'O':  # row C
        answer = 'won'
    elif current_board[1][2] == 'X' and current_board[2][2] == 'X' and current_board[3][2] == 'X':  # column 1
        answer = 'won'
    elif current_board[1][2] == 'O' and current_board[2][2] == 'O' and current_board[3][2] == 'O':  # column 1
        answer = 'won'
    elif current_board[1][4] == 'X' and current_board[2][4] == 'X' and current_board[3][4] == 'X':  # column 2
        answer = 'won'
    elif current_board[1][4] == 'O' and current_board[2][4] == 'O' and current_board[3][4] == 'O':  # column 2
        answer = 'won'
    elif current_board[1][6] == 'X' and current_board[2][6] == 'X' and current_board[3][6] == 'X':  # column 3
        answer = 'won'
    elif current_board[1][6] == 'O' and current_board[2][6] == 'O' and current_board[3][6] == 'O':  # column 3
        answer = 'won'
    elif current_board[1][2] == 'X' and current_board[2][4] == 'X' and current_board[3][6] == 'X':  # diagonal 1
        answer = 'won'
    elif current_board[1][2] == 'O' and current_board[2][4] == 'O' and current_board[3][6] == 'O':  # diagonal 1
        answer = 'won'
    elif current_board[1][6] == 'X' and current_board[2][4] == 'X' and current_board[3][2] == 'X':  # diagonal 2
        answer = 'won'
    elif current_board[1][6] == 'O' and current_board[2][4] == 'O' and current_board[3][2] == 'O':  # diagonal 2
        answer = 'won'

    else:
        answer = 'no winner'

    return answer
