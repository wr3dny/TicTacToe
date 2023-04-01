# empty board

board = [[' ', ' ', '1', ' ', '2', ' ', '3', ' '], ['A', '|', '.', '|', '.', '|', '.', '|'],
         ['B', '|', '.', '|', '.', '|', '.', '|'], ['C', '|', '.', '|', '.', '|', '.', '|']]


def board_display(name1, name2, board):
    cl = max(len(name1), len(name2))
    print(f'{name1 : ^{cl}} -  playing X')
    vs = 'vs'
    print(vs.center(cl))
    print(f'{name2 : ^{cl}} -  playing O')
    print(' ')
    for b in board:
        print(*b)

