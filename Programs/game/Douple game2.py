import random
print('Do you want to play the coin toss game or the number guessing game.')
print("If you want to play the 'coin toss game' press 1.")
print("If you want to play the 'number guessing game' press 2.")
game=input()
if game=='1':
    count=0
    coinpicks=[]
    userpicks=[]
    print('You have chosen the coin toss game.')
    for loop in range(1,11,1):
        print(loop)
        print('Do you want to be heads or tails.')
        user=input()
        coin=['Heads','Tails']
        choice=random.choice(coin)
        coinpicks.append(choice)
        userpicks.append(user)
        if choice==user:
            print('You are correct.')
            count=count+1
        else:
            print('You are wrong.')
    print(coinpicks)
    print(userpicks)
    print('Total score',count,'/10.')
elif game=='2':
    print('You have chosen the number guessing game.')
    
