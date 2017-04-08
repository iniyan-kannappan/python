print('What is your name.')
name=input()
name=list(name)
print('Enter the letter.')
position=input()
name[int(position)]='X'
print(name)
