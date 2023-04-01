# Tic Tac Toe game
from md_board import board, board_display
from md_win import winning_condition


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



def main():
    used_spots = []

    name_1 = input('Player 1 name: ')
    name_2 = input('Player 2 name: ')
    empty_board = board_display(name_1, name_2)

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

