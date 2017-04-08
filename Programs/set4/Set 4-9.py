items={'Bike':'$135','Ripstik':'$35','Roller-skates':'$70','Skis':'$60','Perfume':'$20'}
print(items)
print('Which item do you want to purchase?')
purchase=input()
if purchase in items:
    print(items[purchase])
else:
    print('Check somewhere else.')
    
    
