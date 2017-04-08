import random
print('Do you want play the coin toss game or the  number guessing game.')
print("If you want to play 'Coin Toss Game', press 1.")
print("If you want to play 'Number Guessing Game', press 2.")
game=input()
if game=='1':
    count=0
    coinpick=[]
    userpick=[]
    print('You have chosen the coin toss game.')
    for loop in range(1,11,1):
        coin=['Heads','Tails']
        choice=random.choice(coin)
        coinpick.append(choice)
        print('Guess heads or tails.')
        guess=input()
        userpick.append(guess)
        if choice==guess:
            print('You got it correct.')
            count=count+1
        else:
            print('You got it wrong.')
    print('Total score:',count,'/10.')
    print('Coin picks:',coinpick)
    print('User picks:',userpick)
elif game=='2':
    guesslist=[]
    randomnumber=random.randint(1,10)
    while True:
        print('You have chosen the number guessing game.')
        guess=int(input('Guess a number.'))
        if randomnumber==guess:
            print('You are correct.')
            print('Your prior guesses:',guesslist)
            break
        else:
            print('You are wrong.')
            guesslist.append(guess)
            break
                    
