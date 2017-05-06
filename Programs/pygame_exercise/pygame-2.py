import pygame
def triangle():
    pygame.init()
    screen=pygame.display.set_mode((400,400))
    color=(0,255,0)
    pygame.draw.line(screen,color,(10,20),(40,20))
    pygame.draw.line(screen,color,(10,20),(20,50))
    pygame.draw.line(screen,color,(40,20),(20,50))
    pygame.display.update()

triangle()
