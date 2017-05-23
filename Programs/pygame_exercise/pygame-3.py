import random
import time
import pygame
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
pygame.init()
screen=pygame.display.set_mode((255,255))
color=(r,g,b)
color2=[r,g,b]
while True:
    for loop in range(5,135,10):    
        
        drawcircle=pygame.draw.circle(screen,color,(125,125),loop)
        print(loop)
        if drawcircle==255:
            color.choice(color2)
        pygame.display.update()
        time.sleep(1)
    for loop in range(125,0,-10):
        screen.fill((0,0,0))
        pygame.draw.circle(screen,color,(125,125),loop)
        print(loop)
        pygame.display.update()
        time.sleep(1)

    
