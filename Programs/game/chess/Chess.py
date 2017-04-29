import Pawn,Board
chessboard = [['BR1', 'BK1', 'BB1', 'BQ1', 'BKI1', 'BB2', 'BK2', 'BR2'],
              ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8'],
              ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
              ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
              ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
              ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
              ['WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7', 'WP8'],
              ['WR1', 'WK1', 'WB1', 'WQ1', 'WKI1', 'WB2', 'WK2', 'WR2']]


Board.drawboard(chessboard)
print()
def getindex(coin):
    for row in range(0,7,1):

        for column in range(0,8,1):
            if chessboard[row][column]==coin:
                return(row,column)
turn2='White'
def move(turn):
    global turn2
    print(turn+'s turn.Please enter the coin to move.')
    coin=input().upper()
    position=getindex(coin)
    print(position)
    i,j=getindex(coin)
    print('Enter a row.')
    row = int(input())
    print('Enter a column.')
    column = int(input())
    k=row
    l=column
    if (k==i-1 or k==i-2)and(l==j):
        chessboard[position[0]][position[1]]='  '
        chessboard[row][column] = coin
        Board.drawboard(chessboard)
        if turn2 == 'White':
            turn2 = 'Black'
        else:
            turn2 = 'White'
    else:
        print('Wrong move!')




while True:
    move(turn2)
    move(turn2)
#add useful comments to understand how the code works
#add a conditition in the move that any pawn can move only 1 or 2 steps on the same column any other chess piece can continue to move
#pawn could only move 2 steps in when in first row