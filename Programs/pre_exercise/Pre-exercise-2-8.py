print('Enter your pounds.')
pounds=input()
print('Enter your age.')
age=int(input())
if age>=16 and age<=30 or age>=1 and age<=15:
    print('Your daily water need is 0.6 fl oz/lb.')
elif age>=31 and age<=54:
    print('Your daily water need is 0.54 fl oz/lb.')
elif age>=55 and age<=65:
    print('Your daily water need is 0.45 fl oz/lb.')
elif age>65:
    print('Your daily water need is 0.38 fl oz/lb.')

   
    
    
