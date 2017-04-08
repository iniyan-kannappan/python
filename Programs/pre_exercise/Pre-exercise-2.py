
print('Enter a 4 integer numbers:')
inputlist=[]
output=0
for loop in range(1,5,1):    
    numbers=int(input())
    inputlist.append(numbers)
    output=output+numbers

print('Your numbers:',inputlist)
print('Sum of 4 integer numbers:',output)
