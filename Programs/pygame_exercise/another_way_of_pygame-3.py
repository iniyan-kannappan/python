import pygame
import time
import random
pygame.init()
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
inout='o'
screen=pygame.display.set_mode((400,400))
x=1
while x<=200:
    screen.fill((0,0,0))
    color=(r,g,b)
    pygame.draw.circle(screen,color,(200,200),x,1)
    
    
    time.sleep(.037)

    if x>199:
        inout='i'
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color=(r,g,b)
    elif x==10:
        inout='o'


    if inout=='i':
        x=x-1
        
    elif inout=='o':
        x=x+1
        
    print(x,inout)    
    pygame.display.update()
