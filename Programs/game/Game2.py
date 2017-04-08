quiz={'Q1':'A1','Q2':'A2','Q3':'A3','Q4':'A4'}
print('Guess the answer:')
count=0
for loop in quiz:
    print(loop)
    userguess=input()
    if userguess==quiz[loop]:
        print('You got it right.')
        count=count+1
    else:
        print('You got it wrong.')
print('You got',count,'/4')
