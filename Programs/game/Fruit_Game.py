from random import choice,shuffle
fruits=['apple','mango','peach','jack fruit','grape','orange','raspberry','strawberry','blackberry','pear','plum','guava','litche','apricot','banana','cherry','clementine','elderberry','fig','kiwi','melon','nectarine']
while True:
    n1=choice(fruits)
    n2=list(n1)
    shuffle(n2)
    print(n2)
    fruit=input('Can you unscrammble this fruit.')
    if fruit==n1:
        print('You got it correct.')
    else:
        
        print('You got it wrong.')
    print('Try the next fruit.')
