import random
print('Do you want play the coin toss game or the  number guessing game.')
print("If you want to play 'Coin Toss Game', press 1.")
print("If you want to play 'Number Guessing Game', press 2.")
game=int(input())
if game==1:
    print('You have chosen the coin toss game.')
    count=0
    computerpicks=[]
    userpicks=[]
    for loop in range(1,11,1):
        coin=['Heads','Tails']
        choice=random.choice(coin)
        computerpicks.append(choice)
        
        userinput=input('Enter Heads or Tails:')
        userpicks.append(userinput)        
        
        if choice==userinput:
            print('You got it right.')
            count=count+1
        else:
            print('You got it wrong.')
            
    print('Total score:',count,'/10.')
    print('Computer picks:',computerpicks)
    print('User picks:',userpicks)
        
elif game==2:
    print('You have chosen the number guessing game.')
    priorguesses=[]
    randomnumber=random.randint(1,10)
    #print(randomnumber)
    
    while True:
        print('Try to guess the number:')
        number=int(input())

        if randomnumber==number:
            print('You are right.')
            print('Correct guess.You guessed:',number)
            print('Prior guesses:',priorguesses)
            break
        else:
            print('You are wrong.')
            priorguesses.append(number)    
        






        
        
    
