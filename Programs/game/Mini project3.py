import random
wordlist=['Pokemon','Digimon','Yo-kai','Dinosaur King','Wakfu']
randomword=random.choice(wordlist)
emptylist=len(randomword)*['_']
print(emptylist)
print('Enter the letter.')
while True:
    letter=input()
    print("You are correct.")
    if letter in randomword:
        for position in range(0,len(randomword)):
            if randomword[position]==letter:
                emptylist[position]=letter
                print(emptylist)
    if len(randomword)==len(emptylist) and list(randomword)==emptylist:
        break 
else:
    print('Try the next letter.')
        
