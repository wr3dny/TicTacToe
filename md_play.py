from md_board import board, board_display


def play(player, symbol, bd):
    print(f'{player}, place {symbol} on the board.')
    flag_row = False
    flag_column = False

    while not flag_row:
        row = input('Row: ')
        row = row.capitalize()
        if row == 'A' or row == 'B' or row == 'C':
            flag_row = True
        else:
            print('Invalid input. Please try again.')

        match row:
            case 'A':
                row = 1
            case 'B':
                row = 2
            case 'C':
                row = 3

    while not flag_column:
        column = int(input('Column: '))
        if column == 1 or column == 2 or column == 3:
            flag_column = True
        else:
            print('Invalid input. Please try again.')

    bd[row][column + column] = symbol

    return bd


