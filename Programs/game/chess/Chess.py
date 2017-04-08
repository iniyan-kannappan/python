def board():
    global chess                                            
    chess=[['BR1','BK1','BB1','BQ1','BKI1','BB2','BK2','BR2'],
           ['BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8'],
           ['   ','   ','   ','   ','   ','   ','   ','   '],
           ['   ','   ','   ','   ','   ','   ','   ','   '],
           ['   ','   ','   ','   ','   ','   ','   ','   '],
           ['   ','   ','   ','   ','   ','   ','   ','   '],
           ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'],
           ['WR1','WK1','WB1','WQ1','WKI1','WB2','WK2','WR2']]
    print('  1   2   3   4   5   6   7   8')       
    rownumber=1
    for row in chess:
        print(rownumber,end=' ')
        for column in row: 
            print(column,end='|')
        print(rownumber)
        rownumber=rownumber+1
        print('-'*32)
    print('1   2   3   4   5   6   7   8')
board()
print()
def getindex(coin):
    for row in range(0,7,1):
        for column in range(0,8,1):
            #print(row,column)
            if chess[row][column]==coin:
                return(row,column)
print('Whites turn.Please enter the coin to move')
coin=input()
position=getindex(coin)
print(position)
print('Enter a move')
move=tuple(input())
