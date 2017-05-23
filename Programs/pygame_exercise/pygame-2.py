import random
import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
color=(0,255,0)
randomnumber=random.randint(0,255),random.randint(0,255)
def triangle(a,b,c):

    pygame.draw.line(screen,color,a,b)
    pygame.draw.line(screen,color,c,a)
    pygame.draw.line(screen,color,b,c)
    pygame.display.update()        
for loop in range(0,10,1):
    a=random.randint(0,400),random.randint(0,400)
    b=random.randint(0,400),random.randint(0,400)
    c=random.randint(0,400),random.randint(0,400) 
    triangle(a,b,c)
#homework:write a for loop to draw 10 random triangles
