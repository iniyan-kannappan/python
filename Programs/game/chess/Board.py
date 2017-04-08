def drawboard(chessboard):
    print('   1   2   3   4   5   6   7   8')
    rownumber=1
    for row in chessboard:
        print(rownumber,end=' ')
        for column in row:
            print(column,end='|')
        print(rownumber)
        rownumber=rownumber+1
        if rownumber==7:
            print('iniyan')
        print('-'*32)
    print('1   2   3   4   5   6   7   8')