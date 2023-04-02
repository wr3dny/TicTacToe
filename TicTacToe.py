# Tic Tac Toe game
from md_board import board, board_display
from md_play import play
from md_win import winning_condition



def main():
    name_1 = input('Player 1 name: ')
    name_2 = input('Player 2 name: ')
    board_display(name_1, name_2, board)
    print()

    winner = 'no winner'

    while winner == 'no winner':

        symbol = 'X'
        board_new = play(name_1, symbol, board)
        board_display(name_1, name_2, board_new)
        winner = winning_condition(symbol, board_new)
        if winner == 'won':
            print(f'{name_1} won!')
            break

        symbol = 'O'
        board_new = play(name_2, symbol, board)
        board_display(name_1, name_2, board_new)
        winner = winning_condition(symbol, board_new)
        if winner == 'won':
            print(f'{name_2} won!')
            break






if __name__ == '__main__':
    main()
