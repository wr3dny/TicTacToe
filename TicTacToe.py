# Tic Tac Toe game
from md_board import board, board_display
from md_play import play
from md_win import winning_condition


def main():
    name_1 = input('Player 1 name: ')
    name_2 = input('Player 2 name: ')
    while not winning_condition(name_1, name_2, board):
        symbol = 'X'
        board_new = play(name_1, symbol, board)
        board_display(name_1, name_2, board_new)
        symbol = 'O'
        board_new = play(name_2, symbol, board)
        board_display(name_1, name_2, board_new)


if __name__ == '__main__':
    main()




