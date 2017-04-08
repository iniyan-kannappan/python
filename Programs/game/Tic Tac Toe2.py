numbers={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
win=0
while True:
    
    print(numbers[1],    numbers[2],    numbers[3])
    print(numbers[4],    numbers[5],    numbers[6])
    print(numbers[7],    numbers[8],    numbers[9])

    
    print('Player 1:pick a number in 1 to 9:')
    pick=(int(input()))

    while numbers[pick]=='X' or numbers[pick]=='O':
        print('This number is already is occupied.')
        print('Please enter a new number.')
        pick=(int(input()))        
    numbers[pick]='X'
    if (numbers[1]=='X' and numbers[2]=='X' and numbers[3]=='X') or\
       (numbers[4]=='X' and numbers[5]=='X' and numbers[6]=='X')  or\
       (numbers[7]=='X' and numbers[8]=='X' and numbers[9]=='X') or\
       (numbers[1]=='X' and numbers[4]=='X' and numbers[7]=='X') or\
       (numbers[2]=='X' and numbers[5]=='X' and numbers[8]=='X') or\
       (numbers[3]=='X' and numbers[6]=='X' and numbers[9]=='X') or\
       (numbers[1]=='X' and numbers[5]=='X' and numbers[9]=='X') or\
       (numbers[3]=='X' and numbers[5]=='X' and numbers[7]=='X'):
           print('Player 1 wins!')
           win=1
           break
    if 1 not in numbers.values()and 2 not in numbers.values()and\
       3 not in numbers.values()and 4 not in numbers.values()and\
       5 not in numbers.values()and 6 not in numbers.values()and\
       7 not in numbers.values()and 8 not in numbers.values()and\
       9 not in numbers.values()and win!=1:
           print('The game ends in a tie.')
           break
    print(numbers[1],    numbers[2],    numbers[3])
    print(numbers[4],    numbers[5],    numbers[6])
    print(numbers[7],    numbers[8],    numbers[9])

    print('Player 2:pick a number in 1 to 9:')
    pick=(int(input()))
    while numbers[pick]=='X' or numbers[pick]=='O':
        print('This number is already is occupied.')
        print('Please enter a new number.')
        pick=(int(input()))        
    numbers[pick]='O'
    if (numbers[1]=='O' and numbers[2]=='O' and numbers[3]=='O') or\
       (numbers[4]=='O' and numbers[5]=='O' and numbers[6]=='O')  or\
       (numbers[7]=='O' and numbers[8]=='O' and numbers[9]=='O') or\
       (numbers[1]=='O' and numbers[4]=='O' and numbers[7]=='O') or\
       (numbers[2]=='O' and numbers[5]=='O' and numbers[8]=='O') or\
       (numbers[3]=='O' and numbers[6]=='O' and numbers[9]=='O') or\
       (numbers[1]=='O' and numbers[5]=='O' and numbers[9]=='O') or\
       (numbers[3]=='O' and numbers[5]=='O' and numbers[7]=='O'):
           print('Player 2 wins!')
           win=1
           break
    if 1 not in numbers.values()and 2 not in numbers.values()and\
       3 not in numbers.values()and 4 not in numbers.values()and\
       5 not in numbers.values()and 6 not in numbers.values()and\
       7 not in numbers.values()and 8 not in numbers.values()and\
       9 not in numbers.values()and win!=1:
           print('The game ends in a tie.')
           break
       
