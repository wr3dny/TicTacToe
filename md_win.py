# winning table

def winning_condition(name1, name2, current_board):
    if (current_board[1][2] and current_board[1][4] and current_board[1][6]) == 'X':  # row A
        print(f'Player {name1} won')
    # elif (current_board[2][2] and current_board[2][4] and current_board[2][6]) == 'X':  # row B
    #     print(f'Player {name1} won')
    # elif (current_board[3][2] and current_board[3][4] and current_board[3][6]) == 'X':  # row C
    #     print(f'Player {name1} won')
    # elif (current_board[1][2] and current_board[2][2] and current_board[3][2]) == 'X':  # column 1
    #     print(f'Player {name1} won')
    # elif (current_board[1][4] and current_board[2][4] and current_board[3][4]) == 'X':  # column 2
    #     print(f'Player {name1} won')
    # elif (current_board[1][6] and current_board[2][6] and current_board[3][6]) == 'X':  # column 3
    #     print(f'Player {name1} won')
    # elif (current_board[1][2] and current_board[2][4] and current_board[3][6]) == 'X':  # diagonal 1
    #     print(f'Player {name1} won')
    # elif (current_board[1][6] and current_board[2][4] and current_board[3][2]) == 'X':  # diagonal 2
    #     print(f'Player {name1} won')
    # elif (current_board[1][2] and current_board[1][4] and current_board[1][6]) == 'O':  # row A
    #     print(f'Player {name2} won')
    # elif (current_board[2][2] and current_board[2][4] and current_board[2][6]) == 'O':  # row B
    #     print(f'Player {name2} won')
    # elif (current_board[3][2] and current_board[3][4] and current_board[3][6]) == 'O':  # row C
    #     print(f'Player {name2} won')
    # elif (current_board[1][2] and current_board[2][2] and current_board[3][2]) == 'O':  # column 1
    #     print(f'Player {name2} won')
    # elif (current_board[1][4] and current_board[2][4] and current_board[3][4]) == 'O':  # column 2
    #     print(f'Player {name2} won')
    # elif (current_board[1][6] and current_board[2][6] and current_board[3][6]) == 'O':  # column 3
    #     print(f'Player {name2} won')
    # elif (current_board[1][2] and current_board[2][4] and current_board[3][6]) == 'O':  # diagonal 1
    #     print(f'Player {name2} won')
    # elif (current_board[1][6] and current_board[2][4] and current_board[3][2]) == 'O':  # diagonal 2
    #     print(f'Player {name2} won')
    else:
        print('No winner')