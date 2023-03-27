# Implementacja gry kółko i krzyżyk
#
# Opis:
#
# Stwórz gre w kółko i Krzyżyk dla 2 graczy. Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu,
# opcje takie jak imiona graczy, pomysły własne.
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


def winning_con_x():

    win_x_row_a = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'X', '|', 'X', '|', 'X', '|'],
             ['B', '|', '.', '|', '.', '|', '.', '|'], ['C', '|', '.', '|', '.', '|', '.', '|']]

    win_x_row_b = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', '.', '|'],
             ['B', '|', 'X', '|', 'X', '|', 'X', '|'], ['C', '|', '.', '|', '.', '|', '.', '|']]

    win_x_row_c = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', '.', '|'],
             ['B', '|', '.', '|', '.', '|', '.', '|'], ['C', '|', 'X', '|', 'X', '|', 'X', '|']]

    win_x_column_1 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'X', '|', '.', '|', '.', '|'],
             ['B', '|', 'X', '|', '.', '|', '.', '|'], ['C', '|', 'X', '|', '.', '|', '.', '|']]

    win_x_column_2 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', 'X', '|', '.', '|'],
             ['B', '|', '.', '|', 'X', '|', '.', '|'], ['C', '|', '.', '|', 'X', '|', '.', '|']]

    win_x_column_3 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', 'X', '|'],
             ['B', '|', '.', '|', '.', '|', 'X', '|'], ['C', '|', '.', '|', '.', '|', 'X', '|']]

    win_x_diagonal_1 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'X', '|', '.', '|', '.', '|'],
             ['B', '|', '.', '|', 'X', '|', '.', '|'], ['C', '|', '.', '|', '.', '|', 'X', '|']]

    win_x_diagonal_2 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', 'X', '|'],
             ['B', '|', '.', '|', 'X', '|', '.', '|'], ['C', '|', 'X', '|', '.', '|', '.', '|']]

    win_x = win_x_row_a + win_x_row_b + win_x_row_c + win_x_column_1 + win_x_column_2 + win_x_column_3 +\
            win_x_diagonal_1 + win_x_diagonal_2

    return win_x



def winning_con_o():

    win_o_row_a = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'O', '|', 'O', '|', 'O', '|'],
                   ['B', '|', '.', '|', '.', '|', '.', '|'], ['C', '|', '.', '|', '.', '|', '.', '|']]

    win_o_row_b = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', '.', '|'],
                   ['B', '|', 'O', '|', 'O', '|', 'O', '|'], ['C', '|', '.', '|', '.', '|', '.', '|']]

    win_o_row_c = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', '.', '|'],
                   ['B', '|', '.', '|', '.', '|', '.', '|'], ['C', '|', 'O', '|', 'O', '|', 'O', '|']]

    win_o_column_1 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'O', '|', '.', '|', '.', '|'],
                      ['B', '|', 'O', '|', '.', '|', '.', '|'], ['C', '|', 'O', '|', '.', '|', '.', '|']]

    win_o_column_2 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', 'O', '|', '.', '|'],
                      ['B', '|', '.', '|', 'O', '|', '.', '|'], ['C', '|', '.', '|', 'O', '|', '.', '|']]

    win_o_column_3 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', 'O', '|'],
                      ['B', '|', '.', '|', '.', '|', 'O', '|'], ['C', '|', '.', '|', '.', '|', 'O', '|']]

    win_o_diagonal_1 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'O', '|', '.', '|', '.', '|'],
                        ['B', '|', '.', '|', 'O', '|', '.', '|'], ['C', '|', '.', '|', '.', '|', 'O', '|']]

    win_o_diagonal_2 = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', '.', '|', '.', '|', 'O', '|'],
                        ['B', '|', '.', '|', 'O', '|', '.', '|'], ['C', '|', 'O', '|', '.', '|', '.', '|']]

    win_o = win_o_row_a + win_o_row_b + win_o_row_c + win_o_column_1 + win_o_column_2 + win_o_column_3 + \
            win_o_diagonal_1 + win_o_diagonal_2

    return win_o



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

