import random
import time
import pygame
while True:
    pygame.init()
    screen=pygame.display.set_mode((255,255))
    color=(0,255,0)
    pygame.draw.circle(screen,color,(125,125),125)
    pygame.display.update()
    time.sleep(1)
    
    pygame.init()
    screen2=pygame.display.set_mode((10,10))
    color2=(255,255,255)
    pygame.draw.circle(screen,color2,(5,5),5)
    pygame.display.update()
    time.sleep(1)
