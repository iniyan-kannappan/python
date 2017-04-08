import turtle
import random
turtle.speed(0000000000000000000000000000)
turtle.bgcolor('blue')

x=1

for i in range(500):

    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    turtle.colormode(255)
    turtle.pencolor(r,g,b)
    turtle.fd(50+x)
    turtle.rt(90.911)
    x=x+1

turtle.exitonclick()

        
