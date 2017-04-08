fruits={'Apple':'Red','Watermelon':'Green','Mango':'Golden'}
for loop in fruits:
    print(loop,fruits[loop])
fruits['Grapes']='Purple'    
print(fruits)
print(fruits.pop('Apple'))
print(fruits)
