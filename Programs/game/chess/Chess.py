import Pawn,Board
#below,that is a variable for the list which stores the chessboard
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
            #print(row,column)
            if chessboard[row][column]==coin:
                return(row,column)
def move():
    #this is White turn
    print('Whites turn.Please enter the coin to move.')
    coin=input()
    position=getindex(coin)
    print(position)
    print('Enter a row.')
    row=int(input())
    print('Enter a column.')
    column = int(input())
    chessboard[position[0]][position[1]]='   '
    chessboard[row][column]=coin
    Board.drawboard(chessboard)
move()
#the code below is the black turn
def move2():
    print('Blacks turn.Please enter the coin to move.')
    coin=input()
    position=getindex(coin)
    print(position)
    #this is input for the move's row
    print('Enter a row.')
    row=int(input())
    #this is input for the move's column
    print('Enter a column.')
    column = int(input())
    chessboard[row][column]=coin
    #this draws the board
    chessboard[position[0]][position[1]]='   '
    Board.drawboard(chessboard)
move2()
#clear the position from which the pawn was moved
#convert into move function and call it twice,1 for white turn and 1 for black turn DONE
#add comments describing the code DONE
#at least 6 comments DONE