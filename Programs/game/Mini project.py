import random
wordlist=['Pokemon','Digimon','Yo-kai','Dinsaur King','Wakfu']
randomword=random.choice(wordlist)
emptylist=len(randomword)*['_']
print(emptylist)
print('Enter the letter.')
word2=""
while True:
    
    letter=input()
    if letter in randomword:
        print('You are correct.')
        for position in range(0,len(randomword)):
            if randomword[position]==letter:
                emptylist [position]=letter
                print(emptylist)
                print(position)
        if len(randomword)==len(emptylist) and list(randomword)==emptylist:
            break
        
        #add letter to emptylist at correct position/index/location 
    else:     
        print('Try the next letter.')

