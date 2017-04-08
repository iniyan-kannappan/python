#Spot and Correct the Syntax Errors
name=input('Please enter you name:')
print("Hi",name,". How are you ?")
gender = (input("Are you a boy or a girl?"))
if gender in ['Boy','boy','b','B']:
      print('Hello, Mr.',name)
elif gender in ['Girl','girl','g','G']:
      print("Hello, Miss.",name)
else:
      print("I couldn't understand what you typed in")

number = int(input('Type in any 3 digit number and I will show you something cool.'))
while number in range(100,999):
    number = int(input('Type in any 4 digit number'))
prime = 1
primelist = []
for i in range(2,number):
    for j in range(2,i):
        if i%j == 0:
            prime = 0
    if prime : 
        primelist.append(i)
print("The list of all prime numbers upto",number," is :")
print(primelist)

print('The next program to debug is a program which takes in a word and creates a dictionary with letters and the letter counts')
print("For example : brontosaurus")
dictionary = {}
dictionary = {'b':1,'r':1,'o':2,'s':2}
print('The number of time the letter \'s\' shows up in the word \'brontosaurus\' is ', dictionary['s'])
word = input('Now type in a word of any length')
for letter in word:
    for letter in dictionary:
        dictionary [letter]=dictionary[letter]+1
    else:
        dictionary['z']=3


print(dictionary)

print( "Aaaaand Now for the grand finale, Debug the code below to see something really cool !")

import turtle
import random

turtle.speed(0)
turtle.bgcolor('green')

x = 1
for i in range(400):

    r = random.randint(0,255) #makes variables r,g,b whose value is an integer,
    g = random.randint(0,255) # which is between 0 and 255. It is random, and
    b = random.randint(0,255) # changes every time the loop runs

    turtle.colormode(255) # this is something that is irrelevant at this point
    turtle.pencolor(r,g,b)# obtained by the variables r, g, b changing each time
    turtle.fd(50 + x)
    turtle.rt(90.911)
    x = x+1 

turtle.intonclick() 

print("Awesome you have solved the Debug Challenge. You are now a level 2 debugger !")

