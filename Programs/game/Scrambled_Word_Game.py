import random
while True:
    n1=['Orange','Mango','Grape','Jack Fruit','Banana']
    n2=random.choice(n1)
    n3=list(n2)
    random.shuffle(n3)
    print(n3)
    n4=input('Will you try another fruit.')
    if n4=='y':
        continue
    else:
        break 
