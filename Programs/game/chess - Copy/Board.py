def drawboard(chessboard):
    #the function draws the chess board
    print('   0   1   2   3   4   5   6   7')
    rownumber=0
    for row in chessboard:
        print(rownumber,end=' ')
        for column in row:
            print(column,end='|')
        print(rownumber)
        rownumber=rownumber+1
        print('-'*32)
    print('   0   1   2   3   4   5   6   7')