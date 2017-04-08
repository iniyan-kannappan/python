import random
num=random.randint(20,30)
lis=[]
count=0
while True:
    print('Guess the number.')
    guess=int(input())
    count=count+1
    #guess2=str(guess)
    
    if num==guess:
        print('You are correct.')
        break
    else:
        lis.append(guess)
        print(lis)
        print('You are wrong.')
        
print('You did',str(count),'number of attempts.')
