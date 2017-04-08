def details():
            print('What is your name?')
            name=input()
            print('Who is your relation?')
            relation=input()
            print('What is your address?')
            address=input()
            print('What is your St City?')
            Stcity=input()
            print('What is your zip code?')
            while True:
                try:
                    zipcode=int(input())
                    break
                except ValueError:
                    print('Type a new number for your zipcode.')
            

            print('Name:',name) 
            print('Relation:',relation)
            print('Address:',address)
            print('St City:',Stcity)
            print('Zip:',zipcode)
            print('State:CA')
details()
