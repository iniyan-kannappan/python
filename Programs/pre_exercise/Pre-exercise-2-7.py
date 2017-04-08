print('Enter the weight of your luggage in lbs:')
weight=int(input())

if weight<=50:
    print('You are free.')
elif weight>50 and weight<=60:
    print('For each pound above 50 lbs,$5 will be charged.')    
elif weight>60 and weight<=70:         
    print('For each pound above 60 lbs,$10 will be charged.')    
elif weight>70 and weight<=75:         
    print('A standered rate of $200 must be charged.')
elif weight>75:
    print('You are not allowed because your luggages weight is higher than 75 lbs.')
