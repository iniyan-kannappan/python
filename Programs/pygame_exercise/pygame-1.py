import pygame
import random
width=random.randint(0,400)
height=random.randint(0,400)
pygame.init()
screen=pygame.display.set_mode((400,400))
color=(0,0,255)
pygame.draw.rect(screen,color,(200,200,width,height))
pygame.display.update()
