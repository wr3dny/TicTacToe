# Tic Tac Toe game
from md_board import board
from md_play import play
from md_win import winning_condition


def main():
    name_1 = input('Player 1 name: ')
    name_2 = input('Player 2 name: ')

    concurrent_board = play(name_1, board)
    winning_condition(name_1, name_2, concurrent_board)






if __name__ == '__main__':
    main()




