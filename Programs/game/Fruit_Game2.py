import random
fruits=['apple','peach','watermelen','orange','grape']
while True:
    fruitchoice=random.choice(fruits)
    print(fruitchoice)
    fruitshuffle=list(fruitchoice)
    random.shuffle(fruitshuffle)
    print(fruitshuffle)
    fruit=input('Can you unscrammble this fruit.')
    if fruitchoice==fruit:
        print('You are correct.')
    else:
        print('You are wrong.Try the next fruit.')


