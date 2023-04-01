# winning table
from md_board import board

def winning_condition(name1, name2, current_board):
    if (board[1][3] and board[1][5] and board[1][7]) == 'X':  # row A
        print(f'Player {name1} won')
    elif (board[2][3] and board[2][5] and board[2][7]) == 'X':  # row B
        print(f'Player {name1} won')
    elif (board[3][3] and board[3][5] and board[3][7]) == 'X':  # row C
        print(f'Player {name1} won')
    elif (board[1][3] and board[2][3] and board[3][3]) == 'X':  # column 1
        print(f'Player {name1} won')
    elif (board[1][5] and board[2][5] and board[3][5]) == 'X':  # column 2
        print(f'Player {name1} won')
    elif (board[1][7] and board[2][7] and board[3][7]) == 'X':  # column 3
        print(f'Player {name1} won')
    elif (board[1][3] and board[2][5] and board[3][7]) == 'X':  # diagonal 1
        print(f'Player {name1} won')
    elif (board[1][7] and board[2][5] and board[3][3]) == 'X':  # diagonal 2
        print(f'Player {name1} won')
    elif (board[1][3] and board[1][5] and board[1][7]) == 'O':  # row A
        print(f'Player {name2} won')
    elif (board[2][3] and board[2][5] and board[2][7]) == 'O':  # row B
        print(f'Player {name2} won')
    elif (board[3][3] and board[3][5] and board[3][7]) == 'O':  # row C
        print(f'Player {name2} won')
    elif (board[1][3] and board[2][3] and board[3][3]) == 'O':  # column 1
        print(f'Player {name2} won')
    elif (board[1][5] and board[2][5] and board[3][5]) == 'O':  # column 2
        print(f'Player {name2} won')
    elif (board[1][7] and board[2][7] and board[3][7]) == 'O':  # column 3
        print(f'Player {name2} won')
    elif (board[1][3] and board[2][5] and board[3][7]) == 'O':  # diagonal 1
        print(f'Player {name2} won')
    elif (board[1][7] and board[2][5] and board[3][3]) == 'O':  # diagonal 2
        print(f'Player {name2} won')
    else:
        print('No winner')