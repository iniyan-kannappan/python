appendnumbers=[]
plusnum=0
print('Enter a 4 integer numbers.')
for loop in range(1,5,1):
    numbers=int(input())
    appendnumbers.append(numbers)
    plusnum=plusnum+numbers
    
print('Your input numbers:',appendnumbers)
print('Sum of all numbers:',plusnum)
