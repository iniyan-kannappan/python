import random
print('Do you want play the coin toss game or the  number guessing game.')
print("If you want to play 'Coin Toss Game', press 1.")
print("If you want to play 'Number Guessing Game', press 2.")
game=int(input())
coinpicks=[]
userpicks=[]
count=0
if game==1: 
    for loop in range(1,11,1):
        coin=['Heads','Tails']
        choice=random.choice(coin)
        #print(choice)

        print('Guess what the coin side is.')
        coin2=input()

        coinpicks.append(choice)
        userpicks.append(coin2)
        
        if choice==coin2:
            print('You got it correct.')
            count=count+1
        else:
            print('You got it wrong.')
            
    print('Coin picks:',coinpicks)
    print('User picks:',userpicks)
    print('Total score:',count,'/10.')
elif game==2:
    priorguesses=[]
    randomnumber=random.randint(1,10)
    #print(randomnumber)
    
    while True:        
        print('Guess what is the number:')
        guess=int(input())
        
        if randomnumber==guess:
            print('You got it correct.')
            print('Correct guess:',guess)            
            print('Prior guesses:',priorguesses,'.')
            break
        else:
            print('You are wrong.')
            priorguesses.append(guess)
            
        
