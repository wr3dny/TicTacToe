# Implementacja gry kółko i krzyżyk
#

board = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', '.', '|'],
         ['B', '|', '.', '|', '.', '|', '.', '|'], ['C', '|', '.', '|', '.', '|', '.', '|']]

print(board[1][1])


def board_display(name1, name2):
    cl = max(len(name1), len(name2))
    print(f'{name1 : ^{cl}} -  playing X')
    vs = 'vs'
    print(vs.center(cl))
    print(f'{name2 : ^{cl}} -  playing O')
    print(' ')
    for b in board:
        print(*b)



def winning_condition(name1, name2):
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


def play(n1, n2):
    used_spots = []
    print(f'{n1}, place "X" on the board.')
    flag = 0
    row = input('Row: ')
    row = row.capitalize()
    column = int(input('Column: '))

    if row == 'A':
        row = 1
    elif row == 'B':
        row = 2
    elif row == 'C':
        row = 3

    used_spots.append((row, column))
    board[row][column+column] = 'X'
    x_current_board = []
    x_current_board.append((row, column))
    print(x_current_board)





    print(f'{n2}, place "O" on the board.')
    row = input('Row: ')
    row = row.capitalize()
    column = int(input('Column: '))
    if row == 'A':
        row = 1
    elif row == 'B':
        row = 2
    elif row == 'C':
        row = 3

    used_spots.append((row, column))
    board[row][column+column] = 'O'

    print(used_spots)
    # while (row, column) in used_spots:
    #     print('Not possible. Already in use')
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #

    #
    #
    #
    #
    #
    # while (row, column) in used_spots:
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #

    #
    # print(f'{n2}, place "O" on the board.')
    # row = input('Row: ')
    # row = row.capitalize()
    # column = int(input('Column: '))
    # if row == 'A':
    #     row = 1
    # elif row == 'B':
    #     row = 2
    # elif row == 'C':
    #     row = 3
    # while (row, column) in used_spots:
    #     print('Not possible. Already in use')
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #
    # used_spots.append((row, column))
    # board[row][column+column] = 'O'

    # print(f'{n1}, place "X" on the board.')
    # row = input('Row: ')
    # row = row.capitalize()
    # column = int(input('Column: '))
    # if row == 'A':
    #     row = 1
    # elif row == 'B':
    #     row = 2
    # elif row == 'C':
    #     row = 3
    # while (row, column) in used_spots:
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #
    # used_spots.append((row, column))
    # board[row][column+column] = 'X'
    #
    # print(f'{n2}, place "O" on the board.')
    # row = input('Row: ')
    # row = row.capitalize()
    # column = int(input('Column: '))
    # if row == 'A':
    #     row = 1
    # elif row == 'B':
    #     row = 2
    # elif row == 'C':
    #     row = 3
    # while (row, column) in used_spots:
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #
    # used_spots.append((row, column))
    # board[row][column+column] = 'O'
    #
    # print(f'{n1}, place "X" on the board.')
    # row = input('Row: ')
    # row = row.capitalize()
    # column = int(input('Column: '))
    # if row == 'A':
    #     row = 1
    # elif row == 'B':
    #     row = 2
    # elif row == 'C':
    #     row = 3
    # while (row, column) in used_spots:
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #
    # used_spots.append((row, column))
    # board[row][column+column] = 'X'
    #
    # print(f'{n2}, place "O" on the board.')
    # row = input('Row: ')
    # row = row.capitalize()
    # column = int(input('Column: '))
    # if row == 'A':
    #     row = 1
    # elif row == 'B':
    #     row = 2
    # elif row == 'C':
    #     row = 3
    # while (row, column) in used_spots:
    #     row = input('Row: ')
    #     column = int(input('Column: '))
    #
    # used_spots.append((row, column))
    # board[row][column+column] = 'O'


def main():
    used_spots = []
    name_1 = input('Player 1 name: ')
    name_2 = input('Player 2 name: ')

    player_1_win = winning_con_x()
    player_2_win = winning_con_o()

    board_display(name_1, name_2)

    play(name_1, name_2)
    board_display(name_1, name_2)
    play(name_1, name_2)
    board_display(name_1, name_2)
    play(name_1, name_2)
    board_display(name_1, name_2)
    play(name_1, name_2)
    board_display(name_1, name_2)


if __name__ == '__main__':
    main()


# print(*board, sep = '\n')

# print(*name_column)
# print(*first_column)
# print(*second_column)
# print(*third_column)

