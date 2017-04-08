def change(pennies,nickels,dimes,quarters):
    totalcents=pennies+nickels+dimes+quarters
    totaldollars=totalcents/100
    print('Total in cents:',totalcents,'cents')
    print('Total in dollars:$',totaldollars)
    return(totalcents,totaldollars)
print('How much pennies?')
pennies=int(input())
print('How much nickels?')
nickels=int(input())*5
print('How much dimes?')
dimes=int(input())*10
print('How much quarters?')
quarters=int(input())*25
change(pennies,nickels,dimes,quarters)
