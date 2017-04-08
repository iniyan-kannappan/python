import random
print('Do you want to play the coin toss game or the number guessing game.')
print("If you want to play the 'coin toss game' press 1.")
print("If you want to play the 'number guessing game' press 2.")
game=input()
randompick=0
if game=='1':
    coinpicks=[]
    userpicks=[]
    count=0
    print('You have chosen the coin toss game.')
    
    for i in range(1,11,1):
        coin=['Heads','Tails']
        choice=random.choice(coin)
        coinpicks.append(choice)
        
        user=input('Choose a coin side:')
        userpicks.append(user)

        if user==choice:
            print('You are correct.')
            count=count+1
        else:
            print('You are wrong.')
            
    print('Total score:',count,'/10.')
    print('Computer Picks:',coinpicks)
    print('User Picks:',userpicks)
        
elif game=='2':
    print('You have chosen the number guesing game.')
    priorpick=[]
    randompick=random.randint(1,20)
    
    while True:
        guess=int(input('Guess the number:'))
        
        if randompick==guess:
             print('You are correct.')
             print('Your Prior guesses:',priorpick)
             break
        else:
             print('You are wrong.')
             priorpick.append(guess)
    






