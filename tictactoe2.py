import random
def printBoard(board):
    print(board['1 1'] + '|' + board['1 2'] + '|' + board['1 3'])
    print('-+-+-')
    print(board['2 1'] + '|' + board['2 2'] + '|' + board['2 3'])
    print('-+-+-')
    print(board['3 1'] + '|' + board['3 2'] + '|' + board['3 3'])

theBoard = {'1 1': ' ', '1 2': ' ', '1 3': ' ',
            '2 1': ' ', '2 2': ' ', '2 3': ' ',
            '3 1': ' ', '3 2': ' ', '3 3': ' '}
theBoard2 = {'1 1': ' ', '1 2': ' ', '1 3': ' ',
             '2 1': ' ', '2 2': ' ', '2 3': ' ',
             '3 1': ' ', '3 2': ' ', '3 3': ' '}
turn = 'X'
while theBoard2 != {}:
    if turn == 'X':
        print('Turn for computer.')
        c_move = random.choice(list(theBoard2.keys()))
        theBoard[c_move] = turn
        printBoard(theBoard)
        theBoard2.pop(c_move)
        turn = 'O'
        
    else:
        u_move = input('Turn for user. Move on which cell?: ')
        theBoard[u_move] = turn
        printBoard(theBoard)
        theBoard2.pop(u_move)
        turn = 'X'
        
    
    
    
    
