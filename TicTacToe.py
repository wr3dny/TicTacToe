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
    print(f'{name1 : ^{cl}}')
    vs = 'vs'
    print(vs.center(cl))
    print(f'{name2 : ^{cl}}')
    print(' ')
    for l in board:
        print(*l)


def winning_con():


    win_x = [[' ', '|', '1', '|', '2', '|', '3', '|'], ['A', '|', 'X', '|', '.', '|', '.', '|'],
         ['B', '|', 'X', '|', '.', '|', '.', '|'], ['C', '|', 'X', '|', '.', '|', '.', '|']]
    pass


def play(n1, n2):
    used_spots = []
    print(f'{n1}, place "X" on the board.')
    row = input('Row: ')
    row = row.capitalize()
    column = int(input('Column: '))
    if row == 'A':
        row = 1
    elif row == 'B':
        row = 2
    elif row == 'C':
        row = 3
    while (row, column) in used_spots:
        row = input('Row: ')
        column = int(input('Column: '))

    used_spots.append((row, column))
    board[row][column+column] = 'X'

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
    while (row, column) in used_spots:
        print('Not possible. Already in use')
        row = input('Row: ')
        column = int(input('Column: '))

    used_spots.append((row, column))
    board[row][column+column] = 'O'

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

